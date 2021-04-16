import logging
import logging.config
import os
import pydicom
import shutil
import common.common_tools as ctools
import common.parallelization as pl
import conversion as convtool
from anatomy_query import (
    # FUNCTIONS
    query_anatomy_from_tables,
)
from pydicom.charset import (
    # VARIABLES
    python_encoding,
)
from rightdicom.dcmfix.fix_all import (
    # FUNCTIONS
    fix_dicom,
)
from rightdicom.dcmfix.study_dependent_patches import (
    # FUNCTIONS
    add_anatomy,
    fix_SOPReferencedMacro,
)
from rightdicom.dcmvfy.verify import (
    # FUNCTIONS
    verify_dicom,
)
from dicom_fix_issue_info import (
    # CLASSES
    DicomFileInfo
)

iod_names = [
        "CRImage",
        "CTImage",
        "MRImage",
        "NMImage",
        "USImage",
        "USMultiFrameImage",
        "SCImage",
        "MultiframeSingleBitSCImage",
        "MultiframeGrayscaleByteSCImage",
        "MultiframeGrayscaleWordSCImage",
        "MultiframeTrueColorSCImage",
        "StandaloneOverlay",
        "StandaloneCurve",
        "StandaloneModalityLUT",
        "StandaloneVOILUT",
        "Segmentation",
        "SurfaceSegmentation",
        "SpatialRegistration",
        "DeformableSpatialRegistration",
        "SpatialFiducials",
        "EncapsulatedPDF",
        "EncapsulatedCDA",
        "EncapsulatedSTL",
        "RealWorldValueMapping",
        "IVOCTImage",
        "ParametricMap",
        "BasicDirectory",
        "BasicDirectoryDental",
        "XAImage",
        "XRFImage",
        "EnhancedXAImage",
        "EnhancedXRFImage",
        "XRay3DAngiographicImage",
        "XRay3DCraniofacialImage",
        "PETImage",
        "EnhancedPETImage",
        "LegacyConvertedEnhancedPETImage",
        "PrivatePixelMedLegacyConvertedEnhancedPETImage",
        "RTImage",
        "RTDose",
        "RTStructureSet",
        "RTPlan",
        "RTBeamsTreatmentRecord",
        "RTBrachyTreatmentRecord",
        "RTTreatmentSummaryRecord",
        "RTIonPlan",
        "RTIonBeamsTreatmentRecord",
        "DXImageForProcessing",
        "DXImageForPresentation",
        "MammographyImageForProcessing",
        "MammographyImageForPresentation",
        "MammographyImageForProcessingIHEMammo",
        "MammographyImageForProcessingIHEMammoPartialViewOption",
        "MammographyImageForPresentationIHEMammo",
        "MammographyImageForPresentationIHEMammoPartialViewOption",
        "IntraoralImageForProcessing",
        "IntraoralImageForPresentation",
        "IntraoralImageForPresentationDentalMedia",
        "DXImageForPresentationDentalMedia",
        "BreastTomosynthesisImage",
        "BreastTomosynthesisImageIHEDBT",
        "BreastProjectionXRayImage",
        "VLEndoscopicImage",
        "VLMicroscopicImage",
        "VLSlideCoordinatesMicroscopicImage",
        "VLPhotographicImage",
        "VideoEndoscopicImage",
        "VideoMicroscopicImage",
        "VideoPhotographicImage",
        "OphthalmicPhotography8BitImage",
        "OphthalmicPhotography16BitImage",
        "StereometricRelationship",
        "OphthalmicTomographyImage",
        "VLWholeSlideMicroscopyImage",
        "LensometryMeasurements",
        "AutorefractionMeasurements",
        "KeratometryMeasurements",
        "SubjectiveRefractionMeasurements",
        "VisualAcuityMeasurements",
        "OphthalmicAxialMeasurements",
        "IntraocularLensCalculations",
        "OphthalmicVisualFieldStaticPerimetryMeasurements",
        "BasicVoice",
        "TwelveLeadECG",
        "GeneralECG",
        "AmbulatoryECG",
        "HemodynamicWaveform",
        "CardiacElectrophysiologyWaveform",
        "BasicTextSR",
        "EnhancedSR",
        "ComprehensiveSR",
        "Comprehensive3DSR",
        "KeyObjectSelectionDocument",
        "KeyObjectSelectionDocumentIHEXDSIManifest",
        "MammographyCADSR",
        "ChestCADSR",
        "ProcedureLog",
        "XRayRadiationDoseSR",
        "XRayRadiationDoseSRIHEREM",
        "RadiopharmaceuticalRadiationDoseSR",
        "SpectaclePrescriptionReport",
        "AcquisitionContextSR",
        "GrayscaleSoftcopyPresentationState",
        "ColorSoftcopyPresentationState",
        "PseudoColorSoftcopyPresentationState",
        "BlendingSoftcopyPresentationState",
        "HangingProtocol",
        "ColorPalette",
        "BasicStructuredDisplay",
        "EnhancedMRImage",
        "EnhancedMRColorImage",
        "MRSpectroscopy",
        "RawData",
        "LegacyConvertedEnhancedMRImage",
        "PrivatePixelMedLegacyConvertedEnhancedMRImage",
        "TractographyResults",
        "EnhancedCTImage",
        "LegacyConvertedEnhancedCTImage",
        "PrivatePixelMedLegacyConvertedEnhancedCTImage",
        "EnhancedUltrasoundVolume",
        "EnhancedUltrasoundVolumeQTUS",
    ]


def organize_dcmvfy_errors(issues: list, output: list = []):
    prev_line = None
    for line_ in issues:
        if line_ in iod_names:
            continue
        if line_.startswith('Error - ') or line_.startswith('Warning - '):
            if prev_line is not None:
                output.append(prev_line)
            prev_line = line_
        else:
            if prev_line is not None:
                prev_line += ('\n' + line_)
    if prev_line is not None:
        output.append(prev_line)


def verify_dciodvfy(
        file: str, char_set: str = 'ascii', report_file: str = ''):
    raw_log: list = []
    organized_log: list = []
    dcm_verify = "/Users/afshin/Documents/softwares"\
        "/dicom3tools/most_recent_exe/dciodvfy"
    if not os.path.exists(dcm_verify):
        dcm_verify = shutil.which('dciodvfy')
        if dcm_verify is None:
            print("Error: install dciodvfy into system path")
            assert(False)
    ctools.RunExe(
        [dcm_verify, '-filename', file], '', '',
        errlog=raw_log, char_encoding=char_set)
    organize_dcmvfy_errors(raw_log, organized_log)
    if report_file:
        ctools.WriteStringToFile(report_file, raw_log)
    return (raw_log, organized_log)


def verify_pyverify(
        file: str, report_file: str = '', verbose: bool = False):
    my_code_output = verify_dicom(file, verbose, '')
    if report_file:
        ctools.WriteStringToFile(report_file, my_code_output)
    return my_code_output 


def verify_with_dciodvfy_and_pyvfy(
        file: str, char_set: str = 'ascii', report_file: str = ''):
    rawlog, orglog = verify_dciodvfy(file, char_set)
    pylog = verify_pyverify(file)
    if report_file:
        ctools.WriteStringToFile(report_file, '{:=^120}'.format("dciodvfy"))
        ctools.WriteStringToFile(report_file, rawlog, True)
        ctools.WriteStringToFile(
            report_file, '{:=^120}'.format("pyvfy"), True)
        ctools.WriteStringToFile(report_file, pylog, True)
    return (rawlog, orglog, pylog)


def fix_file(dicom_file: str, 
             anatomy: tuple,
             reference: dict):
    log_fix: list = []
    ds = pydicom.read_file(dicom_file)
    if len(anatomy) == 2:
        add_anatomy(ds, anatomy[0], anatomy[1], log_fix)
    fix_SOPReferencedMacro(ds, log_fix, reference)
    fix_dicom(ds, log_fix)
    return (ds, log_fix)


def fix_file_and_write(
        dicom_file: str, 
        dicom_fixed_file: str,
        anatomy: tuple,
        reference: dict,
        dicom_fix_report_file: str = ''):
    ds, fix_report =  fix_file(dicom_file, anatomy, reference)
    pydicom.write_file(dicom_fixed_file, ds)
    if dicom_fix_report_file:
        ctools.WriteStringToFile(dicom_fix_report_file, fix_report)
    return (ds, fix_report)
    
    
def fix_file_verify_write(
        dicom_file: str, 
        dicom_fixed_file: str,
        anatomy: tuple,
        reference: dict,
        dicom_fix_report_file: str = '',
        pre_fix_vfy_file: str = '',
        post_fix_vfy_file: str = ''
    ):
    ds, fix_report = fix_file_and_write(
        dicom_file,
        dicom_fixed_file,
        anatomy, reference,
        dicom_fix_report_file)
    char_set = DicomFileInfo.get_charset_val_from_dataset(ds)
    pre_rawlog, pre_orglog, pre_pylog = verify_with_dciodvfy_and_pyvfy(
        dicom_file, char_set, pre_fix_vfy_file)
    post_rawlog, post_orglog, post_pylog = verify_with_dciodvfy_and_pyvfy(
        dicom_fixed_file, char_set, post_fix_vfy_file)
    return (ds, fix_report, pre_rawlog, pre_orglog, pre_pylog,
        post_rawlog, post_orglog, post_pylog)
    
    
def fix_file_verify_write_dciodvfy(
        dicom_file: str, 
        dicom_fixed_file: str,
        anatomy: tuple,
        reference: dict,
        dicom_fix_report_file: str = '',
        pre_fix_vfy_file: str = '',
        post_fix_vfy_file: str = ''
    ):
    ds, fix_report = fix_file_and_write(
        dicom_file,
        dicom_fixed_file,
        anatomy, reference,
        dicom_fix_report_file)
    char_set = DicomFileInfo.get_charset_val_from_dataset(ds)
    pre_rawlog, pre_orglog = verify_dciodvfy(
        dicom_file, char_set, pre_fix_vfy_file)
    post_rawlog, post_orglog = verify_dciodvfy(
        dicom_fixed_file, char_set, post_fix_vfy_file)
    return (ds, fix_report, pre_rawlog, pre_orglog,
        post_rawlog, post_orglog)
