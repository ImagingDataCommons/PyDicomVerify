import argparse
import sys
import local_fix_vfy as fx
def main(argv):
    parser = argparse.ArgumentParser(
        description ="Dicom file fix. Specify the input file (-i) "
        "and output file (-o) .")
    parser.add_argument(
        "-i", "--input-dicom-file", dest ="input_file", metavar ="PATH",
        default ="-", required = True, help ="Input DICOM file")
    parser.add_argument(
        "-o", "--output-dicom-file", dest ="output_file", metavar ="PATH",
        default ="-", required = True, help ="Output fixed DICOM file")
    args = parser.parse_args(argv)
    ds, report= fx.fix_file_and_write(
        args.input_file, 
        args.output_file,
        (None, (None, None, None)),
        {})
    print('\n'.join(report))
if __name__ == "__main__":
    main(sys.argv[1:])