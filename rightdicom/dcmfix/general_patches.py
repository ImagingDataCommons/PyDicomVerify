import pydicom
import rightdicom.dcmvfy.mesgtext_cc as mesgtext_cc
import rightdicom.dcmvfy.validate_vr as validate_vr
from pydicom.datadict import (
    # FUNCTIONS
    dictionary_VR,
    tag_for_keyword,
    dictionary_VM,
)
from pydicom.dataelem import (
    # FUNCTIONS
    DataElement_from_raw,
    # VARIABLES
    RawDataElement,
    msg,
)
from pydicom.dataset import (
    # CLASSES
    Dataset,
)
from pydicom.multival import (
    # CLASSES
    MultiValue,
)
from pydicom.sequence import (
    # CLASSES
    Sequence,
)
from rightdicom.dcmfix.fix_tools import (
    # FUNCTIONS
    LoopOverAllAtribsAndRemoveIfConditionIsTrue,
    subfix_HasTrailingNulls,
    subfix_ReplaceSlashWithBackslash,
    subfix_checkandfixBasicCodeSeq,
    find_attribute_in_iod,
    get_full_attrib_list
)
from rightdicom.dcmvfy.condn_h import (
    # FUNCTIONS
    Condition_UnwantedPixelAspectRatioWhenImagerPixelSpacingPresent,
    Condition_UnwantedPixelAspectRatioWhenMPEG2MPHLTransferSyntax,
    Condition_UnwantedPixelAspectRatioWhenNominalScannedPixelSpacingPresent,
    Condition_UnwantedPixelAspectRatioWhenPerFramePixelMeasuresMacro,
    Condition_UnwantedPixelAspectRatioWhenPixelSpacingPresent,
    Condition_UnwantedPixelAspectRatioWhenSharedPixelMeasuresMacro,
)
from rightdicom.dcmvfy.mesgtext_cc import (
    # CLASSES
    ErrorInfo,
    ErrorType,
)
from rightdicom.dcmvfy.sopclc_h import (
    # VARIABLES
    CTImageStorageSOPClassUID,
    MRImageStorageSOPClassUID,
    PETImageStorageSOPClassUID,
)
from rightdicom.dcmvfy.data_elementx import DataElementX
iod_dict = None

def generalfix_RemoveEmptyCodes(
        parent_ds: Dataset, log:list, kw_to_be_removed: list = []) -> bool:
    global iod_dict
    if 'SOPClassUID' in parent_ds:
        iod_dict =  get_full_attrib_list(parent_ds)

    fixed = False
    for key, elem in parent_ds.items():
        elem = parent_ds[key]
        if type(elem) == pydicom.dataelem.RawDataElement:
            elem = pydicom.dataelem.DataElement_from_raw(elem)
        if type(elem.value) == Sequence:
            if elem.keyword.endswith("CodeSequence"):
                if iod_dict is None or elem.keyword not in iod_dict:
                    type_ = None
                else:
                    type_ = iod_dict[elem.keyword]['type']
                if type_ != '1' or type_ != '1C' or type_ != '2'\
                        or type_ != '2C':
                    fixed = fixed or subfix_checkandfixBasicCodeSeq(elem, log)
                if elem.is_empty:
                    kw_to_be_removed.append((parent_ds, elem.keyword))
            else:
                for(item, idx) in zip(elem.value, range(0, len(elem.value))):
                    fixed = fixed or generalfix_RemoveEmptyCodes(
                        item, log, kw_to_be_removed)
        elif type(elem.value) == Dataset:
            fixed = fixed or generalfix_RemoveEmptyCodes(
                elem.value, log, kw_to_be_removed,)
    if 'SOPClassUID' in parent_ds:
        for ddss, k in kw_to_be_removed:
            if k in ddss:
                a = ddss[k]
                # print('{} is present and going to be removed'.format(k))
            else:
                # print('{} is not present and going to continue anyway'.format(k))
                continue
            if iod_dict is None or k not in iod_dict:
                type_ = None
            else:
                type_ = iod_dict[k]['type']
            if type_ != '1' or type_ != '1C' or type_ != '2' or type_ != '2C':
                err = "{} <{}>".format(
                    validate_vr.tag2str(a.tag), a.keyword)
                msg = ErrorInfo(
                    "General Fix - Attribute type SQ has no items",
                    "fixed by removing the whole attribute for {}".format(
                        err))
                log.append(msg.getWholeMessage())
                del ddss[k]
    


def generalfix_TrailingNulls(ds: Dataset, log: list) -> bool:
    fixed = False
    elemsTobeCorrected = []
    for key, a in ds.items():
        a = ds[key]
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
                
                err = "<{}> {}".format(
                    a.keyword, validate_vr.tag2str(a.tag))
                msg = ErrorInfo(
                    "General Fix - Trailing null bytesz",
                    "fixed by removing the trailing null bytes for {}".format(
                        err))
                log.append(msg.getWholeMessage())
                elemsTobeCorrected.append(a)
                fixed = True
    return fixed


def generalfix_RemoveAllRetired(ds: Dataset, log: list) -> bool:
    err = "General Fix - {} is retired"
    return LoopOverAllAtribsAndRemoveIfConditionIsTrue(
        ds, lambda attrib: attrib.is_retired, log, err)


def generalfix_RemoveUnwanterPixelAspctRatio(ds:Dataset, log:list) -> bool:
    fixed = False
    kw = "PixelAspectRatio"
    is_one_to_one = False
    if kw in ds:
        elem = ds[kw]
        if type(elem) == MultiValue:
            if len(elem) == 2:
                is_one_to_one = (elem.value[0] == elem.value[2])
        if(Condition_UnwantedPixelAspectRatioWhenPixelSpacingPresent(
                ds, ds, ds) or
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
            msg = ErrorInfo()
            msg.msg = '{} Error - {}'.format(
                ErrorType.BadValue.value,"<PixelAspectRatio> is 1:1 or redundant")
            msg.fix = "fixed by removing the attribute"
            log.append(msg.getWholeMessage())
            del ds["PixelAspectRatio"]
            fixed = True
    return fixed


def generalfix_ReplaceSlashWithBackslash4CS(ds:Dataset, log:list) -> bool:
    fixed = False
    for ky,  v in ds.items():
        v = ds[ky]
        if type(v.value) == Sequence:
            for item in v.value:
                generalfix_ReplaceSlashWithBackslash4CS(item, log)
        elif type(v.value) == Dataset:
            generalfix_ReplaceSlashWithBackslash4CS(v.value, log)
        else:
            if v.VR == 'CS':
                fixed = subfix_ReplaceSlashWithBackslash(ds[ky], log)
    return fixed


def generalfix_CheckAndFixModality(ds:Dataset, log:list) -> bool:
    fixed = False
    modality_sop ={
        CTImageStorageSOPClassUID: 'CT',
        MRImageStorageSOPClassUID: 'MR',
        PETImageStorageSOPClassUID: 'PT',
    }
    if 'SOPClassUID' in ds:
        sop_class = ds['SOPClassUID'].value 
    else:
        return False
    mod_tg = tag_for_keyword('Modality')
    if mod_tg in ds:
        modality = ds[mod_tg].value
    else:
        modality = ''
    if modality == '' or modality != modality_sop[sop_class]:
        ds [mod_tg]= DataElementX(
            mod_tg, dictionary_VR(mod_tg), modality_sop[sop_class])
        msg = ErrorInfo()
        msg.msg = 'General Fix - {}'.format("<Modality> is wrong or absent")
        msg.fix = "fixed by reading the <SOPClassUID> and setting <Modality>"\
            " from '{}' to '{}'".format(modality, modality_sop[sop_class])
        log.append(msg.getWholeMessage())
        fixed = True
    return fixed


def generalfix_AddPresentationLUTShape(ds:Dataset, log:list) -> bool:
    fixed = False
    photo_in_tg = tag_for_keyword('PhotometricInterpretation')
    if photo_in_tg not in ds:
        return fixed
    photo_in_v = ds[photo_in_tg].value
    pres_lut_shape_tg = tag_for_keyword('PresentationLUTShape')
    if pres_lut_shape_tg in ds:
        pres_lut_shape_a = ds[pres_lut_shape_tg]
    else:
        pres_lut_shape_a = DataElementX(
            pres_lut_shape_tg, dictionary_VR(pres_lut_shape_tg), '')
    old_pls = pres_lut_shape_a.value
    if photo_in_v == 'MONOCHROME2' and old_pls != 'IDENTITY':
        new_pls = 'IDENTITY'
        pres_lut_shape_a.value = new_pls
        fixed = True
    elif photo_in_v == 'MONOCHROME1' and old_pls != 'INVERSE':
        new_pls = 'INVERSE'
        pres_lut_shape_a.value = new_pls
        fixed = True
    if fixed:
        ds [pres_lut_shape_tg]= pres_lut_shape_a
        msg = ErrorInfo()
        msg.msg = 'General Fix - {}'.format(
            "<PresentationLUTShape> is wrong or absent")
        msg.fix = "fixed by setting the <PresentationLUTShape>"\
            " from '{}' to '{}'".format(old_pls, new_pls)
        log.append(msg.getWholeMessage())
    return fixed


def generalfix_WindowWidth(ds, log):
    fixed = False
    wwkw = 'WindowWidth'
    wwtg = tag_for_keyword(wwkw)
    if wwtg in ds:
        if ds[wwtg].value == 0:
            ds[wwtg].value = 1
            err = "<{}> {}".format(
                wwkw, validate_vr.tag2str(wwtg))
            msg = ErrorInfo(
                "General Fix - Window width {} "\
                    "is not allowed to be 0".format(err),
                "fixed by replacing it with 1")
            log.append(msg.getWholeMessage())
            fixed = True
    return fixed


def generalfix_CT_RescaleType(ds, log):
    fixed = False
    modality = None if "Modality" not in ds else ds['Modality'].value
    if modality == 'CT':
        if 'RescaleType' not in ds:
            return fixed
        if ds['RescaleType'] == 'HU':
            return fixed
        containes_localizer = False
        ImageType_v = [] if 'ImageType' not in ds else ds['ImageType'].value
        for i in ImageType_v:
            if i == 'LOCALIZER':
                containes_localizer = True
                break
        if not containes_localizer:
            oldval = ds['RescaleType'].value
            ds['RescaleType'].value = "HU"
            msg = mesgtext_cc.ErrorInfo()
            msg.msg = "General Fix - <RescaletType> is not HU (Hounsfield Units) "
            msg.fix = "fixed by changing the attribute from {} to {}".format(
                oldval, 'HU'
            )
            log.append(msg.getWholeMessage())
            fixed = True
    return fixed

    
def generalfix_VM1(ds, log):
    fixed = False
    elemsTobeCorrected = []
    for key, a in ds.items():
        a = ds[key]
        if key.is_private:
            continue
        try:
            dvr = dictionary_VM(key)
        except (BaseException):
            return fixed
        if dvr != '1':
            continue
        if a.VM <= 1:
            continue
        if (a.VR == 'SQ'):
            continue
        concat = '/'.join(a.value)
        ds[key] = DataElementX(key, a.VR, concat)
        fixed = True
        err = "<{}> {}".format(
            a.keyword, validate_vr.tag2str(a.tag))
        msg = ErrorInfo(
            "General Fix - Value Multiplicity for {} "\
                "is not allowed to be more than one".format(err),
            "fixed by concatenating all itmes into one {}".format(concat))
        log.append(msg.getWholeMessage())
        fixed = True
    return fixed


def generalfix_CapitalizeCS(ds, log):
    fixed = False
    elemsTobeCorrected = []
    def check(v, n, N, a):
            u = v.upper()
            if u != v:
                err = "<{}> {}".format(
                a.keyword, validate_vr.tag2str(a.tag))
                msg = ErrorInfo(
                    "General Fix - {} lower case is not allowed for Code "\
                        "String itme number {}/ {}".format(err, n, N),
                    "fixed by capitalizing the value from {} to {}".format(
                        v, u))
                log.append(msg.getWholeMessage())
                return u
            else:
                return None
    for key, a in ds.items():
        a = ds[key]
        vr = a.VR
        if vr != 'CS':
            continue
        if a.is_empty:
            continue
        val = a.value 
        if type(val) != MultiValue:
            uu = check(val, 1, 1, a)
            if uu is not None:
                a.value = uu
                fixed = True
        else:
            for i in range(len(val)):
                vv = val[i]
                uu = check(vv, i + 1, len(val), a)
                if uu is not None:
                    a.value[i] = uu
                    fixed = True
    return fixed


def generalfix_DS_Precision(ds, log):
    fixed = False
    elemsTobeCorrected = []
    def check(v, n, N, a):
        v = str(v)
        if len(v) > 16:
            f = float(v)
            u = '{:1.10E}'.format(f)
            n = 10
            while len(u) > 16 and n > 0:
                n -= 1
                ptrn = '{{:1.{}E}}'.format(n)
                u = ptrn.format(f)
            err = "<{}> {}".format(
                a.keyword, validate_vr.tag2str(a.tag))
            msg = ErrorInfo(
                "General Fix - {} value length greater than 16 is not allowed"\
                    "for DS value representation in itme number {}/ {}".format(
                        err, n, N),
                "fixed by modifying the precision from {} to {}".format(
                    v, u))
            log.append(msg.getWholeMessage())
            return u
        else:
            return None
    for key, a in ds.items():
        a = ds[key]
        vr = a.VR
        if vr != 'DS':
            continue
        if a.is_empty:
            continue
        val = a.value 
        if type(val) != MultiValue:
            uu = check(val, 1, 1, a)
            if uu is not None:
                a.value = uu
                fixed = True
        else:
            for i in range(len(val)):
                vv = val[i]
                uu = check(vv, i + 1, len(val), a)
                if uu is not None:
                    a.value[i] = uu
                    fixed = True
    return fixed






# def generalfix_EditNotUsedTags(ds:Dataset, log:list) -> bool:
#     fixed = False
#     not_used_attribs = []
#     not_recognized_attribs = []
#     get_not_used_list(ds, not_used_attribs, not_recognized_attribs)
#     print(not_used_attribs)
#     print(not_recognized_attribs)









    # photo_in_tg = tag_for_keyword('PhotometricInterpretation')
    # if photo_in_tg not in ds:
    #     return fixed
    # photo_in_v = ds[photo_in_tg].value
    # pres_lut_shape_tg = tag_for_keyword('PresentationLUTShape')
    # if pres_lut_shape_tg in ds:
    #     pres_lut_shape_a = ds[pres_lut_shape_tg]
    # else:
    #     pres_lut_shape_a = DataElementX(
    #         pres_lut_shape_tg, dictionary_VR(pres_lut_shape_tg), '')
    # old_pls = pres_lut_shape_a.value
    # if photo_in_v == 'MONOCHROME2' and old_pls != 'IDENTITY':
    #     new_pls = 'IDENTITY'
    #     pres_lut_shape_a.value = new_pls
    #     fixed = True
    # elif photo_in_v == 'MONOCHROME1' and old_pls != 'INVERSE':
    #     new_pls = 'INVERSE'
    #     pres_lut_shape_a.value = new_pls
    #     fixed = True
    # if fixed:
    #     ds [pres_lut_shape_tg]= pres_lut_shape_a
    #     msg = ErrorInfo()
    #     msg.msg = 'General Fix - {}'.format(
    #         "<PresentationLUTShape> is wrong or absent")
    #     msg.fix = "fixed by setting the <PresentationLUTShape>"\
    #         " from '{}' to '{}'".format(old_pls, new_pls)
    #     log.append(msg.getWholeMessage())
    # return fixed   

