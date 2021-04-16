import argparse
import sys
import local_fix_convert as fx
def main(argv):
    parser = argparse.ArgumentParser(
        description ="Dicom file verification. Specify the input file (-i) "
        "and verbosity (-v) .")
    parser.add_argument(
        "-i", "--input-dicom-file", dest ="input_file", metavar ="PATH",
        default ="-", required = True, help ="Input DICOM file")
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action ="store_true",
        required = False, help ="Verbosity")
    args = parser.parse_args(argv)
    print(fx.verify_pyverify(args.input_file, '', args.verbose))
if __name__ == "__main__":
    main(sys.argv[1:])