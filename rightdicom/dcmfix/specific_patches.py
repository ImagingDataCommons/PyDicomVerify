import pydicom.datadict as Dictionary
from pydicom.sequence import Sequence as DataElementSequence
import rightdicom.dcmvfy.mesgtext_cc as mesgtext_cc
import rightdicom.dcmvfy.sopclc_h as sopclc_h
from rightdicom.dcmvfy.verify import verify_dicom_dataset
from rightdicom.dcmvfy.dicom_prechecks import get_not_used_list
import rightdicom.dcmvfy.mesgtext_cc as mesgtext_cc
from rightdicom.dcmvfy.validate_vr import tag2str
from pydicom.dataset import(
    # CLASSES
    Dataset,
    # DataElement,
)
from rightdicom.dcmvfy.data_elementx import DataElementX
from rightdicom.dcmfix.fix_tools import (
    # FUNCTIONS
    subfix_AddMissingAttrib,
    subfix_AddOrChangeAttrib,
    subfix_CodeSeqItem2txt,
    subfix_LookUpRegexInLog,
    subfix_RemoveAttrib,
    get_full_attrib_list,
    put_attribute_in_path,
    get_all_kw_paths,
)
from rightdicom.dcmvfy.mesgtext_cc import (
    # CLASSES
    ErrorInfo,
)
from rightdicom.dcmvfy.sopclc_h import (
    # VARIABLES
    PETImageStorageSOPClassUID,
)

def fix_Trivials(ds: Dataset, log: list):
    log.extend(verify_dicom_dataset(ds, False, '', True))
    return True
    # fixed = False
    # exception_kywords = [
    #     #Code Sequence Macro Attributes
    #     #BASIC CODED ENTRY ATTRIBUTES
    #     'CodeValue',
    #     'CodeMeaning',
    #     'CodingSchemeDesignator',
    #     'URNCodeValue',
    #     'LongCodeValue',
    #     'CodingSchemeVersion',
    #     # ENHANCED ENCODING MODE
    #     'ContextIdentifier',
    #     'ContextUID',
    #     'MappingResource',
    #     'MappingResourceUID',
    #     'MappingResourceName',
    #     'ContextGroupVersion',
    #     'ContextGroupExtensionFlag',
    #     'ContextGroupLocalVersion',
    #     'ContextGroupExtensionCreatorUID',
    #     #SOP Instance Reference Macro Attributes
    #     'ReferencedSOPClassUID',
    #     'ReferencedSOPInstanceUID',
    # ]
    # not_used_attribs = []
    # not_recognized_attribs = []
    # wrn_msg = 'Warning - Attribute is not present in standard DICOM IOD - {}'
    # get_not_used_list(ds, not_used_attribs, not_recognized_attribs)
    # standard_ds = get_full_attrib_list(ds)
    # for kw, tg, parent in not_used_attribs:
    #     msg = mesgtext_cc.ErrorInfo()
    #     msg.msg = wrn_msg.format(tag2str(tg))
    #     if kw not in standard_ds:
    #         del parent[tg]
    #         msg.fix = "fixed by removing the attribute"
    #     else:
    #         std__ = standard_ds[kw]
    #         if len(std__) > 1:
    #             msg.fix = "didn't fix because there are more than on "\
    #                 "candidate for displacement of keyword <{}>: ".format(kw)
    #             for i, el in enumerate(std__, 1):
    #                 txt = '\n\t\t\t{}/{}\t{}'.format(i, len(std__), el)
    #                 msg.fix += txt 
    #         else:
    #             path_ = std__[0]['path']
    #             tmp_parent = ds
    #             attribute_is_present = True
    #             pp = list(path_)
    #             pp.append(kw)
    #             for aa in pp:
    #                 if aa in tmp_parent:
    #                     tmp_parent = tmp_parent[aa]
    #                 else:
    #                     attribute_is_present = False
    #                     break
    #             if attribute_is_present:
    #                 attribute_is_present = not tmp_parent.is_empty
    #             if not attribute_is_present:
    #                 msg.fix = "fixed by moving the attribute to the path {}".format(path_)
    #                 attribute = parent[tg]
    #                 del parent[tg]
    #                 put_attribute_in_path(ds, path_, attribute)
    #             else:
    #                 msg.fix = "didn't fixed because there is "\
    #                 "already an attribute in correct place"
    #     log.append(msg.getWholeMessage())
        
            



    # print(not_used_attribs)
    # print(not_recognized_attribs)
    # verify.PrintLog(log)


def fix_PatientSex(ds: Dataset, log: list) -> bool:
    fixed = False
    msg = mesgtext_cc.ErrorInfo()
    kw = "PatientSex"
    error_regex = r".*Unrecognized enumerated value .* for .* of attribute .*Patient.*Sex"
    if kw in ds:
        old_value = ds[kw].value
    else:
        old_value = ''
    new_value = ""
    fix_m = "fixed by modifying the {} from {} to empty string".format(
        kw, old_value)
    return subfix_AddOrChangeAttrib(ds, log, error_regex, fix_m, kw, new_value)


def fix_PregnancyStatus(ds: Dataset, log: list) -> bool:
    fixed = False
    msg = mesgtext_cc.ErrorInfo()
    kw = "PregnancyStatus"
    error_regex = r".*Unrecognized enumerated value .* attribute .*Pregnancy.*Status.*"
    return subfix_RemoveAttrib(ds, log, error_regex, kw)


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
    if not fixed:
        for i in idx:
            log.pop(i)
    return fixed


def fix_RemoveFOVDimensionsWhenZero(ds: Dataset, log: list) -> bool:
    fixed = False
    kw = "FieldOfViewDimensions"
    Error_regex = ".*Value is zero for.*attribute.*Field.*View.*Dimension.*"
    msg = mesgtext_cc.ErrorInfo()
    idx = subfix_LookUpRegexInLog(Error_regex, log)
    if kw in ds:
        if len(idx) == 0:
            idx.append(-1)
            log.append("Error - bad value (=0) for {}".format(kw))
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
        else:
                for i in idx:
                    log.pop(i)
    return fixed


def fix_PatientPositionAndPatientOrientationCodeSequencePresent(
        ds: Dataset, log:list) -> bool:
    code_kws = ['CodeValue', "CodeMeaning", "CodingSchemeDesignator",
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
                if len(seq_elem.value) > 0:
                    msg.fix = "kept {} but removed {}".format(txt, pp)
                    del ds[pp]
                else:
                    msg.fix = "kept {} but removed {}".format(pp, txt)
                    del ds[posq]
                log[i] = msg.getWholeMessage()
            fixed = True
    return fixed


def fix_AddMissingAtribute_RescaleSlope(ds:Dataset, log:list) -> bool:
    subfix_AddMissingAttrib(ds, log, "RescaleSlope", 1)


def fix_AddMissingAtribute_RescaleIntercept(ds:Dataset, log:list) -> bool:
    subfix_AddMissingAttrib(ds, log, "RescaleIntercept", 0)


def fix_ChangeWindowWidthLessThanOne(ds:Dataset, log:list) -> bool:
    regexp = '.*Not permitted to be \< 1 unless VOI LUT Function is ' \
             'LINEAR_EXACT or SIGMOID \- attribute \<WindowWidth\>.*'
    kw = "VOILUTFunction"
    value = "LINEAR_EXACT"
    fix_m = "fixed by modifying the {} to {}".format(kw, value)
    return subfix_AddOrChangeAttrib(ds, log, regexp, fix_m, kw, value)


def fix_InsertValue3ForImageType(ds:Dataset, log:list) -> bool:
    regexp = r'.*A value is required for value 3 in MR Images - attribute .*ImageType.*'
    kw = "ImageType"
    value = "OTHER"
    if not kw in ds:
        return False
    v = ds[kw].value
    if len(v) >= 3:
        v[2] = value
    else:
        v.insert(2, value)
    fix_m = "fixed by inserting the value 3 of {} to {}".format(kw, value)
    return subfix_AddOrChangeAttrib(ds, log, regexp, fix_m, kw, v)


def fix_ChangePhotometric_Interpretation(ds:Dataset, log:list) -> bool:
    fixed = False
    if(ds.SOPClassUID == sopclc_h.PETImageStorageSOPClassUID):
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


def fix_ReferencedImageSequence(ds, log: list) -> bool:
    # This patch is a prticular fixing procedure to replace SOPInstanceUID
    # with ReferencedSOPInstanceUID and SOPClassUID with ReferencedSOPClassUID
    fixed = False
    kw = 'ReferencedImageSequence'
    tg = Dictionary.tag_for_keyword(kw)
    if tg not in ds:
        return True
    val = ds[tg].value
    ref_cls_kw = 'ReferencedSOPClassUID'
    ref_cls_tg = Dictionary.tag_for_keyword(ref_cls_kw)
    ref_inst_kw = 'ReferencedSOPInstanceUID'
    ref_inst_tg = Dictionary.tag_for_keyword(ref_inst_kw)

    i = 0
    while i < len(val):
        item = val[i]
        if 'SOPInstanceUID' in item:
            msg = mesgtext_cc.ErrorInfo()
            msg.msg = "Item {}/{} in <ReferencedImageSequence> holds "\
                "<SOPInstanceUID> instead of <ReferencedSOPInstanceUID>".format(i + 1, len(val))
            msg.fix = "fixed by changing the attribute into <ReferencedSOPInstanceUID>"
            log.append(msg.getWholeMessage())
            item[ref_inst_tg] = DataElementX(
                ref_inst_tg, 'UI', item['SOPInstanceUID'].value) 
            del item['SOPInstanceUID']
            fixed = True
        if 'SOPClassUID' in item:
            msg = mesgtext_cc.ErrorInfo()
            msg.msg = "Item {}/{} in <ReferencedImageSequence> holds "\
                "<SOPClassUID> instead of <ReferencedSOPClassUID>".format(i + 1, len(val))
            msg.fix = "fixed by changing the attribute into <ReferencedSOPClassUID>"
            log.append(msg.getWholeMessage())
            item[ref_cls_tg] = DataElementX(
                ref_cls_tg, 'UI', item['SOPClassUID'].value) 
            del item['SOPClassUID']
            fixed = True
        i += 1
    return fixed



     