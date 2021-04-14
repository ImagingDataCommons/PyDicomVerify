import argparse
import sys
import conversion
def main(argv):
    parser = argparse.ArgumentParser(
        description ="Dicom single frame to multi-frame conversion.\n"
        "Specify the input dicom folder (-i) conaining dicom single frames"
        "and the output dicom folder (-o) to save multifame images .")
    parser.add_argument(
        "-i", "--input-dicom-folder", dest ="input_folder", metavar ="PATH",
        default ="-", required = True, help ="Input DICOM folder")
    parser.add_argument(
        "-o", "--output-dicom-folder", dest ="output_folder", metavar ="PATH",
        default ="-", required = True, help ="Output fixed DICOM folder")
    args = parser.parse_args(argv)
    conversion.ConvertByHighDicomNew(
        args.input_folder,
        args.output_folder)
    print('Conversion finished successfully')
if __name__ == "__main__":
    main(sys.argv[1:])