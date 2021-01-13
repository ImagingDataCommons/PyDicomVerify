import argparse
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


def verify_dicom_dataset(ds: Dataset, verbose:bool, profile:str, fix_trivials=False):
    fm = ds.file_meta
    for [k, v] in fm.items():
        ds[k] = fm[k]
    log = []
    for i in dir(dicom_prechecks):
        if i.startswith("check") or i.startswith("validate"):
            item = getattr(dicom_prechecks, i)
            if callable(item):
                item(ds, log)
    dicom_prechecks.precheckInstanceReferencesAreIncludedInHierarchicalEvidenceSequences(
        ds, ds, log)
    SelectAndRunCompositeIOD(ds, verbose, log, profile, fix_trivials)
    dicom_prechecks.AfterVerificationValidateUsed(ds, log)
    for [k, v] in fm.items():
        del ds[k]
    return log
    


def verify_dicom(dicom_file_path, verbose:bool, profile:str, fix_trivials=False):
    ds = dcmread(dicom_file_path)
    log = verify_dicom_dataset(ds, verbose, profile, fix_trivials)
    lloogg = PrintLog(log)
    return lloogg


def main(argv):
    parser = argparse.ArgumentParser(
        description ="Dicom file verification. Specify the input file (-i) and verbosity (-v) .")
    parser.add_argument("-i", "--input-dicom-file", dest ="input_file", metavar ="PATH",
                        default ="-", required = True, help ="Input DICOM file")
    parser.add_argument("-v", "--verbose", dest ="verbose", type ="bool", action ="count",
                        default = "", required = False, help ="Verbosity")
    parser.add_argument("-p", "--profile", dest ="profile", type ="str",
                        action ="store", default = "", required = False,
                        help ="Don't know right now. To be added later")
    args = parser.parse_args(argv)
    verify_dicom(args.input_file, args.vervose, args.profile)
if __name__ == "__main__":
    main(sys.argv[1:])