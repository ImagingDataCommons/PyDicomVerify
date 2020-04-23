import sopclc_h
from pydicom.tag import Tag
from pydicom.dataset import Dataset
from pydicom.dataelem import DataElement
import pydicom
from pydicom.sequence import Sequence
from pydicom.multival import MultiValue
import pydicom.datadict as Dictionary
import validate_vr
from pydicom.uid import UID
import numpy
from mesgtext_cc import *
from sopclc_h import *
import module_cc
from condn_h import *
import dicom_prechecks
import re
import verify
import enum
import mesgtext_cc
import pydicom.sr._snomed_dict as srt
import sctsrt



def fix_Trivials(ds: Dataset, log: list):
    verify.SelectAndRunCompositeIOD(ds, False, log, True, '')
    # verify.PrintLog(log)

def subfix_LookUpRegexInLog(regexp:str, log:list, appendIfNone = False,
DefaultErrorMsg = ''):
    index = []
    for i in range(0, len(log)):
        if re.match(regexp, log[i]) is not None:
            index.append(i)
    if len(index) == 0 and appendIfNone:
        index.append(-1)
        log.append(DefaultErrorMsg)
    return index


def fix_VRForLongitudinalTemporalInformationModified(ds: Dataset,
                                                     log: list) -> bool:
    fixed = False
    msg = mesgtext_cc.ErrorInfo()
    kw = "LongitudinalTemporalInformationModified"
    Error_regex = ".*Invalid Value Representation SH \(CS Required\)" \
             ".*{}.*".format(kw) 
    idx = subfix_LookUpRegexInLog(Error_regex, log)
    if len(idx) == 0:
        idx.append(-1)
        log.append("Error - bad VR for {}".format(kw))

    if kw in ds:
        tag = Dictionary.tag_for_keyword(kw)

        if ds[tag].VR == "SH":
            ds[tag].VR = "CS"
            for i in idx:
                msg.msg = log[i]
                msg.fix = "fixed by editing SH to CS"
                msg1 = msg.getWholeMessage()
                log[i] =  msg1
                
            fixed = True
    return fixed


def fix_RemoveFOVDimensionsWhenZero(ds: Dataset, log: list) -> bool:
    fixed = False
    kw = "FieldOfViewDimensions"
    Error_regex = ".*Value is zero for.*attribute.*Field.*View.*Dimension.*"
    msg = mesgtext_cc.ErrorInfo()
    
    idx = subfix_LookUpRegexInLog(Error_regex, log)
    if len(idx) == 0:
        idx.append(-1)
        log.append("Error - bad value (=0) for {}".format(kw))
    if kw in ds:
        tag = Dictionary.tag_for_keyword(kw)
        elem = ds[tag]
        for i in elem.value:
            if i == 0:
                fixed = True
                break
        if fixed:
            del ds[kw]
            for i in idx:
                msg.msg = log[i]
                msg.fix = "fixed by removing the attribute"
                msg1 = msg.getWholeMessage()
                log[i] =  msg1
    return fixed


# def fix_RemoveRedundant_InversionTime(ds: Dataset, log: list) -> bool:
#     fixed = False
#     kw = "InversionTime"
#     mod = 'MRImage'
#     cond = Condition_MRIsInversionRecovery
#     if kw not in ds:
#         return fixed
#     success = module_cc.verifyType2C(ds, mod, kw,
#                                      False, log, '',
#                                      cond,
#                                      False,
#                                      ds, ds,
#                                      0, 0)


#     if success == False:
#         del ds[kw]
#         fixed = True
#     return fixed


# def fix_RemoveRedundant_Laterality(ds: Dataset, log: list) -> bool:
#     fixed = False
#     kw = "Laterality"
#     mod = 'GeneralSeries'
#     cond = Condition_LateralityRequired
#     if kw not in ds:
#         return fixed
#     success = module_cc.verifyType2C(ds, mod, kw,
#                                      False, [], '',
#                                      cond,
#                                      False,
#                                      ds, ds,
#                                      0, 0)

#     if success == False:
#         del ds[kw]
#         fixed = True
#     return fixed


def subfix_UpdateOrInsertCodeAttribute(seqelem:DataElement, index:int, kw:str,
    value:str)->str:
    text_fun = lambda ds, att: '{}: {}\t'.format(att,ds[att])

    out_msg = ''
    if kw in seqelem.value[index]:
        out_msg = " {} modified <{}> -> <{}>".format(
            kw, seqelem.value[index][kw].value, value
        )
        seqelem.value[index][kw].value=value
    else:
        out_msg = "{} = <{}> was added".format(kw, value)
        newtag = Dictionary.tag_for_keyword(kw)
        newvr = Dictionary.dictionary_VR(newtag)
        elem = DataElement(newtag, newvr, value)
        seqelem.value[index].add(elem)
    return out_msg
    


def subfix_UpdateSRTCodes(seqelem:DataElement, log:list)->bool:
    fixed = False
    msg = mesgtext_cc.ErrorInfo("General Fix - Upadate old snomed codes to SCT")
    items_to_be_deleted = []
    text_fun = lambda ds, att: '{}: {}\t'.format(att,ds[att])
    for i, item in enumerate(seqelem.value, 1):
        hasCodeValue = True if "CodeValue" in item else False
        emptyCodeValue = True if not hasCodeValue else item["CodeValue"].is_empty
        textCodeValue = '' if not hasCodeValue else text_fun(item,"CodeValue")
        hasCodeMeaning = True if "CodeMeaning" in item else False
        emptyCodeMeaning = True if not hasCodeMeaning else item["CodeMeaning"].is_empty
        textCodeMeaning = '' if not hasCodeMeaning else text_fun(item,"CodeMeaning")
        hasLongCodeValue = True if "LongCodeValue" in item else False
        emptyLongCodeValue = True if not hasLongCodeValue else item["LongCodeValue"].is_empty
        textLongCodeValue = '' if not hasLongCodeValue else text_fun(item,"LongCodeValue")
        hasURNCodeValue = True if "URNCodeValue" in item else False
        emptyURNCodeValue = True if not hasURNCodeValue else item["CodURNCodeValue"].is_empty
        textURNCodeValue = '' if not hasURNCodeValue else text_fun(item,"CodURNCodeValue")
        hasCodingSchemeDesignator = True if "CodingSchemeDesignator" in item else False
        emptyCodingSchemeDesignator = True if not hasCodingSchemeDesignator else item["CodingSchemeDesignator"].is_empty
        textCodingSchemeDesignator = '' if not hasCodingSchemeDesignator else text_fun(item,"CodingSchemeDesignator")
        hasCodingSchemeVersion = True if "CodingSchemeVersion" in item else False
        emptyCodingSchemeVersion = True if not hasCodingSchemeVersion else item["CodingSchemeVersion"].is_empty
        textCodingSchemeVersion = '' if not hasCodingSchemeVersion else text_fun(item,"CodingSchemeVersion")
        hasCodeValue = hasCodeValue or hasLongCodeValue or hasURNCodeValue
        emptyCodeValue = not (not emptyCodeValue or not emptyLongCodeValue or not emptyURNCodeValue)
        textCodeValue = (textCodeValue + textLongCodeValue + textURNCodeValue)
        bit_code = numpy.uint8(0)
        if emptyCodeValue:
            bit_code = bit_code | 0x1
        if emptyCodeMeaning:
            bit_code = bit_code | 0x10
        if emptyCodingSchemeDesignator:
            bit_code = bit_code | 0x100
        state_text = subfix_CodeSeqItem2txt(seqelem, i-1)
        isSRT = False
        if hasCodingSchemeDesignator:
            v = item["CodingSchemeDesignator"].value
            if v == "SNM3" or v == "99SDM" or v == "SRT":
                isSRT = True
        else:
            if hasCodeValue:
                v = item["CodeValue"].value
                if re.match("[A-Z][A-Z0-9]{0,2}-[0-9A-Z]{4,5}",v) is not None:                
                    isSRT = True
        if not isSRT or not hasCodeValue:
            return False
        value = item["CodeValue"].value
        first_dict = srt.mapping['SRT']
        second_dict = sctsrt.replaced_entries
        replacing_value = ''
        if value in first_dict:
            replacing_value = first_dict[value]
        elif value in second_dict:
            replacingvalue = second_dict[value]

        if len(replacing_value) == 0:
            return False
        replacing_meaning = ''
        if replacing_value in sctsrt.sct_meaning:
            replacing_meaning = sctsrt.sct_meaning[replacing_value]
        msg1 = "item {} of {}:\t".format(i,seqelem.keyword)
        msg1 += "({}-{})".format(i,1) + subfix_UpdateOrInsertCodeAttribute(
            seqelem, i-1, "CodeValue", replacing_value)
        msg1 += "({}-{})".format(i,2) + subfix_UpdateOrInsertCodeAttribute(
            seqelem, i-1, "CodeMeaning", replacing_meaning)
        msg1 += "({}-{})".format(i,3) + subfix_UpdateOrInsertCodeAttribute(
            seqelem, i-1, "CodingSchemeDesignator", 'SCT')
        msg.fix = msg1
        msg2 = msg.getWholeMessage()
        log.append(msg2)
        fixed = True
    return fixed

        
        

def subfix_checkandfixBasicCodeSeq(seqelem:DataElement, log:list)->bool:
    fixed = False
    msg = mesgtext_cc.ErrorInfo("General Fix - Remove empty code seq ")

    items_to_be_deleted = []
    text_fun = lambda ds, att: '{}: <{}>\t'.format(att,ds[att].value)
    subfix_UpdateSRTCodes(seqelem, log)
    for i, item in enumerate(seqelem.value, 1):
        hasCodeValue = True if "CodeValue" in item else False
        emptyCodeValue = True if not hasCodeValue else item["CodeValue"].is_empty
        textCodeValue = '' if not hasCodeValue else text_fun(item,"CodeValue")
        hasCodeMeaning = True if "CodeMeaning" in item else False
        emptyCodeMeaning = True if not hasCodeMeaning else item["CodeMeaning"].is_empty
        textCodeMeaning = '' if not hasCodeMeaning else text_fun(item,"CodeMeaning")
        hasLongCodeValue = True if "LongCodeValue" in item else False
        emptyLongCodeValue = True if not hasLongCodeValue else item["LongCodeValue"].is_empty
        textLongCodeValue = '' if not hasLongCodeValue else text_fun(item,"LongCodeValue")
        hasURNCodeValue = True if "URNCodeValue" in item else False
        emptyURNCodeValue = True if not hasURNCodeValue else item["CodURNCodeValue"].is_empty
        textURNCodeValue = '' if not hasURNCodeValue else text_fun(item,"CodURNCodeValue")
        hasCodingSchemeDesignator = True if "CodingSchemeDesignator" in item else False
        emptyCodingSchemeDesignator = True if not hasCodingSchemeDesignator else item["CodingSchemeDesignator"].is_empty
        textCodingSchemeDesignator = '' if not hasCodingSchemeDesignator else text_fun(item,"CodingSchemeDesignator")
        hasCodingSchemeVersion = True if "CodingSchemeVersion" in item else False
        emptyCodingSchemeVersion = True if not hasCodingSchemeVersion else item["CodingSchemeVersion"].is_empty
        textCodingSchemeVersion = '' if not hasCodingSchemeVersion else text_fun(item,"CodingSchemeVersion")
        hasCodeValue = hasCodeValue or hasLongCodeValue or hasURNCodeValue
        emptyCodeValue = not (not emptyCodeValue or not emptyLongCodeValue or not emptyURNCodeValue)
        textCodeValue = (textCodeValue + textLongCodeValue + textURNCodeValue)
        bit_code = numpy.uint8(0)
        if emptyCodeValue:
            bit_code = bit_code | 0x1
        if emptyCodeMeaning:
            bit_code = bit_code | 0x10
        if emptyCodingSchemeDesignator:
            bit_code = bit_code | 0x100
        state_text = subfix_CodeSeqItem2txt(seqelem, i-1)
        state_text = ". Item current value is: " + state_text if state_text !='' else ''
        if hasCodingSchemeVersion and emptyCodingSchemeVersion:
            del item["CodingSchemeVersion"]
            msg.fix = "Empty CodingSchemeVersion in item {} of {} was deleted".format(
                    i, seqelem.name
                )+ state_text
            del_msg = msg.getWholeMessage()
            log.append(del_msg)
        if bit_code == 0x111 or bit_code == 0x110 or bit_code == 0x011 or \
            bit_code == 0x101 or bit_code == 0x001 or bit_code == 0x010:
            items_to_be_deleted.append(item)
            msg.fix = "Item {} of {} was deleted".format(
                    i, seqelem.keyword
                )
            del_msg = msg.getWholeMessage()
            log.append(del_msg)
            fixed = True
        if bit_code == 0x100:
            if hasCodingSchemeDesignator:
                item["CodingSchemeDesignator"] = '99LOCAL'
                msg.fix = "The value for CodingSchemeDesignator in "\
                        "item {} of {} was modified to 99LOCAL".format(
                        i, seqelem.keyword
                    ) + state_text
                del_msg = msg.getWholeMessage()
                log.append(del_msg)
            else:
                kw = "CodingSchemeDesignator"
                new_tag = Dictionary.tag_for_keyword(kw)
                new_vr = Dictionary.dictionary_VR(new_tag)
                new_elem = DataElement(new_tag, new_vr, "99LOCAL")
                item[kw] = new_elem
                msg.fix = "An element of CodingSchemeDesignator with value "\
                        "<99LOCAL> in item {} of {} was added".format(
                        i, seqelem.keyword
                    )+ state_text
                del_msg = msg.getWholeMessage()
                log.append(del_msg)
            fixed = True
    
    for el in items_to_be_deleted:
        seqelem.value.remove(el)
        

def generalfix_RemoveEmptyCodes(parent_ds: Dataset, log:list) -> bool:
    fixed = False
    elems_to_be_removed = []
    for key, elem in parent_ds.items():
        if type(elem) == pydicom.dataelem.RawDataElement:
            elem = pydicom.dataelem.DataElement_from_raw(elem)
        items_to_be_removed = []
        if type(elem.value) == Sequence:
            if elem.keyword.endswith("CodeSequence"):
                fixed = fixed or subfix_checkandfixBasicCodeSeq(elem, log)
            else:
                for (item, idx) in zip(elem.value, range(0, len(elem.value))):
                    fixed = fixed or generalfix_RemoveEmptyCodes(item, log)
        elif type(elem.value) == Dataset:
            fixed = fixed or generalfix_RemoveEmptyCodes(elem.value, log)
             


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

def subfix_CodeSeqItem2txt(seq_elem:DataElement, index:int)->str:
    code_kws = ['CodeValue', "CodeMeaning" , "CodingSchemeDesignator",
    "LongCodeValue", "URNCodeValue", "CodingSchemeVersion"]
    code_state = ''
    pattern = "{}: {}"
    counter = 1
    for kw in code_kws:
        if index < len(seq_elem.value):
            if kw in seq_elem.value[index]:
                x = pattern.format(kw, seq_elem.value[index][kw].value)
                code_state += '({}.{}){}'.format(index+1,counter,x)
                counter += 1
    code_state = 'Empty' if code_state == '' else code_state
    code_state = 'Item {} of {}:'.format(index+1, seq_elem.keyword)+code_state
    return code_state

    

def fix_PatientPositionAndPatientOrientationCodeSequencePresent(
        ds: Dataset, log:list) -> bool:
    code_kws = ['CodeValue', "CodeMeaning" , "CodingSchemeDesignator",
    "LongCodeValue", "URNCodeValue", "CodingSchemeVersion"]
    msg = mesgtext_cc.ErrorInfo()
    fixed = False
    pp = 'PatientPosition'
    posq = 'PatientOrientationCodeSequence'
    Error_regex = ".*May not be present when {} is present.*{}.*".format(
        posq, pp
    )
    if posq in ds:
        if pp in ds:
            seq_elem = ds[posq]
            idx = subfix_LookUpRegexInLog(Error_regex, log)
            txt = subfix_CodeSeqItem2txt(seq_elem, 0)
            if len(idx) == 0:
                idx.append(-1)
                log.append("{} = {} and {} both are present".format(
                pp, ds[pp].value, txt))
            for i in idx:
                msg.msg = log[i]
                if len(seq_elem.value)>0:
                    msg.fix = "kept {} but removed {}".format(txt, pp)
                    del ds[pp]
                else:
                    msg.fix = "kept {} but removed {}".format(pp, txt)
                    del ds[posq]
                log[i] = msg.getWholeMessage()
            fixed = True
             
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
                ttaagg = validate_vr.tag2str(a.tag)
                attrib = "<{}> -> {}".format(a.keyword, ttaagg)
                tmperr = err.format(attrib)
                msg = mesgtext_cc.ErrorInfo()
                msg.msg = tmperr
                msg.fix = "fixed by removing the attribute"
                
                log.append(msg.getWholeMessage())
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


def generalfix_TrailingNulls(ds: Dataset, log: list) -> bool:
    fixed = False
    elemsTobeCorrected = []
    for key, a in ds.items():
        if key.is_private:
            continue
        if a.VR == 'UI' or a.VR == 'OB' or a.VR == 'OW' or a.VR == 'UN':
            continue
        if type(a) == pydicom.dataelem.RawDataElement:
            a = pydicom.dataelem.DataElement_from_raw(a)
        if type(a.value) == Sequence:
            for item in a.value:
                fixed = fixed or generalfix_TrailingNulls(item, log)
        elif type(a.value) == Dataset:
            fixed = fixed or generalfix_TrailingNulls(a.value, log)
        else:
            partial_fixed = subfix_HasTrailingNulls(a)


            if partial_fixed:
                msg = mesgtext_cc.ErrorInfo(
                    "<{}> {}".format(a.description(),
                                       validate_vr.tag2str(a.tag))
                )
                err = "<{}> {}".format(a.description(),
                                       validate_vr.tag2str(a.tag))
                msg = mesgtext_cc.ErrorInfo("General Fix - Trailing null bytesz",
                    "fixed by removing the trailing null bytes for {}".format(
                        err
                    )) 
                
                log.append(msg.getWholeMessage())
                elemsTobeCorrected.append(a)
                fixed = True
    return fixed




def generalfix_RemoveAllRetired(ds: Dataset, log: list) -> bool:
    err = "General Fix - {} is retired"
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
def generalfix_RemoveUnwanterPixelAspctRatio(ds:Dataset, log:list) -> bool:
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
            msg = mesgtext_cc.ErrorInfo()
            msg.msg = '{} Error - {}'.format(ErrorType.BadValue.value,"<PixelAspectRatio> is 1:1 or redundant")
            msg.fix = "fixed by removing the attribute"
            log.append(msg.getWholeMessage())
            del ds["PixelAspectRatio"]
            fixed = True
    return fixed


# def subfix_AddEmptyAttrib(ds: Dataset, kw: str,log:list):
#     fixed = False

#     if kw not in ds:
#         ttag = pydicom.datadict.tag_for_keyword(kw)
#         if ttag is None:
#             return False
#         vr = pydicom.datadict.dictionary_VR(ttag)
#         element = DataElement(ttag, vr, '')
#         element.value = element.empty_value
#         msg = "{} Error: {} :->: {}"
#         err =  "<{}> attribute is missing ".format(kw)
#         fx = "fixed by adding an empty attribute"
#         msg = msg.format(ErrorType.Type2CAbsent.value, err, fx)
#         log.append(msg)
#         ds[kw] = element
#         fixed = True
#     return fixed


# def fix_AddEmptyAccessionNumber(ds: Dataset, log:list) -> bool:
#     return subfix_AddEmptyAttrib(ds, "AccessionNumber", log)


# def fix_AddEmptyPatientOrientation(ds: Dataset, log:list) -> bool:
#     fixed = False
#     if Condition_PatientOrientationRequired(ds, ds, ds):
#         fixed = subfix_AddEmptyAttrib(ds, "PatientOrientation", log)
#     return fixed

# def fix_AddEmptyCollimatorType(ds:Dataset, log:list):
#     fixed = subfix_AddEmptyAttrib(ds, "CollimatorType", log)
#     return fixed
# def fix_AddEmptyCorrectedImage(ds:Dataset, log:list):
#     fixed = subfix_AddEmptyAttrib(ds, "CorrectedImage", log)
#     return fixed

def subfix_ConvertImageData16(ds:Dataset, log:list):
    aPixelData = dicom_prechecks.getElementFromDataset(ds, "PixelData")
    aBitsAllocated = dicom_prechecks.getElementFromDataset(ds, "BitsAllocated")
    aBitsStored = dicom_prechecks.getElementFromDataset(ds, "BitsStored")
    aHighBit = dicom_prechecks.getElementFromDataset(ds, "HighBit")
    data = []
    x = bytearray()
    if aBitsStored.value == 8:
        for d in aPixelData.value:
            data.append(numpy.uint16(d))
            x.append(numpy.uint16(d) & 0xff00)
            x.append(numpy.uint16(d) & 0xff)

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
            x = "fixed by conversion of PixelData to 16 bits"
            msg = mesgtext_cc.ErrorInfo(log[i], x)
            log[i] += msg.getWholeMessage()
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
            msg = mesgtext_cc.ErrorInfo(log[i], fix_message)
            log[i] = msg.getWholeMessage()
            ErrorOccured = True
    if ErrorOccured:
        if keyword in ds:
            ds[keyword].value = value # just modify
            fixed = True
        else:
            vr = Dictionary.dictionary_VR(t)
            vm = 1
            elem = DataElement(t, vr, value)
            ds[keyword] = elem
            fixed = True
    return fixed
def subfix_AddMissingAttrib(ds:Dataset, log:list, keyword:str, value)->bool:
    fixed = False
    regexp =".*Missing attribute Type.*\<{}\>".format(keyword)
    fix_m= "fixed by adding attribute {} with value {}".format(keyword, value)
    return subfix_AddOrChangeAttrib(ds, log, regexp, fix_m, keyword, value)
def fix_AddMissingAtribute_RescaleSlope(ds:Dataset, log:list)-> bool:
    subfix_AddMissingAttrib(ds, log, "RescaleSlope", 1)

def fix_AddMissingAtribute_RescaleIntercept(ds:Dataset, log:list)->bool:
    subfix_AddMissingAttrib(ds, log, "RescaleIntercept", 0)

def fix_ChangeWindowWidthLessThanOne(ds:Dataset, log:list)->bool:
    regexp = '.*Not permitted to be \< 1 unless VOI LUT Function is ' \
             'LINEAR_EXACT or SIGMOID \- attribute \<WindowWidth\>.*'
    kw = "VOILUTFunction"
    value = "LINEAR_EXACT"
    fix_m = "fixed by modifying the {} to {}".format(kw, value)
    return subfix_AddOrChangeAttrib(ds, log, regexp, fix_m, kw, value)

def fix_ChangePhotometric_Interpretation(ds:Dataset, log:list)->bool:
    fixed = False
    if (ds.SOPClassUID == sopclc_h.PETImageStorageSOPClassUID):
        kw = "PhotometricInterpretation"
        if kw in ds:
            attrib = ds[kw]
            regexp = '.*Unrecognized enumerated value \<{}\> '\
                'for value 1 of attribute {}.*'.format(
                attrib.value, attrib.name
            )
            value = 'MONOCHROME2'
            fix_m = "fixed by modifying the {} to {}".format(kw, value)
            fixed = subfix_AddOrChangeAttrib(ds, log, regexp, fix_m, kw, value)
    return fixed

def subfix_ReplaceSlashWithBackslash(attrib:DataElement, log:list)->bool:
    fixed = False

    msg = mesgtext_cc.ErrorInfo(
        'General Fix -', '')
    fix = 'fixed attribute <{}> ({}) value by changing slash to backslash {} -> {}'

    if type(attrib.value) == MultiValue:
        tmp = attrib.value
    else:
        tmp = [attrib.value]
    for idx in range(0,len(tmp)):
        old_val = tmp[idx]
        if type(tmp[idx]) == str:
            tmp[idx] = tmp[idx].replace('/','\\')
        elif type(tmp[idx]) == bytes:
            x = bytearray()
            for elem in tmp[idx]:
                if elem == ord('/'):
                    x.append(ord('\\'))
                else:
                    x.append(elem) 
            tmp[idx] = bytes(x)
        if old_val != tmp[idx]:
            msg.fix = fix.format(attrib.name, idx+1, old_val, tmp[idx])
            log.append(msg.getWholeMessage())
            fixed = True

    if type(attrib.value) != MultiValue:
        attrib.value = tmp[0]
            
    return fixed
def generalfix_ReplaceSlashWithBackslash4CS(ds:Dataset, log:list)-> bool:
    fixed = False
    for ky,  v in ds.items():
        if type(v.value) == Sequence:
            for item in v.value:
                generalfix_ReplaceSlashWithBackslash4CS(item,log)
        elif type(v.value) == Dataset:
            generalfix_ReplaceSlashWithBackslash4CS(v.value,log)
        else:
            if v.VR == 'CS':
                fixed = subfix_ReplaceSlashWithBackslash(ds[ky], log)
    return fixed