from pydicom.tag import Tag
from pydicom.dataset import Dataset
from pydicom.dataelem import DataElement
import pydicom
from pydicom.sequence import Sequence
from pydicom.multival import MultiValue
import pydicom.datadict as Dictionary
import validate_vr
from pydicom.uid import UID
from numpy import *
from mesgtext_cc import *
from sopclc_h import *
import module_cc
from condn_h import *
import dicom_prechecks
import re
import verify
import enum





def fix_Trivials(ds: Dataset, log: list):
    verify.SelectAndRunCompositeIOD(ds, False, log, True, '')
    # verify.PrintLog(log)


def fix_VRForLongitudinalTemporalInformationModified(ds: Dataset,
                                                     log: list) -> bool:
    kw = "LongitudinalTemporalInformationModified"
    Error = "Invalid Value Representation SH (CS Required) " \
             "Element=<LongitudinalTemporalInformationModified> " \
             "Module=<SOPCommon> "
    msg = "{} Error: {} :->: {}"
    if kw in ds:
        tag = Dictionary.tag_for_keyword(kw)
        elem = ds[tag]
        if elem.VR == "SH":
            elem.VR = "CS"
            ds[kw] = elem
            msg1 = msg.format(ErrorType.VR, Error, "fixed by editing CS to SH" )
            log.append(msg1)

    else:
        return False
    return True


def fix_RemoveFOVDimensionsWhenZero(ds: Dataset, log: list) -> bool:
    fixed = False
    kw = "FieldOfViewDimensions"
    Error = "Value is zero for attribute <Field of View Dimension(s)"
    msg = "{} Error: {} :->: {}"
    if kw in ds:
        tag = Dictionary.tag_for_keyword(kw)
        elem = ds[tag]
        for i in elem.value:
            if i == 0:
                fixed = True
                break
        if fixed:
            del ds[kw]
            msg1 = msg.format(ErrorType.BadValue.value, Error, "fixed by removing the atribute")
            log.append(msg1)
    return fixed


def fix_RemoveRedundant_InversionTime(ds: Dataset, log: list) -> bool:
    fixed = False
    kw = "InversionTime"
    mod = 'MRImage'
    cond = Condition_MRIsInversionRecovery
    if kw not in ds:
        return fixed
    success = module_cc.verifyType2C(ds, mod, kw,
                                     False, log, '',
                                     cond,
                                     False,
                                     ds, ds,
                                     0, 0)


    if success == False:
        del ds[kw]
        fixed = True
    return fixed


def fix_RemoveRedundant_Laterality(ds: Dataset, log: list) -> bool:
    fixed = False
    kw = "Laterality"
    mod = 'GeneralSeries'
    cond = Condition_LateralityRequired
    if kw not in ds:
        return fixed
    success = module_cc.verifyType2C(ds, mod, kw,
                                     False, [], '',
                                     cond,
                                     False,
                                     ds, ds,
                                     0, 0)

    if success == False:
        del ds[kw]
        fixed = True
    return fixed


def subfix_RemoveEmptyCodes(parent_ds: Dataset, log:list) -> bool:
    fixed = False
    elems_to_be_removed = []
    for key, elem in parent_ds.items():
        if type(elem) == pydicom.dataelem.RawDataElement:
            elem = pydicom.dataelem.DataElement_from_raw(elem)
        items_to_be_removed = []
        if type(elem.value) == Sequence:
            for (item, idx) in zip(elem.value, range(0, len(elem.value))):
                fixed = fixed or subfix_RemoveEmptyCodes(item, log)
                if "CodeMeaning" in item:
                    all_is_empty = True
                    for sub_k, sub_v in item.items():
                        if type(sub_v) == pydicom.dataelem.RawDataElement:
                            sub_v = pydicom.dataelem.DataElement_from_raw(sub_v)
                        if not sub_v.is_empty:
                            all_is_empty = False
                            break

                    if all_is_empty:
                        fixed = True
                        items_to_be_removed.append(item)
            for i in items_to_be_removed:
                elem.value.remove(i)
                msg = ":->: fixed by removing an empty item from seq <{}>".\
                    format(elem.keyword)
                log.append(msg)

                fixed = True
            if len(items_to_be_removed) > 0 and len(elem.value) == 0:
                elems_to_be_removed.append(elem)
                msg = ":->: fixed by removing empty seq <{}>". \
                    format(elem.keyword)
                log.append(msg)
                fixed = True
    for i in elems_to_be_removed:
        del parent_ds[i.tag]

    return fixed


def fix_RemoveEmptyCodes(ds: Dataset, log: list) -> bool:
    fixed = False
    items = ds.items()
    fixed = fixed or subfix_RemoveEmptyCodes(ds, log)
    return fixed


def ReplaceRegex(regexp_find, replace, text, extend=[0, 0], group=0):
    found_iters = re.finditer(regexp_find, text)
    founds = list(found_iters)
    ii = []
    return_text = ''
    if len(founds) != 0:
        yy = []
        before_match = []
        after_match = []
        xx = []

        for mmatch in founds:
            xx.append((mmatch.start(group) - extend[0],
                       mmatch.end(group) + extend[1]))
        s = 0
        for idx in range(0, len(xx)):
            if idx + 1 >= len(xx):
                e = len(xx)
            else:
                e = xx[idx + 1][0]
            return_text = return_text + text[s:xx[idx][0]] + replace + text[
                                                                       xx[idx][
                                                                           1]:e]
            s = e

    else:
        return_text = text

    return return_text


def subfix_FindAndReplaceAttribValue(
        find_regex: str, replace: str, ds: Dataset, ttag: tag, group=0,
        verbose=False):
    replaced_global = False
    changed_element_lists = []
    for key, elem in ds.items():
        i_count = 0
        if type(elem.value) == Sequence:
            for item in elem.value:
                replaced_local = subfix_FindAndReplaceAttribValue(
                    find_regex, replace, item, ttag, group, verbose)
                if replaced_local:
                    replaced_global = True
                i_count += 1
        elif type(elem.value) == Dataset:
            print("dataset {} from {}".format('', elem.keyword))
            replaced_local = subfix_FindAndReplaceAttribValue(
                find_regex, replace, elem.value, ttag, group, verbose)
            replaced_global = replaced_global or replaced_local
        else:
            if ttag is not None:
                if elem.tag != ttag:
                    continue
            if type(elem) == pydicom.dataelem.RawDataElement:
                elem = pydicom.dataelem.DataElement_from_raw(elem)
            if type(elem.value) == MultiValue:
                v = elem.value
            else:
                v = [elem.value]
            replaced_items = []
            for txt, idx in zip(v, range(0, len(v))):
                if type(txt) == str:
                    r = ReplaceRegex(find_regex, replace, txt)

                    if txt != r:
                        replaced_items.append((idx, r))
            if type(elem.value) == MultiValue:
                for idx, replaced_txt in replaced_items:
                    if verbose:
                        t = validate_vr.tag2str(elem.tag)
                        msg = '--->{}[{}] is {} which is replaced by {}'.format(
                            t, idx, elem.value[idx], replaced_txt)
                        print(msg)

                    elem.value[idx] = replaced_txt
                    replaced_global = True
            elif len(replaced_items) != 0:
                if verbose:
                    t = validate_vr.tag2str(elem.tag)
                    msg = '--->{} is {} which is replaced by {}'.format(
                        t, elem.value, replaced_items[0][1])
                    print(msg)
                elem.value = replaced_items[0][1]
                replaced_global = True
            if len(replaced_items) != 0:
                changed_element_lists.append(elem)
    for el in changed_element_lists:
        del ds[el.tag]
        ds[el.tag] = el

    return replaced_global


def fix_RemoveSNM3Codes(ds: Dataset, log: list) -> bool:
    wrong_designator = 'SNM3'
    replace_txt = '99SDM'
    fixed = False
    ttag = Dictionary.tag_for_keyword("CodingSchemeDesignator")
    fixed = fixed or subfix_FindAndReplaceAttribValue(
        wrong_designator, replace_txt, ds, ttag, 0, True)
    return fixed


def fix_PatientPositionAndPatientOrientationCodeSequencePresent(
        ds: Dataset, log:list) -> bool:
    fixed = False
    pp = 'PatientPosition'
    posq = 'PatientOrientationCodeSequence'
    if posq in ds:
        if pp in ds:
            fixed = True
            del ds[pp]
    return fixed


def LoopOverAllAtribsAndRemoveIfConditionIsTrue(ds: Dataset, cond, log:list, err = '') -> bool:
    fixed = False
    elements_to_be_removed = []


    for key, a in ds.items():
        if type(a) == pydicom.dataelem.RawDataElement:
            a = pydicom.dataelem.DataElement_from_raw(a)
        if type(a.value) == Sequence:
            for item in a.value:
                fixed = fixed or LoopOverAllAtribsAndRemoveIfConditionIsTrue(
                    item, cond, log, err)
        elif type(a.value) == Dataset:
            fixed = fixed or LoopOverAllAtribsAndRemoveIfConditionIsTrue(
                a.value, cond, log, err)
        else:
            if cond(a):
                msg = "{} :->: {}"
                ttaagg = validate_vr.tag2str(a.tag)
                attrib = "<{}> -> {}".format(a.keyword, ttaagg)
                tmperr = err.format(attrib)
                msg = msg.format(tmperr,
                           "fixed by removing the attribute")
                log.append(msg)
                fixed = True
                elements_to_be_removed.append(a)
    for a in elements_to_be_removed:
        del ds[a.tag]

    return fixed


# def subfix_RemoveEmptyAtrib(ds:Dataset, ttag:tag)->bool:
#     fixed = False
#     curretn_ds_has_element = False
#     for key , a in ds.items():
#         if type(a) == pydicom.dataelem.RawDataElement:
#             a = pydicom.dataelem.DataElement_from_raw(a)
#         if type(a.value) == Sequence:
#             for item in a.value:
#                 fixed = fixed or subfix_RemoveEmptyAtrib(item, ttag)
#         elif type(a.value) == Dataset:
#             fixed = fixed or subfix_RemoveEmptyAtrib(a.value, ttag)
#         else:
#             if key == BaseTag(ttag):
#                 if a.is_empty:
#                     fixed = True
#                     curretn_ds_has_element = True
#     if curretn_ds_has_element:
#         del ds[ttag]
#
#     return fixed

# def fix_RemoveEmptyCodingSchemeVersion(ds: Dataset, log: list) -> bool:
#     err = "{} {}".format(ErrorType.Type1CRedundantEmpty)
#     return LoopOverAllAtribsAndRemoveIfConditionIsTrue(
#         ds, lambda attrib: attrib.tag == Dictionary.tag_for_keyword(
#             "CodingSchemeVersion") and attrib.is_empty)


def subfix_HasTrailingNulls(elem: DataElement) -> bool:
    fixed = False
    if elem.is_empty:
        return False
    if type(elem.value) == MultiValue:
        v = elem.value
    else:
        v = [elem.value]

    for i in range(0, len(v)):
        if type(v[i]) == str or type(v[i]) == bytes:
            l = len(v[i])
            idx = l - 1
            while idx >= 0:
                if v[i][idx] == 0:
                    idx -= 1
                else:
                    break
            idx = idx + 1
            if idx < l:
                v[i] = v[i][:idx]
                if len(v) % 2 == 1:
                    v[i] = v[i] + b'\x20'
                fixed = True
    if fixed:
        if type(elem.value) == MultiValue:
            elem.value = v
        else:
            elem.value = v[0]
    return fixed


def fix_TrailingNulls(ds: Dataset, log: list) -> bool:
    fixed = False
    elemsTobeCorrected = []
    for key, a in ds.items():
        if a.VR == 'UI' or a.VR == 'OB' or a.VR == 'OW' or a.VR == 'UN':
            continue
        if type(a) == pydicom.dataelem.RawDataElement:
            a = pydicom.dataelem.DataElement_from_raw(a)
        if type(a.value) == Sequence:
            for item in a.value:
                fixed = fixed or fix_TrailingNulls(item, log)
        elif type(a.value) == Dataset:
            fixed = fixed or fix_TrailingNulls(a.value, log)
        else:
            partial_fixed = subfix_HasTrailingNulls(a)


            if partial_fixed:
                msg = "{} Error: {} :->: {}"
                err = "<{}> {}".format(a.description(),
                                       validate_vr.tag2str(a.tag))
                msg1 = msg.format(ErrorType.BadValue.value,
                           err,
                           "fixed by removing the trailing null bytes")
                log.append(msg1)
                elemsTobeCorrected.append(a)
                fixed = True
    return fixed




def fix_RemoveAllRetired(ds: Dataset, log: list) -> bool:
    err = "{} is retired"
    return LoopOverAllAtribsAndRemoveIfConditionIsTrue(
        ds, lambda attrib: attrib.is_retired, log, err)


# def fix_RemoveFrameTimeWhenNotRequired(ds: Dataset, log:list) -> bool:
#     fixed = False
#     kw = 'FrameTime'
#     if kw in ds:
#         success = verifyType1C(ds,
#                                "PETImage", kw, False, [], None,
#                                Condition_PETSeriesType1Gated, False, ds, ds, 0,
#                                0)
#         if success == False:
#             del ds[kw]
def fix_RemoveUnwanterPixelAspctRation(ds:Dataset, log:list) -> bool:
    fixed = False
    kw = "PixelAspectRatio"
    is_one_to_one = False
    if kw in ds:
        elem = ds[kw]
        if type(elem) == MultiValue:
            if len(elem) == 2:
                is_one_to_one = (elem.value[0] == elem.value[2])
        if (Condition_UnwantedPixelAspectRatioWhenPixelSpacingPresent(ds, ds,
                                                                      ds) or
                Condition_UnwantedPixelAspectRatioWhenImagerPixelSpacingPresent(
                    ds, ds, ds) or
                Condition_UnwantedPixelAspectRatioWhenNominalScannedPixelSpacingPresent(
                    ds, ds, ds) or
                Condition_UnwantedPixelAspectRatioWhenSharedPixelMeasuresMacro(
                    ds, ds, ds) or
                Condition_UnwantedPixelAspectRatioWhenPerFramePixelMeasuresMacro(
                    ds, ds, ds) or
                Condition_UnwantedPixelAspectRatioWhenMPEG2MPHLTransferSyntax(
                    ds, ds, ds) or
                is_one_to_one):
            msg = "{} Error: {} :->: {}"
            msg = msg.format(ErrorType.BadValue.value,"<PixelAspectRatio> is 1:1 or redundant",
                       "fixed by removing the attribute")
            log.append(msg)
            del ds["PixelAspectRatio"]
            fixed = True
    return fixed


def subfix_AddEmptyAttrib(ds: Dataset, kw: str,log:list):
    fixed = False

    if kw not in ds:
        ttag = pydicom.datadict.tag_for_keyword(kw)
        if ttag is None:
            return False
        vr = pydicom.datadict.dictionary_VR(ttag)
        element = DataElement(ttag, vr, '')
        element.value = element.empty_value
        msg = "{} Error: {} :->: {}"
        err =  "<{}> attribute is missing ".format(kw)
        fx = "fixed by adding an empty attribute"
        msg = msg.format(ErrorType.Type2CAbsent.value, err, fx)
        log.append(msg)
        ds[kw] = element
        fixed = True
    return fixed


def fix_AddEmptyAccessionNumber(ds: Dataset, log:list) -> bool:
    return subfix_AddEmptyAttrib(ds, "AccessionNumber", log)


def fix_AddEmptyPatientOrientation(ds: Dataset, log:list) -> bool:
    fixed = False
    if Condition_PatientOrientationRequired(ds, ds, ds):
        fixed = subfix_AddEmptyAttrib(ds, "PatientOrientation", log)
    return fixed

def fix_AddEmptyCollimatorType(ds:Dataset, log:list):
    fixed = subfix_AddEmptyAttrib(ds, "CollimatorType", log)
    return fixed
def fix_AddEmptyCorrectedImage(ds:Dataset, log:list):
    fixed = subfix_AddEmptyAttrib(ds, "CorrectedImage", log)
    return fixed

def subfix_ConvertImageData16(ds:Dataset, log:list):
    aPixelData = dicom_prechecks.getElementFromDataset(ds, "PixelData")
    aBitsAllocated = dicom_prechecks.getElementFromDataset(ds, "BitsAllocated")
    aBitsStored = dicom_prechecks.getElementFromDataset(ds, "BitsStored")
    aHighBit = dicom_prechecks.getElementFromDataset(ds, "HighBit")
    data = []
    x = bytearray()
    if aBitsStored.value == 8:
        for d in aPixelData.value:
            data.append(uint16(d))
            x.append(uint16(d) & 0xff00)
            x.append(uint16(d) & 0xff)

        v = bytes(x)
        aPixelData.value = v
        aBitsAllocated.value = 16
        aBitsStored.value = 16
        aHighBit.value = 15

        # for i in range(0, len(data) ):
        #     a =  v[i*2]
        #     b = v[i*2+1]
        #     c = data[i]
        #     print( "{:x} {:x} {:x}".format(a, b, c))
def fix_BitsAllocated8ToBitsAllocated16(ds:Dataset, log:list):
    log_l = len(log)
    ErrorPattern = "Error - Unrecognized enumerated value <{}> for value 1 of " \
    "attribute {} BinaryValueDescription_BitsAre{}"

    convert = False
    for i in range(0, log_l):
        if log[i] == ErrorPattern.format(8, "Bits Allocated", 16) or\
                log[i] == ErrorPattern.format(8, "Bits Stored", 16) or\
                log[i] == ErrorPattern.format(7, "High Bit", 15) :
            x = ":->: fixed by conversion of PixelData to 16 bits"
            log[i] += x
            convert = True
    if convert:
        subfix_ConvertImageData16(ds, log)
def subfix_AddOrChangeAttrib(ds:Dataset, log:list, error_regexp:str,
                             fix_message:str,
                             keyword:str, value)->bool:
    fixed = False
    t = Dictionary.tag_for_keyword(keyword)
    if t is None:
        return False
    desc = Dictionary.dictionary_description(t)
    ErrorOccured = False
    log_l = len(log)
    for i in range(0, log_l):
        if re.match(error_regexp, log[i]) is not None:

            log[i] += " :->: " + fix_message
            ErrorOccured = True
    if ErrorOccured:
        if keyword in ds:
            ds[keyword].value = value # just modify
        else:
            vr = Dictionary.dictionary_VR(t)
            vm = 1
            elem = DataElement(t, vr, value)
            ds[keyword] = elem
            fixed = True
    return fixed
def subfix_AddMissingAttrib(ds:Dataset, log:list, keyword:str, value)->bool:
    fixed = False
    regexp =".*Missing attribute Type 1.*\<{}\>".format(keyword)
    fix_m= "fixed by adding attribute {} with value {}".format(keyword, value)
    return subfix_AddOrChangeAttrib(ds, log, regexp, fix_m, keyword, value)
def fix_AddMissingAtribute_RescaleSlope(ds:Dataset, log:list)-> bool:
    subfix_AddMissingAttrib(ds, log, "RescaleSlope", 1)

def fix_AddMissingAtribute_RescaleIntercept(ds:Dataset, log:list)->bool:
    subfix_AddMissingAttrib(ds, log, "RescaleIntercept", 0)

def fix_ChangeWindowWidthLessThanOne(ds:Dataset, log:list)->bool:
    regexp = '.*Not permitted to be \< 1 unless VOI LUT Function is ' \
             'LINEAR_EXACT or SIGMOID \- attribute \<WindowWidth\>.*'
    kw = "WindowWidth"
    value = 1
    fix_m = "fixed by modifying the {} to {}".format(kw, value)
    return subfix_AddOrChangeAttrib(ds, log, regexp, fix_m, kw, value)





