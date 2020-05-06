import pydicom
import copy
import data_elementx as de


file = '/Users/afshin/Dropbox (Partners HealthCare)/IDC-MF_DICOM/data/TCGA-BLCA/TCGA-4Z-AA82/10-21-2003-AbdomenABDOME2FASESVOL Adult-32850/2-AXIAL SC-84709/000000.dcm'
ds = pydicom.dcmread(file)
ds2 = de.ConvertDataset(ds)
for key, val in ds2.items():
    print(ds2[key].used_in_verification)

 