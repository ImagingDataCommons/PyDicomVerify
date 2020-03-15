from pydicom import *
import pydicom.datadict as Dic
import pydicom.dataelem as Elm
import pydicom.sequence as Seq
from condn_cc import *
import os
from numpy import *

# import condn_cc
dicom_file = "E:\\output\\HighDcm\\TCGA-HNSC\\TCGA-CQ-5323\\08-08-1985-Head and Neck-22718\\1-2.0-39411\\CT_00_.dcm"
ds = dcmread(dicom_file)
xxx= ds["PatientName"]
aa = xxx.value

VMUNLIMITED = iinfo(uint32).max
tt: uint32 = 0xffffffff
VMNONE = 0
xx = getattr(ds, "PatientName")
elem = ds['PatientName']
elem.VM
attrname = "GraphicData"
ttag = Dic.tag_for_keyword(attrname)

ttag1 = elem.tag
x = ttag1.group
seq_elem = ds['DeidentificationMethodCodeSequence']
x = seq_elem.value
T = type(x)
print("type is = {}".format(type(x)))
if type(x) == Seq.Sequence:
    print("it is sequence")
for d in x:
    print(type(d))

s = ds["seq"]






is_private = ttag1.is_private
vvmm = Dic.dictionary_VM(ttag)
x = vvmm.split('-')

validmask = uint16(0)
ost = ""
validmask = validmask | (1 << 0)
value = uint16(0)
bitvalue = value & uint16(1 << 0)
ost += "Priority({})".format("Low" if bitvalue else "High")
Dic.tag

print("VM = {}".format(Dic.dictionary_VM(ttag)))
print("VR = {}".format(Dic.dictionary_VR(ttag)))
print("description = {}".format(Dic.dictionary_description(ttag)))
print("has tag = {}".format(Dic.dictionary_has_tag(ttag)))

# condn_cc.

try:
    yy = ds["Laterality"]
except BaseException as err:
    print('couldn\'t find')
    print(type(err))
    print(err)
if "Laterality" not in ds:
    print("Laterality is not in ds")


# Condition="NotLegacyConvertedCTOrMROrPET"
# # 	Element="SOPClassUID"						Modifier="Not" StringConstantFromRootAttribute="LegacyConvertedEnhancedCTImageStorageSOPClassUID"
# # 	Element="SOPClassUID"		Operator="And"	Modifier="Not" StringConstantFromRootAttribute="LegacyConvertedEnhancedMRImageStorageSOPClassUID"
# # 	Element="SOPClassUID"		Operator="And"	Modifier="Not" StringConstantFromRootAttribute="LegacyConvertedEnhancedPETImageStorageSOPClassUID"
# # ConditionEnd
# def StringValueMatch(ds, tagname, value, idx) -> bool:
#     match = False
#     candidate = 0
#     try:
#         elem = ds[tagname]
#         if idx == -1:
#             candidate = elem.value()
#
#         if (idx >= elem.VM):
#             return False
#         else:
#             candidate = [elem.value[idx]]
#         for v in candidate:
#             if v != value:
#                 return False
#     except KeyError:
#         return False
#
#
# def ConditionNotLegacyConvertedCTOrMROrPET(ds) -> bool:
#     cond = True
#     cond = cond and not StringValueMatch(ds, "SOPClassUID",
#                                          "LegacyConvertedEnhancedCTImageStorageSOPClassUID",
#                                          -1)
#
#     return cond


def BinaryBitMapDescription_RegionFlags(value: uint16):
    validmask = uint16(0)
    ost = ""
    validmask = validmask | (1 << 0)
    bitvalue = value & uint16(1 << 0)
    ost += "Priority({})".formt("Low" if bitvalue else "High")

    # ost << "Priority(" << (bitvalue ? "Low" : "High") << ") " << ends


# xx = "Priority({})".format(bitvalu	# {
# 	validmask|=(1<<1)
# 	Uint16 bitvalue=value&(1<<1)
# 	ost << "Scaling Protection(" << (bitvalue ? "Protected" : "Not Protected") << ") " << ends
# }
# {
# 	validmask|=(1<<2)
# 	Uint16 bitvalue=value&(1<<2)
# 	ost << "Doppler Scale Type(" << (bitvalue ? "Frequency" : "Velocity") << ") " << ends
# }
# {
# 	validmask|=(1<<3)
# 	Uint16 bitvalue=value&(1<<3)
# 	ost << "Scrolling Region(" << (bitvalue ? "Scrolling" : "Not Scrolling") << ") " << ends
# }
# {
# 	validmask|=(1<<4)
# 	Uint16 bitvalue=value&(1<<4)
# 	ost << "Sweeping Region(" << (bitvalue ? "Sweeping" : "Not Sweeping") << ") " << ends
# }
# if (value&~validmask)
# 	return 0
# else
# 	return ost.str()e ? "Low" : "High")

# BinaryBitMapDescription_RegionFlags(Uint16 value)
# {
# 	Uint16 validmask=0
# 	ostrstream ost
# 	{
# 		validmask|=(1<<0)
# 		Uint16 bitvalue=value&(1<<0)
# 		ost << "Priority(" << (bitvalue ? "Low" : "High") << ") " << ends
# 	}
# 	{
# 		validmask|=(1<<1)
# 		Uint16 bitvalue=value&(1<<1)
# 		ost << "Scaling Protection(" << (bitvalue ? "Protected" : "Not Protected") << ") " << ends
# 	}
# 	{
# 		validmask|=(1<<2)
# 		Uint16 bitvalue=value&(1<<2)
# 		ost << "Doppler Scale Type(" << (bitvalue ? "Frequency" : "Velocity") << ") " << ends
# 	}
# 	{
# 		validmask|=(1<<3)
# 		Uint16 bitvalue=value&(1<<3)
# 		ost << "Scrolling Region(" << (bitvalue ? "Scrolling" : "Not Scrolling") << ") " << ends
# 	}
# 	{
# 		validmask|=(1<<4)
# 		Uint16 bitvalue=value&(1<<4)
# 		ost << "Sweeping Region(" << (bitvalue ? "Sweeping" : "Not Sweeping") << ") " << ends
# 	}
# 	if (value&~validmask)
# 		return 0
# 	else
# 		return ost.str()



