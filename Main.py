from iodcomp_h import *
from iodcomp_select_h import SelectAndRunCompositeIOD
import verify

dicom_file = "E:\\output\\HighDcm\\TCGA-HNSC\\TCGA-CQ-5323\\08-08-1985-Head and Neck-22718\\1-2.0-39411\\CT_00_.dcm"
# dicom_file = "E:\\Dropbox\\IDC-MF_DICOM\\data\\TCGA-HNSC\\TCGA-BB-4223\\07-01-1995-MRI NECK W  WO CONTRAST-18215\\3-T1 SAG-02716\\000009.dcm"
verify.verify(dicom_file, False, "")


