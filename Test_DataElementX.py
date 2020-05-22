import pydicom
import copy
import data_elementx as de


file = '/Users/afshin/Dropbox (Partners HealthCare)/IDC-MF_DICOM/out_00/hd/fixed_dicom//TCGA-UCEC/TCGA-D1-A0ZU/08-22-1987-MRI - PELVIS-71997/411-lava arc-03407/MR_00_.dcm'
ds = pydicom.dcmread(file)
ds2 = de.ConvertDataset(ds)
for key, val in ds2.items():
    print(ds2[key].used_in_verification)

 