from pydicom.tag import Tag
from pydicom.dataset import Dataset
from pydicom.dataelem import DataElement
from pydicom.sequence import Sequence
from pydicom.multival import MultiValue
import pydicom.datadict as Dictionary
import validate_vr
from pydicom.uid import UID
from numpy import *
from mesgtext_cc import *
from sopclc_h import *
from module_cc import *
from condn_h import *
import re


def fix_VRForLongitudinalTemporalInformationModified(ds: Dataset) -> bool:
    kw = "LongitudinalTemporalInformationModified"
    if kw in ds:
        tag = Dictionary.tag_for_keyword(kw)
        elem = ds[tag]
        if elem.VR == "SH":
            elem.VR = "CS"
            ds[kw] = elem
    else:
        return False
    return True


def fix_RemoveFOVDimensionsWhenZero(ds: Dataset) -> bool:
    fixed = False
    kw = "FieldOfViewDimensions"
    if kw in ds:
        tag = Dictionary.tag_for_keyword(kw)
        elem = ds[tag]
        for i in elem.value:
            if i == 0:
                fixed = True
                break
        if fixed:
            del ds[kw]
    return fixed

def fix_RemoveRedundant_InversionTime(ds: Dataset) -> bool:
    fixed = False
    kw = "InversionTime"
    mod = 'MRImage'
    cond = Condition_MRIsInversionRecovery
    if kw not in ds:
        return fixed
    success = verifyType2C(ds, mod, kw,
                           False, [], '',
                           cond,
                           False,
                           ds, ds,
                           0, 0)

    if success == False:
        del ds[kw]
        fixed = True
    return fixed

def fix_RemoveRedundant_Laterality(ds: Dataset) -> bool:
    fixed = False
    kw = "Laterality"
    mod = 'GeneralSeries'
    cond = Condition_LateralityRequired
    if kw not in ds:
        return fixed
    success = verifyType2C(ds, mod, kw,
                           False, [], '',
                           cond,
                           False,
                           ds, ds,
                           0, 0)

    if success == False:
        del ds[kw]
        fixed = True
    return fixed