import pydicom.datadict as Dictionary
import rightdicom.dcmvfy.mesgtext_cc as mesgtext_cc
import rightdicom.dcmvfy.sopclc_h as sopclc_h
from rightdicom.dcmvfy.verify import verify_dicom_dataset
from rightdicom.dcmvfy.dicom_prechecks import get_not_used_list
import rightdicom.dcmvfy.mesgtext_cc as mesgtext_cc
from rightdicom.dcmvfy.validate_vr import tag2str
from pydicom.dataset import(
    # CLASSES
    Dataset,
)
from rightdicom.dcmfix.fix_tools import (
    # FUNCTIONS
    subfix_AddMissingAttrib,
    subfix_AddOrChangeAttrib,
    subfix_CodeSeqItem2txt,
    subfix_LookUpRegexInLog,
    get_full_attrib_list,
    put_attribute_in_path,
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
    fixed = False
    
    not_used_attribs = []
    not_recognized_attribs = []
    wrn_msg = 'Warning - Attribute is not present in standard DICOM IOD - {}'
    get_not_used_list(ds, not_used_attribs, not_recognized_attribs)
    standard_ds = get_full_attrib_list(ds)
    for kw, tg, parent in not_used_attribs:
        msg = mesgtext_cc.ErrorInfo()
        msg.msg = wrn_msg.format(tag2str(tg))
        if kw not in standard_ds:
            del parent[tg]
            msg.fix = "fixed by removing the attribute"
        else:
            path_ = standard_ds[kw]['path']
            msg.fix = "fixed by moving the attribute to the path {}".format(path_)
            attribute = parent[tg]
            del parent[tg]
            put_attribute_in_path(ds, path_, attribute)
        log.append(msg.getWholeMessage())
        
            



    # print(not_used_attribs)
    # print(not_recognized_attribs)
    # verify.PrintLog(log)


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