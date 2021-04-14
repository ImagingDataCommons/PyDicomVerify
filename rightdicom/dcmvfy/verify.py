import sys
import rightdicom.dcmvfy.dicom_prechecks as dicom_prechecks
from rightdicom.dcmvfy.iodcomp_select_h import(
    # FUNCTIONS
    SelectAndRunCompositeIOD,)
from pydicom import dcmread, Dataset


def PrintLog(log) -> str:
    out = ''
    for item in log:
        out += item + '\n'
    return out


def verify_dicom_dataset(
        ds: Dataset, verbose:bool, profile:str, fix_trivials=False):
    fm = ds.file_meta
    for [k, v] in fm.items():
        ds[k] = fm[k]
    log = []
    for i in dir(dicom_prechecks):
        if i.startswith("check") or i.startswith("validate"):
            item = getattr(dicom_prechecks, i)
            if callable(item):
                item(ds, log)
    dicom_prechecks.\
        precheckInstanceReferencesAreIncludedInHierarchicalEvidenceSequences(
            ds, ds, log)
    SelectAndRunCompositeIOD(ds, verbose, log, profile, fix_trivials)
    dicom_prechecks.AfterVerificationValidateUsed(ds, log)
    for [k, v] in fm.items():
        del ds[k]
    return log


def verify_dicom(
        dicom_file_path, verbose:bool, profile:str, fix_trivials=False):
    ds = dcmread(dicom_file_path)
    log = verify_dicom_dataset(ds, verbose, profile, fix_trivials)
    lloogg = PrintLog(log)
    return lloogg


