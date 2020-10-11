import pydicom
import rightdicom.dcmvfy.mesgtext_cc as mesgtext_cc
import rightdicom.dcmvfy.validate_vr as validate_vr
from pydicom.dataelem import(
    # FUNCTIONS
    DataElement_from_raw,
    # CLASSES
    DataElement,
    # VARIABLES
    RawDataElement,
    RawDataElement
    )
from pydicom.dataset import(
    # CLASSES
    Dataset,)
from pydicom.multival import(
    # CLASSES
    MultiValue,)
from pydicom.sequence import(
    # CLASSES
    Sequence,)
from pydicom.tag import(
    # FUNCTIONS
    Tag,)
from rightdicom.dcmfix.fix_tools import(
    # FUNCTIONS
    LoopOverAllAtribsAndRemoveIfConditionIsTrue,
    subfix_HasTrailingNulls,
    subfix_ReplaceSlashWithBackslash,
    subfix_checkandfixBasicCodeSeq,)
from rightdicom.dcmvfy.condn_h import(
    # FUNCTIONS
    Condition_UnwantedPixelAspectRatioWhenImagerPixelSpacingPresent,
    Condition_UnwantedPixelAspectRatioWhenMPEG2MPHLTransferSyntax,
    Condition_UnwantedPixelAspectRatioWhenNominalScannedPixelSpacingPresent,
    Condition_UnwantedPixelAspectRatioWhenPerFramePixelMeasuresMacro,
    Condition_UnwantedPixelAspectRatioWhenPixelSpacingPresent,
    Condition_UnwantedPixelAspectRatioWhenSharedPixelMeasuresMacro,)
from rightdicom.dcmvfy.mesgtext_cc import(
    # CLASSES
    ErrorInfo,
    ErrorType,)


def generalfix_RemoveEmptyCodes(parent_ds: Dataset, log:list) -> bool:
    fixed = False
    elems_to_be_removed = []
    for key, elem in parent_ds.items():
        elem = parent_ds[key]
        if type(elem) == pydicom.dataelem.RawDataElement:
            elem = pydicom.dataelem.DataElement_from_raw(elem)
        items_to_be_removed = []
        if type(elem.value) == Sequence:
            if elem.keyword.endswith("CodeSequence"):
                fixed = fixed or subfix_checkandfixBasicCodeSeq(elem, log)
            else:
                for(item, idx) in zip(elem.value, range(0, len(elem.value))):
                    fixed = fixed or generalfix_RemoveEmptyCodes(item, log)
        elif type(elem.value) == Dataset:
            fixed = fixed or generalfix_RemoveEmptyCodes(elem.value, log)


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
            msg = mesgtext_cc.ErrorInfo()
            msg.msg = '{} Error - {}'.format(ErrorType.BadValue.value,"<PixelAspectRatio> is 1:1 or redundant")
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