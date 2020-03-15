from iodcomp_h import *
from iodcomp_select_h import SelectAndRunCompositeIOD
from pydicom import *
from condn_cc import *
import argparse
import sys
def PrintLog(log):
    for item in log:
        print(item)
def verify(dicom_file_path, verbose:bool, profile:str):
    ds = dcmread(dicom_file_path)
    fm = ds.file_meta
    for [k,v] in fm.items():
        ds[k] = v

    log = []
    SelectAndRunCompositeIOD(ds, verbose, log , Dic.DicomDictionary, profile)
    PrintLog(log)

def main(argv):
    parser = argparse.ArgumentParser(
        description="Dicom file verification. Specify the input file (-i) and verbosity (-v) .")
    parser.add_argument("-i", "--input-dicom-file", dest="input_file", metavar="PATH",
                        default="-", required=True, help="Input DICOM file")
    parser.add_argument("-v", "--verbose", dest="verbose", type="bool", action="count",
                        default="", required=False, help="Verbosity")
    parser.add_argument("-p", "--profile", dest="profile", type="str",
                        action="store", default="", required=False,
                        help="Don't know right now. To be added later")
    args = parser.parse_args(argv)


    verify(args.input_file, args.vervose, args.profile)


if __name__ == "__main__":
    main(sys.argv[1:])