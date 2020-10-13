CompositeIOD="CRImage"			Condition="CRImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="CRSeries"					Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="C"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="CRImage"					Usage="M"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="ModalityLUT"				Usage="U"	Condition="NeedModuleModalityLUT"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="CTImage"			Condition="CTImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePlane"					Usage="M"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="C"	Condition="NeedModuleContrastBolus"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="CTImage"					Usage="M"
		Module="MultienergyCTImage"			Usage="C"	Condition="IsMultienergyCTAcquisition"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MRImage"			Condition="MRImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePlane"					Usage="M"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="C"	Condition="NeedModuleContrastBolus"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="MRImage"					Usage="M"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="NMImage"			Condition="NMImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="NMPETPatientOrientation"	Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="AcquisitionContext"			Usage="U"	Condition="NeedModuleAcquisitionContext"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="NMImagePixel"				Usage="M"
		Module="MultiFrame"					Usage="M"
		Module="NMMultiFrame"				Usage="M"
		Module="NMImage"					Usage="M"
		Module="NMIsotope"					Usage="M"
		Module="NMDetector"					Usage="M"
		Module="NMTomoAcquisition"			Usage="C"	Condition="NeedModuleNMTomoAcquisition"
		Module="NMMultiGatedAcquisition"	Usage="C"	Condition="NeedModuleNMMultiGatedAcquisition"
		Module="NMPhase"					Usage="C"	Condition="NeedModuleNMPhase"
		Module="NMReconstruction"			Usage="C"	Condition="NeedModuleNMReconstruction"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="MultiFrameOverlay"			Usage="U"	Condition="NeedModuleMultiFrameOverlay"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"			Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="USImage"			Condition="USImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
		Module="Synchronization"			Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="C"	Condition="NeedModuleContrastBolus"
		Module="PaletteColorLookupTable"	Usage="C"	Condition="PhotometricInterpretationIsPaletteColor"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="USRegionCalibration"		Usage="U"	Condition="NeedModuleUSRegionCalibration"
		Module="USImage"					Usage="M"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="USMultiFrameImage"	Condition="USMultiFrameImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
		Module="Synchronization"			Usage="C"	Condition="NeedModuleSynchronizationForIVUS"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="C"	Condition="NeedModuleContrastBolus"
		Module="Cine"						Usage="M"
		Module="MultiFrame"					Usage="M"
		Module="FramePointers"				Usage="U"	Condition="NeedModuleFramePointers"
		Module="PaletteColorLookupTable"	Usage="C"	Condition="PhotometricInterpretationIsPaletteColor"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="USRegionCalibration"		Usage="U"	Condition="NeedModuleUSRegionCalibration"
		Module="USImage"					Usage="M"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"			Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="SCImage"			Condition="SCImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="U"	Condition="NeedModuleGeneralEquipment"
		Module="SCEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="SCImage"					Usage="M"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="ModalityLUT"				Usage="U"	Condition="NeedModuleModalityLUT"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MultiframeSingleBitSCImage"			Condition="MultiframeSingleBitSCImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"				Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"							Usage="M"
		Module="ClinicalTrialSubject"				Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"						Usage="M"
		Module="PatientStudy"						Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"					Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"						Usage="M"
		Module="ClinicalTrialSeries"				Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"					Usage="U"	Condition="NeedModuleGeneralEquipment"
		Module="SCEquipment"						Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"						Usage="M"
		Module="GeneralReference"					Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"							Usage="M"
		Module="Cine"								Usage="C"	Condition="NeedModuleCineForSC"
		Module="MultiFrame"							Usage="M"
		Module="FramePointers"						Usage="U"	Condition="NeedModuleFramePointers"
		Module="Device"								Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"							Usage="U"	Condition="NeedModuleSpecimen"
		Module="SCImage"							Usage="U"
		Module="SCMultiFrameImage"					Usage="M"
		Module="SCMultiFrameVector"					Usage="C"	Condition="NumberOfFramesGreaterThanOne"
		Module="SOPCommon"							Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"						Usage="C"	Condition="NeedModuleFrameExtraction"
		Module="MultiframeSingleBitSCImagePseudo"	Usage="M"
		# how to forbid presence of VOI LUT Module and Overlay Module :( ?
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MultiframeGrayscaleByteSCImage"			Condition="MultiframeGrayscaleByteSCImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"					Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"								Usage="M"
		Module="ClinicalTrialSubject"					Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"							Usage="M"
		Module="PatientStudy"							Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"						Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"							Usage="M"
		Module="ClinicalTrialSeries"					Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"						Usage="C"	Condition="PixelMeasuresOrPlanePositionOrPlaneOrientationSequenceIsPresent"
		Module="Synchronization"						Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"						Usage="U"	Condition="NeedModuleGeneralEquipment"
		Module="SCEquipment"							Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"							Usage="M"
		Module="GeneralReference"						Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"								Usage="M"
		Module="Cine"									Usage="C"	Condition="NeedModuleCineForSC"
		Module="MultiFrame"								Usage="M"
		Module="FramePointers"							Usage="U"	Condition="NeedModuleFramePointers"
		Module="Device"									Usage="U"	Condition="NeedModuleDevice"
		Module="MultiFrameFunctionalGroupsCommon"		Usage="U"	Condition="MultiFrameFunctionalGroupsModuleIsPresent"
		Module="MultiFrameFunctionalGroupsForMFSC"		Usage="U"	Condition="MultiFrameFunctionalGroupsModuleIsPresent"
		Module="MultiFrameDimension"					Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="Specimen"								Usage="U"	Condition="NeedModuleSpecimen"
		Module="SCImage"								Usage="U"
		Module="SCMultiFrameImage"						Usage="M"
		Module="SCMultiFrameVector"						Usage="C"	Condition="NumberOfFramesGreaterThanOne"
		Module="VOILUT"									Usage="C"	Condition="NeedModuleVOILUT"
		Module="SOPCommon"								Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"						Usage="C"	Condition="NeedModuleFrameExtraction"
		Module="MultiframeGrayscaleByteSCImagePseudo"	Usage="M"
		# how to forbid presence of Overlay Module :( ?
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MultiframeGrayscaleWordSCImage"			Condition="MultiframeGrayscaleWordSCImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"					Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"								Usage="M"
		Module="ClinicalTrialSubject"					Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"							Usage="M"
		Module="PatientStudy"							Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"						Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"							Usage="M"
		Module="ClinicalTrialSeries"					Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"						Usage="C"	Condition="PixelMeasuresOrPlanePositionOrPlaneOrientationSequenceIsPresent"
		Module="Synchronization"						Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"						Usage="U"	Condition="NeedModuleGeneralEquipment"
		Module="SCEquipment"							Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"							Usage="M"
		Module="GeneralReference"						Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"								Usage="M"
		Module="Cine"									Usage="C"	Condition="NeedModuleCineForSC"
		Module="MultiFrame"								Usage="M"
		Module="FramePointers"							Usage="U"
		Module="Device"									Usage="U"	Condition="NeedModuleDevice"
		Module="MultiFrameFunctionalGroupsCommon"		Usage="U"	Condition="MultiFrameFunctionalGroupsModuleIsPresent"
		Module="MultiFrameFunctionalGroupsForMFSC"		Usage="U"	Condition="MultiFrameFunctionalGroupsModuleIsPresent"
		Module="MultiFrameDimension"					Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="Specimen"								Usage="U"	Condition="NeedModuleSpecimen"
		Module="SCImage"								Usage="U"
		Module="SCMultiFrameImage"						Usage="M"
		Module="SCMultiFrameVector"						Usage="C"	Condition="NumberOfFramesGreaterThanOne"
		Module="VOILUT"									Usage="C"	Condition="NeedModuleVOILUT"
		Module="SOPCommon"								Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"						Usage="C"	Condition="NeedModuleFrameExtraction"
		Module="MultiframeGrayscaleWordSCImagePseudo"	Usage="M"
		# how to forbid presence of Overlay Module :( ?
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MultiframeTrueColorSCImage"				Condition="MultiframeTrueColorSCImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"					Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"								Usage="M"
		Module="ClinicalTrialSubject"					Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"							Usage="M"
		Module="PatientStudy"							Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"						Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"							Usage="M"
		Module="ClinicalTrialSeries"					Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"						Usage="C"	Condition="PixelMeasuresOrPlanePositionOrPlaneOrientationSequenceIsPresent"
		Module="Synchronization"						Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"						Usage="U"	Condition="NeedModuleGeneralEquipment"
		Module="SCEquipment"							Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"							Usage="M"
		Module="GeneralReference"						Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"								Usage="M"
		Module="Cine"									Usage="C"	Condition="NeedModuleCineForSC"
		Module="MultiFrame"								Usage="M"
		Module="FramePointers"							Usage="U"
		Module="Device"									Usage="U"	Condition="NeedModuleDevice"
		Module="MultiFrameFunctionalGroupsCommon"		Usage="U"	Condition="MultiFrameFunctionalGroupsModuleIsPresent"
		Module="MultiFrameFunctionalGroupsForMFSC"		Usage="U"	Condition="MultiFrameFunctionalGroupsModuleIsPresent"
		Module="MultiFrameDimension"					Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="Specimen"								Usage="U"	Condition="NeedModuleSpecimen"
		Module="SCImage"								Usage="U"
		Module="SCMultiFrameImage"						Usage="M"
		Module="SCMultiFrameVector"						Usage="C"	Condition="NumberOfFramesGreaterThanOne"
		Module="ICCProfile"								Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"								Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"						Usage="C"	Condition="NeedModuleFrameExtraction"
		Module="MultiframeTrueColorSCImagePseudo"		Usage="M"
		# how to forbid presence of VOI LUT Module and Overlay Module :( ?
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="StandaloneOverlay"		Condition="StandaloneOverlayInstance"	Retired="true"
	InformationEntity="File"
		Module="FileMetaInformation"	Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"				Usage="M"
		Module="ClinicalTrialSubject"	Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"			Usage="M"
		Module="PatientStudy"			Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"		Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"			Usage="M"
		Module="ClinicalTrialSeries"	Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"		Usage="M"
	InformationEntityEnd
	InformationEntity="Overlay"
		Module="OverlayIdentification"	Usage="M"
		Module="OverlayPlane"			Usage="M"
		Module="SOPCommon"				Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="StandaloneCurve"			Condition="StandaloneCurveInstance"	Retired="true"
	InformationEntity="File"
		Module="FileMetaInformation"	Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"				Usage="M"
		Module="ClinicalTrialSubject"	Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"			Usage="M"
		Module="PatientStudy"			Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"		Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"			Usage="M"
		Module="ClinicalTrialSeries"	Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"		Usage="M"
	InformationEntityEnd
	InformationEntity="Curve"
		Module="CurveIdentification"	Usage="M"
		Module="Curve"					Usage="M"
		Module="SOPCommon"				Usage="M"
	InformationEntityEnd
CompositeIODEnd


CompositeIOD="StandaloneModalityLUT"	Condition="StandaloneModalityLUTInstance"	Retired="true"
	InformationEntity="File"
		Module="FileMetaInformation"	Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"				Usage="M"
		Module="ClinicalTrialSubject"	Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"			Usage="M"
		Module="PatientStudy"			Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"		Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"			Usage="M"
		Module="ClinicalTrialSeries"	Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"		Usage="M"
	InformationEntityEnd
	InformationEntity="ModalityLUT"
		Module="ModalityLUT"			Usage="M"
		Module="LUTIdentification"		Usage="M"
		Module="SOPCommon"				Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="StandaloneVOILUT"			Condition="StandaloneVOILUTInstance"	Retired="true"
	InformationEntity="File"
		Module="FileMetaInformation"	Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"				Usage="M"
		Module="ClinicalTrialSubject"	Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"			Usage="M"
		Module="PatientStudy"			Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"		Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"			Usage="M"
		Module="ClinicalTrialSeries"	Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"		Usage="M"
	InformationEntityEnd
	InformationEntity="VOILUT"
		Module="VOILUT"					Usage="M"
		Module="LUTIdentification"		Usage="M"
		Module="SOPCommon"				Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="Segmentation"				Condition="SegmentationInstance"
	InformationEntity="File"
		Module="FileMetaInformation"					Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"								Usage="M"
		Module="ClinicalTrialSubject"					Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"							Usage="M"
		Module="PatientStudy"							Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"						Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"							Usage="M"
		Module="ClinicalTrialSeries"					Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="SegmentationSeries"						Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"						Usage="C"	Condition="DerivationImageFunctionalGroupNotPresentOrFrameOfReferenceUIDPresent"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"						Usage="M"
		Module="EnhancedGeneralEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"									Usage="M"
		Module="GeneralReference"								Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"										Usage="M"
		Module="SegmentationImage"								Usage="M"
		Module="CommonInstanceReference"						Usage="C"	Condition="DerivationImageFunctionalGroupPresent"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForSegmentation"		Usage="M"
		Module="MultiFrameDimension"							Usage="M"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="SOPCommon"										Usage="M"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
		# how to forbid presence of VOI LUT Module and Overlay Module :( ?
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="SurfaceSegmentation"				Condition="SurfaceSegmentationInstance"
	InformationEntity="File"
		Module="FileMetaInformation"					Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"								Usage="M"
		Module="ClinicalTrialSubject"					Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"							Usage="M"
		Module="PatientStudy"							Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"						Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"							Usage="M"
		Module="ClinicalTrialSeries"					Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="SegmentationSeries"						Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"						Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"						Usage="M"
		Module="EnhancedGeneralEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="Surface"
		Module="SurfaceSegmentation"					Usage="M"
		Module="SurfaceMesh"							Usage="M"
		Module="CommonInstanceReference"				Usage="C"	Condition="NeedModuleCommonInstanceReference"
		Module="GeneralReference"						Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"								Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="SpatialRegistration"			Condition="SpatialRegistrationInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="SpatialRegistrationSeries"	Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="SpatialRegistration"
		Module="SpatialRegistration"		Usage="M"
		Module="CommonInstanceReference"	Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="DeformableSpatialRegistration"			Condition="DeformableSpatialRegistrationInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="SpatialRegistrationSeries"	Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
		Module="EnhancedGeneralEquipment"	Usage="M"
	InformationEntityEnd
	InformationEntity="SpatialRegistration"
		Module="DeformableSpatialRegistration"	Usage="M"
		Module="CommonInstanceReference"		Usage="M"
		Module="GeneralReference"				Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"						Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="SpatialFiducials"				Condition="SpatialFiducialsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="SpatialFiducialsSeries"		Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="SpatialFiducials"
		Module="SpatialFiducials"			Usage="M"
		Module="CommonInstanceReference"	Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EncapsulatedPDF"				Condition="EncapsulatedPDFInstance"
	InformationEntity="File"
		Module="FileMetaInformation"			Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"						Usage="M"
		Module="ClinicalTrialSubject"			Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"					Usage="M"
		Module="PatientStudy"					Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"				Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="EncapsulatedDocumentSeries"		Usage="M"
		Module="ClinicalTrialSeries"			Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"				Usage="M"
		Module="SCEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="EncapsulatedDocument"
		Module="EncapsulatedDocument"			Usage="M"
		Module="EncapsulatedDocumentPDFPseudo"	Usage="M"
		Module="SOPCommon"						Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EncapsulatedCDA"					Condition="EncapsulatedCDAInstance"
	InformationEntity="File"
		Module="FileMetaInformation"			Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"						Usage="M"
		Module="ClinicalTrialSubject"			Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"					Usage="M"
		Module="PatientStudy"					Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"				Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="EncapsulatedDocumentSeries"		Usage="M"
		Module="ClinicalTrialSeries"			Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"				Usage="M"
		Module="SCEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="EncapsulatedDocument"
		Module="EncapsulatedDocument"			Usage="M"
		Module="EncapsulatedDocumentCDAPseudo"	Usage="M"
		Module="SOPCommon"						Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EncapsulatedSTL"					Condition="EncapsulatedSTLInstance"
	InformationEntity="File"
		Module="FileMetaInformation"			Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"						Usage="M"
		Module="ClinicalTrialSubject"			Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"					Usage="M"
		Module="PatientStudy"					Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"				Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="EncapsulatedDocumentSeries"		Usage="M"
		Module="EncapsulatedDocumentSTLSeriesPseudo"	Usage="M"
		Module="ClinicalTrialSeries"			Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"				Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"				Usage="M"
		Module="EnhancedGeneralEquipment"		Usage="M"
	InformationEntityEnd
	InformationEntity="EncapsulatedDocument"
		Module="EncapsulatedDocument"			Usage="M"
		Module="EncapsulatedDocumentSTLPseudo"	Usage="M"
		Module="Manufacturing3DModel"			Usage="M"
		Module="SOPCommon"						Usage="M"
		Module="CommonInstanceReference"		Usage="C"	Condition="NeedModuleCommonInstanceReference"	# really should check if contained references are present :(
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RealWorldValueMapping"				Condition="RealWorldValueMappingInstance"
	InformationEntity="File"
		Module="FileMetaInformation"			Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"						Usage="M"
		Module="ClinicalTrialSubject"			Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"					Usage="M"
		Module="PatientStudy"					Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"				Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"					Usage="M"
		Module="ClinicalTrialSeries"			Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="RealWorldValueMappingSeries"	Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="RealWorldValueMapping"
		Module="RealWorldValueMapping"			Usage="M"
		Module="CommonInstanceReference"		Usage="M"
		Module="SOPCommon"						Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="IVOCTImage"			Condition="IVOCTImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"									Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"												Usage="M"
		Module="ClinicalTrialSubject"									Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"											Usage="M"
		Module="PatientStudy"											Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"										Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"											Usage="M"
		Module="ClinicalTrialSeries"									Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="IntravascularOCTSeries"									Usage="M"	
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"										Usage="M"
		Module="Synchronization"										Usage="M"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"										Usage="M"
		Module="EnhancedGeneralEquipment"								Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"												Usage="M"
		Module="SupplementalPaletteColorLUT"							Usage="C"	Condition="NeedModuleSupplementalPaletteColorLUT"
		Module="EnhancedContrastBolus"									Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"						Usage="M"
		Module="MultiFrameFunctionalGroupsForIVOCTImageForPresentation"	Usage="C"	Condition="PresentationIntentTypeIsForPresentation"
		Module="MultiFrameFunctionalGroupsForIVOCTImageForProcessing"	Usage="C"	Condition="PresentationIntentTypeIsForProcessing"
		Module="MultiFrameDimension"									Usage="M"
		Module="AcquisitionContext"										Usage="M"
		Module="CardiacSynchronization"									Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="IntravascularOCTImage"									Usage="M"
		Module="IntravascularOCTAcquisitionParameters"					Usage="M"
		Module="IntravascularOCTProcessingParameters"					Usage="C"	Condition="PresentationIntentTypeIsForProcessing"
		Module="IntravascularImageAcquisitionParameters"				Usage="M"
		Module="Device"													Usage="U"	Condition="NeedModuleDevice"
		Module="SOPCommon"												Usage="M"
		Module="CommonInstanceReference"								Usage="M"
		Module="FrameExtraction"										Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="ParametricMap" Condition="ParametricMapInstance"
	InformationEntity="File"
		Module="FileMetaInformation"									Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"												Usage="M"
		Module="ClinicalTrialSubject"									Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"											Usage="M"
		Module="PatientStudy"											Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"										Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"											Usage="M"
		Module="ParametricMapSeries"									Usage="M"
		Module="ClinicalTrialSeries"									Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"										Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"										Usage="M"
		Module="EnhancedGeneralEquipment"								Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"											Usage="M"
		Module="GeneralReference"										Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"												Usage="C"	Condition="PixelDataPresent"
		Module="FloatingPointImagePixel"								Usage="C"	Condition="FloatPixelDataPresent"
		Module="DoubleFloatingPointImagePixel"							Usage="C"	Condition="DoubleFloatPixelDataPresent"
		Module="ParametricMapImage"										Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"						Usage="M"
		Module="MultiFrameFunctionalGroupsForParametricMap"				Usage="M"
		Module="MultiFrameDimension"									Usage="M"
		Module="PaletteColorLookupTable"								Usage="C"	Condition="PixelPresentationIsColorRangeAndPaletteColorLookupTableUIDAbsent"
		Module="CardiacSynchronization"									Usage="U"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"								Usage="U"	Condition="NeedModuleRespiratorySynchronization"
		Module="BulkMotionSynchronization"								Usage="U"	Condition="NeedModuleBulkMotion"
		Module="AcquisitionContext"										Usage="M"
		Module="Device"													Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"												Usage="U"	Condition="NeedModuleSpecimen"
		Module="CommonInstanceReference"								Usage="C"	Condition="NeedModuleCommonInstanceReference"	# really should check if contained references are present :(
		Module="SOPCommon"												Usage="M"
		Module="FrameExtraction"										Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd
CompositeIOD="BasicDirectory"					Condition="MediaStorageDirectoryInstance"
	InformationEntity="File"
		Module="FileMetaInformation"			Usage="M"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Directory"
		Module="FileSetIdentification"			Usage="M"
		Module="DirectoryInformation"			Usage="U"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="BasicDirectoryDental"				Condition="MediaStorageDirectoryInstance"	Profile="Dental"
	InformationEntity="File"
		Module="FileMetaInformation"			Usage="M"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Directory"
		Module="FileSetIdentification"			Usage="M"
		Module="DirectoryInformation"			Usage="U"
		Module="DirectoryInformationDental"		Usage="U"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="XAImage"		Condition="XAImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="C"	Condition="NeedModuleContrastBolus"
		Module="Cine"						Usage="C"	Condition="NeedModuleCine"
		Module="MultiFrame"					Usage="C" 	Condition="NeedModuleMultiFrame"
		Module="FramePointers"				Usage="U"	Condition="NeedModuleFramePointers"
		Module="Mask"						Usage="C" 	Condition="NeedModuleMask"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="XRayImage"					Usage="M"
		Module="XRayAcquisition"			Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="XRayTable"					Usage="C"	Condition="NeedModuleXRayTable"
		Module="XAPositioner"				Usage="M"
		Module="DXDetector"					Usage="U"	Condition="NeedModuleDXDetector"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="MultiFrameOverlay"			Usage="C" 	Condition="NeedModuleMultiFrameOverlay"
		Module="ModalityLUT"				Usage="C"	Condition="XRayNeedModuleModalityLUT"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"			Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="XRFImage"		Condition="XRFImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="C"	Condition="NeedModuleContrastBolus"
		Module="Cine"						Usage="C"	Condition="NeedModuleCine"
		Module="MultiFrame"					Usage="C" 	Condition="NeedModuleMultiFrame"
		Module="FramePointers"				Usage="U"	Condition="NeedModuleFramePointers"
		Module="Mask"						Usage="C" 	Condition="NeedModuleMask"
		Module="XRayImage"					Usage="M"
		Module="XRayAcquisition"			Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="XRayTable"					Usage="C"	Condition="NeedModuleXRayTable"
		Module="XRFPositioner"				Usage="U"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedModuleXRayTomographyAcquisitionBasedOnScanOptions"
		Module="DXDetector"					Usage="U"	Condition="NeedModuleDXDetector"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="MultiFrameOverlay"			Usage="C" 	Condition="NeedModuleMultiFrameOverlay"
		Module="ModalityLUT"				Usage="C"	Condition="XRayNeedModuleModalityLUT"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"			Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EnhancedXAImage"		Condition="EnhancedXAImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="XAXRFSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="C"	Condition="CArmPositionerTabletopRelationshipIsYes"
		Module="Synchronization"			Usage="C"	Condition="CArmPositionerTabletopRelationshipIsYes"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
		Module="EnhancedGeneralEquipment"	Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"							Usage="M"
		Module="EnhancedContrastBolus"				Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="Mask"								Usage="U" 	Condition="NeedModuleMask"
		Module="Device"								Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"						Usage="U"	Condition="NeedModuleIntervention"
		Module="AcquisitionContext"					Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForEnhancedXAImage"	Usage="M"
		Module="MultiFrameDimension"				Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="CardiacSynchronization"				Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"			Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="Specimen"							Usage="U"	Condition="NeedModuleSpecimen"
		Module="XRayFiltration"						Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"							Usage="U"	Condition="NeedModuleXRayGrid"
		Module="EnhancedXAXRFImage"					Usage="M"
		Module="XAXRFAcquisition"					Usage="C"	Condition="ImageTypeValue1Original"
		Module="XRayImageIntensifier"				Usage="C"	Condition="XRayReceptorTypeIsImageIntensifier"
		Module="XRayDetector"						Usage="C"	Condition="XRayReceptorTypeIsDigitalDetector"
		Module="XAXRFMultiFramePresentation"		Usage="U"	Condition="NeedModuleXAXRFMultiFramePresentation"
		Module="SOPCommon"							Usage="M"
		Module="CommonInstanceReference"			Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"					Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EnhancedXRFImage"		Condition="EnhancedXRFImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="XAXRFSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
		Module="Synchronization"			Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
		Module="EnhancedGeneralEquipment"	Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"							Usage="M"
		Module="EnhancedContrastBolus"				Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="Mask"								Usage="U" 	Condition="NeedModuleMask"
		Module="Device"								Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"						Usage="U"	Condition="NeedModuleIntervention"
		Module="AcquisitionContext"					Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForEnhancedXRFImage"	Usage="M"
		Module="MultiFrameDimension"				Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="CardiacSynchronization"				Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"			Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="Specimen"							Usage="U"	Condition="NeedModuleSpecimen"
		Module="XRayTomographyAcquisition"			Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayFiltration"						Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"							Usage="U"	Condition="NeedModuleXRayGrid"
		Module="EnhancedXAXRFImage"					Usage="M"
		Module="XAXRFAcquisition"					Usage="C"	Condition="ImageTypeValue1Original"
		Module="XRayImageIntensifier"				Usage="C"	Condition="XRayReceptorTypeIsImageIntensifier"
		Module="XRayDetector"						Usage="C"	Condition="XRayReceptorTypeIsDigitalDetector"
		Module="XAXRFMultiFramePresentation"		Usage="U"	Condition="NeedModuleXAXRFMultiFramePresentation"
		Module="SOPCommon"							Usage="M"
		Module="CommonInstanceReference"			Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"					Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="XRay3DAngiographicImage"		Condition="XRay3DAngiographicImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="EnhancedSeries"				Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
		Module="EnhancedGeneralEquipment"	Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"												Usage="M"
		Module="EnhancedContrastBolus"									Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="Device"													Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"											Usage="U"	Condition="NeedModuleIntervention"
		Module="AcquisitionContext"										Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"						Usage="M"
		Module="MultiFrameFunctionalGroupsForXRay3DAngiographicImage"	Usage="M"
		Module="MultiFrameDimension"									Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="CardiacSynchronization"									Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"								Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="PatientOrientation"										Usage="U"	Condition="NeedModulePatientOrientation"
		Module="ImageEquipmentCoordinateRelationship"					Usage="U"	Condition="NeedModuleImageEquipmentCoordinateRelationship"
		Module="Specimen"												Usage="U"	Condition="NeedModuleSpecimen"
		Module="XRay3DImage"											Usage="M"
		Module="XRay3DAngiographicImageContributingSources"				Usage="U"	Condition="NeedModuleXRay3DAngiographicImageContributingSources"
		Module="XRay3DAngiographicAcquisition"							Usage="U"	Condition="NeedModuleXRay3DAngiographicAcquisition"
		Module="XRay3DReconstruction"									Usage="U"	Condition="NeedModuleXRay3DReconstruction"
		Module="SOPCommon"												Usage="M"
		Module="CommonInstanceReference"								Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"										Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="XRay3DCraniofacialImage"		Condition="XRay3DCraniofacialImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="EnhancedSeries"				Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
		Module="EnhancedGeneralEquipment"	Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"												Usage="M"
		Module="EnhancedContrastBolus"									Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="Device"													Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"											Usage="U"	Condition="NeedModuleIntervention"
		Module="AcquisitionContext"										Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"						Usage="M"
		Module="MultiFrameFunctionalGroupsForXRay3DCraniofacialImage"	Usage="M"
		Module="MultiFrameDimension"									Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="PatientOrientation"										Usage="U"	Condition="NeedModulePatientOrientation"
		Module="ImageEquipmentCoordinateRelationship"					Usage="U"	Condition="NeedModuleImageEquipmentCoordinateRelationship"
		Module="Specimen"												Usage="U"	Condition="NeedModuleSpecimen"
		Module="XRay3DImage"											Usage="M"
		Module="XRay3DCraniofacialImageContributingSources"				Usage="U"	Condition="NeedModuleXRay3DCraniofacialImageContributingSources"
		Module="XRay3DCraniofacialAcquisition"							Usage="U"	Condition="NeedModuleXRay3DCraniofacialAcquisition"
		Module="XRay3DReconstruction"									Usage="U"	Condition="NeedModuleXRay3DReconstruction"
		Module="SOPCommon"												Usage="M"
		Module="CommonInstanceReference"								Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"										Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="PETImage"		Condition="PETImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="PETSeries"					Usage="M"
		Module="PETIsotope"					Usage="M"
		Module="PETMultigatedAcquisition"	Usage="C"	Condition="NeedModulePETMultigatedAcquisition"
		Module="NMPETPatientOrientation"	Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePlane"					Usage="M"
		Module="ImagePixel"					Usage="M"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="PETImage"					Usage="M"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="AcquisitionContext"			Usage="U"	Condition="NeedModuleAcquisitionContext"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EnhancedPETImage"			Condition="EnhancedPETImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="EnhancedPETSeries"								Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="Intervention"									Usage="U"	Condition="NeedModuleIntervention"
		Module="AcquisitionContext"								Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForEnhancedPETImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="M"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedPETIsotope"								Usage="M"
		Module="EnhancedPETAcquisition"							Usage="M"
		Module="EnhancedPETImage"								Usage="M"
		Module="EnhancedPETCorrections"							Usage="M"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="LegacyConvertedEnhancedPETImage"	Condition="LegacyConvertedEnhancedPETImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="EnhancedPETSeries"								Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="U"	Condition="EnhancedGeneralEquipmentIsPresent"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="Intervention"									Usage="U"	Condition="NeedModuleIntervention"
		Module="AcquisitionContext"								Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForLegacyConvertedEnhancedPETImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="C"	Condition="NeedModuleMultiFrameDimension"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedPETImage"								Usage="M"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="PrivatePixelMedLegacyConvertedEnhancedPETImage"	Condition="PrivatePixelMedLegacyConvertedEnhancedPETImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="EnhancedPETSeries"								Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="U"	Condition="EnhancedGeneralEquipmentIsPresent"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="ContrastBolus"									Usage="C"	Condition="NeedModuleContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForPrivatePixelMedLegacyConvertedEnhancedPETImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="C"	Condition="NeedModuleMultiFrameDimension"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="AcquisitionContext"								Usage="M"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedPETImage"								Usage="M"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd
CompositeIOD="RTImage"		Condition="RTImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="RTSeries"					Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="C"	Condition="NeedModuleContrastBolus"
		Module="Cine"						Usage="C"	Condition="NeedModuleCine"
		Module="MultiFrame"					Usage="C"	Condition="NeedModuleMultiFrame"
		Module="RTImage"					Usage="M"
		Module="ModalityLUT"				Usage="U"	Condition="NeedModuleModalityLUT"
		Module="VOILUT"						Usage="U"	Condition="NeedModuleVOILUT"
		Module="Approval"					Usage="U"	Condition="NeedModuleApproval"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"			Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RTDose"		Condition="RTDoseInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="RTSeries"					Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="C"	Condition="DoseDataGridbased"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePlane"					Usage="C"	Condition="DoseDataGridbased"
		Module="ImagePixel"					Usage="C"	Condition="DoseDataGridbased"
		Module="MultiFrame"					Usage="C"	Condition="DoseDataGridbasedAndNeedModuleMultiFrame"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="MultiFrameOverlay"			Usage="U"	Condition="NeedModuleMultiFrameOverlay"
		Module="ModalityLUT"				Usage="U"	Condition="NeedModuleModalityLUT"
		Module="RTDose"						Usage="M"
		Module="RTDVH"						Usage="U"	Condition="NeedModuleRTDVH"
		Module="StructureSet"				Usage="C"	Condition="DoseDataPointsOrCurves"
		Module="ROIContour"					Usage="C"	Condition="DoseDataPointsOrCurves"
		Module="RTDoseROI"					Usage="C"	Condition="DoseDataPointsOrCurves"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"			Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RTStructureSet"		Condition="RTStructureSetInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="RTSeries"					Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="StructureSet"
		Module="StructureSet"				Usage="M"
		Module="ROIContour"					Usage="M"
		Module="RTROIObservations"			Usage="M"
		Module="Approval"					Usage="U"	Condition="NeedModuleApproval"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RTPlan"			Condition="RTPlanInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="RTSeries"					Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Plan"
		Module="RTGeneralPlan"				Usage="M"
		Module="RTPrescription"				Usage="U"	Condition="NeedModuleRTPrescription"
		Module="RTToleranceTables"			Usage="U"	Condition="NeedModuleRTToleranceTables"
		Module="RTPatientSetup"				Usage="U"	Condition="NeedModuleRTPatientSetup"
		Module="RTFractionScheme"			Usage="U"	Condition="NeedModuleRTFractionScheme"
		Module="RTBeams"					Usage="C"	Condition="NeedRTBeams"
		Module="RTBrachyApplicationSetups"	Usage="C"	Condition="NeedRTBrachyApplicationSetups"
		Module="Approval"					Usage="U"	Condition="NeedModuleApproval"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RTBeamsTreatmentRecord"			Condition="RTBeamsTreatmentRecordInstance"
	InformationEntity="File"
		Module="FileMetaInformation"			Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"						Usage="M"
		Module="ClinicalTrialSubject"			Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"					Usage="M"
		Module="PatientStudy"					Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"				Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="RTSeries"						Usage="M"
		Module="ClinicalTrialSeries"			Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="TreatmentRecord"
		Module="RTGeneralTreatmentRecord"		Usage="M"
		Module="RTPatientSetup"					Usage="U"	Condition="NeedModuleRTPatientSetup"
		Module="RTTreatmentMachineRecord"		Usage="M"
		Module="MeasuredDoseReferenceRecord"	Usage="U"	Condition="NeedModuleMeasuredDoseReferenceRecord"
		Module="CalculatedDoseReferenceRecord"	Usage="U"	Condition="NeedModuleCalculatedDoseReferenceRecord"
		Module="RTBeamsSessionRecord"			Usage="M"
		Module="RTTreatmentSummaryRecord"		Usage="U"	Condition="NeedModuleRTTreatmentSummaryRecord"
		Module="GeneralReference"				Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"						Usage="M"
		Module="CommonInstanceReference"		Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RTBrachyTreatmentRecord"			Condition="RTBrachyTreatmentRecordInstance"
	InformationEntity="File"
		Module="FileMetaInformation"			Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"						Usage="M"
		Module="ClinicalTrialSubject"			Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"					Usage="M"
		Module="PatientStudy"					Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"				Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="RTSeries"						Usage="M"
		Module="ClinicalTrialSeries"			Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="TreatmentRecord"
		Module="RTGeneralTreatmentRecord"		Usage="M"
		Module="RTPatientSetup"					Usage="U"	Condition="NeedModuleRTPatientSetup"
		Module="RTTreatmentMachineRecord"		Usage="M"
		Module="MeasuredDoseReferenceRecord"	Usage="U"	Condition="NeedModuleMeasuredDoseReferenceRecord"
		Module="CalculatedDoseReferenceRecord"	Usage="U"	Condition="NeedModuleCalculatedDoseReferenceRecord"
		Module="RTBrachySessionRecord"			Usage="M"
		Module="RTTreatmentSummaryRecord"		Usage="U"	Condition="NeedModuleRTTreatmentSummaryRecord"
		Module="GeneralReference"				Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"						Usage="M"
		Module="CommonInstanceReference"		Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RTTreatmentSummaryRecord"			Condition="RTTreatmentSummaryRecordInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="RTSeries"					Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="TreatmentRecord"
		Module="RTGeneralTreatmentRecord"	Usage="M"
		Module="RTTreatmentSummaryRecord"	Usage="U"	Condition="NeedModuleRTTreatmentSummaryRecord"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RTIonPlan"			Condition="RTIonPlanInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="RTSeries"					Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Plan"
		Module="RTGeneralPlan"				Usage="M"
		Module="RTPrescription"				Usage="U"	Condition="NeedModuleRTPrescription"
		Module="RTIonToleranceTables"		Usage="U"	Condition="NeedModuleRTIonToleranceTables"
		Module="RTPatientSetup"				Usage="U"	Condition="NeedModuleRTPatientSetup"
		Module="RTFractionScheme"			Usage="U"	Condition="NeedModuleRTFractionScheme"
		Module="RTIonBeams"					Usage="C"	Condition="NeedRTIonBeams"
		Module="Approval"					Usage="U"	Condition="NeedModuleApproval"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RTIonBeamsTreatmentRecord"			Condition="RTIonBeamsTreatmentRecordInstance"
	InformationEntity="File"
		Module="FileMetaInformation"			Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"						Usage="M"
		Module="ClinicalTrialSubject"			Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"					Usage="M"
		Module="PatientStudy"					Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"				Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="RTSeries"						Usage="M"
		Module="ClinicalTrialSeries"			Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="TreatmentRecord"
		Module="RTGeneralTreatmentRecord"		Usage="M"
		Module="RTPatientSetup"					Usage="U"	Condition="NeedModuleRTPatientSetup"
		Module="RTTreatmentMachineRecord"		Usage="M"
		Module="MeasuredDoseReferenceRecord"	Usage="U"	Condition="NeedModuleMeasuredDoseReferenceRecord"
		Module="CalculatedDoseReferenceRecord"	Usage="U"	Condition="NeedModuleCalculatedDoseReferenceRecord"
		Module="RTIonBeamsSessionRecord"		Usage="M"
		Module="RTTreatmentSummaryRecord"		Usage="U"	Condition="NeedModuleRTTreatmentSummaryRecord"
		Module="GeneralReference"				Usage="U"	Condition="NeedModuleGeneralReference"
		Module="SOPCommon"						Usage="M"
		Module="CommonInstanceReference"		Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="DXImageForProcessing"			Condition="DXImageForProcessingInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="DXImageForPresentation"			Condition="DXImageForPresentationInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MammographyImageForProcessing"			Condition="MammographyImageForProcessingInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
		Module="MammographySeries"			Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="MammographyImage"			Usage="M"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MammographyImageForPresentation"			Condition="MammographyImageForPresentationInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
		Module="MammographySeries"			Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="MammographyImage"			Usage="M"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MammographyImageForProcessingIHEMammo"			Condition="MammographyImageForProcessingInstance"	Profile="IHEMammo"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
		Module="MammographySeries"			Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="MammographyImage"			Usage="M"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="IHEMammoProfile"			Usage="M"
		Module="IHEMammoProfileWithoutPartialViewOption"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MammographyImageForProcessingIHEMammoPartialViewOption"			Condition="MammographyImageForProcessingInstance"	Profile="IHEMammoPartialViewOption"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
		Module="MammographySeries"			Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="MammographyImage"			Usage="M"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="IHEMammoProfile"			Usage="M"
		Module="IHEMammoProfileWithPartialViewOption"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MammographyImageForPresentationIHEMammo"			Condition="MammographyImageForPresentationInstance"	Profile="IHEMammo"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
		Module="MammographySeries"			Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="MammographyImage"			Usage="M"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="IHEMammoProfile"			Usage="M"
		Module="IHEMammoProfileWithoutPartialViewOption"		Usage="M"
		Module="IHEMammoProfileForPresentationOnly"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MammographyImageForPresentationIHEMammoPartialViewOption"			Condition="MammographyImageForPresentationInstance"	Profile="IHEMammoPartialViewOption"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
		Module="MammographySeries"			Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="MammographyImage"			Usage="M"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="IHEMammoProfile"			Usage="M"
		Module="IHEMammoProfileWithPartialViewOption"		Usage="M"
		Module="IHEMammoProfileForPresentationOnly"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="IntraoralImageForProcessing"			Condition="IntraoralImageForProcessingInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
		Module="IntraoralSeries"			Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="IntraoralImage"				Usage="M"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="IntraoralImageForPresentation"			Condition="IntraoralImageForPresentationInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
		Module="IntraoralSeries"			Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="IntraoralImage"				Usage="M"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="IntraoralImageForPresentationDentalMedia"			Condition="IntraoralImageForPresentationInstance"	Profile="Dental"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
		Module="IntraoralSeries"			Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="IntraoralImage"				Usage="M"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="DentalImageOnMediaProfile"	Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="DXImageForPresentationDentalMedia"			Condition="DXImageForPresentationInstance"	Profile="Dental"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="ContrastBolus"				Usage="U"	Condition="NeedModuleContrastBolus"
		Module="DisplayShutter"				Usage="U"	Condition="NeedModuleDisplayShutter"
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"				Usage="U"	Condition="NeedModuleIntervention"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="DXAnatomyImaged"			Usage="M"
		Module="DXImage"					Usage="M"
		Module="DXDetector"					Usage="M"
		Module="XRayCollimator"				Usage="U"	Condition="NeedModuleXRayCollimator"
		Module="DXPositioning"				Usage="U"	Condition="NeedModuleDXPositioning"
		Module="XRayTomographyAcquisition"	Usage="U"	Condition="NeedToCheckModuleXRayTomographyAcquisition"
		Module="XRayAcquisitionDose"		Usage="U"	Condition="NeedModuleXRayAcquisitionDose"
		Module="XRayGeneration"				Usage="U"	Condition="NeedModuleXRayGeneration"
		Module="XRayFiltration"				Usage="U"	Condition="NeedModuleXRayFiltration"
		Module="XRayGrid"					Usage="U"	Condition="NeedModuleXRayGrid"
		Module="OverlayPlane"				Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="VOILUT"						Usage="C"	Condition="DXNeedModuleVOILUT"
		Module="ImageHistogram"				Usage="U"	Condition="NeedModuleImageHistogram"
		Module="AcquisitionContext"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="DentalImageOnMediaProfile"	Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="BreastTomosynthesisImage"					Condition="BreastTomosynthesisInstance"
	InformationEntity="File"
		Module="FileMetaInformation"					Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"								Usage="M"
		Module="ClinicalTrialSubject"					Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"							Usage="M"
		Module="PatientStudy"							Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"						Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"							Usage="M"
		Module="ClinicalTrialSeries"					Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="EnhancedMammographySeries"				Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"						Usage="U"	Condition="NeedModuleFrameOfReference"
		Module="Synchronization"						Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"						Usage="M"
		Module="EnhancedGeneralEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"												Usage="M"
		Module="EnhancedContrastBolus"									Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="Device"													Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"											Usage="U"	Condition="NeedModuleIntervention"
		Module="AcquisitionContext"										Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"						Usage="M"
		Module="MultiFrameFunctionalGroupsForBreastTomosynthesisImage"	Usage="M"
		Module="MultiFrameDimension"									Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="ImageEquipmentCoordinateRelationship"					Usage="U"	Condition="NeedModuleImageEquipmentCoordinateRelationship"
		Module="Specimen"												Usage="U"	Condition="NeedModuleSpecimen"
		Module="XRay3DImage"											Usage="M"
		Module="BreastTomosynthesisContributingSources"					Usage="U"	Condition="NeedModuleBreastTomosynthesisContributingSources"
		Module="BreastTomosynthesisAcquisition"							Usage="U"	Condition="NeedModuleBreastTomosynthesisAcquisition"
		Module="XRay3DReconstruction"									Usage="U"	Condition="NeedModuleXRay3DReconstruction"
		Module="BreastView"												Usage="M"
		Module="SOPCommon"												Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"										Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="BreastTomosynthesisImageIHEDBT"				Condition="BreastTomosynthesisInstance"	Profile="IHEDBT"
	InformationEntity="File"
		Module="FileMetaInformation"					Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"								Usage="M"
		Module="ClinicalTrialSubject"					Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"							Usage="M"
		Module="PatientStudy"							Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"						Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"							Usage="M"
		Module="ClinicalTrialSeries"					Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="EnhancedMammographySeries"				Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"						Usage="U"	Condition="NeedModuleFrameOfReference"
		Module="Synchronization"						Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"						Usage="M"
		Module="EnhancedGeneralEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"												Usage="M"
		Module="EnhancedContrastBolus"									Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="Device"													Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"											Usage="U"	Condition="NeedModuleIntervention"
		Module="AcquisitionContext"										Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"						Usage="M"
		Module="MultiFrameFunctionalGroupsForBreastTomosynthesisImage"	Usage="M"
		Module="MultiFrameDimension"									Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="ImageEquipmentCoordinateRelationship"					Usage="U"	Condition="NeedModuleImageEquipmentCoordinateRelationship"
		Module="Specimen"												Usage="U"	Condition="NeedModuleSpecimen"
		Module="XRay3DImage"											Usage="M"
		Module="BreastTomosynthesisContributingSources"					Usage="U"	Condition="NeedModuleBreastTomosynthesisContributingSources"
		Module="BreastTomosynthesisAcquisition"							Usage="U"	Condition="NeedModuleBreastTomosynthesisAcquisition"
		Module="XRay3DReconstruction"									Usage="U"	Condition="NeedModuleXRay3DReconstruction"
		Module="BreastView"												Usage="M"
		Module="SOPCommon"												Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"										Usage="C"	Condition="NeedModuleFrameExtraction"
		Module="IHEDBTProfile"			Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="BreastProjectionXRayImage"	Condition="BreastProjectionXRayImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"					Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"								Usage="M"
		Module="ClinicalTrialSubject"					Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"							Usage="M"
		Module="PatientStudy"							Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"						Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"							Usage="M"
		Module="ClinicalTrialSeries"					Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="DXSeries"								Usage="M"
		Module="EnhancedMammographySeries"				Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"						Usage="M"
		Module="Synchronization"						Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"						Usage="M"
		Module="EnhancedGeneralEquipment"				Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="EnhancedMammographyImage"				Usage="M"
		Module="BreastView"								Usage="M"
		Module="ImagePixel"								Usage="M"
		Module="EnhancedContrastBolus"					Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="Device"									Usage="U"	Condition="NeedModuleDevice"
		Module="Intervention"							Usage="U"	Condition="NeedModuleIntervention"
		Module="AcquisitionContext"						Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"		Usage="M"
		Module="MultiFrameFunctionalGroupsForBreastProjectionXRayImage"	Usage="M"
		Module="MultiFrameDimension"					Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="PatientOrientation"						Usage="M"
		Module="Specimen"								Usage="U"	Condition="NeedModuleSpecimen"
		Module="SOPCommon"								Usage="M"
		Module="CommonInstanceReference"				Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"						Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd
CompositeIOD="VLEndoscopicImage"		Condition="VisibleLightEndoscopicImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="VLEndoscopicSeriesPseudo"	Usage="M"	# not in standard ... use to check conditions
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="AcquisitionContext"			Usage="M"	# not check for baseline CIDs yet
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="VLImage"					Usage="M"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="VLMicroscopicImage"		Condition="VisibleLightMicroscopicImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="VLMicroscopicSeriesPseudo"	Usage="M"	# not in standard ... use to check conditions
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="AcquisitionContext"			Usage="M"	# not check for baseline CIDs yet
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="C"	Condition="NeedModuleSpecimen"	# real-world "is a specimen"
		Module="VLImage"					Usage="M"
		Module="OpticalPath"				Usage="U"	Condition="NeedModuleOpticalPath"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="VLSlideCoordinatesMicroscopicImage"		Condition="VisibleLightSlideCoordinatesMicroscopicImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="VLSlideCoordinatesMicroscopicSeriesPseudo"	Usage="M"	# not in standard ... use to check conditions
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="AcquisitionContext"			Usage="M"	# not check for baseline CIDs yet
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="M"
		Module="VLImage"					Usage="M"
		Module="SlideCoordinates"			Usage="M"
		Module="OpticalPath"				Usage="U"	Condition="NeedModuleOpticalPath"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="VLPhotographicImage"		Condition="VisibleLightPhotographicImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="VLPhotographicSeriesPseudo"	Usage="M"	# not in standard ... use to check conditions
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"					Usage="M"
		Module="AcquisitionContext"			Usage="M"	# not check for baseline CIDs yet
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="C"	Condition="NeedModuleSpecimen"	# real-world "is a specimen"
		Module="VLImage"					Usage="M"
		Module="OverlayPlane"				Usage="U"	Condition="NeedModuleOverlayPlane"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="CheckSingleFramePseudo"		Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="VideoEndoscopicImage"			Condition="VideoEndoscopicImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="VLEndoscopicSeriesPseudo"	Usage="M"	# not in standard ... use to check conditions
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="Cine"						Usage="M"
		Module="MultiFrame"					Usage="M"
		Module="ImagePixel"					Usage="M"
		Module="AcquisitionContext"			Usage="M"	# no check for baseline CIDs yet
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="C"	Condition="NeedModuleSpecimen"	# real-world "is a specimen"
		Module="VLImage"					Usage="M"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"			Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="VideoMicroscopicImage"		Condition="VideoMicroscopicImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="VLMicroscopicSeriesPseudo"	Usage="M"	# not in standard ... use to check conditions
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="Cine"						Usage="M"
		Module="MultiFrame"					Usage="M"
		Module="ImagePixel"					Usage="M"
		Module="AcquisitionContext"			Usage="M"	# not check for baseline CIDs yet
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="C"	Condition="NeedModuleSpecimen"	# real-world "is a specimen"
		Module="VLImage"					Usage="M"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"			Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="VideoPhotographicImage"		Condition="VideoPhotographicImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="VLPhotographicSeriesPseudo"	Usage="M"	# not in standard ... use to check conditions
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"				Usage="M"
		Module="GeneralReference"			Usage="U"	Condition="NeedModuleGeneralReference"
		Module="Cine"						Usage="M"
		Module="MultiFrame"					Usage="M"
		Module="ImagePixel"					Usage="M"
		Module="AcquisitionContext"			Usage="M"	# not check for baseline CIDs yet
		Module="Device"						Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"					Usage="C"	Condition="NeedModuleSpecimen"	# real-world "is a specimen"
		Module="VLImage"					Usage="M"
		Module="ICCProfile"					Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"					Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"			Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="OphthalmicPhotography8BitImage"		Condition="OphthalmicPhotography8BitImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="OphthalmicPhotographySeries"				Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"							Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"								Usage="M"
		Module="GeneralReference"							Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"									Usage="M"
		Module="EnhancedContrastBolus"						Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="Cine"										Usage="C"	Condition="NeedModuleCine"
		Module="MultiFrame"									Usage="M"
		Module="AcquisitionContext"							Usage="U"	Condition="NeedModuleAcquisitionContext"
		Module="OphthalmicPhotographyImage"					Usage="M"
		Module="OphthalmicPhotography8BitImagePseudo"		Usage="M"	# not in standard ... use to check bit depths
		Module="OcularRegionImaged"							Usage="M"
		Module="OphthalmicPhotographyAcquisitionParameters"	Usage="M"
		Module="OphthalmicPhotographicParameters"			Usage="M"
		Module="ICCProfile"									Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"									Usage="M"
		Module="CommonInstanceReference"					Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"							Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="OphthalmicPhotography16BitImage"		Condition="OphthalmicPhotography16BitImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="OphthalmicPhotographySeries"					Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"							Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"								Usage="M"
		Module="GeneralReference"							Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"									Usage="M"
		Module="EnhancedContrastBolus"						Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="Cine"										Usage="C"	Condition="NeedModuleCine"
		Module="MultiFrame"									Usage="M"
		Module="AcquisitionContext"							Usage="U"	Condition="NeedModuleAcquisitionContext"
		Module="OphthalmicPhotographyImage"					Usage="M"
		Module="OphthalmicPhotography16BitImagePseudo"		Usage="M"	# not in standard ... use to check bit depths
		Module="OcularRegionImaged"							Usage="M"
		Module="OphthalmicPhotographyAcquisitionParameters"	Usage="M"
		Module="OphthalmicPhotographicParameters"			Usage="M"
		Module="ICCProfile"									Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"									Usage="M"
		Module="CommonInstanceReference"					Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"							Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd


CompositeIOD="StereometricRelationship"			Condition="StereometricRelationshipInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="StereometricSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="StereometricRelationship"	Usage="M"
		Module="CommonInstanceReference"	Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="OphthalmicTomographyImage"		Condition="OphthalmicTomographyImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="OphthalmicTomographySeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"							Usage="C"	Condition="NeedModuleFrameOfReference"			# condition is real-world (Ophthalmic Photography Reference Image available) ... just check if present
		Module="Synchronization"							Usage="C"	Condition="NeedToCheckModuleSynchronization"	# condition is real-world (Ophthalmic Photography Reference Image available) ... just check if present
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"									Usage="M"
		Module="EnhancedContrastBolus"						Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"			Usage="M"
		Module="MultiFrameFunctionalGroupsForOphthalmicTomography"	Usage="M"
		Module="MultiFrameDimension"						Usage="M"
		Module="AcquisitionContext"							Usage="M"
		Module="CardiacSynchronization"						Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="OphthalmicTomographyImage"					Usage="M"
		Module="OphthalmicTomographyAcquisitionParameters"	Usage="M"
		Module="OphthalmicTomographyParameters"				Usage="M"
		Module="OcularRegionImaged"							Usage="M"
		Module="SOPCommon"									Usage="M"
		Module="CommonInstanceReference"					Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"							Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="VLWholeSlideMicroscopyImage"		Condition="VLWholeSlideMicroscopyImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="WholeSlideMicroscopySeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"							Usage="C"	Condition="NeedModuleFrameOfReference"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"								Usage="M"
		Module="GeneralReference"							Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"									Usage="M"
		Module="AcquisitionContext"							Usage="M"
		Module="MultiFrameFunctionalGroupsCommon"			Usage="M"
		Module="MultiFrameFunctionalGroupsForWholeSlideMicroscopy"	Usage="M"
		Module="MultiFrameDimension"						Usage="M"
		Module="Specimen"									Usage="M"
		Module="WholeSlideMicroscopyImage"					Usage="M"
		Module="OpticalPath"								Usage="M"
		Module="MultiResolutionNavigation"					Usage="C"	Condition="ImageTypeValue3Localizer"
		Module="SlideLabel"									Usage="C"	Condition="NeedModuleSlideLabel"
		Module="SOPCommon"									Usage="M"
		Module="CommonInstanceReference"					Usage="M"
		Module="FrameExtraction"							Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="LensometryMeasurements" Condition="LensometryMeasurementsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="LensometryMeasurementsSeries"				Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Measurements"
		Module="GeneralOphthalmicRefractiveMeasurements"	Usage="M"
		Module="LensometryMeasurements"						Usage="M"
		Module="SOPCommon"									Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="AutorefractionMeasurements" Condition="AutorefractionMeasurementsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="AutorefractionMeasurementsSeries"			Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Measurements"
		Module="GeneralOphthalmicRefractiveMeasurements"	Usage="M"
		Module="AutorefractionMeasurements"					Usage="M"
		Module="SOPCommon"									Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="KeratometryMeasurements" Condition="KeratometryMeasurementsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="KeratometryMeasurementsSeries"				Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Measurements"
		Module="GeneralOphthalmicRefractiveMeasurements"	Usage="M"
		Module="KeratometryMeasurements"					Usage="M"
		Module="SOPCommon"									Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="SubjectiveRefractionMeasurements" Condition="SubjectiveRefractionMeasurementsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="SubjectiveRefractionMeasurementsSeries"		Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Measurements"
		Module="GeneralOphthalmicRefractiveMeasurements"	Usage="M"
		Module="SubjectiveRefractionMeasurements"			Usage="M"
		Module="SOPCommon"									Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="VisualAcuityMeasurements" Condition="VisualAcuityMeasurementsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="VisualAcuityMeasurementsSeries"				Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Measurements"
		Module="GeneralOphthalmicRefractiveMeasurements"	Usage="M"
		Module="VisualAcuityMeasurements"					Usage="M"
		Module="SOPCommon"									Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="OphthalmicAxialMeasurements" Condition="OphthalmicAxialMeasurementsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="OphthalmicAxialMeasurementsSeries"			Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Measurements"
		Module="OphthalmicAxialMeasurements"				Usage="M"
		Module="GeneralOphthalmicRefractiveMeasurements"	Usage="M"
		Module="SOPCommon"									Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="IntraocularLensCalculations" Condition="IntraocularLensCalculationsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"								Usage="M"
		Module="IntraocularLensCalculationsSeries"			Usage="M"
		Module="ClinicalTrialSeries"						Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Measurements"
		Module="IntraocularLensCalculations"				Usage="M"
		Module="GeneralOphthalmicRefractiveMeasurements"	Usage="M"
		Module="SOPCommon"									Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="OphthalmicVisualFieldStaticPerimetryMeasurements" Condition="OphthalmicVisualFieldStaticPerimetryMeasurementsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"						Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"									Usage="M"
		Module="ClinicalTrialSubject"						Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"								Usage="M"
		Module="PatientStudy"								Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"							Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="VisualFieldStaticPerimetryMeasurementsSeries"	Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"							Usage="M"
		Module="EnhancedGeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Measurements"
		Module="VisualFieldStaticPerimetryTestParameters"					Usage="M"
		Module="VisualFieldStaticPerimetryTestReliability"					Usage="M"
		Module="VisualFieldStaticPerimetryTestMeasurements"					Usage="M"
		Module="VisualFieldStaticPerimetryTestResults"						Usage="M"
		Module="OphthalmicPatientClinicalInformationandTestLensParameters"	Usage="U"
		Module="SOPCommon"													Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="BasicVoice"		Condition="BasicVoiceInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Waveform"
		Module="WaveformIdentification"		Usage="M"
		Module="Waveform"					Usage="M"
		Module="AcquisitionContext"			Usage="M"
		Module="WaveformAnnotation"			Usage="U"	Condition="NeedModuleWaveformAnnotation"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="TwelveLeadECG"				Condition="TwelveLeadECGInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Waveform"
		Module="WaveformIdentification"		Usage="M"
		Module="Waveform"					Usage="M"
		Module="AcquisitionContext"			Usage="M"
		Module="WaveformAnnotation"			Usage="C"	Condition="NeedModuleWaveformAnnotation"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="GeneralECG"				Condition="GeneralECGInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Waveform"
		Module="WaveformIdentification"		Usage="M"
		Module="Waveform"					Usage="M"
		Module="AcquisitionContext"			Usage="M"
		Module="WaveformAnnotation"			Usage="C"	Condition="NeedModuleWaveformAnnotation"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="AmbulatoryECG"				Condition="AmbulatoryECGInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Waveform"
		Module="WaveformIdentification"		Usage="M"
		Module="Waveform"					Usage="M"
		Module="AcquisitionContext"			Usage="M"
		Module="WaveformAnnotation"			Usage="C"	Condition="NeedModuleWaveformAnnotation"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="HemodynamicWaveform"			Condition="HemodynamicWaveformInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="C"	Condition="ReallyNeedModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Waveform"
		Module="WaveformIdentification"		Usage="M"
		Module="Waveform"					Usage="M"
		Module="AcquisitionContext"			Usage="M"
		Module="WaveformAnnotation"			Usage="C"	Condition="NeedModuleWaveformAnnotation"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="CardiacElectrophysiologyWaveform"		Condition="CardiacElectrophysiologyWaveformInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="C"	Condition="ReallyNeedModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Waveform"
		Module="WaveformIdentification"		Usage="M"
		Module="Waveform"					Usage="M"
		Module="AcquisitionContext"			Usage="M"
		Module="WaveformAnnotation"			Usage="C"	Condition="NeedModuleWaveformAnnotation"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="BasicTextSR"				Condition="BasicTextSRStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EnhancedSR"				Condition="EnhancedSRStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="ComprehensiveSR"				Condition="ComprehensiveSRStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="Comprehensive3DSR"				Condition="Comprehensive3DSRStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="KeyObjectSelectionDocument"		Condition="KeyObjectSelectionDocumentStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="KeyObjectDocumentSeries"	Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="KeyObjectDocument"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="KeyObjectSelectionDocumentIHEXDSIManifest"		Condition="KeyObjectSelectionDocumentStorageInstance"	Profile="IHEXDSIManifest"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="KeyObjectDocumentSeries"	Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="KeyObjectDocument"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="IHEXDSIManifestProfile"		Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MammographyCADSR"				Condition="MammographyCADSRStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="ChestCADSR"				Condition="ChestCADSRStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="ProcedureLog"				Condition="ProcedureLogStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="XRayRadiationDoseSR"				Condition="XRayRadiationDoseSRStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="C"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="XRayRadiationDoseSRIHEREM"				Condition="XRayRadiationDoseSRStorageInstance"	Profile="IHEREM"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="C"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
		Module="IHEREMProfile"				Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RadiopharmaceuticalRadiationDoseSR"	Condition="RadiopharmaceuticalRadiationDoseSRStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="C"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="SpectaclePrescriptionReport" Condition="SpectaclePrescriptionReportInstance"
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
		Module="EnhancedGeneralEquipment"	Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="AcquisitionContextSR"	Condition="AcquisitionContextSRStorageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd	
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="SRDocumentSeries"			Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="Synchronization"			Usage="C"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="Document"
		Module="SRDocumentGeneral"			Usage="M"
		Module="SRDocumentContent"			Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="GrayscaleSoftcopyPresentationState"	Condition="GrayscaleSoftcopyPresentationStateInstance"
	InformationEntity="File"
		Module="FileMetaInformation"				Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"							Usage="M"
		Module="ClinicalTrialSubject"				Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"						Usage="M"
		Module="PatientStudy"						Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"					Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"						Usage="M"
		Module="ClinicalTrialSeries"				Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="PresentationSeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Presentation"
		Module="PresentationStateIdentification"	Usage="M"
		Module="PresentationStateRelationship"		Usage="M"
		Module="PresentationStateShutter"			Usage="M"
		Module="PresentationStateMask"				Usage="M"
		Module="Mask"								Usage="C"	Condition="NeedModuleMask"
		Module="DisplayShutter"						Usage="C"	Condition="NeedModuleDisplayShutter"
		Module="BitmapDisplayShutter"				Usage="C"	Condition="NeedModuleBitmapDisplayShutter"
		Module="OverlayPlane"						Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="OverlayActivation"					Usage="C"	Condition="NeedModuleOverlayActivation"
		Module="DisplayedArea"						Usage="M"
		Module="GraphicAnnotation"					Usage="C"	Condition="NeedModuleGraphicAnnotation"
		Module="SpatialTransformation"				Usage="C"	Condition="NeedModuleSpatialTransformation"
		Module="GraphicLayer"						Usage="C"	Condition="NeedModuleGraphicLayer"
		Module="ModalityLUT"						Usage="C"	Condition="NeedModuleModalityLUT"
		Module="SoftcopyVOILUT"						Usage="C"	Condition="NeedModuleSoftcopyVOILUT"
		Module="SoftcopyPresentationLUT"			Usage="M"
		Module="SOPCommon"							Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="ColorSoftcopyPresentationState"	Condition="ColorSoftcopyPresentationStateInstance"
	InformationEntity="File"
		Module="FileMetaInformation"				Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"							Usage="M"
		Module="ClinicalTrialSubject"				Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"						Usage="M"
		Module="PatientStudy"						Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"					Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"						Usage="M"
		Module="ClinicalTrialSeries"				Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="PresentationSeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Presentation"
		Module="PresentationStateIdentification"	Usage="M"
		Module="PresentationStateRelationship"		Usage="M"
		Module="PresentationStateShutter"			Usage="M"
		Module="DisplayShutter"						Usage="C"	Condition="NeedModuleDisplayShutter"
		Module="BitmapDisplayShutter"				Usage="C"	Condition="NeedModuleBitmapDisplayShutter"
		Module="OverlayPlane"						Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="OverlayActivation"					Usage="C"	Condition="NeedModuleOverlayActivation"
		Module="DisplayedArea"						Usage="M"
		Module="GraphicAnnotation"					Usage="C"	Condition="NeedModuleGraphicAnnotation"
		Module="SpatialTransformation"				Usage="C"	Condition="NeedModuleSpatialTransformation"
		Module="GraphicLayer"						Usage="C"	Condition="NeedModuleGraphicLayer"
		Module="ICCProfile"							Usage="M"
		Module="SOPCommon"							Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="PseudoColorSoftcopyPresentationState"	Condition="PseudoColorSoftcopyPresentationStateInstance"
	InformationEntity="File"
		Module="FileMetaInformation"				Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"							Usage="M"
		Module="ClinicalTrialSubject"				Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"						Usage="M"
		Module="PatientStudy"						Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"					Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"						Usage="M"
		Module="ClinicalTrialSeries"				Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="PresentationSeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Presentation"
		Module="PresentationStateIdentification"	Usage="M"
		Module="PresentationStateRelationship"		Usage="M"
		Module="PresentationStateShutter"			Usage="M"
		Module="PresentationStateMask"				Usage="M"
		Module="Mask"								Usage="C"	Condition="NeedModuleMask"
		Module="DisplayShutter"						Usage="C"	Condition="NeedModuleDisplayShutter"
		Module="BitmapDisplayShutter"				Usage="C"	Condition="NeedModuleBitmapDisplayShutter"
		Module="OverlayPlane"						Usage="C"	Condition="NeedModuleOverlayPlane"
		Module="OverlayActivation"					Usage="C"	Condition="NeedModuleOverlayActivation"
		Module="DisplayedArea"						Usage="M"
		Module="GraphicAnnotation"					Usage="C"	Condition="NeedModuleGraphicAnnotation"
		Module="SpatialTransformation"				Usage="C"	Condition="NeedModuleSpatialTransformation"
		Module="GraphicLayer"						Usage="C"	Condition="NeedModuleGraphicLayer"
		Module="ModalityLUT"						Usage="C"	Condition="NeedModuleModalityLUT"
		Module="SoftcopyVOILUT"						Usage="C"	Condition="NeedModuleSoftcopyVOILUT"
		Module="PaletteColorLookupTable"			Usage="M"
		Module="ICCProfile"							Usage="M"
		Module="SOPCommon"							Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="BlendingSoftcopyPresentationState"	Condition="BlendingSoftcopyPresentationStateInstance"
	InformationEntity="File"
		Module="FileMetaInformation"				Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"							Usage="M"
		Module="ClinicalTrialSubject"				Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"						Usage="M"
		Module="PatientStudy"						Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"					Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"						Usage="M"
		Module="ClinicalTrialSeries"				Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="PresentationSeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"					Usage="M"
	InformationEntityEnd
	InformationEntity="Presentation"
		Module="PresentationStateIdentification"	Usage="M"
		Module="PresentationStateBlending"			Usage="M"
		Module="DisplayedArea"						Usage="M"
		Module="GraphicAnnotation"					Usage="C"	Condition="NeedModuleGraphicAnnotation"
		Module="SpatialTransformation"				Usage="C"	Condition="NeedModuleSpatialTransformation"
		Module="GraphicLayer"						Usage="C"	Condition="NeedModuleGraphicLayer"
		Module="PaletteColorLookupTable"			Usage="M"
		Module="ICCProfile"							Usage="M"
		Module="SOPCommon"							Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="HangingProtocol"	Condition="HangingProtocolInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="HangingProtocol"
		Module="HangingProtocolDefinition"	Usage="M"
		Module="HangingProtocolEnvironment"	Usage="M"
		Module="HangingProtocolDisplay"		Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="ColorPalette"	Condition="ColorPaletteInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="ColorPalette"
		Module="ColorPaletteDefinition"		Usage="M"
		Module="PaletteColorLookupTable"	Usage="M"
		Module="ICCProfile"					Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="BasicStructuredDisplay"	Condition="BasicStructuredDisplayInstance"
	InformationEntity="File"
		Module="FileMetaInformation"				Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"							Usage="M"
		Module="ClinicalTrialSubject"				Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"						Usage="M"
		Module="PatientStudy"						Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"					Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"						Usage="M"
		Module="ClinicalTrialSeries"				Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="PresentationSeries"					Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"					Usage="M"
		Module="EnhancedGeneralEquipment"			Usage="U"	Condition="EnhancedGeneralEquipmentIsPresent"
	InformationEntityEnd
	InformationEntity="Presentation"
		Module="StructuredDisplay"					Usage="M"
		Module="StructuredDisplayImageBox"			Usage="M"
		Module="StructuredDisplayAnnotation"		Usage="U"	Condition="NeedModuleStructuredDisplayAnnotation"
		Module="CommonInstanceReference"			Usage="M"
		Module="SOPCommon"							Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EnhancedMRImage"			Condition="EnhancedMRImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="MRSeries"										Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="EnhancedContrastBolus"							Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForEnhancedMRImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="M"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="BulkMotionSynchronization"						Usage="C"	Condition="NeedModuleBulkMotion"
		Module="SupplementalPaletteColorLUT"					Usage="C"	Condition="NeedModuleSupplementalPaletteColorLUT"
		Module="AcquisitionContext"								Usage="M"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedMRImage"								Usage="M"
		Module="MRPulseSequence"								Usage="C"	Condition="NeedModuleMRPulseSequence"
		Module="ICCProfile"										Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EnhancedMRColorImage"			Condition="EnhancedMRColorImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="MRSeries"										Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="EnhancedContrastBolus"							Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForEnhancedMRImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="M"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="BulkMotionSynchronization"						Usage="C"	Condition="NeedModuleBulkMotion"
		Module="SupplementalPaletteColorLUT"					Usage="C"	Condition="NeedModuleSupplementalPaletteColorLUT"
		Module="AcquisitionContext"								Usage="M"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"										Usage="C"	Condition="NeedModuleSpecimen"
		Module="EnhancedMRImage"								Usage="M"
		Module="MRPulseSequence"								Usage="C"	Condition="NeedModuleMRPulseSequence"
		Module="ICCProfile"										Usage="M"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="MRSpectroscopy"			Condition="MRSpectroscopyInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="MRSeries"										Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="M"
	InformationEntityEnd
	InformationEntity="MRSpectroscopy"
		Module="EnhancedContrastBolus"							Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForMRSpectroscopy"	Usage="M"
		Module="MultiFrameDimension"							Usage="M"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="BulkMotionSynchronization"						Usage="C"	Condition="NeedModuleBulkMotion"
		Module="AcquisitionContext"								Usage="M"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="MRSpectroscopy"									Usage="M"
		Module="MRSpectroscopyPulseSequence"					Usage="C"	Condition="NeedModuleMRSpectroscopyPulseSequence"
		Module="MRSpectroscopyData"								Usage="M"
		Module="SOPCommon"										Usage="M"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="RawData"			Condition="RawDataInstance"
	InformationEntity="File"
		Module="FileMetaInformation"		Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"					Usage="M"
		Module="ClinicalTrialSubject"		Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"				Usage="M"
		Module="PatientStudy"				Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"			Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"				Usage="M"
		Module="ClinicalTrialSeries"		Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"			Usage="U"	Condition="NeedModuleFrameOfReference"
		Module="Synchronization"			Usage="C"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"			Usage="M"
	InformationEntityEnd
	InformationEntity="RawData"
		Module="AcquisitionContext"			Usage="M"
		Module="Specimen"					Usage="U"	Condition="NeedModuleSpecimen"
		Module="RawData"					Usage="M"
		Module="SOPCommon"					Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="LegacyConvertedEnhancedMRImage"	Condition="LegacyConvertedEnhancedMRImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="MRSeries"										Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="U"	Condition="EnhancedGeneralEquipmentIsPresent"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="ContrastBolus"									Usage="U"	Condition="NeedModuleContrastBolus"
		Module="EnhancedContrastBolus"							Usage="U"	Condition="NeedModuleEnhancedContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForLegacyConvertedEnhancedMRImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="CardiacSynchronization"							Usage="U"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="U"	Condition="NeedModuleRespiratorySynchronization"
		Module="BulkMotionSynchronization"						Usage="U"	Condition="NeedModuleBulkMotion"
		Module="AcquisitionContext"								Usage="M"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedMRImage"								Usage="M"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="PrivatePixelMedLegacyConvertedEnhancedMRImage"	Condition="PrivatePixelMedLegacyConvertedEnhancedMRImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="MRSeries"										Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="U"	Condition="EnhancedGeneralEquipmentIsPresent"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="ContrastBolus"									Usage="C"	Condition="NeedModuleContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForPrivatePixelMedLegacyConvertedEnhancedMRImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="C"	Condition="NeedModuleMultiFrameDimension"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="BulkMotionSynchronization"						Usage="C"	Condition="NeedModuleBulkMotion"
		Module="AcquisitionContext"								Usage="M"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedMRImage"								Usage="M"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="TractographyResults" Condition="TractographyResultsInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="TractographyResultsSeries"						Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="M"
	InformationEntityEnd
	InformationEntity="TractographyResults"
		Module="TractographyResults"							Usage="M"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="CommonInstanceReference"						Usage="M"
		Module="SOPCommon"										Usage="M"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EnhancedCTImage"			Condition="EnhancedCTImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="CTSeries"										Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="EnhancedContrastBolus"							Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForEnhancedCTImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="M"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="SupplementalPaletteColorLUT"					Usage="C"	Condition="NeedModuleSupplementalPaletteColorLUT"
		Module="AcquisitionContext"								Usage="M"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedCTImage"								Usage="M"
		Module="EnhancedMultienergyCTAcquisition"				Usage="C"	Condition="IsMultienergyCTAcquisition"
		Module="ICCProfile"										Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"	Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="LegacyConvertedEnhancedCTImage"	Condition="LegacyConvertedEnhancedCTImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="CTSeries"										Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="U"	Condition="EnhancedGeneralEquipmentIsPresent"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="ContrastBolus"									Usage="U"	Condition="NeedModuleContrastBolus"
		Module="EnhancedContrastBolus"							Usage="U"	Condition="NeedModuleEnhancedContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForLegacyConvertedEnhancedCTImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="U"	Condition="NeedModuleMultiFrameDimension"
		Module="CardiacSynchronization"							Usage="U"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="U"	Condition="NeedModuleRespiratorySynchronization"
		Module="AcquisitionContext"								Usage="M"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedCTImage"								Usage="M"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="PrivatePixelMedLegacyConvertedEnhancedCTImage"	Condition="PrivatePixelMedLegacyConvertedEnhancedCTImageInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="CTSeries"										Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="Synchronization"								Usage="U"	Condition="NeedToCheckModuleSynchronization"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="U"	Condition="EnhancedGeneralEquipmentIsPresent"
	InformationEntityEnd
	InformationEntity="Image"
		Module="ImagePixel"										Usage="M"
		Module="ContrastBolus"									Usage="C"	Condition="NeedModuleContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForPrivatePixelMedLegacyConvertedEnhancedCTImage"	Usage="M"
		Module="MultiFrameDimension"							Usage="C"	Condition="NeedModuleMultiFrameDimension"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="AcquisitionContext"								Usage="M"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedCTImage"								Usage="M"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd
CompositeIOD="EnhancedUltrasoundVolume"			Condition="EnhancedUltrasoundVolumeInstance"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="EnhancedUSSeries"								Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="UltrasoundFrameOfReference"						Usage="M"
		Module="Synchronization"								Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"									Usage="M"
		Module="GeneralReference"								Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"										Usage="M"
		Module="EnhancedContrastBolus"							Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForEnhancedUSVolume"	Usage="M"
		Module="MultiFrameDimension"							Usage="M"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="AcquisitionContext"								Usage="M"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedPaletteColorLookupTable"				Usage="U"	Condition="NeedModuleEnhancedPaletteColorLookupTable"
		Module="EnhancedUSImage"								Usage="M"
		Module="IVUSImage"										Usage="C"	Condition="ModalityIsIVUS"
		Module="ExcludedIntervals"								Usage="U"	Condition="NeedModuleExcludedIntervals"
		Module="ICCProfile"										Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
	InformationEntityEnd
CompositeIODEnd

CompositeIOD="EnhancedUltrasoundVolumeQTUS"			Condition="EnhancedUltrasoundVolumeInstance"	Profile="QTUS"
	InformationEntity="File"
		Module="FileMetaInformation"							Usage="C"	Condition="NeedModuleFileMetaInformation"
	InformationEntityEnd
	InformationEntity="Patient"
		Module="Patient"										Usage="M"
		Module="ClinicalTrialSubject"							Usage="U"	Condition="NeedModuleClinicalTrialSubject"
	InformationEntityEnd
	InformationEntity="Study"
		Module="GeneralStudy"									Usage="M"
		Module="PatientStudy"									Usage="U"	# no condition ... all attributes type 3
		Module="ClinicalTrialStudy"								Usage="U"	Condition="NeedModuleClinicalTrialStudy"
		Module="QTUSEnhancedUltrasoundVolumeProfileStudy"		Usage="M"
	InformationEntityEnd
	InformationEntity="Series"
		Module="GeneralSeries"									Usage="M"
		Module="ClinicalTrialSeries"							Usage="U"	Condition="NeedModuleClinicalTrialSeries"
		Module="EnhancedUSSeries"								Usage="M"
		Module="QTUSEnhancedUltrasoundVolumeProfileSeries"		Usage="M"
	InformationEntityEnd
	InformationEntity="FrameOfReference"
		Module="FrameOfReference"								Usage="M"
		Module="UltrasoundFrameOfReference"						Usage="M"
		Module="Synchronization"								Usage="M"
		Module="QTUSEnhancedUltrasoundVolumeProfileFrameOfReference"	Usage="M"
	InformationEntityEnd
	InformationEntity="Equipment"
		Module="GeneralEquipment"								Usage="M"
		Module="EnhancedGeneralEquipment"						Usage="M"
		Module="QTUSEnhancedUltrasoundVolumeProfileEquipment"	Usage="M"
	InformationEntityEnd
	InformationEntity="Image"
		Module="GeneralImage"									Usage="M"
		Module="GeneralReference"								Usage="U"	Condition="NeedModuleGeneralReference"
		Module="ImagePixel"										Usage="M"
		Module="EnhancedContrastBolus"							Usage="C"	Condition="NeedModuleEnhancedContrastBolus"
		Module="MultiFrameFunctionalGroupsCommon"				Usage="M"
		Module="MultiFrameFunctionalGroupsForEnhancedUSVolume"	Usage="M"
		Module="MultiFrameDimension"							Usage="M"
		Module="CardiacSynchronization"							Usage="C"	Condition="NeedModuleCardiacSynchronization"
		Module="RespiratorySynchronization"						Usage="C"	Condition="NeedModuleRespiratorySynchronization"
		Module="Device"											Usage="U"	Condition="NeedModuleDevice"
		Module="AcquisitionContext"								Usage="M"
		Module="Specimen"										Usage="U"	Condition="NeedModuleSpecimen"
		Module="EnhancedPaletteColorLookupTable"				Usage="U"	Condition="NeedModuleEnhancedPaletteColorLookupTable"
		Module="EnhancedUSImage"								Usage="M"
		Module="IVUSImage"										Usage="C"	Condition="ModalityIsIVUS"
		Module="ExcludedIntervals"								Usage="U"	Condition="NeedModuleExcludedIntervals"
		Module="ICCProfile"										Usage="U"	Condition="NeedModuleICCProfile"
		Module="SOPCommon"										Usage="M"
		Module="CommonInstanceReference"						Usage="U"	Condition="NeedModuleCommonInstanceReference"
		Module="FrameExtraction"								Usage="C"	Condition="NeedModuleFrameExtraction"
		Module="QTUSEnhancedUltrasoundVolumeProfileInstance"	Usage="M"
	InformationEntityEnd
CompositeIODEnd

