# Automatically generated from template - EDITS WILL BE LOST

from condn_cc import *
from sopclc_h import *
from pydicom.tag import Tag
from pydicom.dataset import Dataset
def Condition_Never(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	 return False
def Condition_Always(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	 return True
def Condition_TractographyResultsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, TractographyResultsStorageSOPClassUID))
	return cond0
def Condition_ParametricMapInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, ParametricMapStorageSOPClassUID))
	return cond0
def Condition_VLWholeSlideMicroscopyImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, VLWholeSlideMicroscopyImageStorageSOPClassUID))
	return cond0
def Condition_EnhancedUltrasoundVolumeInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedUSVolumeStorageSOPClassUID))
	return cond0
def Condition_BasicStructuredDisplayInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, BasicStructuredDisplayStorageSOPClassUID))
	return cond0
def Condition_IVOCTImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, IVOCTImageStorageForProcessingSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, IVOCTImageStorageForPresentationSOPClassUID))
	return cond0
def Condition_BreastTomosynthesisInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, BreastTomosynthesisImageStorageSOPClassUID))
	return cond0
def Condition_NotBreastTomosynthesisInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, BreastTomosynthesisImageStorageSOPClassUID))
	return cond0
def Condition_ColorPaletteInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, ColorPaletteStorageSOPClassUID))
	return cond0
def Condition_NotColorPaletteInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, ColorPaletteStorageSOPClassUID))
	return cond0
def Condition_SegmentationInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, SegmentationStorageSOPClassUID))
	return cond0
def Condition_SurfaceSegmentationInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, SurfaceSegmentationStorageSOPClassUID))
	return cond0
def Condition_EnhancedXAImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedXAImageStorageSOPClassUID))
	return cond0
def Condition_EnhancedXRFImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedXRFImageStorageSOPClassUID))
	return cond0
def Condition_RealWorldValueMappingInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RealWorldValueMappingStorageSOPClassUID))
	return cond0
def Condition_EncapsulatedPDFInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EncapsulatedPDFStorageSOPClassUID))
	return cond0
def Condition_EncapsulatedCDAInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EncapsulatedCDAStorageSOPClassUID))
	return cond0
def Condition_EncapsulatedSTLInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EncapsulatedSTLStorageSOPClassUID))
	return cond0
def Condition_OphthalmicPhotography8BitImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, OphthalmicPhotography8BitImageStorageSOPClassUID))
	return cond0
def Condition_OphthalmicPhotography16BitImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, OphthalmicPhotography16BitImageStorageSOPClassUID))
	return cond0
def Condition_StereometricRelationshipInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, StereometricRelationshipStorageSOPClassUID))
	return cond0
def Condition_OphthalmicTomographyImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, OphthalmicTomographyImageStorageSOPClassUID))
	return cond0
def Condition_HangingProtocolInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, HangingProtocolStorageSOPClassUID))
	return cond0
def Condition_SpatialFiducialsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, SpatialFiducialsStorageSOPClassUID))
	return cond0
def Condition_SpatialRegistrationInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, SpatialRegistrationStorageSOPClassUID))
	return cond0
def Condition_DeformableSpatialRegistrationInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DeformableSpatialRegistrationStorageSOPClassUID))
	return cond0
def Condition_EnhancedCTImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedCTImageStorageSOPClassUID))
	return cond0
def Condition_NotLegacyConvertedCTOrMROrPET(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedCTImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedMRImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedPETImageStorageSOPClassUID))
	return cond0
def Condition_LegacyConvertedEnhancedCTImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedCTImageStorageSOPClassUID))
	return cond0
def Condition_NotLegacyConvertedCT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedCTImageStorageSOPClassUID))
	return cond0
def Condition_PrivatePixelMedLegacyConvertedEnhancedCTImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, PrivatePixelMedLegacyConvertedEnhancedCTImageStorageSOPClassUID))
	return cond0
def Condition_RawDataInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RawDataStorageSOPClassUID))
	return cond0
def Condition_MRSpectroscopyInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, MRSpectroscopyStorageSOPClassUID))
	return cond0
def Condition_EnhancedMRImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedMRImageStorageSOPClassUID))
	return cond0
def Condition_EnhancedMRColorImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedMRColorImageStorageSOPClassUID))
	return cond0
def Condition_LegacyConvertedEnhancedMRImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedMRImageStorageSOPClassUID))
	return cond0
def Condition_NotLegacyConvertedMR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedMRImageStorageSOPClassUID))
	return cond0
def Condition_PrivatePixelMedLegacyConvertedEnhancedMRImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, PrivatePixelMedLegacyConvertedEnhancedMRImageStorageSOPClassUID))
	return cond0
def Condition_KeyObjectSelectionDocumentStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, KeyObjectSelectionDocumentStorageSOPClassUID))
	return cond0
def Condition_MammographyCADSRStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, MammographyCADSRStorageSOPClassUID))
	return cond0
def Condition_ChestCADSRStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, ChestCADSRStorageSOPClassUID))
	return cond0
def Condition_BasicTextSRStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, BasicTextSRStorageSOPClassUID))
	return cond0
def Condition_EnhancedSRStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedSRStorageSOPClassUID))
	return cond0
def Condition_ComprehensiveSRStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, ComprehensiveSRStorageSOPClassUID))
	return cond0
def Condition_Comprehensive3DSRStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, Comprehensive3DSRStorageSOPClassUID))
	return cond0
def Condition_ProcedureLogStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, ProcedureLogStorageSOPClassUID))
	return cond0
def Condition_XRayRadiationDoseSRStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, XRayRadiationDoseSRStorageSOPClassUID))
	return cond0
def Condition_RadiopharmaceuticalRadiationDoseSRStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RadiopharmaceuticalRadiationDoseSRStorageSOPClassUID))
	return cond0
def Condition_SpectaclePrescriptionReportInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, SpectaclePrescriptionReportStorageSOPClassUID))
	return cond0
def Condition_AcquisitionContextSRStorageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, AcquisitionContextSRStorageSOPClassUID))
	return cond0
def Condition_GrayscaleSoftcopyPresentationStateInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, GrayscaleSoftcopyPresentationStateStorageSOPClassUID))
	return cond0
def Condition_ColorSoftcopyPresentationStateInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, ColorSoftcopyPresentationStateStorageSOPClassUID))
	return cond0
def Condition_PseudoColorSoftcopyPresentationStateInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, PseudoColorSoftcopyPresentationStateStorageSOPClassUID))
	return cond0
def Condition_BlendingSoftcopyPresentationStateInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, BlendingSoftcopyPresentationStateStorageSOPClassUID))
	return cond0
def Condition_IsForProcessingSOPClass(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalXRayImageStorageForProcessingSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalMammographyXRayImageStorageForProcessingSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalIntraoralXRayImageStorageForProcessingSOPClassUID))
	return cond0
def Condition_IsForPresentationSOPClass(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalXRayImageStorageForPresentationSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalMammographyXRayImageStorageForPresentationSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalIntraoralXRayImageStorageForPresentationSOPClassUID))
	return cond0
def Condition_DXImageForProcessingInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalXRayImageStorageForProcessingSOPClassUID))
	return cond0
def Condition_DXImageForPresentationInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalXRayImageStorageForPresentationSOPClassUID))
	return cond0
def Condition_MammographyImageForProcessingInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalMammographyXRayImageStorageForProcessingSOPClassUID))
	return cond0
def Condition_MammographyImageForPresentationInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalMammographyXRayImageStorageForPresentationSOPClassUID))
	return cond0
def Condition_IntraoralImageForProcessingInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalIntraoralXRayImageStorageForProcessingSOPClassUID))
	return cond0
def Condition_IntraoralImageForPresentationInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalIntraoralXRayImageStorageForPresentationSOPClassUID))
	return cond0
def Condition_MediaStorageDirectoryInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "MediaStorageSOPClassUID", -1, MediaStorageDirectoryStorageSOPClassUID))
	return cond0
def Condition_PETImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, PETImageStorageSOPClassUID))
	return cond0
def Condition_EnhancedPETImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedPETImageStorageSOPClassUID))
	return cond0
def Condition_LegacyConvertedEnhancedPETImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedPETImageStorageSOPClassUID))
	return cond0
def Condition_NotLegacyConvertedPET(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedPETImageStorageSOPClassUID))
	return cond0
def Condition_PrivatePixelMedLegacyConvertedEnhancedPETImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, PrivatePixelMedLegacyConvertedEnhancedPETImageStorageSOPClassUID))
	return cond0
def Condition_StandalonePETCurveInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, StandalonePETCurveStorageSOPClassUID))
	return cond0
def Condition_RTImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RTImageStorageSOPClassUID))
	return cond0
def Condition_RTDoseInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RTDoseStorageSOPClassUID))
	return cond0
def Condition_RTStructureSetInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RTStructureSetStorageSOPClassUID))
	return cond0
def Condition_RTPlanInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RTPlanStorageSOPClassUID))
	return cond0
def Condition_RTIonPlanInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RTIonPlanStorageSOPClassUID))
	return cond0
def Condition_RTBeamsTreatmentRecordInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RTBeamsTreatmentRecordStorageSOPClassUID))
	return cond0
def Condition_RTIonBeamsTreatmentRecordInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RTIonBeamsTreatmentRecordStorageSOPClassUID))
	return cond0
def Condition_RTBrachyTreatmentRecordInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RTBrachyTreatmentRecordStorageSOPClassUID))
	return cond0
def Condition_RTTreatmentSummaryRecordInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RTTreatmentSummaryRecordStorageSOPClassUID))
	return cond0
def Condition_VisibleLightEndoscopicImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, VisibleLightEndoscopicImageStorageSOPClassUID))
	return cond0
def Condition_VideoEndoscopicImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, VideoEndoscopicImageStorageSOPClassUID))
	return cond0
def Condition_VisibleLightMicroscopicImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, VisibleLightMicroscopicImageStorageSOPClassUID))
	return cond0
def Condition_VideoMicroscopicImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, VideoMicroscopicImageStorageSOPClassUID))
	return cond0
def Condition_VisibleLightSlideCoordinatesMicroscopicImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, VisibleLightSlideCoordinatesMicroscopicImageStorageSOPClassUID))
	return cond0
def Condition_VisibleLightPhotographicImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, VisibleLightPhotographicImageStorageSOPClassUID))
	return cond0
def Condition_VideoPhotographicImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, VideoPhotographicImageStorageSOPClassUID))
	return cond0
def Condition_BasicVoiceInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, BasicVoiceStorageSOPClassUID))
	return cond0
def Condition_TwelveLeadECGInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, TwelveLeadECGStorageSOPClassUID))
	return cond0
def Condition_GeneralECGInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, GeneralECGStorageSOPClassUID))
	return cond0
def Condition_AmbulatoryECGInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, AmbulatoryECGStorageSOPClassUID))
	return cond0
def Condition_HemodynamicWaveformInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, HemodynamicWaveformStorageSOPClassUID))
	return cond0
def Condition_CardiacElectrophysiologyWaveformInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, CardiacElectrophysiologyWaveformStorageSOPClassUID))
	return cond0
def Condition_RespiratoryWaveformInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, RespiratoryWaveformStorageSOPClassUID))
	return cond0
def Condition_CRImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, ComputedRadiographyImageStorageSOPClassUID))
	return cond0
def Condition_CTImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, CTImageStorageSOPClassUID))
	return cond0
def Condition_MRImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, MRImageStorageSOPClassUID))
	return cond0
def Condition_NMImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, NuclearMedicineImageStorageSOPClassUID))
	return cond0
def Condition_USImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, UltrasoundImageStorageSOPClassUID))
	return cond0
def Condition_USMultiFrameImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, UltrasoundMultiframeImageStorageSOPClassUID))
	return cond0
def Condition_SCImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, SecondaryCaptureImageStorageSOPClassUID))
	return cond0
def Condition_MultiframeSingleBitSCImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, MultiframeSingleBitSecondaryCaptureImageStorageSOPClassUID))
	return cond0
def Condition_MultiframeGrayscaleByteSCImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, MultiframeGrayscaleByteSecondaryCaptureImageStorageSOPClassUID))
	return cond0
def Condition_MultiframeGrayscaleWordSCImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, MultiframeGrayscaleWordSecondaryCaptureImageStorageSOPClassUID))
	return cond0
def Condition_MultiframeTrueColorSCImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, MultiframeTrueColorSecondaryCaptureImageStorageSOPClassUID))
	return cond0
def Condition_XAImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, XRayAngiographicImageStorageSOPClassUID))
	return cond0
def Condition_XABiplaneImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, XRayAngiographicBiplaneImageStorageSOPClassUID))
	return cond0
def Condition_XRFImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, XRayRadioFluoroscopicImageStorageSOPClassUID))
	return cond0
def Condition_XRay3DAngiographicImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, XRay3DAngiographicImageStorageSOPClassUID))
	return cond0
def Condition_XRay3DCraniofacialImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, XRay3DCraniofacialImageStorageSOPClassUID))
	return cond0
def Condition_StandaloneOverlayInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, StandaloneOverlayStorageSOPClassUID))
	return cond0
def Condition_StandaloneCurveInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, StandaloneCurveStorageSOPClassUID))
	return cond0
def Condition_StandaloneModalityLUTInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, StandaloneModalityLUTStorageSOPClassUID))
	return cond0
def Condition_StandaloneVOILUTInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, StandaloneVOILUTStorageSOPClassUID))
	return cond0
def Condition_LensometryMeasurementsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, LensometryMeasurementsStorageSOPClassUID))
	return cond0
def Condition_AutorefractionMeasurementsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, AutorefractionMeasurementsStorageSOPClassUID))
	return cond0
def Condition_KeratometryMeasurementsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, KeratometryMeasurementsStorageSOPClassUID))
	return cond0
def Condition_SubjectiveRefractionMeasurementsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, SubjectiveRefractionMeasurementsStorageSOPClassUID))
	return cond0
def Condition_VisualAcuityMeasurementsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, VisualAcuityMeasurementsStorageSOPClassUID))
	return cond0
def Condition_OphthalmicAxialMeasurementsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, OphthalmicAxialMeasurementsStorageSOPClassUID))
	return cond0
def Condition_IntraocularLensCalculationsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, IntraocularLensCalculationsStorageSOPClassUID))
	return cond0
def Condition_OphthalmicVisualFieldStaticPerimetryMeasurementsInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, OphthalmicVisualFieldStaticPerimetryMeasurementsStorageSOPClassUID))
	return cond0
def Condition_BreastProjectionXRayImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, BreastProjectionXRayImageStorageForPresentationSOPClassUID))
	cond0 = cond0 or(StringValueMatch(rootds , "SOPClassUID", -1, BreastProjectionXRayImageStorageForProcessingSOPClassUID))
	return cond0
def Condition_NeedModuleCommonInstanceReference(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ReferencedSeriesSequence"))
	cond0 = cond0  or (ElementPresent(ds , "StudiesContainingOtherReferencedInstancesSequence"))
	return cond0
def Condition_NeedModuleAcquisitionContext(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "AcquisitionContextSequence"))
	return cond0
def Condition_NeedModuleContrastBolus(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ContrastBolusAgent"))
	return cond0
def Condition_NeedModuleCine(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FrameTime"))
	cond0 = cond0  or (ElementPresent(ds , "FrameTimeVector"))
	return cond0
def Condition_NeedModuleMultiFrame(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfFrames"))
	cond0 = cond0  or (ElementPresent(ds , "FrameIncrementPointer"))
	return cond0
def Condition_NumberOfFramesGreaterThanOne(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfFrames"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfFrames", -1, BinaryValueMatchOperator.GreaterThan, 1))
	return cond0
def Condition_NumberOfFramesIsAbsentOrOne(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "NumberOfFrames"))
	cond0 = cond0 or(BinaryValueMatch(ds , "NumberOfFrames", -1, BinaryValueMatchOperator.Equals, 1))
	return cond0
def Condition_NeedModuleNMMultiGatedAcquisitionImageRetired(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FrameTime"))
	return cond0
def Condition_NeedModuleNMSPECTAcquisitionImageRetired(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "AngularStep"))
	return cond0
def Condition_NeedModuleUSFrameOfReference(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RegionLocationMinX0"))
	cond0 = cond0  or (ElementPresent(ds , "RegionLocationMinY0"))
	cond0 = cond0  or (ElementPresent(ds , "RegionLocationMaxX1"))
	cond0 = cond0  or (ElementPresent(ds , "RegionLocationMaxY1"))
	cond0 = cond0  or (ElementPresent(ds , "PhysicalUnitsXDirection"))
	cond0 = cond0  or (ElementPresent(ds , "PhysicalUnitsYDirection"))
	cond0 = cond0  or (ElementPresent(ds , "PhysicalDeltaX"))
	cond0 = cond0  or (ElementPresent(ds , "PhysicalDeltaY"))
	return cond0
def Condition_NeedModuleOverlayPlane(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayRows", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayColumns", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayType", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlaySubtype", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayOrigin", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayBitsAllocated", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayBitPosition", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayData", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "ROIArea", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "ROIMean", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "ROIStandardDeviation", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayDescriptorGray", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayDescriptorRed", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayDescriptorGreen", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayDescriptorBlue", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayGray", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayRed", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayGreen", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayBlue", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayDescription", 0xff00))
	cond0 = cond0  or (ElementPresentMasked(ds , "OverlayLabel", 0xff00))
	return cond0
def Condition_NeedModuleApproval(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ApprovalStatus"))
	cond0 = cond0  or (ElementPresent(ds , "ReviewDate"))
	cond0 = cond0  or (ElementPresent(ds , "ReviewTime"))
	cond0 = cond0  or (ElementPresent(ds , "ReviewerName"))
	return cond0
def Condition_NeedModuleModalityLUT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RescaleIntercept"))
	cond0 = cond0  or (ElementPresent(ds , "RescaleSlope"))
	cond0 = cond0  or (ElementPresent(ds , "RescaleType"))
	cond0 = cond0  or (ElementPresent(ds , "ModalityLUTSequence"))
	return cond0
def Condition_NeedModuleVOILUT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "WindowCenter"))
	cond0 = cond0  or (ElementPresent(ds , "WindowWidth"))
	cond0 = cond0  or (ElementPresent(ds , "WindowCenterWidthExplanation"))
	cond0 = cond0  or (ElementPresent(ds , "VOILUTSequence"))
	cond0 = cond0  or (ElementPresent(ds , "VOILUTFunction"))
	return cond0
def Condition_NeedModuleFrameOfReference(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FrameOfReferenceUID"))
	cond0 = cond0  or (ElementPresent(ds , "PositionReferenceIndicator"))
	return cond0
def Condition_NeedModuleFrameOfReferenceInVLI(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FrameOfReferenceUID"))
	cond0 = cond0  or (ElementPresent(ds , "PositionReferenceIndicator"))
	return cond0
def Condition_NeedModuleImagePlane(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelSpacing"))
	cond0 = cond0  or (ElementPresent(ds , "ImageOrientationPatient"))
	cond0 = cond0  or (ElementPresent(ds , "ImagePositionPatient"))
	return cond0
def Condition_NeedModuleMultiFrameOverlay(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfFramesInOverlay"))
	return cond0
def Condition_NeedModuleGeneralReference(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ReferencedImageSequence"))
	cond0 = cond0  or (ElementPresent(ds , "ReferencedInstanceSequence"))
	cond0 = cond0  or (ElementPresent(ds , "DerivationDescription"))
	cond0 = cond0  or (ElementPresent(ds , "DerivationCodeSequence"))
	cond0 = cond0  or (ElementPresent(ds , "SourceImageSequence"))
	cond0 = cond0  or (ElementPresent(ds , "SourceInstanceSequence"))
	return cond0
def Condition_NeedModuleUSRegionCalibration(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SequenceOfUltrasoundRegions"))
	return cond0
def Condition_NeedModuleGeneralEquipment(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "Manufacturer"))
	cond0 = cond0  or (ElementPresent(ds , "InstitutionName"))
	cond0 = cond0  or (ElementPresent(ds , "InstitutionAddress"))
	cond0 = cond0  or (ElementPresent(ds , "StationName"))
	cond0 = cond0  or (ElementPresent(ds , "InstitutionalDepartmentName"))
	cond0 = cond0  or (ElementPresent(ds , "ManufacturerModelName"))
	cond0 = cond0  or (ElementPresent(ds , "DeviceSerialNumber"))
	cond0 = cond0  or (ElementPresent(ds , "SoftwareVersions"))
	cond0 = cond0  or (ElementPresent(ds , "GantryID"))
	cond0 = cond0  or (ElementPresent(ds , "SpatialResolution"))
	cond0 = cond0  or (ElementPresent(ds , "DateOfLastCalibration"))
	cond0 = cond0  or (ElementPresent(ds , "TimeOfLastCalibration"))
	cond0 = cond0  or (ElementPresent(ds , "PixelPaddingValue"))
	return cond0
def Condition_EnhancedGeneralEquipmentIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "Manufacturer"))
	cond0 = cond0  and (ElementPresent(ds , "ManufacturerModelName"))
	cond0 = cond0  and (ElementPresent(ds , "DeviceSerialNumber"))
	cond0 = cond0  and (ElementPresent(ds , "SoftwareVersions"))
	return cond0
def Condition_NeedModuleNMTomoAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "GATED TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON GATED TOMO"))
	return cond0
def Condition_NeedModuleNMMultiGatedAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "GATED TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON GATED TOMO"))
	return cond0
def Condition_NeedModuleNMPhase(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "DYNAMIC"))
	return cond0
def Condition_NeedModuleNMReconstruction(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON GATED TOMO"))
	return cond0
def Condition_NeedModuleSpecimen(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ContainerIdentifier"))
	cond0 = cond0  or (ElementPresent(ds , "IssuerOfTheContainerIdentifierSequence"))
	cond0 = cond0  or (ElementPresent(ds , "AlternateContainerIdentifierSequence"))
	cond0 = cond0  or (ElementPresent(ds , "ContainerTypeCodeSequence"))
	cond0 = cond0  or (ElementPresent(ds , "ContainerDescription"))
	cond0 = cond0  or (ElementPresent(ds , "ContainerComponentSequence"))
	cond0 = cond0  or (ElementPresent(ds , "SpecimenDescriptionSequence"))
	return cond0
def Condition_NeedModuleDXDetector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "DetectorType"))
	return cond0
def Condition_NeedModuleXAXRFMultiFramePresentation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PreferredPlaybackSequencing"))
	cond0 = cond0  or (ElementPresent(ds , "FrameDisplaySequence"))
	cond0 = cond0  or (ElementPresent(ds , "RecommendedViewingMode"))
	cond0 = cond0  or (ElementPresent(ds , "DisplayFilterPercentage"))
	return cond0
def Condition_RecommendedViewingModeIsSUB(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "RecommendedViewingMode", -1, "SUB"))
	return cond0
def Condition_CodingSchemeVersionRequired(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "BI"))
	cond0 = cond0 or(StringValueMatch(ds , "CodingSchemeDesignator", -1, "SCPECG"))
	cond0 = cond0 or(StringValueMatch(ds , "CodingSchemeDesignator", -1, "BARI"))
	cond0 = cond0 or(StringValueMatch(ds , "CodingSchemeDesignator", -1, "NCDR"))
	return cond0
def Condition_SpecimenIsSlide(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Modality", -1, "SM"))
	return cond0
def Condition_ModalityIsSM(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Modality", -1, "SM"))
	return cond0
def Condition_SpecimenNeedsDescription(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	return cond0
def Condition_NeedMeasurementUnitsCodeSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0 or(StringValueMatch(ds , "ValueType", -1, "NUM"))
	cond0 = cond0  or (ElementPresent(ds , "NumericValue"))
	return cond0
def Condition_MeasurementUnitsCodeSequencePresentAndNumericValueAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "MeasurementUnitsCodeSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "NumericValue"))
	return cond0
def Condition_AcquisitionContextItemIsNumeric(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "NUMERIC"))
	cond0 = cond0 or(ElementPresent(ds , "NumericValue"))
	cond0 = cond0 or(ElementPresent(ds , "FloatingPointValue"))
	cond0 = cond0 or(ElementPresent(ds , "RationalNumeratorValue"))
	cond0 = cond0 or(ElementPresent(ds , "RationalDenominatorValue"))
	cond0 = cond0 or(ElementPresent(ds , "MeasurementUnitsCodeSequence"))
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "Time"))
	cond1 = cond1  and  not (ElementPresent(ds , "PersonName"))
	cond1 = cond1  and  not (ElementPresent(ds , "TextValue"))
	cond1 = cond1  and  not (ElementPresent(ds , "ConceptCodeSequence"))
	cond1 = cond1  and  not (ElementPresent(ds , "Date"))
	cond0 = cond0 or cond1
	return cond0
def Condition_AcquisitionContextItemIsNotNumeric(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "ValueType", -1, "NUMERIC"))
	cond0 = cond0 or not (ElementPresent(ds , "NumericValue"))
	cond0 = cond0 or(ElementPresent(ds , "Time"))
	cond0 = cond0 or(ElementPresent(ds , "PersonName"))
	cond0 = cond0 or(ElementPresent(ds , "TextValue"))
	cond0 = cond0 or(ElementPresent(ds , "ConceptCodeSequence"))
	cond0 = cond0 or(ElementPresent(ds , "Date"))
	return cond0
def Condition_AcquisitionContextItemIsDate(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "DATE"))
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "Time"))
	cond1 = cond1  and  not (ElementPresent(ds , "PersonName"))
	cond1 = cond1  and  not (ElementPresent(ds , "TextValue"))
	cond1 = cond1  and  not (ElementPresent(ds , "ConceptCodeSequence"))
	cond1 = cond1  and  not (ElementPresent(ds , "NumericValue"))
	cond0 = cond0 or cond1
	return cond0
def Condition_AcquisitionContextItemIsTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "TIME"))
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "Date"))
	cond1 = cond1  and  not (ElementPresent(ds , "PersonName"))
	cond1 = cond1  and  not (ElementPresent(ds , "TextValue"))
	cond1 = cond1  and  not (ElementPresent(ds , "ConceptCodeSequence"))
	cond1 = cond1  and  not (ElementPresent(ds , "NumericValue"))
	cond0 = cond0 or cond1
	return cond0
def Condition_AcquisitionContextItemIsPersonName(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "PNAME"))
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "Date"))
	cond1 = cond1  and  not (ElementPresent(ds , "Time"))
	cond1 = cond1  and  not (ElementPresent(ds , "TextValue"))
	cond1 = cond1  and  not (ElementPresent(ds , "ConceptCodeSequence"))
	cond1 = cond1  and  not (ElementPresent(ds , "NumericValue"))
	cond0 = cond0 or cond1
	return cond0
def Condition_AcquisitionContextItemIsTextValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "TEXT"))
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "Date"))
	cond1 = cond1  and  not (ElementPresent(ds , "Time"))
	cond1 = cond1  and  not (ElementPresent(ds , "PersonName"))
	cond1 = cond1  and  not (ElementPresent(ds , "ConceptCodeSequence"))
	cond1 = cond1  and  not (ElementPresent(ds , "NumericValue"))
	cond0 = cond0 or cond1
	return cond0
def Condition_AcquisitionContextItemIsConceptCodeSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "CODE"))
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "Date"))
	cond1 = cond1  and  not (ElementPresent(ds , "Time"))
	cond1 = cond1  and  not (ElementPresent(ds , "PersonName"))
	cond1 = cond1  and  not (ElementPresent(ds , "TextValue"))
	cond1 = cond1  and  not (ElementPresent(ds , "NumericValue"))
	cond0 = cond0 or cond1
	return cond0
def Condition_ConceptNameCodeSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ConceptNameCodeSequence"))
	return cond0
def Condition_UnformattedTextValueNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "UnformattedTextValue"))
	return cond0
def Condition_ContextIdentifierIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ContextIdentifier"))
	return cond0
def Condition_ExtendedCodingScheme(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ContextGroupExtensionFlag", -1, "Y"))
	return cond0
def Condition_SamplesPerPixelGreaterThanOne(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.GreaterThan, 1))
	return cond0
def Condition_PhotometricInterpretationNeedsPalette(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "PALETTE COLOR"))
	return cond0
def Condition_ImagePixelMacroNeedsPaletteDescriptor(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "PALETTE COLOR"))
	cond0 = cond0 or(StringValueMatch(ds , "PixelPresentation", -1, "COLOR"))
	cond0 = cond0 or(StringValueMatch(ds , "PixelPresentation", -1, "MIXED"))
	return cond0
def Condition_ImagePixelMacroNeedsPaletteDescriptorAndNotSegmentedLegallyPresentInPaletteColorModule(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "PALETTE COLOR"))
	cond1 = cond1 or(StringValueMatch(ds , "PixelPresentation", -1, "COLOR"))
	cond1 = cond1 or(StringValueMatch(ds , "PixelPresentation", -1, "MIXED"))
	cond0 = cond0 or cond1
	cond1 = False
	cond1 = cond1  or (ElementPresent(ds , "SegmentedRedPaletteColorLookupTableData"))
	cond1 = cond1  and (ElementPresent(ds , "SegmentedGreenPaletteColorLookupTableData"))
	cond1 = cond1  and (ElementPresent(ds , "SegmentedBluePaletteColorLookupTableData"))
	cond2 = False
	cond2 = cond2  or (StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.6.1"))
	cond2 = cond2 or(StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.3.1"))
	cond1 = cond1 and cond2
	cond0 = cond0 and  not cond1
	return cond0
def Condition_NeedsNonSegmentedLookupTableData(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "SegmentedRedPaletteColorLookupTableData"))
	cond1 = cond1  and  not (ElementPresent(ds , "SegmentedGreenPaletteColorLookupTableData"))
	cond1 = cond1  and  not (ElementPresent(ds , "SegmentedBluePaletteColorLookupTableData"))
	cond0 = cond0 or cond1
	cond0 = cond0 or(StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.11.3"))
	cond0 = cond0 or(StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.11.4"))
	cond0 = cond0 or(StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.39.1"))
	return cond0
def Condition_NeedsSegmentedLookupTableData(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "RedPaletteColorLookupTableData"))
	cond0 = cond0  and  not (ElementPresent(ds , "GreenPaletteColorLookupTableData"))
	cond0 = cond0  and  not (ElementPresent(ds , "BluePaletteColorLookupTableData"))
	cond0 = cond0  and  not (StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.11.3"))
	cond0 = cond0  and  not (StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.11.4"))
	cond0 = cond0  and  not (StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.39.1"))
	return cond0
def Condition_PhotometricInterpretationIsPaletteColor(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "PALETTE COLOR"))
	return cond0
def Condition_PhotometricInterpretationIsMonochrome2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_PhotometricInterpretationIsMonochrome1(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "MONOCHROME1"))
	return cond0
def Condition_PhotometricInterpretationIsMonochrome(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "MONOCHROME1"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_PhotometricInterpretationNeedsOneSample(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "PALETTE COLOR"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "MONOCHROME1"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_PhotometricInterpretationIsGrayscaleOrAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PhotometricInterpretation"))
	cond0 = cond0 or(StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME1"))
	cond0 = cond0 or(StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_PhotometricInterpretationIsColor(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME1"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_PhotometricInterpretationNeedsThreeSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "RGB"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_FULL"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_FULL_422"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_PARTIAL_422"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_PARTIAL_420"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_RCT"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_ICT"))
	return cond0
def Condition_SOPClassIsCTOrMR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedMRImageStorageSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedMRColorImageStorageSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, MRSpectroscopyStorageSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, MRImageStorageSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedCTImageStorageSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, CTImageStorageSOPClassUID))
	return cond0
def Condition_ModalityIsCTOrMR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Modality", -1, "MR"))
	cond0 = cond0  or (StringValueMatch(ds , "Modality", -1, "CT"))
	return cond0
def Condition_PatientOrientationRequired(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedMRImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedMRColorImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedMRImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, MRSpectroscopyStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, MRImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, CTImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedCTImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedCTImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, NuclearMedicineImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, NuclearMedicineImageStorageRetiredSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, PETImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, EnhancedPETImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedPETImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, ParametricMapStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, RTDoseStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, VLWholeSlideMicroscopyImageStorageSOPClassUID))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "SOPClassUID", -1, SegmentationStorageSOPClassUID))
	cond2 = False
	cond2 = cond2  or (ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 and cond2
	cond0 = cond0 and  not cond1
	return cond0
def Condition_DXPatientOrientationRequired(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ViewCodeSequence"))
	cond1 = False
	cond1 = cond1  or (ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "ViewCodeSequence", -1, "SRT"))
	cond2 = False
	cond2 = cond2  or (ElementStringValueMatchWithin(ds , "CodeValue", "ViewCodeSequence", -1, "G-8300"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "ViewCodeSequence", -1, "G-8310"))
	cond1 = cond1 and cond2
	cond0 = cond0 or  not cond1
	return cond0
def Condition_MRIsNotEchoPlanarOrIsSegmentedKSpace(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "ScanningSequence", -1, "EP"))
	cond0 = cond0 or(StringValueMatch(ds , "SequenceVariant", -1, "SK"))
	return cond0
def Condition_MRIsInversionRecovery(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ScanningSequence", -1, "IR"))
	return cond0
def Condition_MRIsCardiacOrPulseGated(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ScanOptions", -1, "CG"))
	cond0 = cond0 or(StringValueMatch(ds , "ScanOptions", -1, "PPG"))
	return cond0
def Condition_NMIsWholeBody(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "NuclearMedicineSeriesType", -1, "WHOLE BODY"))
	return cond0
def Condition_CurveDataDescriptorPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentMasked(ds , "CurveDataDescriptor", 0xff00))
	return cond0
def Condition_ModalityLUTSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ModalityLUTSequence"))
	return cond0
def Condition_RescaleSlopePresentAndNotIdentity(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RescaleSlope"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "RescaleIntercept", -1, BinaryValueMatchOperator.NotEquals, 0))
	cond1 = cond1 or(BinaryValueMatch(ds , "RescaleSlope", -1, BinaryValueMatchOperator.NotEquals, 1))
	cond0 = cond0 and cond1
	return cond0
def Condition_RescaleInterceptPresentAndNotIdentity(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RescaleIntercept"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "RescaleIntercept", -1, BinaryValueMatchOperator.NotEquals, 0))
	cond1 = cond1 or(BinaryValueMatch(ds , "RescaleSlope", -1, BinaryValueMatchOperator.NotEquals, 1))
	cond0 = cond0 and cond1
	return cond0
def Condition_RescaleInterceptPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RescaleIntercept"))
	return cond0
def Condition_RescaleInterceptNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "RescaleIntercept"))
	return cond0
def Condition_RescaleTypeIsPresentAndNotHU(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RescaleType"))
	cond0 = cond0  and  not (StringValueMatch(ds , "RescaleType", -1, "HU"))
	return cond0
def Condition_MultienergyAcquisitionOrRescaleTypeIsPresentAndNotHU(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	cond0 = cond0 or(ElementPresent(ds , "RescaleType"))
	cond0 = cond0  and  not (StringValueMatch(ds , "RescaleType", -1, "HU"))
	return cond0
def Condition_RescaleTypeIsPresentAndNotHUAndImageIsOriginalNotLocalizerAndNotMultienergyAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RescaleType"))
	cond0 = cond0  and  not (StringValueMatch(ds , "RescaleType", -1, "HU"))
	cond0 = cond0  and (StringValueMatch(ds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (StringValueMatch(ds , "ImageType", 2, "LOCALIZER"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	return cond0
def Condition_RescaleTypeIsPresentAndIsHUAndImageIsOriginalLocalizerAndNotMultienergyAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RescaleType"))
	cond0 = cond0  and (StringValueMatch(ds , "RescaleType", -1, "HU"))
	cond0 = cond0  and (StringValueMatch(ds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and (StringValueMatch(ds , "ImageType", 2, "LOCALIZER"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	return cond0
def Condition_KVPNotEmptyWhenAlsoPresentInMultienergyCTAcquisitionSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "KVP", -1, ""))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "KVP", "MultienergyCTAcquisitionSequence"))
	return cond0
def Condition_WindowCenterPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "WindowCenter"))
	return cond0
def Condition_WindowCenterNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "WindowCenter"))
	return cond0
def Condition_MonochromeAndWindowCenterNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "WindowCenter"))
	cond0 = cond0  and (BinaryValueMatch(rootds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 1))
	cond0 = cond0  and  not (ElementPresent(ds , "RedPaletteColorLookupTableDescriptor"))
	return cond0
def Condition_VOILUTSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "VOILUTSequence"))
	return cond0
def Condition_MonochromeAndVOILUTSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "VOILUTSequence"))
	cond0 = cond0  and (BinaryValueMatch(rootds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 1))
	cond0 = cond0  and  not (ElementPresent(ds , "RedPaletteColorLookupTableDescriptor"))
	return cond0
def Condition_NumberOfFramesPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfFrames"))
	return cond0
def Condition_ImageTypeValue3WholeBodyOrStatic(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "WHOLE BODY"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "STATIC"))
	return cond0
def Condition_ImageTypeValue3WholeBody(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "WHOLE BODY"))
	return cond0
def Condition_ImageTypeValue3Gated(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "GATED"))
	return cond0
def Condition_ImageTypeValue3Dynamic(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "DYNAMIC"))
	return cond0
def Condition_ImageTypeValue3Tomo(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "TOMO"))
	return cond0
def Condition_ImageTypeValue3GatedTomo(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "GATED TOMO"))
	return cond0
def Condition_ImageTypeValue3ReconTomo(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON TOMO"))
	return cond0
def Condition_ImageTypeValue3ReconGatedTomo(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON GATED TOMO"))
	return cond0
def Condition_ImageTypeValue3TomoFamily(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "GATED TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON TOMO"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RECON GATED TOMO"))
	return cond0
def Condition_ImageTypeValue4TransmissionAndNotTomo(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "STATIC"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "WHOLE BODY"))
	cond0 = cond0  and (StringValueMatch(ds , "ImageType", 3, "TRANSMISSION"))
	return cond0
def Condition_ImageTypeValue4Transmission(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 3, "TRANSMISSION"))
	return cond0
def Condition_FrameIncrementPointerContainsEnergyWindowVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0054,0x0010)))
	return cond0
def Condition_FrameIncrementPointerContainsDetectorVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0054,0x0020)))
	return cond0
def Condition_FrameIncrementPointerContainsPhaseVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0054,0x0030)))
	return cond0
def Condition_FrameIncrementPointerContainsRotationVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0054,0x0050)))
	return cond0
def Condition_FrameIncrementPointerContainsRRIntervalVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0054,0x0060)))
	return cond0
def Condition_FrameIncrementPointerContainsTimeSlotVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0054,0x0070)))
	return cond0
def Condition_FrameIncrementPointerContainsSliceVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0054,0x0080)))
	return cond0
def Condition_FrameIncrementPointerContainsAngularViewVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0054,0x0090)))
	return cond0
def Condition_FrameIncrementPointerContainsTimeSliceVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0054,0x0100)))
	return cond0
def Condition_FrameIncrementPointerContainsInstanceNumber(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0020,0x0013)))
	return cond0
def Condition_FrameIncrementPointerContainsImageTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0008,0x0033)))
	return cond0
def Condition_TriggerVectorIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TriggerVector"))
	return cond0
def Condition_FrameIncrementPointerContainsFrameTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x1063)))
	return cond0
def Condition_FrameIncrementPointerContainsFrameTimeVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x1065)))
	return cond0
def Condition_ImageTypeValue3BiplaneAOrB(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "BIPLANE A"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "BIPLANE B"))
	return cond0
def Condition_OneOverlayForBothPlanesOfBiplane(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "OverlayPlanes", -1, BinaryValueMatchOperator.Equals, 1))
	cond0 = cond0  and (StringValueMatch(ds , "ImageType", 2, "BIPLANE"))
	return cond0
def Condition_PositionerMotionDynamic(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PositionerMotion", -1, "DYNAMIC"))
	return cond0
def Condition_TableMotionDynamic(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TableMotion", -1, "DYNAMIC"))
	return cond0
def Condition_ExposureNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "Exposure"))
	return cond0
def Condition_XRayTubeCurrentAndExposureTimeNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "XRayTubeCurrent"))
	cond0 = cond0  and  not (ElementPresent(ds , "ExposureTime"))
	return cond0
def Condition_DeviceDiameterIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "DeviceDiameter"))
	return cond0
def Condition_ShutterShapeIsAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ShutterShape"))
	return cond0
def Condition_ShutterShapeIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ShutterShape"))
	return cond0
def Condition_ShutterShapeIsRectangular(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ShutterShape", -1, "RECTANGULAR"))
	return cond0
def Condition_ShutterShapeIsCircular(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ShutterShape", -1, "CIRCULAR"))
	return cond0
def Condition_ShutterShapeIsPolygonal(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ShutterShape", -1, "POLYGONAL"))
	return cond0
def Condition_CollimatorShapeIsRectangular(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CollimatorShape", -1, "RECTANGULAR"))
	return cond0
def Condition_CollimatorShapeIsCircular(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CollimatorShape", -1, "CIRCULAR"))
	return cond0
def Condition_CollimatorShapeIsPolygonal(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CollimatorShape", -1, "POLYGONAL"))
	return cond0
def Condition_MaskOperationIsTID(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "MaskOperation", -1, "TID"))
	return cond0
def Condition_MaskOperationIsAvgSub(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "MaskOperation", -1, "AVG_SUB"))
	return cond0
def Condition_NeedModuleFramePointers(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RepresentativeFrameNumber"))
	cond0 = cond0  or (ElementPresent(ds , "FrameNumbersOfInterest"))
	cond0 = cond0  or (ElementPresent(ds , "FrameOfInterestDescription"))
	return cond0
def Condition_NeedModuleMask(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "MaskSubtractionSequence"))
	cond0 = cond0  or (ElementPresent(ds , "RecommendedViewingMode"))
	return cond0
def Condition_NeedModuleDisplayShutter(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ShutterShape"))
	cond0 = cond0  and  not (StringValueMatch(ds , "ShutterShape", -1, "BITMAP"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterLeftVerticalEdge"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterRightVerticalEdge"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterUpperHorizontalEdge"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterLowerHorizontalEdge"))
	cond0 = cond0  or (ElementPresent(ds , "CenterOfCircularShutter"))
	cond0 = cond0  or (ElementPresent(ds , "RadiusOfCircularShutter"))
	cond0 = cond0  or (ElementPresent(ds , "VerticesOfThePolygonalShutter"))
	return cond0
def Condition_NeedModuleDevice(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "DeviceSequence"))
	return cond0
def Condition_NeedModuleIntervention(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "InterventionSequence"))
	return cond0
def Condition_NeedModuleXRayCollimator(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CollimatorShape"))
	return cond0
def Condition_NeedModuleXRayTable(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TableMotion"))
	cond0 = cond0  or (ElementPresent(ds , "TableAngle"))
	return cond0
def Condition_XRayNeedModuleModalityLUT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PixelIntensityRelationship", -1, "LOG"))
	return cond0
def Condition_NeedModuleBiplaneOverlay(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "OverlayPlanes"))
	cond0 = cond0  or (ElementPresent(ds , "OverlayPlaneOrigin"))
	return cond0
def Condition_NeedModuleXRayTomographyAcquisitionBasedOnScanOptions(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ScanOptions", -1, "TOMO"))
	return cond0
def Condition_NeedToCheckModuleXRayTomographyAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TomoLayerHeight"))
	return cond0
def Condition_NeedModuleFileMetaInformation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or GroupPresent(ds , "FileMetaInformationVersion")
	return cond0
def Condition_PrivateInformationCreatorUIDPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PrivateInformationCreatorUID"))
	return cond0
def Condition_NeedPixelComponentOrganization(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelComponentMask"))
	cond0 = cond0  or (ElementPresent(ds , "PixelComponentRangeStart"))
	cond0 = cond0  or (ElementPresent(ds , "PixelComponentRangeStop"))
	cond0 = cond0  or (ElementPresent(ds , "PixelComponentPhysicalUnits"))
	cond0 = cond0  or (ElementPresent(ds , "PixelComponentDataType"))
	cond0 = cond0  or (ElementPresent(ds , "NumberOfTableBreakPoints"))
	cond0 = cond0  or (ElementPresent(ds , "TableOfXBreakPoints"))
	cond0 = cond0  or (ElementPresent(ds , "TableOfYBreakPoints"))
	cond0 = cond0  or (ElementPresent(ds , "NumberOfTableEntries"))
	cond0 = cond0  or (ElementPresent(ds , "TableOfPixelValues"))
	cond0 = cond0  or (ElementPresent(ds , "TableOfParameterValues"))
	return cond0
def Condition_PixelComponentOrganizationPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelComponentOrganization"))
	return cond0
def Condition_PixelComponentOrganizationIs0Or1(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "PixelComponentOrganization", -1, BinaryValueMatchOperator.Equals, 0))
	cond0 = cond0  or (BinaryValueMatch(ds , "PixelComponentOrganization", -1, BinaryValueMatchOperator.Equals, 1))
	return cond0
def Condition_PixelComponentOrganizationIs0(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "PixelComponentOrganization", -1, BinaryValueMatchOperator.Equals, 0))
	return cond0
def Condition_PixelComponentOrganizationIs1(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "PixelComponentOrganization", -1, BinaryValueMatchOperator.Equals, 1))
	return cond0
def Condition_PixelComponentOrganizationIs2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "PixelComponentOrganization", -1, BinaryValueMatchOperator.Equals, 2))
	return cond0
def Condition_PixelComponentOrganizationIs3(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "PixelComponentOrganization", -1, BinaryValueMatchOperator.Equals, 3))
	return cond0
def Condition_PixelComponentOrganizationIs2Or3(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "PixelComponentOrganization", -1, BinaryValueMatchOperator.Equals, 2))
	cond0 = cond0  or (BinaryValueMatch(ds , "PixelComponentOrganization", -1, BinaryValueMatchOperator.Equals, 3))
	return cond0
def Condition_US8BitSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "RGB"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_FULL"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_FULL_422"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_PARTIAL_422"))
	return cond0
def Condition_US8Or16BitSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "PALETTE COLOR"))
	return cond0
def Condition_USNeedsColorByPlaneOrPixel(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "RGB"))
	return cond0
def Condition_USNeedsColorByPlane(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_FULL"))
	return cond0
def Condition_USNeedsColorByPixel(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_FULL_422"))
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_PARTIAL_422"))
	return cond0
def Condition_DirectorySOPInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "IMAGE"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "OVERLAY"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "MODALITY LUT"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "VOI LUT"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "CURVE"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "VISIT"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RESULTS"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "INTERPRETATION"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "STUDY COMPONENT"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "FILM SESSION"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "FILM BOX"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "IMAGE BOX"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "STORED PRINT"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RT DOSE"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RT STRUCTURE SET"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RT PLAN"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RT TREAT RECORD"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "PRESENTATION"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "WAVEFORM"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "SR DOCUMENT"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "KEY OBJECT DOC"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "SPECTROSCOPY"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RAW DATA"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "REGISTRATION"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "FIDUCIAL"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "ENCAP DOC"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "HL7 STRUC DOC"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "HANGING PROTOCOL"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "VALUE MAP"))
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "STEREOMETRIC"))
	return cond0
def Condition_DirectoryRecordTypeIsPatient(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "PATIENT"))
	return cond0
def Condition_DirectoryRecordTypeIsStudy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "STUDY"))
	return cond0
def Condition_DirectoryRecordTypeIsSeries(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "SERIES"))
	return cond0
def Condition_DirectoryRecordTypeIsImage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "IMAGE"))
	return cond0
def Condition_DirectoryRecordTypeIsOverlay(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "OVERLAY"))
	return cond0
def Condition_DirectoryRecordTypeIsModalityLUT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "MODALITY LUT"))
	return cond0
def Condition_DirectoryRecordTypeIsVOILUT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "VOI LUT"))
	return cond0
def Condition_DirectoryRecordTypeIsCurve(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "CURVE"))
	return cond0
def Condition_DirectoryRecordTypeIsTopic(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "TOPIC"))
	return cond0
def Condition_DirectoryRecordTypeIsVisit(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "VISIT"))
	return cond0
def Condition_DirectoryRecordTypeIsResults(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RESULTS"))
	return cond0
def Condition_DirectoryRecordTypeIsInterpretation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "INTERPRETATION"))
	return cond0
def Condition_DirectoryRecordTypeIsStudyComponent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "STUDY COMPONENT"))
	return cond0
def Condition_DirectoryRecordTypeIsPrintQueue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "PRINT QUEUE"))
	return cond0
def Condition_DirectoryRecordTypeIsFilmSession(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "FILM SESSION"))
	return cond0
def Condition_DirectoryRecordTypeIsFilmBox(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "FILM BOX"))
	return cond0
def Condition_DirectoryRecordTypeIsImageBox(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "IMAGE BOX"))
	return cond0
def Condition_DirectoryRecordTypeIsStoredPrint(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "STORED PRINT"))
	return cond0
def Condition_DirectoryRecordTypeIsRTDose(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RT DOSE"))
	return cond0
def Condition_DirectoryRecordTypeIsRTStructureSet(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RT STRUCTURE SET"))
	return cond0
def Condition_DirectoryRecordTypeIsRTPlan(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RT PLAN"))
	return cond0
def Condition_DirectoryRecordTypeIsRTTreatmentRecord(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RT TREAT RECORD"))
	return cond0
def Condition_DirectoryRecordTypeIsPresentation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "PRESENTATION"))
	return cond0
def Condition_DirectoryRecordTypeIsWaveform(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "WAVEFORM"))
	return cond0
def Condition_DirectoryRecordTypeIsSRDocument(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "SR DOCUMENT"))
	return cond0
def Condition_DirectoryRecordTypeIsKeyObjectDocument(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "KEY OBJECT DOC"))
	return cond0
def Condition_DirectoryRecordTypeIsSpectroscopy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "SPECTROSCOPY"))
	return cond0
def Condition_DirectoryRecordTypeIsRawData(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "RAW DATA"))
	return cond0
def Condition_DirectoryRecordTypeIsRegistration(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "REGISTRATION"))
	return cond0
def Condition_DirectoryRecordTypeIsFiducial(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "FIDUCIAL"))
	return cond0
def Condition_DirectoryRecordTypeIsEncapsulatedDocument(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "ENCAP DOC"))
	return cond0
def Condition_DirectoryRecordTypeIsHL7StructuredDocument(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "HL7 STRUC DOC"))
	return cond0
def Condition_DirectoryRecordTypeIsHangingProtocol(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "HANGING PROTOCOL"))
	return cond0
def Condition_DirectoryRecordTypeIsRealWorldValueMapping(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "VALUE MAP"))
	return cond0
def Condition_DirectoryRecordTypeIsStereometricRelationship(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "STEREOMETRIC"))
	return cond0
def Condition_DirectoryRecordTypeIsSurface(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "SURFACE"))
	return cond0
def Condition_DirectoryRecordTypeIsPrivate(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "PRIVATE"))
	return cond0
def Condition_DirectoryRecordTypeIsMRDR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DirectoryRecordType", -1, "MRDR"))
	return cond0
def Condition_ReferencedSOPInstanceUIDInFileIsNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedSOPInstanceUIDInFile"))
	return cond0
def Condition_NeedModuleRTPrescription(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PrescriptionDescription"))
	cond0 = cond0  or (ElementPresent(ds , "DoseReferenceSequence"))
	return cond0
def Condition_NeedModuleRTToleranceTables(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ToleranceTableSequence"))
	return cond0
def Condition_NeedModuleRTIonToleranceTables(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "IonToleranceTableSequence"))
	return cond0
def Condition_NeedModuleRTPatientSetup(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PatientSetupSequence"))
	return cond0
def Condition_NeedModuleRTFractionScheme(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FractionGroupSequence"))
	return cond0
def Condition_NeedRTBeams(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FractionGroupSequence"))
	cond0 = cond0  and (ElementPresent(ds , "NumberOfBeams"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfBeams", -1, BinaryValueMatchOperator.GreaterThan, 0))
	cond0 = cond0  or (ElementPresent(ds , "BeamSequence"))
	return cond0
def Condition_NeedRTIonBeams(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FractionGroupSequence"))
	cond0 = cond0  and (ElementPresent(ds , "NumberOfBeams"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfBeams", -1, BinaryValueMatchOperator.GreaterThan, 0))
	cond0 = cond0  or (ElementPresent(ds , "IonBeamSequence"))
	return cond0
def Condition_NeedRTBrachyApplicationSetups(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FractionGroupSequence"))
	cond0 = cond0  and (ElementPresent(ds , "NumberOfBrachyApplicationSetups"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfBrachyApplicationSetups", -1, BinaryValueMatchOperator.GreaterThan, 0))
	cond0 = cond0  or (ElementPresent(ds , "BrachyTreatmentTechnique"))
	cond0 = cond0  or (ElementPresent(ds , "BrachyTreatmentType"))
	cond0 = cond0  or (ElementPresent(ds , "TreatmentMachineSequence"))
	cond0 = cond0  or (ElementPresent(ds , "ApplicationSetupSequence"))
	return cond0
def Condition_DoseDataGridbased(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "InstanceNumber"))
	cond0 = cond0  or (ElementPresent(ds , "PixelSpacing"))
	cond0 = cond0  or (ElementPresent(ds , "ImageOrientationPatient"))
	cond0 = cond0  or (ElementPresent(ds , "ImagePositionPatient"))
	cond0 = cond0  or (ElementPresent(ds , "SliceThickness"))
	cond0 = cond0  or (ElementPresent(ds , "SamplesPerPixel"))
	cond0 = cond0  or (ElementPresent(ds , "PhotometricInterpretation"))
	cond0 = cond0  or (ElementPresent(ds , "Rows"))
	cond0 = cond0  or (ElementPresent(ds , "Columns"))
	cond0 = cond0  or (ElementPresent(ds , "BitsAllocated"))
	cond0 = cond0  or (ElementPresent(ds , "BitsStored"))
	cond0 = cond0  or (ElementPresent(ds , "HighBit"))
	cond0 = cond0  or (ElementPresent(ds , "PixelRepresentation"))
	cond0 = cond0  or (ElementPresent(ds , "PixelData"))
	return cond0
def Condition_DoseDataGridbasedAndNeedModuleMultiFrame(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or (ElementPresent(ds , "InstanceNumber"))
	cond1 = cond1  or (ElementPresent(ds , "PixelSpacing"))
	cond1 = cond1  or (ElementPresent(ds , "ImageOrientationPatient"))
	cond1 = cond1  or (ElementPresent(ds , "ImagePositionPatient"))
	cond1 = cond1  or (ElementPresent(ds , "SliceThickness"))
	cond1 = cond1  or (ElementPresent(ds , "SamplesPerPixel"))
	cond1 = cond1  or (ElementPresent(ds , "PhotometricInterpretation"))
	cond1 = cond1  or (ElementPresent(ds , "Rows"))
	cond1 = cond1  or (ElementPresent(ds , "Columns"))
	cond1 = cond1  or (ElementPresent(ds , "BitsAllocated"))
	cond1 = cond1  or (ElementPresent(ds , "BitsStored"))
	cond1 = cond1  or (ElementPresent(ds , "HighBit"))
	cond1 = cond1  or (ElementPresent(ds , "PixelRepresentation"))
	cond1 = cond1  or (ElementPresent(ds , "PixelData"))
	cond0 = cond0 or cond1
	cond1 = False
	cond1 = cond1  or (ElementPresent(ds , "NumberOfFrames"))
	cond1 = cond1  and (BinaryValueMatch(ds , "NumberOfFrames", -1, BinaryValueMatchOperator.GreaterThan, 1))
	cond0 = cond0 and cond1
	return cond0
def Condition_DoseDataPointsOrCurves(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "StructureSetLabel"))
	cond0 = cond0  or (ElementPresent(ds , "ROIContourSequence"))
	cond0 = cond0  or (ElementPresent(ds , "RTDoseROISequence"))
	return cond0
def Condition_NeedModuleRTDVH(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ReferencedStructureSetSequence"))
	cond0 = cond0  or (ElementPresent(ds , "DVHNormalizationPoint"))
	cond0 = cond0  or (ElementPresent(ds , "DVHNormalizationDoseValue"))
	cond0 = cond0  or (ElementPresent(ds , "DVHSequence"))
	return cond0
def Condition_ImageTypeValue3SimulatorOrPortal(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "SIMULATOR"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "PORTAL"))
	return cond0
def Condition_ImageTypeValue3SimulatorOrPortalOrRadiograph(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "SIMULATOR"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "PORTAL"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RADIOGRAPH"))
	return cond0
def Condition_ImageTypeValue3SimulatorOrRadiograph(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "SIMULATOR"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "RADIOGRAPH"))
	return cond0
def Condition_ImageTypeValue3Portal(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "PORTAL"))
	return cond0
def Condition_ImageTypeValue3Fluence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "FLUENCE"))
	return cond0
def Condition_RTImagePlaneIsNonNormal(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "RTImagePlane", -1, "NON_NORMAL"))
	return cond0
def Condition_NeedExposureSequenceReferencedFrameNumber(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfFrames"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfFrames", -1, BinaryValueMatchOperator.GreaterThan, 1))
	return cond0
def Condition_RTBeamLimitingDeviceTypeMLCXOrMLCY(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "RTBeamLimitingDeviceType", -1, "MLCX"))
	cond0 = cond0  or (StringValueMatch(ds , "RTBeamLimitingDeviceType", -1, "MLCY"))
	return cond0
def Condition_NumberOfBlocksNotZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfBlocks"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfBlocks", -1, BinaryValueMatchOperator.GreaterThan, 0))
	return cond0
def Condition_NumberOfRangeShiftersNotZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfRangeShifters"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfRangeShifters", -1, BinaryValueMatchOperator.GreaterThan, 0))
	return cond0
def Condition_NumberOfLateralSpreadingDevicesNotZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfLateralSpreadingDevices"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfLateralSpreadingDevices", -1, BinaryValueMatchOperator.GreaterThan, 0))
	return cond0
def Condition_NumberOfRangeModulatorsNotZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfRangeModulators"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfRangeModulators", -1, BinaryValueMatchOperator.GreaterThan, 0))
	return cond0
def Condition_NumberOfBeamsNotZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfBeams"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfBeams", -1, BinaryValueMatchOperator.GreaterThan, 0))
	return cond0
def Condition_NumberOfBrachyApplicationSetupsNotZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfBrachyApplicationSetups"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfBrachyApplicationSetups", -1, BinaryValueMatchOperator.GreaterThan, 0))
	return cond0
def Condition_NumberOfWedgesNotZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfWedges"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfWedges", -1, BinaryValueMatchOperator.GreaterThan, 0))
	return cond0
def Condition_NumberOfCompensatorsNotZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfCompensators"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfCompensators", -1, BinaryValueMatchOperator.GreaterThan, 0))
	return cond0
def Condition_NeedSourceToCompensatorDistance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "MaterialID"))
	cond0 = cond0  and (ValuePresent(ds , "MaterialID", -1))
	cond0 = cond0  and (ElementPresent(ds , "CompensatorMountingPosition"))
	cond0 = cond0  and (StringValueMatch(ds , "CompensatorMountingPosition", -1, "DOUBLE_SIDED"))
	return cond0
def Condition_NeedIsocenterToCompensatorDistance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "MaterialID"))
	cond0 = cond0  and (ValuePresent(ds , "MaterialID", -1))
	cond0 = cond0  and (ElementPresent(ds , "CompensatorMountingPosition"))
	cond0 = cond0  and (StringValueMatch(ds , "CompensatorMountingPosition", -1, "DOUBLE_SIDED"))
	return cond0
def Condition_NumberOfBoliNotZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfBoli"))
	cond0 = cond0  and (BinaryValueMatch(ds , "NumberOfBoli", -1, BinaryValueMatchOperator.GreaterThan, 0))
	return cond0
def Condition_PixelDataPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelData"))
	return cond0
def Condition_FloatPixelDataPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FloatPixelData"))
	return cond0
def Condition_DoubleFloatPixelDataPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "DoubleFloatPixelData"))
	return cond0
def Condition_NeedReferencedRTPlanSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "PLAN"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "MULTI_PLAN"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "FRACTION"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BEAM"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BRACHY"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "FRACTION_SESSION"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BEAM_SESSION"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BRACHY_SESSION"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "CONTROL_POINT"))
	return cond0
def Condition_NeedReferencedFractionGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "FRACTION"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BEAM"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BRACHY"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "FRACTION_SESSION"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BEAM_SESSION"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BRACHY_SESSION"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "CONTROL_POINT"))
	return cond0
def Condition_NeedReferencedBeamSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BEAM"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BEAM_SESSION"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "CONTROL_POINT"))
	return cond0
def Condition_DoseSummationTypeControlPoint(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "CONTROL_POINT"))
	return cond0
def Condition_NeedReferencedBrachyApplicationSetupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BRACHY"))
	cond0 = cond0  or (StringValueMatch(rootds , "DoseSummationType", -1, "BRACHY_SESSION"))
	return cond0
def Condition_NeedGridFrameOffsetVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x3004,0x000C)))
	return cond0
def Condition_RTPlanGeometryIsPatient(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "RTPlanGeometry", -1, "PATIENT"))
	return cond0
def Condition_PlanIntentIsVerification(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PlanIntent", -1, "VERIFICATION"))
	return cond0
def Condition_DoseReferenceStructureTypePointOrVolume(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DoseReferenceStructureType", -1, "POINT"))
	cond0 = cond0  or (StringValueMatch(ds , "DoseReferenceStructureType", -1, "VOLUME"))
	return cond0
def Condition_DoseReferenceStructureTypeCoordinates(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DoseReferenceStructureType", -1, "COORDINATES"))
	return cond0
def Condition_PatientAdditionalPositionNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PatientAdditionalPosition"))
	return cond0
def Condition_PatientPositionNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PatientPosition"))
	return cond0
def Condition_BrachyTreatmentTypePDR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "BrachyTreatmentType", -1, "PDR"))
	return cond0
def Condition_SourceApplicatorNumberPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SourceApplicatorNumber"))
	return cond0
def Condition_SourceMovementTypeStepwise(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SourceMovementType", -1, "STEPWISE"))
	return cond0
def Condition_TransferTubeNumberNotNull(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TransferTubeNumber"))
	cond0 = cond0  and (ValuePresent(ds , "TransferTubeNumber", -1))
	return cond0
def Condition_ApprovalStatusApprovedOrRejected(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ApprovalStatus", -1, "APPROVED"))
	cond0 = cond0  or (StringValueMatch(ds , "ApprovalStatus", -1, "REJECTED"))
	return cond0
def Condition_NeedReferencedFrameNumberInContourImageSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	return cond0
def Condition_NeedModuleRTTreatmentSummaryRecord(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CurrentTreatmentStatus"))
	return cond0
def Condition_NeedModuleCalculatedDoseReferenceRecord(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CalculatedDoseReferenceSequence"))
	return cond0
def Condition_NeedModuleMeasuredDoseReferenceRecord(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "MeasuredDoseReferenceSequence"))
	return cond0
def Condition_MeasuredDoseReferenceNumberNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "MeasuredDoseReferenceNumber"))
	return cond0
def Condition_ReferencedMeasuredDoseReferenceNumberNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedMeasuredDoseReferenceNumber"))
	return cond0
def Condition_ReferencedDoseReferenceNumberNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedDoseReferenceNumber"))
	return cond0
def Condition_ReferencedCalculatedDoseReferenceNumberNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedCalculatedDoseReferenceNumber"))
	return cond0
def Condition_CalculatedDoseReferenceNumberNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "CalculatedDoseReferenceNumber"))
	return cond0
def Condition_NominalBeamEnergyIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NominalBeamEnergy"))
	return cond0
def Condition_BrachyTreatmentTypeIsPDR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "BrachyTreatmentType", -1, "PDR"))
	return cond0
def Condition_TransferTubeNumberIsNotEmpty(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ValuePresent(ds , "TransferTubeNumber", -1))
	return cond0
def Condition_SourceIsNotGammaEmitter(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "ReferenceAirKermaRate", -1, BinaryValueMatchOperator.Equals, 0))
	return cond0
def Condition_NeedModulePETMultigatedAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SeriesType", 0, "GATED"))
	return cond0
def Condition_PETSeriesType2Reprojection(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SeriesType", 1, "REPROJECTION"))
	return cond0
def Condition_PETSeriesType1Gated(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SeriesType", 0, "GATED"))
	return cond0
def Condition_PETSeriesType1Dynamic(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SeriesType", 0, "DYNAMIC"))
	return cond0
def Condition_PETSeriesType1GatedAndBeatRejection(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SeriesType", 0, "DYNAMIC"))
	cond0 = cond0  and (ElementPresent(ds , "BeatRejectionFlag"))
	cond0 = cond0  and (StringValueMatch(ds , "BeatRejectionFlag", -1, "Y"))
	return cond0
def Condition_DecayCorrectionNotNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "DecayCorrection"))
	cond0 = cond0  and  not (StringValueMatch(ds , "DecayCorrection", -1, "NONE"))
	return cond0
def Condition_TypeOfDataIsBloodSample(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TypeOfData"))
	cond0 = cond0  and (StringValueMatch(ds , "TypeOfData", -1, "BLDSMPL"))
	return cond0
def Condition_AxisUnitsIncludesCounts(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TypeOfData", -1, "CNTS"))
	cond0 = cond0  or (StringValueMatch(ds , "TypeOfData", -1, "CPS"))
	return cond0
def Condition_NeedModuleXRayAcquisitionDose(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "KVP"))
	cond0 = cond0  or (ElementPresent(ds , "XRayTubeCurrent"))
	cond0 = cond0  or (ElementPresent(ds , "XRayTubeCurrentInuA"))
	cond0 = cond0  or (ElementPresent(ds , "XRayTubeCurrentInmA"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureTime"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureTimeInuS"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureTimeInms"))
	cond0 = cond0  or (ElementPresent(ds , "Exposure"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureInuAs"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureInmAs"))
	cond0 = cond0  or (ElementPresent(ds , "DistanceSourceToDetector"))
	cond0 = cond0  or (ElementPresent(ds , "DistanceSourceToPatient"))
	cond0 = cond0  or (ElementPresent(ds , "ImageAndFluoroscopyAreaDoseProduct"))
	cond0 = cond0  or (ElementPresent(ds , "BodyPartThickness"))
	cond0 = cond0  or (ElementPresent(ds , "EntranceDose"))
	cond0 = cond0  or (ElementPresent(ds , "ExposedArea"))
	cond0 = cond0  or (ElementPresent(ds , "DistanceSourceToEntrance"))
	cond0 = cond0  or (ElementPresent(ds , "CommentsOnRadiationDose"))
	cond0 = cond0  or (ElementPresent(ds , "XRayOutput"))
	cond0 = cond0  or (ElementPresent(ds , "HalfValueLayer"))
	cond0 = cond0  or (ElementPresent(ds , "OrganDose"))
	cond0 = cond0  or (ElementPresent(ds , "OrganExposed"))
	cond0 = cond0  or (ElementPresent(ds , "AnodeTargetMaterial"))
	cond0 = cond0  or (ElementPresent(ds , "FilterMaterial"))
	cond0 = cond0  or (ElementPresent(ds , "FilterThicknessMaximum"))
	cond0 = cond0  or (ElementPresent(ds , "FilterThicknessMinimum"))
	cond0 = cond0  or (ElementPresent(ds , "RectificationType"))
	return cond0
def Condition_NeedModuleXRayGeneration(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "KVP"))
	cond0 = cond0  or (ElementPresent(ds , "XRayTubeCurrent"))
	cond0 = cond0  or (ElementPresent(ds , "XRayTubeCurrentInuA"))
	cond0 = cond0  or (ElementPresent(ds , "XRayTubeCurrentInmA"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureTime"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureTimeInuS"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureTimeInms"))
	cond0 = cond0  or (ElementPresent(ds , "Exposure"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureInuAs"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureInmAs"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureControlMode"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureControlModeDescription"))
	cond0 = cond0  or (ElementPresent(ds , "ExposureStatus"))
	cond0 = cond0  or (ElementPresent(ds , "PhototimerSetting"))
	cond0 = cond0  or (ElementPresent(ds , "FocalSpots"))
	cond0 = cond0  or (ElementPresent(ds , "AnodeTargetMaterial"))
	cond0 = cond0  or (ElementPresent(ds , "RectificationType"))
	return cond0
def Condition_XRayTubeCurrentInmAIsPresentAndOthersAreNot(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "XRayTubeCurrentInmA"))
	cond0 = cond0  and  not (ValuePresent(ds , "XRayTubeCurrent", -1))
	cond0 = cond0  and  not (ValuePresent(ds , "XRayTubeCurrentInuA", -1))
	return cond0
def Condition_ExposureTimeInmsIsPresentAndOthersAreNot(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ExposureTimeInms"))
	cond0 = cond0  and  not (ValuePresent(ds , "ExposureTime", -1))
	cond0 = cond0  and  not (ValuePresent(ds , "ExposureTimeInuS", -1))
	return cond0
def Condition_ExposureInmAsIsPresentAndOthersAreNot(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ExposureInmAs"))
	cond0 = cond0  and  not (ValuePresent(ds , "Exposure", -1))
	cond0 = cond0  and  not (ValuePresent(ds , "ExposureInuAs", -1))
	return cond0
def Condition_NeedModuleXRayFiltration(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FilterType"))
	cond0 = cond0  or (ElementPresent(ds , "FilterMaterial"))
	cond0 = cond0  or (ElementPresent(ds , "FilterThicknessMaximum"))
	cond0 = cond0  or (ElementPresent(ds , "FilterThicknessMinimum"))
	return cond0
def Condition_NeedModuleDXPositioning(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ProjectionEponymousNameCodeSequence"))
	cond0 = cond0  or (ElementPresent(ds , "PatientPosition"))
	cond0 = cond0  or (ElementPresent(ds , "ViewPosition"))
	cond0 = cond0  or (ElementPresent(ds , "ViewCodeSequence"))
	cond0 = cond0  or (ElementPresent(ds , "ViewModifierCodeSequence"))
	cond0 = cond0  or (ElementPresent(ds , "PatientOrientationCodeSequence"))
	cond0 = cond0  or (ElementPresent(ds , "EstimatedRadiographicMagnificationFactor"))
	cond0 = cond0  or (ElementPresent(ds , "PositionerType"))
	cond0 = cond0  or (ElementPresent(ds , "DetectorPrimaryAngle"))
	cond0 = cond0  or (ElementPresent(ds , "DetectorSecondaryAngle"))
	cond0 = cond0  or (ElementPresent(ds , "ColumnAngulation"))
	cond0 = cond0  or (ElementPresent(ds , "TableAngle"))
	return cond0
def Condition_NeedModuleXRayGrid(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "Grid"))
	cond0 = cond0  or (ElementPresent(ds , "GridAbsorbingMaterial"))
	cond0 = cond0  or (ElementPresent(ds , "GridSpacingMaterial"))
	cond0 = cond0  or (ElementPresent(ds , "GridThickness"))
	cond0 = cond0  or (ElementPresent(ds , "GridPitch"))
	cond0 = cond0  or (ElementPresent(ds , "GridAspectRatio"))
	cond0 = cond0  or (ElementPresent(ds , "GridPeriod"))
	cond0 = cond0  or (ElementPresent(ds , "GridFocalDistance"))
	return cond0
def Condition_DXNeedModuleVOILUT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PresentationIntentType", -1, "FOR PRESENTATION"))
	return cond0
def Condition_NeedModuleImageHistogram(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "HistogramSequence"))
	return cond0
def Condition_ImageLateralityNotSent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ImageLaterality"))
	return cond0
def Condition_SeriesNeedReferencedPerformedProcedureStepSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ReferencedPerformedProcedureStepSequence"))
	return cond0
def Condition_CodingSchemeDesignatorisSNM3(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "SNM3"))
	return cond0
def Condition_ForPresentationAndWindowCenterNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PresentationIntentType", -1, "FOR PRESENTATION"))
	cond0 = cond0  and  not (ElementPresent(ds , "WindowCenter"))
	return cond0
def Condition_ForPresentationAndVOILUTSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PresentationIntentType", -1, "FOR PRESENTATION"))
	cond0 = cond0  and  not (ElementPresent(ds , "VOILUTSequence"))
	return cond0
def Condition_FieldOfViewRotationOrFieldOfViewHorizontalFlipPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FieldOfViewRotation"))
	cond0 = cond0  or (ElementPresent(ds , "FieldOfViewHorizontalFlip"))
	return cond0
def Condition_FieldOfViewRotationPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FieldOfViewRotation"))
	return cond0
def Condition_FieldOfViewHorizontalFlipPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FieldOfViewHorizontalFlip"))
	return cond0
def Condition_NoPrimaryAnatomicStructureSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentAbove(parentds , "PrimaryAnatomicStructureSequence"))
	return cond0
def Condition_NoAnatomicRegionModifierSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentWithin(ds , "AnatomicRegionModifierSequence", "AnatomicRegionSequence"))
	return cond0
def Condition_NeedModuleSoftcopyVOILUT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SoftcopyVOILUTSequence"))
	return cond0
def Condition_RequireTextObjectSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TextObjectSequence"))
	cond0 = cond0  or  not (ElementPresent(ds , "GraphicObjectSequence"))
	return cond0
def Condition_RequireGraphicObjectSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "GraphicObjectSequence"))
	cond0 = cond0  or  not (ElementPresent(ds , "TextObjectSequence"))
	return cond0
def Condition_BoundingBoxTopLeftHandCornerPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "BoundingBoxTopLeftHandCorner"))
	return cond0
def Condition_BoundingBoxTopLeftHandCornerOrBottomRightHandCornerPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "BoundingBoxTopLeftHandCorner"))
	cond0 = cond0  or (ElementPresent(ds , "BoundingBoxBottomRightHandCorner"))
	return cond0
def Condition_BoundingBoxTopLeftHandCornerOrBottomRightHandCornerNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "BoundingBoxTopLeftHandCorner"))
	cond0 = cond0  and  not (ElementPresent(ds , "BoundingBoxBottomRightHandCorner"))
	return cond0
def Condition_AnchorPointNeeded(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "BoundingBoxTopLeftHandCorner"))
	cond0 = cond0  and  not (ElementPresent(ds , "BoundingBoxBottomRightHandCorner"))
	return cond0
def Condition_AnchorPointPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "AnchorPoint"))
	return cond0
def Condition_AnchorPointNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "AnchorPoint"))
	return cond0
def Condition_BoundingBoxNeeded(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "BoundingBoxTopLeftHandCorner"))
	cond0 = cond0  or (ElementPresent(ds , "BoundingBoxBottomRightHandCorner"))
	cond0 = cond0  or  not (ElementPresent(ds , "AnchorPoint"))
	return cond0
def Condition_PresentationLUTShapeNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PresentationLUTShape"))
	return cond0
def Condition_PresentationLUTSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PresentationLUTSequence"))
	return cond0
def Condition_DisplayOrBitmapDisplayShutterModulePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ShutterShape"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterLeftVerticalEdge"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterRightVerticalEdge"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterUpperHorizontalEdge"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterLowerHorizontalEdge"))
	cond0 = cond0  or (ElementPresent(ds , "CenterOfCircularShutter"))
	cond0 = cond0  or (ElementPresent(ds , "RadiusOfCircularShutter"))
	cond0 = cond0  or (ElementPresent(ds , "VerticesOfThePolygonalShutter"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterPresentationValue"))
	cond0 = cond0  or (ElementPresent(ds , "ShutterOverlayGroup"))
	return cond0
def Condition_DisplayOrBitmapDisplayShutterModulePresentAndNotGrayscaleSoftcopyPresentationState(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, GrayscaleSoftcopyPresentationStateStorageSOPClassUID))
	cond0 = cond0  and (ElementPresent(ds , "ShutterShape"))
	return cond0
def Condition_MaskModulePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "MaskSubtractionSequence"))
	cond0 = cond0  or (ElementPresent(ds , "RecommendedViewingMode"))
	return cond0
def Condition_NeedModuleBitmapDisplayShutter(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ShutterShape", -1, "BITMAP"))
	return cond0
def Condition_NeedModuleOverlayActivation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "OverlayActivationLayer"))
	cond0 = cond0  or (ElementPresent(ds , "CurveActivationLayer"))
	return cond0
def Condition_NeedModuleGraphicAnnotation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "GraphicAnnotationSequence"))
	return cond0
def Condition_NeedModuleSpatialTransformation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ImageRotation"))
	cond0 = cond0  or (ElementPresent(ds , "ImageHorizontalFlip"))
	return cond0
def Condition_NeedModuleGraphicLayer(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "GraphicLayerSequence"))
	return cond0
def Condition_ImageTypeValue3StereoLOrR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "STEREO L"))
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "STEREO R"))
	return cond0
def Condition_RequirePresentationPixelSpacing(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PresentationSizeMode", -1, "TRUE SIZE"))
	cond0 = cond0  or  not (ElementPresent(ds , "PresentationPixelAspectRatio"))
	return cond0
def Condition_RequirePresentationPixelAspectRatio(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PresentationPixelSpacing"))
	return cond0
def Condition_RequirePresentationPixelMagnificationRatio(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PresentationSizeMode", -1, "MAGNIFY"))
	return cond0
def Condition_VerificationFlagIsVerified(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "VerificationFlag", -1, "VERIFIED"))
	return cond0
def Condition_VerificationFlagIsVerifiedAndCompletionFlagIsNotComplete(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "CompletionFlag", -1, "COMPLETE"))
	cond0 = cond0  and (StringValueMatch(ds , "VerificationFlag", -1, "VERIFIED"))
	return cond0
def Condition_TemplateExtensionFlagIsY(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TemplateExtensionFlag", -1, "Y"))
	return cond0
def Condition_ValueTypeIsText(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "TEXT"))
	return cond0
def Condition_ValueTypeIsNum(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "NUM"))
	return cond0
def Condition_ValueTypeIsNumeric(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "NUMERIC"))
	return cond0
def Condition_ValueTypeIsCode(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "CODE"))
	return cond0
def Condition_ValueTypeIsDateTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "DATETIME"))
	return cond0
def Condition_ValueTypeIsDate(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "DATE"))
	return cond0
def Condition_ValueTypeIsTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "TIME"))
	return cond0
def Condition_ValueTypeIsPersonName(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "PNAME"))
	return cond0
def Condition_ValueTypeIsUID(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "UIDREF"))
	return cond0
def Condition_NeedConceptName(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "TEXT"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "NUM"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "CODE"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "DATETIME"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "DATE"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "TIME"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "PNAME"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "UIDREF"))
	return cond0
def Condition_ValueTypeIsTextOrNumericOrCodeOrDateTimeOrDateOrTimeOrPersonNameOrUIDOrContainer(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "TEXT"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "NUM"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "CODE"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "DATETIME"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "DATE"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "TIME"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "PNAME"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "UIDREF"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "CONTAINER"))
	return cond0
def Condition_ValueTypeIsImage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "IMAGE"))
	return cond0
def Condition_ValueTypeIsWaveform(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "WAVEFORM"))
	return cond0
def Condition_ValueTypeIsComposite(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "COMPOSITE"))
	return cond0
def Condition_ValueTypeIsCompositeOrImage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "COMPOSITE"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "IMAGE"))
	return cond0
def Condition_ValueTypeIsCompositeOrImageOrWaveform(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "COMPOSITE"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "IMAGE"))
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "WAVEFORM"))
	return cond0
def Condition_ValueTypeIsSpatialCoordinates(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "SCOORD"))
	return cond0
def Condition_ValueTypeIsSpatialCoordinates3D(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "SCOORD3D"))
	return cond0
def Condition_ValueTypeIsTemporalCoordinates(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "TCOORD"))
	return cond0
def Condition_NoReferencedDateTimeOrReferencedTimeOffsets(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedDateTime"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedTimeOffsets"))
	return cond0
def Condition_NoReferencedDateTimeOrReferencedSamplePositions(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedSamplePositions"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedDateTime"))
	return cond0
def Condition_NoReferencedTimeOffsetsOrReferencedSamplePositions(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedSamplePositions"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedTimeOffsets"))
	return cond0
def Condition_ValueTypeIsContainer(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ValueType", -1, "CONTAINER"))
	return cond0
def Condition_RelationshipByReference(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ValueType"))
	cond0 = cond0  and (ElementPresent(ds , "ReferencedContentItemIdentifier"))
	cond0 = cond0  and  not (StringValueMatch(ds , "RelationshipType", -1, "CONTAINS"))
	return cond0
def Condition_RelationshipByValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ValueType"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedContentItemIdentifier"))
	return cond0
def Condition_NeedModuleWaveformAnnotation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "WaveformAnnotationSequence"))
	return cond0
def Condition_ReallyNeedModuleSynchronization(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "WaveformOriginality", -1, "ORIGINAL"))
	cond0 = cond0  or (ElementPresent(ds , "SynchronizationFrameOfReferenceUID"))
	cond0 = cond0  or (ElementPresent(ds , "SynchronizationTrigger"))
	cond0 = cond0  or (ElementPresent(ds , "TriggerSourceOrType"))
	cond0 = cond0  or (ElementPresent(ds , "SynchronizationChannel"))
	cond0 = cond0  or (ElementPresent(ds , "AcquisitionTimeSynchronized"))
	cond0 = cond0  or (ElementPresent(ds , "TimeSource"))
	cond0 = cond0  or (ElementPresent(ds , "TimeDistributionProtocol"))
	return cond0
def Condition_NeedModuleSynchronizationForIVUS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Modality", -1, "IVUS"))
	cond0 = cond0  or (ElementPresent(ds , "SynchronizationFrameOfReferenceUID"))
	cond0 = cond0  or (ElementPresent(ds , "SynchronizationTrigger"))
	cond0 = cond0  or (ElementPresent(ds , "TriggerSourceOrType"))
	cond0 = cond0  or (ElementPresent(ds , "SynchronizationChannel"))
	cond0 = cond0  or (ElementPresent(ds , "AcquisitionTimeSynchronized"))
	cond0 = cond0  or (ElementPresent(ds , "TimeSource"))
	cond0 = cond0  or (ElementPresent(ds , "TimeDistributionProtocol"))
	return cond0
def Condition_NeedToCheckModuleSynchronization(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SynchronizationFrameOfReferenceUID"))
	cond0 = cond0  or (ElementPresent(ds , "SynchronizationTrigger"))
	cond0 = cond0  or (ElementPresent(ds , "TriggerSourceOrType"))
	cond0 = cond0  or (ElementPresent(ds , "SynchronizationChannel"))
	cond0 = cond0  or (ElementPresent(ds , "AcquisitionTimeSynchronized"))
	cond0 = cond0  or (ElementPresent(ds , "TimeSource"))
	cond0 = cond0  or (ElementPresent(ds , "TimeDistributionProtocol"))
	return cond0
def Condition_AcquisitionTimeSynchronizedIsY(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionTimeSynchronized", -1, "Y"))
	return cond0
def Condition_ChannelSensitivityIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ChannelSensitivity"))
	return cond0
def Condition_ChannelSampleSkewNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ChannelSampleSkew"))
	return cond0
def Condition_ChannelTimeSkewNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ChannelTimeSkew"))
	return cond0
def Condition_AnnotationNeedsReferencedSamplePositions(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TemporalRangeType"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedTimeOffsets"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedDateTime"))
	return cond0
def Condition_AnnotationNeedsReferencedTimeOffsets(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TemporalRangeType"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedSamplePositions"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedDateTime"))
	return cond0
def Condition_AnnotationNeedsReferencedDateTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TemporalRangeType"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedSamplePositions"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedTimeOffsets"))
	return cond0
def Condition_NeedModuleCineForSC(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x1063)))
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x1065)))
	return cond0
def Condition_FrameIncrementPointerContainsPageNumberVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x2001)))
	return cond0
def Condition_FrameIncrementPointerContainsFrameLabelVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x2002)))
	return cond0
def Condition_FrameIncrementPointerContainsFramePrimaryAngleVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x2003)))
	return cond0
def Condition_FrameIncrementPointerContainsFrameSecondaryAngleVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x2004)))
	return cond0
def Condition_FrameIncrementPointerContainsSliceLocationVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x2005)))
	return cond0
def Condition_FrameIncrementPointerContainsDisplayWindowLabelVector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "FrameIncrementPointer", -1, Tag(0x0018,0x2006)))
	return cond0
def Condition_MonochromeNotBitmapPhotometricInterpretation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	cond0 = cond0  and (BinaryValueMatch(ds , "BitsStored", -1, BinaryValueMatchOperator.GreaterThan, 1))
	return cond0
def Condition_ConversionTypeDigitizedFilm(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ConversionType", -1, "DF"))
	return cond0
def Condition_NotSCMultiFrameOrNumberOfFramesGreaterThanOne(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.7.1"))
	cond0 = cond0  and  not (StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.7.2"))
	cond0 = cond0  and  not (StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.7.3"))
	cond0 = cond0  and  not (StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.7.4"))
	cond0 = cond0 or(BinaryValueMatch(ds , "NumberOfFrames", -1, BinaryValueMatchOperator.GreaterThan, 1))
	return cond0
def Condition_ModalityIsIVUS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Modality", -1, "IVUS"))
	return cond0
def Condition_IVUSAcquisitionIsMotor(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "IVUSAcquisition", -1, "MOTOR_PULLBACK"))
	return cond0
def Condition_IVUSAcquisitionIsGated(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "IVUSAcquisition", -1, "GATED_PULLBACK"))
	return cond0
def Condition_IVUSAcquisitionIsMotorOrGated(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "IVUSAcquisition", -1, "MOTOR_PULLBACK"))
	cond0 = cond0 or(StringValueMatch(ds , "IVUSAcquisition", -1, "GATED_PULLBACK"))
	return cond0
def Condition_CertifiedTimestampIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CertifiedTimestamp"))
	return cond0
def Condition_NeedModuleMRPulseSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PulseSequenceName"))
	cond0 = cond0 or(ElementPresent(ds , "MRAcquisitionType"))
	cond0 = cond0 or(StringValueMatch(ds , "ImageType", 0, "ORIGINAL"))
	return cond0
def Condition_NeedModuleMRSpectroscopyPulseSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PulseSequenceName"))
	cond0 = cond0 or(ElementPresent(ds , "MRSpectroscopyAcquisitionType"))
	cond0 = cond0 or(StringValueMatch(ds , "ImageType", 0, "ORIGINAL"))
	return cond0
def Condition_NeedModuleCardiacSynchronization(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CardiacSynchronizationTechnique"))
	return cond0
def Condition_NeedModuleRespiratorySynchronization(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RespiratoryMotionCompensationTechnique"))
	return cond0
def Condition_NeedModuleBulkMotion(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "BulkMotionCompensationTechnique"))
	return cond0
def Condition_NeedModuleSupplementalPaletteColorLUT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PixelPresentation", -1, "COLOR"))
	cond0 = cond0 or(StringValueMatch(ds , "PixelPresentation", -1, "MIXED"))
	return cond0
def Condition_StackIDIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "StackID"))
	return cond0
def Condition_NeedRealWorldValueFirstValueMapped(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelData"))
	cond0 = cond0 or(ElementPresent(ds , "RealWorldValueLUTData"))
	cond0 = cond0 or not (ElementPresent(ds , "DoubleFloatRealWorldValueFirstValueMapped"))
	return cond0
def Condition_NeedRealWorldValueLastValueMapped(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelData"))
	cond0 = cond0 or(ElementPresent(ds , "RealWorldValueLUTData"))
	cond0 = cond0 or not (ElementPresent(ds , "DoubleFloatRealWorldValueLastValueMapped"))
	return cond0
def Condition_NeedDoubleFloatRealWorldValueFirstValueMapped(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "RealWorldValueFirstValueMapped"))
	return cond0
def Condition_NeedDoubleFloatRealWorldValueLastValueMapped(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "RealWorldValueLastValueMapped"))
	return cond0
def Condition_NeedRealWorldValueSlopeAndIntercept(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FloatPixelData"))
	cond0 = cond0 or(ElementPresent(ds , "DoubleFloatPixelData"))
	cond0 = cond0 or not (ElementPresent(ds , "RealWorldValueLUTData"))
	return cond0
def Condition_RealWorldValueLUTDataNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "RealWorldValueLUTData"))
	return cond0
def Condition_RealWorldValueInterceptNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "RealWorldValueIntercept"))
	return cond0
def Condition_CardiacSynchronizationTechniqueNotNoneAndOriginalOrMixed(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (ElementPresent(ds , "CardiacSynchronizationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "NONE"))
	return cond0
def Condition_CardiacSynchronizationTechniqueProspectiveOrRetrospective(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "PROSPECTIVE"))
	cond0 = cond0 or(StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "RETROSPECTIVE"))
	return cond0
def Condition_RespiratoryMotionCompensationTechniqueNotNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RespiratoryMotionCompensationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(ds , "RespiratoryMotionCompensationTechnique", -1, "NONE"))
	return cond0
def Condition_RespiratoryMotionCompensationTechniqueNotNoneOrRealTimeOrBreathHoldAndOriginalOrMixed(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (ElementPresent(ds , "RespiratoryMotionCompensationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(ds , "RespiratoryMotionCompensationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (StringValueMatch(ds , "RespiratoryMotionCompensationTechnique", -1, "BREATH_HOLD"))
	cond0 = cond0  and  not (StringValueMatch(ds , "RespiratoryMotionCompensationTechnique", -1, "REALTIME"))
	return cond0
def Condition_BulkMotionCompensationTechniqueNotNoneAndOriginalOrMixed(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (ElementPresent(ds , "BulkMotionCompensationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(ds , "BulkMotionCompensationTechnique", -1, "NONE"))
	return cond0
def Condition_ImageTypeValue1Original(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	return cond0
def Condition_ImageTypeValue1Derived(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	return cond0
def Condition_ImageTypeValue1NotDerived(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	return cond0
def Condition_ImageTypeValue1OriginalOrMixed(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "MIXED"))
	return cond0
def Condition_ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedOrWholeSlide(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedCTImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedMRImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedPETImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, VLWholeSlideMicroscopyImageStorageSOPClassUID))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "MIXED"))
	cond0 = cond0 and cond1
	return cond0
def Condition_ImageTypeValue1OriginalOrMixedAndNotLegacyConverted(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedCTImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedMRImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedPETImageStorageSOPClassUID))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "MIXED"))
	cond0 = cond0 and cond1
	return cond0
def Condition_ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedMR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedMRImageStorageSOPClassUID))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "MIXED"))
	cond0 = cond0 and cond1
	return cond0
def Condition_ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedCT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedCTImageStorageSOPClassUID))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "MIXED"))
	cond0 = cond0 and cond1
	return cond0
def Condition_ImageTypeValue1OriginalAndNotLegacyConvertedPET(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, LegacyConvertedEnhancedPETImageStorageSOPClassUID))
	return cond0
def Condition_ImageTypeValue1OriginalOrMixedAndRectilinear(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "GeometryOfKSpaceTraversal", -1, "RECTILINEAR"))
	return cond0
def Condition_ImageTypeValue1OriginalOrMixedAnd3D(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "MRAcquisitionType", -1, "3D"))
	return cond0
def Condition_ImageTypeValue1OriginalOrMixedAndSpectroscopyVolume(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "MRSpectroscopyAcquisitionType", -1, "VOLUME"))
	return cond0
def Condition_ImageTypeValue1OriginalOrMixedAndEchoPulseSequenceNotGradient(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "EchoPulseSequence", -1, "GRADIENT"))
	return cond0
def Condition_ImageTypeValue3ASL(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 2, "ASL"))
	return cond0
def Condition_ConcatenationUIDIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ConcatenationUID"))
	return cond0
def Condition_InConcatenationTotalNumberIsLessThanOrEqualToOne(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "InConcatenationTotalNumber", -1, BinaryValueMatchOperator.LessThanOrEquals, 1))
	return cond0
def Condition_ConcatenationAttributesArePresentAndTotalNumberIfPresentGreaterThanOne(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or (ElementPresent(ds , "ConcatenationFrameOffsetNumber"))
	cond1 = cond1 or(ElementPresent(ds , "ConcatenationUID"))
	cond1 = cond1 or(ElementPresent(ds , "SOPInstanceUIDOfConcatenationSource"))
	cond1 = cond1 or(ElementPresent(ds , "InConcatenationNumber"))
	cond1 = cond1 or(ElementPresent(ds , "InConcatenationTotalNumber"))
	cond0 = cond0 or cond1
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "InConcatenationTotalNumber"))
	cond1 = cond1 or(BinaryValueMatch(ds , "InConcatenationTotalNumber", -1, BinaryValueMatchOperator.GreaterThan, 1))
	cond0 = cond0 and cond1
	return cond0
def Condition_ReferencedImageSequenceIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ReferencedImageSequence"))
	return cond0
def Condition_ReferencedImageSequenceIsPresentInFunctionalGroups(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentInPathFromRootFirstItem(rootds , "ReferencedImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "ReferencedImageSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_SourceImageSequenceIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SourceImageSequence"))
	return cond0
def Condition_SourceImageSequenceIsPresentInFunctionalGroups(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentInPathFromRootFirstItem(rootds , "SourceImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "SourceImageSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_ImageTypeNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ImageType"))
	return cond0
def Condition_FrameTypeNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "FrameType"))
	return cond0
def Condition_GradientOutputIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "GradientOutput"))
	return cond0
def Condition_GradientOutputTypeIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "GradientOutputType"))
	return cond0
def Condition_InversionRecoveryIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "InversionRecovery", -1, "YES"))
	return cond0
def Condition_FlowCompensationNotNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "FlowCompensation", -1, "NONE"))
	return cond0
def Condition_EchoPulseSequenceGradientOrBoth(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "EchoPulseSequence", -1, "GRADIENT"))
	cond0 = cond0 or(StringValueMatch(rootds , "EchoPulseSequence", -1, "BOTH"))
	return cond0
def Condition_PartialFourierIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PartialFourier", -1, "YES"))
	return cond0
def Condition_ParallelAcquisitionIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ParallelAcquisition", -1, "YES"))
	return cond0
def Condition_TaggingIsGridOrLine(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Tagging", -1, "GRID"))
	cond0 = cond0  or (StringValueMatch(ds , "Tagging", -1, "LINE"))
	return cond0
def Condition_TaggingIsGrid(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Tagging", -1, "GRID"))
	return cond0
def Condition_ReceiveCoilTypeIsMultiCoil(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ReceiveCoilType", -1, "MULTICOIL"))
	return cond0
def Condition_DiffusionDirectionalityIsDirectional(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DiffusionDirectionality", -1, "DIRECTIONAL"))
	return cond0
def Condition_DiffusionDirectionalityIsBMatrix(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DiffusionDirectionality", -1, "BMATRIX"))
	return cond0
def Condition_NeedDiffusionAnisotropyType(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 3, "DIFFUSION_ANISO"))
	return cond0
def Condition_DerivationImageFunctionalGroupPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_DerivationImageFunctionalGroupNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_DerivationImageFunctionalGroupNotPresentOrFrameOfReferenceUIDPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresent(ds , "FrameOfReferenceUID"))
	return cond0
def Condition_RadiopharmaceuticalUsageSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "RadiopharmaceuticalUsageSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_RadiopharmaceuticalUsageSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "RadiopharmaceuticalUsageSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_SegmentIdentificationSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "SegmentIdentificationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_SegmentIdentificationSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "SegmentIdentificationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PixelMeasuresOrPlanePositionOrPlaneOrientationSequenceIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PixelMeasuresSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PixelMeasuresSequenceNotInSharedFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = False
	cond2 = cond2  or (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or  not cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_PixelMeasuresSequenceNotInSharedFunctionalGroupSequenceAndPlanePositionSequenceOrPlaneOrientationSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond2 = False
	cond2 = cond2  or (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or  not cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequenceAndPlanePositionSequenceOrPlaneOrientationSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_PlanePositionSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PlanePositionSequenceNotInSharedFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = False
	cond2 = cond2  or (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or  not cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_PlanePositionSequenceNotInSharedFunctionalGroupSequenceAndPixelMeasuresSequenceOrPlaneOrientationSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_PlanePositionSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PlanePositionSequenceNotInPerFrameFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond2 = False
	cond2 = cond2  or (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or  not cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_PlanePositionSequenceNotInPerFrameFunctionalGroupSequenceAndPixelMeasuresSequenceOrPlaneOrientationSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_PlaneOrientationSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PlaneOrientationSequenceNotInSharedFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = False
	cond2 = cond2  or (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or  not cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_PlaneOrientationSequenceNotInSharedFunctionalGroupSequenceAndPixelMeasuresSequenceOrPlanePositionSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	cond2 = False
	cond2 = cond2  or (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or  not cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequenceAndPixelMeasuresSequenceOrPlanePositionSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_DerivationImageSequenceNotInSharedFunctionalGroupSequenceAndPixelMeasuresPlanePositionPlaneOrientationNotPresentInEitherMBPO(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = False
	cond2 = cond2  or (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or  not cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_DerivationImageSequenceNotInPerFrameFunctionalGroupSequenceAndPixelMeasuresPlanePositionPlaneOrientationNotPresentInEitherMBPO(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond2 = False
	cond2 = cond2  or (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond2 = cond2 or(ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or  not cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_FrameAnatomyMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FrameAnatomySequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "FrameAnatomySequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FrameAnatomySequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FrameAnatomySequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_FrameAnatomyMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameAnatomySequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "FrameAnatomySequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameAnatomySequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PixelValueTransformationSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PixelValueTransformationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PixelValueTransformationSequenceNotInSharedFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PixelValueTransformationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_PixelValueTransformationSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PixelValueTransformationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PixelValueTransformationSequenceNotInPerFrameFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PixelValueTransformationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_MRImageFrameTypeSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "MRImageFrameTypeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_MRImageFrameTypeSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "MRImageFrameTypeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_MRSpectroscopyFrameTypeSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "MRSpectroscopyFrameTypeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_MRSpectroscopyFrameTypeSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "MRSpectroscopyFrameTypeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PETFrameTypeSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PETFrameTypeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PETFrameTypeSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PETFrameTypeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedRealWorldValueMappingMacroInSharedFunctionalGroupSequenceIfMultienergy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "RealWorldValueMappingSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "RealWorldValueMappingSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedRealWorldValueMappingMacroInPerFrameFunctionalGroupSequenceIfMultienergy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "RealWorldValueMappingSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "RealWorldValueMappingSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (ElementPresent(rootds , "CardiacSynchronizationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "CardiacSynchronizationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CardiacSynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CardiacSynchronizationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (ElementPresent(rootds , "CardiacSynchronizationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "CardiacSynchronizationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CardiacSynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CardiacSynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequenceRegardlessOfImageType(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "CardiacSynchronizationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "CardiacSynchronizationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CardiacSynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CardiacSynchronizationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequenceRegardlessOfImageType(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "CardiacSynchronizationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "CardiacSynchronizationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CardiacSynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CardiacSynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedRespiratorySynchronizationMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (ElementPresent(rootds , "RespiratoryMotionCompensationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "REALTIME"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "BREATH_HOLD"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "RespiratorySynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "RespiratorySynchronizationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedRespiratorySynchronizationMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (ElementPresent(rootds , "RespiratoryMotionCompensationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "REALTIME"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "BREATH_HOLD"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "RespiratorySynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "RespiratorySynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedRespiratorySynchronizationMacroInSharedFunctionalGroupSequenceRegardlessOfImageType(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "RespiratoryMotionCompensationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "REALTIME"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "BREATH_HOLD"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "RespiratorySynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "RespiratorySynchronizationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedRespiratorySynchronizationMacroInPerFrameFunctionalGroupSequenceRegardlessOfImageType(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "RespiratoryMotionCompensationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "REALTIME"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "BREATH_HOLD"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "RespiratorySynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "RespiratorySynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPatientPhysiologicalStateMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PatientPhysiologicalStateSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 2, "REST"))
	cond1 = cond1 or(StringValueMatch(rootds , "ImageType", 2, "STRESS"))
	cond0 = cond0 and cond1
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PatientPhysiologicalStateSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPatientPhysiologicalStateMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PatientPhysiologicalStateSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 2, "REST"))
	cond1 = cond1 or(StringValueMatch(rootds , "ImageType", 2, "STRESS"))
	cond0 = cond0 and cond1
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PatientPhysiologicalStateSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRTimingAndRelatedParametersMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRTimingAndRelatedParametersSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRTimingAndRelatedParametersSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRTimingAndRelatedParametersMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRTimingAndRelatedParametersSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRTimingAndRelatedParametersSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRFOVGeometryMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "GeometryOfKSpaceTraversal", -1, "RECTILINEAR"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRFOVGeometrySequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRFOVGeometrySequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRFOVGeometryMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "GeometryOfKSpaceTraversal", -1, "RECTILINEAR"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRFOVGeometrySequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRFOVGeometrySequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRSpectroscopyFOVGeometryMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "GeometryOfKSpaceTraversal", -1, "RECTILINEAR"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRSpectroscopyFOVGeometrySequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRSpectroscopyFOVGeometrySequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRSpectroscopyFOVGeometryMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "GeometryOfKSpaceTraversal", -1, "RECTILINEAR"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRSpectroscopyFOVGeometrySequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRSpectroscopyFOVGeometrySequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMREchoMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MREchoSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MREchoSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMREchoMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MREchoSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MREchoSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRModifierMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRModifierSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRModifierSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRModifierMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRModifierSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRModifierSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRImagingModifierMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRImagingModifierSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRImagingModifierSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRImagingModifierMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRImagingModifierSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRImagingModifierSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRReceiveCoilMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRReceiveCoilSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRReceiveCoilSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRReceiveCoilMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRReceiveCoilSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRReceiveCoilSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRTransmitCoilMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRTransmitCoilSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRTransmitCoilSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRTransmitCoilMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRTransmitCoilSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRTransmitCoilSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRDiffusionMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "AcquisitionContrast", -1, "DIFFUSION"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRDiffusionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRDiffusionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRDiffusionMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "AcquisitionContrast", -1, "DIFFUSION"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRDiffusionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRDiffusionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRSpatialSaturationMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "SpatialPresaturation", -1, "SLAB"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRSpatialSaturationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRSpatialSaturationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRSpatialSaturationMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "SpatialPresaturation", -1, "SLAB"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRSpatialSaturationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRSpatialSaturationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRAveragesMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRAveragesSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRAveragesSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRAveragesMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRAveragesSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRAveragesSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRMetaboliteMapMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 2, "METABOLITE_MAP"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRMetaboliteMapSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRMetaboliteMapSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRMetaboliteMapMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 2, "METABOLITE_MAP"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRMetaboliteMapSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRMetaboliteMapSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRVelocityEncodingMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "PhaseContrast", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRVelocityEncodingSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRVelocityEncodingSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRVelocityEncodingMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and (StringValueMatch(rootds , "PhaseContrast", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRVelocityEncodingSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRVelocityEncodingSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRArterialSpinLabelingMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 2, "ASL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "MRArterialSpinLabelingSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "MRArterialSpinLabelingSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedMRArterialSpinLabelingMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 2, "ASL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "MRArterialSpinLabelingSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "MRArterialSpinLabelingSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PhaseContrastIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PhaseContrast", -1, "YES"))
	return cond0
def Condition_NeedPETFrameAcquisitionMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "PETFrameAcquisitionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PETFrameAcquisitionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETFrameAcquisitionMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "PETFrameAcquisitionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PETFrameAcquisitionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETDetectorMotionDetailsMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PETDetectorMotionDetailsSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond1 = cond1  and  not (StringValueMatch(rootds , "TypeOfDetectorMotion", -1, "STATIONARY"))
	cond0 = cond0 and cond1
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PETDetectorMotionDetailsSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETDetectorMotionDetailsMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PETDetectorMotionDetailsSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond1 = cond1  and  not (StringValueMatch(rootds , "TypeOfDetectorMotion", -1, "STATIONARY"))
	cond0 = cond0 and cond1
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PETDetectorMotionDetailsSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETPositionMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "PETPositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PETPositionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETPositionMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "PETPositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PETPositionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETFrameCorrectionFactorsMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "PETFrameCorrectionFactorsSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PETFrameCorrectionFactorsSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETFrameCorrectionFactorsMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "PETFrameCorrectionFactorsSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PETFrameCorrectionFactorsSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETReconstructionMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "PETReconstructionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PETReconstructionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETReconstructionMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "PETReconstructionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PETReconstructionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETTableDynamicsMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PETTableDynamicsSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond1 = cond1  and (StringValueMatch(rootds , "TableMotion", -1, "DYNAMIC"))
	cond0 = cond0 and cond1
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PETTableDynamicsSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPETTableDynamicsMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PETTableDynamicsSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond1 = cond1  and (StringValueMatch(rootds , "TableMotion", -1, "DYNAMIC"))
	cond0 = cond0 and cond1
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PETTableDynamicsSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_LossyImageCompressionIs01(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "LossyImageCompression", -1, "01"))
	return cond0
def Condition_VolumeLocalizationTechniqueNotNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "VolumeLocalizationTechnique", -1, "NONE"))
	return cond0
def Condition_DecouplingIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Decoupling", -1, "YES"))
	return cond0
def Condition_DataPointRowsGreaterThanOne(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "DataPointRows", -1, BinaryValueMatchOperator.GreaterThan, 1))
	return cond0
def Condition_FirstOrderPhaseCorrectionIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "FirstOrderPhaseCorrection", -1, "YES"))
	return cond0
def Condition_ClinicalTrialSubjectReadingIDAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ClinicalTrialSubjectReadingID"))
	return cond0
def Condition_ClinicalTrialSubjectIDAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ClinicalTrialSubjectID"))
	return cond0
def Condition_NeedModuleClinicalTrialSubject(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialSponsorName"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialProtocolID"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialProtocolName"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialSiteID"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialSiteName"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialSubjectID"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialSubjectReadingID"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialProtocolEthicsCommitteeName"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialProtocolEthicsCommitteeApprovalNumber"))
	return cond0
def Condition_NeedModuleClinicalTrialStudy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialTimePointID"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialTimePointDescription"))
	cond0 = cond0  or (ElementPresent(ds , "ConsentForClinicalTrialUseSequence"))
	return cond0
def Condition_NeedModuleClinicalTrialSeries(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialCoordinatingCenterName"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialSeriesID"))
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialSeriesDescription"))
	return cond0
def Condition_NeedModuleEnhancedContrastBolus(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ContrastBolusAgentSequence"))
	return cond0
def Condition_NeedModuleMultiFrameDimension(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "DimensionOrganizationSequence"))
	cond0 = cond0  or (ElementPresent(ds , "DimensionIndexSequence"))
	return cond0
def Condition_MultiFrameFunctionalGroupsModuleIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SharedFunctionalGroupsSequence"))
	cond0 = cond0  or (ElementPresent(ds , "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "ContrastBolusAgentSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "ContrastBolusUsageSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "ContrastBolusUsageSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "ContrastBolusAgentSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "ContrastBolusUsageSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "ContrastBolusUsageSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_ParametricMapFrameTypeSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "ParametricMapFrameTypeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_ParametricMapFrameTypeSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "ParametricMapFrameTypeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_CTImageFrameTypeSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "CTImageFrameTypeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_CTImageFrameTypeSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "CTImageFrameTypeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTAcquisitionTypeMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CTAcquisitionTypeSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CTAcquisitionTypeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTAcquisitionTypeMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CTAcquisitionTypeSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CTAcquisitionTypeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTAcquisitionDetailsMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CTAcquisitionDetailsSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CTAcquisitionDetailsSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTAcquisitionDetailsMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CTAcquisitionDetailsSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CTAcquisitionDetailsSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTTableDynamicsMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CTTableDynamicsSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CTTableDynamicsSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTTableDynamicsMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CTTableDynamicsSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CTTableDynamicsSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTPositionMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CTPositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CTPositionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTPositionMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CTPositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CTPositionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTGeometryMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CTGeometrySequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CTGeometrySequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTGeometryMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CTGeometrySequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CTGeometrySequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTReconstructionMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CTReconstructionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CTReconstructionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTReconstructionMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CTReconstructionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CTReconstructionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTExposureMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CTExposureSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CTExposureSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTExposureMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CTExposureSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CTExposureSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTXRayDetailsMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CTXRayDetailsSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CTXRayDetailsSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedCTXRayDetailsMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "AcquisitionType", -1, "CONSTANT_ANGLE"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CTXRayDetailsSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CTXRayDetailsSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_CTAdditionalXRaySourceMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "CTAdditionalXRaySourceSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "CTAdditionalXRaySourceSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_CTAdditionalXRaySourceMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "CTAdditionalXRaySourceSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "CTAdditionalXRaySourceSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_MultienergyCTProcessingMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "MultienergyCTProcessingSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "MultienergyCTProcessingSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_MultienergyCTProcessingMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "MultienergyCTProcessingSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "MultienergyCTProcessingSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_MultienergyCTCharacteristicsMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "MultienergyCTCharacteristicsSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "MultienergyCTCharacteristicsSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_MultienergyCTCharacteristicsMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "MultienergyCTCharacteristicsSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "MultienergyCTCharacteristicsSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_AcquisitionTypeConstantAngle(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionType", -1, "CONSTANT_ANGLE"))
	return cond0
def Condition_ConvolutionKernelIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ConvolutionKernel"))
	return cond0
def Condition_ReconstructionFieldOfViewAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReconstructionFieldOfView"))
	return cond0
def Condition_ReconstructionDiameterAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReconstructionDiameter"))
	return cond0
def Condition_ExposureModulationTypeIsNotNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "ExposureModulationType", -1, "NONE"))
	return cond0
def Condition_MultiFrameIODAndNotSpecimen(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfFrames"))
	cond0 = cond0  and  not (ElementPresent(ds , "SpecimenAccessionNumber"))
	return cond0
def Condition_VOILUTSequenceLUTDescriptorRequiredToBe8Or16(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, DigitalXRayImageStorageForProcessingSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, DigitalMammographyXRayImageStorageForProcessingSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, DigitalIntraoralXRayImageStorageForProcessingSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, DigitalXRayImageStorageForPresentationSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, DigitalMammographyXRayImageStorageForPresentationSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, DigitalIntraoralXRayImageStorageForPresentationSOPClassUID))
	return cond0
def Condition_ReferencedImageSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedImageSequence"))
	return cond0
def Condition_FrameOfReferenceUIDNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "FrameOfReferenceUID"))
	return cond0
def Condition_FiducialIdentifierNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "FiducialIdentifier"))
	return cond0
def Condition_ContourDataIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ContourData"))
	return cond0
def Condition_ContourDataNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ContourData"))
	return cond0
def Condition_FrameOfReferenceUIDIsPresentInParent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentAbove(parentds , "FrameOfReferenceUID"))
	return cond0
def Condition_JPEGTransferSyntaxButNotYBR_FULL_422(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.50"))
	cond0 = cond0  and  not (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_FULL_422"))
	return cond0
def Condition_JPEG2000LosslessTransferSyntaxButNotYBR_RCT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.90"))
	cond0 = cond0  and  not (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_RCT"))
	return cond0
def Condition_JPEG2000TransferSyntaxButNotYBR_RCTorYBR_ICT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.91"))
	cond0 = cond0  and  not (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_RCT"))
	cond0 = cond0  and  not (StringValueMatch(ds , "PhotometricInterpretation", -1, "YBR_ICT"))
	return cond0
def Condition_JPEGLossyTransferSyntaxAndThreeSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.50"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.51"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.52"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.53"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.54"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.55"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.56"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.59"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.60"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.61"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.62"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.63"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.64"))
	cond0 = cond0 and cond1
	return cond0
def Condition_JPEGLossyTransferSyntaxAndThreeSamplesOtherThanWSI(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.50"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.51"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.52"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.53"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.54"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.55"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.56"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.59"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.60"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.61"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.62"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.63"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.64"))
	cond0 = cond0 and cond1
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, VLWholeSlideMicroscopyImageStorageSOPClassUID))
	return cond0
def Condition_JPEGLosslessTransferSyntaxAndThreeSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.57"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.58"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.65"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.66"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.70"))
	cond0 = cond0 and cond1
	return cond0
def Condition_JPEG2000LosslessTransferSyntaxAndThreeSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.90"))
	cond0 = cond0  and (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	return cond0
def Condition_JPEG2000LosslessTransferSyntaxAndThreeSamplesOtherThanWSI(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.90"))
	cond0 = cond0  and (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, VLWholeSlideMicroscopyImageStorageSOPClassUID))
	return cond0
def Condition_JPEG2000TransferSyntaxAndThreeSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.90"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.91"))
	cond0 = cond0 and cond1
	return cond0
def Condition_JPEG2000TransferSyntaxAndThreeSamplesOtherThanWSI(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.90"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.91"))
	cond0 = cond0 and cond1
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, VLWholeSlideMicroscopyImageStorageSOPClassUID))
	return cond0
def Condition_MPEG2TransferSyntax(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond0 = cond0 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	return cond0
def Condition_UncompressedTransferSyntaxAndThreeSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.1"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.2"))
	cond0 = cond0 and cond1
	return cond0
def Condition_RLETransferSyntaxAndThreeSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.5"))
	cond0 = cond0  and (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	return cond0
def Condition_MPEG2TransferSyntaxAndNotThreeSamples(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (BinaryValueMatch(ds , "SamplesPerPixel", -1, BinaryValueMatchOperator.Equals, 3))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond0 = cond0 and cond1
	return cond0
def Condition_MPEG2TransferSyntaxAndNotBitsAllocated8(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (BinaryValueMatch(ds , "BitsAllocated", -1, BinaryValueMatchOperator.Equals, 8))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond0 = cond0 and cond1
	return cond0
def Condition_MPEG2TransferSyntaxAndNotBitsStored8(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (BinaryValueMatch(ds , "BitsStored", -1, BinaryValueMatchOperator.Equals, 8))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond0 = cond0 and cond1
	return cond0
def Condition_MPEG2TransferSyntaxAndNotHighBit7(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (BinaryValueMatch(ds , "HighBit", -1, BinaryValueMatchOperator.Equals, 7))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond0 = cond0 and cond1
	return cond0
def Condition_MPEG2TransferSyntaxAndNotPixelRepresentation0(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (BinaryValueMatch(ds , "PixelRepresentation", -1, BinaryValueMatchOperator.Equals, 0))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond0 = cond0 and cond1
	return cond0
def Condition_MPEG2TransferSyntaxAndNotPlanarConfiguration0(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (BinaryValueMatch(ds , "PixelRepresentation", -1, BinaryValueMatchOperator.Equals, 0))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond0 = cond0 and cond1
	return cond0
def Condition_MPEG2MPMLTransferSyntaxAndColumnsGreaterThan720(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "Columns", -1, BinaryValueMatchOperator.GreaterThan, 720))
	cond0 = cond0  and (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	return cond0
def Condition_MPEG2MPMLTransferSyntaxAndRowsGreaterThan480NTSCOr576PAL(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "Rows", -1, BinaryValueMatchOperator.GreaterThan, 576))
	cond2 = False
	cond2 = cond2  or (BinaryValueMatch(ds , "Rows", -1, BinaryValueMatchOperator.GreaterThan, 480))
	cond3 = False
	cond3 = cond3  or (BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.NotEquals, 40))
	cond4 = False
	cond4 = cond4  or (ElementPresent(ds , "CineRate"))
	cond4 = cond4  and (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.NotEquals, 25))
	cond3 = cond3 or cond4
	cond2 = cond2 and cond3
	cond1 = cond1 or cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_MPEG2MPHLTransferSyntaxAndRowsNot720Or1080(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  and (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "Rows", -1, BinaryValueMatchOperator.Equals, 720))
	cond1 = cond1 or(BinaryValueMatch(ds , "Rows", -1, BinaryValueMatchOperator.Equals, 1080))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_MPEG2MPHLTransferSyntaxAndColumnsNot1280Or1920(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  and (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "Columns", -1, BinaryValueMatchOperator.Equals, 1280))
	cond1 = cond1 or(BinaryValueMatch(ds , "Columns", -1, BinaryValueMatchOperator.Equals, 1920))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_MPEG2MPHLTransferSyntaxAndColumnsInconsistentWithRows(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  and (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond1 = False
	cond2 = False
	cond2 = cond2  or (BinaryValueMatch(ds , "Rows", -1, BinaryValueMatchOperator.Equals, 720))
	cond2 = cond2  and (BinaryValueMatch(ds , "Columns", -1, BinaryValueMatchOperator.Equals, 1280))
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (BinaryValueMatch(ds , "Rows", -1, BinaryValueMatchOperator.Equals, 1080))
	cond2 = cond2  and (BinaryValueMatch(ds , "Columns", -1, BinaryValueMatchOperator.Equals, 1920))
	cond1 = cond1 or cond2
	cond0 = cond0 and  not cond1
	return cond0
def Condition_MPEG2MPMLTransferSyntaxAndFrameTimeNotNTSCOrPAL(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 40))
	cond1 = cond1 or(BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 33))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_MPEG2MPMLTransferSyntaxAndCineRateNotNTSCOrPAL(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond0 = cond0  and (ElementPresent(ds , "CineRate"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 25))
	cond1 = cond1 or(BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 30))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_MPEG2MPMLTransferSyntaxAndCineRateInconsistentWithFrameTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond0 = cond0  and (ElementPresent(ds , "CineRate"))
	cond0 = cond0  and (ElementPresent(ds , "FrameTime"))
	cond1 = False
	cond2 = False
	cond2 = cond2  or (BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 40))
	cond2 = cond2  and (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 25))
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 33))
	cond2 = cond2  and (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 30))
	cond1 = cond1 or cond2
	cond0 = cond0 and  not cond1
	return cond0
def Condition_MPEG2MPHLTransferSyntaxAndFrameTimeNotValid(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 40))
	cond1 = cond1 or(BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 33))
	cond1 = cond1 or(BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 20))
	cond1 = cond1 or(BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 16))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_MPEG2MPHLTransferSyntaxAndCineRateNotValid(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond0 = cond0  and (ElementPresent(ds , "CineRate"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 25))
	cond1 = cond1 or(BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 30))
	cond1 = cond1  or (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 50))
	cond1 = cond1 or(BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 60))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_MPEG2MPHLTransferSyntaxAndCineRateInconsistentWithFrameTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond0 = cond0  and (ElementPresent(ds , "CineRate"))
	cond0 = cond0  and (ElementPresent(ds , "FrameTime"))
	cond1 = False
	cond2 = False
	cond2 = cond2  or (BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 40))
	cond2 = cond2  and (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 25))
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 33))
	cond2 = cond2  and (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 30))
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 20))
	cond2 = cond2  and (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 50))
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (BinaryValueMatch(ds , "FrameTime", -1, BinaryValueMatchOperator.Equals, 16))
	cond2 = cond2  and (BinaryValueMatch(ds , "CineRate", -1, BinaryValueMatchOperator.Equals, 60))
	cond1 = cond1 or cond2
	cond0 = cond0 and  not cond1
	return cond0
def Condition_UnwantedPixelAspectRatioWhenMPEG2MPHLTransferSyntax(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond0 = cond0  and (ElementPresent(ds , "PixelAspectRatio"))
	return cond0
def Condition_ModalityNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "Modality"))
	return cond0
def Condition_AnatomicRegionSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "AnatomicRegionSequence"))
	return cond0
def Condition_AnatomicRegionSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "AnatomicRegionSequence"))
	return cond0
def Condition_ImageSetSelectorCategoryIsRelativeTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageSetSelectorCategory", -1, "RELATIVE_TIME"))
	return cond0
def Condition_RelativeTimePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RelativeTime"))
	return cond0
def Condition_ImageSetSelectorCategoryIsAbstractPriorAndAbstractPriorCodeSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageSetSelectorCategory", -1, "ABSTRACT_PRIOR"))
	cond0 = cond0  and  not (ElementPresent(ds , "AbstractPriorCodeSequence"))
	return cond0
def Condition_ImageSetSelectorCategoryIsAbstractPriorAndAbstractPriorValueNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageSetSelectorCategory", -1, "ABSTRACT_PRIOR"))
	cond0 = cond0  and  not (ElementPresent(ds , "AbstractPriorValue"))
	return cond0
def Condition_ScreenMinimumColorBitDepthNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ScreenMinimumColorBitDepth"))
	return cond0
def Condition_ScreenMinimumGrayscaleBitDepthNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ScreenMinimumGrayscaleBitDepth"))
	return cond0
def Condition_ImageBoxLayoutTypeIsTiled(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageBoxLayoutType", -1, "TILED"))
	return cond0
def Condition_ImageBoxLayoutTypeIsCine(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageBoxLayoutType", -1, "CINE"))
	return cond0
def Condition_ImageBoxLayoutTypeIsStack(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageBoxLayoutType", -1, "STACK"))
	return cond0
def Condition_ImageBoxLayoutTypeIsTiledAndMoreThanOneTile(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "ImageBoxTileHorizontalDimension", -1, BinaryValueMatchOperator.GreaterThan, 1))
	cond0 = cond0  or (BinaryValueMatch(ds , "ImageBoxTileVerticalDimension", -1, BinaryValueMatchOperator.GreaterThan, 1))
	cond0 = cond0  and (StringValueMatch(ds , "ImageBoxLayoutType", -1, "TILED"))
	return cond0
def Condition_ImageBoxSmallScrollTypePresentWithValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ImageBoxSmallScrollType"))
	return cond0
def Condition_ImageBoxLargeScrollTypePresentWithValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ImageBoxLargeScrollType"))
	return cond0
def Condition_ImageBoxLayoutTypeIsCineAndCineRelativeToRealTimeNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageBoxLayoutType", -1, "CINE"))
	cond0 = cond0  and  not (ElementPresent(ds , "CineRelativeToRealTime"))
	return cond0
def Condition_ImageBoxLayoutTypeIsCineAndRecommendedDisplayFrameRateNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageBoxLayoutType", -1, "CINE"))
	cond0 = cond0  and  not (ElementPresent(ds , "RecommendedDisplayFrameRate"))
	return cond0
def Condition_SelectorAttributeNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "SelectorAttribute"))
	return cond0
def Condition_SelectorAttributePresentAndFilterByOperatorNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SelectorAttribute"))
	cond0 = cond0  and  not (ElementPresent(ds , "FilterByOperator"))
	return cond0
def Condition_FilterByCategoryNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "FilterByCategory"))
	return cond0
def Condition_SelectorAttributeOrFilterByCategoryAndFilterByOperatorPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SelectorAttribute"))
	cond0 = cond0  or (ElementPresent(ds , "FilterByCategory"))
	cond0 = cond0  and (ElementPresent(ds , "FilterByOperator"))
	return cond0
def Condition_SelectorAttributeAndFilterByOperatorPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SelectorAttribute"))
	cond0 = cond0  and (ElementPresent(ds , "FilterByOperator"))
	return cond0
def Condition_SelectorAttributePresentAndFilterByAttributePresenceNotPresentOrFilterByCategoryPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SelectorAttribute"))
	cond0 = cond0  and (ElementPresent(ds , "FilterByAttributePresence"))
	cond0 = cond0 or(ElementPresent(ds , "FilterByCategory"))
	return cond0
def Condition_SortByCategoryNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "SortByCategory"))
	return cond0
def Condition_SelectorAttributePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SelectorAttribute"))
	return cond0
def Condition_ReformattingOperationTypeIsSlabOrMPR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ReformattingOperationType", -1, "SLAB"))
	cond0 = cond0 or(StringValueMatch(ds , "ReformattingOperationType", -1, "MPR"))
	return cond0
def Condition_ReformattingOperationTypeIsMPROr3D(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ReformattingOperationType", -1, "MPR"))
	cond0 = cond0 or(StringValueMatch(ds , "ReformattingOperationType", -1, "3D_RENDERING"))
	return cond0
def Condition_ReformattingOperationTypeIs3D(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ReformattingOperationType", -1, "3D_RENDERING"))
	return cond0
def Condition_SelectorAttributeVRIsAT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "AT"))
	return cond0
def Condition_SelectorAttributeVRIsCS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "CS"))
	return cond0
def Condition_SelectorAttributeVRIsIS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "IS"))
	return cond0
def Condition_SelectorAttributeVRIsLO(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "LO"))
	return cond0
def Condition_SelectorAttributeVRIsLT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "LT"))
	return cond0
def Condition_SelectorAttributeVRIsPN(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "PN"))
	return cond0
def Condition_SelectorAttributeVRIsSH(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "SH"))
	return cond0
def Condition_SelectorAttributeVRIsST(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "ST"))
	return cond0
def Condition_SelectorAttributeVRIsUT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "UT"))
	return cond0
def Condition_SelectorAttributeVRIsDS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "DS"))
	return cond0
def Condition_SelectorAttributeVRIsFD(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "FD"))
	return cond0
def Condition_SelectorAttributeVRIsFL(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "FL"))
	return cond0
def Condition_SelectorAttributeVRIsUL(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "UL"))
	return cond0
def Condition_SelectorAttributeVRIsUS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "US"))
	return cond0
def Condition_SelectorAttributeVRIsSL(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "SL"))
	return cond0
def Condition_SelectorAttributeVRIsSS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "SS"))
	return cond0
def Condition_SelectorAttributeVRIsSQ(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SelectorAttributeVR", -1, "SQ"))
	return cond0
def Condition_PatientEyeMovementCommandedIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PatientEyeMovementCommanded", -1, "YES"))
	return cond0
def Condition_PupilDilatedIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PupilDilated", -1, "YES"))
	return cond0
def Condition_PartialViewIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PartialView", -1, "YES"))
	return cond0
def Condition_PixelPaddingValueIsAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PixelPaddingValue"))
	return cond0
def Condition_PixelPaddingValueIsPresentAndInstanceIsNotAnImage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelPaddingValue"))
	cond0 = cond0  and  not (ElementPresent(ds , "PixelData"))
	cond0 = cond0  and  not (ElementPresent(ds , "PixelDataProviderURL"))
	return cond0
def Condition_PixelSpacingCalibrationTypeIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelSpacingCalibrationType"))
	return cond0
def Condition_PatientIdentityRemovedAndNotDeidentificationMethodCodeSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PatientIdentityRemoved", -1, "YES"))
	cond0 = cond0  and  not (ElementPresent(ds , "DeidentificationMethodCodeSequence"))
	return cond0
def Condition_PatientIdentityRemovedAndNotDeidentificationMethod(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PatientIdentityRemoved", -1, "YES"))
	cond0 = cond0  and  not (ElementPresent(ds , "DeidentificationMethod"))
	return cond0
def Condition_TransferSyntaxIsReferencedPixelData(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.94"))
	cond0 = cond0 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.95"))
	return cond0
def Condition_PixelDataProviderURLIsAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PixelDataProviderURL"))
	return cond0
def Condition_SOPClassIsEnhancedXAXRF(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.12.1.1"))
	cond0 = cond0 or(StringValueMatch(ds , "SOPClassUID", -1, "1.2.840.10008.5.1.4.1.1.12.2.1"))
	return cond0
def Condition_MaskOperationIsRevTID(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "MaskOperation", -1, "REV_TID"))
	return cond0
def Condition_MaskOperationIsTIDOrRevTID(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "MaskOperation", -1, "TID"))
	cond0 = cond0 or(StringValueMatch(ds , "MaskOperation", -1, "REV_TID"))
	return cond0
def Condition_ModalityIsMR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "Modality", -1, "MR"))
	return cond0
def Condition_ModalityIsCT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "Modality", -1, "CT"))
	return cond0
def Condition_ModalityIsMROrPET(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "Modality", -1, "MR"))
	cond0 = cond0 or(StringValueMatch(rootds , "Modality", -1, "PT"))
	return cond0
def Condition_IsocenterPositionIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "IsocenterPosition"))
	return cond0
def Condition_RadiationTypeIsIon(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "RadiationType", -1, "ION"))
	return cond0
def Condition_CompensatorMountingPositionNotDoubleSided(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "CompensatorMountingPosition", -1, "DOUBLE_SIDED"))
	return cond0
def Condition_RangeModulatorTypeIsWhlModWeights(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "RangeModulatorType", -1, "WHL_MODWEIGHTS"))
	return cond0
def Condition_ScanModeAboveIsModulatedOrModulatedSpec(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(parentds , "ScanMode", -1, "MODULATED"))
	return cond0
def Condition_ScanModeIsModulatedSpec(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ScanMode", -1, "MODULATED"))
	return cond0
def Condition_PlanesInAcquisitionNotUndefined(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "ImageType", -1, "UNDEFINED"))
	return cond0
def Condition_PositionerIsCArm(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PositionerType", -1, "CARM"))
	return cond0
def Condition_PositionerIsCArmWithTableTopRelationship(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PositionerType", -1, "CARM"))
	cond0 = cond0  and (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	return cond0
def Condition_CArmPositionerTabletopRelationshipIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	return cond0
def Condition_PositionerIsColumn(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PositionerType", -1, "COLUMN"))
	return cond0
def Condition_BitsAllocatedIs8(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "BitsAllocated", -1, BinaryValueMatchOperator.Equals, 8))
	return cond0
def Condition_BitsAllocatedIs16(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "BitsAllocated", -1, BinaryValueMatchOperator.Equals, 16))
	return cond0
def Condition_BitsStoredIs8(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "BitsStored", -1, BinaryValueMatchOperator.Equals, 8))
	return cond0
def Condition_BitsStoredGreaterThan8(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "BitsStored", -1, BinaryValueMatchOperator.GreaterThan, 8))
	return cond0
def Condition_ExposureInmAsNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ExposureInmAs"))
	return cond0
def Condition_XRayTubeCurrentInmAOrExposureTimeInmsNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "XRayTubeCurrentInmA"))
	cond0 = cond0 or not (ElementPresent(ds , "ExposureTimeInms"))
	return cond0
def Condition_IsocenterReferenceSystemSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "IsocenterReferenceSystemSequence"))
	return cond0
def Condition_XRayReceptorTypeIsImageIntensifier(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "XRayReceptorType", -1, "IMG_INTENSIFIER"))
	cond0 = cond0 or(StringValueMatch(rootds , "XRayReceptorType", -1, "IMG_INTENSIFIER"))
	return cond0
def Condition_XRayReceptorTypeIsDigitalDetector(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "XRayReceptorType", -1, "DIGITAL_DETECTOR"))
	cond0 = cond0 or(StringValueMatch(rootds , "XRayReceptorType", -1, "DIGITAL_DETECTOR"))
	return cond0
def Condition_ExposureControlSensingRegionShapeIsRectangular(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ExposureControlSensingRegionShape", -1, "RECTANGULAR"))
	return cond0
def Condition_ExposureControlSensingRegionShapeIsCircular(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ExposureControlSensingRegionShape", -1, "CIRCULAR"))
	return cond0
def Condition_ExposureControlSensingRegionShapeIsPolygonal(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ExposureControlSensingRegionShape", -1, "POLYGONAL"))
	return cond0
def Condition_GeometricalPropertiesIsNonUniform(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "GeometricalProperties", -1, "NON_UNIFORM"))
	return cond0
def Condition_DistanceObjectToTableTopNotEmpty(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ValuePresent(ds , "DistanceObjectToTableTop", -1))
	return cond0
def Condition_WaveformSampleInterpretationNeeds8Bit(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "WaveformSampleInterpretation", -1, "SB"))
	cond0 = cond0 or(StringValueMatch(ds , "WaveformSampleInterpretation", -1, "UB"))
	cond0 = cond0 or(StringValueMatch(ds , "WaveformSampleInterpretation", -1, "MB"))
	cond0 = cond0 or(StringValueMatch(ds , "WaveformSampleInterpretation", -1, "AB"))
	return cond0
def Condition_WaveformSampleInterpretationNeeds16Bit(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "WaveformSampleInterpretation", -1, "SS"))
	cond0 = cond0 or(StringValueMatch(ds , "WaveformSampleInterpretation", -1, "US"))
	return cond0
def Condition_InstitutionCodeSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "InstitutionCodeSequence"))
	return cond0
def Condition_InstitutionNameNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "InstitutionName"))
	return cond0
def Condition_ObserverTypeIsPerson(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ObserverType", -1, "PSN"))
	return cond0
def Condition_ObserverTypeIsDevice(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ObserverType", -1, "DEV"))
	return cond0
def Condition_PlanePositionSequenceOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PlanePositionSequenceOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PlanePositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PlaneOrientationSequenceOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PlaneOrientationSequenceOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PlaneOrientationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "PlaneOrientationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PixelValueTransformationSequenceOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PixelValueTransformationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "PixelValueTransformationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PixelValueTransformationSequenceOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PixelValueTransformationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "PixelValueTransformationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FrameVOILUTMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameVOILUTSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "FrameVOILUTSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_FrameVOILUTMacroOKInSharedFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameVOILUTSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "FrameVOILUTSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FrameVOILUTSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "FrameVOILUTSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FrameVOILUTMacroOKInPerFrameFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FrameVOILUTSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "FrameVOILUTSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_RealWorldValueMappingSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "RealWorldValueMappingSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "RealWorldValueMappingSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "RealWorldValueMappingSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_RealWorldValueMappingMacroOKInSharedFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "RealWorldValueMappingSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "RealWorldValueMappingSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_RealWorldValueMappingSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "RealWorldValueMappingSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "RealWorldValueMappingSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "RealWorldValueMappingSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "RealWorldValueMappingSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "RealWorldValueMappingSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_ReferencedImageMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "ReferencedImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "ReferencedImageSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_ReferencedImageMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "ReferencedImageSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "ReferencedImageSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_DerivationImageMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_DerivationImageMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "CardiacSynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "CardiacSynchronizationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "CardiacSynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "CardiacSynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FramePixelShiftMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FramePixelShiftSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "FramePixelShiftSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_FramePixelShiftMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FramePixelShiftSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "FramePixelShiftSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FrameDisplayShutterMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameDisplayShutterSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "FrameDisplayShutterSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_FrameDisplayShutterMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FrameDisplayShutterSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "FrameDisplayShutterSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "RespiratorySynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "RespiratorySynchronizationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "RespiratorySynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "RespiratorySynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayFrameCharacteristicsMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "XAXRFFrameCharacteristicsSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "XAXRFFrameCharacteristicsSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRayFrameCharacteristicsMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "XAXRFFrameCharacteristicsSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "XAXRFFrameCharacteristicsSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayExposureControlSensingRegionsMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "ExposureControlSensingRegionsSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "ExposureControlSensingRegionsSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRayExposureControlSensingRegionsMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "ExposureControlSensingRegionsSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "ExposureControlSensingRegionsSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayCalibrationDeviceUsageMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "CalibrationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "CalibrationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRayCalibrationDeviceUsageMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "CalibrationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "CalibrationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayObjectThicknessMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "ObjectThicknessSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "ObjectThicknessSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRayObjectThicknessMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "ObjectThicknessSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "ObjectThicknessSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayFrameAcquisitionMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameAcquisitionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "FrameAcquisitionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRayFrameAcquisitionMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FrameAcquisitionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "FrameAcquisitionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayIsocenterReferenceSystemMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "IsocenterReferenceSystemSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "IsocenterReferenceSystemSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	return cond0
def Condition_XRayIsocenterReferenceSystemMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "IsocenterReferenceSystemSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "IsocenterReferenceSystemSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	return cond0
def Condition_PatientOrientationInFrameMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PatientOrientationInFrameSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "PatientOrientationInFrameSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PatientOrientationInFrameMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PatientOrientationInFrameSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "PatientOrientationInFrameSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_TemporalPositionMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "TemporalPositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "TemporalPositionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_TemporalPositionMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "TemporalPositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "TemporalPositionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_TemporalPositionMacroOKInSharedFunctionalGroupSequenceAndNotCardiacOrRespiratoryEvent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "TemporalPositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "TemporalPositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CardiacSynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CardiacSynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "RespiratorySynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "RespiratorySynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_TemporalPositionMacroOKInPerFrameFunctionalGroupSequenceAndNotCardiacOrRespiratoryEvent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "TemporalPositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "TemporalPositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CardiacSynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CardiacSynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "RespiratorySynchronizationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "RespiratorySynchronizationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FrameVOILUTSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FrameVOILUTSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_FrameVOILUTSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameVOILUTSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_ImageDataTypeSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "ImageDataTypeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_ImageDataTypeSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "ImageDataTypeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_IrradiationEventIdentificationMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "IrradiationEventIdentificationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "IrradiationEventIdentificationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_IrradiationEventIdentificationMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "IrradiationEventIdentificationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "IrradiationEventIdentificationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_IrradiationEventIdentificationSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "IrradiationEventIdentificationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_IrradiationEventIdentificationSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "IrradiationEventIdentificationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_ConversionSourceAttributesSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "ConversionSourceAttributesSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_ConversionSourceAttributesSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "ConversionSourceAttributesSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FramePixelDataPropertiesSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FramePixelDataPropertiesSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_FramePixelDataPropertiesSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FramePixelDataPropertiesSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPixelIntensityRelationshipLUTMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PixelIntensityRelationship", -1, "LOG"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "PixelIntensityRelationshipLUTSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PixelIntensityRelationshipLUTSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPixelIntensityRelationshipLUTMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PixelIntensityRelationship", -1, "LOG"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "PixelIntensityRelationshipLUTSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PixelIntensityRelationshipLUTSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPatientOrientationInFrameMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "PatientOrientationInFrameSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PatientOrientationInFrameSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPatientOrientationInFrameMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "PatientOrientationInFrameSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PatientOrientationInFrameSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FieldOfViewSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FieldOfViewSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FieldOfViewSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FieldOfViewSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayFieldOfViewMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "IsocenterReferenceSystemSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "FieldOfViewSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "FieldOfViewSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayFieldOfViewMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "IsocenterReferenceSystemSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "FieldOfViewSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "FieldOfViewSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayFrameDetectorParametersMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameDetectorParametersSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "FrameDetectorParametersSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRayFrameDetectorParametersMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "FrameDetectorParametersSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "FrameDetectorParametersSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayFrameDetectorParametersMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "XRayReceptorType", -1, "DIGITAL_DETECTOR"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameDetectorParametersSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "FrameDetectorParametersSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayFrameDetectorParametersMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "XRayReceptorType", -1, "DIGITAL_DETECTOR"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "FrameDetectorParametersSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "FrameDetectorParametersSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayProjectionPixelCalibrationMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "ProjectionPixelCalibrationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "ProjectionPixelCalibrationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayProjectionPixelCalibrationMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "ProjectionPixelCalibrationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "ProjectionPixelCalibrationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayPositionerMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "PositionerPositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PositionerPositionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayPositionerMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "PositionerPositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PositionerPositionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayTablePositionMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "TablePositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "TablePositionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayTablePositionMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "TablePositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "TablePositionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_CollimatorShapeSequenceSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "CollimatorShapeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_CollimatorShapeSequenceSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "CollimatorShapeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayCollimatorMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "CollimatorShapeSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "CollimatorShapeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayCollimatorMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "CollimatorShapeSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "CollimatorShapeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayGeometryMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "XRayGeometrySequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "XRayGeometrySequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedXRayGeometryMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "CArmPositionerTabletopRelationship", -1, "YES"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "XRayGeometrySequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "XRayGeometrySequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_ResponsiblePersonIsPresentWithValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ResponsiblePerson"))
	cond0 = cond0  and (ValuePresent(ds , "ResponsiblePerson", -1))
	return cond0
def Condition_IsHuman(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or (ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "PatientSpeciesCodeSequence", -1, "SRT"))
	cond2 = False
	cond2 = cond2  or (ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85B00"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85003"))
	cond1 = cond1 and cond2
	cond0 = cond0 or cond1
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "PatientSpeciesDescription"))
	cond1 = cond1  and  not (ElementPresent(ds , "PatientSpeciesCodeSequence"))
	cond1 = cond1  and  not (ElementPresent(ds , "PatientBreedDescription"))
	cond1 = cond1  and  not (ElementPresent(ds , "PatientBreedCodeSequence"))
	cond1 = cond1  and  not (ElementPresent(ds , "BreedRegistrationSequence"))
	cond1 = cond1  and  not (ElementPresent(ds , "StrainDescription"))
	cond1 = cond1  and  not (ElementPresent(ds , "StrainNomenclature"))
	cond1 = cond1  and  not (ElementPresent(ds , "StrainCodeSequence"))
	cond1 = cond1  and  not (ElementPresent(ds , "StrainAdditionalInformation"))
	cond1 = cond1  and  not (ElementPresent(ds , "StrainStockSequence"))
	cond0 = cond0 or cond1
	return cond0
def Condition_IsAnimal(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or (ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "PatientSpeciesCodeSequence", -1, "SRT"))
	cond2 = False
	cond2 = cond2  or (ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85B00"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85003"))
	cond1 = cond1 and cond2
	cond0 = cond0 or  not cond1
	cond1 = False
	cond1 = cond1  or (ElementPresent(ds , "PatientSpeciesDescription"))
	cond1 = cond1 or(ElementPresent(ds , "PatientSpeciesCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "PatientBreedDescription"))
	cond1 = cond1 or(ElementPresent(ds , "PatientBreedCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "BreedRegistrationSequence"))
	cond1 = cond1 or(ElementPresent(ds , "StrainDescription"))
	cond1 = cond1 or(ElementPresent(ds , "StrainNomenclature"))
	cond1 = cond1 or(ElementPresent(ds , "StrainCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "StrainAdditionalInformation"))
	cond1 = cond1 or(ElementPresent(ds , "StrainStockSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_IsAnimalAndPatientSpeciesCodeSequenceAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PatientSpeciesCodeSequence"))
	cond1 = False
	cond2 = False
	cond2 = cond2  or (ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "PatientSpeciesCodeSequence", -1, "SRT"))
	cond3 = False
	cond4 = False
	cond4 = cond4  or (ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85B00"))
	cond4 = cond4 or(ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85003"))
	cond3 = cond3 or  not cond4
	cond2 = cond2 and cond3
	cond1 = cond1 or cond2
	cond1 = cond1  or (ElementPresent(ds , "PatientSpeciesDescription"))
	cond1 = cond1 or(ElementPresent(ds , "PatientBreedDescription"))
	cond1 = cond1 or(ElementPresent(ds , "PatientBreedCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "BreedRegistrationSequence"))
	cond1 = cond1 or(ElementPresent(ds , "StrainDescription"))
	cond1 = cond1 or(ElementPresent(ds , "StrainNomenclature"))
	cond1 = cond1 or(ElementPresent(ds , "StrainCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "StrainAdditionalInformation"))
	cond1 = cond1 or(ElementPresent(ds , "StrainStockSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_IsAnimalAndPatientSpeciesDescriptionAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PatientSpeciesDescription"))
	cond1 = False
	cond2 = False
	cond2 = cond2  or (ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "PatientSpeciesCodeSequence", -1, "SRT"))
	cond3 = False
	cond4 = False
	cond4 = cond4  or (ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85B00"))
	cond4 = cond4 or(ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85003"))
	cond3 = cond3 or  not cond4
	cond2 = cond2 and cond3
	cond1 = cond1 or cond2
	cond1 = cond1  or (ElementPresent(ds , "PatientSpeciesCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "PatientBreedDescription"))
	cond1 = cond1 or(ElementPresent(ds , "PatientBreedCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "BreedRegistrationSequence"))
	cond1 = cond1 or(ElementPresent(ds , "StrainDescription"))
	cond1 = cond1 or(ElementPresent(ds , "StrainNomenclature"))
	cond1 = cond1 or(ElementPresent(ds , "StrainCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "StrainAdditionalInformation"))
	cond1 = cond1 or(ElementPresent(ds , "StrainStockSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_IsAnimalAndPatientBreedCodeSequenceEmpty(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (SequenceHasItems(ds , "PatientBreedCodeSequence"))
	cond1 = False
	cond2 = False
	cond2 = cond2  or (ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "PatientSpeciesCodeSequence", -1, "SRT"))
	cond3 = False
	cond4 = False
	cond4 = cond4  or (ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85B00"))
	cond4 = cond4 or(ElementStringValueMatchWithin(ds , "CodeValue", "PatientSpeciesCodeSequence", -1, "L-85003"))
	cond3 = cond3 or  not cond4
	cond2 = cond2 and cond3
	cond1 = cond1 or cond2
	cond1 = cond1  or (ElementPresent(ds , "PatientSpeciesDescription"))
	cond1 = cond1 or(ElementPresent(ds , "PatientSpeciesCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "PatientBreedDescription"))
	cond1 = cond1 or(ElementPresent(ds , "PatientBreedCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "BreedRegistrationSequence"))
	cond1 = cond1 or(ElementPresent(ds , "StrainDescription"))
	cond1 = cond1 or(ElementPresent(ds , "StrainNomenclature"))
	cond1 = cond1 or(ElementPresent(ds , "StrainCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "StrainAdditionalInformation"))
	cond1 = cond1 or(ElementPresent(ds , "StrainStockSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_DetectorTypeIsStorage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DetectorType", -1, "STORAGE"))
	return cond0
def Condition_DetectorTypeIsNotStorage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "DetectorType", -1, "STORAGE"))
	return cond0
def Condition_CodingSchemeDesignatorIsACR(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "ACR"))
	return cond0
def Condition_CodingSchemeDesignatorIsASTMSigpurpose(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "ASTM-sigpurpose"))
	return cond0
def Condition_CodingSchemeDesignatorIsC4(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "C4"))
	return cond0
def Condition_CodingSchemeDesignatorIsC5(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "C5"))
	return cond0
def Condition_CodingSchemeDesignatorIsCD2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "CD2"))
	return cond0
def Condition_CodingSchemeDesignatorIsDCM(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "DCM"))
	return cond0
def Condition_CodingSchemeDesignatorIsDCMUID(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "DCMUID"))
	return cond0
def Condition_CodingSchemeDesignatorIsHPC(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "HPC"))
	return cond0
def Condition_CodingSchemeDesignatorIsI10(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "I10"))
	return cond0
def Condition_CodingSchemeDesignatorIsI10P(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "I10P"))
	return cond0
def Condition_CodingSchemeDesignatorIsI9(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "I9"))
	return cond0
def Condition_CodingSchemeDesignatorIsI9C(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "I9C"))
	return cond0
def Condition_CodingSchemeDesignatorIsISO3166_1(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "ISO3166_1"))
	return cond0
def Condition_CodingSchemeDesignatorIsISO639_1(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "ISO639_1"))
	return cond0
def Condition_CodingSchemeDesignatorIsISO639_2(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "ISO639_2"))
	return cond0
def Condition_CodingSchemeDesignatorIsLN(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "LN"))
	return cond0
def Condition_CodingSchemeDesignatorIsPOS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "POS"))
	return cond0
def Condition_CodingSchemeDesignatorIsRFC3066(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "RFC3066"))
	return cond0
def Condition_CodingSchemeDesignatorIsSNM3(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "SNM3"))
	return cond0
def Condition_CodingSchemeDesignatorIsSCT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "SCT"))
	return cond0
def Condition_CodingSchemeDesignatorIsSRT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "SRT"))
	return cond0
def Condition_CodingSchemeDesignatorIsCTV3(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "CTV3"))
	return cond0
def Condition_CodingSchemeDesignatorIsUCUM(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "UCUM"))
	return cond0
def Condition_CodingSchemeDesignatorIsUMLS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "UMLS"))
	return cond0
def Condition_CodingSchemeDesignatorIsUPC(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "UPC"))
	return cond0
def Condition_PixelPaddingRangeLimitIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelPaddingRangeLimit"))
	return cond0
def Condition_PatientPositionAndPatientOrientationCodeSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PatientPosition"))
	cond0 = cond0  and (ElementPresent(ds , "PatientOrientationCodeSequence"))
	return cond0
def Condition_VOILUTSequencePresentAndPresentationIntentTypeIsNotForPresentation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "VOILUTSequence"))
	cond0 = cond0  and  not (StringValueMatch(ds , "PresentationIntentType", -1, "FOR PRESENTATION"))
	return cond0
def Condition_WindowCenterPresentAndPresentationIntentTypeIsNotForPresentation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "WindowCenter"))
	cond0 = cond0  and  not (StringValueMatch(ds , "PresentationIntentType", -1, "FOR PRESENTATION"))
	return cond0
def Condition_SpatialLocationsPreservedReorientedOnly(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SpatialLocationsPreserved", -1, "REORIENTED_ONLY"))
	return cond0
def Condition_UnwantedPixelAspectRatioWhenPixelSpacingPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelAspectRatio"))
	cond0 = cond0  and (ElementPresent(ds , "PixelSpacing"))
	return cond0
def Condition_UnwantedPixelAspectRatioWhenImagerPixelSpacingPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelAspectRatio"))
	cond0 = cond0  and (ElementPresent(ds , "ImagerPixelSpacing"))
	return cond0
def Condition_UnwantedPixelAspectRatioWhenNominalScannedPixelSpacingPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelAspectRatio"))
	cond0 = cond0  and (ElementPresent(ds , "NominalScannedPixelSpacing"))
	return cond0
def Condition_UnwantedPixelAspectRatioWhenSharedPixelMeasuresMacro(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelAspectRatio"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "PixelMeasuresSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_UnwantedPixelAspectRatioWhenPerFramePixelMeasuresMacro(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelAspectRatio"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "PixelMeasuresSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_DimensionIndexPointerIsNotFunctionalGroup(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9304)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9301)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9360)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9321)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9312)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9329)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9326)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9314)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9308)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9325)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9455)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9118)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9407)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9341)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0020,0x9172)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0008,0x9124)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9434)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9432)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9417)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0020,0x9071)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9451)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9472)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0028,0x9443)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0028,0x9415)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0028,0x9132)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9807)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0052,0x0027)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0052,0x0029)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0052,0x0025)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9477)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9462)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9251)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9119)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9117)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9114)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9125)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9226)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9006)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9152)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9115)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9042)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9107)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9103)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9227)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9112)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9049)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9197)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0022,0x0031)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0048,0x0207)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9456)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9733)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9732)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9736)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9751)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9735)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9749)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9734)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0040,0x9092)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0020,0x9450)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9771)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0028,0x9422)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0028,0x9110)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0028,0x9145)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0020,0x9116)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0020,0x9113)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0048,0x021a)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9405)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9401)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9737)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0040,0x9096)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0008,0x1140)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0020,0x9253)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0062,0x000a)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0048,0x0110)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9406)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0020,0x9310)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9476)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9412)))
	cond0 = cond0  and  not (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0018,0x9504)))
	return cond0
def Condition_DimensionIndexPointerIsFrameContentSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0020,0x9111)))
	return cond0
def Condition_DimensionIndexPointerIsDimensionIndexValues(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (TagValueMatch(ds , "DimensionIndexPointer", -1, Tag(0x0020,0x9157)))
	return cond0
def Condition_CardiacSignalSourcePresentAndCardiacSynchronizationTechniqueIsNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CardiacSignalSource"))
	cond0 = cond0  and (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "NONE"))
	return cond0
def Condition_CardiacRRIntervalSpecifiedPresentAndCardiacSynchronizationTechniqueIsNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CardiacRRIntervalSpecified"))
	cond0 = cond0  and (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "NONE"))
	return cond0
def Condition_CardiacBeatRejectionTechniquePresentAndCardiacSynchronizationTechniqueIsNotProspectiveOrRetrospective(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CardiacBeatRejectionTechnique"))
	cond0 = cond0  and  not (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "PROSPECTIVE"))
	cond0 = cond0  and  not (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "RETROSPECTIVE"))
	return cond0
def Condition_LowRRValuePresentAndCardiacSynchronizationTechniqueIsNotProspectiveOrRetrospective(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "LowRRValue"))
	cond0 = cond0  and  not (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "PROSPECTIVE"))
	cond0 = cond0  and  not (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "RETROSPECTIVE"))
	return cond0
def Condition_HighRRValuePresentAndCardiacSynchronizationTechniqueIsNotProspectiveOrRetrospective(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "HighRRValue"))
	cond0 = cond0  and  not (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "PROSPECTIVE"))
	cond0 = cond0  and  not (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "RETROSPECTIVE"))
	return cond0
def Condition_IntervalsAcquiredPresentAndCardiacSynchronizationTechniqueIsNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "IntervalsAcquired"))
	cond0 = cond0  and (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "NONE"))
	return cond0
def Condition_IntervalsRejectedPresentAndCardiacSynchronizationTechniqueIsNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "IntervalsRejected"))
	cond0 = cond0  and (StringValueMatch(ds , "CardiacSynchronizationTechnique", -1, "NONE"))
	return cond0
def Condition_RespiratorySignalSourcePresentAndRespiratoryMotionCompensationTechniqueIsNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RespiratorySignalSource"))
	cond0 = cond0  and (StringValueMatch(ds , "RespiratoryMotionCompensationTechnique", -1, "NONE"))
	return cond0
def Condition_BulkMotionSignalSourcePresentAndBulkMotionCompensationTechniqueIsNone(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "BulkMotionSignalSource"))
	cond0 = cond0  and (StringValueMatch(ds , "BulkMotionCompensationTechnique", -1, "NONE"))
	return cond0
def Condition_ReferencedFrameNumberAndReferencedSegmentNumberPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ReferencedFrameNumber"))
	cond0 = cond0  and (ElementPresent(ds , "ReferencedSegmentNumber"))
	return cond0
def Condition_IsUltrasoundStageProtocol(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NumberOfStages"))
	cond0 = cond0  or (ElementPresent(ds , "NumberOfViewsInStage"))
	cond0 = cond0  or (ElementPresent(ds , "StageName"))
	cond0 = cond0  or (ElementPresent(ds , "StageCodeSequence"))
	cond0 = cond0  or (ElementPresent(ds , "StageNumber"))
	cond0 = cond0  or (ElementPresent(ds , "ViewName"))
	cond0 = cond0  or (ElementPresent(ds , "ViewNumber"))
	return cond0
def Condition_NominalScannedPixelSpacingPresentAndConversionTypeNotDigitizedFilmScannedDocumentScannedImage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "NominalScannedPixelSpacing"))
	cond0 = cond0  and  not (StringValueMatch(ds , "ConversionType", -1, "DF"))
	cond0 = cond0  and  not (StringValueMatch(ds , "ConversionType", -1, "SD"))
	cond0 = cond0  and  not (StringValueMatch(ds , "ConversionType", -1, "SI"))
	return cond0
def Condition_PartialViewNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PartialView"))
	return cond0
def Condition_CodeValueIllegalOrDeprecated(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodeValue", -1, "Y-X1770"))
	cond0 = cond0  or (StringValueMatch(ds , "CodeValue", -1, "Y-X1771"))
	cond0 = cond0  or (StringValueMatch(ds , "CodeValue", -1, "TBD"))
	return cond0
def Condition_CodingSchemeDesignatorDeprecated(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "SRT"))
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "SNM3"))
	cond0 = cond0  or (StringValueMatch(ds , "CodingSchemeDesignator", -1, "99SDM"))
	return cond0
def Condition_CodeMeaningIllegalOrDeprecated(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CodeValue", -1, "TBD"))
	return cond0
def Condition_LongCodeValueAndURNCodeValueAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "LongCodeValue"))
	cond0 = cond0  and  not (ElementPresent(ds , "URNCodeValue"))
	return cond0
def Condition_CodeValueOrLongCodeValuePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CodeValue"))
	cond0 = cond0 or(ElementPresent(ds , "LongCodeValue"))
	return cond0
def Condition_CodeValueAndURNCodeValueAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "CodeValue"))
	cond0 = cond0  and  not (ElementPresent(ds , "URNCodeValue"))
	return cond0
def Condition_CodeValueAndLongCodeValueAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "CodeValue"))
	cond0 = cond0  and  not (ElementPresent(ds , "LongCodeValue"))
	return cond0
def Condition_NeedOphthalmicFrameLocationMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "OphthalmicFrameLocationSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "OphthalmicFrameLocationSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedOphthalmicFrameLocationMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "OphthalmicFrameLocationSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "OphthalmicFrameLocationSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	return cond0
def Condition_OphthalmicImageOrientationIsTransverse(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "OphthalmicImageOrientation", -1, "TRANSVERSE"))
	return cond0
def Condition_ReferencedSOPClassUIDInFileIsEncapsulatedCDADocument(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ReferencedSOPClassUIDInFile", -1, EncapsulatedCDAStorageSOPClassUID))
	return cond0
def Condition_XRay3DFrameTypeSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "XRay3DFrameTypeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRay3DFrameTypeSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "XRay3DFrameTypeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedModulePatientOrientation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PatientOrientationCodeSequence"))
	cond0 = cond0  or (ElementPresent(ds , "PatientGantryRelationshipCodeSequence"))
	return cond0
def Condition_NeedModuleImageEquipmentCoordinateRelationship(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ImageToEquipmentMappingMatrix"))
	cond0 = cond0  or (ElementPresent(ds , "EquipmentCoordinateSystemIdentification"))
	return cond0
def Condition_NeedModuleXRay3DAngiographicImageContributingSources(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ContributingSourcesSequence"))
	return cond0
def Condition_NeedModuleXRay3DCraniofacialImageContributingSources(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ContributingSourcesSequence"))
	return cond0
def Condition_NeedModuleXRay3DAngiographicAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "XRay3DAcquisitionSequence"))
	return cond0
def Condition_NeedModuleXRay3DCraniofacialAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "XRay3DAcquisitionSequence"))
	return cond0
def Condition_NeedModuleXRay3DReconstruction(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "XRay3DReconstructionSequence"))
	return cond0
def Condition_SingleCardiacIntervalAcquired(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "IntervalsAcquired", -1, BinaryValueMatchOperator.Equals, 1))
	return cond0
def Condition_CardiacSynchronizationTechniqueOtherThanNoneOrRealTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "CardiacSynchronizationTechnique"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "CardiacSynchronizationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "CardiacSynchronizationTechnique", -1, "REALTIME"))
	return cond0
def Condition_NeedRespiratoryIntervalTime(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "NONE"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryMotionCompensationTechnique", -1, "REALTIME"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "RespiratoryTriggerType", -1, "AMPLITUDE"))
	return cond0
def Condition_RespiratoryTriggerTypeTimeOrBoth(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "RespiratoryTriggerType", -1, "TIME"))
	cond0 = cond0  or (StringValueMatch(rootds , "RespiratoryTriggerType", -1, "BOTH"))
	return cond0
def Condition_RespiratoryTriggerTypeAmplitudeOrBoth(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "RespiratoryTriggerType", -1, "AMPLITUDE"))
	cond0 = cond0  or (StringValueMatch(rootds , "RespiratoryTriggerType", -1, "BOTH"))
	return cond0
def Condition_StartingRespiratoryAmplitudeIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "StartingRespiratoryAmplitude"))
	return cond0
def Condition_EndingRespiratoryAmplitudeIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "EndingRespiratoryAmplitude"))
	return cond0
def Condition_BlendingSequenceIsNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "BlendingSequence"))
	return cond0
def Condition_ReferencedSeriesSequenceIsNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedSeriesSequence"))
	return cond0
def Condition_AnatomicRegionSequenceIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "AnatomicRegionSequence"))
	return cond0
def Condition_AnatomicRegionSequenceIsNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "AnatomicRegionSequence"))
	return cond0
def Condition_ModalityIsNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "Modality"))
	return cond0
def Condition_AbsoluteChannelDisplayScaleIsNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "AbsoluteChannelDisplayScale"))
	return cond0
def Condition_FractionalChannelDisplayScaleIsNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "FractionalChannelDisplayScale"))
	return cond0
def Condition_SpecimenIdentifierIsPresentWithValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SpecimenIdentifier"))
	cond0 = cond0  and (ValuePresent(ds , "SpecimenIdentifier", -1))
	return cond0
def Condition_ROIPhysicalPropertyIsElemFraction(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ROIPhysicalProperty", -1, "ELEM_FRACTION"))
	return cond0
def Condition_PixelSpacingIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelSpacing"))
	return cond0
def Condition_ImageTypeValue3MissingOrEmpty(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ValuePresent(ds , "ImageType", 2))
	cond0 = cond0 or(StringValueMatch(ds , "ImageType", 2, ""))
	return cond0
def Condition_ImageTypeValue4MissingOrEmpty(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ValuePresent(ds , "ImageType", 3))
	cond0 = cond0 or(StringValueMatch(ds , "ImageType", 3, ""))
	return cond0
def Condition_LateralityHasNoValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "Laterality"))
	cond0 = cond0  and  not (ValuePresent(ds , "Laterality", -1))
	return cond0
def Condition_LateralityRequired(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ImageLaterality"))
	cond0 = cond0  and  not (ElementPresent(ds , "MeasurementLaterality"))
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "FrameAnatomySequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "FrameAnatomySequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "SegmentSequence"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, BasicVoiceStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, TwelveLeadECGStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, GeneralECGStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, AmbulatoryECGStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, CardiacElectrophysiologyWaveformStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, RespiratoryWaveformStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(ds , "Modality", -1, "ECG"))
	cond0 = cond0  and  not (StringValueMatch(ds , "Modality", -1, "EPS"))
	cond0 = cond0  and  not (StringValueMatch(ds , "Modality", -1, "RESP"))
	cond0 = cond0  and  not (ElementPresent(ds , "SpecimenDescriptionSequence"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "BodyPartExamined", -1, "ABDOMEN"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "ABDOMENPELVIS"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "AORTA"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "BACK"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "BLADDER"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "BRAIN"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "CEREBELLUM"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "CSPINE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "CTSPINE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "CERVIX"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "CHEST"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "CHESTABDOMEN"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "CHESTABDPELVIS"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "CIRCLEOFWILLIS"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "COCCYX"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "COLON"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "CORONARYARTERY"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "DUODENUM"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "WHOLEBODY"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "ESOPHAGUS"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "FACE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "GALLBLADDER"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "HEAD"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "HEADNECK"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "HEART"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "ILEUM"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "ILIUM"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "JAW"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "JEJUNUM"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "LARYNX"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "LIVER"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "LSPINE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "LSSPINE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "JAW"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "MAXILLA"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "MEDIASTINUM"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "MOUTH"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "NECK"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "NECKCHEST"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "NECKCHESTABDOMEN"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "NECKCHESTABDPELV"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "NOSE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "PANCREAS"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "PELVIS"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "PENIS"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "PHARYNX"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "PROSTATE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "RECTUM"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "SSPINE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "SCALP"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "SKULL"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "SPINE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "SPLEEN"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "STERNUM"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "STOMACH"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "TSPINE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "TLSPINE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "THYMUS"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "THYROID"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "TONGUE"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "TRACHEA"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "URETER"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "URETHRA"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "UTERUS"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "VAGINA"))
	cond1 = cond1 or(StringValueMatch(ds , "BodyPartExamined", -1, "VULVA"))
	cond0 = cond0 and  not cond1
	cond1 = False
	cond2 = False
	cond2 = cond2  or (ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D4000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "R-FAB57"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-42500"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-41070"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-59490"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-42000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-42300"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-32602"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-32502"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-42100"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D2100"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-60610"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-74000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-DD123"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-A0100"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D6500"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-11501"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D00F7"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-83200"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D3000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "R-FAB55"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "R-FAB56"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-45526"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-11BF0"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-59300"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-42400"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-58200"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D0010"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-56000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-DD163"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-63000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D1100"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D1000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-32000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-58600"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-58400"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-59000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-24100"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-62000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-11503"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D00F9"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-28000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D3300"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-2300C"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D1600"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "R-FAB52"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "R-FAB53"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "R-FAB54"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-21000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-65000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-65010"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-65600"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D6000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "R-FAB58"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-91000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D2700"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-55002"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-20101"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-9200B"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-59600"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D4900"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-11AD0"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D1160"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D1460"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-59470"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-11000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-11100"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-58000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-A7010"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D0146"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-C3000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-46460"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-48890"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-11210"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-57000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-11218"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-42070"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-11502"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D00F8"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D3000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-C8000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-B6000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-53000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-25000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-DD006"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-F1810"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-D4230"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-48817"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-75000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-83000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-88920"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-82000"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodeValue", "AnatomicRegionSequence", -1, "T-81000"))
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "AnatomicRegionSequence", -1, "SRT"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "AnatomicRegionSequence", -1, "SNM3"))
	cond2 = cond2 or(ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "AnatomicRegionSequence", -1, "99SDM"))
	cond1 = cond1 and cond2
	cond0 = cond0 and  not cond1
	return cond0
def Condition_LossyImageCompressionMethodInconsistentWithTransferSyntax(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "LossyImageCompressionMethod"))
	cond0 = cond0  and (ElementPresent(ds , "TransferSyntaxUID"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.1"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.1.99"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.2"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.57"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.58"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.65"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.66"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.70"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.80"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.90"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.92"))
	cond1 = cond1 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.5"))
	cond0 = cond0 and  not cond1
	cond1 = False
	cond2 = False
	cond2 = cond2  or (StringValueMatch(ds , "LossyImageCompressionMethod", -1, "ISO_10918_1"))
	cond3 = False
	cond3 = cond3  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.50"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.51"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.52"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.53"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.54"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.55"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.56"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.59"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.60"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.61"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.62"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.63"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.64"))
	cond2 = cond2 and  not cond3
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (StringValueMatch(ds , "LossyImageCompressionMethod", -1, "ISO_14495_1"))
	cond3 = False
	cond3 = cond3  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.81"))
	cond2 = cond2 and  not cond3
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (StringValueMatch(ds , "LossyImageCompressionMethod", -1, "ISO_15444_1"))
	cond3 = False
	cond3 = cond3  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.91"))
	cond2 = cond2 and  not cond3
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (StringValueMatch(ds , "LossyImageCompressionMethod", -1, "ISO_15444_2"))
	cond3 = False
	cond3 = cond3  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.93"))
	cond2 = cond2 and  not cond3
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (StringValueMatch(ds , "LossyImageCompressionMethod", -1, "ISO_13818_2"))
	cond3 = False
	cond3 = cond3  or (StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.100"))
	cond3 = cond3 or(StringValueMatch(ds , "TransferSyntaxUID", -1, "1.2.840.10008.1.2.4.101"))
	cond2 = cond2 and  not cond3
	cond1 = cond1 or cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_UniversalEntityIDPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "UniversalEntityID"))
	return cond0
def Condition_UniversalEntityIDNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "UniversalEntityID"))
	return cond0
def Condition_LocalNamespaceEntityIDNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "LocalNamespaceEntityID"))
	return cond0
def Condition_CodeMeaningEmptyOrNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "CodeMeaning"))
	cond0 = cond0 or not (ValuePresent(ds , "CodeMeaning", -1))
	return cond0
def Condition_AnatomicRegionSequencePresentAndEmptyButBodyPartExaminedHasValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "AnatomicRegionSequence"))
	cond0 = cond0  and  not (SequenceHasItems(ds , "AnatomicRegionSequence"))
	cond0 = cond0  and (ValuePresent(ds , "BodyPartExamined", -1))
	return cond0
def Condition_ViewCodeSequenceAbsentOrEmptyButViewPositionHasValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ValuePresent(ds , "ViewPosition", -1))
	cond0 = cond0  and  not (SequenceHasItems(ds , "ViewCodeSequence"))
	return cond0
def Condition_InstanceIsNotAnImage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "PixelData"))
	cond0 = cond0  and  not (ElementPresent(ds , "PixelDataProviderURL"))
	return cond0
def Condition_SegmentationTypeIsBinary(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SegmentationType", -1, "BINARY"))
	return cond0
def Condition_SegmentationTypeIsNotBinary(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "SegmentationType", -1, "BINARY"))
	return cond0
def Condition_SegmentationTypeIsFractional(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SegmentationType", -1, "FRACTIONAL"))
	return cond0
def Condition_SegmentAlgorithmTypeIsNotManual(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "SegmentAlgorithmType", -1, "MANUAL"))
	return cond0
def Condition_InstancesAreReferencedAndStudiesContainingOtherReferencedInstancesSequenceAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "StudiesContainingOtherReferencedInstancesSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRootFirstItem(rootds , "ReferencedSOPInstanceUID", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "StereoPairsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "RegistrationSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "DeformableRegistrationSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "FiducialSetSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "ReferencedImageRealWorldValueMappingSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_InstancesAreReferencedAndReferencedSeriesSequenceAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedSeriesSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRootFirstItem(rootds , "ReferencedSOPInstanceUID", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "StereoPairsSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "RegistrationSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "DeformableRegistrationSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "FiducialSetSequence"))
	cond1 = cond1 or(ElementPresentInPathFromRoot(rootds , "ReferencedSOPInstanceUID", "ReferencedImageRealWorldValueMappingSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_NotSecondaryCaptureSOPClass(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "SOPClassUID", -1, SecondaryCaptureImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, MultiframeSingleBitSecondaryCaptureImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, MultiframeGrayscaleByteSecondaryCaptureImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, MultiframeGrayscaleWordSecondaryCaptureImageStorageSOPClassUID))
	cond0 = cond0  and  not (StringValueMatch(rootds , "SOPClassUID", -1, MultiframeTrueColorSecondaryCaptureImageStorageSOPClassUID))
	return cond0
def Condition_AcquisitionStartConditionDENS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionStartCondition", -1, "DENS"))
	return cond0
def Condition_AcquisitionStartConditionRDD(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionStartCondition", -1, "RDD"))
	return cond0
def Condition_AcquisitionStartConditionCARD_TRIG(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionStartCondition", -1, "CARD_TRIG"))
	return cond0
def Condition_AcquisitionStartConditionRESP_TRIG(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionStartCondition", -1, "RESP_TRIG"))
	return cond0
def Condition_AcquisitionTerminationConditionCNTS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionTerminationCondition", -1, "CNTS"))
	return cond0
def Condition_AcquisitionTerminationConditionDENS(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionTerminationCondition", -1, "DENS"))
	return cond0
def Condition_AcquisitionTerminationConditionRDD(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionTerminationCondition", -1, "RDD"))
	return cond0
def Condition_AcquisitionTerminationConditionTIME(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionTerminationCondition", -1, "TIME"))
	return cond0
def Condition_AcquisitionTerminationConditionCARD_TRIG(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionTerminationCondition", -1, "CARD_TRIG"))
	return cond0
def Condition_AcquisitionTerminationConditionRESP_TRIG(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "AcquisitionTerminationCondition", -1, "RESP_TRIG"))
	return cond0
def Condition_OriginalAndTypeOfDetectorMotionIsStationary(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 0, "ORIGINAL"))
	cond0 = cond0  and (StringValueMatch(ds , "TypeOfDetectorMotion", -1, "STATIONARY"))
	return cond0
def Condition_DetectorGeometryPresentAndTypeOfDetectorMotionIsNotStationary(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "DetectorGeometry"))
	cond0 = cond0  and  not (StringValueMatch(ds , "TypeOfDetectorMotion", -1, "STATIONARY"))
	return cond0
def Condition_IsRandomsCorrected(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "RandomsCorrected", -1, "YES"))
	return cond0
def Condition_IsAttenuationCorrected(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "AttenuationCorrected", -1, "YES"))
	return cond0
def Condition_IsScatterCorrected(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ScatterCorrected", -1, "YES"))
	return cond0
def Condition_IsDecayCorrected(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "DecayCorrected", -1, "YES"))
	return cond0
def Condition_IsIterativeReconstruction(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "IterativeReconstructionMethod", -1, "YES"))
	return cond0
def Condition_MultiEnergyProportionalWeighting(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementStringValueMatchWithin(ds , "CodeValue", "DerivationCodeSequence", -1, "113097"))
	cond0 = cond0  and (ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "DerivationCodeSequence", -1, "DCM"))
	return cond0
def Condition_EnergyWeightingFactorPresentInRoot(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "EnergyWeightingFactor"))
	return cond0
def Condition_ImageTypeValue1IsOriginal(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	return cond0
def Condition_ClinicalTrialProtocolEthicsCommitteeApprovalNumberIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ClinicalTrialProtocolEthicsCommitteeApprovalNumber"))
	return cond0
def Condition_ConsentForDistributionFlagIsYesOrWithdrawn(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ConsentForDistributionFlag", -1, "YES"))
	cond0 = cond0 or(StringValueMatch(ds , "ConsentForDistributionFlag", -1, "WITHDRAWN"))
	return cond0
def Condition_DistributionTypeIsNotNamedProtocol(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "DistributionType", -1, "NAMED_PROTOCOL"))
	return cond0
def Condition_FluenceModeIsNonStandard(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "FluenceMode", -1, "NON_STANDARD"))
	return cond0
def Condition_DoseSummationTypeIsNotMultiPlanAndReferencedRTPlanSequenceHasMultipleItems(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "DoseSummationType", -1, "MULTI_PLAN"))
	cond0 = cond0  and (SequenceHasMultipleItems(ds , "ReferencedRTPlanSequence"))
	return cond0
def Condition_DoseSummationTypeIsMultiPlanAndReferencedRTPlanSequenceHasLessThanTwoItems(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DoseSummationType", -1, "MULTI_PLAN"))
	cond1 = False
	cond1 = cond1  or  not (SequenceHasItems(ds , "ReferencedRTPlanSequence"))
	cond1 = cond1 or(SequenceHasOneItem(ds , "ReferencedRTPlanSequence"))
	cond0 = cond0 and cond1
	return cond0
def Condition_NeedSimpleFrameListInFrameExtractionModule(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "CalculatedFrameList"))
	cond0 = cond0  and  not (ElementPresent(ds , "TimeRange"))
	return cond0
def Condition_NeedCalculatedFrameListInFrameExtractionModule(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "SimpleFrameList"))
	cond0 = cond0  and  not (ElementPresent(ds , "TimeRange"))
	return cond0
def Condition_NeedTimeRangeInFrameExtractionModule(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "SimpleFrameList"))
	cond0 = cond0  and  not (ElementPresent(ds , "CalculatedFrameList"))
	return cond0
def Condition_NeedModuleFrameExtraction(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FrameExtractionSequence"))
	return cond0
def Condition_MydriaticAgentConcentrationIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "MydriaticAgentConcentration"))
	return cond0
def Condition_ImageTypeValue1DerivedAndImageTypeValue3MissingOrEmpty(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 0, "DERIVED"))
	cond1 = False
	cond1 = cond1  or  not (ValuePresent(ds , "ImageType", 2))
	cond1 = cond1 or(StringValueMatch(ds , "ImageType", 2, ""))
	cond0 = cond0 and cond1
	return cond0
def Condition_ImageTypeValue1NotDerivedAndImageTypeValueNotMissingOrEmpty(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(ds , "ImageType", 0, "DERIVED"))
	cond1 = False
	cond1 = cond1  or  not (ValuePresent(ds , "ImageType", 2))
	cond1 = cond1 or(StringValueMatch(ds , "ImageType", 2, ""))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_ASLContextIsControlLOrLabel(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ASLContext", -1, "CONTROL"))
	cond0 = cond0  or (StringValueMatch(ds , "ASLContext", -1, "LABEL"))
	return cond0
def Condition_ASLCrusherFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ASLCrusherFlag", -1, "YES"))
	return cond0
def Condition_ASLBolusCutoffFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ASLBolusCutoffFlag", -1, "YES"))
	return cond0
def Condition_GraphicTypeIsPOINT(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "GraphicType", -1, "POINT"))
	return cond0
def Condition_GraphicTypeIsCIRCLE(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "GraphicType", -1, "CIRCLE"))
	return cond0
def Condition_GraphicTypeIsELLIPSE(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "GraphicType", -1, "ELLIPSE"))
	return cond0
def Condition_GraphicTypeIsELLIPSOID(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "GraphicType", -1, "ELLIPSOID"))
	return cond0
def Condition_XRay3DReconstructionSequenceIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "XRay3DReconstructionSequence"))
	return cond0
def Condition_ModalityIsMG(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Modality", -1, "MG"))
	return cond0
def Condition_ViewModifierCodeSequenceIsMagnificationOrSpotCompression(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	return cond0
def Condition_FieldOfViewDimensionsInFloatPresentAndFieldOfViewShapeIsRectangle(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FieldOfViewDimensionsInFloat"))
	cond0 = cond0  and (StringValueMatch(ds , "FieldOfViewShape", -1, "StringValue="))
	return cond0
def Condition_FieldOfViewDimensionsInFloatPresentAndFieldOfViewShapeIsRound(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FieldOfViewDimensionsInFloat"))
	cond0 = cond0  and (StringValueMatch(ds , "FieldOfViewShape", -1, "StringValue="))
	return cond0
def Condition_FieldOfViewDimensionsInFloatPresentAndFieldOfViewShapeIsHexagon(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FieldOfViewDimensionsInFloat"))
	cond0 = cond0  and (StringValueMatch(ds , "FieldOfViewShape", -1, "StringValue="))
	return cond0
def Condition_NeedModuleBreastTomosynthesisContributingSources(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ContributingSourcesSequence"))
	return cond0
def Condition_NeedModuleBreastTomosynthesisAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "XRay3DAcquisitionSequence"))
	return cond0
def Condition_SurfaceProcessingIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SurfaceProcessing", -1, "StringValue="))
	return cond0
def Condition_AxisOfRotationIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "AxisOfRotation"))
	return cond0
def Condition_StudyInstanceUIDIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "StudyInstanceUID"))
	return cond0
def Condition_PositionerMotionIsPresentAndNumberOfFramesIsAbsentOrOne(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PositionerMotion"))
	cond1 = False
	cond1 = cond1  or  not (ElementPresent(ds , "NumberOfFrames"))
	cond1 = cond1 or(BinaryValueMatch(ds , "NumberOfFrames", -1, BinaryValueMatchOperator.Equals, 1))
	cond0 = cond0 and cond1
	return cond0
def Condition_RationalNumeratorValueIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RationalNumeratorValue"))
	return cond0
def Condition_FloatingPointValuePresentButValueTypeIsNotNumeric(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FloatingPointValue"))
	cond0 = cond0  and  not (StringValueMatch(ds , "ValueType", -1, "NUM"))
	return cond0
def Condition_RationalNumeratorValuePresentButValueTypeIsNotNumeric(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RationalNumeratorValue"))
	cond0 = cond0  and  not (StringValueMatch(ds , "ValueType", -1, "NUM"))
	return cond0
def Condition_RationalDenominatorValueButValueTypeIsNotNumeric(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RationalDenominatorValue"))
	cond0 = cond0  and  not (StringValueMatch(ds , "ValueType", -1, "NUM"))
	return cond0
def Condition_FloatingPointValuePresentButAcquisitionContextItemIsNotNumeric(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FloatingPointValue"))
	cond1 = False
	cond1 = cond1  or  not (StringValueMatch(ds , "ValueType", -1, "NUMERIC"))
	cond1 = cond1 or not (ElementPresent(ds , "NumericValue"))
	cond1 = cond1 or(ElementPresent(ds , "Time"))
	cond1 = cond1 or(ElementPresent(ds , "PersonName"))
	cond1 = cond1 or(ElementPresent(ds , "TextValue"))
	cond1 = cond1 or(ElementPresent(ds , "ConceptCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "Date"))
	cond0 = cond0 and cond1
	return cond0
def Condition_RationalNumeratorValuePresentButAcquisitionContextItemIsNotNumeric(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RationalNumeratorValue"))
	cond1 = False
	cond1 = cond1  or  not (StringValueMatch(ds , "ValueType", -1, "NUMERIC"))
	cond1 = cond1 or not (ElementPresent(ds , "NumericValue"))
	cond1 = cond1 or(ElementPresent(ds , "Time"))
	cond1 = cond1 or(ElementPresent(ds , "PersonName"))
	cond1 = cond1 or(ElementPresent(ds , "TextValue"))
	cond1 = cond1 or(ElementPresent(ds , "ConceptCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "Date"))
	cond0 = cond0 and cond1
	return cond0
def Condition_RationalDenominatorValuePresentButAcquisitionContextItemIsNotNumeric(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RationalDenominatorValue"))
	cond1 = False
	cond1 = cond1  or  not (StringValueMatch(ds , "ValueType", -1, "NUMERIC"))
	cond1 = cond1 or not (ElementPresent(ds , "NumericValue"))
	cond1 = cond1 or(ElementPresent(ds , "Time"))
	cond1 = cond1 or(ElementPresent(ds , "PersonName"))
	cond1 = cond1 or(ElementPresent(ds , "TextValue"))
	cond1 = cond1 or(ElementPresent(ds , "ConceptCodeSequence"))
	cond1 = cond1 or(ElementPresent(ds , "Date"))
	cond0 = cond0 and cond1
	return cond0
def Condition_DimensionIndexSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(rootds , "DimensionIndexSequence"))
	return cond0
def Condition_InStackPositionNumberIsZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "InStackPositionNumber", -1, BinaryValueMatchOperator.Equals, 0))
	return cond0
def Condition_TemporalPositionIndexIsZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "TemporalPositionIndex", -1, BinaryValueMatchOperator.Equals, 0))
	return cond0
def Condition_DimensionIndexValuesContainsZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "DimensionIndexValues", -1, BinaryValueMatchOperator.Equals, 0))
	return cond0
def Condition_WindowWidthIsNegative(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "WindowWidth", -1, BinaryValueMatchOperator.LessThan, 0))
	return cond0
def Condition_WindowWidthIsZeroAndSigmoid(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "WindowWidth", -1, BinaryValueMatchOperator.Equals, 0))
	cond0 = cond0  and (StringValueMatch(ds , "VOILUTFunction", -1, "SIGMOID"))
	return cond0
def Condition_WindowWidthIsLessThanOneAndNotExact(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "WindowWidth", -1, BinaryValueMatchOperator.LessThan, 1))
	cond0 = cond0  and  not (StringValueMatch(ds , "VOILUTFunction", -1, "LINEAR_EXACT"))
	cond0 = cond0  and  not (StringValueMatch(ds , "VOILUTFunction", -1, "SIGMOID"))
	return cond0
def Condition_IVUSAcquisitionIsMotorized(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "IVUSAcquisition", -1, "MOTORIZED"))
	return cond0
def Condition_IVUSAcquisitionIsMeasured(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "IVUSAcquisition", -1, "MEASURED"))
	return cond0
def Condition_IntravascularOCTFrameTypeSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "IntravascularOCTFrameTypeSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_IntravascularOCTFrameTypeSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "IntravascularOCTFrameTypeSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_IntravascularFrameContentSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "IntravascularFrameContentSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_IntravascularFrameContentSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "IntravascularFrameContentSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_IntravascularFrameContentSequenceNotInSharedFunctionalGroupSequenceAndAcquisitionIsMeasured(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "IntravascularFrameContentSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "IVUSAcquisition", -1, "MEASURED"))
	return cond0
def Condition_IntravascularFrameContentSequenceNotInPerFrameFunctionalGroupSequenceAndAcquisitionIsMeasured(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "IntravascularFrameContentSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "IVUSAcquisition", -1, "MEASURED"))
	return cond0
def Condition_IntravascularOCTFrameContentSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "IntravascularOCTFrameContentSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_IntravascularOCTFrameContentSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "IntravascularOCTFrameContentSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_PresentationIntentTypeIsForProcessing(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PresentationIntentType", -1, "FOR PROCESSING"))
	return cond0
def Condition_PresentationIntentTypeIsForPresentation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PresentationIntentType", -1, "FOR PRESENTATION"))
	return cond0
def Condition_PixelPresentationIsColorRef(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "PixelPresentation", -1, "COLOR_REF"))
	return cond0
def Condition_RotationalCatheterInformationIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CatheterDirectionOfRotation"))
	cond0 = cond0  or (ElementPresent(ds , "CatheterRotationalRate"))
	return cond0
def Condition_ImageBoxOverlapPriorityValueNot1To100(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ImageBoxOverlapPriority"))
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "ImageBoxOverlapPriority", -1, BinaryValueMatchOperator.LessThan, 1))
	cond1 = cond1  or (BinaryValueMatch(ds , "ImageBoxOverlapPriority", -1, BinaryValueMatchOperator.GreaterThan, 100))
	cond0 = cond0 and cond1
	return cond0
def Condition_RecommendedDisplayFrameRateNotGreaterThanZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "RecommendedDisplayFrameRate"))
	cond0 = cond0  and (BinaryValueMatch(ds , "RecommendedDisplayFrameRate", -1, BinaryValueMatchOperator.LessThan, 0))
	return cond0
def Condition_CineRelativeToRealTimeNotGreaterThanZero(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CineRelativeToRealTime"))
	cond0 = cond0  and (BinaryValueMatch(ds , "CineRelativeToRealTime", -1, BinaryValueMatchOperator.LessThan, 0))
	return cond0
def Condition_NoReferencedPresentationStateOrStereometricInstanceOrInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedPresentationStateSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedStereometricInstanceSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedInstanceSequence"))
	return cond0
def Condition_NoReferencedImageOrStereometricInstanceOrInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedImageSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedStereometricInstanceSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedInstanceSequence"))
	return cond0
def Condition_NoReferencedPresentationStateOrStereometricInstanceOrImage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedPresentationStateSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedStereometricInstanceSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedImageSequence"))
	return cond0
def Condition_NoReferencedPresentationStateOrInstanceOrImage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "ReferencedPresentationStateSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedInstanceSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "ReferencedImageSequence"))
	return cond0
def Condition_NeedModuleStructuredDisplayAnnotation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "StructuredDisplayTextBoxSequence"))
	return cond0
def Condition_ViewIsCardiacShortOrLongAxis(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ViewCodeSequence"))
	cond1 = False
	cond1 = cond1  or (ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "ViewCodeSequence", -1, "SRT"))
	cond1 = cond1 or(ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "ViewCodeSequence", -1, "SNM3"))
	cond1 = cond1 or(ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "ViewCodeSequence", -1, "99SDM"))
	cond0 = cond0 and cond1
	cond1 = False
	cond1 = cond1  or (ElementStringValueMatchWithin(ds , "CodeValue", "ViewCodeSequence", -1, "G-A186"))
	cond1 = cond1 or(ElementStringValueMatchWithin(ds , "CodeValue", "ViewCodeSequence", -1, "G-A18A"))
	cond1 = cond1 or(ElementStringValueMatchWithin(ds , "CodeValue", "ViewCodeSequence", -1, "G-A18B"))
	cond0 = cond0 and cond1
	return cond0
def Condition_ViewIsNotSpecimen(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ViewCodeSequence"))
	cond1 = False
	cond1 = cond1  or (ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "ViewCodeSequence", -1, "SRT"))
	cond1 = cond1 or(ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "ViewCodeSequence", -1, "SNM3"))
	cond1 = cond1 or(ElementStringValueMatchWithin(ds , "CodingSchemeDesignator", "ViewCodeSequence", -1, "99SDM"))
	cond0 = cond0 and cond1
	cond1 = False
	cond1 = cond1  or (ElementStringValueMatchWithin(ds , "CodeValue", "ViewCodeSequence", -1, "G-8310"))
	cond0 = cond0 and cond1
	return cond0
def Condition_UltrasoundAcquisitionGeometryIsApex(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "UltrasoundAcquisitionGeometry", -1, "APEX"))
	return cond0
def Condition_NeedPatientFrameOfReferenceSource(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentInPathFromRootFirstItem(rootds , "ImagePositionPatient", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "ImagePositionPatient", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "ImageOrientationPatient", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "ImageOrientationPatient", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_PatientFrameOfReferenceSourceIsTable(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PatientFrameOfReferenceSource", -1, "TABLE"))
	return cond0
def Condition_PerformedProtocolCodeSequenceIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PerformedProtocolCodeSequence"))
	return cond0
def Condition_NeedPositionMeasuringDeviceUsed(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "VolumetricProperties", -1, "VOLUME"))
	cond0 = cond0  and (StringValueMatch(ds , "VolumeBasedCalculationTechnique", -1, "NONE"))
	return cond0
def Condition_PerformedProtocolTypeIsStaged(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PerformedProtocolType", -1, "STAGED"))
	return cond0
def Condition_AnyDataPathAssignmentIsOtherThanPrimaryPValues(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementStringValueMatchWithin(ds , "DataPathAssignment", "DataFrameAssignmentSequence", -1, "PRIMARY_SINGLE"))
	cond0 = cond0 or(ElementStringValueMatchWithin(ds , "DataPathAssignment", "DataFrameAssignmentSequence", -1, "SECONDARY_SINGLE"))
	cond0 = cond0 or(ElementStringValueMatchWithin(ds , "DataPathAssignment", "DataFrameAssignmentSequence", -1, "SECONDARY_HIGH"))
	cond0 = cond0 or(ElementStringValueMatchWithin(ds , "DataPathAssignment", "DataFrameAssignmentSequence", -1, "SECONDARY_LOW"))
	return cond0
def Condition_BlendingLUT1TransferFunctionIsConstant(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "BlendingLUT1TransferFunction", -1, "CONSTANT"))
	return cond0
def Condition_BlendingLUT2TransferFunctionIsConstant(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "BlendingLUT2TransferFunction", -1, "CONSTANT"))
	return cond0
def Condition_BlendingLUT1TransferFunctionIsTable(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "BlendingLUT1TransferFunction", -1, "TABLE"))
	return cond0
def Condition_RGBLUTTransferFunctionIsTable(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "RGBLUTTransferFunction", -1, "TABLE"))
	return cond0
def Condition_NeedModuleEnhancedPaletteColorLookupTable(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "DataFrameAssignmentSequence"))
	cond0 = cond0  or (ElementPresent(ds , "BlendingLUT1Sequence"))
	cond0 = cond0  or (ElementPresent(ds , "BlendingLUT2Sequence"))
	cond0 = cond0  or (ElementPresent(ds , "EnhancedPaletteColorLookupTableSequence"))
	return cond0
def Condition_NeedModuleExcludedIntervals(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ExcludedIntervalsSequence"))
	return cond0
def Condition_ImageTypeValue3Localizer(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "LOCALIZER"))
	return cond0
def Condition_ImageTypeValue3Label(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "LABEL"))
	return cond0
def Condition_NeedModuleICCProfile(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ICCProfile"))
	return cond0
def Condition_NeedModuleOpticalPath(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "OpticalPathSequence"))
	return cond0
def Condition_SpecimenReferenceMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "SpecimenReferenceSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "SpecimenReferenceSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_SpecimenReferenceMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "SpecimenReferenceSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "SpecimenReferenceSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedPlanePositionSlideMacroInSharedFunctionalGroupSequenceForWholeSlideMicroscopy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "PlanePositionSlideSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "DimensionOrganizationType", 0, "TILED_FULL"))
	return cond0
def Condition_NeedPlanePositionSlideMacroInPerFrameFunctionalGroupSequenceForWholeSlideMicroscopy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "PlanePositionSlideSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "DimensionOrganizationType", 0, "TILED_FULL"))
	return cond0
def Condition_NeedOpticalPathIdentificationMacroInSharedFunctionalGroupSequenceForWholeSlideMicroscopy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "OpticalPathIdentificationSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRoot(rootds , "OpticalPathIdentificationSequence", "SharedFunctionalGroupsSequence"))
	cond1 = cond1 or not (StringValueMatch(rootds , "DimensionOrganizationType", 0, "TILED_FULL"))
	cond0 = cond0 and cond1
	return cond0
def Condition_NeedOpticalPathIdentificationMacroInPerFrameFunctionalGroupSequenceForWholeSlideMicroscopy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "OpticalPathIdentificationSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (ElementPresentInPathFromRootFirstItem(rootds , "OpticalPathIdentificationSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = cond1 or not (StringValueMatch(rootds , "DimensionOrganizationType", 0, "TILED_FULL"))
	cond0 = cond0 and cond1
	return cond0
def Condition_ImageTypeValue3LocalizerOrLabel(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "LOCALIZER"))
	cond0 = cond0 or(StringValueMatch(ds , "ImageType", 2, "LABEL"))
	return cond0
def Condition_ExtendedDepthOfFieldIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ExtendedDepthOfField", -1, "YES"))
	return cond0
def Condition_IlluminationColorCodeSequenceNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "IlluminationColorCodeSequence"))
	return cond0
def Condition_IlluminationWaveLengthNotPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "IlluminationWaveLength"))
	return cond0
def Condition_NeedICCProfileInOpticalPathSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PaletteColorLookupTableSequence"))
	cond0 = cond0 or not (StringValueMatch(rootds , "PhotometricInterpretation", -1, "MONOCHROME2"))
	return cond0
def Condition_NeedZeroVelocityPixelValue(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "DataType", -1, "TISSUE_VELOCITY"))
	cond0 = cond0  or (StringValueMatch(ds , "DataType", -1, "FLOW_VELOCITY"))
	cond0 = cond0  or (StringValueMatch(ds , "DataType", -1, "DIRECTION_POWER"))
	return cond0
def Condition_SpatialTransformOfDoseIsRigidOrNonRigid(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "SpatialTransformOfDose", -1, "RIGID"))
	cond0 = cond0  or (StringValueMatch(ds , "SpatialTransformOfDose", -1, "NON_RIGID"))
	return cond0
def Condition_PixelSpacingRequiredInPixelMeasures(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or (ElementPresent(rootds , "VolumetricProperties"))
	cond1 = cond1  and  not (StringValueMatch(rootds , "VolumetricProperties", -1, "DISTORTED"))
	cond1 = cond1  and  not (StringValueMatch(rootds , "VolumetricProperties", -1, "SAMPLED"))
	cond0 = cond0 or cond1
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "SOPClassUID", -1, SegmentationStorageSOPClassUID))
	cond1 = cond1  and (ElementPresent(rootds , "FrameOfReferenceUID"))
	cond0 = cond0 or cond1
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "SOPClassUID", -1, OphthalmicTomographyImageStorageSOPClassUID))
	cond1 = cond1  and (StringValueMatch(rootds , "OphthalmicVolumetricPropertiesFlag", -1, "YES"))
	cond0 = cond0 or cond1
	cond0 = cond0 or(StringValueMatch(rootds , "SOPClassUID", -1, OphthalmicOpticalCoherenceTomographyBscanVolumeAnalysisStorageSOPClassUID))
	return cond0
def Condition_SliceThicknessRequiredInPixelMeasures(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or (ElementPresent(rootds , "VolumetricProperties"))
	cond1 = cond1  and  not (StringValueMatch(rootds , "VolumetricProperties", -1, "DISTORTED"))
	cond1 = cond1  and  not (StringValueMatch(rootds , "VolumetricProperties", -1, "SAMPLED"))
	cond0 = cond0 or cond1
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "SOPClassUID", -1, SegmentationStorageSOPClassUID))
	cond1 = cond1  and (ElementPresent(rootds , "FrameOfReferenceUID"))
	cond0 = cond0 or cond1
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "SOPClassUID", -1, OphthalmicTomographyImageStorageSOPClassUID))
	cond1 = cond1  and (StringValueMatch(rootds , "OphthalmicVolumetricPropertiesFlag", -1, "YES"))
	cond0 = cond0 or cond1
	cond0 = cond0 or(StringValueMatch(rootds , "SOPClassUID", -1, OphthalmicOpticalCoherenceTomographyBscanVolumeAnalysisStorageSOPClassUID))
	return cond0
def Condition_ImagePositionPatientNotPresentInEitherSharedOrPerFrameFunctionalGroupsAndEitherFrameTypeIsOriginalAndVolumetricPropertiesIsNotDistortedOrSegmentationWithFrameOfReference(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "ImagePositionPatient", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "ImagePositionPatient", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond2 = False
	cond2 = cond2  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond2 = cond2  and  not (StringValueMatch(rootds , "VolumetricProperties", -1, "DISTORTED"))
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (StringValueMatch(rootds , "SOPClassUID", -1, SegmentationStorageSOPClassUID))
	cond2 = cond2  and (ElementPresent(rootds , "FrameOfReferenceUID"))
	cond1 = cond1 or cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_ImageOrientationPatientNotPresentInEitherSharedOrPerFrameFunctionalGroupsAndEitherFrameTypeIsOriginalAndVolumetricPropertiesIsNotDistortedOrSegmentationWithFrameOfReference(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "ImageOrientationPatient", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "ImageOrientationPatient", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond2 = False
	cond2 = cond2  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond2 = cond2  and  not (StringValueMatch(rootds , "VolumetricProperties", -1, "DISTORTED"))
	cond1 = cond1 or cond2
	cond2 = False
	cond2 = cond2  or (StringValueMatch(rootds , "SOPClassUID", -1, SegmentationStorageSOPClassUID))
	cond2 = cond2  and (ElementPresent(rootds , "FrameOfReferenceUID"))
	cond1 = cond1 or cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_BitsStoredPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "BitsStored"))
	return cond0
def Condition_HighBitPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "HighBit"))
	return cond0
def Condition_PixelRepresentationPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PixelRepresentation"))
	return cond0
def Condition_PlanarConfigurationPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PlanarConfiguration"))
	return cond0
def Condition_FloatPixelPaddingValuePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FloatPixelPaddingValue"))
	return cond0
def Condition_DoubleFloatPixelPaddingValuePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "DoubleFloatPixelPaddingValue"))
	return cond0
def Condition_ImageTypeValue3IsTissueIntensity(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 2, "TISSUE_INTENSITY"))
	return cond0
def Condition_ImageTypeValue3IsSoundSpeed(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 2, "SOUND_SPEED"))
	return cond0
def Condition_ImageTypeValue3IsAttenuation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 2, "ATTENUATION"))
	return cond0
def Condition_ImageTypeValue3IsSoundSpeedOrAttenuation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 2, "SOUND_SPEED"))
	cond0 = cond0 or(StringValueMatch(rootds , "ImageType", 2, "ATTENUATION"))
	return cond0
def Condition_VisualAcuityTypeCodeSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "VisualAcuityTypeCodeSequence"))
	return cond0
def Condition_RightLensSequenceAndLeftLensSequenceAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "RightLensSequence"))
	cond0 = cond0  and  not (ElementPresent(ds , "LeftLensSequence"))
	return cond0
def Condition_OptotypeIsLettersNumbersOrPictures(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "Optotype", -1, "LETTERS"))
	cond0 = cond0 or(StringValueMatch(ds , "Optotype", -1, "NUMBERS"))
	cond0 = cond0 or(StringValueMatch(ds , "Optotype", -1, "PICTURES"))
	return cond0
def Condition_OphthalmicAxialMeasurementsDeviceTypeIsUltrasound(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "OphthalmicAxialMeasurementsDeviceType", -1, "ULTRASOUND"))
	return cond0
def Condition_OphthalmicAxialMeasurementsDeviceTypeIsOptical(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "OphthalmicAxialMeasurementsDeviceType", -1, "OPTICAL"))
	return cond0
def Condition_MydriaticAgentConcentrationPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "MydriaticAgentConcentration"))
	return cond0
def Condition_OphthalmicAxialLengthMeasurementsTypeAboveIsTotalLength(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(parentds , "OphthalmicAxialLengthMeasurementsType", -1, "TOTAL LENGTH"))
	return cond0
def Condition_OphthalmicAxialLengthMeasurementsTypeIsTotalLength(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "OphthalmicAxialLengthMeasurementsType", -1, "TOTAL LENGTH"))
	return cond0
def Condition_OphthalmicAxialLengthMeasurementsTypeAboveIsLengthSummation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(parentds , "OphthalmicAxialLengthMeasurementsType", -1, "LENGTH SUMMATION"))
	return cond0
def Condition_OphthalmicAxialLengthMeasurementsTypeIsLengthSummation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "OphthalmicAxialLengthMeasurementsType", -1, "LENGTH SUMMATION"))
	return cond0
def Condition_OphthalmicAxialLengthMeasurementsTypeAboveIsSegmentalLength(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(parentds , "OphthalmicAxialLengthMeasurementsType", -1, "SEGMENTAL LENGTH"))
	return cond0
def Condition_OphthalmicAxialLengthMeasurementsTypeIsSegmentalLength(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "OphthalmicAxialLengthMeasurementsType", -1, "SEGMENTAL LENGTH"))
	return cond0
def Condition_RefractiveProcedureOccurredIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "RefractiveProcedureOccurred", -1, "YES"))
	return cond0
def Condition_ReferencedFrameNumberPresentAndReferencedSOPClassUIDIsNotMultiFrame(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ReferencedFrameNumber"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "ReferencedSOPClassUID", -1, NuclearMedicineImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, UltrasoundMultiframeImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, MultiframeSingleBitSecondaryCaptureImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, MultiframeGrayscaleByteSecondaryCaptureImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, MultiframeGrayscaleWordSecondaryCaptureImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, MultiframeTrueColorSecondaryCaptureImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, XRayAngiographicImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, XRayAngiographicBiplaneImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, XRayRadioFluoroscopicImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, RTImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, RTDoseStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, VideoEndoscopicImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, VideoMicroscopicImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, VideoPhotographicImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, VLWholeSlideMicroscopyImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, EnhancedMRImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, MRSpectroscopyStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, EnhancedMRColorImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, EnhancedCTImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, OphthalmicPhotography8BitImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, OphthalmicPhotography16BitImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, EnhancedXAImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, EnhancedXRFImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, SegmentationStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, OphthalmicTomographyImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, XRay3DAngiographicImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, XRay3DCraniofacialImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, BreastTomosynthesisImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, EnhancedPETImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, EnhancedUSVolumeStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, IVOCTImageStorageForProcessingSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, IVOCTImageStorageForPresentationSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, LegacyConvertedEnhancedCTImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, LegacyConvertedEnhancedMRImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, LegacyConvertedEnhancedPETImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, BreastProjectionXRayImageStorageForPresentationSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, BreastProjectionXRayImageStorageForProcessingSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, ParametricMapStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, WideFieldOphthalmicPhotographyStereographicProjectionImageStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, WideFieldOphthalmicPhotography3DCoordinatesImageStorageSOPClassUID))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_ReferencedSegmentNumberPresentAndReferencedSOPClassUIDIsNotSegmentationOrSurfaceSegmentation(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "ReferencedSegmentNumber"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "ReferencedSOPClassUID", -1, SurfaceSegmentationStorageSOPClassUID))
	cond1 = cond1 or(StringValueMatch(ds , "ReferencedSOPClassUID", -1, SegmentationStorageSOPClassUID))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_NeedDerivationImageMacroInSharedFunctionalGroupSequenceForBreastProjection(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "DerivationImageSequence", "PerFrameFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond2 = False
	cond2 = cond2  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond2 = cond2  and (StringValueMatch(rootds , "PresentationIntentType", -1, "FOR PRESENTATION"))
	cond1 = cond1 or cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_NeedDerivationImageMacroInPerFrameFunctionalGroupSequenceForBreastProjection(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "DerivationImageSequence", "SharedFunctionalGroupsSequence"))
	cond1 = False
	cond1 = cond1  or (StringValueMatch(rootds , "ImageType", 0, "DERIVED"))
	cond2 = False
	cond2 = cond2  or (StringValueMatch(rootds , "ImageType", 0, "ORIGINAL"))
	cond2 = cond2  and (StringValueMatch(rootds , "PresentationIntentType", -1, "FOR PRESENTATION"))
	cond1 = cond1 or cond2
	cond0 = cond0 and cond1
	return cond0
def Condition_NeedBreastXRayPositionerMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "PositionerPositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "PositionerPositionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedBreastXRayPositionerMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "PositionerPositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "PositionerPositionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_NeedBreastXRayDetectorMacroInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  and  not (ElementPresentInPathFromRootFirstItem(rootds , "DetectorPositionSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRoot(rootds , "DetectorPositionSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_NeedBreastXRayDetectorMacroInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  and  not (ElementPresentInPathFromRoot(rootds , "DetectorPositionSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0 or(ElementPresentInPathFromRootFirstItem(rootds , "DetectorPositionSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayGeometrySequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "XRayGeometrySequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayGeometrySequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "XRayGeometrySequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRayAcquisitionDoseSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "XRayAcquisitionDoseSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayAcquisitionDoseSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "XRayAcquisitionDoseSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_IsocenterReferenceSystemSequenceNotInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "IsocenterReferenceSystemSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_IsocenterReferenceSystemSequenceNotInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "IsocenterReferenceSystemSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRayGridMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "XRayGridSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "XRayGridSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayGridMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "XRayGridSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "XRayGridSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_XRayFilterMacroOKInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "XRayFilterSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRootFirstItem(rootds , "XRayFilterSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_XRayFilterMacroOKInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "XRayFilterSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (ElementPresentInPathFromRoot(rootds , "XRayFilterSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_AlternateBeamDosePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "AlternateBeamDose"))
	return cond0
def Condition_AlternateBeamDoseTypeSameValueAsBeamDoseType(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "AlternateBeamDose", -1, "PHYSICAL"))
	cond1 = cond1  and (StringValueMatch(ds , "BeamDoseType", -1, "PHYSICAL"))
	cond0 = cond0 or cond1
	cond1 = False
	cond1 = cond1  or (StringValueMatch(ds , "AlternateBeamDose", -1, "EFFECTIVE"))
	cond1 = cond1  and (StringValueMatch(ds , "BeamDoseType", -1, "EFFECTIVE"))
	cond0 = cond0 or cond1
	return cond0
def Condition_TrackingIDIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TrackingID"))
	return cond0
def Condition_TrackingUIDIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "TrackingUID"))
	return cond0
def Condition_ImageTypeValuesNotDBTThinThickGenerated2D(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "NumberOfFrames", -1, BinaryValueMatchOperator.GreaterThan, 1))
	cond1 = cond1  and (StringValueMatch(ds , "ImageType", 2, "TOMOSYNTHESIS"))
	cond2 = False
	cond2 = cond2  or (StringValueMatch(ds , "ImageType", 3, "NONE"))
	cond3 = False
	cond3 = cond3  or (StringValueMatch(ds , "ImageType", 0, "DERIVED"))
	cond4 = False
	cond4 = cond4  or (StringValueMatch(ds , "ImageType", 3, "MAXIMUM"))
	cond4 = cond4 or(StringValueMatch(ds , "ImageType", 3, "MEAN"))
	cond4 = cond4 or(StringValueMatch(ds , "ImageType", 3, "SUBTRACTION"))
	cond4 = cond4 or(StringValueMatch(ds , "ImageType", 3, "ADDITION"))
	cond3 = cond3 and cond4
	cond2 = cond2 or cond3
	cond1 = cond1 and cond2
	cond0 = cond0 or  not cond1
	cond1 = False
	cond1 = cond1  or (BinaryValueMatch(ds , "NumberOfFrames", -1, BinaryValueMatchOperator.Equals, 1))
	cond1 = cond1  or (StringValueMatch(ds , "ImageType", 0, "DERIVED"))
	cond1 = cond1  and (StringValueMatch(ds , "ImageType", 2, "TOMOSYNTHESIS"))
	cond1 = cond1  and (StringValueMatch(ds , "ImageType", 3, "GENERATED_2D"))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_PixelPresentationIsColorRange(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PixelPresentation", -1, "COLOR_RANGE"))
	return cond0
def Condition_PixelPresentationIsColorRangeAndPaletteColorLookupTableModuleAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PixelPresentation", -1, "COLOR_RANGE"))
	cond1 = False
	cond1 = cond1  or (ElementPresent(ds , "RedPaletteColorLookupTableData"))
	cond1 = cond1 or(ElementPresent(ds , "GreenPaletteColorLookupTableData"))
	cond1 = cond1 or(ElementPresent(ds , "BluePaletteColorLookupTableData"))
	cond1 = cond1 or(ElementPresent(ds , "SegmentedRedPaletteColorLookupTableData"))
	cond1 = cond1 or(ElementPresent(ds , "SegmentedGreenPaletteColorLookupTableData"))
	cond1 = cond1 or(ElementPresent(ds , "SegmentedBluePaletteColorLookupTableData"))
	cond1 = cond1 or(ElementPresent(ds , "RedPaletteColorLookupTableDescriptor"))
	cond1 = cond1 or(ElementPresent(ds , "GreenPaletteColorLookupTableDescriptor"))
	cond1 = cond1 or(ElementPresent(ds , "BluePaletteColorLookupTableDescriptor"))
	cond0 = cond0 and  not cond1
	return cond0
def Condition_PixelPresentationIsColorRangeAndPaletteColorLookupTableUIDAbsent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PixelPresentation", -1, "COLOR_RANGE"))
	cond0 = cond0  and  not (ElementPresent(ds , "PaletteColorLookupTableUID"))
	return cond0
def Condition_StoredValueColorRangeSequenceNotInPerFrameFunctionalGroupSequenceAndPixelPresentationIsColorRange(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRootFirstItem(rootds , "StoredValueColorRangeSequence", "PerFrameFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "PixelPresentation", -1, "COLOR_RANGE"))
	return cond0
def Condition_StoredValueColorRangeSequenceNotInSharedFunctionalGroupSequenceAndPixelPresentationIsColorRange(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentInPathFromRoot(rootds , "StoredValueColorRangeSequence", "SharedFunctionalGroupsSequence"))
	cond0 = cond0  and (StringValueMatch(rootds , "PixelPresentation", -1, "COLOR_RANGE"))
	return cond0
def Condition_WaterEquivalentDiameterIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "WaterEquivalentDiameter"))
	return cond0
def Condition_CTDIvolIsPresentButCTDIPhantomTypeCodeSequenceIsNot(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "CTDIvol"))
	cond0 = cond0  and  not (ElementPresent(ds , "CTDIPhantomTypeCodeSequence"))
	return cond0
def Condition_UnassignedSharedConvertedAttributesMacroPresentInSharedFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentInPathFromRoot(rootds , "UnassignedSharedConvertedAttributesSequence", "SharedFunctionalGroupsSequence"))
	return cond0
def Condition_UnassignedPerFrameConvertedAttributesMacroPresentInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentInPathFromRootFirstItem(rootds , "UnassignedPerFrameConvertedAttributesSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_ImageFrameConversionSourceMacroPresentInPerFrameFunctionalGroupSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresentInPathFromRootFirstItem(rootds , "ConversionSourceAttributesSequence", "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_IlluminationWaveLengthInvalid(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (BinaryValueMatch(ds , "IlluminationWaveLength", -1, BinaryValueMatchOperator.LessThanOrEquals, 0))
	return cond0
def Condition_NeedModuleSlideLabel(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ImageType", 2, "LABEL"))
	cond0 = cond0  or (ElementPresent(ds , "BarcodeValue"))
	cond0 = cond0  or (ElementPresent(ds , "LabelText"))
	return cond0
def Condition_LongitudinalTemporalOffsetFromEventIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "LongitudinalTemporalOffsetFromEvent"))
	return cond0
def Condition_NeedRecommendedDisplayCIELabValueListInTrackSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "RecommendedDisplayCIELabValue"))
	cond0 = cond0  and  not (ElementPresentAbove(parentds , "RecommendedDisplayCIELabValue"))
	return cond0
def Condition_NeedRecommendedDisplayCIELabValueInTrackSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresent(ds , "RecommendedDisplayCIELabValueList"))
	cond0 = cond0  and  not (ElementPresentAbove(parentds , "RecommendedDisplayCIELabValue"))
	return cond0
def Condition_NeedRecommendedDisplayCIELabValueInTrackSetSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (ElementPresentWithin(ds , "RecommendedDisplayCIELabValueList", "TrackSequence"))
	cond0 = cond0  and  not (ElementPresentWithin(ds , "RecommendedDisplayCIELabValue", "TrackSequence"))
	return cond0
def Condition_PerFrameFunctionalGroupsSequencePresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "PerFrameFunctionalGroupsSequence"))
	return cond0
def Condition_FrameContentMacroPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "FrameContentSequence"))
	return cond0
def Condition_DimensionOrganizationTypeIsTILED_FULL(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "DimensionOrganizationType", 0, "TILED_FULL"))
	return cond0
def Condition_DimensionOrganizationTypeIsNotTILED_FULL(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (StringValueMatch(rootds , "DimensionOrganizationType", 0, "TILED_FULL"))
	return cond0
def Condition_DimensionOrganizationTypeIsTILED_FULLAndTotalPixelMatrixFocalPlanesGreaterThanOne(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "DimensionOrganizationType", 0, "TILED_FULL"))
	cond0 = cond0  and (BinaryValueMatch(ds , "TotalPixelMatrixFocalPlanes", -1, BinaryValueMatchOperator.GreaterThan, 1))
	return cond0
def Condition_ReferencedSOPClassUIDIsSegmentationStorage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ReferencedSOPClassUID", -1, SegmentationStorageSOPClassUID))
	return cond0
def Condition_ReferencedSOPClassUIDIsSpatialFiducialsStorage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ReferencedSOPClassUID", -1, SpatialFiducialsStorageSOPClassUID))
	return cond0
def Condition_ReferencedSOPClassUIDIsRTStructureSetStorage(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ReferencedSOPClassUID", -1, RTStructureSetStorageSOPClassUID))
	return cond0
def Condition_ExcessiveFalsePositivesDataFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ExcessiveFalsePositivesDataFlag", -1, "YES"))
	return cond0
def Condition_FalsePositivesEstimateFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "FalsePositivesEstimateFlag", -1, "YES"))
	return cond0
def Condition_ExcessiveFalseNegativesDataFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ExcessiveFalseNegativesDataFlag", -1, "YES"))
	return cond0
def Condition_FalseNegativesEstimateFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "FalseNegativesEstimateFlag", -1, "YES"))
	return cond0
def Condition_CatchTrialsDataFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CatchTrialsDataFlag", -1, "YES"))
	return cond0
def Condition_ExcessiveFixationLossesDataFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ExcessiveFixationLossesDataFlag", -1, "YES"))
	return cond0
def Condition_IndexNormalsFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "IndexNormalsFlag", -1, "YES"))
	return cond0
def Condition_TestPointNormalsDataFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "TestPointNormalsDataFlag", -1, "YES"))
	return cond0
def Condition_GeneralizedDefectCorrectedSensitivityDeviationFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "GeneralizedDefectCorrectedSensitivityDeviationFlag", -1, "YES"))
	return cond0
def Condition_BlindSpotLocalizedIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "BlindSpotLocalized", -1, "YES"))
	return cond0
def Condition_ScreeningBaselineMeasuredIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ScreeningBaselineMeasured", -1, "YES"))
	return cond0
def Condition_FovealPointNormativeDataFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "FovealPointNormativeDataFlag", -1, "YES"))
	return cond0
def Condition_FovealSensitivityMeasuredIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "FovealSensitivityMeasured", -1, "YES"))
	return cond0
def Condition_PresentedVisualStimuliDataFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PresentedVisualStimuliDataFlag", -1, "YES"))
	return cond0
def Condition_LocalDeviationProbabilityNormalsFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "LocalDeviationProbabilityNormalsFlag", -1, "YES"))
	return cond0
def Condition_GlobalDeviationProbabilityNormalsFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "GlobalDeviationProbabilityNormalsFlag", -1, "YES"))
	return cond0
def Condition_VisualFieldTestNormalsFlagIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "VisualFieldTestNormalsFlag", -1, "YES"))
	return cond0
def Condition_ShortTermFluctuationCalculatedIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ShortTermFluctuationCalculated", -1, "YES"))
	return cond0
def Condition_ShortTermFluctuationProbabilityCalculatedIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "ShortTermFluctuationProbabilityCalculated", -1, "YES"))
	return cond0
def Condition_CorrectedLocalizedDeviationFromNormalCalculatedIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CorrectedLocalizedDeviationFromNormalCalculated", -1, "YES"))
	return cond0
def Condition_CorrectedLocalizedDeviationFromNormalProbabilityCalculatedIsYes(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "CorrectedLocalizedDeviationFromNormalProbabilityCalculated", -1, "YES"))
	return cond0
def Condition_MeasurementLateralityLeftOrBoth(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "MeasurementLaterality", -1, "L"))
	cond0 = cond0  or (StringValueMatch(ds , "MeasurementLaterality", -1, "B"))
	return cond0
def Condition_MeasurementLateralityRightOrBoth(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "MeasurementLaterality", -1, "R"))
	cond0 = cond0  or (StringValueMatch(ds , "MeasurementLaterality", -1, "B"))
	return cond0
def Condition_PrivateDataElementValueRepresentationIsSequence(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "PrivateDataElementValueRepresentation", -1, "SQ"))
	return cond0
def Condition_BlockIdentifyingInformationStatusIsMIXED(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "BlockIdentifyingInformationStatus", -1, "MIXED"))
	return cond0
def Condition_NeedAnatomicRegionSequenceInGeneralImageModule(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalXRayImageStorageForProcessingSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalMammographyXRayImageStorageForProcessingSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalIntraoralXRayImageStorageForProcessingSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalXRayImageStorageForPresentationSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalMammographyXRayImageStorageForPresentationSOPClassUID))
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, DigitalIntraoralXRayImageStorageForPresentationSOPClassUID))
	return cond0
def Condition_SelectorSequencePointerIsPresent(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (ElementPresent(ds , "SelectorSequencePointer"))
	return cond0
def Condition_ReferencedFrameNumberOrReferencedFrameNumbersPresentButNMImageInstance(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "SOPClassUID", -1, NuclearMedicineImageStorageSOPClassUID))
	cond1 = False
	cond1 = cond1  or (ElementPresent(ds , "ReferencedFrameNumber"))
	cond1 = cond1 or(ElementPresent(ds , "ReferencedFrameNumbers"))
	cond0 = cond0 and cond1
	return cond0
def Condition_IsMultienergyCTAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	return cond0
def Condition_ImageTypeValue4MissingOrEmptyForMultienergy(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	cond1 = False
	cond1 = cond1  or  not (ValuePresent(ds , "ImageType", 3))
	cond1 = cond1 or(StringValueMatch(ds , "ImageType", 3, ""))
	cond0 = cond0 and cond1
	return cond0
def Condition_ImageTypeValue4IsVMI(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(rootds , "ImageType", 3, "VMI"))
	return cond0
def Condition_MultienergySourceTechniqueIsSWITCHING_SOURCE(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "MultienergySourceTechnique", -1, "SWITCHING_SOURCE"))
	return cond0
def Condition_MultienergyDetectorTypeIsPHOTON_COUNTING(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or (StringValueMatch(ds , "MultienergyDetectorType", -1, "PHOTON_COUNTING"))
	return cond0
def Condition_CTAcquisitionDetailsSequenceNotOneItemAndNotMultienergyAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (SequenceHasOneItem(ds , "CTAcquisitionDetailsSequence"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	return cond0
def Condition_CTGeometrySequenceNotOneItemAndNotMultienergyAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (SequenceHasOneItem(ds , "CTGeometrySequence"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	return cond0
def Condition_CTExposureSequenceNotOneItemAndNotMultienergyAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (SequenceHasOneItem(ds , "CTExposureSequence"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	return cond0
def Condition_CTXRayDetailsSequenceNotOneItemAndNotMultienergyAcquisition(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:
	cond0 = False
	cond0 = cond0  or  not (SequenceHasOneItem(ds , "CTXRayDetailsSequence"))
	cond0 = cond0  and  not (StringValueMatch(rootds , "MultienergyCTAcquisition", -1, "YES"))
	return cond0
