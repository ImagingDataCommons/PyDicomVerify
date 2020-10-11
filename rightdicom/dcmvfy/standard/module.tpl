DefineMacro="IconImageSequenceMacro"
	#InvokeMacro="ImagePixelMacro" # would be nice to do this, but can't then insert verify statements (undeclared variables)
	Name="SamplesPerPixel"							Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"				Type="1"	StringEnumValues="IconImagePhotometricInterpretation"
	Name="Rows"										Type="1"	NotZeroError=""
	Name="Columns"									Type="1"	NotZeroError=""
	Name="BitsAllocated"							Type="1"	BinaryEnumValues="BitsAre1Or8"
	Name="BitsStored"								Type="1"	BinaryEnumValues="BitsAre1Or8"
	Name="HighBit"									Type="1"	BinaryEnumValues="BitsAre0Or7"
	Name="PixelRepresentation"						Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="PixelData"								Type="1"
	Name="PlanarConfiguration"						Type="1C"	BinaryEnumValues="PlanarConfiguration"	Condition="Never"
	Name="PixelAspectRatio"							Type="3"	BinaryEnumValues="One"
	Name="SmallestImagePixelValue"					Type="3"
	Name="LargestImagePixelValue"					Type="3"
	Name="RedPaletteColorLookupTableDescriptor"		Type="1C"	Condition="PhotometricInterpretationNeedsPalette"
	Verify="RedPaletteColorLookupTableDescriptor"				ValueSelector="2"	BinaryEnumValues="BitsAre8Or16"
	Name="GreenPaletteColorLookupTableDescriptor"	Type="1C"	Condition="PhotometricInterpretationNeedsPalette"
	Verify="GreenPaletteColorLookupTableDescriptor"				ValueSelector="2"	BinaryEnumValues="BitsAre8Or16"
	Name="BluePaletteColorLookupTableDescriptor"	Type="1C"	Condition="PhotometricInterpretationNeedsPalette"
	Verify="BluePaletteColorLookupTableDescriptor"				ValueSelector="2"	BinaryEnumValues="BitsAre8Or16"
	Name="RedPaletteColorLookupTableData"			Type="1C"	Condition="PhotometricInterpretationNeedsPalette"
	Name="GreenPaletteColorLookupTableData"			Type="1C"	Condition="PhotometricInterpretationNeedsPalette"
	Name="BluePaletteColorLookupTableData"			Type="1C"	Condition="PhotometricInterpretationNeedsPalette"
	Name="ICCProfile"								Type="3"
	Name="ColorSpace"								Type="3"
MacroEnd

DefineMacro="BasicCodeSequenceMacro"
	Name="CodeValue"						Type="1C"	Condition="LongCodeValueAndURNCodeValueAbsent"
	Verify="CodeValue"									Condition="CodeValueIllegalOrDeprecated"	ThenErrorMessage="Code Value is illegal or deprecated" ShowValueWithMessage="true"
	Name="CodingSchemeDesignator"			Type="1C"	Condition="CodeValueOrLongCodeValuePresent"	StringDefinedTerms="MiscellaneousCodingSchemeDesignators"	mbpo="true"
	Verify="CodingSchemeDesignator"						Condition="CodingSchemeDesignatorDeprecated"	ThenWarningMessage="Coding Scheme Designator is deprecated" ShowValueWithMessage="true"
	Name="CodingSchemeVersion"				Type="1C"	Condition="CodingSchemeVersionRequired" mbpo="true"
	Name="CodeMeaning"						Type="1"
	Verify="CodeMeaning"								Condition="CodeMeaningIllegalOrDeprecated"	ThenErrorMessage="Code Meaning is illegal or deprecated" ShowValueWithMessage="true"
	Name="LongCodeValue"					Type="1C"	Condition="CodeValueAndURNCodeValueAbsent"
	Name="URNCodeValue"						Type="1C"	Condition="CodeValueAndLongCodeValueAbsent"
MacroEnd

DefineMacro="EnhancedCodeSequenceMacro"
	Name="ContextIdentifier"				Type="3"
	Name="ContextUID"						Type="3"
	Name="MappingResource"					Type="1C"	Condition="ContextIdentifierIsPresent"		StringDefinedTerms="MappingResources"
	Name="MappingResourceUID"				Type="3"	StringDefinedTerms="MappingResourceUIDs"
	Name="MappingResourceName"				Type="3"	StringDefinedTerms="MappingResourceNames"
	Name="ContextGroupVersion"				Type="1C"	Condition="ContextIdentifierIsPresent"
	Name="ContextGroupExtensionFlag"		Type="3"	StringEnumValues="YesNoLetter"
	Name="ContextGroupLocalVersion"			Type="1C"	Condition="ExtendedCodingScheme"
	Name="ContextGroupExtensionCreatorUID"	Type="1C"	Condition="ExtendedCodingScheme"
MacroEnd

DefineMacro="CodeSequenceMacro"
	InvokeMacro="BasicCodeSequenceMacro"
	Sequence="EquivalentCodeSequence"		Type="3"	VM="1-n"
		InvokeMacro="BasicCodeSequenceMacro"
		InvokeMacro="EnhancedCodeSequenceMacro"
	SequenceEnd
	InvokeMacro="EnhancedCodeSequenceMacro"
MacroEnd

DefineMacro="BasicCodeSequenceMeaningOptionalMacro"
	Name="CodeValue"						Type="1C"	Condition="LongCodeValueAndURNCodeValueAbsent"
	Verify="CodeValue"									Condition="CodeValueIllegalOrDeprecated"	ThenErrorMessage="Code Value is illegal or deprecated" ShowValueWithMessage="true"
	Name="CodingSchemeDesignator"			Type="1C"	Condition="CodeValueOrLongCodeValuePresent"	StringDefinedTerms="MiscellaneousCodingSchemeDesignators"	mbpo="true"
	Verify="CodingSchemeDesignator"						Condition="CodingSchemeDesignatorDeprecated"	ThenWarningMessage="Coding Scheme Designator is deprecated" ShowValueWithMessage="true"
	Name="CodingSchemeVersion"				Type="1C"	Condition="CodingSchemeVersionRequired" mbpo="true"
	Name="CodeMeaning"						Type="3"
	Verify="CodeMeaning"								Condition="CodeMeaningEmptyOrNotPresent"	ThenWarningMessage="Code Meaning is missing or empty, which is legal but undesirable"
	Verify="CodeMeaning"								Condition="CodeMeaningIllegalOrDeprecated"	ThenErrorMessage="Code Meaning is illegal or deprecated" ShowValueWithMessage="true"
	Name="LongCodeValue"					Type="1C"	Condition="CodeValueAndURNCodeValueAbsent"
	Name="URNCodeValue"						Type="1C"	Condition="CodeValueAndLongCodeValueAbsent"
MacroEnd

DefineMacro="CodeSequenceMeaningOptionalMacro"
	InvokeMacro="BasicCodeSequenceMeaningOptionalMacro"
	Sequence="EquivalentCodeSequence"		Type="3"	VM="1-n"
		InvokeMacro="BasicCodeSequenceMacro"
		InvokeMacro="EnhancedCodeSequenceMacro"
	SequenceEnd
	InvokeMacro="EnhancedCodeSequenceMacro"
MacroEnd

DefineMacro="PersonIdentificationMacro"
	Sequence="PersonIdentificationCodeSequence"			Type="1"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="PersonAddress"								Type="3"
	Name="PersonTelephoneNumbers"						Type="3"
	Name="InstitutionName"								Type="1C"	Condition="InstitutionCodeSequenceNotPresent"
	Name="InstitutionAddress"							Type="3"
	Sequence="InstitutionCodeSequence"					Type="1C"	VM="1"	Condition="InstitutionNameNotPresent"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="InstitutionalDepartmentName"					Type="3"
	Sequence="InstitutionalDepartmentTypeCodeSequence"	Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="7030"
	SequenceEnd
MacroEnd

DefineMacro="ContentItemMacro"
	Name="ValueType"						Type="1"	StringEnumValues="ContentItemValueTypes"
	Name="ObservationDateTime"				Type="3"
	Sequence="ConceptNameCodeSequence"		Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="DateTime"							Type="1C"	Condition="ValueTypeIsDateTime"
	Name="Date"								Type="1C"	Condition="ValueTypeIsDate"
	Name="Time"								Type="1C"	Condition="ValueTypeIsTime"
	Name="PersonName"						Type="1C"	Condition="ValueTypeIsPersonName"
	Name="UID"								Type="1C"	Condition="ValueTypeIsUID"
	Name="TextValue"						Type="1C"	Condition="ValueTypeIsText"
	Sequence="ConceptCodeSequence"			Type="1C"	VM="1"	Condition="ValueTypeIsCode"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="NumericValue"						Type="1C"	Condition="ValueTypeIsNumeric"
	Name="FloatingPointValue"				Type="1C"	NoCondition=""
	Verify="FloatingPointValue"							Condition="FloatingPointValuePresentButValueTypeIsNotNumeric"	ThenErrorMessage="May only be present for NUMERIC ValueType"
	Name="RationalNumeratorValue"			Type="1C"	NoCondition=""
	Verify="RationalNumeratorValue"						Condition="RationalNumeratorValuePresentButValueTypeIsNotNumeric"	ThenErrorMessage="May only be present for NUMERIC ValueType"
	Name="RationalDenominatorValue"			Type="1C"	Condition="RationalNumeratorValueIsPresent" NotZeroError=""
	Verify="RationalDenominatorValue"					Condition="RationalDenominatorValueButValueTypeIsNotNumeric"	ThenErrorMessage="May only be present for NUMERIC ValueType"
	Sequence="MeasurementUnitsCodeSequence"	Type="1C"	VM="1"	Condition="ValueTypeIsNumeric"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="ReferencedSOPSequence"		Type="1C"	VM="1"	Condition="ValueTypeIsCompositeOrImage"
		InvokeMacro="SOPInstanceReferenceMacro"
		Name="ReferencedFrameNumber"		Type="1C"	NoCondition=""	NotZeroError=""	# cannot just check SOP Class and mbpo false, since may be absent for multi-frame if applies to all frames (including multi-frame SOP Class with only 1 frame) :(
		Verify="ReferencedFrameNumber"					Condition="ReferencedFrameNumberPresentAndReferencedSOPClassUIDIsNotMultiFrame"	ThenErrorMessage="May not be present for Referenced SOP Class that is not multi-frame"
		Name="ReferencedSegmentNumber"		Type="1C"	NoCondition=""	NotZeroError=""	# cannot just check SOP Class and mbpo false, since may be absent for segmentation if applies to all segments :(
		Verify="ReferencedSegmentNumber"				Condition="ReferencedSegmentNumberPresentAndReferencedSOPClassUIDIsNotSegmentationOrSurfaceSegmentation"	ThenErrorMessage="May not be present for Referenced SOP Class that is not segmentation"
		Verify="ReferencedSegmentNumber"				Condition="ReferencedFrameNumberAndReferencedSegmentNumberPresent"	ThenErrorMessage="May not be present when ReferencedFrameNumber is present"
		SequenceEnd
MacroEnd

DefineMacro="ContentItemWithModifiersMacro"
	InvokeMacro="ContentItemMacro"
	Sequence="ContentItemModifierSequence"	Type="3"	VM="1-n"
		InvokeMacro="ContentItemMacro"
	SequenceEnd
MacroEnd

DefineMacro="ImageSOPInstanceReferenceMacro" InformationEntity="Image"
	InvokeMacro="SOPInstanceReferenceMacro"
	Name="ReferencedFrameNumber"					Type="1C"	NoCondition=""	NotZeroError=""	# cannot just check SOP Class and mbpo false, since may be absent for multi-frame if applies to all frames (including multi-frame SOP Class with only 1 frame) :(
	Verify="ReferencedFrameNumber"								Condition="ReferencedFrameNumberPresentAndReferencedSOPClassUIDIsNotMultiFrame"	ThenErrorMessage="May not be present for Referenced SOP Class that is not multi-frame"
	Name="ReferencedSegmentNumber"					Type="1C"	NoCondition=""	NotZeroError=""	# cannot just check SOP Class and mbpo false, since may be absent for segmentation if applies to all segments :(
	Verify="ReferencedSegmentNumber"							Condition="ReferencedSegmentNumberPresentAndReferencedSOPClassUIDIsNotSegmentationOrSurfaceSegmentation"	ThenErrorMessage="May not be present for Referenced SOP Class that is not segmentation"
	Verify="ReferencedSegmentNumber"							Condition="ReferencedFrameNumberAndReferencedSegmentNumberPresent"	ThenErrorMessage="May not be present when ReferencedFrameNumber is present"
MacroEnd

DefineMacro="ReferencedInstancesAndAccessMacro" InformationEntity="Image"
	Name="TypeOfInstances"					Type="1"	VM="1"	StringDefinedTerms="TypeOfInstances"
	Name="StudyInstanceUID"					Type="1C"	VM="1"	Condition="TypeOfInstancesIsDICOM"
	Name="SeriesInstanceUID"				Type="1C"	VM="1"	Condition="TypeOfInstancesIsDICOM"
	Sequence="ReferencedSOPSequence"		Type="1"	VM="1-n"
		Name="ReferencedSOPClassUID"		Type="1"
		Name="ReferencedSOPInstanceUID"		Type="1"
		Name="HL7InstanceIdentifier"		Type="1C"	VM="1"	Condition="TypeOfInstancesInParentIsCDA"
		Name="ReferencedFrameNumber"		Type="1C"	VM="1"	NoCondition="" mbpo="true"	# real-world - could check mutually exclusive with ReferencedSegmentNumber though :(
		Name="ReferencedSegmentNumber"		Type="1C"	VM="1"	NoCondition="" mbpo="true"	# real-world - could check mutually exclusive with ReferencedFrameNumber though :(
	SequenceEnd
	Sequence="DICOMRetrievalSequence"		Type="1C"	VM="1"	Condition="NeedDICOMRetrievalSequence" mbpo="true"
		Name="RetrieveAETitle"				Type="1"
	SequenceEnd
	Sequence="DICOMMediaRetrievalSequence"	Type="1C"	VM="1"	Condition="NeedDICOMMediaRetrievalSequence" mbpo="true"
		Name="StorageMediaFileSetID"		Type="2"
		Name="StorageMediaFileSetUID"		Type="1"
	SequenceEnd
	Sequence="WADORetrievalSequence"		Type="1C"	VM="1"	Condition="NeedWADORetrievalSequence" mbpo="true"
		Name="RetrieveURI"					Type="1"
	SequenceEnd
	Sequence="XDSRetrievalSequence"			Type="1C"	VM="1"	Condition="NeedXDSRetrievalSequence" mbpo="true"
		Name="RepositoryUniqueID"			Type="1"
		Name="HomeCommunityID"				Type="3"
	SequenceEnd
	Sequence="WADORSRetrievalSequence"		Type="1C"	VM="1"	Condition="NeedWADORSRetrievalSequence" mbpo="true"
		Name="RetrieveURL"					Type="1"
	SequenceEnd
MacroEnd

DefineMacro="SeriesAndInstanceReferenceMacro" InformationEntity="Image"
	Sequence="ReferencedSeriesSequence"				Type="1"	VM="1-n"
		Name="SeriesInstanceUID"					Type="1"
		Sequence="ReferencedInstanceSequence"		Type="1"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="PrimaryAnatomicStructureMacro" InformationEntity="Frame"
	Sequence="PrimaryAnatomicStructureSequence"				Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
		Sequence="PrimaryAnatomicStructureModifierSequence"	Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"	BaselineContextID="2"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="GeneralAnatomyMandatoryMacro" InformationEntity="Frame"
	Sequence="AnatomicRegionSequence"						Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"
		Sequence="AnatomicRegionModifierSequence"			Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"	BaselineContextID="2"
		SequenceEnd
	SequenceEnd
	InvokeMacro="PrimaryAnatomicStructureMacro"
	Sequence="AnatomicRegionModifierSequence"				Type="1C"	VM="1-n"	Condition="Never"
	SequenceEnd
	Sequence="PrimaryAnatomicStructureModifierSequence"		Type="1C"	VM="1-n"	Condition="Never"
	SequenceEnd
MacroEnd

DefineMacro="GeneralAnatomyRequiredMacro" InformationEntity="Frame"
	Sequence="AnatomicRegionSequence"						Type="2"	VM="0-1"
		InvokeMacro="CodeSequenceMacro"
		Sequence="AnatomicRegionModifierSequence"			Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"	BaselineContextID="2"
		SequenceEnd
	SequenceEnd
	Verify="AnatomicRegionSequence"													Condition="AnatomicRegionSequencePresentAndEmptyButBodyPartExaminedHasValue"	ThenErrorMessage="AnatomicRegionSequence is only permitted to be empty when actually unknown, but BodyPartExamined has a value, therefore it is known"
	InvokeMacro="PrimaryAnatomicStructureMacro"
	Sequence="AnatomicRegionModifierSequence"				Type="1C"	VM="1-n"	Condition="Never"
	SequenceEnd
	Sequence="PrimaryAnatomicStructureModifierSequence"		Type="1C"	VM="1-n"	Condition="Never"
	SequenceEnd
MacroEnd

DefineMacro="GeneralAnatomyOptionalMacro" InformationEntity="Frame"
	Sequence="AnatomicRegionSequence"						Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
		Sequence="AnatomicRegionModifierSequence"			Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"	BaselineContextID="2"
		SequenceEnd
	SequenceEnd
	InvokeMacro="PrimaryAnatomicStructureMacro"
	Sequence="AnatomicRegionModifierSequence"				Type="1C"	VM="1-n"	Condition="Never"
	SequenceEnd
	Sequence="PrimaryAnatomicStructureModifierSequence"		Type="1C"	VM="1-n"	Condition="Never"
	SequenceEnd
MacroEnd

DefineMacro="RequestAttributesMacro" InformationEntity="Series"
	Name="RequestedProcedureID"							Type="1C"	NoCondition="" mbpo="true"
	Name="AccessionNumber"								Type="3"
	Sequence="IssuerOfAccessionNumberSequence"			Type="3"	VM="1"
		InvokeMacro="HL7v2HierarchicDesignatorMacro"
	SequenceEnd
	Name="StudyInstanceUID"								Type="3"
	Sequence="ReferencedStudySequence"					Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Name="RequestedProcedureDescription"				Type="3"
	Sequence="RequestedProcedureCodeSequence"			Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="ReasonForTheRequestedProcedure"				Type="3"
	Sequence="ReasonForRequestedProcedureCodeSequence"	Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="ScheduledProcedureStepID"						Type="1C"	NoCondition="" mbpo="true"
	Name="ScheduledProcedureStepDescription"			Type="3"
	Sequence="ScheduledProtocolCodeSequence"			Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
		Sequence="ProtocolContextSequence"				Type="3"	VM="1-n"
			InvokeMacro="ContentItemMacro"
			Sequence="ContentItemModifierSequence"		Type="3"	VM="1-n"
				InvokeMacro="ContentItemMacro"
			SequenceEnd
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="BasicPixelSpacingCalibrationMacro" InformationEntity="Frame"
	Name="PixelSpacing"							Type="1C"	NoCondition=""	NotZeroError=""
	Name="PixelSpacingCalibrationType"			Type="3"
	Name="PixelSpacingCalibrationDescription"	Type="1C"	Condition="PixelSpacingCalibrationTypeIsPresent"
MacroEnd

DefineMacro="SOPInstanceReferenceMacro"
	Name="ReferencedSOPClassUID"				Type="1"
	Name="ReferencedSOPInstanceUID"				Type="1"
MacroEnd

DefineMacro="DisplayShutterMacro" InformationEntity="Frame"
	Name="ShutterShape"							Type="1"	StringEnumValues="ShutterShape"
	Name="ShutterLeftVerticalEdge"				Type="1C"	Condition="ShutterShapeIsRectangular"
	Name="ShutterRightVerticalEdge"				Type="1C"	Condition="ShutterShapeIsRectangular"
	Name="ShutterUpperHorizontalEdge"			Type="1C"	Condition="ShutterShapeIsRectangular"
	Name="ShutterLowerHorizontalEdge"			Type="1C"	Condition="ShutterShapeIsRectangular"
	Name="CenterOfCircularShutter"				Type="1C"	Condition="ShutterShapeIsCircular"
	Name="RadiusOfCircularShutter"				Type="1C"	Condition="ShutterShapeIsCircular"
	Name="VerticesOfThePolygonalShutter"		Type="1C"	Condition="ShutterShapeIsPolygonal"
	Name="ShutterPresentationValue"				Type="3"
	Name="ShutterPresentationColorCIELabValue"	Type="3"
MacroEnd

DefineMacro="ContentIdentificationMacro" InformationEntity="Instance"
	Name="InstanceNumber"										Type="1"
	Name="ContentLabel"											Type="1"
	Name="ContentDescription"									Type="2"
	Sequence="ConceptNameCodeSequence"							Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="AlternateContentDescriptionSequence"				Type="3"	VM="1-n"
		Name="ContentDescription"								Type="1"
		Sequence="LanguageCodeSequence"							Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"									DefinedContextID="5000"
		SequenceEnd
		Sequence="ConceptNameCodeSequence"						Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="ContentCreatorName"									Type="2"
	Sequence="ContentCreatorIdentificationCodeSequence"		Type="3"	VM="1"
		InvokeMacro="PersonIdentificationMacro"
	SequenceEnd
MacroEnd

DefineMacro="HL7v2HierarchicDesignatorMacro"
	Name="LocalNamespaceEntityID"								Type="1C"	Condition="UniversalEntityIDNotPresent" mbpo="true"
	Name="UniversalEntityID"									Type="1C"	Condition="LocalNamespaceEntityIDNotPresent" mbpo="true"
	Name="UniversalEntityIDType"								Type="1C"	Condition="UniversalEntityIDPresent" StringDefinedTerms="UniversalEntityIDType"
MacroEnd

DefineMacro="IssuerOfPatientIDMacro"
	Name="IssuerOfPatientID"									Type="3"
	Sequence="IssuerOfPatientIDQualifiersSequence"				Type="3"	VM="1"
		Name="UniversalEntityID"								Type="3"
		Name="UniversalEntityIDType"							Type="3"	StringDefinedTerms="UniversalEntityIDType"
		Name="IdentifierTypeCode"								Type="3"	StringDefinedTerms="HL7Table0203IdentifierType"
		Sequence="AssigningFacilitySequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Sequence="AssigningJurisdictionCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"									BaselineContextID="5001"
		SequenceEnd
		Sequence="AssigningAgencyOrDepartmentCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="AlgorithmIdentificationMacro"
	Sequence="AlgorithmFamilyCodeSequence"						Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="AlgorithmNameCodeSequence"						Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="AlgorithmName"										Type="1"
	Name="AlgorithmVersion"										Type="1"
	Name="AlgorithmParameters"									Type="3"
	Name="AlgorithmSource"										Type="3"
MacroEnd

DefineMacro="SelectorAttributeMacro"
	Name="SelectorAttribute"						Type="1C"	VM="1"	NoCondition=""
	Name="SelectorValueNumber"						Type="1C"	VM="1"	NoCondition=""
	Name="SelectorSequencePointer"					Type="1C"	VM="1"	NoCondition=""
	Name="SelectorSequencePointerPrivateCreator"	Type="1C"	VM="1"	NoCondition=""
	Name="SelectorSequencePointerItems"				Type="1C"	VM="1"	Condition="SelectorSequencePointerIsPresent"
	Name="SelectorAttributePrivateCreator"			Type="1C"	VM="1"	NoCondition=""
MacroEnd

DefineMacro="ExtendedSelectorAttributeMacro"
	Name="SelectorAttributeName"					Type="1"	VM="1"
	Name="SelectorAttributeKeyword"					Type="3"	VM="1"
	Name="SelectorAttributeVR"						Type="1"	VM="1"
	InvokeMacro="SelectorAttributeMacro"
MacroEnd

DefineMacro="DataSetIdentificationMacro"
	Name="DataSetName"			Type="1"
	Name="DataSetVersion"		Type="1"
	Name="DataSetSource"		Type="1"
	Name="DataSetDescription"	Type="3"
MacroEnd

# no information entity specified for this macro, else screws up attributes that are otherwise at the Series entity level
DefineMacro="GeneralContributingSourcesMacro"
	Sequence="ContributingSOPInstancesReferenceSequence"	Type="1C"	VM="1-n"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
		Name="StudyInstanceUID"								Type="3"
		Sequence="ReferencedSeriesSequence"					Type="1"	VM="1-n"
			Name="SeriesInstanceUID"						Type="1"
			Name="SeriesNumber"								Type="2"
			Sequence="ReferencedInstanceSequence"			Type="1"	VM="1-n"
				InvokeMacro="SOPInstanceReferenceMacro"
				Name="InstanceNumber"						Type="2"
			SequenceEnd
		SequenceEnd
	SequenceEnd
	Name="Manufacturer"										Type="2"
	Name="ManufacturerModelName"							Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
	Name="DeviceSerialNumber"								Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
	Name="SoftwareVersions"									Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
	Name="AcquisitionDateTime"								Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
	Name="StationName"										Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
	Name="OperatorsName"									Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
	Sequence="OperatorIdentificationSequence"				Type="1C"	VM="1-n"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
		InvokeMacro="PersonIdentificationMacro"
	SequenceEnd
	Name="ProtocolName"										Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
	Sequence="PerformedProtocolCodeSequence"				Type="1C"	VM="1-n"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="AcquisitionProtocolName"							Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
MacroEnd

DefineMacro="ContributingImageSourcesMacro" InformationEntity="Instance"
	Name="Rows"												Type="1"	NotZeroError=""
	Name="Columns"											Type="1"	NotZeroError=""
	Name="BitsStored"										Type="1"	NotZeroError=""
	Name="LossyImageCompression"							Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"						Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"						Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
MacroEnd

DefineMacro="PatientOrientationMacro" InformationEntity="Instance"
	Sequence="PatientOrientationCodeSequence"				Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"									BaselineContextID="19"
		Sequence="PatientOrientationModifierCodeSequence"   Type="1C"	VM="1"	NoCondition=""	# real-world - orientation wrt. gravity
 			InvokeMacro="CodeSequenceMacro"								BaselineContextID="20"
		SequenceEnd
	SequenceEnd
	Sequence="PatientGantryRelationshipCodeSequence"		Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"									BaselineContextID="21"
	SequenceEnd
MacroEnd

DefineMacro="PerformedProcedureStepSummaryMacro" InformationEntity="Series"
	Name="PerformedProcedureStepID"							Type="3"
	Name="PerformedProcedureStepStartDate"					Type="3"
	Name="PerformedProcedureStepStartTime"					Type="3"
	Name="PerformedProcedureStepDescription"				Type="3"
	Sequence="PerformedProtocolCodeSequence"				Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
		Sequence="ProtocolContextSequence"					Type="3"	VM="1-n"
			InvokeMacro="ContentItemMacro"
			Sequence="ContentItemModifierSequence"			Type="3"	VM="1-n"
				InvokeMacro="ContentItemMacro"
			SequenceEnd
		SequenceEnd
	SequenceEnd
	Name="CommentsOnThePerformedProcedureStep"				Type="3"
MacroEnd

DefineMacro="ExposureIndexMacro" InformationEntity="Frame"
	Name="ExposureIndex"									Type="3"	NotZeroWarning=""
	Name="TargetExposureIndex"								Type="3"	NotZeroWarning=""
	Name="DeviationIndex"									Type="3"	NotZeroWarning=""
MacroEnd

DefineMacro="MandatoryViewAndSliceProgressionDirectionMacro" InformationEntity="Frame"
	Sequence="ViewCodeSequence"								Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"						BaselineContextID="26"
		Sequence="ViewModifierCodeSequence"					Type="2C"	VM="0-n"	NoCondition=""	# real-world - if needed to fully specify the view
			InvokeMacro="ContentItemMacro"					BaselineContextID="23"
		SequenceEnd
	SequenceEnd
	Name="SliceProgressionDirection"						Type="1C"	StringEnumValues="CardiacSliceProgressionDirection"	Condition="ViewIsCardiacShortOrLongAxis"	mbpo="true"
MacroEnd

DefineMacro="OptionalViewAndSliceProgressionDirectionMacro" InformationEntity="Frame"
	Sequence="ViewCodeSequence"								Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"						BaselineContextID="26"
		Sequence="ViewModifierCodeSequence"					Type="3"	VM="1-n"
			InvokeMacro="ContentItemMacro"					BaselineContextID="23"
		SequenceEnd
	SequenceEnd
	Name="SliceProgressionDirection"						Type="3"	StringEnumValues="CardiacSliceProgressionDirection"
MacroEnd

DefineMacro="RTEquipmentCorrelationMacro" InformationEntity="Image"
	Name="PatientSupportAngle"								Type="3"
	Name="TableTopPitchAngle"								Type="3"
	Name="TableTopRollAngle"								Type="3"
	Name="TableTopLongitudinalPosition"						Type="3"
	Name="TableTopLateralPosition"							Type="3"
MacroEnd

DefineMacro="PatientGroupMacro" InformationEntity="Patient"
	Sequence="SourcePatientGroupIdentificationSequence"		Type="3"	VM="1"
		Name="PatientID"									Type="1"
		InvokeMacro="IssuerOfPatientIDMacro"
	SequenceEnd
	Sequence="GroupOfPatientsIdentificationSequence"		Type="3"	VM="1-n"
		Name="PatientID"									Type="1"
		InvokeMacro="IssuerOfPatientIDMacro"
		Name="SubjectRelativePositionInImage"				Type="3"
		Name="PatientPosition"								Type="3"
	SequenceEnd
MacroEnd

DefineMacro="UDIMacro" InformationEntity="Equipment"
	Name="UniqueDeviceIdentifier"							Type="1"
	Name="DeviceDescription"								Type="3"
MacroEnd

Module="Patient"
	Name="PatientName"						Type="2"
	Name="PatientID"						Type="2"
	InvokeMacro="IssuerOfPatientIDMacro"
	Name="TypeOfPatientID"					Type="3"	StringDefinedTerms="TypeOfPatientID"
	Name="PatientBirthDate"					Type="2"
	Name="PatientBirthDateInAlternativeCalendar"	Type="3"
	Name="PatientDeathDateInAlternativeCalendar"	Type="3"
	Name="PatientAlternativeCalendar"				Type="1C"	Condition="PatientAlternativeCalendarNeeded"	StringDefinedTerms="PatientAlternativeCalendar"
	Name="PatientSex"						Type="2"	StringEnumValues="Sex"
	Sequence="ReferencedPatientPhotoSequence"	Type="3"	VM="1"
		InvokeMacro="ReferencedInstancesAndAccessMacro"
	SequenceEnd
	Name="QualityControlSubject"			Type="3"	StringEnumValues="YesNoFull"
	Sequence="ReferencedPatientSequence"	Type="3"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Name="PatientBirthTime"					Type="3"
	Sequence="OtherPatientIDsSequence"		Type="3"	VM="1-n"
		Name="PatientID"					Type="1"
		InvokeMacro="IssuerOfPatientIDMacro"
		Name="TypeOfPatientID"				Type="1"	StringDefinedTerms="TypeOfPatientID"
	SequenceEnd
	Name="OtherPatientNames"				Type="3"
	Name="EthnicGroup"						Type="3"
	Name="PatientComments"					Type="3"
	Name="PatientSpeciesDescription"		Type="1C"	Condition="IsAnimalAndPatientSpeciesCodeSequenceAbsent" mbpo="true"
	Sequence="PatientSpeciesCodeSequence"	Type="1C"	VM="1"	Condition="IsAnimalAndPatientSpeciesDescriptionAbsent" mbpo="true"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="PatientBreedDescription"			Type="2C"	Condition="IsAnimalAndPatientBreedCodeSequenceEmpty" mbpo="true"
	Sequence="PatientBreedCodeSequence"		Type="2C"	VM="0-1"	Condition="IsAnimal"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="BreedRegistrationSequence"	Type="2C"	VM="0-n"	Condition="IsAnimal"
		Name="BreedRegistrationNumber"		Type="1"
		Sequence="BreedRegistryCodeSequence"	Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="StrainDescription"						Type="3"
	Name="StrainNomenclature"						Type="3"
	Sequence="StrainCodeSequence"					Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="StrainAdditionalInformation"				Type="3"
	Sequence="StrainStockSequence"					Type="3"	VM="1"
		Name="StrainStockNumber"					Type="1"
		Name="StrainSource"							Type="1"
		Sequence="StrainSourceRegistryCodeSequence"	Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="GeneticModificationsSequence"				Type="3"	VM="1"
		Name="GeneticModificationsDescription"			Type="1"
		Name="GeneticModificationsNomenclature"			Type="1"
		Sequence="GeneticModificationsCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="ResponsiblePerson"				Type="2C"	Condition="IsAnimal" mbpo="true"
	Name="ResponsiblePersonRole"			Type="1C"	Condition="ResponsiblePersonIsPresentWithValue"	StringDefinedTerms="ResponsiblePersonRole"
	Name="ResponsibleOrganization"			Type="2C"	Condition="IsAnimal" mbpo="true"
	Name="PatientIdentityRemoved"			Type="3"	StringEnumValues="YesNoFull"
	Name="DeidentificationMethod"					Type="1C"	Condition="PatientIdentityRemovedAndNotDeidentificationMethodCodeSequence" mbpo="true"
	Sequence="DeidentificationMethodCodeSequence"	Type="1C"	VM="1-n"	Condition="PatientIdentityRemovedAndNotDeidentificationMethod" mbpo="true"
		InvokeMacro="CodeSequenceMacro"					DefinedContextID="7050"
	SequenceEnd
	InvokeMacro="PatientGroupMacro"
ModuleEnd

Module="ClinicalTrialSubject"
	Name="ClinicalTrialSponsorName"			Type="1"
	Name="ClinicalTrialProtocolID"			Type="1"
	Name="ClinicalTrialProtocolName"		Type="2"
	Name="ClinicalTrialSiteID"				Type="2"
	Name="ClinicalTrialSiteName"			Type="2"
	Name="ClinicalTrialSubjectID"			Type="1C"	Condition="ClinicalTrialSubjectReadingIDAbsent" mbpo="true"
	Name="ClinicalTrialSubjectReadingID"	Type="1C"	Condition="ClinicalTrialSubjectIDAbsent" mbpo="true"
	Name="ClinicalTrialProtocolEthicsCommitteeName"	Type="1C"	Condition="ClinicalTrialProtocolEthicsCommitteeApprovalNumberIsPresent"
	Name="ClinicalTrialProtocolEthicsCommitteeApprovalNumber"	Type="3"

ModuleEnd

Module="GeneralStudy"
	Name="StudyInstanceUID"									Type="1"
	Name="StudyDate"										Type="2"
	Name="StudyTime"										Type="2"
	Name="ReferringPhysicianName"							Type="2"
	Sequence="ReferringPhysicianIdentificationSequence"		Type="3"	VM="1"
		InvokeMacro="PersonIdentificationMacro"
	SequenceEnd
	Name="ConsultingPhysicianName"							Type="3"
	Sequence="ConsultingPhysicianIdentificationSequence"	Type="3"	VM="1-n"
		InvokeMacro="PersonIdentificationMacro"
	SequenceEnd
	Name="StudyID"											Type="2"
	Name="AccessionNumber"									Type="2"
	Sequence="IssuerOfAccessionNumberSequence"				Type="3"	VM="1"
		InvokeMacro="HL7v2HierarchicDesignatorMacro"
	SequenceEnd
	Name="StudyDescription"									Type="3"
	Name="PhysiciansOfRecord"								Type="3"
	Sequence="PhysiciansOfRecordIdentificationSequence"		Type="3"	VM="1-n"
		InvokeMacro="PersonIdentificationMacro"
	SequenceEnd
	Name="NameOfPhysiciansReadingStudy"						Type="3"
	Sequence="PhysiciansReadingStudyIdentificationSequence"	Type="3"	VM="1-n"
		InvokeMacro="PersonIdentificationMacro"
	SequenceEnd
	Sequence="RequestingServiceCodeSequence"				Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"						DefinedContextID="7030"
	SequenceEnd
	Sequence="ReferencedStudySequence"						Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ProcedureCodeSequence"						Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="ReasonForPerformedProcedureCodeSequence"		Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
ModuleEnd

Module="PatientStudy"
	Name="AdmittingDiagnosesDescription"		Type="3"
	Sequence="AdmittingDiagnosesCodeSequence"	Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="PatientAge"							Type="3"
	Name="PatientSize"							Type="3"	NotZeroWarning=""
	Name="PatientWeight"						Type="3"	NotZeroWarning=""
	Name="PatientBodyMassIndex"					Type="3"	NotZeroWarning=""
	Name="MeasuredAPDimension"					Type="3"	NotZeroWarning=""
	Name="MeasuredLateralDimension"				Type="3"	NotZeroWarning=""
	Sequence="PatientSizeCodeSequence"			Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="MedicalAlerts"						Type="3"
	Name="Allergies"							Type="3"
	Name="SmokingStatus"						Type="3"	StringEnumValues="SmokingStatus"
	Name="PregnancyStatus"						Type="3"	BinaryEnumValues="PregnancyStatus"
	Name="LastMenstrualDate"					Type="3"
	Name="PatientState"							Type="3"
	Name="Occupation"							Type="3"
	Name="AdditionalPatientHistory"				Type="3"
	Name="AdmissionID"							Type="3"
	Name="IssuerOfAdmissionID"					Type="3"
	Sequence="IssuerOfAdmissionIDSequence"		Type="3"	VM="1"
		InvokeMacro="HL7v2HierarchicDesignatorMacro"
	SequenceEnd
	Name="ServiceEpisodeID"						Type="3"
	Sequence="IssuerOfServiceEpisodeIDSequence"	Type="3"	VM="1"
		InvokeMacro="HL7v2HierarchicDesignatorMacro"
	SequenceEnd
	Name="ServiceEpisodeDescription"			Type="3"
	Name="PatientSexNeutered"					Type="2C"	Condition="IsAnimal"	StringEnumValues="PatientSexNeutered" mbpo="true"
ModuleEnd

Module="ClinicalTrialStudy"
	Name="ClinicalTrialTimePointID"					Type="2"
	Name="ClinicalTrialTimePointDescription"		Type="3"
	Name="LongitudinalTemporalOffsetFromEvent"		Type="3"
	Name="LongitudinalTemporalEventType"			Type="1C"	Condition="LongitudinalTemporalOffsetFromEventIsPresent"	StringDefinedTerms="LongitudinalTemporalEventType"
	Sequence="ConsentForClinicalTrialUseSequence"	Type="3"	VM="1-n"
		Name="DistributionType"						Type="1C"	Condition="ConsentForDistributionFlagIsYesOrWithdrawn"	StringEnumValues="DistributionType"
		Name="ClinicalTrialProtocolID"				Type="1C"	NoCondition=""
		Verify="ClinicalTrialProtocolID"						Condition="DistributionTypeIsNotNamedProtocol"		ThenErrorMessage="Only permitted when DistributionType is NAMED_PROTOCOL"
		Name="ConsentForDistributionFlag"			Type="1"	StringEnumValues="ConsentForDistributionFlag"
	SequenceEnd
ModuleEnd

Module="GeneralSeries"
	Name="Modality"											Type="1C"	Condition="NotSecondaryCaptureSOPClass" mbpo="true"
	Verify="Modality"													StringDefinedTerms="Modality"
	Name="SeriesInstanceUID"								Type="1"
	Name="SeriesNumber"										Type="2"
	Name="Laterality"										Type="2C"	Condition="LateralityRequired"	StringEnumValues="Laterality"
	Verify="Laterality"													Condition="LateralityHasNoValue"	ThenWarningMessage="is only permitted to be empty when actually unknown; should be absent (not empty) if an unpaired body part, and have a value if a paired body part"
	Name="SeriesDate"										Type="3"
	Name="SeriesTime"										Type="3"
	Name="PerformingPhysicianName"							Type="3"
	Sequence="PerformingPhysicianIdentificationSequence"	Type="3"	VM="1-n"
		InvokeMacro="PersonIdentificationMacro"
	SequenceEnd
	Name="ProtocolName"										Type="3"
	Sequence="ReferencedDefinedProtocolSequence"			Type="1C"	VM="1-n"	NoCondition="" mbpo="true"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedPerformedProtocolSequence"			Type="1C"	VM="1-n"	NoCondition="" mbpo="true"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Name="SeriesDescription"								Type="3"
	Sequence="SeriesDescriptionCodeSequence"				Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="OperatorsName"									Type="3"
	Sequence="OperatorIdentificationSequence"				Type="3"	VM="1-n"
		InvokeMacro="PersonIdentificationMacro"
	SequenceEnd
	Sequence="ReferencedPerformedProcedureStepSequence"		Type="3"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="RelatedSeriesSequence"						Type="3"	VM="1-n"
		Name="StudyInstanceUID"								Type="1"
		Name="SeriesInstanceUID"							Type="1"
		Sequence="PurposeOfReferenceCodeSequence"			Type="2"	VM="0-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="BodyPartExamined"									Type="3"
	Verify="BodyPartExamined"											Condition="IsHuman"		StringDefinedTerms="BodyPartExaminedHuman"
	Verify="BodyPartExamined"											Condition="IsAnimal"	StringDefinedTerms="BodyPartExaminedAnimal"
	Name="PatientPosition"									Type="2C"	StringDefinedTerms="PatientPosition"	Condition="SOPClassIsCTOrMR" mbpo="true"
	Verify="PatientPosition"											Condition="PatientPositionAndPatientOrientationCodeSequencePresent"	ThenErrorMessage="May not be present when PatientOrientationCodeSequence is present"
	Name="SmallestPixelValueInSeries"						Type="3"
	Name="LargestPixelValueInSeries"						Type="3"
	Sequence="RequestAttributesSequence"					Type="3"	VM="1-n"
		InvokeMacro="RequestAttributesMacro"
	SequenceEnd
	InvokeMacro="PerformedProcedureStepSummaryMacro"
	Name="AnatomicalOrientationType"						Type="1C"	NoCondition=""	StringEnumValues="AnatomicalOrientationType"
ModuleEnd

Module="ClinicalTrialSeries"
	Name="ClinicalTrialCoordinatingCenterName"				Type="2"
	Name="ClinicalTrialSeriesID"							Type="3"
	Name="ClinicalTrialSeriesDescription"					Type="3"
ModuleEnd

Module="EnhancedSeries"
	Name="SeriesNumber"										Type="1"
	Sequence="ReferencedPerformedProcedureStepSequence"		Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="FrameOfReference"
	Name="FrameOfReferenceUID"								Type="1"
	Name="PositionReferenceIndicator"						Type="2"
ModuleEnd

Module="GeneralEquipment"
	Name="Manufacturer"										Type="2"
	Name="InstitutionName"									Type="3"
	Name="InstitutionAddress"								Type="3"
	Name="StationName"										Type="3"
	Name="InstitutionalDepartmentName"						Type="3"
	Sequence="InstitutionalDepartmentTypeCodeSequence"		Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"									BaselineContextID="7030"
	SequenceEnd
	Name="ManufacturerModelName"							Type="3"
	Name="ManufacturerDeviceClassUID"						Type="3"
	Name="DeviceSerialNumber"								Type="3"
	Name="SoftwareVersions"									Type="3"
	Name="GantryID"											Type="3"
	Sequence="UDISequence"									Type="3"	VM="1-n"
		InvokeMacro="UDIMacro"
	SequenceEnd
	Name="DeviceUID"										Type="3"
	Name="SpatialResolution"								Type="3"
	Name="DateOfLastCalibration"							Type="3"
	Name="TimeOfLastCalibration"							Type="3"
	Name="PixelPaddingValue"								Type="1C"	Condition="PixelPaddingRangeLimitIsPresent" mbpo="true"
	Verify="PixelPaddingValue"											Condition="PixelPaddingValueIsPresentAndInstanceIsNotAnImage"	ThenErrorMessage="May not be present when not an integer pixel data image"
ModuleEnd

Module="EnhancedGeneralEquipment"
	Name="Manufacturer"										Type="1"
	Name="ManufacturerModelName"							Type="1"
	Name="DeviceSerialNumber"								Type="1"
	Name="SoftwareVersions"									Type="1"
ModuleEnd

Module="GeneralReference"
	Sequence="ReferencedImageSequence"						Type="3"	VM="1-n"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="ReferencedInstanceSequence"					Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"			Type="1"	VM="1"
 			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="DerivationDescription"							Type="3"
	Sequence="DerivationCodeSequence"						Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="SourceImageSequence"							Type="3"	VM="1-n"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="SpatialLocationsPreserved"					Type="3"	StringEnumValues="YesNoReorientedOnly"
		Name="PatientOrientation"							Type="1C"	Condition="SpatialLocationsPreservedReorientedOnly"
	SequenceEnd
	Sequence="SourceInstanceSequence"						Type="3"	VM="1-n"	NoCondition=""
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="GeneralImage"
	Name="InstanceNumber"									Type="2"
	Name="PatientOrientation"								Type="2C"	Condition="PatientOrientationRequired" mbpo="true"
	# ImageDate and ImageTime real-world condition "images are temporally related"
	Name="ContentDate"										Type="2C"	NoCondition=""	# "if temporally related" ... real world
	Name="ContentTime"										Type="2C"	NoCondition=""	# "if temporally related" ... real world
	Name="ImageType"										Type="3"	ValueSelector="0"	StringEnumValues="ImageType1"
	Verify="ImageType"										Type="3"	ValueSelector="1"	StringEnumValues="ImageType2"
	Name="AcquisitionNumber"								Type="3"
	Name="AcquisitionDate"									Type="3"
	Name="AcquisitionTime"									Type="3"
	Name="AcquisitionDateTime"								Type="3"
	Name="ImagesInAcquisition"								Type="3"
	Name="ImageComments"									Type="3"
	Name="QualityControlImage"								Type="3"	StringEnumValues="YesNoFull"
	Name="BurnedInAnnotation"								Type="3"	StringEnumValues="YesNoFull"
	Name="RecognizableVisualFeatures"						Type="3"	StringEnumValues="YesNoFull"
	Name="LossyImageCompression"							Type="3"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"						Type="3"
	Name="LossyImageCompressionMethod"						Type="3"	StringDefinedTerms="LossyImageCompressionMethod"
	Verify="LossyImageCompressionMethod"								Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Sequence="IconImageSequence"							Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
	Name="PresentationLUTShape"								Type="3"	StringEnumValues="SoftcopyPresentationLUTShape"
	Verify="PresentationLUTShape"							Condition="PhotometricInterpretationIsMonochrome1"			StringEnumValues="InversePresentationLUTShape"
	Verify="PresentationLUTShape"							Condition="PhotometricInterpretationIsMonochrome2"			StringEnumValues="IdentityPresentationLUTShape"
	Verify="PresentationLUTShape"							Condition="PhotometricInterpretationIsColor"				StringEnumValues="IdentityPresentationLUTShape"
	Name="IrradiationEventUID"								Type="3"
	# multienergy condition for RWVM is from IOD not module
	Sequence="RealWorldValueMappingSequence"				Type="1C"	VM="1-n"	Condition="IsMultienergyCTAcquisition"	mbpo="true"
		InvokeMacro="RealWorldValueMappingItemMacro"
	SequenceEnd
	Name="ImageLaterality"									Type="3"	StringEnumValues="ImageLaterality"
	Sequence="AnatomicRegionSequence"						Type="2C"	VM="0-1"	Condition="NeedAnatomicRegionSequenceInGeneralImageModule"	mbpo="true"
		InvokeMacro="CodeSequenceMacro"
		Sequence="AnatomicRegionModifierSequence"			Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"	BaselineContextID="2"
		SequenceEnd
	SequenceEnd
	InvokeMacro="PrimaryAnatomicStructureMacro"
	Sequence="AnatomicRegionModifierSequence"				Type="1C"	VM="1-n"	Condition="Never"
	SequenceEnd
	Sequence="PrimaryAnatomicStructureModifierSequence"		Type="1C"	VM="1-n"	Condition="Never"
	SequenceEnd
ModuleEnd

Module="ImagePlane"
	Name="PixelSpacing"										Type="1"	NotZeroError=""
	Name="ImageOrientationPatient"							Type="1"
	Name="ImagePositionPatient"								Type="1"
	Name="SliceThickness"									Type="2"	NotZeroError=""
	Name="SliceLocation"									Type="3"
ModuleEnd

DefineMacro="ImagePixelMacro" InformationEntity="Instance"
	Name="SamplesPerPixel"							Type="1"
	Verify="SamplesPerPixel"						Condition="PhotometricInterpretationNeedsOneSample"	BinaryEnumValues="One"
	Verify="SamplesPerPixel"						Condition="PhotometricInterpretationNeedsThreeSamples"	BinaryEnumValues="Three"
	Verify="SamplesPerPixel"						Condition="MPEG2TransferSyntaxAndNotThreeSamples"		ThenErrorMessage="May only be 3 for MPEG Transfer Syntax"
	
	Name="PhotometricInterpretation"				Type="1"	StringDefinedTerms="PhotometricInterpretation"
	#PS3.5 constraints only - others checked with IOD-specific modules
	Verify="PhotometricInterpretation"				Condition="JPEGLossyTransferSyntaxAndOneSample"							StringEnumValues="PhotometricInterpretationMonochrome"
	Verify="PhotometricInterpretation"				Condition="JPEGLossyTransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRFull422OrRGB"

	Verify="PhotometricInterpretation"				Condition="JPEGLosslessTransferSyntaxAndOneSample"						StringEnumValues="PhotometricInterpretationMonochromeOrPaletteColor"
	Verify="PhotometricInterpretation"				Condition="JPEGLosslessTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationYBRFullOrRGB"

	Verify="PhotometricInterpretation"				Condition="JPEGLSLosslessTransferSyntaxAndOneSample"					StringEnumValues="PhotometricInterpretationMonochromeOrPaletteColor"
	Verify="PhotometricInterpretation"				Condition="JPEGLSLosslessTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationYBRFullOrRGB"

	Verify="PhotometricInterpretation"				Condition="JPEGLSNearLosslessTransferSyntaxAndOneSample"				StringEnumValues="PhotometricInterpretationMonochrome"
	Verify="PhotometricInterpretation"				Condition="JPEGLSNearLosslessTransferSyntaxAndThreeSamples"				StringEnumValues="PhotometricInterpretationYBRFullOrRGB"

	Verify="PhotometricInterpretation"				Condition="JPEG2000LosslessTransferSyntaxAndOneSample"					StringEnumValues="PhotometricInterpretationMonochromeOrPaletteColor"
	Verify="PhotometricInterpretation"				Condition="JPEG2000LosslessTransferSyntaxAndThreeSamples"				StringEnumValues="PhotometricInterpretationYBRFullOrRGBOrYBR_RCT"

	Verify="PhotometricInterpretation"				Condition="JPEG2000TransferSyntaxAndOneSample"							StringEnumValues="PhotometricInterpretationMonochrome"
	Verify="PhotometricInterpretation"				Condition="JPEG2000TransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRFullOrRGBOrYBR_RCTOrYBR_ICT"

	Verify="PhotometricInterpretation"				Condition="MPEG2TransferSyntax"											StringEnumValues="PhotometricInterpretationYBRPartial420"	# regardless of number of samples (required to be 3 by PS 3.5)

	Verify="PhotometricInterpretation"				Condition="RLETransferSyntaxAndOneSample"								StringEnumValues="PhotometricInterpretationMonochromeOrPaletteColor"
	Verify="PhotometricInterpretation"				Condition="RLETransferSyntaxAndThreeSamples"							StringEnumValues="PhotometricInterpretationYBRFullOrRGB"

	Verify="PhotometricInterpretation"				Condition="UncompressedTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationYBRFullOrRGBOrYBR_RCTOrYBR_ICT"
	
	Name="Rows"										Type="1"	NotZeroError=""
	Verify="Rows"									Condition="MPEG2MPMLTransferSyntaxAndRowsGreaterThan480NTSCOr576PAL"	ThenErrorMessage="Must be <= 480 (NTSC) or 576 (PAL) for MPEG MP@MLTransfer Syntax"
	Verify="Rows"									Condition="MPEG2MPHLTransferSyntaxAndRowsNot720Or1080"					ThenErrorMessage="Must be 720 or 1080 for MPEG MP@HLTransfer Syntax"
	
	Name="Columns"									Type="1"	NotZeroError=""
	Verify="Columns"								Condition="MPEG2MPMLTransferSyntaxAndColumnsGreaterThan720"				ThenErrorMessage="Must be <= 720 for MPEG MP@MLTransfer Syntax"
	Verify="Columns"								Condition="MPEG2MPHLTransferSyntaxAndColumnsNot1280Or1920"				ThenErrorMessage="Must be 1280 or 1920 for MPEG MP@HLTransfer Syntax"
	Verify="Columns"								Condition="MPEG2MPHLTransferSyntaxAndColumnsInconsistentWithRows"		ThenErrorMessage="Must be 1280 when 720 Rows, or 1920 when 1080 Rows, for MPEG MP@HLTransfer Syntax"
	
	Name="BitsAllocated"							Type="1"	NotZeroError=""
	Verify="BitsAllocated"							Condition="MPEG2TransferSyntaxAndNotBitsAllocated8"		ThenErrorMessage="May only be 8 for MPEG Transfer Syntax"
	
	Name="BitsStored"								Type="1"	NotZeroError=""
	Verify="BitsStored"								Condition="MPEG2TransferSyntaxAndNotBitsStored8"		ThenErrorMessage="May only be 8 for MPEG Transfer Syntax"
	
	Name="HighBit"									Type="1"
	Verify="HighBit"								Condition="MPEG2TransferSyntaxAndNotHighBit7"		ThenErrorMessage="May only be 7 for MPEG Transfer Syntax"
	
	Name="PixelRepresentation"						Type="1"	BinaryEnumValues="PixelRepresentation"
	Verify="PixelRepresentation"					Condition="MPEG2TransferSyntaxAndNotPixelRepresentation0"		ThenErrorMessage="May only be 0 for MPEG Transfer Syntax"
	
	Name="PixelData"								Type="1C"	Condition="PixelDataProviderURLIsAbsent"

	Name="PlanarConfiguration"						Type="1C"	BinaryEnumValues="PlanarConfiguration"	Condition="SamplesPerPixelGreaterThanOne"
	Verify="PlanarConfiguration"					Condition="MPEG2TransferSyntaxAndNotPlanarConfiguration0"		ThenErrorMessage="May only be 0 for MPEG Transfer Syntax"
	
	# PixelAspectRatio required if the image plane module not applicable and the aspect ratio is not 1:1
	Name="PixelAspectRatio"							Type="1C"	NoCondition=""	# "if ! image plane module present && not 1:1" ... too hard for now :(
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenPixelSpacingPresent"					ThenErrorMessage="May not be present when Pixel Spacing is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenImagerPixelSpacingPresent"			ThenErrorMessage="May not be present when Imager Pixel Spacing is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenNominalScannedPixelSpacingPresent"	ThenErrorMessage="May not be present when Nominal Scanned Pixel Spacing is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenSharedPixelMeasuresMacro"			ThenErrorMessage="May not be present when Pixel Measures Macro is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenPerFramePixelMeasuresMacro"			ThenErrorMessage="May not be present when Pixel Measures Macro is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenMPEG2MPHLTransferSyntax"				ThenErrorMessage="May not be present for MPEG MP@HLTransfer Syntax"
	Name="SmallestImagePixelValue"					Type="3"
	Name="LargestImagePixelValue"					Type="3"
	Name="RedPaletteColorLookupTableDescriptor"	Type="1C"	Condition="ImagePixelMacroNeedsPaletteDescriptor"
	Verify="RedPaletteColorLookupTableDescriptor"			ValueSelector="2"	BinaryEnumValues="BitsAre8Or16"
	Name="GreenPaletteColorLookupTableDescriptor"	Type="1C"	Condition="ImagePixelMacroNeedsPaletteDescriptor"
	Verify="GreenPaletteColorLookupTableDescriptor"			ValueSelector="2"	BinaryEnumValues="BitsAre8Or16"
	Name="BluePaletteColorLookupTableDescriptor"	Type="1C"	Condition="ImagePixelMacroNeedsPaletteDescriptor"
	Verify="BluePaletteColorLookupTableDescriptor"			ValueSelector="2"	BinaryEnumValues="BitsAre8Or16"
	Name="RedPaletteColorLookupTableData"			Type="1C"	Condition="ImagePixelMacroNeedsPaletteDescriptorAndNotSegmentedLegallyPresentInPaletteColorModule"
	Name="GreenPaletteColorLookupTableData"			Type="1C"	Condition="ImagePixelMacroNeedsPaletteDescriptorAndNotSegmentedLegallyPresentInPaletteColorModule"
	Name="BluePaletteColorLookupTableData"			Type="1C"	Condition="ImagePixelMacroNeedsPaletteDescriptorAndNotSegmentedLegallyPresentInPaletteColorModule"
	Name="ICCProfile"								Type="3"
	Name="ColorSpace"								Type="3"
MacroEnd

Module="FloatingPointImagePixel"
	Name="SamplesPerPixel"							Type="1"	BinaryEnumValues="One"
	Name="PhotometricInterpretation"				Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="Rows"										Type="1"	NotZeroError=""
	Name="Columns"									Type="1"	NotZeroError=""
	Name="BitsAllocated"							Type="1"	BinaryEnumValues="BitsAre32"
	Verify="BitsStored"								Condition="BitsStoredPresent"			ThenErrorMessage="May not be present for Float Pixel Data"
	Verify="HighBit"								Condition="HighBitPresent"				ThenErrorMessage="May not be present for Float Pixel Data"
	Verify="PixelRepresentation"					Condition="PixelRepresentationPresent"	ThenErrorMessage="May not be present for Float Pixel Data"
	Verify="PlanarConfiguration"					Condition="PlanarConfigurationPresent"	ThenErrorMessage="May not be present for Float Pixel Data"

	Name="FloatPixelData"							Type="1"

	# PixelAspectRatio required if the image plane module not applicable and the aspect ratio is not 1:1
	Name="PixelAspectRatio"							Type="1C"	NoCondition=""	# "if ! image plane module present && not 1:1" ... too hard for now :(
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenPixelSpacingPresent"					ThenErrorMessage="May not be present when Pixel Spacing is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenImagerPixelSpacingPresent"			ThenErrorMessage="May not be present when Imager Pixel Spacing is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenNominalScannedPixelSpacingPresent"	ThenErrorMessage="May not be present when Nominal Scanned Pixel Spacing is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenSharedPixelMeasuresMacro"			ThenErrorMessage="May not be present when Pixel Measures Macro is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenPerFramePixelMeasuresMacro"			ThenErrorMessage="May not be present when Pixel Measures Macro is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenMPEG2MPHLTransferSyntax"				ThenErrorMessage="May not be present for MPEG MP@HLTransfer Syntax"

	Name="FloatPixelPaddingValue"					Type="3"
	Name="FloatPixelPaddingRangeLimit"				Type="1C"	Condition="FloatPixelPaddingValuePresent"
ModuleEnd

Module="DoubleFloatingPointImagePixel"
	Name="SamplesPerPixel"							Type="1"	BinaryEnumValues="One"
	Name="PhotometricInterpretation"				Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="Rows"										Type="1"	NotZeroError=""
	Name="Columns"									Type="1"	NotZeroError=""
	Name="BitsAllocated"							Type="1"	BinaryEnumValues="BitsAre64"
	Verify="BitsStored"								Condition="BitsStoredPresent"			ThenErrorMessage="May not be present for Float Pixel Data"
	Verify="HighBit"								Condition="HighBitPresent"				ThenErrorMessage="May not be present for Float Pixel Data"
	Verify="PixelRepresentation"					Condition="PixelRepresentationPresent"	ThenErrorMessage="May not be present for Float Pixel Data"
	Verify="PlanarConfiguration"					Condition="PlanarConfigurationPresent"	ThenErrorMessage="May not be present for Float Pixel Data"

	Name="DoubleFloatPixelData"						Type="1"

	# PixelAspectRatio required if the image plane module not applicable and the aspect ratio is not 1:1
	Name="PixelAspectRatio"							Type="1C"	NoCondition=""	# "if ! image plane module present && not 1:1" ... too hard for now :(
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenPixelSpacingPresent"					ThenErrorMessage="May not be present when Pixel Spacing is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenImagerPixelSpacingPresent"			ThenErrorMessage="May not be present when Imager Pixel Spacing is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenNominalScannedPixelSpacingPresent"	ThenErrorMessage="May not be present when Nominal Scanned Pixel Spacing is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenSharedPixelMeasuresMacro"			ThenErrorMessage="May not be present when Pixel Measures Macro is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenPerFramePixelMeasuresMacro"			ThenErrorMessage="May not be present when Pixel Measures Macro is present"
	Verify="PixelAspectRatio"									Condition="UnwantedPixelAspectRatioWhenMPEG2MPHLTransferSyntax"				ThenErrorMessage="May not be present for MPEG MP@HLTransfer Syntax"

	Name="DoubleFloatPixelPaddingValue"				Type="3"
	Name="DoubleFloatPixelPaddingRangeLimit"		Type="1C"	Condition="DoubleFloatPixelPaddingValuePresent"
ModuleEnd

Module="ImagePixel"
	InvokeMacro="ImagePixelMacro"
	Name="PixelDataProviderURL"								Type="1C"	Condition="TransferSyntaxIsReferencedPixelData"
	Name="PixelPaddingRangeLimit"							Type="1C"	NoCondition=""		# real world
ModuleEnd

Module="ContrastBolus"
	Name="ContrastBolusAgent"							Type="2"
	Sequence="ContrastBolusAgentSequence"				Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="ContrastBolusRoute"							Type="3"
	Sequence="ContrastBolusAdministrationRouteSequence"	Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
		Sequence="AdditionalDrugSequence"				Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="ContrastBolusVolume"							Type="3"
	Name="ContrastBolusStartTime"						Type="3"
	Name="ContrastBolusStopTime"						Type="3"
	Name="ContrastBolusTotalDose"						Type="3"
	Name="ContrastFlowRate"								Type="3"
	Name="ContrastFlowDuration"							Type="3"
	Name="ContrastBolusIngredient"						Type="3"
	Name="ContrastBolusIngredientConcentration"			Type="3"
ModuleEnd

Module="EnhancedContrastBolus"
	Sequence="ContrastBolusAgentSequence"					Type="1"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
		Name="ContrastBolusAgentNumber"						Type="1"
		Sequence="ContrastBolusAdministrationRouteSequence"	Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="ContrastBolusIngredientCodeSequence"		Type="2"	VM="0-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="ContrastBolusVolume"							Type="2"
		Name="ContrastBolusIngredientConcentration"			Type="2"
		Name="ContrastBolusIngredientPercentByVolume"		Type="3"
		Name="ContrastBolusIngredientOpaque"				Type="3"	StringEnumValues="YesNoFull"
		Sequence="ContrastAdministrationProfileSequence"	Type="3"	VM="1-n"
			Name="ContrastBolusVolume"						Type="2"
			Name="ContrastBolusStartTime"					Type="3"
			Name="ContrastBolusStopTime"					Type="3"
			Name="ContrastFlowRate"							Type="3"
			Name="ContrastFlowDuration"						Type="3"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="Cine"
	Name="PreferredPlaybackSequencing"		Type="3"	BinaryEnumValues="PreferredPlaybackSequencing"
	
	Name="FrameTime"						Type="1C"	Condition="FrameIncrementPointerContainsFrameTime"
	Verify="FrameTime"						Condition="MPEG2MPMLTransferSyntaxAndFrameTimeNotNTSCOrPAL"	ThenErrorMessage="Must be 33.3 (NTSC) or 40 (PAL) for MPEG MP@MLTransfer Syntax"
	Verify="FrameTime"						Condition="MPEG2MPHLTransferSyntaxAndFrameTimeNotValid"	ThenErrorMessage="Must be 16.17, 20, 33.33, or 40 (PAL) for MPEG MP@HLTransfer Syntax"
	
	Name="FrameTimeVector"					Type="1C"	Condition="FrameIncrementPointerContainsFrameTimeVector"
	Name="StartTrim"						Type="3"
	Name="StopTrim"							Type="3"
	Name="RecommendedDisplayFrameRate"		Type="3"
	
	Name="CineRate"							Type="3"
	Verify="CineRate"						Condition="MPEG2MPMLTransferSyntaxAndCineRateNotNTSCOrPAL"	ThenErrorMessage="Must be 30 (NTSC) or 25 (PAL) for MPEG MP@MLTransfer Syntax"
	Verify="CineRate"						Condition="MPEG2MPHLTransferSyntaxAndCineRateNotValid"	ThenErrorMessage="Must be 25, 30, 50 or 60 for MPEG MP@HLTransfer Syntax"
	Verify="CineRate"						Condition="MPEG2MPMLTransferSyntaxAndCineRateInconsistentWithFrameTime"	ThenErrorMessage="Must be 30 when FrameTime is 33.3 (NTSC) or 25 when FrameTime is 40 (PAL) for MPEG MP@MLTransfer Syntax"
	Verify="CineRate"						Condition="MPEG2MPHLTransferSyntaxAndCineRateInconsistentWithFrameTime"	ThenErrorMessage="Must be 30 when FrameTime is 33.3, 25 when FrameTime is 40, 60 when FrameTime is 16.17, or 50 when FrameTime is 20 for MPEG MP@HLTransfer Syntax"
	
	Name="FrameDelay"						Type="3"
	Name="ImageTriggerDelay"				Type="3"
	Name="EffectiveDuration"				Type="3"
	Name="ActualFrameDuration"				Type="3"
	Sequence="MultiplexedAudioChannelsDescriptionCodeSequence"	Type="3"	VM="1-n"
		Name="ChannelIdentificationCode"	Type="1"
		Name="ChannelMode"					Type="1"
		Sequence="ChannelSourceSequence"	Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="MultiFrame"
	Name="NumberOfFrames"					Type="1"	NotZeroError=""
	Name="FrameIncrementPointer"			Type="1C"	Condition="NotSCMultiFrameOrNumberOfFramesGreaterThanOne"
	Name="StereoPairsPresent"				Type="3"	StringEnumValues="YesNoFull"
ModuleEnd

Module="MultiFrameFunctionalGroupsCommon"
	# the Type 2 Shared Functional Groups Sequence and Type 1 Per-frame Functional Groups Sequence are included in the IOD-specific pseudo-modules
	Name="InstanceNumber"						Type="1"
	Name="ContentDate"							Type="1"
	Name="ContentTime"							Type="1"
	Name="NumberOfFrames"						Type="1"	NotZeroError=""
	Name="StereoPairsPresent"					Type="3"	StringEnumValues="YesNoFull"
	Name="ConcatenationFrameOffsetNumber"		Type="1C"	Condition="ConcatenationUIDIsPresent"
	Name="RepresentativeFrameNumber"			Type="3"	NotZeroError=""
	Name="ConcatenationUID"						Type="1C"	Condition="ConcatenationAttributesArePresentAndTotalNumberIfPresentGreaterThanOne"
	Name="SOPInstanceUIDOfConcatenationSource"	Type="1C"	Condition="ConcatenationUIDIsPresent"
	Name="InConcatenationNumber"				Type="1C"	Condition="ConcatenationUIDIsPresent"
	Name="InConcatenationTotalNumber"			Type="3"
	Verify="InConcatenationTotalNumber"						Condition="InConcatenationTotalNumberIsLessThanOrEqualToOne"	ThenErrorMessage="Cannot be less than or equal to one since then not a Concatenation"
ModuleEnd

DefineMacro="PixelMeasuresMacro" InformationEntity="FunctionalGroup"
	Sequence="PixelMeasuresSequence"		Type="1"	VM="1"
		Name="PixelSpacing"					Type="1C"	NotZeroError=""	Condition="PixelSpacingRequiredInPixelMeasures" mbpo="true"
		Name="SliceThickness"				Type="1C"	NotZeroError=""	Condition="SliceThicknessRequiredInPixelMeasures" mbpo="true"
		Name="SpacingBetweenSlices"			Type="1C"	NotZeroError="" Condition="DimensionOrganizationTypeIsTILED_FULLAndTotalPixelMatrixFocalPlanesGreaterThanOne" mbpo="true"
	SequenceEnd
MacroEnd

DefineMacro="FrameContentMacro" InformationEntity="FunctionalGroup"
	Sequence="FrameContentSequence"				Type="1"	VM="1"
		Name="FrameAcquisitionNumber"			Type="3"
		Name="FrameReferenceDateTime"			Type="1C"	Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedOrWholeSlide" mbpo="true" # approximates (../../[SharedFunctionalGroupsSequence or PerFrameFunctionalGroupsSequence item for this frame]MRImageFrameTypeMacro/FrameType is ORIGINAL) and not legacy CT, MR or PET or WSI ... too hard :(
		Name="FrameAcquisitionDateTime"			Type="1C"	Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedOrWholeSlide" mbpo="true" # approximates (../../[SharedFunctionalGroupsSequence or PerFrameFunctionalGroupsSequence item for this frame]MRImageFrameTypeMacro/FrameType is ORIGINAL) and not legacy CT, MR or PET or WSI ... too hard :(
		Name="FrameAcquisitionDuration"			Type="1C"	Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedOrWholeSlide" mbpo="true" NotZeroWarning=""	# approximates (../../[SharedFunctionalGroupsSequence or PerFrameFunctionalGroupsSequence item for this frame]MRImageFrameTypeMacro/FrameType is ORIGINAL) and not legacy CT, MR or PET or WSI ... too hard :(
		Name="CardiacCyclePosition"				Type="3"	StringDefinedTerms="CardiacCyclePosition"
		Name="RespiratoryCyclePosition"			Type="3"	StringDefinedTerms="RespiratoryCyclePosition"
		Name="DimensionIndexValues"				Type="1C"	Condition="DimensionIndexSequencePresent"
		Verify="DimensionIndexValues"						Condition="DimensionIndexValuesContainsZero"	ThenErrorMessage="Must start from one, not zero"
		Name="TemporalPositionIndex"			Type="1C"	Condition="EnhancedPETImageInstance" mbpo="true"
		Verify="TemporalPositionIndex"						Condition="TemporalPositionIndexIsZero"	ThenErrorMessage="Must start from one, not zero"
		Name="StackID"							Type="1C"	Condition="EnhancedPETImageInstance" mbpo="true"
		Name="InStackPositionNumber"			Type="1C"	Condition="StackIDIsPresent"
		Verify="InStackPositionNumber"						Condition="InStackPositionNumberIsZero"	ThenErrorMessage="Must start from one, not zero"
		Name="FrameComments"					Type="3"
		Name="FrameLabel"						Type="3"
	SequenceEnd
MacroEnd

DefineMacro="PlanePositionMacro" InformationEntity="FunctionalGroup"
	Sequence="PlanePositionSequence"			Type="1"	VM="1"
		Name="ImagePositionPatient"				Type="1C"	Condition="ImagePositionPatientNotPresentInEitherSharedOrPerFrameFunctionalGroupsAndEitherFrameTypeIsOriginalAndVolumetricPropertiesIsNotDistortedOrSegmentationWithFrameOfReference" mbpo="true"
	SequenceEnd
MacroEnd

DefineMacro="PlaneOrientationMacro" InformationEntity="FunctionalGroup"
	Sequence="PlaneOrientationSequence"			Type="1"	VM="1"
		Name="ImageOrientationPatient"			Type="1C"		Condition="ImageOrientationPatientNotPresentInEitherSharedOrPerFrameFunctionalGroupsAndEitherFrameTypeIsOriginalAndVolumetricPropertiesIsNotDistortedOrSegmentationWithFrameOfReference" mbpo="true"
	SequenceEnd
MacroEnd

DefineMacro="ReferencedImageMacro" InformationEntity="FunctionalGroup"
	Sequence="ReferencedImageSequence"				Type="2"	VM="0-n"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"	Type="1C"	VM="1"	Condition="NotLegacyConvertedCTOrMROrPET" mbpo="true"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="DerivationImageMacro" InformationEntity="FunctionalGroup"
	Sequence="DerivationImageSequence"					Type="2"	VM="0-n"
		Name="DerivationDescription"					Type="3" 
		Sequence="DerivationCodeSequence"				Type="1C"	VM="1-n"	Condition="NotLegacyConvertedCTOrMROrPET" mbpo="true"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="SourceImageSequence"					Type="2"	VM="0-n"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
			Sequence="PurposeOfReferenceCodeSequence"	Type="1C"	VM="1"	Condition="NotLegacyConvertedCTOrMROrPET" mbpo="true"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="CardiacSynchronizationMacro" InformationEntity="FunctionalGroup"
	Sequence="CardiacSynchronizationSequence"	Type="1"	VM="1"
		Name="NominalPercentageOfCardiacPhase"	Type="1C"  	NoCondition="" mbpo="true"	# too hard
		Name="NominalCardiacTriggerDelayTime"	Type="1"
		Name="ActualCardiacTriggerDelayTime"	Type="1C"	Condition="SingleCardiacIntervalAcquired" mbpo="true"
		Name="IntervalsAcquired"				Type="3"
		Name="IntervalsRejected"				Type="3"
		Name="HeartRate"						Type="3"
		Name="RRIntervalTimeNominal"			Type="1C"	Condition="CardiacSynchronizationTechniqueOtherThanNoneOrRealTime" mbpo="true"
		Name="LowRRValue"						Type="3"
		Name="HighRRValue"						Type="3"
	SequenceEnd
MacroEnd

DefineMacro="FrameAnatomyMacro" InformationEntity="FunctionalGroup"
	Sequence="FrameAnatomySequence"						Type="1"	VM="1"
		Name="FrameLaterality"							Type="1"	StringEnumValues="ImageLaterality"
		InvokeMacro="GeneralAnatomyMandatoryMacro"
	SequenceEnd
MacroEnd

DefineMacro="PixelValueTransformationMacro" InformationEntity="FunctionalGroup"
	Sequence="PixelValueTransformationSequence"		Type="1"	VM="1"
		Name="RescaleIntercept"						Type="1" 
		Name="RescaleSlope"							Type="1"	NotZeroError=""
		Name="RescaleType"							Type="1"
		Verify="RescaleType"						Type="1C"	StringDefinedTerms="RescaleTypeUnspecified"	Condition="ModalityIsMROrPET"
	SequenceEnd
MacroEnd

DefineMacro="FrameVOILUTMacro" InformationEntity="FunctionalGroup"
	Sequence="FrameVOILUTSequence"				Type="1"	VM="1"
		Name="WindowCenter"						Type="1"
		Name="WindowWidth"						Type="1"	NotZeroError=""
		Verify="WindowWidth"								Condition="WindowWidthIsNegative"	ThenErrorMessage="Not permitted to be negative" ShowValueWithMessage="true"
		Name="WindowCenterWidthExplanation"		Type="3"
		Verify="WindowCenterWidthExplanation"	Type="1C"	StringDefinedTerms="EnhancedCTWindowCenterWidthExplanation"	Condition="ModalityIsCT"
		Name="VOILUTFunction"					Type="3"	StringDefinedTerms="VOILUTFunction"
	SequenceEnd
MacroEnd

DefineMacro="RealWorldValueMappingMacro" InformationEntity="FunctionalGroup"
	Sequence="RealWorldValueMappingSequence"		Type="1"	VM="1-n"
		InvokeMacro="RealWorldValueMappingItemMacro"
	SequenceEnd
MacroEnd

DefineMacro="RealWorldValueMappingItemMacro" InformationEntity="FunctionalGroup"
	Name="RealWorldValueFirstValueMapped"				Type="1C" 	Condition="NeedRealWorldValueFirstValueMapped"
	Name="RealWorldValueLastValueMapped"				Type="1C" 	Condition="NeedRealWorldValueLastValueMapped"
	Name="DoubleFloatRealWorldValueFirstValueMapped"	Type="1C" 	Condition="NeedDoubleFloatRealWorldValueFirstValueMapped"
	Name="DoubleFloatRealWorldValueLastValueMapped"		Type="1C" 	Condition="NeedDoubleFloatRealWorldValueLastValueMapped"
	Name="RealWorldValueIntercept"				Type="1C" 	Condition="NeedRealWorldValueSlopeAndIntercept"
	Name="RealWorldValueSlope"					Type="1C" 	Condition="NeedRealWorldValueSlopeAndIntercept"
	Name="RealWorldValueLUTData"				Type="1C" 	Condition="RealWorldValueInterceptNotPresent"
	Name="LUTExplanation"						Type="1" 
	Name="LUTLabel"								Type="1" 
	Sequence="MeasurementUnitsCodeSequence"		Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"						DefinedContextID="7181"
	SequenceEnd
	Sequence="QuantityDefinitionSequence"		Type="3"	VM="1-n"
		InvokeMacro="ContentItemMacro"
	SequenceEnd
MacroEnd

DefineMacro="ContrastBolusUsageMacro" InformationEntity="FunctionalGroup"
	Sequence="ContrastBolusUsageSequence"			Type="1"	VM="1-n"
		Name="ContrastBolusAgentNumber"				Type="1" 
		Name="ContrastBolusAgentAdministered"		Type="1"	StringEnumValues="YesNoFull"
		Name="ContrastBolusAgentDetected"			Type="2"	StringEnumValues="YesNoFull"
		Name="ContrastBolusAgentPhase"				Type="2C"	NoCondition="" StringDefinedTerms="ContrastBolusAgentPhase"
	SequenceEnd
MacroEnd

DefineMacro="PixelIntensityRelationshipLUTMacro" InformationEntity="FunctionalGroup"
	Sequence="PixelIntensityRelationshipLUTSequence"	Type="1"	VM="1-n"
		Name="LUTDescriptor"							Type="1" 
		Name="LUTData"									Type="1" 
		Name="LUTFunction"								Type="1" 	StringEnumValues="PixelIntensityRelationshipLUTFunction"
	SequenceEnd
MacroEnd

DefineMacro="FramePixelShiftMacro" InformationEntity="FunctionalGroup"
	Sequence="FramePixelShiftSequence"		Type="1"	VM="1-n"
		Name="SubtractionItemID"			Type="1" 
		Name="MaskSubPixelShift"			Type="1"
	SequenceEnd
MacroEnd

DefineMacro="PatientOrientationInFrameMacro" InformationEntity="FunctionalGroup"
	Sequence="PatientOrientationInFrameSequence"		Type="1"	VM="1"
		Name="PatientOrientation"						Type="1"
	SequenceEnd
MacroEnd

DefineMacro="FrameDisplayShutterMacro" InformationEntity="FunctionalGroup"
	Sequence="FrameDisplayShutterSequence"		Type="1"	VM="1"
		InvokeMacro="DisplayShutterMacro"
	SequenceEnd
MacroEnd

DefineMacro="RespiratorySynchronizationMacro" InformationEntity="FunctionalGroup"
	Sequence="RespiratorySynchronizationSequence"		Type="1"	VM="1"
		Name="RespiratoryIntervalTime"					Type="1C"	Condition="NeedRespiratoryIntervalTime"
		Name="NominalPercentageOfRespiratoryPhase"		Type="1C"  	NoCondition="" mbpo="true"	# too hard
		Name="NominalRespiratoryTriggerDelayTime"		Type="1"
		Name="ActualRespiratoryTriggerDelayTime"		Type="1C"	Condition="RespiratoryTriggerTypeTimeOrBoth"
		Name="StartingRespiratoryAmplitude"				Type="1C"	Condition="RespiratoryTriggerTypeAmplitudeOrBoth"
		Name="StartingRespiratoryPhase"					Type="1C"	Condition="StartingRespiratoryAmplitudeIsPresent"	StringEnumValues="RespiratoryPhase"
		Name="EndingRespiratoryAmplitude"				Type="1C"	Condition="RespiratoryTriggerTypeAmplitudeOrBoth"
		Name="EndingRespiratoryPhase"					Type="1C"	Condition="EndingRespiratoryAmplitudeIsPresent"		StringEnumValues="RespiratoryPhase"
		
	SequenceEnd
MacroEnd

DefineMacro="IrradiationEventIdentificationMacro" InformationEntity="FunctionalGroup"
	Sequence="IrradiationEventIdentificationSequence"	Type="1"	VM="1"
		Name="IrradiationEventUID"						Type="1"
	SequenceEnd
MacroEnd

DefineMacro="RadiopharmaceuticalUsageMacro" InformationEntity="FunctionalGroup"
	Sequence="RadiopharmaceuticalUsageSequence"	Type="1"	VM="1"
		Name="RadiopharmaceuticalAgentNumber"	Type="1"
	SequenceEnd
MacroEnd

DefineMacro="PatientPhysiologicalStateMacro" InformationEntity="FunctionalGroup"
	Sequence="PatientPhysiologicalStateSequence"			Type="1"	VM="1"
		Sequence="PatientPhysiologicalStateCodeSequence"	Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"					DefinedContextID="3101"
		SequenceEnd
	SequenceEnd
MacroEnd

Module="MultiFrameDimension"
	Sequence="DimensionOrganizationSequence"	Type="1"	VM="1-n"
		Name="DimensionOrganizationUID"			Type="1" 
	SequenceEnd
	Name="DimensionOrganizationType"			Type="3"	StringDefinedTerms="DimensionOrganizationType"
	Sequence="DimensionIndexSequence"			Type="1C"	VM="1-n" Condition="DimensionOrganizationTypeIsNotTILED_FULL"	mbpo="true"
		Name="DimensionIndexPointer"			Type="1"
		Verify="DimensionIndexPointer"						Condition="DimensionIndexPointerIsFrameContentSequence"	ThenErrorMessage="May not be FrameContentSequence"
		Verify="DimensionIndexPointer"						Condition="DimensionIndexPointerIsDimensionIndexValues"	ThenErrorMessage="May not be DimensionIndexValues"
		Name="DimensionIndexPrivateCreator"		Type="1C"	NoCondition="" # too hard to check
		Name="FunctionalGroupPointer"			Type="1C"	Condition="DimensionIndexPointerIsNotFunctionalGroup"
		Name="FunctionalGroupPrivateCreator"	Type="1C"	NoCondition="" # too hard to check
		Name="DimensionOrganizationUID"			Type="1"
		Name="DimensionDescriptionLabel"		Type="3" 
	SequenceEnd
ModuleEnd

Module="CardiacSynchronization"	
	Name="CardiacSynchronizationTechnique"		Type="1C" 	StringEnumValues="CardiacSynchronizationTechnique"	Condition="ImageTypeValue1OriginalOrMixed" mbpo="true"
	Name="CardiacSignalSource"					Type="1C" 	StringDefinedTerms="CardiacSignalSource"		Condition="CardiacSynchronizationTechniqueNotNoneAndOriginalOrMixed" mbpo="true"
	Verify="CardiacSignalSource"							Condition="CardiacSignalSourcePresentAndCardiacSynchronizationTechniqueIsNone"	ThenErrorMessage="May not be present when CardiacSynchronizationTechnique is NONE"
	Name="CardiacRRIntervalSpecified"			Type="1C" 	Condition="CardiacSynchronizationTechniqueNotNoneAndOriginalOrMixed"
	Verify="CardiacRRIntervalSpecified"						Condition="CardiacRRIntervalSpecifiedPresentAndCardiacSynchronizationTechniqueIsNone"	ThenErrorMessage="May not be present when CardiacSynchronizationTechnique is NONE"
	Name="CardiacBeatRejectionTechnique"		Type="1C" 	StringDefinedTerms="CardiacBeatRejectionTechnique"	Condition="CardiacSynchronizationTechniqueProspectiveOrRetrospective"
	Verify="CardiacBeatRejectionTechnique"					Condition="CardiacBeatRejectionTechniquePresentAndCardiacSynchronizationTechniqueIsNotProspectiveOrRetrospective"	ThenErrorMessage="May not be present when CardiacSynchronizationTechnique is not PROSPECTIVE or RETROSPECTIVE"
	Name="LowRRValue"							Type="2C" 	Condition="CardiacSynchronizationTechniqueProspectiveOrRetrospective"
	Verify="LowRRValue"										Condition="LowRRValuePresentAndCardiacSynchronizationTechniqueIsNotProspectiveOrRetrospective"	ThenErrorMessage="May not be present when CardiacSynchronizationTechnique is not PROSPECTIVE or RETROSPECTIVE"
	Name="HighRRValue"							Type="2C" 	Condition="CardiacSynchronizationTechniqueProspectiveOrRetrospective"
	Verify="HighRRValue"									Condition="HighRRValuePresentAndCardiacSynchronizationTechniqueIsNotProspectiveOrRetrospective"	ThenErrorMessage="May not be present when CardiacSynchronizationTechnique is not PROSPECTIVE or RETROSPECTIVE"
	Name="IntervalsAcquired"					Type="2C" 	Condition="CardiacSynchronizationTechniqueNotNoneAndOriginalOrMixed"
	Verify="IntervalsAcquired"								Condition="IntervalsAcquiredPresentAndCardiacSynchronizationTechniqueIsNone"	ThenErrorMessage="May not be present when CardiacSynchronizationTechnique is NONE"
	Name="IntervalsRejected"					Type="2C" 	Condition="CardiacSynchronizationTechniqueNotNoneAndOriginalOrMixed"
	Verify="IntervalsRejected"								Condition="IntervalsRejectedPresentAndCardiacSynchronizationTechniqueIsNone"	ThenErrorMessage="May not be present when CardiacSynchronizationTechnique is NONE"
	Name="SkipBeats"							Type="3" 
	Name="CardiacFramingType"					Type="1C"	NoCondition="" 	StringDefinedTerms="CardiacFramingType"
ModuleEnd

Module="RespiratorySynchronization"
	Name="RespiratoryMotionCompensationTechnique"	Type="1C" 	StringDefinedTerms="RespiratoryMotionCompensationTechnique"	Condition="ImageTypeValue1OriginalOrMixed" mbpo="true"
	Name="RespiratorySignalSource"					Type="1C" 	StringDefinedTerms="RespiratorySignalSource"			Condition="RespiratoryMotionCompensationTechniqueNotNone"
	Verify="RespiratorySignalSource"							Condition="RespiratorySignalSourcePresentAndRespiratoryMotionCompensationTechniqueIsNone"	ThenErrorMessage="May not be present when RespiratoryMotionCompensationTechnique is NONE"
	Name="RespiratoryTriggerDelayThreshold"			Type="1C" 	Condition="RespiratoryMotionCompensationTechniqueNotNoneOrRealTimeOrBreathHoldAndOriginalOrMixed" mbpo="true"
	Name="RespiratoryTriggerType"					Type="1C"	NoCondition="" 	StringDefinedTerms="RespiratoryTriggerType"
ModuleEnd

Module="BulkMotionSynchronization"
	Name="BulkMotionCompensationTechnique"		Type="1C" 	StringDefinedTerms="BulkMotionCompensationTechnique"	Condition="ImageTypeValue1OriginalOrMixed"
	Name="BulkMotionSignalSource"				Type="1C" 	StringDefinedTerms="BulkMotionSignalSource"		Condition="BulkMotionCompensationTechniqueNotNoneAndOriginalOrMixed"
	Verify="BulkMotionSignalSource"							Condition="BulkMotionSignalSourcePresentAndBulkMotionCompensationTechniqueIsNone"	ThenErrorMessage="May not be present when BulkMotionCompensationTechnique is NONE"
ModuleEnd

Module="SupplementalPaletteColorLUT"
	Name="RedPaletteColorLookupTableDescriptor"		Type="1"
	Verify="RedPaletteColorLookupTableDescriptor"	Type="1"	ValueSelector="2"	BinaryEnumValues="BitsAre16"
	Name="GreenPaletteColorLookupTableDescriptor"	Type="1"
	Verify="GreenPaletteColorLookupTableDescriptor"	Type="1"	ValueSelector="2"	BinaryEnumValues="BitsAre16"
	Name="BluePaletteColorLookupTableDescriptor"	Type="1"
	Verify="BluePaletteColorLookupTableDescriptor"	Type="1"	ValueSelector="2"	BinaryEnumValues="BitsAre16"
	Name="RedPaletteColorLookupTableData"			Type="1"
	Name="GreenPaletteColorLookupTableData"			Type="1"
	Name="BluePaletteColorLookupTableData"			Type="1"
ModuleEnd

DefineMacro="PaletteColorLookupTableMacro"
	Name="RedPaletteColorLookupTableDescriptor"			Type="1"
	Verify="RedPaletteColorLookupTableDescriptor"					Condition="NotColorPaletteInstance"	ValueSelector="2"	BinaryEnumValues="BitsAre16"
	Verify="RedPaletteColorLookupTableDescriptor"					Condition="ColorPaletteInstance"	ValueSelector="2"	BinaryEnumValues="BitsAre8"
	Name="GreenPaletteColorLookupTableDescriptor"		Type="1"
	Verify="GreenPaletteColorLookupTableDescriptor"					Condition="NotColorPaletteInstance"	ValueSelector="2"	BinaryEnumValues="BitsAre16"
	Verify="GreenPaletteColorLookupTableDescriptor"					Condition="ColorPaletteInstance"	ValueSelector="2"	BinaryEnumValues="BitsAre8"
	Name="BluePaletteColorLookupTableDescriptor"		Type="1"
	Verify="BluePaletteColorLookupTableDescriptor"					Condition="NotColorPaletteInstance"	ValueSelector="2"	BinaryEnumValues="BitsAre16"
	Verify="BluePaletteColorLookupTableDescriptor"					Condition="ColorPaletteInstance"	ValueSelector="2"	BinaryEnumValues="BitsAre8"
	Name="PaletteColorLookupTableUID"					Type="3"	# should check matches SOPInstanceUID if is ColorPaletteInstance :(
	Name="RedPaletteColorLookupTableData"				Type="1C"	Condition="NeedsNonSegmentedLookupTableData"
	Name="GreenPaletteColorLookupTableData"				Type="1C"	Condition="NeedsNonSegmentedLookupTableData"
	Name="BluePaletteColorLookupTableData"				Type="1C"	Condition="NeedsNonSegmentedLookupTableData"
	Name="SegmentedRedPaletteColorLookupTableData"		Type="1C"	Condition="NeedsSegmentedLookupTableData"
	Name="SegmentedGreenPaletteColorLookupTableData"	Type="1C"	Condition="NeedsSegmentedLookupTableData"
	Name="SegmentedBluePaletteColorLookupTableData"		Type="1C"	Condition="NeedsSegmentedLookupTableData"
MacroEnd

Module="PaletteColorLookupTable"
	InvokeMacro="PaletteColorLookupTableMacro"
ModuleEnd

Module="PatientOrientation"
	InvokeMacro="PatientOrientationMacro"
ModuleEnd

Module="ImageEquipmentCoordinateRelationship"
	Name="ImageToEquipmentMappingMatrix"				Type="1"
	Name="EquipmentCoordinateSystemIdentification"		Type="1"	StringEnumValues="EquipmentCoordinateSystemIdentification"
ModuleEnd

Module="CRSeries"
	Name="BodyPartExamined"				Type="2"
	Verify="BodyPartExamined"						Condition="IsHuman"		StringDefinedTerms="BodyPartExaminedHuman"
	Verify="BodyPartExamined"						Condition="IsAnimal"	StringDefinedTerms="BodyPartExaminedAnimal"
	Name="ViewPosition"					Type="2"
	Verify="ViewPosition"							Condition="IsHuman"		StringDefinedTerms="ViewPositionHuman"
	Verify="ViewPosition"							Condition="IsAnimal"	StringDefinedTerms="ViewPositionAnimal"
	Name="FilterType"					Type="3"
	Name="CollimatorGridName"			Type="3"
	Name="FocalSpots"					Type="3"
	Name="PlateType"					Type="3"
	Name="PhosphorType"					Type="3"
ModuleEnd

Module="CRImage"
	Name="PhotometricInterpretation"				Type="1"	StringEnumValues="PhotometricInterpretationMonochrome"
	Name="KVP"										Type="3"	NotZeroWarning=""
	Name="PlateID"									Type="3"
	Name="DistanceSourceToDetector"					Type="3"
	Name="DistanceSourceToPatient"					Type="3"
	Name="ExposureTime"								Type="3"	NotZeroWarning=""
	Verify="ExposureTimeInms"									Condition="ExposureTimeInmsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <CRImage> - use ExposureTime instead of"

	Name="XRayTubeCurrent"							Type="3"	NotZeroWarning=""
	Verify="XRayTubeCurrentInmA"								Condition="XRayTubeCurrentInmAIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <CRImage> - use XRayTubeCurrent instead of"

	Name="Exposure"									Type="3"	NotZeroWarning=""
	Name="ExposureInuAs"							Type="3"	NotZeroWarning=""
	Verify="ExposureInmAs"										Condition="ExposureInmAsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <CRImage> - use Exposure and/or ExposureInuAs instead of"

	Name="ImagerPixelSpacing"						Type="3"	NotZeroError=""
	InvokeMacro="BasicPixelSpacingCalibrationMacro"
	Name="GeneratorPower"							Type="3"	NotZeroWarning=""
	Name="AcquisitionDeviceProcessingDescription"	Type="3"
	Name="AcquisitionDeviceProcessingCode"			Type="3"
	Name="CassetteOrientation"						Type="3"	StringEnumValues="Orientation"
	Name="CassetteSize"								Type="3"	StringDefinedTerms="CassetteSize"
	Name="ExposuresOnPlate"							Type="3"	NotZeroWarning=""
	Name="RelativeXRayExposure"						Type="3"	NotZeroWarning=""
	Name="Sensitivity"								Type="3"	NotZeroWarning=""
	InvokeMacro="GeneralAnatomyOptionalMacro"
	InvokeMacro="ExposureIndexMacro"
ModuleEnd

Module="CTImage"
	Name="ImageType"					Type="1"	ValueSelector="2"	StringDefinedTerms="CTImageType3"
	Verify="ImageType"								ValueSelector="3"	StringDefinedTerms="CTImageType4"
	Verify="ImageType"								Condition="ImageTypeValue3MissingOrEmpty"	ThenErrorMessage="A value is required for value 3 in CT Images"
	Verify="ImageType"								Condition="ImageTypeValue4MissingOrEmptyForMultienergy"	ThenErrorMessage="A value is required for value 4 in multi-energy acquisition CT Images"
	Name="MultienergyCTAcquisition"		Type="3"	StringEnumValues="YesNoFull"
	Name="SamplesPerPixel"				Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"	Type="1"	StringEnumValues="PhotometricInterpretationMonochrome"
	Name="BitsAllocated"				Type="1"	BinaryEnumValues="BitsAre16"
	Name="BitsStored"					Type="1"	BinaryEnumValues="BitsAre12To16"
	Name="HighBit"						Type="1"	BinaryEnumValues="BitsAre11To15"
	Name="RescaleIntercept"				Type="1"
	Name="RescaleSlope"					Type="1"	NotZeroError=""
	Name="RescaleType"					Type="1C"	Condition="MultienergyAcquisitionOrRescaleTypeIsPresentAndNotHU"	StringDefinedTerms="RescaleTypeHounsfieldUnits" mbpo="true"
	Verify="RescaleType"							Condition="RescaleTypeIsPresentAndNotHUAndImageIsOriginalNotLocalizerAndNotMultienergyAcquisition" ThenErrorMessage="If RescaleType is present and not multi-energy acquisition, must be HU for ORIGINAL non-LOCALIZER images"
	Verify="RescaleType"							Condition="RescaleTypeIsPresentAndIsHUAndImageIsOriginalLocalizerAndNotMultienergyAcquisition"   ThenWarningMessage="If RescaleType is present and not multi-energy acquisition, should not be HU for ORIGINAL LOCALIZER images"
	Name="KVP"							Type="2"	NotZeroWarning=""
	Verify="KVP"									Condition="KVPNotEmptyWhenAlsoPresentInMultienergyCTAcquisitionSequence" ThenErrorMessage="Attribute shall be empty within Module <CTImage> when also present in MultienergyCTAcquisitionSequence"
	Name="AcquisitionNumber"			Type="2"
	Name="ScanOptions"					Type="3"	# too hard to check multi-energy contraint of same value
	Name="DataCollectionDiameter"		Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Name="DataCollectionCenterPatient"	Type="3"
	Name="ReconstructionDiameter"		Type="3"	NotZeroWarning=""
	Name="ReconstructionTargetCenterPatient"	Type="3"
	Name="DistanceSourceToDetector"		Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Name="DistanceSourceToPatient"		Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Name="GantryDetectorTilt"			Type="3"
	Name="TableHeight"					Type="3"
	Name="RotationDirection"			Type="3"	StringEnumValues="RotationDirection"
	Name="ExposureTime"					Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Verify="ExposureTimeInms"						Condition="ExposureTimeInmsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <CTImage> - use ExposureTime instead of"
	
	Name="XRayTubeCurrent"				Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Verify="XRayTubeCurrentInmA"					Condition="XRayTubeCurrentInmAIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <CTImage> - use XRayTubeCurrent instead of"
	
	Name="Exposure"						Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Name="ExposureInuAs"				Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Verify="ExposureInmAs"							Condition="ExposureInmAsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <CTImage> - use Exposure and/or ExposureInuAs instead of"
	
	Name="FilterType"					Type="3"	# too hard to check multi-energy contraint of same value
	Name="GeneratorPower"				Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Name="FocalSpots"					Type="3"	# too hard to check multi-energy contraint of same value
	Name="ConvolutionKernel"			Type="3"
	Name="RevolutionTime"				Type="3"	NotZeroWarning=""
	Name="SingleCollimationWidth"		Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Name="TotalCollimationWidth"		Type="3"	NotZeroWarning=""	# too hard to check multi-energy contraint of same value
	Name="TableSpeed"					Type="3"	NotZeroWarning=""
	Name="TableFeedPerRotation"			Type="3"	NotZeroWarning=""
	Name="SpiralPitchFactor"			Type="3"	NotZeroWarning=""
	Name="ExposureModulationType"		Type="3"
	Name="EstimatedDoseSaving"			Type="3"
	Name="CTDIvol"						Type="3"	NotZeroWarning=""
	Verify="CTDIvol"							Condition="CTDIvolIsPresentButCTDIPhantomTypeCodeSequenceIsNot"   ThenWarningMessage="CTDIvol is present but it is uninterpretable without CTDIPhantomTypeCodeSequence, which is absent"
	Sequence="CTDIPhantomTypeCodeSequence"	Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"				DefinedContextID="4052"
	SequenceEnd
	Name="WaterEquivalentDiameter"		Type="3"	NotZeroWarning=""
	Sequence="WaterEquivalentDiameterCalculationMethodCodeSequence"	Type="1C"	VM="1"	Condition="WaterEquivalentDiameterIsPresent"
		InvokeMacro="CodeSequenceMacro"				DefinedContextID="10024"
	SequenceEnd
	Name="ImageAndFluoroscopyAreaDoseProduct"	Type="3"	NotZeroWarning=""
	InvokeMacro="GeneralAnatomyOptionalMacro"
	InvokeMacro="OptionalViewAndSliceProgressionDirectionMacro"
	Name="CalciumScoringMassFactorPatient"		Type="3"	NotZeroWarning=""
	Name="CalciumScoringMassFactorDevice"		Type="3"	NotZeroWarning=""
	Name="EnergyWeightingFactor"				Type="1C"	Condition="MultiEnergyProportionalWeighting" mbpo="true"
	Sequence="CTAdditionalXRaySourceSequence"	Type="3"	VM="1-n"
		Name="KVP"								Type="1"	NotZeroWarning=""
		Name="XRayTubeCurrentInmA"				Type="1"	NotZeroWarning=""
		Name="DataCollectionDiameter"			Type="1"	NotZeroWarning=""
		Name="FocalSpots"						Type="1"
		Name="FilterType"						Type="1"
		Name="FilterMaterial"					Type="1"
		Name="ExposureInmAs"					Type="3"	NotZeroWarning=""
		Name="EnergyWeightingFactor"			Type="1C"	NotZeroWarning=""	Condition="EnergyWeightingFactorPresentInRoot" mbpo="true"	# delegate condition since hard otherwise; same result
	SequenceEnd
	Name="IsocenterPosition"					Type="3"
	InvokeMacro="RTEquipmentCorrelationMacro"
ModuleEnd

Module="MRImage"
	Name="ImageType"					Type="1"	ValueSelector="2"	StringDefinedTerms="MRImageType3"
	Verify="ImageType"								Condition="ImageTypeValue3MissingOrEmpty"	ThenErrorMessage="A value is required for value 3 in MR Images"
	Name="SamplesPerPixel"				Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"	Type="1"	StringEnumValues="PhotometricInterpretationMonochrome"
	Name="BitsAllocated"				Type="1"	BinaryEnumValues="BitsAre16"
	Name="ScanningSequence"				Type="1"	StringEnumValues="ScanningSequence"
	Name="SequenceVariant"				Type="1"	StringDefinedTerms="SequenceVariant"
	Name="ScanOptions"					Type="2"	StringDefinedTerms="ScanOptions"
	Name="MRAcquisitionType"			Type="2"	StringEnumValues="MRAcquisitionType"
	Name="RepetitionTime"				Type="2C"	Condition="MRIsNotEchoPlanarOrIsSegmentedKSpace" mbpo="true"
	Name="EchoTime"						Type="2"	NotZeroWarning=""
	Name="EchoTrainLength"				Type="2"	NotZeroWarning=""
	Name="InversionTime"				Type="2C"	Condition="MRIsInversionRecovery"	NotZeroWarning=""
	Name="TriggerTime"					Type="2C"	Condition="MRIsCardiacOrPulseGated"
	Name="SequenceName"					Type="3"
	Name="AngioFlag"					Type="3"	StringEnumValues="AngioFlag"
	Name="NumberOfAverages"				Type="3"	NotZeroWarning=""
	Name="ImagingFrequency"				Type="3"	NotZeroWarning=""
	Name="ImagedNucleus"				Type="3"
	Name="EchoNumbers"					Type="3"
	Name="MagneticFieldStrength"		Type="3"	NotZeroWarning=""
	Name="SpacingBetweenSlices"			Type="3"
	Name="NumberOfPhaseEncodingSteps"	Type="3"
	Name="PercentSampling"				Type="3"
	Name="PercentPhaseFieldOfView"		Type="3"
	Name="PixelBandwidth"				Type="3"
	Name="NominalInterval"				Type="3"
	Name="BeatRejectionFlag"			Type="3"	StringEnumValues="YesNoLetter"
	Name="LowRRValue"					Type="3"
	Name="HighRRValue"					Type="3"
	Name="IntervalsAcquired"			Type="3"
	Name="IntervalsRejected"			Type="3"
	Name="PVCRejection"					Type="3"
	Name="SkipBeats"					Type="3"
	Name="HeartRate"					Type="3"
	Name="CardiacNumberOfImages"		Type="3"
	Name="TriggerWindow"				Type="3"
	Name="ReconstructionDiameter"		Type="3"
	Name="ReceiveCoilName"				Type="3"
	Name="TransmitCoilName"				Type="3"
	Name="AcquisitionMatrix"			Type="3"
	Name="InPlanePhaseEncodingDirection"	Type="3"	StringEnumValues="PhaseEncodingDirection"
	Name="FlipAngle"					Type="3"	NotZeroWarning=""
	Name="SAR"							Type="3"
	Name="VariableFlipAngleFlag"		Type="3"	StringEnumValues="YesNoLetter"
	Name="dBdt"							Type="3"
	Name="TemporalPositionIdentifier"	Type="3"
	Name="NumberOfTemporalPositions"	Type="3"
	Name="TemporalResolution"			Type="3"
	InvokeMacro="GeneralAnatomyOptionalMacro"
	InvokeMacro="OptionalViewAndSliceProgressionDirectionMacro"
	Name="IsocenterPosition"			Type="3"
	Name="B1rms"						Type="3"
	Verify="RescaleIntercept"							Condition="RescaleInterceptPresentAndNotIdentity"	ThenWarningMessage="Non-identity Modality LUT not expected to be present in standard MR IOD - may cause windowing problems" ShowValueWithMessage="true"
	Verify="RescaleSlope"								Condition="RescaleSlopePresentAndNotIdentity"		ThenWarningMessage="Non-identity Modality LUT not expected to be present in standard MR IOD - may cause windowing problems" ShowValueWithMessage="true"
ModuleEnd

Module="NMPETPatientOrientation"
	Sequence="PatientOrientationCodeSequence"				Type="2"	VM="0-1"
		InvokeMacro="CodeSequenceMeaningOptionalMacro"							BaselineContextID="19"
		Sequence="PatientOrientationModifierCodeSequence"   Type="2C"	VM="0-1"	NoCondition=""	# real-world - orientation wrt. gravity
 			InvokeMacro="CodeSequenceMeaningOptionalMacro"						BaselineContextID="20"
		SequenceEnd
	SequenceEnd
	Sequence="PatientGantryRelationshipCodeSequence"		Type="2"	VM="0-1"
		InvokeMacro="CodeSequenceMeaningOptionalMacro"							BaselineContextID="21"
	SequenceEnd
ModuleEnd

Module="NMImagePixel"
	Name="SamplesPerPixel"				Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"   	Type="1"	StringEnumValues="NMPhotometricInterpretation"
	Name="BitsAllocated"				Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"					Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="HighBit"						Type="1"	BinaryEnumValues="BitsAre7Or15"
	Name="PixelSpacing"					Type="2"	NotZeroError=""
ModuleEnd

Module="NMMultiFrame"
	Name="FrameIncrementPointer"   		Type="1"	TagEnumValues="NMFrameIncrementPointerValues"
	
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3WholeBodyOrStatic"	ValueSelector="0"	TagEnumValues="FrameIncrementPointerIsEnergyWindowVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3WholeBodyOrStatic"	ValueSelector="1"	TagEnumValues="FrameIncrementPointerIsDetectorVector"
	
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Dynamic"	ValueSelector="0"	TagEnumValues="FrameIncrementPointerIsEnergyWindowVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Dynamic"	ValueSelector="1"	TagEnumValues="FrameIncrementPointerIsDetectorVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Dynamic"	ValueSelector="2"	TagEnumValues="FrameIncrementPointerIsPhaseVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Dynamic"	ValueSelector="3"	TagEnumValues="FrameIncrementPointerIsTimeSliceVector"

	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Gated"	ValueSelector="0"	TagEnumValues="FrameIncrementPointerIsEnergyWindowVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Gated"	ValueSelector="1"	TagEnumValues="FrameIncrementPointerIsDetectorVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Gated"	ValueSelector="2"	TagEnumValues="FrameIncrementPointerIsRRIntervalVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Gated"	ValueSelector="3"	TagEnumValues="FrameIncrementPointerIsTimeSlotVector"

	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Tomo"	ValueSelector="0"	TagEnumValues="FrameIncrementPointerIsEnergyWindowVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Tomo"	ValueSelector="1"	TagEnumValues="FrameIncrementPointerIsDetectorVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Tomo"	ValueSelector="2"	TagEnumValues="FrameIncrementPointerIsRotationVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3Tomo"	ValueSelector="3"	TagEnumValues="FrameIncrementPointerIsAngularViewVector"

	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3GatedTomo"	ValueSelector="0"	TagEnumValues="FrameIncrementPointerIsEnergyWindowVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3GatedTomo"	ValueSelector="1"	TagEnumValues="FrameIncrementPointerIsDetectorVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3GatedTomo"	ValueSelector="2"	TagEnumValues="FrameIncrementPointerIsRotationVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3GatedTomo"	ValueSelector="3"	TagEnumValues="FrameIncrementPointerIsRRIntervalVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3GatedTomo"	ValueSelector="4"	TagEnumValues="FrameIncrementPointerIsTimeSlotVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3GatedTomo"	ValueSelector="5"	TagEnumValues="FrameIncrementPointerIsAngularViewVector"

	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3ReconTomo"	ValueSelector="0"	TagEnumValues="FrameIncrementPointerIsSliceVector"

	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3ReconGatedTomo"	ValueSelector="0"	TagEnumValues="FrameIncrementPointerIsRRIntervalVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3ReconGatedTomo"	ValueSelector="1"	TagEnumValues="FrameIncrementPointerIsTimeSlotVector"
	Verify="FrameIncrementPointer"					Condition="ImageTypeValue3ReconGatedTomo"	ValueSelector="2"	TagEnumValues="FrameIncrementPointerIsSliceVector"
	
	Name="EnergyWindowVector"   		Type="1C"	Condition="FrameIncrementPointerContainsEnergyWindowVector"
	Name="NumberOfEnergyWindows"   		Type="1"
	Name="DetectorVector"				Type="1C"	Condition="FrameIncrementPointerContainsDetectorVector"
	Name="NumberOfDetectors"			Type="1"
	Name="PhaseVector"					Type="1C"	Condition="FrameIncrementPointerContainsPhaseVector"
	Name="NumberOfPhases"				Type="1C"	Condition="FrameIncrementPointerContainsPhaseVector"
	Name="RotationVector"				Type="1C"	Condition="FrameIncrementPointerContainsRotationVector"
	Name="NumberOfRotations"			Type="1C"	Condition="ImageTypeValue3TomoFamily"
	Name="RRIntervalVector"				Type="1C"	Condition="FrameIncrementPointerContainsRRIntervalVector"
	Name="NumberOfRRIntervals"   		Type="1C"	Condition="FrameIncrementPointerContainsRRIntervalVector"
	Name="TimeSlotVector"				Type="1C"	Condition="FrameIncrementPointerContainsTimeSlotVector"
	Name="NumberOfTimeSlots"			Type="1C"	Condition="FrameIncrementPointerContainsTimeSlotVector"
	Name="SliceVector"					Type="1C"	Condition="FrameIncrementPointerContainsSliceVector"
	Name="NumberOfSlices"				Type="1C"	Condition="FrameIncrementPointerContainsSliceVector"
	Name="AngularViewVector"			Type="1C"	Condition="FrameIncrementPointerContainsAngularViewVector"
	Name="TimeSliceVector"				Type="1C"	Condition="FrameIncrementPointerContainsTimeSliceVector"
ModuleEnd

Module="NMImage"
	Name="ImageType"						Type="1"	ValueSelector="1"	StringEnumValues="NMImageTypeValue2"
	Verify="ImageType"									ValueSelector="2"	StringEnumValues="NMImageTypeValue3"
	Verify="ImageType"									ValueSelector="3"	StringEnumValues="NMImageTypeValue4"
	Verify="ImageType"								Condition="ImageTypeValue3MissingOrEmpty"	ThenErrorMessage="A value is required for value 3 in NM Images"
	Verify="ImageType"								Condition="ImageTypeValue4MissingOrEmpty"	ThenErrorMessage="A value is required for value 4 in NM Images"
	Name="ImageID"							Type="3"
	Name="LossyImageCompression"			Type="1C"	NoCondition=""	StringEnumValues="LossyImageCompression"
	Name="CountsAccumulated"				Type="2"
	Name="AcquisitionTerminationCondition"	Type="3"	StringDefinedTerms="NMAcquisitionTerminationCondition"
	Name="TableHeight"						Type="3"
	Name="TableTraverse"					Type="3"
	Name="ActualFrameDuration"				Type="1C"	Condition="ImageTypeValue3WholeBodyOrStatic"
	Name="CountRate"						Type="3"
	Name="ProcessingFunction"				Type="3"
	Name="CorrectedImage"					Type="3"	StringDefinedTerms="NMCorrectedImage"
	Name="WholeBodyTechnique"				Type="3"	StringEnumValues="NMWholeBodyTechnique"
	Name="ScanVelocity"						Type="2C"	Condition="ImageTypeValue3WholeBody"
	Name="ScanLength"						Type="2C"	Condition="ImageTypeValue3WholeBody"
	Name="TriggerSourceOrType"   			Type="3"	StringDefinedTerms="EKG"
	InvokeMacro="GeneralAnatomyOptionalMacro"
	Sequence="RealWorldValueMappingSequence"		Type="3"	VM="1-n"
		InvokeMacro="RealWorldValueMappingItemMacro"
	SequenceEnd
ModuleEnd
	
Module="NMIsotope"
	Sequence="EnergyWindowInformationSequence"   		Type="2"	VM="0-n"
            Name="EnergyWindowName"						Type="3"
            Sequence="EnergyWindowRangeSequence"   		Type="3"	VM="1-n"
                    Name="EnergyWindowLowerLimit"   	Type="3"
                    Name="EnergyWindowUpperLimit"   	Type="3"
	    SequenceEnd
	SequenceEnd
	Sequence="RadiopharmaceuticalInformationSequence"  	Type="2"	VM="0-n"
		Sequence="RadionuclideCodeSequence"				Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMeaningOptionalMacro"		BaselineContextID="18"
	    SequenceEnd
		Name="RadiopharmaceuticalRoute"					Type="3"
		Sequence="AdministrationRouteCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMeaningOptionalMacro"		BaselineContextID="11"
	    SequenceEnd
		Name="RadiopharmaceuticalVolume"				Type="3"
		Name="RadiopharmaceuticalStartTime"				Type="3"
		Name="RadiopharmaceuticalStopTime"				Type="3"
		Name="RadionuclideTotalDose"					Type="3"
		Sequence="CalibrationDataSequence"				Type="3"	VM="1-n"
			Name="EnergyWindowNumber"					Type="1"
			Name="SyringeCounts"						Type="3"
			Name="ResidualSyringeCounts"				Type="3"
	    SequenceEnd
		Name="Radiopharmaceutical"						Type="3"
		Sequence="RadiopharmaceuticalCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMeaningOptionalMacro"		BaselineContextID="25"
	    SequenceEnd
	SequenceEnd
	Sequence="InterventionDrugInformationSequence"   	Type="3"	VM="1-n"
		Name="InterventionDrugName"						Type="3"
		Sequence="InterventionDrugCodeSequence"   		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMeaningOptionalMacro"		BaselineContextID="10"
	    SequenceEnd
		Sequence="AdministrationRouteCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMeaningOptionalMacro"		BaselineContextID="11"
	    SequenceEnd
		Name="InterventionDrugStartTime"				Type="3"
		Name="InterventionDrugStopTime"					Type="3"
		Name="InterventionDrugDose"						Type="3"
	SequenceEnd
ModuleEnd

Module="NMDetector"
	Sequence="DetectorInformationSequence"   	Type="2"	VM="0-n"
		Name="CollimatorGridName"   			Type="3"
		Name="CollimatorType"   				Type="2"	StringDefinedTerms="NMCollimatorType"
		Name="FieldOfViewShape"   				Type="3"	StringDefinedTerms="NMFieldOfViewShape"
		Name="FieldOfViewDimensions"   			Type="3"
		Name="FocalDistance"					Type="3"
		Name="XFocusCenter"						Type="3"
		Name="YFocusCenter"						Type="3"
		Name="ZoomCenter"						Type="3"
		Name="ZoomFactor"						Type="3"
		Name="CenterOfRotationOffset"   		Type="3"
		Name="GantryDetectorTilt"   			Type="3"
		Name="DistanceSourceToDetector"   		Type="2C"	Condition="ImageTypeValue4TransmissionAndNotTomo"
		Name="StartAngle"						Type="3"
		Name="RadialPosition"   				Type="3"
		Name="ImageOrientationPatient"   		Type="2"
		Name="ImagePositionPatient"   			Type="2"
		Sequence="ViewCodeSequence"   			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMeaningOptionalMacro"		BaselineContextID="26"
			Sequence="ViewModifierCodeSequence" Type="2C"	VM="0-1"	NoCondition=""	# if needed to fully specify the view
				InvokeMacro="CodeSequenceMeaningOptionalMacro"	BaselineContextID="23"
			SequenceEnd
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="NMTomoAcquisition"
	Sequence="RotationInformationSequence"  Type="2"	VM="0-n"
		Name="StartAngle"   				Type="1"
		Name="AngularStep"   				Type="1"
		Name="RotationDirection"   			Type="1"	StringEnumValues="RotationDirection"
		Name="ScanArc"   					Type="1"
		Name="ActualFrameDuration"   		Type="1"
		Name="RadialPosition"   			Type="3"
		Name="DistanceSourceToDetector"  	Type="2C"	Condition="ImageTypeValue4Transmission"
		Name="NumberOfFramesInRotation"   	Type="1"
		Name="TableTraverse"   				Type="3"
		Name="TableHeight"   				Type="3"
	SequenceEnd
	Name="TypeOfDetectorMotion"   			Type="3"	StringEnumValues="NMTypeOfDetectorMotion"
ModuleEnd

Module="NMMultiGatedAcquisition"
	Name="BeatRejectionFlag"						Type="3"	StringEnumValues="YesNoLetter"
	Name="PVCRejection"								Type="3"
	Name="SkipBeats"								Type="3"
	Name="HeartRate"								Type="3"
	Sequence="GatedInformationSequence"   			Type="2C"	VM="0-n"	Condition="FrameIncrementPointerContainsRRIntervalVector"
		Name="TriggerTime"							Type="3"
		Name="CardiacFramingType"					Type="3"
		Sequence="DataInformationSequence"   		Type="2"	VM="0-n"
			Name="FrameTime"						Type="1"
			Name="NominalInterval"					Type="3"
			Name="LowRRValue"						Type="3"
			Name="HighRRValue"						Type="3"
			Name="IntervalsAcquired"				Type="3"
			Name="IntervalsRejected"				Type="3"
			Sequence="TimeSlotInformationSequence"  Type="2C"	VM="0-n"	Condition="FrameIncrementPointerContainsTimeSlotVector"
				Name="TimeSlotTime"					Type="3"
			SequenceEnd
	    SequenceEnd
	SequenceEnd
ModuleEnd

Module="NMPhase"
	Sequence="PhaseInformationSequence"   	Type="2C"	VM="0-n"	Condition="FrameIncrementPointerContainsPhaseVector"
		Name="PhaseDelay"					Type="1"
		Name="ActualFrameDuration"			Type="1"
		Name="PauseBetweenFrames"			Type="1"
		Name="NumberOfFramesInPhase"		Type="1"
		Name="TriggerVector"				Type="3"
		Name="NumberOfTriggersInPhase"   	Type="1C"	Condition="TriggerVectorIsPresent"
		Name="PhaseDescription"				Type="3"	StringDefinedTerms="NMPhaseDescription"
	SequenceEnd
ModuleEnd

Module="NMReconstruction"
	Name="SpacingBetweenSlices"   		Type="2"
	Name="ReconstructionDiameter"   	Type="3"	NotZeroWarning=""
	Name="ConvolutionKernel"			Type="3"
	Name="SliceThickness"				Type="2"	NotZeroWarning=""
	Name="SliceLocation"				Type="3"
	Name="SliceProgressionDirection"	Type="3"	StringEnumValues="CardiacSliceProgressionDirection"
ModuleEnd

Module="USRegionCalibration"
	Sequence="SequenceOfUltrasoundRegions"			Type="1"	VM="1-n"
		Name="RegionLocationMinX0"					Type="1"
		Name="RegionLocationMinY0"					Type="1"
		Name="RegionLocationMaxX1"					Type="1"
		Name="RegionLocationMaxY1"					Type="1"
		Name="PhysicalUnitsXDirection"				Type="1"
		Name="PhysicalUnitsYDirection"				Type="1"
		Name="PhysicalDeltaX"						Type="1"
		Name="PhysicalDeltaY"						Type="1"
		Name="ReferencePixelX0"						Type="3"
		Name="ReferencePixelY0"						Type="3"
		Name="ReferencePixelPhysicalValueX"			Type="3"
		Name="ReferencePixelPhysicalValueY"			Type="3"
		Name="RegionSpatialFormat"					Type="1"	BinaryEnumValues="RegionSpatialFormat"
		Name="RegionDataType"						Type="1"	BinaryEnumValues="RegionDataType"
		Name="RegionFlags"							Type="1"	BinaryBitMap="RegionFlags"
		Name="PixelComponentOrganization"			Type="1C"	Condition="NeedPixelComponentOrganization"	BinaryEnumValues="PixelComponentOrganization"
		Name="PixelComponentMask"					Type="1C"	Condition="PixelComponentOrganizationIs0"
		Name="PixelComponentRangeStart"				Type="1C"	Condition="PixelComponentOrganizationIs1"
		Name="PixelComponentRangeStop"				Type="1C"	Condition="PixelComponentOrganizationIs1"
		Name="PixelComponentPhysicalUnits"			Type="1C"	Condition="PixelComponentOrganizationPresent"	BinaryEnumValues="PixelComponentPhysicalUnits"
		Name="PixelComponentDataType"				Type="1C"	Condition="PixelComponentOrganizationPresent"	BinaryEnumValues="PixelComponentDataType"
		Name="NumberOfTableBreakPoints"				Type="1C"	Condition="PixelComponentOrganizationIs0Or1"
		Name="TableOfXBreakPoints"					Type="1C"	Condition="PixelComponentOrganizationIs0Or1"
		Name="TableOfYBreakPoints"					Type="1C"	Condition="PixelComponentOrganizationIs0Or1"
		Name="NumberOfTableEntries"					Type="1C"	Condition="PixelComponentOrganizationIs2Or3"
		Name="TableOfPixelValues"					Type="1C"	Condition="PixelComponentOrganizationIs2"
		Name="TableOfParameterValues"				Type="1C"	Condition="PixelComponentOrganizationIs2"
		Sequence="PixelValueMappingCodeSequence"	Type="1C"	VM="1-n"	Condition="PixelComponentOrganizationIs3"
			InvokeMacro="CodeSequenceMacro"			BaselineContextID="3497"
		SequenceEnd
		Name="TransducerFrequency"					Type="3"
		Name="PulseRepetitionFrequency"				Type="3"
		Name="DopplerCorrectionAngle"				Type="3"
		Name="SteeringAngle"						Type="3"
		Name="DopplerSampleVolumeXPosition"			Type="3"
		Name="DopplerSampleVolumeYPosition"			Type="3"
		Name="TMLinePositionX0"						Type="3"
		Name="TMLinePositionY0"						Type="3"
		Name="TMLinePositionX1"						Type="3"
		Name="TMLinePositionY1"						Type="3"
	SequenceEnd
ModuleEnd

Module="USImage"
	Name="SamplesPerPixel"							Type="1"	NotZeroError=""
	Verify="SamplesPerPixel"									Condition="PhotometricInterpretationNeedsOneSample"	BinaryEnumValues="SamplesPerPixelIsOne"
	Verify="SamplesPerPixel"									Condition="PhotometricInterpretationNeedsThreeSamples"	BinaryEnumValues="SamplesPerPixelIsThree"
	Name="PhotometricInterpretation"				Type="1"	StringDefinedTerms="USPhotometricInterpretation"

	Verify="PhotometricInterpretation"				Condition="UncompressedTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"				Condition="JPEGLSLosslessTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"				Condition="JPEG2000TransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRICT"
	Verify="PhotometricInterpretation"				Condition="JPEG2000LosslessTransferSyntaxAndThreeSamples"				StringEnumValues="PhotometricInterpretationYBRRCT"
	Verify="PhotometricInterpretation"				Condition="MPEG2TransferSyntax"											StringEnumValues="PhotometricInterpretationYBRPartial420"	# regardless of number of samples (required to be 3 by PS 3.5)
	Verify="PhotometricInterpretation"				Condition="JPEGLossyTransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRFull422"
	Verify="PhotometricInterpretation"				Condition="RLETransferSyntaxAndThreeSamples"							StringEnumValues="PhotometricInterpretationYBRFullOrRGB"

	Name="BitsAllocated"							Type="1"	NotZeroError=""
	Verify="BitsAllocated"										Condition="US8BitSamples"	BinaryEnumValues="BitsAre8"
	Verify="BitsAllocated"										Condition="US8Or16BitSamples"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"								Type="1"	NotZeroError=""
	Verify="BitsStored"											Condition="US8BitSamples"	BinaryEnumValues="BitsAre8"
	Verify="BitsStored"											Condition="US8Or16BitSamples"	BinaryEnumValues="BitsAre8Or16"
	Name="HighBit"									Type="1"
	Verify="HighBit"											Condition="US8BitSamples"	BinaryEnumValues="BitsAre7"
	Verify="HighBit"											Condition="US8Or16BitSamples"	BinaryEnumValues="BitsAre7Or15"
	Name="PlanarConfiguration"						Type="1C"	Condition="SamplesPerPixelGreaterThanOne"	BinaryEnumValues="USPlanarConfiguration"
	Verify="PlanarConfiguration"								Condition="USNeedsColorByPlaneOrPixel"	BinaryEnumValues="PlanarConfigurationIsColorByPlaneOrPixel"
	Verify="PlanarConfiguration"								Condition="USNeedsColorByPixel"		BinaryEnumValues="PlanarConfigurationIsColorByPixel"
	Verify="PlanarConfiguration"								Condition="USNeedsColorByPlane"		BinaryEnumValues="PlanarConfigurationIsColorByPlane"
	Name="PixelRepresentation"						Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="FrameIncrementPointer"					Type="1C"	Condition="NumberOfFramesPresent"
	Name="ImageType"								Type="2"  	ValueSelector="2"	StringDefinedTerms="USImageType3"
	Verify="ImageType"											ValueSelector="3"	StringDefinedTerms="USImageType4"
	Name="LossyImageCompression"					Type="1C"	NoCondition=""	StringEnumValues="LossyImageCompression"
	Name="NumberOfStages"							Type="2C"	Condition="IsUltrasoundStageProtocol"
	Name="NumberOfViewsInStage"						Type="2C"	Condition="IsUltrasoundStageProtocol"
	Name="RWaveTimeVector"							Type="3"
	Name="UltrasoundColorDataPresent"				Type="3"	BinaryEnumValues="UltrasoundColorDataPresent"
	Name="StageName"								Type="3"	StringDefinedTerms="USStageName"
	Sequence="StageCodeSequence"					Type="3"	VM="1-n"
 		InvokeMacro="CodeSequenceMacro"				BaselineContextID="12002"
	SequenceEnd
	Name="StageNumber"								Type="3"
	Name="ViewName"									Type="3"
	Name="ViewNumber"								Type="3"
	Name="NumberOfEventTimers"						Type="3"
	Name="EventElapsedTimes"						Type="3"
	Name="EventTimerNames"							Type="3"
	InvokeMacro="GeneralAnatomyOptionalMacro"
	InvokeMacro="OptionalViewAndSliceProgressionDirectionMacro"
	Name="AcquisitionDateTime"						Type="1C"	Condition="ModalityIsIVUS" mbpo="true"
	Name="TriggerTime"								Type="3"
	Name="NominalInterval"							Type="3"
	Name="BeatRejectionFlag"						Type="3"	StringEnumValues="YesNoLetter"
	Name="LowRRValue"								Type="3"
	Name="HighRRValue"								Type="3"
	Name="HeartRate"								Type="3"
	Name="IVUSAcquisition"							Type="1C"	Condition="ModalityIsIVUS"	StringDefinedTerms="IVUSAcquisition"
	Name="IVUSPullbackRate"							Type="1C"	Condition="IVUSAcquisitionIsMotor"
	Name="IVUSGatedRate"							Type="1C"	Condition="IVUSAcquisitionIsGated"
	Name="IVUSPullbackStartFrameNumber"				Type="1C"	Condition="IVUSAcquisitionIsMotorOrGated"	NotZeroError=""
	Name="IVUSPullbackStopFrameNumber"				Type="1C"	Condition="IVUSAcquisitionIsMotorOrGated"	NotZeroError=""
	Name="LesionNumber"								Type="3"
	Name="OutputPower"								Type="3"
	Name="TransducerData"							Type="3"
	Name="TransducerType"							Type="3"	StringDefinedTerms="USTransducerType"
	Name="FocusDepth"								Type="3"
	Name="ProcessingFunction"						Type="3"
	Name="MechanicalIndex"							Type="3"
	Name="BoneThermalIndex"							Type="3"
	Name="CranialThermalIndex"						Type="3"
	Name="SoftTissueThermalIndex"					Type="3"
	Name="SoftTissueFocusThermalIndex"				Type="3"
	Name="SoftTissueSurfaceThermalIndex"			Type="3"
	Name="DepthOfScanField"							Type="3"
	Name="OverlaySubtype"							Type="3"	StringDefinedTerms="OverlaySubtypeUS"
ModuleEnd

Module="SCEquipment"
	Name="ConversionType"								Type="1"	StringDefinedTerms="ConversionType"
	Name="Modality"										Type="3"	StringDefinedTerms="Modality"
	Name="SecondaryCaptureDeviceID"						Type="3"
	Name="SecondaryCaptureDeviceManufacturer"			Type="3"
	Name="SecondaryCaptureDeviceManufacturerModelName"	Type="3"
	Name="SecondaryCaptureDeviceSoftwareVersions"		Type="3"
	Name="VideoImageFormatAcquired"						Type="3"
	Name="DigitalImageFormatAcquired"					Type="3"
ModuleEnd

Module="SCImage"
	Name="DateOfSecondaryCapture"						Type="3"
	Name="TimeOfSecondaryCapture"						Type="3"
	Name="NominalScannedPixelSpacing"					Type="3"	NotZeroError=""
	InvokeMacro="BasicPixelSpacingCalibrationMacro"
	InvokeMacro="OptionalViewAndSliceProgressionDirectionMacro"
ModuleEnd

Module="SCMultiFrameImage"
	Name="BurnedInAnnotation"							Type="1"	StringEnumValues="YesNoFull"
	Name="RecognizableVisualFeatures"					Type="3"	StringEnumValues="YesNoFull"
	Name="PresentationLUTShape"							Type="1C"	StringEnumValues="SecondaryCapturePresentationLUTShape"	Condition="MonochromeNotBitmapPhotometricInterpretation"
	Name="Illumination"									Type="3"
	Name="ReflectedAmbientLight"						Type="3"
	Name="RescaleIntercept"								Type="1C"	Condition="MonochromeNotBitmapPhotometricInterpretation"
	Name="RescaleSlope"									Type="1C"	Condition="MonochromeNotBitmapPhotometricInterpretation"
	Name="RescaleType"									Type="1C"	StringDefinedTerms="RescaleTypeUnspecified"	Condition="MonochromeNotBitmapPhotometricInterpretation"
	Name="FrameIncrementPointer"						Type="1C"	Condition="NumberOfFramesGreaterThanOne"
	Name="NominalScannedPixelSpacing"					Type="1C"	Condition="ConversionTypeDigitizedFilm"	mbpo="true" NotZeroError=""
	Verify="NominalScannedPixelSpacing"								Condition="NominalScannedPixelSpacingPresentAndConversionTypeNotDigitizedFilmScannedDocumentScannedImage" ThenErrorMessage="May not be present unless ConversionType is DF, SD or SI"
	InvokeMacro="BasicPixelSpacingCalibrationMacro"
	Name="DigitizingDeviceTransportDirection"			Type="3"	StringEnumValues="TransportDirection"
	Name="RotationOfScannedFilm"						Type="3"
ModuleEnd

Module="SCMultiFrameVector"
	Name="FrameTimeVector"								Type="1C"	Condition="FrameIncrementPointerContainsFrameTimeVector"
	Name="PageNumberVector"								Type="1C"	Condition="FrameIncrementPointerContainsPageNumberVector"
	Name="FrameLabelVector"								Type="1C"	Condition="FrameIncrementPointerContainsFrameLabelVector"
	Name="FramePrimaryAngleVector"						Type="1C"	Condition="FrameIncrementPointerContainsFramePrimaryAngleVector"
	Name="FrameSecondaryAngleVector"					Type="1C"	Condition="FrameIncrementPointerContainsFrameSecondaryAngleVector"
	Name="SliceLocationVector"							Type="1C"	Condition="FrameIncrementPointerContainsSliceLocationVector"
	Name="DisplayWindowLabelVector"						Type="1C"	Condition="FrameIncrementPointerContainsDisplayWindowLabelVector"
ModuleEnd

Module="MultiFrameFunctionalGroupsForMFSC"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequenceAndPlanePositionSequenceOrPlaneOrientationSequencePresent"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequenceAndPixelMeasuresSequenceOrPlaneOrientationSequencePresent"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequenceAndPixelMeasuresSequenceOrPlanePositionSequencePresent"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequenceAndPlanePositionSequenceOrPlaneOrientationSequencePresent"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequenceAndPixelMeasuresSequenceOrPlaneOrientationSequencePresent"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequenceAndPixelMeasuresSequenceOrPlanePositionSequencePresent"
	SequenceEnd
ModuleEnd

Module="OverlayIdentification"
	Name="OverlayNumber"								Type="2"
	Name="OverlayDate"									Type="3"
	Name="OverlayTime"									Type="3"
	Sequence="ReferencedImageSequence"					Type="3"	VM="1-n"
		Name="ReferencedSOPClassUID"					Type="1"
		Name="ReferencedSOPInstanceUID"					Type="1"
	SequenceEnd
ModuleEnd

Module="OverlayPlane"
	Name="OverlayRows"									Type="1"	NotZeroError=""
	Name="OverlayColumns"								Type="1"	NotZeroError=""
	Name="OverlayType"									Type="1"	StringEnumValues="OverlayType"
	Name="OverlayOrigin"								Type="1"
	Name="OverlayBitsAllocated"							Type="1"	BinaryEnumValues="One"
	Name="OverlayBitPosition"							Type="1"	BinaryEnumValues="Zero"
	Name="OverlayData"									Type="1"
	Name="OverlayDescription"							Type="3"
	Name="OverlaySubtype"								Type="3"	StringDefinedTerms="OverlaySubtype"
	Name="OverlayLabel"									Type="3"
	Name="ROIArea"										Type="3"
	Name="ROIMean"										Type="3"
	Name="ROIStandardDeviation"							Type="3"
ModuleEnd

Module="MultiFrameOverlay"
	Name="NumberOfFramesInOverlay"						Type="1"
	Name="ImageFrameOrigin"								Type="3"
ModuleEnd

Module="CurveIdentification"
	Name="CurveNumber"									Type="2"
	Name="CurveDate"									Type="3"
	Name="CurveTime"									Type="3"
	Sequence="ReferencedImageSequence"					Type="3"	VM="1-n"
		Name="ReferencedSOPClassUID"					Type="1"
		Name="ReferencedSOPInstanceUID"					Type="1"
	SequenceEnd
	Sequence="ReferencedOverlaySequence"				Type="3"	VM="1-n"
		Name="ReferencedSOPClassUID"					Type="1"
		Name="ReferencedSOPInstanceUID"					Type="1"
	SequenceEnd
	Sequence="ReferencedCurveSequence"					Type="3"	VM="1-n"
		Name="ReferencedSOPClassUID"					Type="1"
		Name="ReferencedSOPInstanceUID"					Type="1"
	SequenceEnd
ModuleEnd

Module="Curve"
	Name="CurveDimensions"								Type="1"
	Name="NumberOfPoints"								Type="1"
	Name="TypeOfData"									Type="1"	StringDefinedTerms="CurveTypeOfData"
	Name="DataValueRepresentation"						Type="1"	BinaryEnumValues="CurveDataValueRepresentation"
	Name="CurveData"									Type="1"
	Name="CurveDescription"								Type="3"
	Name="AxisUnits"									Type="3"	StringDefinedTerms="CurveAxisUnits"
	Name="AxisLabels"									Type="3"
	Name="MinimumCoordinateValue"						Type="3"
	Name="MaximumCoordinateValue"						Type="3"
	Name="CurveRange"									Type="3"
	Name="CurveDataDescriptor"							Type="1C"	BinaryEnumValues="CurveDataDescriptor"	Condition="Never"
	Name="CoordinateStartValue"							Type="1C"	Condition="CurveDataDescriptorPresent"
	Name="CoordinateStepValue"							Type="1C"	Condition="CurveDataDescriptorPresent"
	Name="CurveLabel"									Type="3"
	Sequence="ReferencedOverlaySequence"				Type="3"	VM="1-n"
		Name="ReferencedSOPClassUID"					Type="1"
		Name="ReferencedSOPInstanceUID"					Type="1"
		Name="CurveReferencedOverlayGroup"				Type="1"
	SequenceEnd
ModuleEnd

Module="Audio"
	Name="AudioType"									Type="1"	BinaryEnumValues="AudioType"
	Name="AudioSampleFormat"							Type="1"	BinaryEnumValues="AudioSampleFormat"
	Name="NumberOfChannels"								Type="1"	BinaryEnumValues="NumberOfChannels"
	Name="NumberOfSamples"								Type="1"
	Name="SampleRate"									Type="1"
	Name="TotalTime"									Type="1"
	Name="AudioSampleData"								Type="1"
	Sequence="ReferencedImageSequence"					Type="3"	VM="1-n"
		Name="ReferencedSOPClassUID"					Type="1"
		Name="ReferencedSOPInstanceUID"					Type="1"
	SequenceEnd
	Name="AudioComments"
ModuleEnd

DefineMacro="ModalityLUTMacro"	InformationEntity="Frame"
	Sequence="ModalityLUTSequence"						Type="1C"	VM="1"	Condition="RescaleInterceptNotPresent"
		Name="LUTDescriptor"							Type="1"
		Verify="LUTDescriptor"										ValueSelector="2"	BinaryEnumValues="BitsAre8Or16"
		Name="LUTExplanation"							Type="3"
		Name="ModalityLUTType"							Type="1"	StringDefinedTerms="ModalityLUTType"
		Name="LUTData"									Type="1"
	SequenceEnd
	Name="RescaleIntercept"								Type="1C"	Condition="ModalityLUTSequenceNotPresent"
	Name="RescaleSlope"									Type="1C"	Condition="RescaleInterceptPresent"	NotZeroError=""
	Name="RescaleType"									Type="1C"	Condition="RescaleInterceptPresent"	StringDefinedTerms="ModalityLUTType"
	Verify="PhotometricInterpretation"					Condition="PhotometricInterpretationIsGrayscaleOrAbsent"	ElseWarningMessage="Modality LUT Module (Rescale Slope and Intercept) not appropriate for non-grayscale images" ShowValueWithMessage="true"
MacroEnd

Module="ModalityLUT"
	InvokeMacro="ModalityLUTMacro"
ModuleEnd

DefineMacro="VOILUTMacro"	InformationEntity="Frame"
	Sequence="VOILUTSequence"							Type="1C"	VM="1-n"	Condition="MonochromeAndWindowCenterNotPresent" mbpo="true"
		Name="LUTDescriptor"							Type="1"
		Verify="LUTDescriptor"										Condition="VOILUTSequenceLUTDescriptorRequiredToBe8Or16"	ValueSelector="2"	BinaryEnumValues="BitsAre8Or16"
		Name="LUTExplanation"							Type="3"
		Name="LUTData"									Type="1"
	SequenceEnd
	Name="WindowCenter"									Type="1C"	Condition="MonochromeAndVOILUTSequenceNotPresent" mbpo="true"
	Name="WindowWidth"									Type="1C"	Condition="WindowCenterPresent"	NotZeroError=""
	Verify="WindowWidth"											Condition="WindowWidthIsNegative"	ThenErrorMessage="Not permitted to be negative" ShowValueWithMessage="true"
	Verify="WindowWidth"											Condition="WindowWidthIsLessThanOneAndNotExact"	ThenErrorMessage="Not permitted to be < 1 unless VOI LUT Function is LINEAR_EXACT or SIGMOID" ShowValueWithMessage="true"
	Verify="WindowWidth"											Condition="WindowWidthIsZeroAndSigmoid"	ThenErrorMessage="Not permitted to be 0 when VOI LUT Function is SIGMOID" ShowValueWithMessage="true"
	Name="WindowCenterWidthExplanation"					Type="3"
	Name="VOILUTFunction"								Type="3"	StringDefinedTerms="VOILUTFunction"
	Verify="PhotometricInterpretation"					Condition="PhotometricInterpretationIsGrayscaleOrAbsent"	ElseWarningMessage="VOI LUT Module (Window Center and Width) not appropriate for non-grayscale images" ShowValueWithMessage="true"
ModuleEnd

Module="VOILUT"
	InvokeMacro="VOILUTMacro"
ModuleEnd

Module="LUTIdentification"
	Name="LUTNumber"									Type="2"
	Sequence="ReferencedImageSequence"					Type="3"	VM="1-n"
		Name="ReferencedSOPClassUID"					Type="1"
		Name="ReferencedSOPInstanceUID"					Type="1"
	SequenceEnd
ModuleEnd

DefineMacro="DigitalSignaturesMacro"	InformationEntity="Instance"
	Sequence="MACParametersSequence"					Type="3"	VM="1-n"
		Name="MACIDNumber"								Type="1"
		Name="MACCalculationTransferSyntaxUID"			Type="1"
		Name="MACAlgorithm"								Type="1"	StringDefinedTerms="MACAlgorithm"
		Name="DataElementsSigned"						Type="1"
	SequenceEnd
	Sequence="DigitalSignaturesSequence"				Type="3"	VM="1-n"
		Name="MACIDNumber"								Type="1"
		Name="DigitalSignatureUID"						Type="1"
		Name="DigitalSignatureDateTime"					Type="1"
		Name="CertificateType"							Type="1"	StringDefinedTerms="CertificateType"
		Name="CertificateOfSigner"						Type="1"
		Name="Signature"								Type="1"
		Name="CertifiedTimestampType"					Type="1C"	Condition="CertifiedTimestampIsPresent"	StringDefinedTerms="CertifiedTimestampType"
		Name="CertifiedTimestamp"						Type="3"
		Sequence="DigitalSignaturePurposeCodeSequence"	Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="7007"
		SequenceEnd
	SequenceEnd
MacroEnd

Module="SOPCommon"
	Name="SOPClassUID"									Type="1"
	Name="SOPInstanceUID"								Type="1"
	Name="SpecificCharacterSet"							Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
	Name="InstanceCreationDate"							Type="3"
	Name="InstanceCreationTime"							Type="3"
	Name="InstanceCoercionDateTime"						Type="3"
	Name="InstanceCreatorUID"							Type="3"
	Name="RelatedGeneralSOPClassUID"					Type="3"
	Name="OriginalSpecializedSOPClassUID"				Type="3"
	Sequence="CodingSchemeIdentificationSequence"		Type="3"	VM="1-n"
		Name="CodingSchemeDesignator"					Type="1"	StringDefinedTerms="MiscellaneousCodingSchemeDesignators"
		Name="CodingSchemeRegistry"						Type="1C"	NoCondition=""	StringDefinedTerms="CodingSchemeRegistries"
		Name="CodingSchemeUID"							Type="1C"	NoCondition=""	StringDefinedTerms="MiscellaneousCodingSchemeUIDs"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsACR"				StringEnumValues="CodingSchemeUIDForACR"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsASTMSigpurpose"	StringEnumValues="CodingSchemeUIDForASTMSigpurpose"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsC4"				StringEnumValues="CodingSchemeUIDForC4"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsC5"				StringEnumValues="CodingSchemeUIDForC5"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsCD2"				StringEnumValues="CodingSchemeUIDForCD2"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsCTV3"			StringEnumValues="CodingSchemeUIDForCTV3"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsDCM"				StringEnumValues="CodingSchemeUIDForDCM"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsDCMUID"			StringEnumValues="CodingSchemeUIDForDCMUID"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsHPC"				StringEnumValues="CodingSchemeUIDForHPC"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsI10"				StringEnumValues="CodingSchemeUIDForI10"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsI10P"			StringEnumValues="CodingSchemeUIDForI10P"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsI9"				StringEnumValues="CodingSchemeUIDForI9"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsI9C"				StringEnumValues="CodingSchemeUIDForI9C"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsISO3166_1"		StringEnumValues="CodingSchemeUIDForISO3166_1"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsISO639_1"		StringEnumValues="CodingSchemeUIDForISO639_1"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsISO639_2"		StringEnumValues="CodingSchemeUIDForISO639_2"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsLN"				StringEnumValues="CodingSchemeUIDForLN"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsPOS"				StringEnumValues="CodingSchemeUIDForPOS"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsRFC3066"			StringEnumValues="CodingSchemeUIDForRFC3066"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsSNM3"			StringEnumValues="CodingSchemeUIDForSNM3"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsSCT"				StringEnumValues="CodingSchemeUIDForSCT"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsSRT"				StringEnumValues="CodingSchemeUIDForSRT"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsUCUM"			StringEnumValues="CodingSchemeUIDForUCUM"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsUMLS"			StringEnumValues="CodingSchemeUIDForUMLS"
		Verify="CodingSchemeUID"						Condition="CodingSchemeDesignatorIsUPC"				StringEnumValues="CodingSchemeUIDForUPC"
		Name="CodingSchemeExternalID"					Type="2C"	NoCondition=""
		Name="CodingSchemeName"							Type="3"
		Name="CodingSchemeVersion"						Type="3"
		Name="CodingSchemeResponsibleOrganization"		Type="3"
		Sequence="CodingSchemeResourcesSequence"		Type="3"	VM="1-n"
			Name="CodingSchemeURLType"					Type="1"	StringDefinedTerms="CodingSchemeURLType"
			Name="CodingSchemeURL"						Type="1"
		SequenceEnd
	SequenceEnd
	Sequence="ContextGroupIdentificationSequence"		Type="3"	VM="1-n"
		Name="ContextIdentifier"						Type="1"
		Name="ContextUID"								Type="3"
		Name="MappingResource"							Type="1"	StringDefinedTerms="MappingResources"
		Name="ContextGroupVersion"						Type="1"
	SequenceEnd
	Sequence="MappingResourceIdentificationSequence"	Type="3"	VM="1-n"
		Name="MappingResource"							Type="1"	StringDefinedTerms="MappingResources"
		Name="MappingResourceUID"						Type="3"	StringDefinedTerms="MappingResourceUIDs"
		Name="MappingResourceName"						Type="3"	StringDefinedTerms="MappingResourceNames"
	SequenceEnd
	Name="TimezoneOffsetFromUTC"						Type="3"
	Sequence="ContributingEquipmentSequence"			Type="3"	VM="1-n"
		Sequence="PurposeOfReferenceCodeSequence"		Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"							DefinedContextID="7005"
		SequenceEnd
		Name="Manufacturer"								Type="1"
		Name="InstitutionName"							Type="3"
		Name="InstitutionAddress"						Type="3"
		Name="StationName"								Type="3"
		Name="InstitutionalDepartmentName"				Type="3"
		Sequence="InstitutionalDepartmentTypeCodeSequence"	Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"								BaselineContextID="7030"
		SequenceEnd
		Name="OperatorsName"							Type="3"
		Sequence="OperatorIdentificationSequence"		Type="3"	VM="1-n"
			InvokeMacro="PersonIdentificationMacro"
		SequenceEnd
		Name="ManufacturerModelName"					Type="3"
		Name="DeviceSerialNumber"						Type="3"
		Name="SoftwareVersions"							Type="3"
		Name="SpatialResolution"						Type="3"
		Name="DateOfLastCalibration"					Type="3"
		Name="TimeOfLastCalibration"					Type="3"
		Name="ContributionDateTime"						Type="3"
		Name="ContributionDescription"					Type="3"
	SequenceEnd
	Name="InstanceNumber"								Type="3"
	Name="SOPInstanceStatus"							Type="3"
	Name="SOPAuthorizationDateTime"						Type="3"
	Name="SOPAuthorizationComment"						Type="3"
	Name="AuthorizationEquipmentCertificationNumber"	Type="3"
	InvokeMacro="DigitalSignaturesMacro"
	Sequence="EncryptedAttributesSequence"				Type="1C"	VM="1-n"	NoCondition=""
		Name="EncryptedContentTransferSyntaxUID"		Type="1"
		Name="EncryptedContent"							Type="1"
	SequenceEnd
	Sequence="OriginalAttributesSequence"				Type="3"	VM="1-n"
		Name="SourceOfPreviousValues"					Type="2"
		Name="AttributeModificationDateTime"			Type="1"
		Name="ModifyingSystem"							Type="1"
		Name="ReasonForTheAttributeModification"		Type="1"
		Sequence="ModifiedAttributesSequence"			Type="1"	VM="1"
		SequenceEnd
		Sequence="NonconformingModifiedAttributesSequence"	Type="3"	VM="1"
			InvokeMacro="SelectorAttributeMacro"
			Name="NonconformingDataElementValue"		Type="1"
		SequenceEnd
	SequenceEnd
	Sequence="HL7StructuredDocumentReferenceSequence"	Type="1C"	VM="1-n"	NoCondition=""
		Name="ReferencedSOPClassUID"					Type="1"
		Name="ReferencedSOPInstanceUID"					Type="1"
		Name="HL7InstanceIdentifier"					Type="1"
		Name="RetrieveURI"								Type="1"
	SequenceEnd
	Name="LongitudinalTemporalInformationModified"		Type="3"	StringEnumValues="LongitudinalTemporalInformationModified"
	Name="QueryRetrieveView"							Type="1C"	NoCondition=""	StringEnumValues="QueryRetrieveView"
	Sequence="ConversionSourceAttributesSequence"		Type="1C"	VM="1-n"	NoCondition=""
		InvokeMacro="ImageSOPInstanceReferenceMacro"
	SequenceEnd
	Name="ContentQualification"							Type="3"	StringEnumValues="ContentQualification"
	Sequence="PrivateDataElementCharacteristicsSequence"	Type="3"	VM="1-n"
		Name="PrivateGroupReference"						Type="1"
		Name="PrivateCreatorReference"						Type="1"
		Sequence="PrivateDataElementDefinitionSequence"		Type="3"	VM="1-n"
			Name="PrivateDataElement"						Type="1"
			Name="PrivateDataElementValueMultiplicity"		Type="1"
			Name="PrivateDataElementValueRepresentation"	Type="1"	StringEnumValues="ValueRepresentations"
			Name="PrivateDataElementNumberOfItems"			Type="1C"	Condition="PrivateDataElementValueRepresentationIsSequence"
			Name="PrivateDataElementKeyword"				Type="1"
			Name="PrivateDataElementName"					Type="1"
			Name="PrivateDataElementDescription"			Type="3"
			Name="PrivateDataElementEncoding"				Type="3"
			Name="RetrieveURI"								Type="3"
		SequenceEnd
		Name="BlockIdentifyingInformationStatus"			Type="1"	StringEnumValues="BlockIdentifyingInformationStatus"
		Name="NonidentifyingPrivateElements"				Type="1C"	Condition="BlockIdentifyingInformationStatusIsMIXED"
		Sequence="DeidentificationActionSequence"			Type="3"	VM="1-n"
			Name="IdentifyingPrivateElements"				Type="1"
			Name="DeidentificationAction"					Type="1"	StringEnumValues="DeidentificationAction"
		SequenceEnd
	SequenceEnd
	Name="InstanceOriginStatus"							Type="3"	StringEnumValues="InstanceOriginStatus"
	Name="BarcodeValue"									Type="3"
ModuleEnd

Module="FrameExtraction"
	Sequence="FrameExtractionSequence"					Type="1"	VM="1-n"
		Name="MultiFrameSourceSOPInstanceUID"			Type="1"
		Name="SimpleFrameList"							Type="1C"	Condition="NeedSimpleFrameListInFrameExtractionModule"
		Name="CalculatedFrameList"						Type="1C"	Condition="NeedCalculatedFrameListInFrameExtractionModule"
		Name="TimeRange"								Type="1C"	Condition="NeedTimeRangeInFrameExtractionModule"
	SequenceEnd
ModuleEnd

Module="MultiframeSingleBitSCImagePseudo"
	Name="SamplesPerPixel"				Type="1"	BinaryEnumValues="One"
	Name="PhotometricInterpretation"	Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"				Type="1"	BinaryEnumValues="One"
	Name="BitsStored"					Type="1"	BinaryEnumValues="One"
	Name="HighBit"						Type="1"	BinaryEnumValues="Zero"
	Name="PixelRepresentation"			Type="1"	BinaryEnumValues="Zero"
	Name="PlanarConfiguration"			Type="1C"	BinaryEnumValues="PlanarConfiguration"	Condition="Never"
ModuleEnd

Module="MultiframeGrayscaleByteSCImagePseudo"
	Name="SamplesPerPixel"				Type="1"	BinaryEnumValues="One"
	Name="PhotometricInterpretation"	Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"				Type="1"	BinaryEnumValues="BitsAre8"
	Name="BitsStored"					Type="1"	BinaryEnumValues="BitsAre8"
	Name="HighBit"						Type="1"	BinaryEnumValues="BitsAre7"
	Name="PixelRepresentation"			Type="1"	BinaryEnumValues="Zero"
	Name="PlanarConfiguration"			Type="1C"	BinaryEnumValues="PlanarConfiguration"	Condition="Never"
 	Name="RescaleIntercept"				Type="1"	BinaryEnumValues="Zero"
 	Name="RescaleSlope"					Type="1"	BinaryEnumValues="One"
 	Name="RescaleType"					Type="1"	StringEnumValues="RescaleTypeUnspecified"
ModuleEnd

Module="MultiframeGrayscaleWordSCImagePseudo"
	Name="SamplesPerPixel"				Type="1"	BinaryEnumValues="One"
	Name="PhotometricInterpretation"	Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"				Type="1"	BinaryEnumValues="BitsAre16"
	Name="BitsStored"					Type="1"	BinaryEnumValues="BitsAre9To16"
	Name="HighBit"						Type="1"	BinaryEnumValues="BitsAre8To15"	# :( should be one less than bits stored
	Name="PixelRepresentation"			Type="1"	BinaryEnumValues="Zero"
	Name="PlanarConfiguration"			Type="1C"	BinaryEnumValues="PlanarConfiguration"	Condition="Never"
ModuleEnd

Module="MultiframeTrueColorSCImagePseudo"

	Name="SamplesPerPixel"				Type="1"	BinaryEnumValues="Three"
	Name="PhotometricInterpretation"	Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2OrRGBOrYBR_FULL_422OrYBR_RCTOrYBR_ICTOrYBR_PARTIAL_420"
	Verify="PhotometricInterpretation"				Condition="JPEGTransferSyntaxButNotYBR_FULL_422"			ThenErrorMessage="JPEG transfer syntax is required to have Photometric Interpretation of YBR_FULL422" ShowValueWithMessage="true"
	Verify="PhotometricInterpretation"				Condition="JPEG2000LosslessTransferSyntaxButNotYBR_RCT"		ThenErrorMessage="JPEG 2000 reversible transfer syntax is required to have Photometric Interpretation of YBR_RCT" ShowValueWithMessage="true"
	Verify="PhotometricInterpretation"				Condition="JPEG2000TransferSyntaxButNotYBR_RCTOrYBR_ICT"	ThenErrorMessage="JPEG 2000 transfer syntax is required to have Photometric Interpretation of YBR_RCT or YBR_ICT" ShowValueWithMessage="true"
	# MPEG2TransferSyntaxButNotYBR_PARTIAL_420 is generic too ImagePixelMacro and not repeated here (PS 3.5 requirement)
	Name="BitsAllocated"				Type="1"	BinaryEnumValues="BitsAre8"
	Name="BitsStored"					Type="1"	BinaryEnumValues="BitsAre8"
	Name="HighBit"						Type="1"	BinaryEnumValues="BitsAre7"
	Name="PixelRepresentation"			Type="1"	BinaryEnumValues="Zero"
	Name="PlanarConfiguration"			Type="1"	BinaryEnumValues="Zero"		# only needs to be 0 for RGB

ModuleEnd

Module="CommonInstanceReference"
	# do not use SeriesAndInstanceReferenceMacro, but conditional inclusion instead, per CP 926
	# cannot actually check whether instances that are referenced are in this study or another study
	# may be present otherwise because cannot check whether or not both sequences are needed
	Sequence="ReferencedSeriesSequence"								Type="1C"	VM="1-n"	Condition="InstancesAreReferencedAndStudiesContainingOtherReferencedInstancesSequenceAbsent" mbpo="true"
		Name="SeriesInstanceUID"									Type="1"
		Verify="StudyInstanceUID"															Condition="StudyInstanceUIDIsPresent"	ThenErrorMessage="StudyInstanceUID should not be present in ReferencedSeriesSequence in CommonInstanceReference Module - use StudiesContainingOtherReferencedInstancesSequence if not the same Study"
		Sequence="ReferencedInstanceSequence"						Type="1"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="StudiesContainingOtherReferencedInstancesSequence"	Type="1C"	VM="1-n"	Condition="InstancesAreReferencedAndReferencedSeriesSequenceAbsent" mbpo="true"
		Name="StudyInstanceUID"										Type="1"
		InvokeMacro="SeriesAndInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="SegmentationSeries"
	Name="Modality"												Type="1"	StringEnumValues="SEGModality"
	Name="SeriesNumber"											Type="1"
	Sequence="ReferencedPerformedProcedureStepSequence"			Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="SegmentationImage"
	Name="ImageType"										Type="1"	VM="2"
	Verify="ImageType"													ValueSelector="0"	StringEnumValues="ImageType1DerivedOnly"
	Verify="ImageType"													ValueSelector="1"	StringEnumValues="ImageType2PrimaryOnly"
	InvokeMacro="ContentIdentificationMacro"
	Name="SamplesPerPixel"									Type="1"	BinaryEnumValues="One"
	Name="PhotometricInterpretation"						Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="PixelRepresentation"								Type="1"	BinaryEnumValues="Zero"
	Name="BitsAllocated"									Type="1"
	Verify="BitsAllocated"												Condition="SegmentationTypeIsBinary"	BinaryEnumValues="One"
	Verify="BitsAllocated"												Condition="SegmentationTypeIsNotBinary"	BinaryEnumValues="BitsAre8"
	Name="BitsStored"										Type="1"
	Verify="BitsStored"													Condition="SegmentationTypeIsBinary"	BinaryEnumValues="One"
	Verify="BitsStored"													Condition="SegmentationTypeIsNotBinary"	BinaryEnumValues="BitsAre8"
	Name="HighBit"											Type="1"
	Verify="HighBit"													Condition="SegmentationTypeIsBinary"	BinaryEnumValues="Zero"
	Verify="HighBit"													Condition="SegmentationTypeIsNotBinary"	BinaryEnumValues="BitsAre7"
	Name="PlanarConfiguration"								Type="1C"	BinaryEnumValues="PlanarConfiguration"	Condition="Never"
	Name="LossyImageCompression"							Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"						Type="1C"	NoCondition=""
	Name="LossyImageCompressionMethod"						Type="1C"	NoCondition=""
	Verify="LossyImageCompressionMethod"								Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="SegmentationType"									Type="1"	StringEnumValues="SegmentationType"
	Name="SegmentationFractionalType"						Type="1C"	Condition="SegmentationTypeIsFractional"	StringEnumValues="SegmentationFractionalType"
	Name="MaximumFractionalValue"							Type="1C"	Condition="SegmentationTypeIsFractional"
	# should verify than 0 < MaximumFractionalValue < 256 :(
	Name="SegmentsOverlap"									Type="3"	StringEnumValues="YesNoFullUndefined"
	Sequence="SegmentSequence"								Type="1"	VM="1-n"
		InvokeMacro="SegmentDescriptionMacro"
		Name="SegmentAlgorithmName"							Type="1C"	Condition="SegmentAlgorithmTypeIsNotManual"
		Sequence="SegmentationAlgorithmIdentificationSequence"	Type="3"	VM="1"
			InvokeMacro="AlgorithmIdentificationMacro"									BaselineContextID="7162"
		SequenceEnd
		Name="RecommendedDisplayGrayscaleValue"				Type="3"
		Name="RecommendedDisplayCIELabValue"				Type="3"
	SequenceEnd
ModuleEnd

DefineMacro="SegmentDescriptionMacro" InformationEntity="Instance"
	Name="SegmentNumber"										Type="1"	NotZeroError=""
	Name="SegmentLabel"											Type="1"
	Name="SegmentDescription"									Type="3"
	Name="SegmentAlgorithmType"									Type="1"	StringEnumValues="SegmentAlgorithmType"
	InvokeMacro="GeneralAnatomyOptionalMacro"
	Sequence="SegmentedPropertyCategoryCodeSequence"			Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"										BaselineContextID="7150"
	SequenceEnd
	Sequence="SegmentedPropertyTypeCodeSequence"				Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"										BaselineContextID="7151"
		Sequence="SegmentedPropertyTypeModifierCodeSequence"	Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"									BaselineContextID="244"
		SequenceEnd
	SequenceEnd
	Name="TrackingID"											Type="1C"	Condition="TrackingUIDIsPresent"
	Name="TrackingUID"											Type="1C"	Condition="TrackingIDIsPresent"
	Sequence="DefinitionSourceSequence"							Type="3"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
		Name="ReferencedROINumber"								Type="1C"	Condition="ReferencedSOPClassUIDIsRTStructureSetStorage"
	SequenceEnd
MacroEnd

DefineMacro="SegmentationMacro" InformationEntity="FunctionalGroup"
	Sequence="SegmentIdentificationSequence"				Type="1"	VM="1"
		Name="ReferencedSegmentNumber"						Type="1"	VM="1"
	SequenceEnd
MacroEnd

Module="SurfaceSegmentation"
	InvokeMacro="ContentIdentificationMacro"
	Name="ContentDate"															Type="1"
	Name="ContentTime"															Type="1"
	Sequence="SegmentSequence"													Type="1"	VM="1-n"
		InvokeMacro="SegmentDescriptionMacro"
		Name="SurfaceCount"														Type="1"	NotZeroError="" 
		Sequence="ReferencedSurfaceSequence"									Type="1"	VM="1-n"				# should check that number of items equals SurfaceCount :(
			Name="ReferencedSurfaceNumber"										Type="1"	VM="1" 	NotZeroError=""	# should check that SurfaceNumber exists in SurfaceSequence :(
			Sequence="SegmentSurfaceGenerationAlgorithmIdentificationSequence"	Type="1"	VM="1"
				InvokeMacro="AlgorithmIdentificationMacro"									BaselineContextID="7162"
			SequenceEnd
			Sequence="SegmentSurfaceSourceInstanceSequence"						Type="2"	VM="0-n"
				InvokeMacro="ImageSOPInstanceReferenceMacro"
			SequenceEnd
		SequenceEnd
	SequenceEnd
ModuleEnd

DefineMacro="PointsMacro" InformationEntity="Surface"
	Name="NumberOfSurfacePoints"												Type="1"	NotZeroError=""
	Name="PointCoordinatesData"													Type="1"
	Name="PointPositionAccuracy"												Type="3"
	Name="MeanPointDistance"													Type="3"
	Name="MaximumPointDistance"													Type="3"
	Name="PointsBoundingBoxCoordinates"											Type="3"
	Name="AxisOfRotation"														Type="3"
	Name="CenterOfRotation"														Type="1C"	Condition="AxisOfRotationIsPresent" mbpo="true"
MacroEnd

DefineMacro="VectorsMacro" InformationEntity="Surface"
	Name="NumberOfVectors"														Type="1"	NotZeroError=""
	Name="VectorDimensionality"													Type="1"	NotZeroError=""
	Name="VectorAccuracy"														Type="3"
	Name="VectorCoordinateData"													Type="1"
MacroEnd

DefineMacro="SurfaceMeshPrimitivesMacro" InformationEntity="Surface"
	Name="LongVertexPointIndexList"												Type="2"
	Name="LongEdgePointIndexList"												Type="2"						# should check has 2n values :(
	Name="LongTrianglePointIndexList"											Type="2"						# should check has 3n values :(
	Sequence="TriangleStripSequence"											Type="2"	VM="0-n"
		Name="LongPrimitivePointIndexList"										Type="1"
	SequenceEnd
	Sequence="TriangleFanSequence"												Type="2"	VM="0-n"
		Name="LongPrimitivePointIndexList"										Type="1"
	SequenceEnd
	Sequence="LineSequence"														Type="2"	VM="0-n"
		Name="LongPrimitivePointIndexList"										Type="1"
	SequenceEnd
	Sequence="FacetSequence"													Type="2"	VM="0-n"
		Name="LongPrimitivePointIndexList"										Type="1"
	SequenceEnd
MacroEnd

Module="SurfaceMesh"
	Name="NumberOfSurfaces"														Type="1"	NotZeroError=""
	Sequence="SurfaceSequence"													Type="1"	VM="1-n"				# should check that number of items equals NumberOfSurfaces :(
		Name="SurfaceNumber"													Type="1"	NotZeroError=""			# should check that starts at a value of 1, and increases monotonically by 1 :(
		Name="SurfaceComments"													Type="3"
		Sequence="SegmentedPropertyCategoryCodeSequence"						Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"													BaselineContextID="7150"
		SequenceEnd
		Sequence="SegmentedPropertyTypeCodeSequence"							Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"													BaselineContextID="7151"
		SequenceEnd
		Name="SurfaceProcessing"												Type="2"	StringEnumValues="YesNoFull"
		Name="SurfaceProcessingRatio"											Type="2C"	Condition="SurfaceProcessingIsYes"
		Name="SurfaceProcessingDescription"										Type="3"
		Sequence="SurfaceProcessingAlgorithmIdentificationSequence"				Type="2C"	VM="0-n"	Condition="SurfaceProcessingIsYes"
			InvokeMacro="AlgorithmIdentificationMacro"										BaselineContextID="7162"
		SequenceEnd
		Name="RecommendedDisplayGrayscaleValue"									Type="1"
		Name="RecommendedDisplayCIELabValue"									Type="1"
		Name="RecommendedPresentationOpacity"									Type="1"
		Name="RecommendedPresentationType"										Type="1"	StringDefinedTerms="RecommendedPresentationType"
		Name="RecommendedPointRadius"											Type="3"
		Name="RecommendedLineThickness"											Type="3"
		Name="FiniteVolume"														Type="1"	StringEnumValues="YesNoFullUnknown"
		Name="Manifold"															Type="1"	StringEnumValues="YesNoFullUnknown"
		Sequence="SurfacePointsSequence"										Type="1"	VM="1"
			InvokeMacro="PointsMacro"
		SequenceEnd
		Sequence="SurfacePointsNormalsSequence"									Type="2"	VM="0-1"
			InvokeMacro="VectorsMacro"																				# should check that NumberOfVectors equals NumberOfSurfacePoints in SurfacePointsSequence, and VectorDimensionality equals 3 :(
		SequenceEnd
		Sequence="SurfaceMeshPrimitivesSequence"								Type="1"	VM="1"
			InvokeMacro="SurfaceMeshPrimitivesMacro"																# should check that indices do not exceed NumberOfSurfacePoints in SurfacePointsSequence :(
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="MultiFrameFunctionalGroupsForSegmentation"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageSequenceNotInPerFrameFunctionalGroupSequenceAndPixelMeasuresPlanePositionPlaneOrientationNotPresentInEitherMBPO"
		InvokeMacro="SegmentationMacro"			Condition="SegmentIdentificationSequenceNotInPerFrameFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequenceAndDerivationImageMacroNotPresentInEitherMBPO"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageSequenceNotInSharedFunctionalGroupSequenceAndPixelMeasuresPlanePositionPlaneOrientationNotPresentInEitherMBPO"
		InvokeMacro="SegmentationMacro"			Condition="SegmentIdentificationSequenceNotInSharedFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="SpatialRegistrationSeries"
	Name="Modality"												Type="1"	StringEnumValues="REGModality"
ModuleEnd

Module="SpatialRegistration"
	Name="ContentDate"											Type="1"
	Name="ContentTime"											Type="1"
	InvokeMacro="ContentIdentificationMacro"
	Sequence="RegistrationSequence"								Type="1"	VM="1-n"
		Name="FrameOfReferenceUID"								Type="1C"	Condition="ReferencedImageSequenceNotPresent" mbpo="true"
		Sequence="ReferencedImageSequence"						Type="1C"	VM="1-n"	Condition="FrameOfReferenceUIDNotPresent" mbpo="true"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="MatrixRegistrationSequence"					Type="1"	VM="1"
			Name="FrameOfReferenceTransformationComment"		Type="3"
			Sequence="RegistrationTypeCodeSequence"				Type="2"	VM="0-1"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Sequence="MatrixSequence"							Type="1"	VM="1-n"
				Name="FrameOfReferenceTransformationMatrix"		Type="1"
				Name="FrameOfReferenceTransformationMatrixType"	Type="1"	StringEnumValues="FrameOfReferenceTransformationMatrixType"
			SequenceEnd
		SequenceEnd
		Sequence="UsedFiducialsSequence"						Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
			Name="FiducialUID"									Type="1"
		SequenceEnd
		Sequence="UsedSegmentsSequence"							Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
			Name="ReferencedSegmentNumber"						Type="1"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="DeformableSpatialRegistration"
	Name="ContentDate"											Type="1"
	Name="ContentTime"											Type="1"
	InvokeMacro="ContentIdentificationMacro"
	Sequence="DeformableRegistrationSequence"					Type="1"	VM="1-n"
		Name="SourceFrameOfReferenceUID"						Type="1"
		Sequence="ReferencedImageSequence"						Type="1C"	VM="1-n"	NoCondition=""
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
		Name="FrameOfReferenceTransformationComment"			Type="3"
		Sequence="RegistrationTypeCodeSequence"					Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="PreDeformationMatrixRegistrationSequence"		Type="1C"	VM="1"	NoCondition=""
			Name="FrameOfReferenceTransformationMatrix"			Type="1"
			Name="FrameOfReferenceTransformationMatrixType"		Type="1"	StringEnumValues="FrameOfReferenceTransformationMatrixType"
		SequenceEnd
		Sequence="PostDeformationMatrixRegistrationSequence"	Type="1C"	VM="1"	NoCondition=""
			Name="FrameOfReferenceTransformationMatrix"			Type="1"
			Name="FrameOfReferenceTransformationMatrixType"		Type="1"	StringDefinedTerms="FrameOfReferenceTransformationMatrixType"
		SequenceEnd
		Sequence="DeformableRegistrationGridSequence"			Type="1C"	VM="1"	NoCondition=""
			Name="ImageOrientationPatient"						Type="1"
			Name="ImagePositionPatient"							Type="1"
			Name="GridDimensions"								Type="1"
			Name="GridResolution"								Type="1"
			Name="VectorGridData"								Type="1"
		SequenceEnd
		Sequence="UsedFiducialsSequence"						Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
			Name="FiducialUID"									Type="1"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="SpatialFiducialsSeries"
	Name="Modality"												Type="1"	StringEnumValues="FIDModality"
ModuleEnd

Module="SpatialFiducials"
	Name="ContentDate"											Type="1"
	Name="ContentTime"											Type="1"
	InvokeMacro="ContentIdentificationMacro"
	Sequence="FiducialSetSequence"								Type="1"	VM="1-n"
		Name="FrameOfReferenceUID"								Type="1C"	Condition="ReferencedImageSequenceNotPresent"
		Sequence="ReferencedImageSequence"						Type="1C"	VM="1-n"	Condition="FrameOfReferenceUIDNotPresent"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="FiducialSequence"								Type="1"	VM="1-n"
			Name="FiducialIdentifier"							Type="1"
			Sequence="FiducialsPropertyCategoryCodeSequence"	Type="3"	VM="1"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Sequence="FiducialIdentifierCodeSequence"			Type="1C"	VM="1"	Condition="FiducialIdentifierNotPresent"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Name="FiducialUID"									Type="3"
			Name="FiducialDescription"							Type="3"
			Name="ShapeType"									Type="1"	StringDefinedTerms="FiducialShapeType"
			Name="NumberOfContourPoints"						Type="1C"	Condition="ContourDataIsPresent"	NotZeroError=""
			Name="ContourData"									Type="1C"	Condition="FrameOfReferenceUIDIsPresentInParent"
			Name="ContourUncertaintyRadius"						Type="3"
			Sequence="GraphicCoordinatesDataSequence"			Type="1C"	VM="1-n"	Condition="ContourDataNotPresent"
				Name="GraphicData"								Type="1"
				Sequence="ReferencedImageSequence"				Type="1"	VM="1"
					InvokeMacro="ImageSOPInstanceReferenceMacro"
				SequenceEnd
			SequenceEnd
			Sequence="DefinitionSourceSequence"					Type="3"	VM="1"
				InvokeMacro="SOPInstanceReferenceMacro"
				Name="ReferencedROINumber"						Type="1C"	Condition="ReferencedSOPClassUIDIsRTStructureSetStorage"
			SequenceEnd
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="EncapsulatedDocumentSeries"
	Name="Modality"												Type="1"	StringDefinedTerms="Modality"
	Name="SeriesInstanceUID"									Type="1"
	Name="SeriesNumber"											Type="1"
	Sequence="ReferencedPerformedProcedureStepSequence"			Type="3"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Name="ProtocolName"											Type="3"
	Name="SeriesDescription"									Type="3"
	Sequence="SeriesDescriptionCodeSequence"					Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="RequestAttributesSequence"						Type="3"	VM="1-n"
		InvokeMacro="RequestAttributesMacro"
	SequenceEnd
	InvokeMacro="PerformedProcedureStepSummaryMacro"
ModuleEnd

Module="EncapsulatedDocument"
	Name="InstanceNumber"										Type="1"
	Name="ContentDate"											Type="2"
	Name="ContentTime"											Type="2"
	Name="AcquisitionDateTime"									Type="2"
	Name="BurnedInAnnotation"									Type="1"	StringEnumValues="YesNoFull"
	Name="RecognizableVisualFeatures"							Type="3"	StringEnumValues="YesNoFull"
	Sequence="SourceInstanceSequence"							Type="1C"	VM="1-n"	NoCondition=""
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"				Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"									DefinedContextID="7060"
		SequenceEnd
	SequenceEnd
	Name="DocumentTitle"										Type="2"
	Sequence="ConceptNameCodeSequence"							Type="2"	VM="0-1"
		InvokeMacro="CodeSequenceMacro"										BaselineContextID="7020"	# or 7061 if Modality is M3D ... not checke anyway :(
	SequenceEnd
	Name="VerificationFlag"										Type="3"	StringEnumValues="VerificationFlag"
	Name="HL7InstanceIdentifier"								Type="1C"	Condition="EncapsulatedCDAInstance"
	Sequence="PredecessorDocumentsSequence"						Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="IdenticalDocumentsSequence"						Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Name="MIMETypeOfEncapsulatedDocument"						Type="1"
	Name="ListOfMIMETypes"										Type="1C"	NoCondition=""
	Name="ImageLaterality"										Type="3"	StringEnumValues="ImageLaterality"
	Name="EncapsulatedDocument"									Type="1"
	Name="EncapsulatedDocumentLength"							Type="3"
ModuleEnd

Module="EncapsulatedDocumentPDFPseudo"
	Name="MIMETypeOfEncapsulatedDocument"						Type="1"	StringEnumValues="MIMETypeApplicationPDF"
ModuleEnd

Module="EncapsulatedDocumentCDAPseudo"
	Name="MIMETypeOfEncapsulatedDocument"						Type="1"	StringEnumValues="MIMETypeApplicationCDA"
ModuleEnd

Module="EncapsulatedDocumentSTLPseudo"
	Name="MIMETypeOfEncapsulatedDocument"						Type="1"	StringEnumValues="MIMETypeApplicationSTL"
ModuleEnd

Module="EncapsulatedDocumentSTLSeriesPseudo"
	Name="Modality"												Type="1"	StringEnumValues="M3DModality"
ModuleEnd

Module="CheckSingleFramePseudo"
	Name="NumberOfFrames"										Type="3"	DoNotSetUsed="" BinaryEnumValues="One"
ModuleEnd

Module="RealWorldValueMappingSeries"
	Name="Modality"												Type="1"	StringDefinedTerms="RealWorldValueMappingModality"
ModuleEnd

Module="RealWorldValueMapping"
	Name="ContentDate"											Type="1"
	Name="ContentTime"											Type="1"
	InvokeMacro="ContentIdentificationMacro"
	Sequence="ReferencedImageRealWorldValueMappingSequence"		Type="1"	VM="1-n"
		InvokeMacro="RealWorldValueMappingMacro"
		Sequence="ReferencedImageSequence"						Type="1"	VM="1-n"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
	SequenceEnd
ModuleEnd


Module="IntravascularOCTSeries"
	Name="Modality"											Type="1"	StringEnumValues="IVOCTModality"
	Name="SeriesNumber"										Type="1"
	Sequence="ReferencedPerformedProcedureStepSequence"		Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Name="PresentationIntentType"							Type="1"	StringEnumValues="PresentationIntentType"
	Verify="PresentationIntentType"										Condition="IsForProcessingSOPClass"		StringEnumValues="ForProcessing"
	Verify="PresentationIntentType"										Condition="IsForPresentationSOPClass"	StringEnumValues="ForPresentation"
ModuleEnd

Module="IntravascularOCTImage"
	Name="ImageType"								Type="1"	VM="4"
	Verify="ImageType"											ValueSelector="0"	StringEnumValues="CommonEnhancedImageType1"
	Verify="ImageType"											ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
	Verify="ImageType"											ValueSelector="2"	StringDefinedTerms="IVOCTImageAndFrameTypeValue3"
	Verify="ImageType"											ValueSelector="3"	StringDefinedTerms="CommonEnhancedImageType4"

	Name="VolumetricProperties"						Type="1"	StringEnumValues="IVOCTVolumetricProperties"
	Name="PixelPresentation"						Type="1"	StringEnumValues="IVOCTPixelPresentationImageLevel"
	Name="SamplesPerPixel"							Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="AcquisitionDateTime"						Type="1"
	Name="AcquisitionDuration"						Type="1C"	Condition="ImageTypeValue1Original"
	Name="AcquisitionNumber"						Type="1"
	Name="PhotometricInterpretation"				Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="PixelRepresentation"						Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="BitsAllocated"							Type="1"	BinaryEnumValues="BitsAre8Or12Or16"
	Name="BitsStored"								Type="1"	BinaryEnumValues="BitsAre8Or12Or16"
	Name="HighBit"									Type="1"	BinaryEnumValues="BitsAre7Or11Or15"
	Name="PresentationLUTShape"						Type="1C"	Condition="PresentationIntentTypeIsForPresentation"	StringEnumValues="IdentityPresentationLUTShape"
	Name="LossyImageCompression"					Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"				Type="1C"	Condition="LossyImageCompressionIs01"
	Name="LossyImageCompressionMethod"				Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Name="BurnedInAnnotation"						Type="1"	StringEnumValues="NoFull"
	Name="RecognizableVisualFeatures"				Type="1"	StringEnumValues="NoFull"
	Sequence="ReferencedInstanceSequence"			Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"	Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="ImageComments"							Type="3"
	Name="RecommendedDisplayFrameRate"				Type="3"
	Name="InterpolationType"						Type="1C"	Condition="PresentationIntentTypeIsForPresentation"	StringEnumValues="IVOCTInterpolationType"
	Name="ReferencedColorPaletteInstanceUID"		Type="1C"	Condition="PixelPresentationIsColorRef"				StringDefinedTerms="WellKnownColorPaletteInstanceUIDs"
ModuleEnd

Module="IntravascularOCTAcquisitionParameters"
	Name="OCTFocalDistance"						Type="2"
	Name="BeamSpotSize"							Type="2"
	Name="EffectiveRefractiveIndex"				Type="2C"		Condition="PresentationIntentTypeIsForProcessing"
	Name="OCTAcquisitionDomain"					Type="1"		StringDefinedTerms="OCTAcquisitionDomain"
	Name="OCTOpticalCenterWavelength"			Type="2"
	Name="AxialResolution"						Type="2"
	Name="RangingDepth"							Type="1"
	Name="ALineRate"							Type="1"
	Name="ALinesPerFrame"						Type="1"
ModuleEnd

Module="IntravascularImageAcquisitionParameters"
	Name="IVUSAcquisition"						Type="1"	StringEnumValues="IVOCTIVUSAcquisition"
	Name="IVUSPullbackRate"						Type="1C"	Condition="IVUSAcquisitionIsMotorized"
	Name="IVUSPullbackStartFrameNumber"			Type="1C"	Condition="IVUSAcquisitionIsMotorized"
	Name="IVUSPullbackStopFrameNumber"			Type="1C"	Condition="IVUSAcquisitionIsMotorized"
	Name="CatheterDirectionOfRotation"			Type="1C"	Condition="RotationalCatheterInformationIsPresent"	StringEnumValues="CatheterDirectionOfRotation"
	Name="CatheterRotationalRate"				Type="1C"	Condition="RotationalCatheterInformationIsPresent"				
	Sequence="ModeOfPercutaneousAccessSequence"	Type="2"	VM="0-1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd				
ModuleEnd

Module="IntravascularOCTProcessingParameters"
	Name="OCTZOffsetApplied"					Type="1"	StringEnumValues="YesNoFull"
	Name="RefractiveIndexApplied"				Type="1"	StringEnumValues="YesNoFull"
	Name="ALinePixelSpacing"					Type="1"	NotZeroError=""
	Name="PixelIntensityRelationship"			Type="1"	StringEnumValues="IVOCTPixelIntensityRelationship"
	Name="FirstALineLocation"					Type="1"
ModuleEnd

DefineMacro="IntravascularOCTFrameTypeMacro"		InformationEntity="FunctionalGroup"
	Sequence="IntravascularOCTFrameTypeSequence"	Type="1"	VM="1"
		Name="FrameType"							Type="1"	VM="4"
		Verify="FrameType"										ValueSelector="0"	StringEnumValues="CommonEnhancedImageType1"
		Verify="FrameType"										ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
		Verify="FrameType"										ValueSelector="2"	StringDefinedTerms="IVOCTImageAndFrameTypeValue3"
		Verify="FrameType"										ValueSelector="3"	StringDefinedTerms="CommonEnhancedImageType4"
	SequenceEnd
MacroEnd

DefineMacro="IntravascularFrameContentMacro"		InformationEntity="FunctionalGroup"
	Sequence="IntravascularFrameContentSequence"	Type="1"	VM="1"
		Name="IntravascularLongitudinalDistance"	Type="1C"	Condition="IVUSAcquisitionIsMeasured"
		Name="SeamLineLocation"						Type="2C"	Condition="PresentationIntentTypeIsForPresentation"
	SequenceEnd
MacroEnd

DefineMacro="IntravascularOCTFrameContentMacro"		InformationEntity="FunctionalGroup"
	Sequence="IntravascularOCTFrameContentSequence"	Type="1"	VM="1"
		Name="OCTZOffsetCorrection"					Type="1"
		Name="SeamLineIndex"						Type="1"
		Name="NumberOfPaddedALines"					Type="1C"	NoCondition=""
		Verify="NumberOfPaddedALines"							Condition="PresentationIntentTypeIsForPresentation"	ThenErrorMessage="Only permitted for FOR PROCESSING images"
	SequenceEnd
MacroEnd

Module="MultiFrameFunctionalGroupsForIVOCTImageForPresentation"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PixelIntensityRelationshipLUTMacro"	Condition="NeedPixelIntensityRelationshipLUTMacroInSharedFunctionalGroupSequence"
		InvokeMacro="IntravascularOCTFrameTypeMacro"		Condition="IntravascularOCTFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="IntravascularFrameContentMacro"		Condition="IntravascularFrameContentSequenceNotInPerFrameFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelIntensityRelationshipLUTMacro"	Condition="NeedPixelIntensityRelationshipLUTMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="IntravascularOCTFrameTypeMacro"		Condition="IntravascularOCTFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="IntravascularFrameContentMacro"		Condition="IntravascularFrameContentSequenceNotInSharedFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="MultiFrameFunctionalGroupsForIVOCTImageForProcessing"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PixelIntensityRelationshipLUTMacro"	Condition="NeedPixelIntensityRelationshipLUTMacroInSharedFunctionalGroupSequence"
		InvokeMacro="IntravascularOCTFrameTypeMacro"		Condition="IntravascularOCTFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="IntravascularFrameContentMacro"		Condition="IntravascularFrameContentSequenceNotInPerFrameFunctionalGroupSequenceAndAcquisitionIsMeasured"
		InvokeMacro="IntravascularOCTFrameContentMacro"		Condition="IntravascularOCTFrameContentSequenceNotInPerFrameFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelIntensityRelationshipLUTMacro"	Condition="NeedPixelIntensityRelationshipLUTMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="IntravascularOCTFrameTypeMacro"		Condition="IntravascularOCTFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="IntravascularFrameContentMacro"		Condition="IntravascularFrameContentSequenceNotInSharedFunctionalGroupSequenceAndAcquisitionIsMeasured"
		InvokeMacro="IntravascularOCTFrameContentMacro"		Condition="IntravascularOCTFrameContentSequenceNotInSharedFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="ParametricMapSeries"
	Name="Modality"												Type="1"
	Name="SeriesNumber"											Type="1"
	Sequence="ReferencedPerformedProcedureStepSequence"			Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="ParametricMapImage"
	Name="ImageType"										Type="1"	VM="4"
	Verify="ImageType"										ValueSelector="0"	StringEnumValues="ParametricMapImageAndFrameType1"
	Verify="ImageType"										ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
	Verify="ImageType"										ValueSelector="2"	StringDefinedTerms="CommonEnhancedImageAndFrameType3"
	Verify="ImageType"										ValueSelector="3"	StringDefinedTerms="EnhancedMRImageType4"
	InvokeMacro="ContentIdentificationMacro"
	Name="PixelPresentation"								Type="3"	StringEnumValues="ParametricMapImagePixelPresentation"
	Name="SamplesPerPixel"									Type="1"	BinaryEnumValues="One"
	Name="PhotometricInterpretation"						Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"									Type="1"
	Verify="BitsAllocated"												Condition="PixelDataPresent"			BinaryEnumValues="BitsAre16"
	Verify="BitsAllocated"												Condition="FloatPixelDataPresent"		BinaryEnumValues="BitsAre32"
	Verify="BitsAllocated"												Condition="DoubleFloatPixelDataPresent"	BinaryEnumValues="BitsAre64"
	Name="BitsStored"										Type="1C"	Condition="PixelDataPresent"			BinaryEnumValues="BitsAre16"
	Name="HighBit"											Type="1C"	Condition="PixelDataPresent"			BinaryEnumValues="BitsAre15"
	Name="PresentationLUTShape"								Type="1"	StringEnumValues="IdentityPresentationLUTShape"
	Name="LossyImageCompression"							Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"						Type="1C"	NoCondition=""
	Name="LossyImageCompressionMethod"						Type="1C"	NoCondition=""
	Verify="LossyImageCompressionMethod"								Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="BurnedInAnnotation"								Type="1"	StringEnumValues="NoFull"
	Name="RecognizableVisualFeatures"						Type="1"	StringEnumValues="YesNoFull"
	Name="ContentQualification"								Type="1"	StringEnumValues="ContentQualification"
	Name="PaletteColorLookupTableUID"						Type="1C"	Condition="PixelPresentationIsColorRangeAndPaletteColorLookupTableModuleAbsent"
	Name="ICCProfile"										Type="1C"	Condition="PixelPresentationIsColorRange"
	Name="ColorSpace"										Type="3"
ModuleEnd

Module="MultiFrameFunctionalGroupsForParametricMap"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="IdentityPixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTWithLUTMacro"				Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="RealWorldValueMappingSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="ParametricMapFrameTypeMacro"			Condition="ParametricMapFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="StoredValueColorRangeMacro"			Condition="StoredValueColorRangeSequenceNotInPerFrameFunctionalGroupSequenceAndPixelPresentationIsColorRange"
		InvokeMacro="UnassignedSharedConvertedAttributesMacro"	Condition="UnassignedSharedConvertedAttributesMacroPresentInSharedFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="IdentityPixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTWithLUTMacro"				Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="RealWorldValueMappingSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="ParametricMapFrameTypeMacro"			Condition="ParametricMapFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="StoredValueColorRangeMacro"			Condition="StoredValueColorRangeSequenceNotInSharedFunctionalGroupSequenceAndPixelPresentationIsColorRange"
		InvokeMacro="UnassignedPerFrameConvertedAttributesMacro"	Condition="UnassignedPerFrameConvertedAttributesMacroPresentInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

DefineMacro="ParametricMapFrameTypeMacro" InformationEntity="FunctionalGroup"
	Sequence="ParametricMapFrameTypeSequence"	Type="1"	VM="1"
		Name="FrameType"						Type="1"	VM="4"
		Verify="FrameType"								ValueSelector="0"	StringEnumValues="ParametricMapImageAndFrameType1"
		Verify="FrameType"								ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
		Verify="FrameType"								ValueSelector="2"	StringDefinedTerms="CommonEnhancedImageAndFrameType3"
		Verify="FrameType"								ValueSelector="3"	StringDefinedTerms="EnhancedMRFrameType4"
	SequenceEnd
MacroEnd

DefineMacro="StoredValueColorRangeMacro" InformationEntity="FunctionalGroup"
	Sequence="StoredValueColorRangeSequence"	Type="1"	VM="1"
		Name="MinimumStoredValueMapped"			Type="1"	VM="1"
		Name="MaximumStoredValueMapped"			Type="1"	VM="1"
	SequenceEnd
MacroEnd

Module="Manufacturing3DModel"
	Sequence="MeasurementUnitsCodeSequence"		Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"									DefinedContextID="7063"
	SequenceEnd
	Name="ModelModification"					Type="3"				StringEnumValues="YesNoFull"
	Name="ModelMirroring"						Type="3"				StringEnumValues="YesNoFull"
	Sequence="ModelUsageCodeSequence"			Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"									BaselineContextID="7064"
	SequenceEnd
	Name="ContentDescription"					Type="3"
	Sequence="IconImageSequence"				Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
	Sequence="DerivationAlgorithmSequence"		Type="3"	VM="1"
		InvokeMacro="AlgorithmIdentificationMacro"
	SequenceEnd
ModuleEnd

Module="FileMetaInformation"

	Name="FileMetaInformationGroupLength"	Type="1"
	Name="FileMetaInformationVersion"	Type="1"
	Name="MediaStorageSOPClassUID"	Type="1"
	Name="MediaStorageSOPInstanceUID"	Type="1"
	Name="TransferSyntaxUID"		Type="1"
	Name="ImplementationClassUID"		Type="1"
	Name="ImplementationVersionName"	Type="3"
	Name="SourceApplicationEntityTitle"	Type="3"
	Name="SendingApplicationEntityTitle"	Type="3"
	Name="ReceivingApplicationEntityTitle"	Type="3"
	Name="SourcePresentationAddress"	Type="3"
	Name="SendingPresentationAddress"	Type="3"
	Name="ReceivingPresentationAddress"	Type="3"
	Name="PrivateInformationCreatorUID"	Type="3"
	Name="PrivateInformation"		Type="1C"	Condition="PrivateInformationCreatorUIDPresent"

ModuleEnd

Module="FileSetIdentification"

	Name="FileSetID"			Type="2"
	Name="FileSetDescriptorFileID"		Type="3"
	Name="SpecificCharacterSetOfFileSetDescriptorFile"		Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"

ModuleEnd

Module="DirectoryInformation"

	Name="OffsetOfTheFirstDirectoryRecordOfTheRootDirectoryEntity"					Type="1"
	Name="OffsetOfTheLastDirectoryRecordOfTheRootDirectoryEntity"					Type="1"
	Name="FileSetConsistencyFlag"					Type="1"	BinaryEnumValues="FileSetConsistencyFlag"
	Sequence="DirectoryRecordSequence"				Type="2"	VM="0-n"
		Name="OffsetOfTheNextDirectoryRecord"			Type="1"
		Name="RecordInUseFlag"						Type="1"	BinaryEnumValues="RecordInUseFlag"
		Name="OffsetOfReferencedLowerLevelDirectoryEntity"			Type="1"
		Name="DirectoryRecordType"					Type="1"	StringEnumValues="DirectoryRecordType"
		Name="PrivateRecordUID"						Type="1C"	Condition="DirectoryRecordTypeIsPrivate"
		Name="ReferencedFileID"						Type="1C"	Condition="DirectorySOPInstance" mbpo="true"	# mbpo since may be (optional) Detached Patient instance reference, for example
		Name="ReferencedSOPClassUIDInFile"			Type="1C"	Condition="DirectorySOPInstance" mbpo="true"
		Name="ReferencedSOPInstanceUIDInFile"		Type="1C"	Condition="DirectorySOPInstance" mbpo="true"
		Name="ReferencedTransferSyntaxUIDInFile"	Type="1C"	Condition="DirectorySOPInstance" mbpo="true"
		
		InvokeMacro="PatientDirectoryRecord"					Condition="DirectoryRecordTypeIsPatient"
		InvokeMacro="StudyDirectoryRecord"						Condition="DirectoryRecordTypeIsStudy"
		InvokeMacro="SeriesDirectoryRecord"						Condition="DirectoryRecordTypeIsSeries"
		InvokeMacro="ImageDirectoryRecord"						Condition="DirectoryRecordTypeIsImage"
		InvokeMacro="RTDoseDirectoryRecord"						Condition="DirectoryRecordTypeIsRTDose"
		InvokeMacro="RTStructureSetDirectoryRecord"				Condition="DirectoryRecordTypeIsRTStructureSet"
		InvokeMacro="RTPlanDirectoryRecord"						Condition="DirectoryRecordTypeIsRTPlan"
		InvokeMacro="RTTreatmentRecordDirectoryRecord"			Condition="DirectoryRecordTypeIsRTTreatmentRecord"
		InvokeMacro="PresentationDirectoryRecord"				Condition="DirectoryRecordTypeIsPresentation"
		InvokeMacro="WaveformDirectoryRecord"					Condition="DirectoryRecordTypeIsWaveform"
		InvokeMacro="SRDocumentDirectoryRecord"					Condition="DirectoryRecordTypeIsSRDocument"
		InvokeMacro="KeyObjectDocumentDirectoryRecord"			Condition="DirectoryRecordTypeIsKeyObjectDocument"
		InvokeMacro="SpectroscopyDirectoryRecord"				Condition="DirectoryRecordTypeIsSpectroscopy"
		InvokeMacro="RawDataDirectoryRecord"					Condition="DirectoryRecordTypeIsRawData"
		InvokeMacro="RegistrationDirectoryRecord"				Condition="DirectoryRecordTypeIsRegistration"
		InvokeMacro="FiducialDirectoryRecord"					Condition="DirectoryRecordTypeIsFiducial"
		InvokeMacro="HangingProtocolDirectoryRecord"			Condition="DirectoryRecordTypeIsHangingProtocol"
		InvokeMacro="EncapsulatedDocumentDirectoryRecord"		Condition="DirectoryRecordTypeIsEncapsulatedDocument"
		InvokeMacro="HL7StructuredDocumentDirectoryRecord"		Condition="DirectoryRecordTypeIsHL7StructuredDocument"
		InvokeMacro="RealWorldValueMappingDirectoryRecord"		Condition="DirectoryRecordTypeIsRealWorldValueMapping"
		InvokeMacro="StereometricRelationshipDirectoryRecord"	Condition="DirectoryRecordTypeIsStereometricRelationship"
		InvokeMacro="SurfaceDirectoryRecord"					Condition="DirectoryRecordTypeIsSurface"
	SequenceEnd
ModuleEnd

DefineMacro="PatientDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="PatientName"							Type="2"
		Name="PatientID"							Type="1"
MacroEnd

DefineMacro="StudyDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="StudyDate"							Type="1"
		Name="StudyTime"							Type="1"
		Name="StudyDescription"						Type="2"
		Name="StudyInstanceUID"						Type="1C"	Condition="ReferencedSOPInstanceUIDInFileIsNotPresent"
		Name="StudyID"								Type="1"
		Name="AccessionNumber"						Type="2"
MacroEnd
		
DefineMacro="SeriesDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="Modality"								Type="1"
		Name="SeriesInstanceUID"					Type="1"
		Name="SeriesNumber"							Type="1"
		Sequence="IconImageSequence"				Type="3"	VM="1"
			InvokeMacro="IconImageSequenceMacro"
		SequenceEnd
MacroEnd
		
DefineMacro="ImageDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="InstanceNumber"						Type="1"
		Sequence="IconImageSequence"				Type="3"	VM="1"
			InvokeMacro="IconImageSequenceMacro"
		SequenceEnd
MacroEnd

DefineMacro="RTDoseDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="InstanceNumber"						Type="1"
		Name="DoseSummationType"					Type="1"
		Name="DoseComment"							Type="3"
		Sequence="IconImageSequence"				Type="3"	VM="1"
			InvokeMacro="IconImageSequenceMacro"
		SequenceEnd
MacroEnd

DefineMacro="RTStructureSetDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="InstanceNumber"						Type="1"
		Name="StructureSetLabel"					Type="1"
		Name="StructureSetDate"						Type="2"
		Name="StructureSetTime"						Type="2"
MacroEnd

DefineMacro="RTPlanDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="InstanceNumber"						Type="1"
		Name="RTPlanLabel"							Type="1"
		Name="RTPlanDate"							Type="2"
		Name="RTPlanTime"							Type="2"
MacroEnd

DefineMacro="RTTreatmentRecordDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="InstanceNumber"						Type="1"
		Name="TreatmentDate"						Type="2"
		Name="TreatmentTime"						Type="2"
MacroEnd

DefineMacro="PresentationDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="PresentationCreationDate"				Type="1C"	Condition="DirectoryRecordTypeIsPresentation"
		Name="PresentationCreationTime"				Type="1C"	Condition="DirectoryRecordTypeIsPresentation"
		InvokeMacro="ContentIdentificationMacro"
		Sequence="ReferencedSeriesSequence"			Type="1C"	VM="1-n"	Condition="BlendingSequenceIsNotPresent"				# condition is actually whether or not present in instance, but this is equivalent based on SOP Classes known
			Name="SeriesInstanceUID"				Type="1"
			Sequence="ReferencedImageSequence"		Type="1"	VM="1-n"
				InvokeMacro="SOPInstanceReferenceMacro"
			SequenceEnd
		SequenceEnd
		Sequence="BlendingSequence"					Type="1C"	VM="2"		Condition="ReferencedSeriesSequenceIsNotPresent"		# condition is actually whether or not present in instance, but this is equivalent based on SOP Classes known
			Name="StudyInstanceUID"					Type="1"
			Sequence="ReferencedSeriesSequence"		Type="1"	VM="1-n"
				Name="SeriesInstanceUID"			Type="1"
				Sequence="ReferencedImageSequence"	Type="1"	VM="1-n"
					InvokeMacro="SOPInstanceReferenceMacro"
				SequenceEnd
			SequenceEnd
		SequenceEnd
MacroEnd

DefineMacro="WaveformDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="InstanceNumber"						Type="1"
		Name="ContentDate"							Type="1"
		Name="ContentTime"							Type="1"
MacroEnd

DefineMacro="SRDocumentDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="InstanceNumber"						Type="1"
		Name="CompletionFlag"						Type="1"
		Name="VerificationFlag"						Type="1"
		Name="ContentDate"							Type="1"
		Name="ContentTime"							Type="1"
		Name="VerificationDateTime"					Type="1C"	Condition="VerificationFlagIsVerified"
		Sequence="ConceptNameCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="ContentSequence"					Type="1C"	VM="1-n"	NoCondition=""
			Name="RelationshipType"					Type="1"	StringEnumValues="SRRelationshipTypeHasConceptModifier"
			InvokeMacro="DocumentContentMacro"
		SequenceEnd
MacroEnd

DefineMacro="KeyObjectDocumentDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="InstanceNumber"						Type="1"
		Name="ContentDate"							Type="1"
		Name="ContentTime"							Type="1"
		Sequence="ConceptNameCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="ContentSequence"					Type="1C"	VM="1-n"	NoCondition=""
			Name="RelationshipType"					Type="1"	StringEnumValues="SRRelationshipTypeHasConceptModifier"
			InvokeMacro="DocumentContentMacro"
		SequenceEnd
MacroEnd

DefineMacro="SpectroscopyDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="ImageType"							Type="1"
		Name="ContentDate"							Type="1"
		Name="ContentTime"							Type="1"
		Name="InstanceNumber"						Type="1"
		Sequence="ReferencedImageEvidenceSequence"	Type="1"	VM="1-n"	NoCondition=""
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Name="NumberOfFrames"						Type="1"
		Name="Rows"									Type="1"
		Name="Columns"								Type="1"
		Name="DataPointRows"						Type="1"
		Name="DataPointColumns"						Type="1"
		Sequence="IconImageSequence"				Type="3"	VM="1"
			InvokeMacro="IconImageSequenceMacro"
		SequenceEnd
MacroEnd

DefineMacro="RawDataDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="ContentDate"							Type="1"
		Name="ContentTime"							Type="1"
		Name="InstanceNumber"						Type="2"
		Sequence="IconImageSequence"				Type="3"	VM="1"
			InvokeMacro="IconImageSequenceMacro"
		SequenceEnd
MacroEnd

DefineMacro="RegistrationDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="ContentDate"							Type="1"
		Name="ContentTime"							Type="1"
		InvokeMacro="ContentIdentificationMacro"
MacroEnd

DefineMacro="FiducialDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="ContentDate"							Type="1"
		Name="ContentTime"							Type="1"
		InvokeMacro="ContentIdentificationMacro"
MacroEnd

DefineMacro="HangingProtocolDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="HangingProtocolName"									Type="1"
		Name="HangingProtocolDescription"							Type="1"
		Name="HangingProtocolLevel"									Type="1"
		Name="HangingProtocolCreator"								Type="1"
		Name="HangingProtocolCreationDateTime"						Type="1"
		Sequence="HangingProtocolDefinitionSequence"				Type="1"	VM="1-n"
			Name="Modality"											Type="1C"	Condition="AnatomicRegionSequenceIsNotPresent" mbpo="true"
			Sequence="AnatomicRegionSequence"						Type="1C"	VM="1-n"	Condition="ModalityIsNotPresent" mbpo="true"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Name="Laterality"										Type="2C"	Condition="AnatomicRegionSequenceIsPresent" mbpo="true"
			Sequence="ProcedureCodeSequence"						Type="2"	VM="1-n"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Sequence="ReasonForRequestedProcedureCodeSequence"		Type="2"	VM="1-n"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
		SequenceEnd
		Name="NumberOfPriorsReferenced"								Type="1"
		Sequence="HangingProtocolUserIdentificationCodeSequence"	Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
MacroEnd

DefineMacro="EncapsulatedDocumentDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="ContentDate"							Type="2"
		Name="ContentTime"							Type="2"
		Name="InstanceNumber"						Type="1"
		Name="DocumentTitle"						Type="2"
		Name="HL7InstanceIdentifier"				Type="1C"	Condition="ReferencedSOPClassUIDInFileIsEncapsulatedCDADocument"
		Sequence="ConceptNameCodeSequence"			Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="MIMETypeOfEncapsulatedDocument"		Type="1"
MacroEnd

DefineMacro="HL7StructuredDocumentDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="HL7InstanceIdentifier"				Type="1"
		Name="HL7DocumentEffectiveTime"				Type="1"
		Sequence="HL7DocumentTypeCodeSequence"		Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
MacroEnd

DefineMacro="RealWorldValueMappingDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="ContentDate"							Type="1"
		Name="ContentTime"							Type="1"
		InvokeMacro="ContentIdentificationMacro"
MacroEnd

DefineMacro="StereometricRelationshipDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		InvokeMacro="ContentIdentificationMacro"
MacroEnd

DefineMacro="SurfaceDirectoryRecord"
		Name="SpecificCharacterSet"					Type="1C"	NoCondition=""	StringDefinedTerms="SpecificCharacterSet"
		Name="ContentDate"							Type="1"
		Name="ContentTime"							Type="1"
		InvokeMacro="ContentIdentificationMacro"
MacroEnd

Module="DirectoryInformationDental"
	Sequence="DirectoryRecordSequence"				Type="2"	VM="0-n"
		Name="ReferencedSOPClassUIDInFile"			Type="1C"	Condition="DirectorySOPInstance"	StringEnumValues="DentalMediaProfileSOPClasses"
		Name="ReferencedTransferSyntaxUIDInFile"	Type="1C"	Condition="DirectorySOPInstance"	StringEnumValues="DentalMediaProfileTransferSyntaxes"
	SequenceEnd
ModuleEnd

Module="PETSeries"
	Name="SeriesDate"									Type="1"
	Name="SeriesTime"									Type="1"
	Name="Units"										Type="1"	StringDefinedTerms="PETUnits"
	Name="SUVType"										Type="3"	StringEnumValues="SUVType"
	Name="CountsSource"									Type="1"	StringEnumValues="CountsSource"
	Name="SeriesType"									Type="1"	ValueSelector="0"	StringEnumValues="PETSeriesType1"
	Verify="SeriesType"									Type="1"	ValueSelector="1"	StringEnumValues="PETSeriesType2"
	Name="ReprojectionMethod"							Type="2C"	Condition="PETSeriesType2Reprojection"	StringDefinedTerms="ReprojectionMethod"
	Name="NumberOfRRIntervals"							Type="1C"	Condition="PETSeriesType1Gated"
	Name="NumberOfTimeSlots"							Type="1C"	Condition="PETSeriesType1Gated"
	Name="NumberOfTimeSlices"							Type="1C"	Condition="PETSeriesType1Dynamic"
	Name="NumberOfSlices"								Type="1"
	Name="CorrectedImage"								Type="2"	StringDefinedTerms="CorrectedImage"
	Name="RandomsCorrectionMethod"						Type="3"	StringDefinedTerms="RandomsCorrectionMethod"
	Name="AttenuationCorrectionMethod"					Type="3"
	Name="ScatterCorrectionMethod"						Type="3"
	Name="DecayCorrection"								Type="1"	StringDefinedTerms="DecayCorrection"
	Name="ReconstructionDiameter"						Type="3"	NotZeroWarning=""
	Name="ConvolutionKernel"							Type="3"
	Name="ReconstructionMethod"							Type="3"
	Name="DetectorLinesOfResponseUsed"					Type="3"
	Name="AcquisitionStartCondition"					Type="3"	StringDefinedTerms="AcquisitionStartCondition"
	Name="AcquisitionStartConditionData"				Type="3"
	Name="AcquisitionTerminationCondition"				Type="3"	StringDefinedTerms="PETAcquisitionTerminationCondition"
	Name="AcquisitionTerminationConditionData"			Type="3"
	Name="FieldOfViewShape"								Type="3"	StringDefinedTerms="PETFieldOfViewShape"
	Name="FieldOfViewDimensions"						Type="3"	NotZeroWarning=""
	Name="GantryDetectorTilt"							Type="3"
	Name="GantryDetectorSlew"							Type="3"
	Name="TypeOfDetectorMotion"							Type="3"	StringDefinedTerms="TypeOfDetectorMotion"
	Name="CollimatorType"								Type="2"	StringDefinedTerms="PETCollimatorType"
	Name="CollimatorGridName"							Type="3"
	Name="AxialAcceptance"								Type="3"
	Name="AxialMash"									Type="3"
	Name="TransverseMash"								Type="3"
	Name="DetectorElementSize"							Type="3"	NotZeroError=""
	Name="CoincidenceWindowWidth"						Type="3"
	Sequence="EnergyWindowRangeSequence"				Type="3"	VM="1-n"
		Name="EnergyWindowLowerLimit"					Type="3"
		Name="EnergyWindowUpperLimit"					Type="3"
	SequenceEnd
	Name="SecondaryCountsType"							Type="3"	StringDefinedTerms="SecondaryCountsType"
ModuleEnd

Module="PETIsotope"
	Sequence="RadiopharmaceuticalInformationSequence"	Type="2"	VM="0-n"
		Sequence="RadionuclideCodeSequence"				Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="4020"
		SequenceEnd
		Name="RadiopharmaceuticalRoute"					Type="3"
		Sequence="AdministrationRouteCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="11"
		SequenceEnd
		Name="RadiopharmaceuticalVolume"				Type="3"
		Name="RadiopharmaceuticalStartTime"				Type="3"
		Name="RadiopharmaceuticalStartDateTime"			Type="3"
		Name="RadiopharmaceuticalStopTime"				Type="3"
		Name="RadiopharmaceuticalStopDateTime"			Type="3"
		Name="RadionuclideTotalDose"					Type="3"
		Name="RadionuclideHalfLife"						Type="3"
		Name="RadionuclidePositronFraction"				Type="3"
		Name="RadiopharmaceuticalSpecificActivity"		Type="3"
		Name="Radiopharmaceutical"						Type="3"
		Sequence="RadiopharmaceuticalCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="4021"
		SequenceEnd
	SequenceEnd
	Sequence="InterventionDrugInformationSequence"		Type="3"	VM="1-n"
		Name="InterventionDrugName"						Type="3"
		Sequence="InterventionDrugCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="10"
		SequenceEnd
		Name="InterventionDrugStartTime"				Type="3"
		Name="InterventionDrugStopTime"					Type="3"
		Name="InterventionDrugDose"						Type="3"
	SequenceEnd
ModuleEnd

Module="PETMultigatedAcquisition"
	Name="BeatRejectionFlag"							Type="2"	StringEnumValues="YesNoLetter"
	Name="TriggerSourceOrType"							Type="3"	StringDefinedTerms="EKG"
	Name="PVCRejection"									Type="3"
	Name="SkipBeats"									Type="3"
	Name="HeartRate"									Type="3"
	Name="CardiacFramingType"							Type="3"	StringDefinedTerms="CardiacFramingType"
ModuleEnd

Module="PETImage"
	Name="ImageType"									Type="1"	ValueSelector="0"	StringEnumValues="ImageType1"
	Verify="ImageType"									Type="1"	ValueSelector="1"	StringEnumValues="PETImageTypeValue2"
	Name="SamplesPerPixel"								Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"					Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"								Type="1"	BinaryEnumValues="BitsAre16"
	Name="BitsStored"									Type="1"	BinaryEnumValues="BitsAre16"
	Name="HighBit"										Type="1"	BinaryEnumValues="BitsAre15"
	Name="RescaleIntercept"								Type="1"	BinaryEnumValues="Zero"
	Name="RescaleSlope"									Type="1"	NotZeroError=""
	Name="FrameReferenceTime"							Type="1"
	Name="TriggerTime"									Type="1C"	Condition="PETSeriesType1Gated"
	Name="FrameTime"									Type="1C"	Condition="PETSeriesType1Gated"
	Name="LowRRValue"									Type="1C"	Condition="PETSeriesType1GatedAndBeatRejection"
	Name="HighRRValue"									Type="1C"	Condition="PETSeriesType1GatedAndBeatRejection"
	Name="LossyImageCompression"						Type="1C"	NoCondition=""	StringEnumValues="LossyImageCompression"
	Name="ImageIndex"									Type="1"
	Name="AcquisitionDate"								Type="2"
	Name="AcquisitionTime"								Type="2"
	Name="ActualFrameDuration"							Type="2"
	Name="NominalInterval"								Type="3"
	Name="IntervalsAcquired"							Type="3"
	Name="IntervalsRejected"							Type="3"
	Name="PrimaryPromptsCountsAccumulated"				Type="3"
	Name="SecondaryCountsAccumulated"					Type="3"
	Name="SliceSensitivityFactor"						Type="3"
	Name="DecayFactor"									Type="1C"	Condition="DecayCorrectionNotNone"
	Name="DoseCalibrationFactor"						Type="3"
	Name="ScatterFractionFactor"						Type="3"
	Name="DeadTimeFactor"								Type="3"
	InvokeMacro="GeneralAnatomyOptionalMacro"
	InvokeMacro="OptionalViewAndSliceProgressionDirectionMacro"
	Name="IsocenterPosition"							Type="3"
ModuleEnd

Module="MultiFrameFunctionalGroupsForEnhancedPETImage"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="NeedRespiratorySynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RadiopharmaceuticalUsageMacro"		Condition="RadiopharmaceuticalUsageSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PatientPhysiologicalStateMacro"	Condition="NeedPatientPhysiologicalStateMacroInSharedFunctionalGroupSequence"
		InvokeMacro="PETFrameTypeMacro"		Condition="PETFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PETFrameAcquisitionMacro"	Condition="NeedPETFrameAcquisitionMacroInSharedFunctionalGroupSequence"
		InvokeMacro="PETDetectorMotionDetailsMacro"	Condition="NeedPETDetectorMotionDetailsMacroInSharedFunctionalGroupSequence"
		InvokeMacro="PETPositionMacro"	Condition="NeedPETPositionMacroInSharedFunctionalGroupSequence"
		InvokeMacro="PETFrameCorrectionFactorsMacro"	Condition="NeedPETFrameCorrectionFactorsMacroInSharedFunctionalGroupSequence"
		InvokeMacro="PETReconstructionMacro"	Condition="NeedPETReconstructionMacroInSharedFunctionalGroupSequence"
		InvokeMacro="PETTableDynamicsMacro"	Condition="NeedPETTableDynamicsMacroInSharedFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"					Condition="TemporalPositionMacroOKInSharedFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="NeedRespiratorySynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RadiopharmaceuticalUsageMacro"		Condition="RadiopharmaceuticalUsageSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PatientPhysiologicalStateMacro"	Condition="NeedPatientPhysiologicalStateMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="PETFrameTypeMacro"		Condition="PETFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PETFrameAcquisitionMacro"	Condition="NeedPETFrameAcquisitionMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="PETDetectorMotionDetailsMacro"	Condition="NeedPETDetectorMotionDetailsMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="PETPositionMacro"	Condition="NeedPETPositionMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="PETFrameCorrectionFactorsMacro"	Condition="NeedPETFrameCorrectionFactorsMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="PETReconstructionMacro"	Condition="NeedPETReconstructionMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="PETTableDynamicsMacro"	Condition="NeedPETTableDynamicsMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"			Condition="TemporalPositionMacroOKInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="MultiFrameFunctionalGroupsForLegacyConvertedEnhancedPETImage"
	Sequence="SharedFunctionalGroupsSequence"				Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"			Condition="PixelValueTransformationSequenceOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PETFrameTypeMacro"						Condition="PETFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"					Condition="TemporalPositionMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="UnassignedSharedConvertedAttributesMacro"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"				Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"			Condition="PixelValueTransformationSequenceOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PETFrameTypeMacro"						Condition="PETFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"					Condition="TemporalPositionMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="UnassignedPerFrameConvertedAttributesMacro"
		InvokeMacro="ImageFrameConversionSourceMacro"		Condition="ImageFrameConversionSourceMacroPresentInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="MultiFrameFunctionalGroupsForPrivatePixelMedLegacyConvertedEnhancedPETImage"
	Sequence="SharedFunctionalGroupsSequence"				Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"			Condition="PixelValueTransformationSequenceOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PETFrameTypeMacro"						Condition="PETFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="UnassignedSharedConvertedAttributesMacro"
		InvokeMacro="ImageFrameConversionSourceMacro"		Condition="ConversionSourceAttributesSequenceNotInPerFrameFunctionalGroupSequence"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"				Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"			Condition="PixelValueTransformationSequenceOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PETFrameTypeMacro"						Condition="PETFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="UnassignedPerFrameConvertedAttributesMacro"
		InvokeMacro="ImageFrameConversionSourceMacro"		Condition="ConversionSourceAttributesSequenceNotInSharedFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

DefineMacro="PETFrameTypeMacro" InformationEntity="FunctionalGroup"
	Sequence="PETFrameTypeSequence"	Type="1"	VM="1"
		Name="FrameType"						Type="1"	VM="4"
		Verify="FrameType"									ValueSelector="0"	StringEnumValues="CommonEnhancedFrameType1"
		Verify="FrameType"									ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
		Verify="FrameType"									ValueSelector="2"	StringDefinedTerms="CommonEnhancedImageAndFrameType3"
		Verify="FrameType"									ValueSelector="3"	StringDefinedTerms="CommonEnhancedFrameType4"
		InvokeMacro="CommonCTMRImageDescriptionFrameLevelMacro"
	SequenceEnd
MacroEnd

DefineMacro="PETFrameAcquisitionMacro" InformationEntity="FunctionalGroup"
	Sequence="PETFrameAcquisitionSequence"		Type="1"	VM="1"
		Name="TableHeight"						Type="1"	NotZeroWarning=""
		Name="GantryDetectorTilt"				Type="1"
		Name="GantryDetectorSlew"				Type="1"
		Name="DataCollectionDiameter"			Type="1"	NotZeroWarning=""
	SequenceEnd
MacroEnd

DefineMacro="PETDetectorMotionDetailsMacro" InformationEntity="FunctionalGroup"
	Sequence="PETDetectorMotionDetailsSequence"	Type="1"	VM="1"
		Name="RotationDirection"				Type="1"	StringEnumValues="RotationDirection"
		Name="RevolutionTime"					Type="1"	NotZeroWarning=""
	SequenceEnd
MacroEnd

DefineMacro="PETPositionMacro" InformationEntity="FunctionalGroup"
	Sequence="PETPositionSequence"					Type="1"	VM="1"
		Name="TablePosition"						Type="1C"	Condition="Always"	# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="DataCollectionCenterPatient"			Type="1C"	Condition="Always"	# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="ReconstructionTargetCenterPatient"	Type="1C"	Condition="Always"	# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
	SequenceEnd
MacroEnd

DefineMacro="PETFrameCorrectionFactorsMacro" InformationEntity="FunctionalGroup"
	Sequence="PETFrameCorrectionFactorsSequence"	Type="1"	VM="1"
		Name="PrimaryPromptsCountsAccumulated"		Type="1C"	Condition="Always"				NotZeroWarning=""	# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="SliceSensitivityFactor"				Type="1C"	Condition="Always"				NotZeroWarning=""	# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="DecayFactor"							Type="1C"	Condition="IsDecayCorrected"	NotZeroWarning=""	# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="ScatterFractionFactor"				Type="1C"	Condition="Always"									# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="DeadTimeFactor"						Type="1C"	Condition="Always"				NotZeroWarning=""	# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
	SequenceEnd
MacroEnd

DefineMacro="PETReconstructionMacro" InformationEntity="FunctionalGroup"
	Sequence="PETReconstructionSequence"			Type="1"	VM="1"
		Name="ReconstructionType"					Type="1C"	Condition="Always"	StringDefinedTerms="PETReconstructionType"		# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="ReconstructionAlgorithm"				Type="1C"	Condition="Always"	StringDefinedTerms="PETReconstructionAlgorithm"	# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="IterativeReconstructionMethod"		Type="1"						StringEnumValues="YesNoFull"
		Name="NumberOfIterations"					Type="1C"	Condition="IsIterativeReconstruction"		NotZeroWarning=""		# && ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="NumberOfSubsets"						Type="1C"	Condition="IsIterativeReconstruction"		NotZeroWarning=""		# && ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="ReconstructionDiameter"				Type="1C"	Condition="ReconstructionFieldOfViewAbsent"	NotZeroWarning=""		# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="ReconstructionFieldOfView"			Type="1C"	Condition="ReconstructionDiameterAbsent"	NotZeroWarning=""		# ../PETFrameTypeMacro/FrameType[0] == ORIGINAL
	SequenceEnd
MacroEnd

DefineMacro="PETTableDynamicsMacro" InformationEntity="FunctionalGroup"
	Sequence="PETTableDynamicsSequence"				Type="1"	VM="1"
		Name="TableSpeed"							Type="1"	NotZeroWarning=""
	SequenceEnd
MacroEnd

Module="EnhancedPETSeries"
	Name="Modality"										Type="1"	StringEnumValues="PETModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="RelatedSeriesSequence"					Type="1C"	VM="1-n"	NoCondition=""
		Name="StudyInstanceUID"							Type="1"
		Name="SeriesInstanceUID"						Type="1"
		Sequence="PurposeOfReferenceCodeSequence"		Type="2"	VM="0-n"
			InvokeMacro="CodeSequenceMacro"				BaselineContextID="7210"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="EnhancedPETIsotope"
	Sequence="RadiopharmaceuticalInformationSequence"	Type="1"	VM="1-n"
		Name="RadiopharmaceuticalAgentNumber"			Type="1"
		Sequence="RadionuclideCodeSequence"				Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="4020"
		SequenceEnd
		Sequence="AdministrationRouteCodeSequence"		Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="11"
		SequenceEnd
		Name="RadiopharmaceuticalVolume"				Type="3"	NotZeroWarning=""
		Name="RadiopharmaceuticalStartDateTime"			Type="1"
		Name="RadiopharmaceuticalStopDateTime"			Type="3"
		Name="RadionuclideTotalDose"					Type="2"	NotZeroWarning=""
		Name="RadionuclideHalfLife"						Type="1"	NotZeroWarning=""
		Name="RadionuclidePositronFraction"				Type="1"	NotZeroWarning=""
		Name="RadiopharmaceuticalSpecificActivity"		Type="3"	NotZeroWarning=""
		Sequence="RadiopharmaceuticalCodeSequence"		Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="4021"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="EnhancedPETAcquisition"
	Name="AcquisitionStartCondition"					Type="1C"	Condition="ImageTypeValue1Original" mbpo="true" StringDefinedTerms="EnhancedPETAcquisitionStartCondition"
	Name="StartDensityThreshold"						Type="1C"	Condition="AcquisitionStartConditionDENS"
	Name="StartRelativeDensityDifferenceThreshold"		Type="1C"	Condition="AcquisitionStartConditionRDD"
	Name="StartCardiacTriggerCountThreshold"			Type="1C"	Condition="AcquisitionStartConditionCARD_TRIG"
	Name="StartRespiratoryTriggerCountThreshold"		Type="1C"	Condition="AcquisitionStartConditionRESP_TRIG"
	Name="AcquisitionTerminationCondition"				Type="1C"	Condition="ImageTypeValue1Original" mbpo="true" StringDefinedTerms="EnhancedPETAcquisitionTerminationCondition"
	Name="TerminationCountsThreshold"					Type="1C"	Condition="AcquisitionTerminationConditionCNTS"
	Name="TerminationDensityThreshold"					Type="1C"	Condition="AcquisitionTerminationConditionDENS"
	Name="TerminationRelativeDensityThreshold"			Type="1C"	Condition="AcquisitionTerminationConditionRDD"
	Name="TerminationTimeThreshold"						Type="1C"	Condition="AcquisitionTerminationConditionTIME"
	Name="TerminationCardiacTriggerCountThreshold"		Type="1C"	Condition="AcquisitionTerminationConditionCARD_TRIG"
	Name="TerminationRespiratoryTriggerCountThreshold"	Type="1C"	Condition="AcquisitionTerminationConditionRESP_TRIG"
	Name="TypeOfDetectorMotion"							Type="1C"	Condition="ImageTypeValue1Original" mbpo="true" StringDefinedTerms="EnhancedPETTypeOfDetectorMotion"
	Name="DetectorGeometry"								Type="1C"	Condition="OriginalAndTypeOfDetectorMotionIsStationary" mbpo="true" StringDefinedTerms="DetectorGeometry"
	Verify="DetectorGeometry"										Condition="DetectorGeometryPresentAndTypeOfDetectorMotionIsNotStationary"	ThenErrorMessage="may only be present when TypeOfDetectorMotion is STATIONARY " ShowValueWithMessage="false"
	Name="TransverseDetectorSeparation"					Type="1C"	Condition="ImageTypeValue1Original" mbpo="true"
	Name="AxialDetectorDimension"						Type="1C"	Condition="ImageTypeValue1Original" mbpo="true"
	Name="CollimatorType"								Type="1C"	Condition="ImageTypeValue1Original" mbpo="true" StringDefinedTerms="PETCollimatorType"
	Name="CoincidenceWindowWidth"						Type="1C"	Condition="ImageTypeValue1Original" mbpo="true"
	Sequence="EnergyWindowRangeSequence"				Type="1C"	VM="1-n"	Condition="ImageTypeValue1Original" mbpo="true"
		Name="EnergyWindowLowerLimit"					Type="1"
		Name="EnergyWindowUpperLimit"					Type="1"
	SequenceEnd
	Name="TableMotion"									Type="1"	StringEnumValues="TableMotion"
	Name="TimeOfFlightInformationUsed"					Type="1"	StringEnumValues="TrueFalseFull"
	InvokeMacro="MandatoryViewAndSliceProgressionDirectionMacro"
	Name="IsocenterPosition"							Type="3"
ModuleEnd

Module="EnhancedPETImage"
	Name="ImageType"									Type="1"	VM="4"
	Verify="ImageType"											ValueSelector="0"	StringEnumValues="CommonEnhancedImageType1"
	Verify="ImageType"											ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
	Verify="ImageType"											ValueSelector="2"	StringDefinedTerms="CommonEnhancedImageAndFrameType3"
	Verify="ImageType"											ValueSelector="3"	StringDefinedTerms="CommonEnhancedImageType4"
	InvokeMacro="CommonCTMRImageDescriptionImageLevelMacro"
	Name="AcquisitionNumber"							Type="3"
	Name="AcquisitionDateTime"							Type="1C"	Condition="ImageTypeValue1OriginalAndNotLegacyConvertedPET" mbpo="true"
	Name="AcquisitionDuration"							Type="1C"	Condition="ImageTypeValue1OriginalAndNotLegacyConvertedPET" mbpo="true"
	Sequence="ReferencedRawDataSequence"				Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedWaveformSequence"				Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedImageEvidenceSequence"			Type="1C"	VM="1-n"	Condition="ReferencedImageSequenceIsPresentInFunctionalGroups"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="SourceImageEvidenceSequence"				Type="1C"	VM="1-n"	Condition="SourceImageSequenceIsPresentInFunctionalGroups"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Name="SamplesPerPixel"							Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"				Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"							Type="1"	BinaryEnumValues="BitsAre16"
	Name="BitsStored"								Type="1"	BinaryEnumValues="BitsAre16"
	Name="HighBit"									Type="1"	BinaryEnumValues="BitsAre15"
	Name="ContentQualification"						Type="1"	StringEnumValues="ContentQualification"
	Name="ImageComments"							Type="3"
	Name="BurnedInAnnotation"						Type="1C"	StringEnumValues="NoFull"	Condition="NotLegacyConvertedPET" mbpo="true"
	Name="RecognizableVisualFeatures"				Type="3"	StringEnumValues="YesNoFull"
	Name="LossyImageCompression"					Type="1C"	StringEnumValues="LossyImageCompression"	Condition="NotLegacyConvertedPET" mbpo="true"
	Name="LossyImageCompressionRatio"				Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"				Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"						Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="PresentationLUTShape"						Type="1"	StringEnumValues="IdentityPresentationLUTShape"
	Sequence="IconImageSequence"					Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
ModuleEnd

Module="EnhancedPETCorrections"
	Name="CountsSource"									Type="1"	StringEnumValues="CountsSource"
	Name="DecayCorrected"								Type="1"	StringEnumValues="YesNoFull"
	Name="AttenuationCorrected"							Type="1"	StringEnumValues="YesNoFull"
	Name="ScatterCorrected"								Type="1"	StringEnumValues="YesNoFull"
	Name="DeadTimeCorrected"							Type="1"	StringEnumValues="YesNoFull"
	Name="GantryMotionCorrected"						Type="1"	StringEnumValues="YesNoFull"
	Name="PatientMotionCorrected"						Type="1"	StringEnumValues="YesNoFull"
	Name="CountLossNormalizationCorrected"				Type="1"	StringEnumValues="YesNoFull"
	Name="RandomsCorrected"								Type="1"	StringEnumValues="YesNoFull"
	Name="NonUniformRadialSamplingCorrected"			Type="1"	StringEnumValues="YesNoFull"
	Name="SensitivityCalibrated"						Type="1"	StringEnumValues="YesNoFull"
	Name="DetectorNormalizationCorrection"				Type="1"	StringEnumValues="YesNoFull"
	Name="RandomsCorrectionMethod"						Type="1C"	Condition="IsRandomsCorrected"	StringDefinedTerms="RandomsCorrectionMethodEnhanced"
	Name="AttenuationCorrectionSource"					Type="1C"	Condition="IsAttenuationCorrected"	StringDefinedTerms="AttenuationCorrectionSource"
	Name="AttenuationCorrectionTemporalRelationship"	Type="1C"	Condition="IsAttenuationCorrected"	StringDefinedTerms="AttenuationCorrectionTemporalRelationship"
	Name="ScatterCorrectionMethod"						Type="1C"	Condition="IsScatterCorrected"
	Name="DecayCorrectionDateTime"						Type="1C"	Condition="IsDecayCorrected"
ModuleEnd

DefineMacro="BeamLimitingDevicePositionMacro"
	Sequence="BeamLimitingDevicePositionSequence"				Type="1C"	VM="1-n"	NoCondition=""
		Name="RTBeamLimitingDeviceType"							Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
		Name="LeafJawPositions"									Type="1"
	SequenceEnd
MacroEnd

DefineMacro="PatientSupportIdentificationMacro"
	Name="PatientSupportType"									Type="1"	StringDefinedTerms="PatientSupportType"
	Name="PatientSupportID"										Type="3"
	Name="PatientSupportAccessoryCode"							Type="3"
MacroEnd

Module="RTSeries"
	Name="Modality"										Type="1"	StringEnumValues="RTModality"
	Name="SeriesInstanceUID"							Type="1"
	Name="SeriesNumber"									Type="2"
	Name="SeriesDescription"							Type="3"
	Name="SeriesDate"									Type="3"
	Name="SeriesTime"									Type="3"
	Sequence="SeriesDescriptionCodeSequence"			Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="OperatorsName"								Type="2"
	Sequence="OperatorIdentificationSequence"			Type="3"	VM="1-n"
		InvokeMacro="PersonIdentificationMacro"
	SequenceEnd
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="RequestAttributesSequence"				Type="3"	VM="1-n"
		InvokeMacro="RequestAttributesMacro"
	SequenceEnd
	InvokeMacro="PerformedProcedureStepSummaryMacro"
ModuleEnd

Module="RTImage"
	Name="SamplesPerPixel"								Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"					Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"								Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"									Type="1"	BinaryEnumValues="BitsAre8Or12To16"	#should real be 8 if BitsAllocated is 8 and 12 to 16 if BitsAllocated is 16
	Name="HighBit"										Type="1"	BinaryEnumValues="BitsAre7Or11To15"	#should real be one less than BitsStored
	Name="PixelRepresentation"							Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="PixelIntensityRelationship"					Type="1"	StringEnumValues="DXPixelIntensityRelationship"
	Name="PixelIntensityRelationshipSign"				Type="1"	BinaryEnumValues="PixelIntensityRelationshipSign"
	Name="RTImageLabel"									Type="1"
	Name="RTImageName"									Type="3"
	Name="RTImageDescription"							Type="3"
	Name="ImageType"									Type="1"	ValueSelector="2"	StringDefinedTerms="RTImageTypeValue3"
	Verify="ImageType"									Condition="ImageTypeValue3MissingOrEmpty"	ThenErrorMessage="A value is required for value 3 in RT Images"
	Name="ConversionType"								Type="2"	StringDefinedTerms="ConversionType"
	Name="ReportedValuesOrigin"							Type="2C"	Condition="ImageTypeValue3SimulatorOrPortal"	StringEnumValues="ReportedValuesOrigin"
	Name="RTImagePlane"									Type="1"	StringEnumValues="RTImagePlane"
	Name="XRayImageReceptorAngle"						Type="2"
	Name="RTImageOrientation"							Type="2C"	Condition="RTImagePlaneIsNonNormal" mbpo="true"
	Name="ImagePlanePixelSpacing"						Type="2"	NotZeroError=""
	Name="RTImagePosition"								Type="2"
	Name="RadiationMachineName"							Type="2"
	Name="PrimaryDosimeterUnit"							Type="2"	StringEnumValues="PrimaryDosimeterUnit"
	Name="RadiationMachineSAD"							Type="2"
	Name="RadiationMachineSSD"							Type="3"
	Name="RTImageSID"									Type="2"
	Name="SourceToReferenceObjectDistance"				Type="3"
	Sequence="ReferencedRTPlanSequence"					Type="3"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Name="ReferencedBeamNumber"							Type="3"
	Name="ReferencedFractionGroupNumber"				Type="3"
	Name="FractionNumber"								Type="3"
	Name="StartCumulativeMetersetWeight"				Type="3"
	Name="EndCumulativeMetersetWeight"					Type="3"
	Sequence="ExposureSequence"							Type="3"	VM="1-n"
		Name="ReferencedFrameNumber"					Type="1C"	Condition="NeedExposureSequenceReferencedFrameNumber"	NotZeroError=""
		Name="KVP"										Type="2C"	Condition="ImageTypeValue3SimulatorOrPortalOrRadiograph"
		Sequence="PrimaryFluenceModeSequence"			Type="3"	VM="1"
			Name="FluenceMode"							Type="1"	StringEnumValues="FluenceMode"
			Name="FluenceModeID"						Type="1C"	Condition="FluenceModeIsNonStandard"
		SequenceEnd
		Name="XRayTubeCurrent"							Type="2C"	Condition="ImageTypeValue3SimulatorOrRadiograph"
		Name="XRayTubeCurrentInmA"						Type="3"
		Name="ExposureTime"								Type="2C"	Condition="ImageTypeValue3SimulatorOrRadiograph"
		Name="ExposureTimeInms"							Type="3"
		Name="MetersetExposure"							Type="2C"	Condition="ImageTypeValue3Portal"
		Name="DiaphragmPosition"						Type="3"
		Sequence="BeamLimitingDeviceSequence"			Type="3"	VM="1-n"
			Name="RTBeamLimitingDeviceType"				Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
			Name="SourceToBeamLimitingDeviceDistance"	Type="3"
			Name="NumberOfLeafJawPairs"					Type="1"
			Name="LeafPositionBoundaries"				Type="2C"	Condition="RTBeamLimitingDeviceTypeMLCXOrMLCY" mbpo="true"
			Name="LeafJawPositions"						Type="1"
		SequenceEnd
		Sequence="ApplicatorSequence"					Type="3"	VM="1"
			Name="ApplicatorID"							Type="1"
			Name="ApplicatorType"						Type="1"	StringDefinedTerms="ApplicatorType"
			Name="ApplicatorDescription"				Type="3"
		SequenceEnd
		Sequence="GeneralAccessorySequence"				Type="3"	VM="1-n"
			Name="GeneralAccessoryNumber"				Type="1"
			Name="GeneralAccessoryID"					Type="1"
			Name="GeneralAccessoryDescription"			Type="3"
			Name="GeneralAccessoryType"					Type="3"	StringDefinedTerms="RTGeneralAccessoryType"
			Name="AccessoryCode"						Type="3"
			Name="SourceToGeneralAccessoryDistance"		Type="3"
		SequenceEnd
		Name="NumberOfBlocks"							Type="1"
		Sequence="BlockSequence"						Type="2C"	VM="0-n"	Condition="NumberOfBlocksNotZero"
			Name="BlockTrayID"							Type="3"
			Name="TrayAccessoryCode"					Type="3"
			Name="AccessoryCode"						Type="3"
			Name="SourceToBlockTrayDistance"			Type="2"
			Name="BlockType"							Type="1"	StringEnumValues="BlockType"
			Name="BlockDivergence"						Type="2"	StringEnumValues="BlockDivergence"
			Name="BlockMountingPosition"				Type="3"	StringEnumValues="BlockMountingPosition"
			Name="BlockNumber"							Type="1"
			Name="BlockName"							Type="3"
			Name="MaterialID"							Type="2"
			Name="BlockThickness"						Type="3"
			Name="BlockNumberOfPoints"					Type="2"
			Name="BlockData"							Type="2"
		SequenceEnd
	SequenceEnd
	Sequence="FluenceMapSequence"						Type="1C"	VM="1"	Condition="ImageTypeValue3Fluence"
		Name="FluenceDataSource"						Type="1"	StringEnumValues="FluenceDataSource"
		Name="FluenceDataScale"							Type="3"
	SequenceEnd
	Name="GantryAngle"									Type="3"
	Name="GantryPitchAngle"								Type="3"
	Name="BeamLimitingDeviceAngle"						Type="3"
	Name="PatientSupportAngle"							Type="3"
	Name="TableTopEccentricAxisDistance"				Type="3"
	Name="TableTopEccentricAngle"						Type="3"
	Name="TableTopPitchAngle"							Type="3"
	Name="TableTopRollAngle"							Type="3"
	Name="TableTopVerticalPosition"						Type="3"
	Name="TableTopLongitudinalPosition"					Type="3"
	Name="TableTopLateralPosition"						Type="3"
	Name="IsocenterPosition"							Type="3"
	Name="PatientPosition"								Type="1C"	Condition="IsocenterPositionIsPresent"
	Name="ExposureTime"									Type="3"
	Name="ExposureTimeInms"								Type="3"
	Name="MetersetExposure"								Type="3"
ModuleEnd

Module="RTDose"
	Name="SamplesPerPixel"										Type="1C"	Condition="PixelDataPresent"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"							Type="1C"	Condition="PixelDataPresent"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"										Type="1C"	Condition="PixelDataPresent"	BinaryEnumValues="BitsAre16Or32"
	Name="BitsStored"											Type="1C"	Condition="PixelDataPresent"	BinaryEnumValues="BitsAre16Or32"	#should real be same as BitsAllocated
	Name="HighBit"												Type="1C"	Condition="PixelDataPresent"	BinaryEnumValues="BitsAre15Or31"	#should real be one less than BitsStored
	Name="PixelRepresentation"									Type="1C"	Condition="PixelDataPresent"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="ContentDate"											Type="3"
	Name="ContentTime"											Type="3"
	Name="DoseUnits"											Type="1"	StringEnumValues="DoseUnits"
	Name="DoseType"												Type="1"	StringDefinedTerms="DoseType"
	Name="SpatialTransformOfDose"								Type="3"	StringDefinedTerms="SpatialTransformOfDose"
	Sequence="ReferencedSpatialRegistrationSequence"			Type="2C"	VM="0-n"		Condition="SpatialTransformOfDoseIsRigidOrNonRigid"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Name="InstanceNumber"										Type="3"
	Name="DoseComment"											Type="3"
	Name="NormalizationPoint"									Type="3"
	Name="DoseSummationType"									Type="1"	StringDefinedTerms="DoseSummationType"
	Sequence="ReferencedRTPlanSequence"							Type="1C"	VM="1-n"		Condition="NeedReferencedRTPlanSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="ReferencedFractionGroupSequence"				Type="1C"	VM="1"		Condition="NeedReferencedFractionGroupSequence"
			Name="ReferencedFractionGroupNumber"				Type="1"
			Sequence="ReferencedBeamSequence"					Type="1C"	VM="1-n"	Condition="NeedReferencedBeamSequence"
				Name="ReferencedBeamNumber"						Type="1"
				Sequence="ReferencedControlPointSequence"		Type="1C"	VM="1"		Condition="DoseSummationTypeControlPoint"
					Name="ReferencedStartControlPointIndex"		Type="1"
					Name="ReferencedStopControlPointIndex"		Type="1"
				SequenceEnd
			SequenceEnd
			Sequence="ReferencedBrachyApplicationSetupSequence"	Type="1C"	VM="1-n"	Condition="NeedReferencedBrachyApplicationSetupSequence"
				Name="ReferencedBrachyApplicationSetupNumber"	Type="1"
			SequenceEnd
		SequenceEnd
	SequenceEnd
	Verify="ReferencedRTPlanSequence"										Condition="DoseSummationTypeIsNotMultiPlanAndReferencedRTPlanSequenceHasMultipleItems"	ThenErrorMessage="Multiple items not permitted unless DoseSummationType is MULTI_PLAN"
	Verify="ReferencedRTPlanSequence"										Condition="DoseSummationTypeIsMultiPlanAndReferencedRTPlanSequenceHasLessThanTwoItems"	ThenErrorMessage="Two or more items required if DoseSummationType is MULTI_PLAN"
	Name="GridFrameOffsetVector"								Type="1C"	Condition="NeedGridFrameOffsetVector"
	Name="DoseGridScaling"										Type="1C"	Condition="PixelDataPresent"
	Name="TissueHeterogeneityCorrection"						Type="3"	StringEnumValues="TissueHeterogeneityCorrection"
ModuleEnd

Module="RTDVH"
	Sequence="ReferencedStructureSetSequence"					Type="1"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Name="DVHNormalizationPoint"								Type="3"
	Name="DVHNormalizationDoseValue"							Type="3"
	Sequence="DVHSequence"										Type="1"	VM="1-n"
		Sequence="DVHReferencedROISequence"						Type="1"	VM="1-n"
			Name="ReferencedROINumber"							Type="1"
			Name="DVHROIContributionType"						Type="1"	StringEnumValues="DVHROIContributionType"
		SequenceEnd
		Name="DVHType"											Type="1"	StringEnumValues="DVHType"
		Name="DoseUnits"										Type="1"	StringEnumValues="DVHDoseUnits"
		Name="DoseType"											Type="1"	StringDefinedTerms="DVHDoseType"
		Name="DVHDoseScaling"									Type="1"
		Name="DVHVolumeUnits"									Type="1"	StringDefinedTerms="DVHVolumeUnits"
		Name="DVHNumberOfBins"									Type="1"
		Name="DVHData"											Type="1"
		Name="DVHMinimumDose"									Type="3"
		Name="DVHMaximumDose"									Type="3"
		Name="DVHMeanDose"										Type="3"
	SequenceEnd
ModuleEnd

Module="StructureSet"
	Name="StructureSetLabel"									Type="1"
	Name="StructureSetName"										Type="3"
	Name="StructureSetDescription"								Type="3"
	Name="InstanceNumber"										Type="3"
	Name="StructureSetDate"										Type="2"
	Name="StructureSetTime"										Type="2"
	Sequence="ReferencedFrameOfReferenceSequence"				Type="3"	VM="1-n"
		Name="FrameOfReferenceUID"								Type="1"
		Sequence="FrameOfReferenceRelationshipSequence"			Type="3"	VM="1-n"
			Name="RelatedFrameOfReferenceUID"					Type="1"
			Name="FrameOfReferenceTransformationType"			Type="1"	StringDefinedTerms="TransformationType"
			Name="FrameOfReferenceTransformationMatrix"			Type="1"
			Name="FrameOfReferenceTransformationComment"		Type="3"
		SequenceEnd
		Sequence="RTReferencedStudySequence"					Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
			Sequence="RTReferencedSeriesSequence"				Type="1"	VM="1-n"
				Name="SeriesInstanceUID"						Type="1"
				Sequence="ContourImageSequence"					Type="1"	VM="1-n"
					InvokeMacro="ImageSOPInstanceReferenceMacro"
				SequenceEnd
			SequenceEnd
		SequenceEnd
	SequenceEnd
	Sequence="StructureSetROISequence"							Type="1"	VM="1-n"
		Name="ROINumber"										Type="1"
		Name="ReferencedFrameOfReferenceUID"					Type="1"
		Name="ROIName"											Type="2"
		Name="ROIDescription"									Type="3"
		Name="ROIVolume"										Type="3"
		Name="ROIGenerationAlgorithm"							Type="2"	StringDefinedTerms="ROIGenerationAlgorithm"
		Name="ROIGenerationDescription"							Type="3"
		Sequence="ROIDerivationAlgorithmIdentificationSequence"	Type="3"	VM="1"
			InvokeMacro="AlgorithmIdentificationMacro"
		SequenceEnd
		Sequence="DerivationCodeSequence"						Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="DefinitionSourceSequence"						Type="3"	VM="1"
			InvokeMacro="SOPInstanceReferenceMacro"
			Name="ReferencedSegmentNumber"						Type="1C"	Condition="ReferencedSOPClassUIDIsSegmentationStorage"
			Name="ReferencedFiducialUID"						Type="1C"	Condition="ReferencedSOPClassUIDIsSpatialFiducialsStorage"
		SequenceEnd
	SequenceEnd
	Sequence="PredecessorStructureSetSequence"					Type="3"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="ROIContour"
	Sequence="ROIContourSequence"								Type="1"	VM="1-n"
		Name="ReferencedROINumber"								Type="1"
		Name="ROIDisplayColor"									Type="3"
		Sequence="ContourSequence"								Type="3"	VM="1-n"
			Name="ContourNumber"								Type="3"
			Name="AttachedContours"								Type="3"
			Sequence="ContourImageSequence"						Type="3"	VM="1-n"
				InvokeMacro="ImageSOPInstanceReferenceMacro"
			SequenceEnd
			Name="ContourGeometricType"							Type="1"	StringEnumValues="ContourGeometricType"
			Name="ContourSlabThickness"							Type="3"
			Name="ContourOffsetVector"							Type="3"
			Name="NumberOfContourPoints"						Type="1"
			Name="ContourData"									Type="1"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="RTDoseROI"
	Sequence="RTDoseROISequence"								Type="1"	VM="1-n"
		Name="ReferencedROINumber"								Type="1"
		Name="DoseUnits"										Type="1"	StringEnumValues="DoseUnits"
		Name="DoseValue"										Type="1"
	SequenceEnd
ModuleEnd

Module="RTROIObservations"
	Sequence="RTROIObservationsSequence"						Type="1"	VM="1-n"
		Name="ObservationNumber"								Type="1"
		Name="ReferencedROINumber"								Type="1"
		Name="ROIObservationLabel"								Type="3"
		Name="ROIObservationDescription"						Type="3"
		Sequence="RTRelatedROISequence"							Type="3"	VM="1-n"
			Name="ReferencedROINumber"							Type="1"
			Name="RTROIRelationship"							Type="3"	StringDefinedTerms="RTROIRelationship"
		SequenceEnd
		Sequence="RTROIIdentificationCodeSequence"				Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
			Sequence="SegmentedPropertyTypeModifierCodeSequence"	Type="3"	VM="1-n"
				InvokeMacro="CodeSequenceMacro"								BaselineContextID="244"
			SequenceEnd
		SequenceEnd
		Sequence="RelatedRTROIObservationsSequence"				Type="3"	VM="1-n"
			Name="ObservationNumber"							Type="1"
		SequenceEnd
		Name="RTROIInterpretedType"								Type="2"	StringDefinedTerms="RTROIInterpretedType"
		Name="ROIInterpreter"									Type="2"
		Name="MaterialID"										Type="3"
		Sequence="ROIPhysicalPropertiesSequence"				Type="3"	VM="1-n"
			Name="ROIPhysicalProperty"							Type="1"	StringDefinedTerms="ROIPhysicalProperty"
			Sequence="ROIElementalCompositionSequence"				Type="1C"	VM="1-n"	Condition="ROIPhysicalPropertyIsElemFraction"
				Name="ROIElementalCompositionAtomicNumber"			Type="1"
				Name="ROIElementalCompositionAtomicMassFraction"	Type="1"
			SequenceEnd
			Name="ROIPhysicalPropertyValue"						Type="1"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="RTGeneralPlan"
	Name="RTPlanLabel"											Type="1"
	Name="RTPlanName"											Type="3"
	Name="RTPlanDescription"									Type="3"
	Name="InstanceNumber"										Type="3"
	Name="RTPlanDate"											Type="2"
	Name="RTPlanTime"											Type="2"
	Name="TreatmentProtocols"									Type="3"
	Name="PlanIntent"											Type="3"	StringDefinedTerms="PlanIntent"
	Name="TreatmentSites"										Type="3"
	Name="RTPlanGeometry"										Type="1"	StringDefinedTerms="RTPlanGeometry"
	Sequence="ReferencedStructureSetSequence"					Type="1C"	VM="1"	Condition="RTPlanGeometryIsPatient"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedDoseSequence"							Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedRTPlanSequence"							Type="3"`	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
		Name="RTPlanRelationship"								Type="1"	StringDefinedTerms="RTPlanRelationship"
		Verify="RTPlanRelationship"											Condition="PlanIntentIsVerification" StringDefinedTerms="RTPlanRelationshipVerifiedPlan"
	SequenceEnd
	Name="FrameOfReferenceToDisplayedCoordinateSystemTransformationMatrix"	Type="3"
ModuleEnd

Module="RTPrescription"
	Name="PrescriptionDescription"								Type="3"
	Sequence="DoseReferenceSequence"							Type="3"	VM="1-n"
		Name="DoseReferenceNumber"								Type="1"
		Name="DoseReferenceUID"									Type="3"
		Name="DoseReferenceStructureType"						Type="1"	StringDefinedTerms="DoseReferenceStructureType"
		Name="DoseReferenceDescription"							Type="3"
		Name="ReferencedROINumber"								Type="1C"	Condition="DoseReferenceStructureTypePointOrVolume"
		Name="DoseReferencePointCoordinates"					Type="1C"	Condition="DoseReferenceStructureTypeCoordinates"
		Name="NominalPriorDose"									Type="3"
		Name="DoseReferenceType"								Type="1"	StringDefinedTerms="DoseReferenceType"
		Name="ConstraintWeight"									Type="3"
		Name="DeliveryWarningDose"								Type="3"
		Name="DeliveryMaximumDose"								Type="3"
		Name="TargetMinimumDose"								Type="3"
		Name="TargetPrescriptionDose"							Type="3"
		Name="TargetMaximumDose"								Type="3"
		Name="TargetUnderdoseVolumeFraction"					Type="3"
		Name="OrganAtRiskFullVolumeDose"						Type="3"
		Name="OrganAtRiskLimitDose"								Type="3"
		Name="OrganAtRiskMaximumDose"							Type="3"
		Name="OrganAtRiskOverdoseVolumeFraction"				Type="3"
	SequenceEnd
ModuleEnd

Module="RTToleranceTables"
	Sequence="ToleranceTableSequence"							Type="3"	VM="1-n"
		Name="ToleranceTableNumber"								Type="1"
		Name="ToleranceTableLabel"								Type="3"
		Name="GantryAngleTolerance"								Type="3"
		Name="GantryPitchAngleTolerance"						Type="3"
		Name="BeamLimitingDeviceAngleTolerance"					Type="3"
		Sequence="BeamLimitingDeviceToleranceSequence"			Type="3"	VM="1-n"
			Name="RTBeamLimitingDeviceType"						Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
			Name="BeamLimitingDevicePositionTolerance"			Type="1"
		SequenceEnd
		Name="PatientSupportAngleTolerance"						Type="3"
		Name="TableTopEccentricAngleTolerance"					Type="3"
		Name="TableTopPitchAngleTolerance"						Type="3"
		Name="TableTopRollAngleTolerance"						Type="3"
		Name="TableTopVerticalPositionTolerance"				Type="3"
		Name="TableTopLongitudinalPositionTolerance"			Type="3"
		Name="TableTopLateralPositionTolerance"					Type="3"
	SequenceEnd
ModuleEnd

Module="RTPatientSetup"
	Sequence="PatientSetupSequence"								Type="1"	VM="1-n"
		Name="PatientSetupNumber"								Type="1"
		Name="PatientSetupLabel"								Type="3"
		Name="PatientPosition"									Type="1C"	Condition="PatientAdditionalPositionNotPresent"		StringDefinedTerms="RTPatientPosition"
		Name="PatientAdditionalPosition"						Type="1C"	Condition="PatientPositionNotPresent"
		Sequence="ReferencedSetupImageSequence"					Type="3"	VM="1-n"
			Name="SetupImageComment"							Type="3"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="FixationDeviceSequence"						Type="3"	VM="1-n"
			Name="FixationDeviceType"							Type="1"	StringDefinedTerms="FixationDeviceType"
			Name="FixationDeviceLabel"							Type="2"
			Name="FixationDeviceDescription"					Type="3"
			Name="FixationDevicePosition"						Type="3"
			Name="FixationDevicePitchAngle"						Type="3"
			Name="FixationDeviceRollAngle"						Type="3"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Sequence="ShieldingDeviceSequence"						Type="3"	VM="1-n"
			Name="ShieldingDeviceType"							Type="1"	StringDefinedTerms="ShieldingDeviceType"
			Name="ShieldingDeviceLabel"							Type="2"
			Name="ShieldingDeviceDescription"					Type="3"
			Name="ShieldingDevicePosition"						Type="3"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Name="SetupTechnique"									Type="3"	StringDefinedTerms="SetupTechnique"
		Name="SetupTechniqueDescription"						Type="3"
		Sequence="SetupDeviceSequence"							Type="3"	VM="1-n"
			Name="SetupDeviceType"								Type="1"	StringDefinedTerms="SetupDeviceType"
			Name="SetupDeviceLabel"								Type="2"
			Name="SetupDeviceDescription"						Type="3"
			Name="SetupDeviceParameter"							Type="2"
			Name="SetupReferenceDescription"					Type="3"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Name="TableTopVerticalSetupDisplacement"				Type="3"
		Name="TableTopLongitudinalSetupDisplacement"			Type="3"
		Name="TableTopLateralSetupDisplacement"					Type="3"
		Sequence="MotionSynchronizationSequence"				Type="3"	VM="1-n"
			Name="RespiratoryMotionCompensationTechnique"		Type="1"	StringDefinedTerms="RTRespiratoryMotionCompensationTechnique"
			Name="RespiratorySignalSource"						Type="1"	StringDefinedTerms="RTRespiratorySignalSource"
			Name="RespiratoryMotionCompensationTechniqueDescription"	Type="3"
			Name="RespiratorySignalSourceID"					Type="3"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="RTFractionScheme"
	Sequence="FractionGroupSequence"							Type="1"	VM="1-n"
		Name="FractionGroupNumber"								Type="1"
		Name="FractionGroupDescription"							Type="3"
		Sequence="ReferencedDoseSequence"						Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="ReferencedDoseReferenceSequence"				Type="3"	VM="1-n"
			Name="ReferencedDoseReferenceNumber"				Type="1"
			Name="ConstraintWeight"								Type="3"
			Name="DeliveryWarningDose"							Type="3"
			Name="DeliveryMaximumDose"							Type="3"
			Name="TargetMinimumDose"							Type="3"
			Name="TargetPrescriptionDose"						Type="3"
			Name="TargetMaximumDose"							Type="3"
			Name="TargetUnderdoseVolumeFraction"				Type="3"
			Name="OrganAtRiskFullVolumeDose"					Type="3"
			Name="OrganAtRiskLimitDose"							Type="3"
			Name="OrganAtRiskMaximumDose"						Type="3"
			Name="OrganAtRiskOverdoseVolumeFraction"			Type="3"
		SequenceEnd
		Name="NumberOfFractionsPlanned"							Type="2"
		Name="NumberOfFractionPatternDigitsPerDay"				Type="3"
		Name="RepeatFractionCycleLength"						Type="3"
		Name="FractionPattern"									Type="3"
		Name="BeamDoseMeaning"									Type="3"	StringEnumValues="BeamDoseMeaning"
		Name="NumberOfBeams"									Type="1"
		Sequence="ReferencedBeamSequence"						Type="1C"	VM="1-n"	Condition="NumberOfBeamsNotZero"
			Name="ReferencedBeamNumber"							Type="1"
			Name="BeamDoseSpecificationPoint"					Type="3"
			Name="ReferencedDoseReferenceUID"					Type="3"
			Name="BeamDose"										Type="3"
			Name="BeamDoseType"									Type="1C"	Condition="AlternateBeamDosePresent"	StringEnumValues="BeamDoseType"	mbpo="true"
			Verify="BeamDoseType"											Condition="AlternateBeamDoseTypeSameValueAsBeamDoseType"	ThenErrorMessage="A different value than AlternateBeamDoseType is required"
			Name="AlternateBeamDose"							Type="3"
			Name="AlternateBeamDoseType"						Type="1C"	Condition="AlternateBeamDosePresent"	StringEnumValues="BeamDoseType"
			Verify="AlternateBeamDoseType"									Condition="AlternateBeamDoseTypeSameValueAsBeamDoseType"	ThenErrorMessage="A different value than BeamDoseType is required"
			Sequence="BeamDoseVerificationControlPointSequence"	Type="3"	VM="2-n"
				Name="CumulativeMetersetWeight"					Type="1"
				Name="ReferencedControlPointIndex"				Type="1C"	NoCondition=""		# Required if the Referenced Cumulative Meterset corresponds to a Control Point in the Control Point Sequence:(
				Name="AverageBeamDosePointDepth"				Type="2C"	NoCondition=""		# Required for all but the last items in that sequence :(
				Name="AverageBeamDosePointEquivalentDepth"		Type="2C"	NoCondition=""		# Required for all but the last items in that sequence :(
				Name="AverageBeamDosePointSSD"					Type="2C"	NoCondition=""		# Required for all but the last items in that sequence :(
			SequenceEnd
			Name="BeamMeterset"									Type="3"
		SequenceEnd
		Name="NumberOfBrachyApplicationSetups"					Type="1"
		Sequence="ReferencedBrachyApplicationSetupSequence"		Type="1C"	VM="1-n"	Condition="NumberOfBrachyApplicationSetupsNotZero"
			Name="ReferencedBrachyApplicationSetupNumber"		Type="1"
			Name="BrachyApplicationSetupDoseSpecificationPoint"	Type="3"
			Name="BrachyApplicationSetupDose"					Type="3"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="RTBeams"
	Sequence="BeamSequence"										Type="1"	VM="1-n"
		Name="BeamNumber"										Type="1"
		Name="BeamName"											Type="3"
		Name="BeamDescription"									Type="3"
		Name="BeamType"											Type="1"	StringEnumValues="BeamType"
		Name="RadiationType"									Type="2"	StringDefinedTerms="RadiationType"
		Sequence="PrimaryFluenceModeSequence"					Type="3"	VM="1"
			Name="FluenceMode"									Type="1"	StringEnumValues="FluenceMode"
			Name="FluenceModeID"								Type="1C"	Condition="FluenceModeIsNonStandard"
		SequenceEnd
		Name="HighDoseTechniqueType"							Type="1C"	StringDefinedTerms="HighDoseTechniqueType"	NoCondition="" # real-world
		Name="TreatmentMachineName"								Type="2"
		Name="Manufacturer"										Type="3"
		Name="InstitutionName"									Type="3"
		Name="InstitutionAddress"								Type="3"
		Name="InstitutionalDepartmentName"						Type="3"
		Sequence="InstitutionalDepartmentTypeCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"									BaselineContextID="7030"
		SequenceEnd
		Name="ManufacturerModelName"							Type="3"
		Name="DeviceSerialNumber"								Type="3"
		Name="PrimaryDosimeterUnit"								Type="3"	StringEnumValues="PrimaryDosimeterUnit"
		Name="ReferencedToleranceTableNumber"					Type="3"
		Name="SourceAxisDistance"								Type="3"
		Sequence="BeamLimitingDeviceSequence"					Type="1"	VM="1-n"
			Name="RTBeamLimitingDeviceType"						Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
			Name="SourceToBeamLimitingDeviceDistance"			Type="3"
			Name="NumberOfLeafJawPairs"							Type="1"
			Name="LeafPositionBoundaries"						Type="2C"	Condition="RTBeamLimitingDeviceTypeMLCXOrMLCY" mbpo="true"
		SequenceEnd
		Name="ReferencedPatientSetupNumber"						Type="3"
		Sequence="ReferencedReferenceImageSequence"				Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
			Name="ReferenceImageNumber"							Type="1"
			Name="StartCumulativeMetersetWeight"				Type="3"
			Name="EndCumulativeMetersetWeight"					Type="3"
		SequenceEnd
		Sequence="PlannedVerificationImageSequence"				Type="3"	VM="1-n"
			Name="StartCumulativeMetersetWeight"				Type="3"
			Name="MetersetExposure"								Type="3"
			Name="EndCumulativeMetersetWeight"					Type="3"
			Name="RTImagePlane"									Type="3"	StringEnumValues="RTImagePlane"
			Name="XRayImageReceptorAngle"						Type="3"
			Name="RTImageOrientation"							Type="3"
			Name="RTImagePosition"								Type="3"
			Name="RTImageSID"									Type="3"
			Name="ImagingDeviceSpecificAcquisitionParameters"	Type="3"
			Name="ReferencedReferenceImageNumber"		Type="3"
		SequenceEnd
		Name="TreatmentDeliveryType"							Type="3"	StringDefinedTerms="TreatmentDeliveryType"
		Sequence="ReferencedDoseSequence"						Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Name="NumberOfWedges"									Type="1"
		Sequence="WedgeSequence"								Type="1C"	VM="1-n"	Condition="NumberOfWedgesNotZero"
			Name="WedgeNumber"									Type="1"
			Name="WedgeType"									Type="2"	StringDefinedTerms="WedgeType"
			Name="WedgeID"										Type="3"
			Name="AccessoryCode"								Type="3"
			Name="WedgeAngle"									Type="2"
			Name="WedgeFactor"									Type="2"
			Name="WedgeOrientation"								Type="2"
			Name="SourceToWedgeTrayDistance"					Type="3"
		SequenceEnd
		Name="NumberOfCompensators"								Type="1"
		Name="TotalCompensatorTrayFactor"						Type="3"
		Sequence="CompensatorSequence"							Type="1C"	VM="1-n"	Condition="NumberOfCompensatorsNotZero"
			Name="CompensatorDescription"						Type="3"
			Name="CompensatorNumber"							Type="1"
			Name="MaterialID"									Type="2"
			Name="CompensatorID"								Type="3"
			Name="AccessoryCode"								Type="3"
			Name="CompensatorTrayID"							Type="3"
			Name="TrayAccessoryCode"							Type="3"
			Name="SourceToCompensatorTrayDistance"				Type="2"
			Name="CompensatorDivergence"						Type="3"	StringEnumValues="CompensatorDivergence"
			Name="CompensatorMountingPosition"					Type="3"	StringEnumValues="CompensatorMountingPosition"
			Name="CompensatorRows"								Type="1"
			Name="CompensatorColumns"							Type="1"
			Name="CompensatorPixelSpacing"						Type="1"	NotZeroError=""
			Name="CompensatorPosition"							Type="1"
			Name="CompensatorTransmissionData"					Type="1"
			Name="CompensatorThicknessData"						Type="1"
			Name="SourceToCompensatorDistance"					Type="1C"	Condition="NeedSourceToCompensatorDistance"
		SequenceEnd
		Name="NumberOfBoli"										Type="1"
		Sequence="ReferencedBolusSequence"						Type="1C"	VM="1-n"	Condition="NumberOfBoliNotZero"
			Name="ReferencedROINumber"							Type="1"
			Name="BolusID"										Type="3"
			Name="BolusDescription"								Type="3"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Name="NumberOfBlocks"									Type="1"
		Name="TotalBlockTrayFactor"								Type="3"
		Sequence="BlockSequence"								Type="1C"	VM="1-n"	Condition="NumberOfBlocksNotZero"
			Name="BlockTrayID"									Type="3"
			Name="TrayAccessoryCode"							Type="3"
			Name="AccessoryCode"								Type="3"
			Name="SourceToBlockTrayDistance"					Type="2"
			Name="BlockType"									Type="1"	StringEnumValues="BlockType"
			Name="BlockDivergence"								Type="2"	StringEnumValues="BlockDivergence"
			Name="BlockMountingPosition"						Type="3"	StringEnumValues="BlockMountingPosition"
			Name="BlockNumber"									Type="1"
			Name="BlockName"									Type="3"
			Name="MaterialID"									Type="2"
			Name="BlockThickness"								Type="2"
			Name="BlockTransmission"							Type="2"
			Name="BlockNumberOfPoints"							Type="2"
			Name="BlockData"									Type="2"
		SequenceEnd
		Sequence="ApplicatorSequence"							Type="3"	VM="1"
			Name="ApplicatorID"									Type="1"
			Name="AccessoryCode"								Type="3"
			Name="ApplicatorType"								Type="1"	StringDefinedTerms="ApplicatorType"
			Name="ApplicatorDescription"						Type="3"
			Sequence="GeneralAccessorySequence"					Type="3"	VM="1-n"
				Name="GeneralAccessoryNumber"					Type="1"
				Name="GeneralAccessoryID"						Type="1"
				Name="GeneralAccessoryDescription"				Type="3"
				Name="GeneralAccessoryType"						Type="3"	StringDefinedTerms="RTGeneralAccessoryType"
				Name="AccessoryCode"							Type="3"
				Name="SourceToGeneralAccessoryDistance"			Type="3"
			SequenceEnd
		SequenceEnd
		Name="FinalCumulativeMetersetWeight"					Type="1C"	NoCondition=""
		Name="NumberOfControlPoints"							Type="1"
		Sequence="ControlPointSequence"							Type="1"	VM="2-n"
			Name="ControlPointIndex"							Type="1"
			Name="CumulativeMetersetWeight"						Type="2"
			Sequence="ReferencedDoseReferenceSequence"			Type="3"	VM="1-n"
				Name="ReferencedDoseReferenceNumber"			Type="1"
				Name="CumulativeDoseReferenceCoefficient"		Type="2"
			SequenceEnd
			Sequence="ReferencedDoseSequence"					Type="1C"	VM="1-n"	Condition="DoseSummationTypeControlPoint"
				InvokeMacro="SOPInstanceReferenceMacro"
			SequenceEnd
			Name="NominalBeamEnergy"							Type="3"
			Name="DoseRateSet"									Type="3"
			Sequence="WedgePositionSequence"					Type="3"	VM="1-n"
				Name="ReferencedWedgeNumber"					Type="1"
				Name="WedgePosition"							Type="1"	StringEnumValues="WedgePosition"
			SequenceEnd
			Sequence="BeamLimitingDevicePositionSequence"		Type="1C"	VM="1-n"	NoCondition=""
				Name="RTBeamLimitingDeviceType"					Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
				Name="LeafJawPositions"							Type="1"
			SequenceEnd
			Name="GantryAngle"									Type="1C"	NoCondition=""
			Name="GantryRotationDirection"						Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="GantryPitchAngle"								Type="3"
			Name="GantryPitchRotationDirection"					Type="3"	StringEnumValues="RotationDirectionWithNone"
			Name="BeamLimitingDeviceAngle"						Type="1C"	NoCondition=""
			Name="BeamLimitingDeviceRotationDirection"			Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="PatientSupportAngle"							Type="1C"	NoCondition=""
			Name="PatientSupportRotationDirection"				Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopEccentricAxisDistance"				Type="3"
			Name="TableTopEccentricAngle"						Type="1C"	NoCondition=""
			Name="TableTopEccentricRotationDirection"			Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopPitchAngle"							Type="1C"	NoCondition=""
			Name="TableTopPitchRotationDirection"				Type="1C""	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopRollAngle"							Type="1C"	NoCondition=""
			Name="TableTopRollRotationDirection"				Type="1C""	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopVerticalPosition"						Type="2C"	NoCondition=""
			Name="TableTopLongitudinalPosition"					Type="2C"	NoCondition=""
			Name="TableTopLateralPosition"						Type="2C"	NoCondition=""
			Name="IsocenterPosition"							Type="2C"	NoCondition=""
			Name="SurfaceEntryPoint"							Type="3"
			Name="SourceToSurfaceDistance"						Type="3"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="RTBrachyApplicationSetups"
	Name="BrachyTreatmentTechnique"								Type="1"	StringEnumValues="BrachyTreatmentTechnique"
	Name="BrachyTreatmentType"									Type="1"	StringDefinedTerms="BrachyTreatmentType"
	Sequence="TreatmentMachineSequence"							Type="1"	VM="1"
		Name="TreatmentMachineName"								Type="2"
		Name="Manufacturer"										Type="3"
		Name="InstitutionName"									Type="3"
		Name="InstitutionAddress"								Type="3"
		Name="InstitutionalDepartmentName"						Type="3"
		Sequence="InstitutionalDepartmentTypeCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"									BaselineContextID="7030"
		SequenceEnd
		Name="ManufacturerModelName"							Type="3"
		Name="DeviceSerialNumber"								Type="3"
	SequenceEnd
	Sequence="SourceSequence"									Type="1"	VM="1-n"
		Name="SourceNumber"										Type="1"
		Name="SourceSerialNumber"								Type="3"
		Name="SourceModelID"									Type="3"
		Name="SourceDescription"								Type="3"
		Name="SourceType"										Type="1"
		Name="SourceManufacturer"								Type="3"
		Name="ActiveSourceDiameter"								Type="3"
		Name="ActiveSourceLength"								Type="3"
		Name="MaterialID"										Type="3"
		Name="SourceEncapsulationNominalThickness"				Type="3"
		Name="SourceEncapsulationNominalTransmission"			Type="3"
		Name="SourceIsotopeName"								Type="1"
		Name="SourceIsotopeHalfLife"							Type="1"
		Name="SourceStrengthUnits"								Type="1C"	Condition="SourceIsNotGammaEmitter"	StringEnumValues="SourceStrengthUnits" mbpo="true"
		Name="ReferenceAirKermaRate"							Type="1"
		Name="SourceStrength"									Type="1C"	Condition="SourceIsNotGammaEmitter"
		Name="SourceStrengthReferenceDate"						Type="1"
		Name="SourceStrengthReferenceTime"						Type="1"
	SequenceEnd
	Sequence="ApplicationSetupSequence"							Type="1"	VM="1-n"
		Name="ApplicationSetupType"								Type="1"	StringDefinedTerms="ApplicationSetupType"
		Name="ApplicationSetupNumber"							Type="1"
		Name="ApplicationSetupName"								Type="3"
		Name="ApplicationSetupManufacturer"						Type="3"
		Name="TemplateNumber"									Type="3"
		Name="TemplateType"										Type="3"
		Name="TemplateName"										Type="3"
		Sequence="ReferencedReferenceImageSequence"				Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Name="TotalReferenceAirKerma"							Type="1"
		Sequence="BrachyAccessoryDeviceSequence"				Type="3"	VM="1-n"
			Name="BrachyAccessoryDeviceNumber"					Type="2"
			Name="BrachyAccessoryDeviceID"						Type="2"
			Name="BrachyAccessoryDeviceType"					Type="1"	StringDefinedTerms="BrachyAccessoryDeviceType"
			Name="BrachyAccessoryDeviceName"					Type="3"
			Name="MaterialID"									Type="3"
			Name="BrachyAccessoryDeviceNominalThickness"		Type="3"
			Name="BrachyAccessoryDeviceNominalTransmission"		Type="3"
			Name="ReferencedROINumber"							Type="2"
		SequenceEnd
		Sequence="ChannelSequence"								Type="1"	VM="1-n"
			Name="ChannelNumber"								Type="1"
			Name="ChannelLength"								Type="2"
			Name="ChannelTotalTime"								Type="1"
			Name="SourceMovementType"							Type="1"	StringDefinedTerms="SourceMovementType"
			Name="NumberOfPulses"								Type="1C"	Condition="BrachyTreatmentTypePDR"
			Name="PulseRepetitionInterval"						Type="1C"	Condition="BrachyTreatmentTypePDR"
			Name="SourceApplicatorNumber"						Type="3"
			Name="SourceApplicatorID"							Type="2C"	Condition="SourceApplicatorNumberPresent"
			Name="SourceApplicatorType"							Type="1C"	Condition="SourceApplicatorNumberPresent"	StringDefinedTerms="SourceApplicatorType"
			Name="SourceApplicatorName"							Type="3"
			Name="SourceApplicatorLength"						Type="1C"	Condition="SourceApplicatorNumberPresent"
			Name="SourceApplicatorManufacturer"					Type="3"
			Name="MaterialID"									Type="3"
			Name="SourceApplicatorWallNominalThickness"			Type="3"
			Name="SourceApplicatorWallNominalTransmission"		Type="3"
			Name="SourceApplicatorStepSize"						Type="1C"	Condition="SourceMovementTypeStepwise"
			Name="ReferencedROINumber"							Type="2C"	Condition="SourceApplicatorNumberPresent"
			Name="TransferTubeNumber"							Type="2"
			Name="TransferTubeLength"							Type="2C"	Condition="TransferTubeNumberNotNull"
			Sequence="ChannelShieldSequence"					Type="3"	VM="1-n"
				Name="ChannelShieldNumber"						Type="1"
				Name="ChannelShieldID"							Type="2"
				Name="ChannelShieldName"						Type="3"
				Name="MaterialID"								Type="3"
				Name="ChannelShieldNominalThickness"			Type="3"
				Name="ChannelShieldNominalTransmission"			Type="3"
				Name="ReferencedROINumber"						Type="2"
			SequenceEnd
			Name="ReferencedSourceNumber"						Type="1"
			Name="NumberOfControlPoints"						Type="1"
			Name="FinalCumulativeTimeWeight"					Type="1C"	NoCondition=""
			Sequence="BrachyControlPointSequence"				Type="1"	VM="2-n"
				Name="ControlPointIndex"						Type="1"
				Name="CumulativeTimeWeight"						Type="2"
				Name="ControlPointRelativePosition"				Type="1"
				Name="ControlPoint3DPosition"					Type="3"
				Name="ControlPointOrientation"					Type="3"
				Sequence="BrachyReferencedDoseReferenceSequence"	Type="3"	VM="1-n"
					Name="ReferencedDoseReferenceNumber"		Type="1"
					Name="CumulativeDoseReferenceCoefficient"	Type="1"
				SequenceEnd
			SequenceEnd
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="Approval"
	Name="ApprovalStatus"										Type="1"	StringEnumValues="ApprovalStatus"
	Name="ReviewDate"											Type="2C"	Condition="ApprovalStatusApprovedOrRejected"
	Name="ReviewTime"											Type="2C"	Condition="ApprovalStatusApprovedOrRejected"
	Name="ReviewerName"											Type="2C"	Condition="ApprovalStatusApprovedOrRejected"
ModuleEnd

Module="RTGeneralTreatmentRecord"
	Name="InstanceNumber"										Type="1"
	Name="TreatmentDate"										Type="2"
	Name="TreatmentTime"										Type="2"
	Sequence="ReferencedRTPlanSequence"							Type="2"	VM="0-1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedTreatmentRecordSequence"				Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="RTTreatmentMachineRecord"
	Sequence="TreatmentMachineSequence"							Type="1"	VM="1"
		Name="TreatmentMachineName"								Type="2"
		Name="Manufacturer"										Type="2"
		Name="InstitutionName"									Type="2"
		Name="InstitutionAddress"								Type="3"
		Name="InstitutionalDepartmentName"						Type="3"
		Sequence="InstitutionalDepartmentTypeCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"									BaselineContextID="7030"
		SequenceEnd
		Name="ManufacturerModelName"							Type="2"
		Name="DeviceSerialNumber"								Type="2"
	SequenceEnd
ModuleEnd

Module="MeasuredDoseReferenceRecord"
	Sequence="MeasuredDoseReferenceSequence"					Type="1"	VM="1-n"
		Name="ReferencedDoseReferenceNumber"					Type="1C"	Condition="MeasuredDoseReferenceNumberNotPresent"
		Name="MeasuredDoseReferenceNumber"						Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
		Name="DoseUnits"										Type="1"	StringEnumValues="DoseUnits"
		Name="MeasuredDoseValue"								Type="2"
		Name="MeasuredDoseType"									Type="2"	StringDefinedTerms="MeasuredDoseType"
		Name="MeasuredDoseDescription"							Type="3"
	SequenceEnd
ModuleEnd

Module="CalculatedDoseReferenceRecord"
	Sequence="CalculatedDoseReferenceSequence"					Type="1"	VM="1-n"
		Name="ReferencedDoseReferenceNumber"					Type="1C"	Condition="CalculatedDoseReferenceNumberNotPresent"
		Name="CalculatedDoseReferenceNumber"					Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
		Name="CalculatedDoseReferenceDoseValue"					Type="2"
		Name="CalculatedDoseReferenceDescription"				Type="3"
	SequenceEnd
ModuleEnd

Module="RTBeamsSessionRecord"
	Name="ReferencedFractionGroupNumber"						Type="3"
	Name="NumberOfFractionsPlanned"								Type="2"
	Name="PrimaryDosimeterUnit"									Type="1"	StringEnumValues="PrimaryDosimeterUnit"
	Sequence="TreatmentSessionBeamSequence"						Type="1"	VM="1-n"
		Name="ReferencedBeamNumber"								Type="3"
		Name="BeamName"											Type="3"
		Name="BeamDescription"									Type="3"
		Name="BeamType"											Type="1"	StringEnumValues="BeamType"
		Name="RadiationType"									Type="1"	StringDefinedTerms="RadiationType"
		Sequence="PrimaryFluenceModeSequence"					Type="3"	VM="1"
			Name="FluenceMode"									Type="1"	StringEnumValues="FluenceMode"
			Name="FluenceModeID"								Type="1C"	Condition="FluenceModeIsNonStandard"
		SequenceEnd
		Name="HighDoseTechniqueType"							Type="1C"	StringDefinedTerms="HighDoseTechniqueType"	NoCondition="" #real-world
		Sequence="ReferencedVerificationImageSequence"			Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
			Name="StartMeterset"								Type="3"
			Name="EndMeterset"									Type="3"
		SequenceEnd
		Sequence="ReferencedMeasuredDoseReferenceSequence"		Type="3"	VM="1-n"
			Name="ReferencedDoseReferenceNumber"				Type="1C"	Condition="ReferencedMeasuredDoseReferenceNumberNotPresent"
			Name="ReferencedMeasuredDoseReferenceNumber"		Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
			Name="MeasuredDoseValue"							Type="1"
		SequenceEnd
		Sequence="ReferencedCalculatedDoseReferenceSequence"	Type="3"	VM="1-n"
			Name="ReferencedDoseReferenceNumber"				Type="1C"	Condition="ReferencedCalculatedDoseReferenceNumberNotPresent"
			Name="ReferencedCalculatedDoseReferenceNumber"		Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
			Name="CalculatedDoseReferenceDoseValue"				Type="1"
		SequenceEnd
		Name="SourceAxisDistance"								Type="3"
		Sequence="BeamLimitingDeviceLeafPairsSequence"			Type="1"	VM="1-n"
			Name="RTBeamLimitingDeviceType"						Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
			Name="NumberOfLeafJawPairs"							Type="1"
		SequenceEnd
		Name="ReferencedPatientSetupNumber"						Type="3"
		Name="NumberOfWedges"									Type="1"
		Sequence="RecordedWedgeSequence"						Type="1C"	VM="1-n"	Condition="NumberOfWedgesNotZero"
			Name="WedgeNumber"									Type="3"
			Name="WedgeType"									Type="2"	StringDefinedTerms="WedgeType"
			Name="WedgeID"										Type="3"
			Name="AccessoryCode"								Type="3"
			Name="WedgeAngle"									Type="3"
			Name="WedgeOrientation"								Type="3"
		SequenceEnd
		Name="NumberOfCompensators"								Type="2"
		Sequence="RecordedCompensatorSequence"					Type="3"	VM="1-n"
			Name="ReferencedCompensatorNumber"					Type="1"
			Name="CompensatorType"								Type="2"	StringDefinedTerms="CompensatorType"
			Name="CompensatorID"								Type="3"
			Name="AccessoryCode"								Type="3"
			Name="CompensatorTrayID"							Type="3"
			Name="TrayAccessoryCode"							Type="3"
		SequenceEnd
		Name="NumberOfBoli"										Type="2"
		Sequence="ReferencedBolusSequence"						Type="3"	VM="1-n"
			Name="ReferencedROINumber"							Type="1"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Name="NumberOfBlocks"									Type="2"	
		Sequence="RecordedBlockSequence"						Type="3"	VM="1-n"
			Name="BlockTrayID"									Type="3"
			Name="TrayAccessoryCode"							Type="3"
			Name="AccessoryCode"								Type="3"
			Name="ReferencedBlockNumber"						Type="3"
			Name="BlockName"									Type="2"
		SequenceEnd
		Sequence="ApplicatorSequence"							Type="3"	VM="1"
			Name="ApplicatorID"									Type="1"
			Name="AccessoryCode"								Type="3"
			Name="ApplicatorType"								Type="1"	StringDefinedTerms="ApplicatorType"
			Name="ApplicatorDescription"						Type="3"
			Sequence="GeneralAccessorySequence"					Type="3"	VM="1-n"
				Name="GeneralAccessoryNumber"					Type="1"
				Name="GeneralAccessoryID"						Type="1"
				Name="GeneralAccessoryDescription"				Type="3"
				Name="GeneralAccessoryType"						Type="3"	StringDefinedTerms="RTGeneralAccessoryType"
				Name="AccessoryCode"							Type="3"
				Name="SourceToGeneralAccessoryDistance"			Type="3"
			SequenceEnd
		SequenceEnd
		Name="CurrentFractionNumber"							Type="2"
		Name="TreatmentDeliveryType"							Type="2"	StringDefinedTerms="TreatmentDeliveryType"
		Name="TreatmentTerminationStatus"						Type="1"	StringEnumValues="TreatmentTerminationStatus"
		Name="TreatmentTerminationCode"							Type="3"
		Name="TreatmentVerificationStatus"						Type="2"	StringEnumValues="TreatmentVerificationStatus"
		Name="SpecifiedPrimaryMeterset"							Type="3"
		Name="SpecifiedSecondaryMeterset"						Type="3"
		Name="DeliveredPrimaryMeterset"							Type="3"
		Name="DeliveredSecondaryMeterset"						Type="3"
		Name="SpecifiedTreatmentTime"							Type="3"
		Name="DeliveredTreatmentTime"							Type="3"
		Name="NumberOfControlPoints"							Type="1"
		Sequence="ControlPointDeliverySequence"					Type="1"	VM="1-n"
			Name="ReferencedControlPointIndex"					Type="3"
			Name="TreatmentControlPointDate"					Type="1"
			Name="TreatmentControlPointTime"					Type="1"
			Name="SpecifiedMeterset"							Type="2"
			Name="DeliveredMeterset"							Type="1"
			Name="DoseRateSet"									Type="2"
			Name="DoseRateDelivered"							Type="2"
			Name="NominalBeamEnergy"							Type="3"
			Name="NominalBeamEnergyUnit"						Type="1C"	Condition="NominalBeamEnergyIsPresent"	StringDefinedTerms="NominalBeamEnergyUnit"
			Sequence="WedgePositionSequence"					Type="3"	VM="1-n"
				Name="ReferencedWedgeNumber"					Type="1"
				Name="WedgePosition"							Type="1"	StringEnumValues="WedgePosition"
			SequenceEnd
			Sequence="BeamLimitingDevicePositionSequence"		Type="1C"	VM="1-n"	NoCondition="" # too hard :(
				Name="RTBeamLimitingDeviceType"					Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
				Name="LeafJawPositions"							Type="1"
			SequenceEnd
			Name="GantryAngle"									Type="1C"	NoCondition="" # too hard :(
			Name="GantryRotationDirection"						Type="1C"	StringEnumValues="RotationDirectionWithNone"	NoCondition="" # too hard :(
			Name="GantryPitchAngle"								Type="3"
			Name="GantryPitchRotationDirection"					Type="3"	StringEnumValues="RotationDirectionWithNone"
			Name="BeamStopperPosition"							Type="3"	StringEnumValues="BeamStopperPosition"
			Name="BeamLimitingDeviceAngle"						Type="1C"	NoCondition="" # too hard :(
			Name="BeamLimitingDeviceRotationDirection"			Type="1C"	NoCondition="" # too hard :(
			Name="PatientSupportAngle"							Type="1C"	NoCondition="" # too hard :(
			Name="PatientSupportRotationDirection"				Type="1C"	StringEnumValues="RotationDirectionWithNone"	NoCondition="" # too hard :(
			Name="TableTopEccentricAxisDistance"				Type="3"
			Name="TableTopEccentricAngle"						Type="1C"	NoCondition="" # too hard :(
			Name="TableTopEccentricRotationDirection"			Type="1C"	StringEnumValues="RotationDirectionWithNone"	NoCondition="" # too hard :(
			Name="TableTopPitchAngle"							Type="1C"	NoCondition="" # too hard :(
			Name="TableTopPitchRotationDirection"				Type="1C""	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopRollAngle"							Type="1C"	NoCondition="" # too hard :(
			Name="TableTopRollRotationDirection"				Type="1C""	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopVerticalPosition"						Type="2C"	NoCondition="" # too hard :(
			Name="TableTopLongitudinalPosition"					Type="2C"	NoCondition="" # too hard :(
			Name="TableTopLateralPosition"						Type="2C"	NoCondition="" # too hard :(
			Sequence="CorrectedParameterSequence"				Type="3"	VM="1-n"
				Name="ParameterSequencePointer"					Type="1"
				Name="ParameterItemIndex"						Type="1"
				Name="ParameterPointer"							Type="1"
				Name="CorrectionValue"							Type="1"
			SequenceEnd
			Sequence="OverrideSequence"							Type="3"	VM="1-n"
				Name="OverrideParameterPointer"					Type="2"
				Name="ParameterSequencePointer"					Type="3"
				Name="ParameterItemIndex"						Type="3"
				Name="ParameterValueNumber"						Type="3"
				Name="OperatorsName"							Type="2"
				Sequence="OperatorIdentificationSequence"		Type="3"	VM="1"
					InvokeMacro="PersonIdentificationMacro"
				SequenceEnd
				Name="OverrideReason"							Type="3"
			SequenceEnd
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="RTBrachySessionRecord"
	Name="ReferencedFractionGroupNumber"						Type="3"
	Name="NumberOfFractionsPlanned"								Type="2"
	Name="BrachyTreatmentTechnique"								Type="1"	StringEnumValues="BrachyTreatmentTechnique"
	Name="BrachyTreatmentType"									Type="1"	StringDefinedTerms="BrachyTreatmentType"
	Sequence="RecordedSourceSequence"							Type="1"	VM="1-n"
		Name="SourceNumber"										Type="1"
		Name="SourceType"										Type="1"	StringDefinedTerms="SourceType"
		Name="SourceManufacturer"								Type="2"
		Name="SourceSerialNumber"								Type="2"
		Name="SourceIsotopeName"								Type="1"
		Name="SourceIsotopeHalfLife"							Type="1"
		Name="SourceStrengthUnits"								Type="1C"	Condition="SourceIsNotGammaEmitter"	StringEnumValues="SourceStrengthUnits" mbpo="true"
		Name="ReferenceAirKermaRate"							Type="1"
		Name="SourceStrength"									Type="1C"	Condition="SourceIsNotGammaEmitter"
		Name="SourceStrengthReferenceDate"						Type="1"
		Name="SourceStrengthReferenceTime"						Type="1"
	SequenceEnd
	Sequence="TreatmentSessionApplicationSetupSequence"			Type="1"	VM="1-n"
		Name="ApplicationSetupType"								Type="1"	StringDefinedTerms="ApplicationSetupType"
		Name="ReferencedBrachyApplicationSetupNumber"			Type="3"
		Name="ApplicationSetupName"								Type="3"
		Name="ApplicationSetupManufacturer"						Type="3"
		Name="TemplateNumber"									Type="3"
		Name="TemplateType"										Type="3"
		Name="TemplateName"										Type="3"
		Name="ApplicationSetupCheck"							Type="3"	StringEnumValues="ApplicationSetupCheck"
		Sequence="ReferencedVerificationImageSequence"			Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Name="TotalReferenceAirKerma"							Type="1"
		Sequence="ReferencedMeasuredDoseReferenceSequence"		Type="3"	VM="1-n"
			Name="ReferencedDoseReferenceNumber"				Type="1C"	Condition="ReferencedMeasuredDoseReferenceNumberNotPresent"
			Name="ReferencedMeasuredDoseReferenceNumber"		Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
			Name="MeasuredDoseValue"							Type="1"
		SequenceEnd
		Sequence="ReferencedCalculatedDoseReferenceSequence"	Type="3"	VM="1-n"
			Name="ReferencedDoseReferenceNumber"				Type="1C"	Condition="ReferencedCalculatedDoseReferenceNumberNotPresent"
			Name="ReferencedCalculatedDoseReferenceNumber"		Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
			Name="CalculatedDoseReferenceDoseValue"				Type="1"
		SequenceEnd
		Name="CurrentFractionNumber"							Type="2"
		Name="TreatmentDeliveryType"							Type="2"	StringDefinedTerms="TreatmentDeliveryTypeNormalOrContinuation"
		Name="TreatmentTerminationStatus"						Type="1"	StringEnumValues="TreatmentTerminationStatus"
		Name="TreatmentTerminationCode"							Type="3"
		Name="TreatmentVerificationStatus"						Type="2"	StringEnumValues="TreatmentVerificationStatus"
		Sequence="RecordedBrachyAccessoryDeviceSequence"		Type="3"	VM="1-n"
			Name="ReferencedBrachyAccessoryDeviceNumber"		Type="2"
			Name="BrachyAccessoryDeviceID"						Type="2"
			Name="BrachyAccessoryDeviceType"					Type="1"	StringDefinedTerms="BrachyAccessoryDeviceType"
			Name="BrachyAccessoryDeviceName"					Type="3"
		SequenceEnd
		Sequence="RecordedChannelSequence"						Type="1"	VM="1-n"
			Name="ChannelNumber"								Type="1"
			Name="ChannelLength"								Type="2"
			Name="SpecifiedChannelTotalTime"					Type="1"
			Name="DeliveredChannelTotalTime"					Type="1"
			Name="SourceMovementType"							Type="1"	StringDefinedTerms="SourceMovementType"
			Name="SpecifiedNumberOfPulses"						Type="1C"	Condition="BrachyTreatmentTypeIsPDR"
			Name="DeliveredNumberOfPulses"						Type="1C"	Condition="BrachyTreatmentTypeIsPDR"
			Name="SpecifiedPulseRepetitionInterval"				Type="1C"	Condition="BrachyTreatmentTypeIsPDR"
			Name="DeliveredPulseRepetitionInterval"				Type="1C"	Condition="BrachyTreatmentTypeIsPDR"
			Sequence="ReferencedMeasuredDoseReferenceSequence"	Type="3"	VM="1-n"
				Name="ReferencedDoseReferenceNumber"			Type="1C"	Condition="ReferencedMeasuredDoseReferenceNumberNotPresent"
				Name="ReferencedMeasuredDoseReferenceNumber"	Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
				Name="MeasuredDoseValue"						Type="1"
			SequenceEnd
			Sequence="ReferencedCalculatedDoseReferenceSequence"	Type="3"	VM="1-n"
				Name="ReferencedDoseReferenceNumber"			Type="1C"	Condition="ReferencedCalculatedDoseReferenceNumberNotPresent"
				Name="ReferencedCalculatedDoseReferenceNumber"	Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
				Name="CalculatedDoseReferenceDoseValue"			Type="1"
			SequenceEnd
			Sequence="RecordedSourceApplicatorSequence"			Type="3"	VM="1-n"
				Name="ReferencedSourceApplicatorNumber"			Type="2"
				Name="SourceApplicatorID"						Type="2"
				Name="SourceApplicatorType"						Type="1"	StringDefinedTerms="SourceApplicatorType"
				Name="SourceApplicatorName"						Type="3"
				Name="SourceApplicatorLength"					Type="1"
				Name="SourceApplicatorManufacturer"				Type="3"
				Name="SourceApplicatorStepSize"					Type="1C"	NoCondition="" # need StringValueAbove SourceMovementType Stepwise :(
			SequenceEnd
			Name="TransferTubeNumber"							Type="2"
			Name="TransferTubeLength"							Type="2C"	Condition="TransferTubeNumberIsNotEmpty"
			Sequence="RecordedChannelShieldSequence"			Type="3"	VM="1-n"
				Name="ReferencedChannelShieldNumber"			Type="2"
				Name="ChannelShieldID"							Type="2"
				Name="ChannelShieldName"						Type="3"
			SequenceEnd
			Name="ReferencedSourceNumber"						Type="1"
			Name="SafePositionExitDate"							Type="1C"	NoCondition="" # Need StringValueAbove BrachyTreatmentType Not Manual :(
			Name="SafePositionExitTime"							Type="1C"	NoCondition="" # Need StringValueAbove BrachyTreatmentType Not Manual :(
			Name="SafePositionReturnDate"						Type="1C"	NoCondition="" # Need StringValueAbove BrachyTreatmentType Not Manual :(
			Name="SafePositionReturnTime"						Type="1C"	NoCondition="" # Need StringValueAbove BrachyTreatmentType Not Manual :(
			Name="NumberOfControlPoints"						Type="1"
			Sequence="BrachyControlPointDeliveredSequence"		Type="1"	VM="2-n"
				Name="ReferencedControlPointIndex"				Type="3"
				Name="TreatmentControlPointDate"				Type="1"
				Name="TreatmentControlPointTime"				Type="1"
				Name="ControlPointRelativePosition"				Type="1"
				Sequence="OverrideSequence"						Type="3"	VM="1-n"
					Name="OverrideParameterPointer"				Type="2"
					Name="OperatorsName"						Type="2"
					Sequence="OperatorIdentificationSequence"	Type="3"	VM="1"
						InvokeMacro="PersonIdentificationMacro"
					SequenceEnd
					Name="OverrideReason"						Type="3"
				SequenceEnd
			SequenceEnd
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="RTTreatmentSummaryRecord"
	Name="CurrentTreatmentStatus"								Type="1"	StringEnumValues="CurrentTreatmentStatus"
	Name="TreatmentStatusComment"								Type="3"
	Name="FirstTreatmentDate"									Type="2"
	Name="MostRecentTreatmentDate"								Type="2"
	Sequence="FractionGroupSummarySequence"						Type="3"	VM="1-n"
		Name="ReferencedFractionGroupNumber"					Type="3"
		Name="FractionGroupType"								Type="2"	StringEnumValues="FractionGroupType"
		Name="NumberOfFractionsPlanned"							Type="2"
		Name="NumberOfFractionsDelivered"						Type="2"
		Sequence="FractionStatusSummarySequence"				Type="3"	VM="1-n"
			Name="ReferencedFractionNumber"						Type="1"
			Name="TreatmentDate"								Type="2"
			Name="TreatmentTime"								Type="2"
			Name="TreatmentTerminationStatus"					Type="2"	StringEnumValues="TreatmentTerminationStatus"
		SequenceEnd
	SequenceEnd
	Sequence="TreatmentSummaryMeasuredDoseReferenceSequence"	Type="3"	VM="1-n"
		Name="ReferencedDoseReferenceNumber"					Type="3"
		Name="DoseReferenceDescription"							Type="3"
		Name="CumulativeDoseToDoseReference"					Type="1"
	SequenceEnd
	Sequence="TreatmentSummaryCalculatedDoseReferenceSequence"	Type="3"	VM="1-n"
		Name="ReferencedDoseReferenceNumber"					Type="3"
		Name="DoseReferenceDescription"							Type="3"
		Name="CumulativeDoseToDoseReference"					Type="1"
	SequenceEnd
ModuleEnd

Module="RTIonToleranceTables"
	Sequence="IonToleranceTableSequence"						Type="3"	VM="1-n"
		Name="ToleranceTableNumber"								Type="1"
		Name="ToleranceTableLabel"								Type="3"
		Name="GantryAngleTolerance"								Type="3"
		Name="BeamLimitingDeviceAngleTolerance"					Type="3"
		Sequence="BeamLimitingDeviceToleranceSequence"			Type="3"	VM="1-n"
			Name="RTBeamLimitingDeviceType"						Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
			Name="BeamLimitingDevicePositionTolerance"			Type="1"
		SequenceEnd
		Name="PatientSupportAngleTolerance"						Type="3"
		Name="TableTopVerticalPositionTolerance"				Type="3"
		Name="TableTopLongitudinalPositionTolerance"			Type="3"
		Name="TableTopLateralPositionTolerance"					Type="3"
		Name="TableTopPitchAngleTolerance"						Type="3"
		Name="TableTopRollAngleTolerance"						Type="3"
		Name="SnoutPositionTolerance"							Type="3"
	SequenceEnd
ModuleEnd

Module="RTIonBeams"
	Sequence="IonBeamSequence"									Type="1"	VM="1-n"
		Name="BeamNumber"										Type="1"
		Name="BeamName"											Type="1"
		Name="BeamDescription"									Type="3"
		Name="BeamType"											Type="1"	StringEnumValues="BeamType"
		Name="RadiationType"									Type="1"	StringDefinedTerms="IonRadiationType"
		Name="RadiationMassNumber"								Type="1C"	Condition="RadiationTypeIsIon"
		Name="RadiationAtomicNumber"							Type="1C"	Condition="RadiationTypeIsIon"
		Name="RadiationChargeState"								Type="1C"	Condition="RadiationTypeIsIon"
		Name="ScanMode"											Type="1"	StringDefinedTerms="IonScanMode"
		Name="ModulatedScanModeType"							Type="1C"	Condition="ScanModeIsModulatedSpec"	StringDefinedTerms="ModulatedScanModeType"
		Name="TreatmentMachineName"								Type="2"
		Name="Manufacturer"										Type="3"
		Name="InstitutionName"									Type="3"
		Name="InstitutionAddress"								Type="3"
		Name="InstitutionalDepartmentName"						Type="3"
		Sequence="InstitutionalDepartmentTypeCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"									BaselineContextID="7030"
		SequenceEnd
		Name="ManufacturerModelName"							Type="3"
		Name="DeviceSerialNumber"								Type="3"
		Name="PrimaryDosimeterUnit"								Type="3"	StringEnumValues="IonPrimaryDosimeterUnit"
		Name="ReferencedToleranceTableNumber"					Type="3"
		Name="VirtualSourceAxisDistances"						Type="1"
		Sequence="IonBeamLimitingDeviceSequence"				Type="3"	VM="1-n"
			Name="RTBeamLimitingDeviceType"						Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
			Name="IsocenterToBeamLimitingDeviceDistance"		Type="2"
			Name="NumberOfLeafJawPairs"							Type="1"
			Name="LeafPositionBoundaries"						Type="1C"	Condition="RTBeamLimitingDeviceTypeMLCXOrMLCY" mbpo="true"
		SequenceEnd
		Name="ReferencedPatientSetupNumber"						Type="3"
		Sequence="ReferencedReferenceImageSequence"				Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
			Name="ReferenceImageNumber"							Type="1"
		SequenceEnd
		Name="TreatmentDeliveryType"							Type="1"	StringDefinedTerms="TreatmentDeliveryType"
		Sequence="ReferencedDoseSequence"						Type="3"	VM="1-n"
			# SOPInstanceReferenceMacro, but want to check SOPClassUID
			Name="ReferencedSOPClassUID"						Type="1"	StringEnumValues="RTDoseSOPClass"
			Name="ReferencedSOPInstanceUID"						Type="1"
		SequenceEnd
		Name="NumberOfWedges"									Type="1"
		Name="TotalWedgeTrayWaterEquivalentThickness"			Type="3"
		Sequence="IonWedgeSequence"								Type="1C"	VM="1-n"	Condition="NumberOfWedgesNotZero"
			Name="WedgeNumber"									Type="1"
			Name="WedgeType"									Type="2"	StringDefinedTerms="IonWedgeType"
			Name="WedgeID"										Type="3"
			Name="AccessoryCode"								Type="3"
			Name="WedgeAngle"									Type="2"
			Name="WedgeOrientation"								Type="2"
			Name="IsocenterToWedgeTrayDistance"					Type="1"
		SequenceEnd
		Name="NumberOfCompensators"								Type="1"
		Name="TotalCompensatorTrayWaterEquivalentThickness"		Type="3"
		Sequence="IonRangeCompensatorSequence"					Type="1C"	VM="1-n"	Condition="NumberOfCompensatorsNotZero"
			Name="CompensatorDescription"						Type="3"
			Name="CompensatorNumber"							Type="1"
			Name="MaterialID"									Type="2"
			Name="CompensatorID"								Type="3"
			Name="AccessoryCode"								Type="3"
			Name="IsocenterToCompensatorTrayDistance"			Type="1C"	Condition="CompensatorMountingPositionNotDoubleSided"
			Name="CompensatorDivergence"						Type="1"	StringEnumValues="CompensatorDivergence"
			Name="CompensatorMountingPosition"					Type="1"	StringEnumValues="CompensatorMountingPosition"
			Name="CompensatorRows"								Type="1"
			Name="CompensatorColumns"							Type="1"
			Name="CompensatorPixelSpacing"						Type="1"	NotZeroError=""
			Name="CompensatorPosition"							Type="1"
			Name="CompensatorColumnOffset"						Type="1C"	NoCondition=""	# if compensator pattern is hexagonal
			Name="CompensatorThicknessData"						Type="1"
			Name="IsocenterToCompensatorDistances"				Type="1C"	Condition="NeedIsocenterToCompensatorDistance"
			Name="CompensatorRelativeStoppingPowerRatio"		Type="3"
			Name="CompensatorMillingToolDiameter"				Type="3"
		SequenceEnd
		Name="NumberOfBoli"										Type="1"
		Sequence="ReferencedBolusSequence"						Type="1C"	VM="1-n"	Condition="NumberOfBoliNotZero"
			Name="ReferencedROINumber"							Type="1"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Name="NumberOfBlocks"									Type="1"
		Name="TotalBlockTrayWaterEquivalentThickness"			Type="3"
		Sequence="IonBlockSequence"								Type="1C"	VM="1-n"	Condition="NumberOfBlocksNotZero"
			Name="BlockTrayID"									Type="3"
			Name="AccessoryCode"								Type="3"
			Name="IsocenterToBlockTrayDistance"					Type="1"
			Name="BlockType"									Type="1"	StringEnumValues="BlockType"
			Name="BlockDivergence"								Type="1"	StringEnumValues="BlockDivergence"
			Name="BlockMountingPosition"						Type="1"	StringEnumValues="BlockMountingPosition"
			Name="BlockNumber"									Type="1"
			Name="BlockName"									Type="3"
			Name="MaterialID"									Type="2"
			Name="BlockThickness"								Type="1"
			Name="BlockNumberOfPoints"							Type="1"
			Name="BlockData"									Type="1"
		SequenceEnd
		Sequence="SnoutSequence"								Type="3"	VM="1"
			Name="SnoutID"										Type="1"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Sequence="ApplicatorSequence"							Type="3"	VM="1"
			Name="ApplicatorID"									Type="1"
			Name="AccessoryCode"								Type="3"
			Name="ApplicatorType"								Type="1"	StringDefinedTerms="IonApplicatorType"
			Name="ApplicatorDescription"						Type="3"
			Sequence="GeneralAccessorySequence"					Type="3"	VM="1-n"
				Name="GeneralAccessoryNumber"					Type="1"
				Name="GeneralAccessoryID"						Type="1"
				Name="GeneralAccessoryDescription"				Type="3"
				Name="GeneralAccessoryType"						Type="3"	StringDefinedTerms="RTGeneralAccessoryType"
				Name="AccessoryCode"							Type="3"
				Name="IsocenterToGeneralAccessoryDistance"		Type="3"
			SequenceEnd
		SequenceEnd
		Name="NumberOfRangeShifters"							Type="1"
		Sequence="RangeShifterSequence"							Type="1C"	VM="1-n"	Condition="NumberOfRangeShiftersNotZero"
			Name="RangeShifterNumber"							Type="1"
			Name="RangeShifterID"								Type="1"
			Name="AccessoryCode"								Type="3"
			Name="RangeShifterType"								Type="1"	StringDefinedTerms="RangeShifterType"
			Name="RangeShifterDescription"						Type="3"
		SequenceEnd
		Name="NumberOfLateralSpreadingDevices"					Type="1"
		Sequence="LateralSpreadingDeviceSequence"				Type="1C"	VM="1-n"	Condition="NumberOfLateralSpreadingDevicesNotZero"
			Name="LateralSpreadingDeviceNumber"					Type="1"
			Name="LateralSpreadingDeviceID"						Type="1"
			Name="AccessoryCode"								Type="3"
			Name="LateralSpreadingDeviceType"					Type="1"	StringDefinedTerms="LateralSpreadingDeviceType"
			Name="LateralSpreadingDeviceDescription"			Type="3"
		SequenceEnd
		Name="NumberOfRangeModulators"							Type="1"
		Sequence="RangeModulatorSequence"						Type="1C"	VM="1-n"	Condition="NumberOfRangeModulatorsNotZero"
			Name="RangeModulatorNumber"							Type="1"
			Name="RangeModulatorID"								Type="1"
			Name="AccessoryCode"								Type="3"
			Name="RangeModulatorType"							Type="1"	StringDefinedTerms="RangeModulatorType"
			Name="RangeModulatorDescription"					Type="3"
			Name="BeamCurrentModulationID"						Type="1C"	Condition="RangeModulatorTypeIsWhlModWeights"
		SequenceEnd
		InvokeMacro="PatientSupportIdentificationMacro"
		Name="FixationLightAzimuthalAngle"						Type="3"
		Name="FixationLightPolarAngle"							Type="3"
		Name="FinalCumulativeMetersetWeight"					Type="1C"	NoCondition=""
		Name="NumberOfControlPoints"							Type="1"
		Sequence="IonControlPointSequence"						Type="1"	VM="2-n"
			Name="ControlPointIndex"							Type="1"
			Name="CumulativeMetersetWeight"						Type="2"
			Sequence="ReferencedDoseReferenceSequence"			Type="3"	VM="1-n"
				Name="ReferencedDoseReferenceNumber"			Type="1"
				Name="CumulativeDoseReferenceCoefficient"		Type="2"
			SequenceEnd
			Name="NominalBeamEnergy"							Type="1C"	NoCondition=""
			Name="KVP"											Type="1C"	NoCondition=""
			Name="MetersetRate"									Type="3"
			Sequence="IonWedgePositionSequence"					Type="1C"	VM="1-n"	NoCondition=""
				Name="ReferencedWedgeNumber"					Type="1"
				Name="WedgePosition"							Type="1"	StringEnumValues="WedgePosition"
				Name="WedgeThinEdgePosition"					Type="1C"	NoCondition=""
			SequenceEnd
			Sequence="RangeShifterSettingsSequence"				Type="1C"	VM="1-n"	NoCondition=""
				Name="ReferencedRangeShifterNumber"				Type="1"
				Name="RangeShifterSetting"						Type="1"
				Name="IsocenterToRangeShifterDistance"			Type="3"
				Name="RangeShifterWaterEquivalentThickness"		Type="3"
			SequenceEnd
			Sequence="LateralSpreadingDeviceSettingsSequence"			Type="1C"	VM="1-n"	NoCondition=""
				Name="ReferencedLateralSpreadingDeviceNumber"			Type="1"
				Name="LateralSpreadingDeviceSetting"					Type="1"
				Name="IsocenterToLateralSpreadingDeviceDistance"		Type="3"
				Name="LateralSpreadingDeviceWaterEquivalentThickness"	Type="3"
			SequenceEnd
			Sequence="RangeModulatorSettingsSequence"						Type="1C"	VM="1-n"	NoCondition=""
				Name="ReferencedRangeModulatorNumber"						Type="1"
				Name="RangeModulatorGatingStartValue"						Type="1C"	NoCondition=""
				Name="RangeModulatorGatingStopValue"						Type="1C"	NoCondition=""
				Name="RangeModulatorGatingStartWaterEquivalentThickness"	Type="3"
				Name="RangeModulatorGatingStopWaterEquivalentThickness"		Type="3"
			SequenceEnd
			InvokeMacro="BeamLimitingDevicePositionMacro"
			Name="GantryAngle"									Type="1C"	NoCondition=""
			Name="GantryRotationDirection"						Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="GantryPitchAngle"								Type="3"
			Name="GantryPitchRotationDirection"					Type="3"	StringEnumValues="RotationDirectionWithNone"
			Name="BeamLimitingDeviceAngle"						Type="1C"	NoCondition=""
			Name="BeamLimitingDeviceRotationDirection"			Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="ScanSpotPositionMap"							Type="1C"	Condition="ScanModeAboveIsModulatedOrModulatedSpec"
			Name="ScanSpotMetersetWeights"						Type="1C"	Condition="ScanModeAboveIsModulatedOrModulatedSpec"
			Name="ScanningSpotSize"								Type="3"
			Name="NumberOfPaintings"							Type="1C"	Condition="ScanModeAboveIsModulatedOrModulatedSpec"
			Name="PatientSupportAngle"							Type="1C"	NoCondition=""
			Name="PatientSupportRotationDirection"				Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopPitchAngle"							Type="2C"	NoCondition=""
			Name="TableTopPitchRotationDirection"				Type="2C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopRollAngle"							Type="2C"	NoCondition=""
			Name="TableTopRollRotationDirection"				Type="2C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="HeadFixationAngle"							Type="3"
			Name="TableTopVerticalPosition"						Type="2C"	NoCondition=""
			Name="TableTopLongitudinalPosition"					Type="2C"	NoCondition=""
			Name="TableTopLateralPosition"						Type="2C"	NoCondition=""
			Name="SnoutPosition"								Type="2C"	NoCondition=""
			Name="IsocenterPosition"							Type="2C"	NoCondition=""
			Name="SurfaceEntryPoint"							Type="3"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="RTIonBeamsSessionRecord"
	Name="ReferencedFractionGroupNumber"						Type="3"
	Name="NumberOfFractionsPlanned"								Type="2"
	Name="PrimaryDosimeterUnit"									Type="1"	StringEnumValues="IonPrimaryDosimeterUnit"
	Sequence="TreatmentSessionIonBeamSequence"					Type="1"	VM="1-n"
		Name="ReferencedBeamNumber"								Type="1"
		Name="BeamName"											Type="1"
		Name="BeamDescription"									Type="3"
		Name="BeamType"											Type="1"	StringEnumValues="BeamType"
		Name="RadiationType"									Type="1"	StringDefinedTerms="IonRadiationType"
		Name="RadiationMassNumber"								Type="1C"	Condition="RadiationTypeIsIon"
		Name="RadiationAtomicNumber"							Type="1C"	Condition="RadiationTypeIsIon"
		Name="RadiationChargeState"								Type="1C"	Condition="RadiationTypeIsIon"
		Name="ScanMode"											Type="1"	StringDefinedTerms="IonScanMode"
		Name="ModulatedScanModeType"							Type="1C"	Condition="ScanModeIsModulatedSpec"	StringDefinedTerms="ModulatedScanModeType"
		Name="ReferencedToleranceTableNumber"					Type="3"
		Sequence="BeamLimitingDeviceLeafPairsSequence"			Type="3"	VM="1-n"
			Name="RTBeamLimitingDeviceType"						Type="1"	StringEnumValues="RTBeamLimitingDeviceType"
			Name="NumberOfLeafJawPairs"							Type="1"
		SequenceEnd
		Name="ReferencedPatientSetupNumber"						Type="3"
		Sequence="ReferencedVerificationImageSequence"			Type="3"	VM="1-n"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="ReferencedMeasuredDoseReferenceSequence"		Type="3"	VM="1-n"
			Name="ReferencedDoseReferenceNumber"				Type="1C"	Condition="ReferencedMeasuredDoseReferenceNumberNotPresent"
			Name="ReferencedMeasuredDoseReferenceNumber"		Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
			Name="MeasuredDoseValue"							Type="1"
		SequenceEnd
		Sequence="ReferencedCalculatedDoseReferenceSequence"	Type="3"	VM="1-n"
			Name="ReferencedDoseReferenceNumber"				Type="1C"	Condition="ReferencedCalculatedDoseReferenceNumberNotPresent"
			Name="ReferencedCalculatedDoseReferenceNumber"		Type="1C"	Condition="ReferencedDoseReferenceNumberNotPresent"
			Name="CalculatedDoseReferenceDoseValue"				Type="1"
		SequenceEnd
		Name="NumberOfWedges"									Type="1"
		Sequence="RecordedWedgeSequence"						Type="1C"	VM="1-n"	Condition="NumberOfWedgesNotZero"
			Name="WedgeNumber"									Type="1"
			Name="WedgeType"									Type="2"	StringDefinedTerms="IonWedgeType"
			Name="WedgeID"										Type="3"
			Name="AccessoryCode"								Type="3"
			Name="WedgeAngle"									Type="3"
			Name="WedgeOrientation"								Type="3"
		SequenceEnd
		Name="NumberOfCompensators"								Type="1"
		Sequence="RecordedCompensatorSequence"					Type="1C"	VM="1-n"	Condition="NumberOfCompensatorsNotZero"
			Name="ReferencedCompensatorNumber"					Type="1"
			Name="CompensatorType"								Type="2"	StringDefinedTerms="CompensatorType"
			Name="CompensatorID"								Type="3"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Name="NumberOfBoli"										Type="1"
		Sequence="ReferencedBolusSequence"						Type="1C"	VM="1-n"	Condition="NumberOfBoliNotZero"
			Name="ReferencedROINumber"							Type="1"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Name="NumberOfBlocks"									Type="1"
		Sequence="RecordedBlockSequence"						Type="1C"	VM="1-n"	Condition="NumberOfBlocksNotZero"
			Name="BlockTrayID"									Type="3"
			Name="AccessoryCode"								Type="3"
			Name="ReferencedBlockNumber"						Type="1"
			Name="BlockName"									Type="2"
		SequenceEnd
		Sequence="RecordedSnoutSequence"						Type="1C"	VM="1"	NoCondition=""
			Name="SnoutID"										Type="1"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Sequence="ApplicatorSequence"							Type="1C"	VM="1"	NoCondition=""
			Name="ApplicatorID"									Type="1"
			Name="AccessoryCode"								Type="3"
			Name="ApplicatorType"								Type="1"	StringDefinedTerms="IonApplicatorType"
			Name="ApplicatorDescription"						Type="3"
			Sequence="GeneralAccessorySequence"					Type="3"	VM="1-n"
				Name="GeneralAccessoryNumber"					Type="1"
				Name="GeneralAccessoryID"						Type="1"
				Name="GeneralAccessoryDescription"				Type="3"
				Name="GeneralAccessoryType"						Type="3"	StringDefinedTerms="RTGeneralAccessoryType"
				Name="AccessoryCode"							Type="3"
			SequenceEnd
		SequenceEnd
		Name="NumberOfRangeShifters"							Type="1"
		Sequence="RecordedRangeShifterSequence"					Type="1C"	VM="1-n"	Condition="NumberOfRangeShiftersNotZero"
			Name="ReferencedRangeShifterNumber"					Type="1"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Name="NumberOfLateralSpreadingDevices"					Type="1"
		Sequence="RecordedLateralSpreadingDeviceSequence"		Type="1C"	VM="1-n"	Condition="NumberOfLateralSpreadingDevicesNotZero"
			Name="ReferencedLateralSpreadingDeviceNumber"		Type="1"
			Name="LateralSpreadingDeviceID"						Type="1"
			Name="AccessoryCode"								Type="3"
		SequenceEnd
		Name="NumberOfRangeModulators"							Type="1"
		Sequence="RecordedRangeModulatorSequence"				Type="1C"	VM="1-n"	Condition="NumberOfRangeModulatorsNotZero"
			Name="ReferencedRangeModulatorNumber"				Type="1"
			Name="RangeModulatorID"								Type="1"
			Name="AccessoryCode"								Type="3"
			Name="RangeModulatorType"							Type="1"	StringDefinedTerms="RangeModulatorType"
			Name="BeamCurrentModulationID"						Type="1C"	Condition="RangeModulatorTypeIsWhlModWeights"
		SequenceEnd
		InvokeMacro="PatientSupportIdentificationMacro"
		Name="FixationLightAzimuthalAngle"						Type="3"
		Name="FixationLightPolarAngle"							Type="3"
		Name="CurrentFractionNumber"							Type="2"
		Name="TreatmentDeliveryType"							Type="2"	StringDefinedTerms="TreatmentDeliveryType"
		Name="TreatmentTerminationStatus"						Type="1"	StringEnumValues="TreatmentTerminationStatus"
		Name="TreatmentTerminationCode"							Type="3"
		Name="TreatmentVerificationStatus"						Type="2"	StringEnumValues="TreatmentVerificationStatus"
		Name="SpecifiedPrimaryMeterset"							Type="3"
		Name="SpecifiedSecondaryMeterset"						Type="3"
		Name="DeliveredPrimaryMeterset"							Type="3"
		Name="DeliveredSecondaryMeterset"						Type="3"
		Name="SpecifiedTreatmentTime"							Type="3"
		Name="DeliveredTreatmentTime"							Type="3"
		Name="NumberOfControlPoints"							Type="1"
		Sequence="IonControlPointDeliverySequence"				Type="1"	VM="1-n"
			Name="ReferencedControlPointIndex"					Type="1"
			Name="TreatmentControlPointDate"					Type="1"
			Name="TreatmentControlPointTime"					Type="1"
			Name="SpecifiedMeterset"							Type="2"
			Name="DeliveredMeterset"							Type="1"
			Name="MetersetRateSet"								Type="3"
			Name="MetersetRateDelivered"						Type="3"
			Name="NominalBeamEnergy"							Type="1C"	NoCondition=""
			Name="KVP"											Type="1C"	NoCondition=""
			Sequence="IonWedgePositionSequence"					Type="1C"	VM="1-n"	NoCondition=""
				Name="ReferencedWedgeNumber"					Type="1"
				Name="WedgePosition"							Type="1"	StringEnumValues="WedgePosition"
				Name="WedgeThinEdgePosition"					Type="1C"	NoCondition=""
			SequenceEnd
			InvokeMacro="BeamLimitingDevicePositionMacro"
			Sequence="RangeShifterSettingsSequence"				Type="1C"	VM="1-n"	NoCondition=""
				Name="ReferencedRangeShifterNumber"				Type="1"
				Name="RangeShifterSetting"						Type="1"
			SequenceEnd
			Sequence="LateralSpreadingDeviceSettingsSequence"			Type="1C"	VM="1-n"	NoCondition=""
				Name="ReferencedLateralSpreadingDeviceNumber"			Type="1"
				Name="LateralSpreadingDeviceSetting"					Type="1"
			SequenceEnd
			Sequence="RangeModulatorSettingsSequence"						Type="1C"	VM="1-n"	NoCondition=""
				Name="ReferencedRangeModulatorNumber"						Type="1"
				Name="RangeModulatorGatingStartValue"						Type="1C"	NoCondition=""
				Name="RangeModulatorGatingStopValue"						Type="1C"	NoCondition=""
			SequenceEnd
			Name="GantryAngle"									Type="1C"	NoCondition=""
			Name="GantryRotationDirection"						Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="GantryPitchAngle"								Type="3"
			Name="GantryPitchRotationDirection"					Type="3"	StringEnumValues="RotationDirectionWithNone"
			Name="BeamLimitingDeviceAngle"						Type="1C"	NoCondition=""
			Name="BeamLimitingDeviceRotationDirection"			Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="ScanSpotTuneID"								Type="1C"	Condition="ScanModeAboveIsModulatedOrModulatedSpec"
			Name="NumberOfScanSpotPositions"					Type="1C"	Condition="ScanModeAboveIsModulatedOrModulatedSpec"
			Name="ScanSpotPositionMap"							Type="1C"	Condition="ScanModeAboveIsModulatedOrModulatedSpec"
			Name="ScanSpotMetersetsDelivered"					Type="1C"	Condition="ScanModeAboveIsModulatedOrModulatedSpec"
			Name="ScanSpotTimeOffset"							Type="3"
			Name="ScanningSpotSize"								Type="3"
			Name="NumberOfPaintings"							Type="1C"	Condition="ScanModeAboveIsModulatedOrModulatedSpec"
			Name="PatientSupportAngle"							Type="1C"	NoCondition=""
			Name="PatientSupportRotationDirection"				Type="1C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopPitchAngle"							Type="2C"	NoCondition=""
			Name="TableTopPitchRotationDirection"				Type="2C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="TableTopRollAngle"							Type="2C"	NoCondition=""
			Name="TableTopRollRotationDirection"				Type="2C"	NoCondition=""	StringEnumValues="RotationDirectionWithNone"
			Name="HeadFixationAngle"							Type="3"
			Name="TableTopVerticalPosition"						Type="2C"	NoCondition=""
			Name="TableTopLongitudinalPosition"					Type="2C"	NoCondition=""
			Name="TableTopLateralPosition"						Type="2C"	NoCondition=""
			Name="SnoutPosition"								Type="2C"	NoCondition=""
			Sequence="CorrectedParameterSequence"				Type="3"	VM="1-n"
				Name="ParameterSequencePointer"					Type="1"
				Name="ParameterItemIndex"						Type="1"
				Name="ParameterPointer"							Type="1"
				Name="CorrectionValue"							Type="1"
			SequenceEnd
			Sequence="OverrideSequence"							Type="3"	VM="1-n"
				Name="ParameterSequencePointer"					Type="1"
				Name="OverrideParameterPointer"					Type="1"
				Name="ParameterItemIndex"						Type="1"
				Name="ParameterValueNumber"						Type="3"
				Name="OperatorsName"							Type="2"
				Sequence="OperatorIdentificationSequence"		Type="3"	VM="1"
					InvokeMacro="PersonIdentificationMacro"
				SequenceEnd
				Name="OverrideReason"							Type="3"
			SequenceEnd
		SequenceEnd
	SequenceEnd
ModuleEnd
Module="AcquisitionContext"
	Sequence="AcquisitionContextSequence"			Type="2"	VM="0-n"
		Name="ValueType"							Type="3"	StringDefinedTerms="AcquisitionContextValueTypes"
		Name="ObservationDateTime"					Type="3"
		Sequence="ConceptNameCodeSequence"			Type="1"	VM="1"	# should check for 1 and only 1 item present
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="ReferencedFrameNumber"				Type="1C"	NoCondition=""	NotZeroError=""
		Verify="ReferencedFrameNumber"							Condition="ReferencedFrameNumberOrReferencedFrameNumbersPresentButNMImageInstance"	ThenErrorMessage="May not be present for NM Image"
		Name="NumericValue"							Type="1C"	VM="1-n" Condition="AcquisitionContextItemIsNumeric"
		Name="FloatingPointValue"					Type="1C"	VM="1-n" NoCondition=""																# should check that VM is same as NumericValue :(
		Verify="FloatingPointValue"								Condition="FloatingPointValuePresentButAcquisitionContextItemIsNotNumeric"			ThenErrorMessage="May not be present when NumericValue is absent"
		Name="RationalNumeratorValue"				Type="1C"	VM="1-n" NoCondition=""																# should check that VM is same as NumericValue :(
		Verify="RationalNumeratorValue"							Condition="RationalNumeratorValuePresentButAcquisitionContextItemIsNotNumeric"		ThenErrorMessage="May not be present when NumericValue is absent"
		Name="RationalDenominatorValue"				Type="1C"	VM="1-n" Condition="RationalNumeratorValueIsPresent" NotZeroError=""				# should check that VM is same as NumericValue :(
		Verify="RationalDenominatorValue"						Condition="RationalDenominatorValuePresentButAcquisitionContextItemIsNotNumeric"	ThenErrorMessage="May not be present when NumericValue is absent"
		Sequence="MeasurementUnitsCodeSequence"		Type="1C"	VM="1"	Condition="NeedMeasurementUnitsCodeSequence"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Verify="MeasurementUnitsCodeSequence"					Condition="MeasurementUnitsCodeSequencePresentAndNumericValueAbsent"	ThenErrorMessage="May not be present when NumericValue is absent"
		Name="Date"									Type="1C"	Condition="AcquisitionContextItemIsDate"
		Name="Time"									Type="1C"	Condition="AcquisitionContextItemIsTime"
		Name="PersonName"							Type="1C"	Condition="AcquisitionContextItemIsPersonName"
		Name="TextValue"							Type="1C"	Condition="AcquisitionContextItemIsTextValue"
		Sequence="ConceptCodeSequence"				Type="1C"	VM="1"	Condition="AcquisitionContextItemIsConceptCodeSequence"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="AcquisitionContextDescription"			Type="3"
ModuleEnd

DefineMacro="SpecimenMacro"
	Name="ContainerIdentifier"								Type="1"
	Sequence="IssuerOfTheContainerIdentifierSequence"		Type="2"	VM="0-1"
		InvokeMacro="HL7v2HierarchicDesignatorMacro"
	SequenceEnd
	Sequence="AlternateContainerIdentifierSequence"			Type="3"	VM="1-n"
		Name="ContainerIdentifier"							Type="1"
		Sequence="IssuerOfTheContainerIdentifierSequence"	Type="2"	VM="0-1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
	SequenceEnd
	Sequence="ContainerTypeCodeSequence"					Type="2"	VM="0-1"
		InvokeMacro="CodeSequenceMacro"						BaselineContextID="8101"
	SequenceEnd
	Name="ContainerDescription"								Type="3"
	Sequence="ContainerComponentSequence"					Type="3"	VM="1-n"
		Sequence="ContainerComponentTypeCodeSequence"		Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"					BaselineContextID="8102"
		SequenceEnd
		Name="Manufacturer"									Type="3"
		Name="ManufacturerModelName"						Type="3"
		Name="ContainerComponentID"							Type="3"
		Name="ContainerComponentLength"						Type="3"
		Name="ContainerComponentWidth"						Type="3"
		Name="ContainerComponentDiameter"					Type="3"
		Name="ContainerComponentThickness"					Type="3"
		Name="ContainerComponentMaterial"					Type="3"	StringDefinedTerms="ContainerComponentMaterial"
		Name="ContainerComponentDescription"				Type="3"
	SequenceEnd
	Sequence="SpecimenDescriptionSequence"					Type="1"	VM="1-n"
		Name="SpecimenIdentifier"							Type="1"
		Sequence="IssuerOfTheSpecimenIdentifierSequence"	Type="2"	VM="0-1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="SpecimenUID"									Type="1"
		Sequence="SpecimenTypeCodeSequence"					Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"					BaselineContextID="8103"
		SequenceEnd
		Name="SpecimenShortDescription"						Type="3"
		Name="SpecimenDetailedDescription"					Type="3"
		Sequence="SpecimenPreparationSequence"				Type="2"	VM="0-n"
			Sequence="SpecimenPreparationStepContentItemSequence"	Type="1"	VM="1-n"
				InvokeMacro="ContentItemMacro"
			SequenceEnd
		SequenceEnd
		InvokeMacro="PrimaryAnatomicStructureMacro" 
		Sequence="SpecimenLocalizationContentItemSequence"	Type="1C"	VM="1-n"	NoCondition=""	mbpo="true" # real-world multiple specimens
			InvokeMacro="ContentItemMacro"
		SequenceEnd
	SequenceEnd
MacroEnd

Module="Specimen"
	InvokeMacro="SpecimenMacro"
ModuleEnd
Module="XRayAcquisitionDose"
	Name="KVP"									Type="3"	NotZeroWarning=""
	
	Name="XRayTubeCurrent"						Type="3"	NotZeroWarning=""
	Name="XRayTubeCurrentInuA"					Type="3"	NotZeroWarning=""
	Verify="XRayTubeCurrentInmA"							Condition="XRayTubeCurrentInmAIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <XRayAcquisitionDose> - use XRayTubeCurrent and/or XRayTubeCurrentInuA instead of"
	
	Name="ExposureTime"							Type="3"	NotZeroWarning=""
	Name="ExposureTimeInuS"						Type="3"	NotZeroWarning=""
	Verify="ExposureTimeInms"								Condition="ExposureTimeInmsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <XRayAcquisitionDose> - use ExposureTime and/or ExposureTimeInuS instead of"
	
	Name="Exposure"								Type="3"	NotZeroWarning=""
	Name="ExposureInuAs"						Type="3"	NotZeroWarning=""
	Verify="ExposureInmAs"									Condition="ExposureInmAsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <XRayAcquisitionDose> - use Exposure and/or ExposureInuAs instead of"
	
	Name="DistanceSourceToDetector"				Type="3"	NotZeroWarning=""
	Name="DistanceSourceToPatient"				Type="3"	NotZeroWarning=""
	Name="ImageAndFluoroscopyAreaDoseProduct"	Type="3"	NotZeroWarning=""
	Name="BodyPartThickness"					Type="3"	NotZeroWarning=""
	Name="RelativeXRayExposure"					Type="3"	NotZeroWarning=""
	Name="EntranceDose"							Type="3"	NotZeroWarning=""
	Name="EntranceDoseInmGy"					Type="3"	NotZeroWarning=""
	Name="EntranceDoseDerivation"				Type="3"	StringEnumValues="EntranceDoseDerivation"
	Name="ExposedArea"							Type="3"
	Name="DistanceSourceToEntrance"				Type="3"	NotZeroWarning=""
	Name="CommentsOnRadiationDose"				Type="3"
	Name="XRayOutput"							Type="3"	NotZeroWarning=""
	Name="HalfValueLayer"						Type="3"	NotZeroWarning=""
	Name="OrganDose"							Type="3"	NotZeroWarning=""
	Name="OrganExposed"							Type="3"	StringDefinedTerms="OrganExposed"
	Name="AnodeTargetMaterial"					Type="3"	StringDefinedTerms="AnodeTargetMaterial"
	InvokeMacro="XRayFiltrationMacro"
	Name="RectificationType"					Type="3"	StringDefinedTerms="RectificationType"
	InvokeMacro="ExposureIndexMacro"
ModuleEnd

Module="XRayGeneration"
	Name="KVP"									Type="3"	NotZeroWarning=""
	
	Name="XRayTubeCurrent"						Type="3"	NotZeroWarning=""
	Name="XRayTubeCurrentInuA"					Type="3"	NotZeroWarning=""
	Verify="XRayTubeCurrentInmA"							Condition="XRayTubeCurrentInmAIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <XRayGeneration> - use XRayTubeCurrent and/or XRayTubeCurrentInuA instead of"
	
	Name="ExposureTime"							Type="3"	NotZeroWarning=""
	Name="ExposureTimeInuS"						Type="3"	NotZeroWarning=""
	Verify="ExposureTimeInms"								Condition="ExposureTimeInmsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <XRayGeneration> - use ExposureTime and/or ExposureTimeInuS instead of"
	
	Name="Exposure"								Type="3"	NotZeroWarning=""
	Name="ExposureInuAs"						Type="3"	NotZeroWarning=""
	Verify="ExposureInmAs"									Condition="ExposureInmAsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <XRayGeneration> - use Exposure and/or ExposureInuAs instead of"
	
	Name="ExposureControlMode"					Type="3"	StringDefinedTerms="ExposureControlMode"
	Name="ExposureControlModeDescription"		Type="3"
	Name="ExposureStatus"						Type="3"	StringDefinedTerms="ExposureStatus"
	Name="PhototimerSetting"					Type="3"
	Name="FocalSpots"							Type="3"
	Name="AnodeTargetMaterial"					Type="3"	StringDefinedTerms="AnodeTargetMaterial"
	Name="RectificationType"					Type="3"	StringDefinedTerms="RectificationType"
	Name="GeneratorID"							Type="3"
ModuleEnd

DefineMacro="XRayFiltrationMacro"
	Name="FilterType"							Type="3"	StringDefinedTerms="DXFilterType"
	Name="FilterMaterial"						Type="3"	StringDefinedTerms="DXFilterMaterial"
	Name="FilterThicknessMaximum"				Type="3"	NotZeroWarning=""
	Name="FilterThicknessMinimum"				Type="3"	NotZeroWarning=""
	Name="FilterBeamPathLengthMinimum"			Type="3"	NotZeroWarning=""
	Name="FilterBeamPathLengthMaximum"			Type="3"	NotZeroWarning=""
MacroEnd

Module="XRayFiltration"
	InvokeMacro="XRayFiltrationMacro"
ModuleEnd

DefineMacro="XRayGridDescriptionMacro" InformationEntity="Image"
	Name="GridAbsorbingMaterial"				Type="3"
	Name="GridSpacingMaterial"					Type="3"
	Name="GridThickness"						Type="3"	NotZeroWarning=""
	Name="GridPitch"							Type="3"	NotZeroWarning=""
	Name="GridAspectRatio"						Type="3"	NotZeroWarning=""
	Name="GridPeriod"							Type="3"	NotZeroWarning=""
	Name="GridFocalDistance"					Type="3"	NotZeroWarning=""
	Name="GridID"								Type="3"
MacroEnd

Module="XRayGrid"
	Name="Grid"									Type="3"	StringDefinedTerms="XRayGrid"
	InvokeMacro="XRayGridDescriptionMacro"
ModuleEnd

Module="DXSeries"
	Name="Modality"										Type="1"	StringEnumValues="DXModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Name="PresentationIntentType"						Type="1"	StringEnumValues="PresentationIntentType"
	Verify="PresentationIntentType"									Condition="IsForProcessingSOPClass"	StringEnumValues="ForProcessing"
	Verify="PresentationIntentType"									Condition="IsForPresentationSOPClass"	StringEnumValues="ForPresentation"
ModuleEnd

Module="DXAnatomyImaged"
	Name="ImageLaterality"								Type="1"	StringEnumValues="ImageLaterality"
	InvokeMacro="GeneralAnatomyRequiredMacro"
ModuleEnd

Module="DXImage"
	Name="ImageType"									Type="1"	ValueSelector="0"	StringEnumValues="ImageType1"
	Verify="ImageType"												ValueSelector="1"	StringEnumValues="ImageType2"
	Verify="ImageType"												ValueSelector="2"	StringEnumValues="DXImageType3"
	Name="SamplesPerPixel"								Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"					Type="1"	StringEnumValues="PhotometricInterpretationMonochrome"
	Name="BitsAllocated"								Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"									Type="1"	BinaryEnumValues="BitsAre6To16"
	Name="HighBit"										Type="1"	BinaryEnumValues="BitsAre5To15"
	Name="PixelRepresentation"							Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="PixelIntensityRelationship"					Type="1"	StringEnumValues="DXPixelIntensityRelationship"
	Name="PixelIntensityRelationshipSign"				Type="1"	BinaryEnumValues="PixelIntensityRelationshipSign"
	Name="RescaleIntercept"								Type="1"	BinaryEnumValues="Zero"
	Name="RescaleSlope"									Type="1"	BinaryEnumValues="One"
	Name="RescaleType"									Type="1"	StringEnumValues="ModalityLUTTypeUnspecified"
	Name="PresentationLUTShape"							Type="1"	StringEnumValues="DXPresentationLUTShape"
	Name="LossyImageCompression"						Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"					Type="1C"	NoCondition=""	NotZeroError=""
	Name="DerivationDescription"						Type="3"
	Name="AcquisitionDeviceProcessingDescription"		Type="3"
	Name="AcquisitionDeviceProcessingCode"				Type="3"
	Name="PatientOrientation"							Type="1C"	Condition="DXPatientOrientationRequired" mbpo="true"
	Name="CalibrationImage"								Type="3"	StringEnumValues="YesNoFull"
	Name="BurnedInAnnotation"							Type="1"	StringEnumValues="YesNoFull"
	Name="RecognizableVisualFeatures"					Type="3"	StringEnumValues="YesNoFull"
	Sequence="VOILUTSequence"							Type="1C"	VM="1-n"	Condition="ForPresentationAndWindowCenterNotPresent" mbpo="true"
		Name="LUTDescriptor"							Type="1"
		Verify="LUTDescriptor"										ValueSelector="2"	BinaryEnumValues="BitsAre10To16"
		Name="LUTExplanation"							Type="3"
		Name="LUTData"									Type="1"
	SequenceEnd
	Verify="VOILUTSequence"											Condition="VOILUTSequencePresentAndPresentationIntentTypeIsNotForPresentation" ThenErrorMessage="May only be present in For Presentation images"
	Name="WindowCenter"									Type="1C"	Condition="ForPresentationAndVOILUTSequenceNotPresent" mbpo="true"
	Verify="WindowCenter"											Condition="WindowCenterPresentAndPresentationIntentTypeIsNotForPresentation" ThenErrorMessage="May only be present in For Presentation images"
	Name="WindowWidth"									Type="1C"	Condition="WindowCenterPresent"	NotZeroError=""
	Verify="WindowWidth"											Condition="WindowWidthIsNegative"	ThenErrorMessage="Not permitted to be negative" ShowValueWithMessage="true"
	Name="WindowCenterWidthExplanation"					Type="3"
ModuleEnd

DefineMacro="DigitalXRayDetectorMacro" InformationEntity="Image"
	Name="DetectorType"									Type="2"	StringDefinedTerms="DetectorType"
	Name="DetectorConfiguration"						Type="3"	StringDefinedTerms="DetectorConfiguration"
	Name="DetectorDescription"							Type="3"
	Name="DetectorMode"									Type="3"
	Name="DetectorID"									Type="3"
	Name="DateOfLastDetectorCalibration"				Type="3"
	Name="TimeOfLastDetectorCalibration"				Type="3"
	Name="ExposuresOnDetectorSinceLastCalibration"		Type="3"
	Name="ExposuresOnDetectorSinceManufactured"			Type="3"
	Name="DetectorTimeSinceLastExposure"				Type="3"
	Name="DetectorBinning"								Type="3"
	Name="DetectorManufacturerName"						Type="3"
	Name="DetectorManufacturerModelName"				Type="3"
	Name="DetectorConditionsNominalFlag"				Type="3"	StringEnumValues="YesNoFull"
	Name="DetectorTemperature"							Type="3"
	Name="Sensitivity"									Type="3"	NotZeroWarning=""
	Name="DetectorElementPhysicalSize"					Type="3"	NotZeroError=""
	Name="DetectorElementSpacing"						Type="3"	NotZeroError=""
	Name="DetectorActiveShape"							Type="3"	StringEnumValues="DXShape"
	Name="DetectorActiveDimensions"						Type="3"
	Name="DetectorActiveOrigin"							Type="3"
	InvokeMacro="ExposureIndexMacro"
MacroEnd

Module="DXDetector"
	InvokeMacro="DigitalXRayDetectorMacro"
	Name="DetectorActiveTime"							Type="3"
	Name="DetectorActivationOffsetFromExposure"			Type="3"
	Name="FieldOfViewShape"								Type="3"	StringEnumValues="DXShape"
	Name="FieldOfViewDimensions"						Type="3"	NotZeroError=""
	Name="FieldOfViewOrigin"							Type="1C"	Condition="FieldOfViewRotationOrFieldOfViewHorizontalFlipPresent"
	Name="FieldOfViewRotation"							Type="1C"	Condition="FieldOfViewHorizontalFlipPresent"	StringEnumValues="DXFieldOfViewRotation"
	Name="FieldOfViewHorizontalFlip"					Type="1C"	Condition="FieldOfViewRotationPresent"		StringEnumValues="YesNoFull"
	Name="ImagerPixelSpacing"							Type="1"	NotZeroError=""
	InvokeMacro="BasicPixelSpacingCalibrationMacro"
	Name="CassetteID"									Type="3"
	Name="PlateID"										Type="3"
ModuleEnd

Module="DXPositioning"
	Sequence="ProjectionEponymousNameCodeSequence"		Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4012"
	SequenceEnd
	Name="PatientPosition"								Type="3"	StringDefinedTerms="PatientPosition"
	Name="ViewPosition"									Type="3"
	Verify="ViewPosition"											Condition="IsHuman"		StringDefinedTerms="ViewPositionHuman"
	Verify="ViewPosition"											Condition="IsAnimal"	StringDefinedTerms="ViewPositionAnimal"
	Sequence="ViewCodeSequence"							Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4010"
		Sequence="ViewModifierCodeSequence"				Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="4011"
		SequenceEnd
	SequenceEnd
	Verify="ViewCodeSequence"										Condition="ViewCodeSequenceAbsentOrEmptyButViewPositionHasValue"	ThenWarningMessage="ViewCodeSequence is empty or absent, but view is known since ViewPosition has a value"
	Sequence="ViewModifierCodeSequence"					Type="1C"	VM="1-n"	Condition="Never"
	SequenceEnd
	Sequence="PatientOrientationCodeSequence"			Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="19"
		Sequence="PatientOrientationModifierCodeSequence"	Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="20"
		SequenceEnd
	SequenceEnd
	Sequence="PatientOrientationModifierCodeSequence"	Type="1C"	VM="1"	Condition="Never"
	SequenceEnd
	Sequence="PatientGantryRelationshipCodeSequence"	Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="21"
	SequenceEnd
	Name="DistanceSourceToPatient"						Type="3"	NotZeroWarning=""
	Name="DistanceSourceToDetector"						Type="3"	NotZeroWarning=""
	Name="EstimatedRadiographicMagnificationFactor"		Type="3"
	Name="PositionerType"								Type="2"	StringDefinedTerms="DXPositionerType"
	Name="PositionerPrimaryAngle"						Type="3"
	Name="PositionerSecondaryAngle"						Type="3"
	Name="DetectorPrimaryAngle"							Type="3"
	Name="DetectorSecondaryAngle"						Type="3"
	Name="ColumnAngulation"								Type="3"
	Name="TableType"									Type="3"	StringDefinedTerms="DXTableType"
	Name="TableAngle"									Type="3"
	Name="BodyPartThickness"							Type="3"	NotZeroWarning=""
	Name="CompressionForce"								Type="3"
	Name="PaddleDescription"							Type="3"
ModuleEnd

Module="MammographySeries"
	Name="Modality"										Type="1"	StringEnumValues="MammographyModality"
	Sequence="RequestAttributesSequence"				Type="3"	VM="1-n"
		InvokeMacro="RequestAttributesMacro"
	SequenceEnd
ModuleEnd

Module="MammographyImage"
	Name="ImageType"									Type="1"	ValueSelector="2"	StringEnumValues="MammoImageType3"
	Verify="ImageType"												ValueSelector="3"	StringDefinedTerms="MammoImageType4"
	Verify="ImageType"												ValueSelector="4"	StringDefinedTerms="MammoImageType5"
	Name="PositionerType"								Type="1"	StringEnumValues="MammographyPositionerType"
	Name="DistanceSourceToPatient"						Type="3"	NotZeroWarning=""
	Name="DistanceSourceToDetector"						Type="3"	NotZeroWarning=""
	Name="PositionerPrimaryAngle"						Type="3"
	Name="PositionerPrimaryAngleDirection"				Type="3"	StringEnumValues="PositionerPrimaryAngleDirection"
	Name="PositionerSecondaryAngle"						Type="3"
	Name="ImageLaterality"								Type="1"	StringEnumValues="MammographyImageLaterality"
	Name="OrganExposed"									Type="1"	StringDefinedTerms="MammographyOrganExposed"
	Name="BreastImplantPresent"							Type="3"	StringEnumValues="YesNoFull"
	Name="PartialView"									Type="3"	StringEnumValues="YesNoFull"
	Name="PartialViewDescription"						Type="3"
	Sequence="PartialViewCodeSequence"					Type="3"	VM="1-2"
		InvokeMacro="CodeSequenceMacro"								DefinedContextID="4005"
	SequenceEnd
	InvokeMacro="GeneralAnatomyMandatoryMacro"
	Sequence="ViewCodeSequence"							Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"								EnmeratedContextID="4014"
		Sequence="ViewModifierCodeSequence"				Type="2"	VM="0-n"
			InvokeMacro="CodeSequenceMacro"							EnmeratedContextID="4015"
		SequenceEnd
	SequenceEnd
	Sequence="BiopsyTargetSequence"						Type="3"	VM="1-n"
		Name="TargetUID"								Type="1"
		Name="LocalizingCursorPosition"					Type="1"
		Name="CalculatedTargetPosition"					Type="1"
		Name="DisplayedZValue"							Type="1"
		Name="TargetLabel"								Type="3"
	SequenceEnd
ModuleEnd

Module="IntraoralSeries"
	Name="Modality"										Type="1"	StringEnumValues="IntraoralModality"
ModuleEnd

Module="IntraoralImage"
	Name="PositionerType"								Type="1"	StringEnumValues="IntraoralPositionerType"
	Name="ImageLaterality"								Type="1"	StringEnumValues="IntraoralImageLaterality"
	Sequence="AnatomicRegionSequence"					Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"								DefinedContextID="4016"
		Sequence="AnatomicRegionModifierSequence"		Type="1C"	VM="1"	Condition="NoPrimaryAnatomicStructureSequence"
			InvokeMacro="CodeSequenceMacro"							DefinedContextID="4017"
		SequenceEnd
	SequenceEnd
	Sequence="PrimaryAnatomicStructureSequence"			Type="1C"	VM="1-n"	Condition="NoAnatomicRegionModifierSequence"
		InvokeMacro="CodeSequenceMacro"								DefinedContextID="4018 or 4019"
	SequenceEnd
ModuleEnd

Module="ImageHistogram"
	Sequence="HistogramSequence"						Type="1"	VM="1-n"
		Name="HistogramNumberOfBins"					Type="1"
		Name="HistogramFirstBinValue"					Type="1"
		Name="HistogramLastBinValue"					Type="1"
		Name="HistogramBinWidth"						Type="1"
		Name="HistogramExplanation"						Type="3"
		Name="HistogramData"							Type="1"
	SequenceEnd
ModuleEnd

Module="IHEDBTProfile"
	Name="PatientName"						Type="1"
	Name="PatientID"						Type="1"
	Name="PatientBirthDate"					Type="1"
	Name="PatientAge"						Type="1"
	Name="OperatorsName"					Type="1"
	Name="Manufacturer"						Type="1"
	Name="InstitutionName"					Type="1"
	Name="InstitutionAddress"				Type="1"
	Name="ManufacturerModelName"			Type="1"
	Name="DeviceSerialNumber"				Type="1"
	Name="StationName"						Type="1"
	Sequence="ContributingSourcesSequence"	Type="1"	VM="1-n"
		Name="AcquisitionDateTime"			Type="1"
	SequenceEnd
	Sequence="XRay3DAcquisitionSequence"	Type="1"	VM="1-n"
		Name="OrganDose"					Type="1"
		Name="EntranceDoseInmGy"			Type="1"
	SequenceEnd
	Verify="ImageType"								Condition="ImageTypeValuesNotDBTThinThickGenerated2D"	ThenErrorMessage="Values not those required for thin or thick slices or generated 2D image by IHE DBT Rad TF Vol 2 Table 4.8.4.1.2.7-1"
ModuleEnd

Module="IHEMammoProfile"
	Name="PatientName"						Type="1"
	Name="PatientID"						Type="1"
	Name="PatientBirthDate"					Type="1"
	Name="PatientAge"						Type="1"
	Name="AcquisitionDate"					Type="1"
	Name="AcquisitionTime"					Type="1"
	Name="OperatorsName"					Type="1"
	Name="Manufacturer"						Type="1"
	Name="InstitutionName"					Type="1"
	Name="InstitutionAddress"				Type="1"
	Name="ManufacturerModelName"			Type="1"
	Name="DeviceSerialNumber"				Type="1"
	Name="DetectorID"						Type="1"
	Name="SoftwareVersions"					Type="1"
	Name="StationName"						Type="1"
	Name="GantryID"							Type="1C"	Condition="DetectorTypeIsStorage" mbpo="true"
	Name="KVP"								Type="1"	NotZeroWarning=""
	Name="Exposure"							Type="1"	NotZeroWarning=""
	Name="ExposureTime"						Type="1"	NotZeroWarning=""
	Name="FilterMaterial"					Type="1"
	Name="AnodeTargetMaterial"				Type="1"
	Name="CompressionForce"					Type="1"
	Name="BodyPartThickness"				Type="1"	NotZeroWarning=""
	Name="PositionerPrimaryAngle"			Type="1"
	Name="RelativeXRayExposure"				Type="1"	NotZeroWarning=""
	Name="EntranceDoseInmGy"				Type="1"	NotZeroWarning=""
	Name="OrganDose"						Type="1"	NotZeroWarning=""
	Name="BurnedInAnnotation"				Type="1"	StringEnumValues="NoFull"
	Name="BreastImplantPresent"				Type="1"
	Name="PixelPaddingValue"				Type="1"	# really only required if skin edge detected, but cannot check the real world intent
	Name="EstimatedRadiographicMagnificationFactor"	Type="1"
	Name="DateOfLastDetectorCalibration"	Type="1C"	Condition="DetectorTypeIsNotStorage" mbpo="true"
	Verify="PixelSpacing"								Condition="PixelSpacingIsPresent" ThenWarningMessage="Attribute present but not used in IHE Mammo Profile"
ModuleEnd

Module="IHEMammoProfileWithoutPartialViewOption"
	Verify="PartialView"								Condition="PartialViewNotPresent"	ThenWarningMessage="IHE Mammo Profile Partial View Option not supported"
ModuleEnd

Module="IHEMammoProfileWithPartialViewOption"
	Name="PartialView"						Type="1"	# really only required for partial view named option
	Sequence="PartialViewCodeSequence"		Type="1C"	VM="1-2"	Condition="PartialViewIsYes"
	SequenceEnd
ModuleEnd

Module="IHEMammoProfileForPresentationOnly"
	Sequence="SourceImageSequence"			Type="1"	VM="1"
		Name="SpatialLocationsPreserved"	Type="1"
	SequenceEnd
	Sequence="VOILUTSequence"				Type="3"	VM="1-n"
		Name="LUTExplanation"				Type="1"	# really only required if number of items > 1, but cannot check this
	SequenceEnd
	Name="WindowCenterWidthExplanation"		Type="1C"	Condition="WindowCenterPresent"	# really only required if number of values > 1, but cannot check this
	Name="VOILUTFunction"					Type="1"	# really only required if not linear, but cannot check the real world intent
ModuleEnd

Module="DentalImageOnMediaProfile"
	Name="BitsAllocated"					Type="1"	BinaryEnumValues="BitsAre8Or16"
	Verify="BitsAllocated"								Condition="BitsStoredIs8"			BinaryEnumValues="BitsAre8"
	Verify="BitsAllocated"								Condition="BitsStoredGreaterThan8"	BinaryEnumValues="BitsAre16"
	Name="BitsStored"						Type="1"	BinaryEnumValues="BitsAre8Or10Or12Or16"
	Name="InstitutionName"					Type="2"
	Name="ManufacturerModelName"			Type="2"
	Name="DetectorID"						Type="2"
	Name="DetectorManufacturerName"			Type="2"
	Name="DetectorManufacturerModelName"	Type="2"
ModuleEnd

Module="MultiFrameFunctionalGroupsForBreastTomosynthesisImage"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="IdentityPixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTWithLUTMacro"				Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="IdentityPixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTWithLUTMacro"				Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRay3DFrameTypeMacro"
	SequenceEnd
ModuleEnd

DefineMacro="IdentityPixelValueTransformationMacro" InformationEntity="FunctionalGroup"
	Sequence="PixelValueTransformationSequence"		Type="1"	VM="1"
		Name="RescaleIntercept"						Type="1"	BinaryEnumValues="Zero"
		Name="RescaleSlope"							Type="1"	BinaryEnumValues="One"
		Name="RescaleType"							Type="1"	StringEnumValues="ModalityLUTTypeUnspecified"
	SequenceEnd
MacroEnd

DefineMacro="FrameVOILUTWithLUTMacro" InformationEntity="FunctionalGroup"
	Sequence="FrameVOILUTSequence"					Type="1"	VM="1"
		InvokeMacro="VOILUTMacro"
	SequenceEnd
MacroEnd

Module="BreastTomosynthesisContributingSources"
	Sequence="ContributingSourcesSequence"					Type="1"	VM="1-n"
		InvokeMacro="GeneralContributingSourcesMacro"
		InvokeMacro="ContributingImageSourcesMacro"
		Name="DetectorType"									Type="1"	StringDefinedTerms="DetectorTypeExcludingFilm"
		Name="DetectorID"									Type="1"
		Name="DateOfLastDetectorCalibration"				Type="1"
		Name="TimeOfLastDetectorCalibration"				Type="1"
		Name="DetectorElementSpacing"						Type="1"
	SequenceEnd
ModuleEnd

Module="BreastTomosynthesisAcquisition"
	Sequence="XRay3DAcquisitionSequence"					Type="1"	VM="1-n"
		Name="FieldOfViewShape"								Type="1"	StringEnumValues="BreastTomosynthesisFieldOfViewShape"
		Name="XRayReceptorType"								Type="1"	StringEnumValues="BreastTomosynthesisXRayReceptorType"
		InvokeMacro="XRay3DGeneralSharedAcquisitionMacro"
		InvokeMacro="XRay3DGeneralPositionerMovementMacro"
		Name="DistanceSourceToDetector"						Type="1"	NotZeroWarning=""
		Name="DistanceSourceToPatient"						Type="1"	NotZeroWarning=""
		Name="EstimatedRadiographicMagnificationFactor"		Type="1"
		Name="AnodeTargetMaterial"							Type="1"	StringDefinedTerms="AnodeTargetMaterial"
		Name="BodyPartThickness"							Type="1"	NotZeroWarning=""
		Name="ExposureControlMode"							Type="1"	StringDefinedTerms="ExposureControlMode"
		Name="ExposureControlModeDescription"				Type="1"
		Name="HalfValueLayer"								Type="1"	NotZeroWarning=""
		Name="OrganDose"									Type="3"	NotZeroWarning=""
		Name="EntranceDoseInmGy"							Type="3"	NotZeroWarning=""
		Name="EntranceDoseDerivation"						Type="3"	StringEnumValues="EntranceDoseDerivation"
		Name="FocalSpots"									Type="1"
		Name="DetectorBinning"								Type="1C"	NoCondition=""	# real world
		Name="DetectorTemperature"							Type="1"	NotZeroWarning=""
		Name="FilterType"									Type="1"
		Name="FilterMaterial"								Type="1"
		Name="FilterThicknessMinimum"						Type="3"	NotZeroWarning=""
		Name="FilterThicknessMaximum"						Type="3"	NotZeroWarning=""
		Name="FilterBeamPathLengthMinimum"					Type="3"	NotZeroWarning=""
		Name="FilterBeamPathLengthMaximum"					Type="3"	NotZeroWarning=""
		Name="CompressionForce"								Type="1"	NotZeroWarning=""
		Name="PaddleDescription"							Type="1"
		Sequence="PerProjectionAcquisitionSequence"			Type="1"	VM="1-n"
			InvokeMacro="XRay3DGeneralPerProjectionAcquisitionMacro"
			Name="PositionerPrimaryAngle"					Type="1"
			Name="PositionerPrimaryAngleDirection"			Type="3"	StringEnumValues="PositionerPrimaryAngleDirection"
			Name="PositionerSecondaryAngle"					Type="1C"	NoCondition=""	# real world
			Name="ExposureTimeInms"							Type="1"	NotZeroWarning=""
			Name="ExposureInmAs"							Type="1"	NotZeroWarning=""
			Name="RelativeXRayExposure"						Type="1"	NotZeroWarning=""
			Name="OrganDose"								Type="3"	NotZeroWarning=""
			Name="EntranceDoseInmGy"						Type="3"	NotZeroWarning=""
			Name="EntranceDoseDerivation"					Type="3"	StringEnumValues="EntranceDoseDerivation"
			InvokeMacro="ExposureIndexMacro"
			Name="IrradiationEventUID"						Type="3"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="BreastView"
	Name="ImageType"									Type="1"	ValueSelector="2"	StringDefinedTerms="CommonEnhancedImageAndFrameType3AndBreastTomoImageAndFrameType3"
	Verify="ImageType"												ValueSelector="3"	StringDefinedTerms="BreastTomoImageAndFrameType4"
	Verify="ImageType"												ValueSelector="4"	StringDefinedTerms="BreastTomoImageAndFrameType5"
	Sequence="ViewCodeSequence"							Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"								EnmeratedContextID="4014"
		Sequence="ViewModifierCodeSequence"				Type="2"	VM="0-n"
			InvokeMacro="CodeSequenceMacro"							EnmeratedContextID="4015"
		SequenceEnd
	SequenceEnd
	Name="BreastImplantPresent"							Type="1C"	Condition="ModalityIsMG"	StringEnumValues="YesNoFull"
	Name="PartialView"									Type="3"	StringEnumValues="YesNoFull"
	Verify="PartialView"											Condition="ViewModifierCodeSequenceIsMagnificationOrSpotCompression"	StringEnumValues="NoFull"
	Sequence="PartialViewCodeSequence"					Type="1C"	Condition="PartialViewIsYes"	VM="1-2"
		InvokeMacro="CodeSequenceMacro"								DefinedContextID="4005"
	SequenceEnd
ModuleEnd

Module="EnhancedMammographySeries"
	Name="Modality"										Type="1"	StringEnumValues="MammographyModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="RequestAttributesSequence"				Type="3"	VM="1-n"
		InvokeMacro="RequestAttributesMacro"
	SequenceEnd
ModuleEnd

Module="EnhancedMammographyImage"
	Name="PositionerMotion"								Type="1"	StringDefinedTerms="MammographyPositionerAndDetectorMotion"
	Name="PositionerType"								Type="1"	StringEnumValues="MammographyPositionerTypeWithoutNone"
	Name="ContentQualification"							Type="1"	StringEnumValues="ContentQualification"
	Name="AcquisitionDateTime"							Type="1"
	Name="AcquisitionDuration"							Type="1"
	InvokeMacro="DigitalXRayDetectorMacro"
	Name="KVP"											Type="1"
	Name="XRayTubeCurrentInmA"							Type="1C"	Condition="ExposureInmAsNotPresent" mbpo="true"
	Name="ExposureTimeInms"								Type="1C"	Condition="ExposureInmAsNotPresent" mbpo="true"
	Name="ExposureInmAs"								Type="1C"	Condition="XRayTubeCurrentInmAOrExposureTimeInmsNotPresent" mbpo="true"
	Name="FocalSpots"									Type="1"
	Name="AnodeTargetMaterial"							Type="1"	StringDefinedTerms="AnodeTargetMaterial"
	Name="BodyPartThickness"							Type="1"
	Name="CompressionForce"								Type="1"
	Name="PaddleDescription"							Type="1"
	Name="ExposureControlMode"							Type="1"	StringDefinedTerms="ExposureControlMode"
	Name="ExposureControlModeDescription"				Type="1"
	Name="PatientOrientation"							Type="1C"	Condition="ViewIsNotSpecimen" mbpo="true"
	Name="ImageComments"								Type="3"
	Name="SamplesPerPixel"								Type="1"	BinaryEnumValues="One"
	Name="PhotometricInterpretation"					Type="1"	StringEnumValues="PhotometricInterpretationMonochrome"
	Name="BitsAllocated"								Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"									Type="1"	BinaryEnumValues="BitsAre8To16"
	Name="HighBit"										Type="1"	BinaryEnumValues="BitsAre7To15"
	Name="PixelRepresentation"							Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="QualityControlImage"							Type="3"	StringEnumValues="YesNoFull"
	Name="BurnedInAnnotation"							Type="1"	StringEnumValues="NoFull"
	Name="LossyImageCompression"						Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"					Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"					Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"							Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="OrganDose"									Type="1"
	Name="EntranceDoseInmGy"							Type="1"
	Name="EntranceDoseDerivation"						Type="3"	StringEnumValues="EntranceDoseDerivation"
	Name="TypeOfDetectorMotion"							Type="1"	StringDefinedTerms="MammographyPositionerAndDetectorMotion"
	Sequence="IconImageSequence"						Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
	Name="PresentationLUTShape"							Type="1"	StringEnumValues="DXPresentationLUTShape"
ModuleEnd

DefineMacro="BreastXRayPositionerMacro"
	Sequence="PositionerPositionSequence"				Type="1"	VM="1"
		Name="PositionerPrimaryAngle"					Type="1C"	NoCondition=""
		Name="PositionerPrimaryAngleDirection"			Type="1C"	NoCondition=""	StringEnumValues="PositionerPrimaryAngleDirection"
		Name="PositionerSecondaryAngle"					Type="1C"	NoCondition=""
	SequenceEnd
MacroEnd

DefineMacro="BreastXRayDetectorMacro"
	Sequence="DetectorPositionSequence"					Type="1"	VM="1"
		Name="DetectorPrimaryAngle"						Type="1C"	NoCondition=""
		Name="DetectorSecondaryAngle"					Type="1C"	NoCondition=""
	SequenceEnd
MacroEnd

DefineMacro="BreastXRayGeometryMacro"
	Sequence="XRayGeometrySequence"						Type="1"	VM="1"
		Name="DistanceSourceToDetector"					Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="DistanceSourceToPatient"					Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="DistanceSourceToIsocenter"				Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="DistanceSourceToEntrance"					Type="3"
		Name="EstimatedRadiographicMagnificationFactor"	Type="1"
	SequenceEnd
MacroEnd

DefineMacro="BreastXRayAcquisitionDoseMacro"
	Sequence="XRayAcquisitionDoseSequence"				Type="1"	VM="1"
		Name="ExposureTimeInms"							Type="1"
		Name="ExposureInmAs"							Type="1"
		Name="RelativeXRayExposure"						Type="3"
		Name="HalfValueLayer"							Type="3"
		Name="OrganDose"								Type="1"
		Name="EntranceDoseInmGy"						Type="1"
		Name="EntranceDoseDerivation"					Type="3"	StringEnumValues="EntranceDoseDerivation"
	SequenceEnd
MacroEnd

DefineMacro="BreastXRayIsocenterReferenceSystemMacro"
	Sequence="IsocenterReferenceSystemSequence"			Type="1"	VM="1"
		Name="XRaySourceIsocenterPrimaryAngle"			Type="1"
		Name="XRaySourceIsocenterSecondaryAngle"		Type="1"
		Name="BreastSupportIsocenterPrimaryAngle"		Type="1"
		Name="BreastSupportIsocenterSecondaryAngle"		Type="1"
		Name="BreastSupportXPositionToIsocenter"		Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="BreastSupportYPositionToIsocenter"		Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="BreastSupportZPositionToIsocenter"		Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="DetectorIsocenterPrimaryAngle"			Type="1"
		Name="DetectorIsocenterSecondaryAngle"			Type="1"
		Name="DetectorXPositionToIsocenter"				Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="DetectorYPositionToIsocenter"				Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="DetectorZPositionToIsocenter"				Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="DetectorActiveAreaTLHCPosition"			Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
		Name="DetectorActiveAreaOrientation"			Type="1C"	Condition="PresentationIntentTypeIsForProcessing"	mbpo="true"
	SequenceEnd
MacroEnd

DefineMacro="XRayGridMacro"
	Sequence="XRayGridSequence"							Type="1"	VM="1"	StringDefinedTerms="XRayGrid"
		Name="Grid"										Type="1"
		InvokeMacro="XRayGridDescriptionMacro"
	SequenceEnd
MacroEnd

DefineMacro="XRayFilterMacro"
	Sequence="XRayFilterSequence"						Type="1"	VM="1"
		InvokeMacro="XRayFiltrationMacro"
	SequenceEnd
MacroEnd

Module="MultiFrameFunctionalGroupsForBreastProjectionXRayImage"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="NeedDerivationImageMacroInSharedFunctionalGroupSequenceForBreastProjection"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="IdentityPixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTWithLUTMacro"				Condition="FrameVOILUTSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FrameDisplayShutterMacro"				Condition="FrameDisplayShutterMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFrameCharacteristicsMacro"			Condition="XRayFrameCharacteristicsMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFieldOfViewMacro"					Condition="FieldOfViewSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFramePixelDataPropertiesMacro"		Condition="FramePixelDataPropertiesSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFrameDetectorParametersMacro"		Condition="XRayFrameDetectorParametersMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayCalibrationDeviceUsageMacro"		Condition="XRayCalibrationDeviceUsageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFrameAcquisitionMacro"				Condition="XRayFrameAcquisitionMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayCollimatorMacro"					Condition="CollimatorShapeSequenceSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="BreastXRayPositionerMacro"				Condition="NeedBreastXRayPositionerMacroInSharedFunctionalGroupSequence"
		InvokeMacro="BreastXRayDetectorMacro"				Condition="NeedBreastXRayDetectorMacroInSharedFunctionalGroupSequence"
		InvokeMacro="BreastXRayGeometryMacro"				Condition="XRayGeometrySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="BreastXRayAcquisitionDoseMacro"		Condition="XRayAcquisitionDoseSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="BreastXRayIsocenterReferenceSystemMacro"	Condition="IsocenterReferenceSystemSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayGridMacro"							Condition="XRayGridMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFilterMacro"						Condition="XRayFilterMacroOKInSharedFunctionalGroupSequence"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="NeedDerivationImageMacroInPerFrameFunctionalGroupSequenceForBreastProjection"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="IdentityPixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTWithLUTMacro"				Condition="FrameVOILUTSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameDisplayShutterMacro"				Condition="FrameDisplayShutterMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFrameCharacteristicsMacro"			Condition="XRayFrameCharacteristicsMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFieldOfViewMacro"					Condition="FieldOfViewSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFramePixelDataPropertiesMacro"		Condition="FramePixelDataPropertiesSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFrameDetectorParametersMacro"		Condition="XRayFrameDetectorParametersMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayCalibrationDeviceUsageMacro"		Condition="XRayCalibrationDeviceUsageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFrameAcquisitionMacro"				Condition="XRayFrameAcquisitionMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayCollimatorMacro"					Condition="CollimatorShapeSequenceSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="BreastXRayPositionerMacro"				Condition="NeedBreastXRayPositionerMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="BreastXRayDetectorMacro"				Condition="NeedBreastXRayDetectorMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="BreastXRayGeometryMacro"				Condition="XRayGeometrySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="BreastXRayAcquisitionDoseMacro"		Condition="XRayAcquisitionDoseSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="BreastXRayIsocenterReferenceSystemMacro"	Condition="IsocenterReferenceSystemSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="XRayGridMacro"							Condition="XRayGridMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFilterMacro"						Condition="XRayFilterMacroOKInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd
Module="VLImage"
	Name="ImageType"									Type="1"	ValueSelector="0"	StringEnumValues="ImageType1"
	Verify="ImageType"									Type="1"	ValueSelector="1"	StringEnumValues="ImageType2"
	Verify="ImageType"									Type="1"	ValueSelector="2"	StringEnumValues="VLImageType3"
	Name="PhotometricInterpretation"					Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2OrRGBorYBRFULL422orYBRPARTIAL420orYBRRCTorYBRICT"

	Verify="PhotometricInterpretation"				Condition="UncompressedTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"				Condition="JPEGLSLosslessTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"				Condition="JPEG2000TransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRICT"
	Verify="PhotometricInterpretation"				Condition="JPEG2000LosslessTransferSyntaxAndThreeSamples"				StringEnumValues="PhotometricInterpretationYBRRCT"
	Verify="PhotometricInterpretation"				Condition="MPEG2TransferSyntax"											StringEnumValues="PhotometricInterpretationYBRPartial420"	# regardless of number of samples (required to be 3 by PS 3.5)
	Verify="PhotometricInterpretation"				Condition="JPEGLossyTransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRFull422"

	Name="BitsAllocated"								Type="1"	BinaryEnumValues="BitsAre8"
	Name="BitsStored"									Type="1"	BinaryEnumValues="BitsAre8"
	Name="HighBit"										Type="1"	BinaryEnumValues="BitsAre7"
	Name="PixelRepresentation"							Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="SamplesPerPixel"								Type="1"	BinaryEnumValues="SamplesPerPixelIsOneOrThree"
	Verify="SamplesPerPixel"										Condition="PhotometricInterpretationNeedsOneSample"	BinaryEnumValues="One"
	Verify="SamplesPerPixel"										Condition="PhotometricInterpretationNeedsThreeSamples"	BinaryEnumValues="Three"
	Name="PlanarConfiguration"							Type="1C"	BinaryEnumValues="PlanarConfigurationIsColorByPixel"	Condition="SamplesPerPixelGreaterThanOne"
	Name="ContentTime"									Type="1C"	NoCondition=""	# "if temporally related" ... real world
	Name="LossyImageCompression"						Type="2"	StringEnumValues="LossyImageCompression"
	Sequence="ReferencedImageSequence"					Type="1C"	VM="1-n"	Condition="ImageTypeValue3StereoLOrR" mbpo="true"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"		Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"							DefinedContextID="7201"
		SequenceEnd
	SequenceEnd
	Name="WindowCenter"									Type="3C"	Condition="PhotometricInterpretationIsMonochrome2"
	Name="WindowWidth"									Type="1C"	Condition="WindowCenterPresent" 	NotZeroError=""
	Verify="WindowWidth"											Condition="WindowWidthIsNegative"	ThenErrorMessage="Not permitted to be negative" ShowValueWithMessage="true"
	Name="ImageLaterality"								Type="3"	StringEnumValues="ImageLaterality"
	Sequence="AnatomicRegionSequence"					Type="1C"	VM="1"	Condition="MultiFrameIODAndNotSpecimen" mbpo="true"
		InvokeMacro="CodeSequenceMacro"
		Sequence="AnatomicRegionModifierSequence"		Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="2"
		SequenceEnd
	SequenceEnd
	InvokeMacro="PrimaryAnatomicStructureMacro"
	Sequence="ChannelDescriptionCodeSequence"			Type="3"	VM="1-3"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4206"
	SequenceEnd
	Name="PixelSpacing"									Type="3"	NotZeroError=""
	Name="ImagerPixelSpacing"							Type="3"	NotZeroError=""
ModuleEnd

Module="VLEndoscopicSeriesPseudo"
	Name="Modality"										Type="1"	StringEnumValues="VLEndoscopyModality"
ModuleEnd

Module="VLMicroscopicSeriesPseudo"
	Name="Modality"										Type="1"	StringEnumValues="VLMicroscopyModality"
ModuleEnd

Module="VLSlideCoordinatesMicroscopicSeriesPseudo"
	Name="Modality"										Type="1"	StringEnumValues="VLSlideCoordinatesMicroscopyModality"
ModuleEnd

Module="VLPhotographicSeriesPseudo"
	Name="Modality"										Type="1"	StringEnumValues="VLPhotographyModality"
ModuleEnd

Module="SlideCoordinates"
	Sequence="ImageCenterPointCoordinatesSequence"		Type="2"	VM="0-1"
		Name="XOffsetInSlideCoordinateSystem"			Type="1"
		Name="YOffsetInSlideCoordinateSystem"			Type="1"
		Name="ZOffsetInSlideCoordinateSystem"			Type="2"
	SequenceEnd
ModuleEnd

Module="OphthalmicPhotographySeries"
	Name="Modality"										Type="1"	StringEnumValues="OphthalmologyModality"
ModuleEnd

Module="OphthalmicPhotography8BitImagePseudo"
	Name="BitsAllocated"								Type="1"	BinaryEnumValues="BitsAre8"
	Name="BitsStored"									Type="1"	BinaryEnumValues="BitsAre8"
	Name="HighBit"										Type="1"	BinaryEnumValues="BitsAre7"
ModuleEnd

Module="OphthalmicPhotography16BitImagePseudo"
	Name="BitsAllocated"								Type="1"	BinaryEnumValues="BitsAre16"
	Name="BitsStored"									Type="1"	BinaryEnumValues="BitsAre16"
	Name="HighBit"										Type="1"	BinaryEnumValues="BitsAre15"
ModuleEnd

Module="OphthalmicPhotographyImage"
	Name="ImageType"									Type="1"	ValueSelector="0"	StringEnumValues="ImageType1"
	Verify="ImageType"									Type="1"	ValueSelector="1"	StringEnumValues="OphthalmologyImageType2"
	
	Verify="ImageType"									Type="1"	Condition="ImageTypeValue1Derived" ValueSelector="2"	StringDefinedTerms="OphthalmologyImageType3IfDerived"
	Verify="ImageType"												Condition="ImageTypeValue1DerivedAndImageTypeValue3MissingOrEmpty"	ThenErrorMessage="A value for Value 3 is required for DERIVED images"
	Verify="ImageType"												Condition="ImageTypeValue1NotDerivedAndImageTypeValueNotMissingOrEmpty"	ThenErrorMessage="A value for Value 3 may not be present for non-DERIVED images"
	
	Verify="ImageType"									Type="1"	ValueSelector="3"	StringDefinedTerms="OphthalmologyImageType4"

	Name="InstanceNumber"								Type="1"
	Name="SamplesPerPixel"								Type="1"	BinaryEnumValues="SamplesPerPixelIsOneOrThree"
	Verify="SamplesPerPixel"										Condition="PhotometricInterpretationNeedsOneSample"	BinaryEnumValues="One"
	Verify="SamplesPerPixel"										Condition="PhotometricInterpretationNeedsThreeSamples"	BinaryEnumValues="Three"
	Name="SamplesPerPixelUsed"							Type="1C"	NoCondition="" BinaryEnumValues="SamplesPerPixelUsedIsTwo"		# condition is real world
	Name="PhotometricInterpretation"					Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2OrRGBorYBRFULL422orYBRPARTIAL420orYBRRCTorYBRICT"

	Verify="PhotometricInterpretation"				Condition="UncompressedTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"				Condition="JPEGLSLosslessTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"				Condition="JPEG2000TransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRICT"
	Verify="PhotometricInterpretation"				Condition="JPEG2000LosslessTransferSyntaxAndThreeSamples"				StringEnumValues="PhotometricInterpretationYBRRCT"
	Verify="PhotometricInterpretation"				Condition="MPEG2TransferSyntax"											StringEnumValues="PhotometricInterpretationYBRPartial420"	# regardless of number of samples (required to be 3 by PS 3.5)
	Verify="PhotometricInterpretation"				Condition="JPEGLossyTransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRFull422"

	Name="PixelRepresentation"							Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="PlanarConfiguration"							Type="1C"	BinaryEnumValues="PlanarConfigurationIsColorByPixel"	Condition="SamplesPerPixelGreaterThanOne"
	Name="PixelSpacing"									Type="1C"	NotZeroError=""	NoCondition=""		# too hard to check code in Acquisition Device Type Code Sequence :(
	Name="ContentDate"									Type="1"
	Name="ContentTime"									Type="1"
	Name="AcquisitionDateTime"							Type="1C"	Condition="ImageTypeValue1Original" mbpo="true"
	Sequence="SourceImageSequence"						Type="2C"	VM="0-n"	Condition="ImageTypeValue1Derived"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"		Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"							DefinedContextID="7202"
		SequenceEnd
	SequenceEnd
	Name="LossyImageCompression"						Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"					Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"					Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"							Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="PresentationLUTShape"							Type="1C"	Condition="PhotometricInterpretationIsMonochrome2"	StringEnumValues="IdentityPresentationLUTShape"
	Name="CalibrationImage"								Type="3"	StringEnumValues="YesNoFull"
	Name="BurnedInAnnotation"							Type="1"	StringEnumValues="YesNoFull"
	Name="RecognizableVisualFeatures"					Type="3"	StringEnumValues="YesNoFull"
ModuleEnd

Module="OphthalmicPhotographicParameters"
	Sequence="AcquisitionDeviceTypeCodeSequence"		Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4202"
	SequenceEnd
	Sequence="IlluminationTypeCodeSequence"				Type="2"	VM="0-1"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4203"
	SequenceEnd
	Sequence="LightPathFilterTypeStackCodeSequence"		Type="2"	VM="0-n"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4204"
	SequenceEnd
	Name="LightPathFilterPassThroughWavelength"			Type="3"
	Name="LightPathFilterPassBand"						Type="3"
	Sequence="ImagePathFilterTypeStackCodeSequence"		Type="2"	VM="0-n"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4204"
	SequenceEnd
	Name="ImagePathFilterPassThroughWavelength"			Type="3"
	Name="ImagePathFilterPassBand"						Type="3"
	Sequence="LensesCodeSequence"						Type="2"	VM="0-n"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4205"
	SequenceEnd
	Name="DetectorType"									Type="2"	StringDefinedTerms="OphthalmologyDetectorType"
	Sequence="ChannelDescriptionCodeSequence"			Type="1C"	VM="1-3"	NoCondition=""
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4206"
	SequenceEnd
	Name="CameraAngleOfView"							Type="3"
ModuleEnd

DefineMacro="OphthalmicAcquisitionParametersMacro" InformationEntity="Image"
	Sequence="RefractiveStateSequence"					Type="2"	VM="0-1"
		Name="SphericalLensPower"						Type="1"	NotZeroWarning=""
		Name="CylinderLensPower"						Type="1"	NotZeroWarning=""
		Name="CylinderAxis"								Type="1"	NotZeroWarning=""
	SequenceEnd
	Name="EmmetropicMagnification"						Type="2"	NotZeroWarning=""
	Name="IntraOcularPressure"							Type="2"	NotZeroWarning=""
	Name="PupilDilated"									Type="2"	StringEnumValues="YesNoFull"
	Sequence="MydriaticAgentSequence"					Type="2C"	VM="0-n"	Condition="PupilDilatedIsYes"
		Sequence="MydriaticAgentCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="4208"
		SequenceEnd
		Name="MydriaticAgentConcentration"				Type="3"	NotZeroWarning=""
		Sequence="MydriaticAgentConcentrationUnitsSequence"	Type="1C"	VM="1" Condition="MydriaticAgentConcentrationIsPresent"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="3082"
		SequenceEnd
	SequenceEnd
	Name="DegreeOfDilation"								Type="2C"	Condition="PupilDilatedIsYes"
MacroEnd

Module="OphthalmicPhotographyAcquisitionParameters"
	Name="PatientEyeMovementCommanded"					Type="2"	StringEnumValues="YesNoFull"
	Sequence="PatientEyeMovementCommandCodeSequence"	Type="1C"	VM="1"	Condition="PatientEyeMovementCommandedIsYes"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4201"
	SequenceEnd
	Name="HorizontalFieldOfView"						Type="2"	NotZeroWarning=""
	InvokeMacro="OphthalmicAcquisitionParametersMacro"
ModuleEnd

Module="OcularRegionImaged"
	Name="ImageLaterality"								Type="1"	StringEnumValues="OphthalmologyImageLaterality"
	Sequence="RelativeImagePositionCodeSequence"		Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4207"
	SequenceEnd
	InvokeMacro="GeneralAnatomyMandatoryMacro"
ModuleEnd

Module="StereometricSeries"
	Name="Modality"										Type="1"	StringEnumValues="StereometricModality"
ModuleEnd

Module="StereometricRelationship"
	Sequence="StereoPairsSequence"						Type="1"	VM="1-n"
		Name="StereoBaselineAngle"						Type="3"
		Name="StereoBaselineDisplacement"				Type="3"
		Name="StereoHorizontalPixelOffset"				Type="3"
		Name="StereoVerticalPixelOffset"				Type="3"
		Name="StereoRotation"							Type="3"
		Sequence="LeftImageSequence"					Type="1"	VM="1"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="RightImageSequence"					Type="1"	VM="1"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="OphthalmicTomographySeries"
	Name="Modality"										Type="1"	StringEnumValues="OphthalmicTomographyModality"
	Name="SeriesNumber"									Type="1"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="0-1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="OphthalmicTomographyImage"
	Name="ImageType"									Type="1"	ValueSelector="0"	StringEnumValues="ImageType1"
	Verify="ImageType"									Type="1"	ValueSelector="1"	StringEnumValues="ImageType2"
	Name="SamplesPerPixel"								Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="AcquisitionDateTime"							Type="1"
	Name="AcquisitionDuration"							Type="1C"	Condition="ImageTypeValue1Original" mbpo="true"
	Name="AcquisitionNumber"							Type="1"
	Name="PhotometricInterpretation"					Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="PixelRepresentation"							Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="BitsAllocated"								Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"									Type="1"	BinaryEnumValues="BitsAre8Or12Or16"
	Name="HighBit"										Type="1"	BinaryEnumValues="BitsAre7Or11Or15"
	Name="PresentationLUTShape"							Type="1"	StringEnumValues="IdentityPresentationLUTShape"
	Name="LossyImageCompression"						Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"					Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"					Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"							Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="BurnedInAnnotation"							Type="1"	StringEnumValues="NoFull"
	Name="RecognizableVisualFeatures"					Type="3"	StringEnumValues="YesNoFull"
	Name="ConcatenationFrameOffsetNumber"				Type="1"	BinaryEnumValues="Zero"
	Name="InConcatenationNumber"						Type="1"	BinaryEnumValues="One"
	Name="InConcatenationTotalNumber"					Type="1"	BinaryEnumValues="One"
	Name="ImageComments"								Type="3"
ModuleEnd

Module="OphthalmicTomographyAcquisitionParameters"
	Name="AxialLengthOfTheEye"							Type="2"	NotZeroWarning=""
	Name="HorizontalFieldOfView"						Type="2"	NotZeroWarning=""
	InvokeMacro="OphthalmicAcquisitionParametersMacro"
ModuleEnd

Module="OphthalmicTomographyParameters"
	Sequence="AcquisitionDeviceTypeCodeSequence"		Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4210"
	SequenceEnd
	Sequence="LightPathFilterTypeStackCodeSequence"		Type="2"	VM="0-n"
		InvokeMacro="CodeSequenceMacro"								BaselineContextID="4204"
	SequenceEnd
	Name="LightPathFilterPassThroughWavelength"			Type="3"
	Name="LightPathFilterPassBand"						Type="3"
	Name="DetectorType"									Type="1"	StringDefinedTerms="OphthalmicTomographyDetectorType"
	Name="IlluminationWaveLength"						Type="1C"	Condition="AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner" mbpo="true"
	Name="IlluminationPower"							Type="1C"	Condition="AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner" mbpo="true"
	Name="IlluminationBandwidth"						Type="1C"	Condition="AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner" mbpo="true"
	Name="DepthSpatialResolution"						Type="1C"	Condition="AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner" mbpo="true"
	Name="MaximumDepthDistortion"						Type="1C"	Condition="AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner" mbpo="true"
	Name="AlongScanSpatialResolution"					Type="1C"	Condition="AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner" mbpo="true"
	Name="MaximumAlongScanDistortion"					Type="1C"	Condition="AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner" mbpo="true"
	Name="AcrossScanSpatialResolution"					Type="1C"	Condition="AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner" mbpo="true"
	Name="MaximumAcrossScanDistortion"					Type="1C"	Condition="AcquisitionDeviceTypeCodeSequenceIsOpticalCoherenceTomographyScanner" mbpo="true"
ModuleEnd

DefineMacro="OphthalmicFrameLocationMacro" InformationEntity="Frame"
	Sequence="OphthalmicFrameLocationSequence"			Type="1"	VM="1-n"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
			Name="CodeValue"							Type="1"	VM="1" StringDefinedTerms="LocalizerDCMCodeValue"		# this is a bit hokey, but cannot parametrize invocation yet, and macro as nested as if modules not inline :(
		SequenceEnd
		Name="ReferenceCoordinates"						Type="1"
		Name="DepthOfTransverseImage"					Type="2C"	Condition="OphthalmicImageOrientationIsTransverse"
		Name="OphthalmicImageOrientation"				Type="1"	StringEnumValues="OphthalmicImageOrientation"
	SequenceEnd
MacroEnd

Module="MultiFrameFunctionalGroupsForOphthalmicTomography"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"			Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"			Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"			Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"			Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"			Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"				Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"	Condition="NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="OphthalmicFrameLocationMacro"	Condition="NeedOphthalmicFrameLocationMacroInSharedFunctionalGroupSequence"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"			Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"			Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"			Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"			Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"			Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"				Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"	Condition="NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="OphthalmicFrameLocationMacro"	Condition="NeedOphthalmicFrameLocationMacroInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd


Module="WholeSlideMicroscopySeries"
	Name="Modality"										Type="1"	StringEnumValues="VLWholeSlideMicroscopyModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="WholeSlideMicroscopyImage"
	Name="ImageType"									Type="1"	VM="4"
	Verify="ImageType"									Type="1"	ValueSelector="0"	StringEnumValues="WholeSlideImageType1"
	Verify="ImageType"									Type="1"	ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
	Verify="ImageType"									Type="1"	ValueSelector="2"	StringDefinedTerms="WholeSlideImageType3"
	Verify="ImageType"									Type="1"	ValueSelector="3"	StringDefinedTerms="WholeSlideImageType4"
	Name="ImagedVolumeWidth"							Type="1"	NotZeroError=""
	Name="ImagedVolumeHeight"							Type="1"	NotZeroError=""
	Name="ImagedVolumeDepth"							Type="1"	NotZeroError=""
	Name="TotalPixelMatrixColumns"						Type="1"	NotZeroError=""
	Name="TotalPixelMatrixRows"							Type="1"	NotZeroError=""
	Name="TotalPixelMatrixFocalPlanes"					Type="1C"	Condition="DimensionOrganizationTypeIsTILED_FULL"	mbpo="true"	NotZeroError=""
	Sequence="TotalPixelMatrixOriginSequence"			Type="1"	VM="1"
		Name="XOffsetInSlideCoordinateSystem"			Type="1"
		Name="YOffsetInSlideCoordinateSystem"			Type="1"
	SequenceEnd
	Name="ImageOrientationSlide"						Type="1"
	Name="SamplesPerPixel"								Type="1"	BinaryEnumValues="SamplesPerPixelIsOneOrThree"
	Verify="SamplesPerPixel"										Condition="PhotometricInterpretationNeedsOneSample"	BinaryEnumValues="One"
	Verify="SamplesPerPixel"										Condition="PhotometricInterpretationNeedsThreeSamples"	BinaryEnumValues="Three"
	Name="PhotometricInterpretation"					Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2OrRGBorYBRFULL422orYBRRCTorYBRICT"

	Verify="PhotometricInterpretation"								Condition="UncompressedTransferSyntaxAndOneSample"			StringEnumValues="PhotometricInterpretationMonochrome2"
	# it probably isn't intended, but current text actually prohibits compression of monochrome WSI
	Verify="PhotometricInterpretation"								Condition="UncompressedTransferSyntaxAndThreeSamples"		StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"								Condition="JPEGLSLosslessTransferSyntaxAndThreeSamples"		StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"								Condition="JPEG2000LosslessTransferSyntaxAndThreeSamples"	StringEnumValues="PhotometricInterpretationYBRRCTOrRGB"
	Verify="PhotometricInterpretation"								Condition="JPEG2000TransferSyntaxAndThreeSamples"			StringEnumValues="PhotometricInterpretationYBRRCTOrICTOrRGB"
	Verify="PhotometricInterpretation"								Condition="JPEGLossyTransferSyntaxAndThreeSamples"			StringEnumValues="PhotometricInterpretationYBRFull422OrRGB"

	Name="PlanarConfiguration"							Type="1C"	BinaryEnumValues="PlanarConfigurationIsColorByPixel"	Condition="SamplesPerPixelGreaterThanOne"
	Name="NumberOfFrames"								Type="1"
	Verify="NumberOfFrames"											Condition="ImageTypeValue3LocalizerOrLabelOrOverview"	BinaryEnumValues="One"
	Name="BitsAllocated"								Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"									Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="HighBit"										Type="1"	BinaryEnumValues="BitsAre7Or15"
	Name="PixelRepresentation"							Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="AcquisitionDateTime"							Type="1"
	Name="AcquisitionDuration"							Type="3"
	Name="LossyImageCompression"						Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"					Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"					Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"							Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="PresentationLUTShape"							Type="1C"	Condition="PhotometricInterpretationIsMonochrome2"	StringEnumValues="IdentityPresentationLUTShape"
	Name="RescaleSlope"									Type="1C"	Condition="PhotometricInterpretationIsMonochrome2"	BinaryEnumValues="One"
	Name="RescaleIntercept"								Type="1C"	Condition="PhotometricInterpretationIsMonochrome2"	BinaryEnumValues="Zero"
	Name="VolumetricProperties"							Type="1"	StringEnumValues="VolumetricPropertiesVolume"
	Name="SpecimenLabelInImage"							Type="1"	StringEnumValues="YesNoFull"
	Name="BurnedInAnnotation"							Type="1"	StringEnumValues="YesNoFull"
	Name="FocusMethod"									Type="1"	StringEnumValues="WholeSlideFocusMethod"
	Name="ExtendedDepthOfField"							Type="1"	StringEnumValues="YesNoFull"
	Name="NumberOfFocalPlanes"							Type="1C"	Condition="ExtendedDepthOfFieldIsYes"	NotZeroError=""
	Name="DistanceBetweenFocalPlanes"					Type="1C"	Condition="ExtendedDepthOfFieldIsYes"	NotZeroError=""
	Name="AcquisitionDeviceProcessingDescription"		Type="3"
	Name="ConvolutionKernel"							Type="3"
	Name="RecommendedAbsentPixelCIELabValue"			Type="3"
ModuleEnd

Module="OpticalPath"
	Name="NumberOfOpticalPaths"							Type="1C"	Condition="DimensionOrganizationTypeIsTILED_FULL"	mbpo="true"
	Sequence="OpticalPathSequence"						Type="1"	VM="1-n"
		Name="OpticalPathIdentifier"					Type="1"
		Name="OpticalPathDescription"					Type="3"
		Sequence="IlluminatorTypeCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="IlluminationWaveLength"					Type="1C"	Condition="IlluminationColorCodeSequenceNotPresent"	mbpo="true"
		Verify="IlluminationWaveLength"								Condition="IlluminationWaveLengthInvalid"	ThenErrorMessage="Invalid value - required to be greater than zero"
		Sequence="IlluminationColorCodeSequence"		Type="1C"	VM="1"	Condition="IlluminationWaveLengthNotPresent"	mbpo="true"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="IlluminationTypeCodeSequence"			Type="1"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="LightPathFilterTypeStackCodeSequence"	Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="LightPathFilterPassThroughWavelength"		Type="3"	NotZeroWarning=""
		Name="LightPathFilterPassBand"					Type="3"	NotZeroWarning=""	# one of the two value may be zero length, but not zero
		Sequence="ImagePathFilterTypeStackCodeSequence"	Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="ImagePathFilterPassThroughWavelength"		Type="3"	NotZeroWarning=""
		Name="ImagePathFilterPassBand"					Type="3"	NotZeroWarning=""	# one of the two value may be zero length, but not zero
		Sequence="LensesCodeSequence"					Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="CondenserLensPower"						Type="3"	NotZeroWarning=""
		Name="ObjectiveLensPower"						Type="3"	NotZeroWarning=""
		Name="ObjectiveLensNumericalAperture"			Type="3"	NotZeroWarning=""
		Sequence="ChannelDescriptionCodeSequence"		Type="1C"	NoCondition=""	VM="1-3"			# real-world condition but should check number of items matches Samples per Pixel Used or Samples per Pixel :(
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="PaletteColorLookupTableSequence"		Type="3"	VM="1"
			InvokeMacro="PaletteColorLookupTableMacro"
		SequenceEnd
		Name="ICCProfile"								Type="1C"	Condition="NeedICCProfileInOpticalPathSequence"
		Name="ColorSpace"								Type="3"
	SequenceEnd
ModuleEnd

DefineMacro="PlanePositionSlideMacro" InformationEntity="FunctionalGroup"
	Sequence="PlanePositionSlideSequence"				Type="1"	VM="1"
		Name="ColumnPositionInTotalImagePixelMatrix"	Type="1"	NotZeroError=""
		Name="RowPositionInTotalImagePixelMatrix"		Type="1"	NotZeroError=""
		Name="XOffsetInSlideCoordinateSystem"			Type="1"
		Name="YOffsetInSlideCoordinateSystem"			Type="1"
		Name="ZOffsetInSlideCoordinateSystem"			Type="1"
	SequenceEnd
MacroEnd

DefineMacro="OpticalPathIdentificationMacro" InformationEntity="FunctionalGroup"
	Sequence="OpticalPathIdentificationSequence"		Type="1"	VM="1"
		Name="OpticalPathIdentifier"					Type="1"
	SequenceEnd
MacroEnd

DefineMacro="SpecimenReferenceMacro" InformationEntity="FunctionalGroup"
	Sequence="SpecimenReferenceSequence"				Type="2"	VM="0-1"
		Name="SpecimenUID"								Type="1"
	SequenceEnd
MacroEnd

DefineMacro="WholeSlideMicroscopyImageFrameTypeMacro" InformationEntity="FunctionalGroup"
	Sequence="WholeSlideMicroscopyImageFrameTypeSequence"	Type="1"	VM="1"
		Name="FrameType"									Type="1"	VM="4"
		Verify="FrameType"												ValueSelector="0"	StringEnumValues="WholeSlideImageType1"
		Verify="FrameType"												ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
		Verify="FrameType"												ValueSelector="2"	StringDefinedTerms="WholeSlideImageType3"
		Verify="FrameType"												ValueSelector="3"	StringDefinedTerms="WholeSlideImageType4"
	SequenceEnd
MacroEnd

Module="MultiResolutionNavigation"
	Sequence="ReferencedImageNavigationSequence"		Type="1"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
		Name="ReferencedFrameNumber"					Type="1"	VM="1"	NotZeroError=""
		Name="TopLeftHandCornerOfLocalizerArea"			Type="1"
		Name="BottomRightHandCornerOfLocalizerArea"		Type="1"
		Name="PixelSpacing"								Type="1"	NotZeroError=""
		Name="ZOffsetInSlideCoordinateSystem"			Type="1"
		Name="SamplesPerPixel"							Type="1"
		Name="OpticalPathIdentifier"					Type="1"
	SequenceEnd
ModuleEnd

Module="SlideLabel"
	Name="BarcodeValue"									Type="2"
	Name="LabelText"									Type="2"
ModuleEnd

Module="MultiFrameFunctionalGroupsForWholeSlideMicroscopy"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"
		InvokeMacro="ReferencedImageMacro"				Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"				Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"		Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2"
		InvokeMacro="PlanePositionSlideMacro"			Condition="NeedPlanePositionSlideMacroInSharedFunctionalGroupSequenceForWholeSlideMicroscopy"
		InvokeMacro="OpticalPathIdentificationMacro"	Condition="NeedOpticalPathIdentificationMacroInSharedFunctionalGroupSequenceForWholeSlideMicroscopy"
		InvokeMacro="SpecimenReferenceMacro"			Condition="SpecimenReferenceMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="WholeSlideMicroscopyImageFrameTypeMacro"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"	Type="1C"	VM="1-n"	Condition="PerFrameFunctionalGroupsSequencePresent"
		InvokeMacro="FrameContentMacro"					Condition="FrameContentMacroPresent"
		InvokeMacro="ReferencedImageMacro"				Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"				Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"		Condition="RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2"
		InvokeMacro="PlanePositionSlideMacro"			Condition="NeedPlanePositionSlideMacroInPerFrameFunctionalGroupSequenceForWholeSlideMicroscopy"
		InvokeMacro="OpticalPathIdentificationMacro"	Condition="NeedOpticalPathIdentificationMacroInPerFrameFunctionalGroupSequenceForWholeSlideMicroscopy"
		InvokeMacro="SpecimenReferenceMacro"			Condition="SpecimenReferenceMacroOKInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="LensometryMeasurementsSeries"
	Name="Modality"										Type="1"			StringEnumValues="LensometryModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="AutorefractionMeasurementsSeries"
	Name="Modality"										Type="1"			StringEnumValues="AutorefractionModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="KeratometryMeasurementsSeries"
	Name="Modality"										Type="1"			StringEnumValues="KeratometryModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="SubjectiveRefractionMeasurementsSeries"
	Name="Modality"										Type="1"			StringEnumValues="SubjectiveRefractionModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="VisualAcuityMeasurementsSeries"
	Name="Modality"										Type="1"			StringEnumValues="VisualAcuityModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

DefineMacro="CylinderSequenceMacro"
	Sequence="CylinderSequence"							Type="1C"	VM="1"	NoCondition=""
		Name="CylinderPower"							Type="1"		
		Name="CylinderAxis"								Type="1"		
	SequenceEnd
MacroEnd

DefineMacro="PrismSequenceMacro"
	Sequence="PrismSequence"							Type="1C"	VM="1"	NoCondition=""
		Name="HorizontalPrismPower"						Type="1"		
		Name="HorizontalPrismBase"						Type="1"		
		Name="VerticalPrismPower"						Type="1"		
		Name="VerticalPrismBase"						Type="1"		
	SequenceEnd
MacroEnd

Module="GeneralOphthalmicRefractiveMeasurements"
	Name="InstanceNumber"								Type="1"		
	Name="ContentDate"									Type="1"		
	Name="ContentTime"									Type="1"		
	Name="MeasurementLaterality"						Type="3"			StringEnumValues="OphthalmicRefractiveMeasurementLaterality"
	Name="ImageComments"								Type="3"		
	Sequence="ReferencedRefractiveMeasurementsSequence"	Type="2C"	VM="0-n"	Condition="VisualAcuityTypeCodeSequencePresent"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="LensometryMeasurements"
	Name="LensDescription"								Type="2"		
	Sequence="RightLensSequence"						Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="LensometryMeasurementsMacro"
	SequenceEnd
	Sequence="LeftLensSequence"							Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="LensometryMeasurementsMacro"
	SequenceEnd
	Sequence="UnspecifiedLateralityLensSequence"		Type="1C"	VM="1"	Condition="RightLensSequenceAndLeftLensSequenceAbsent"
		InvokeMacro="LensometryMeasurementsMacro"
	SequenceEnd
ModuleEnd

DefineMacro="LensometryMeasurementsMacro"
	Name="SpherePower"									Type="1"		
	InvokeMacro="CylinderSequenceMacro"
	Sequence="AddNearSequence"							Type="1C"	VM="1"	NoCondition=""
		Name="AddPower"									Type="1"		
		Name="ViewingDistance"							Type="3"		
	SequenceEnd
	Sequence="AddIntermediateSequence"					Type="1C"	VM="1"	NoCondition=""
		Name="AddPower"									Type="1"		
		Name="ViewingDistance"							Type="3"		
	SequenceEnd
	InvokeMacro="PrismSequenceMacro"
	Name="LensSegmentType"								Type="3"	VM="1"	StringEnumValues="LensSegmentType"
	Name="OpticalTransmittance"							Type="3"		
	Name="ChannelWidth"									Type="3"		
MacroEnd

Module="AutorefractionMeasurements"
	Sequence="AutorefractionRightEyeSequence"			Type="1C"	VM="1"	NoCondition=""
		Name="SpherePower"								Type="1"		
		InvokeMacro="CylinderSequenceMacro"
		Name="PupilSize"								Type="3"		
		Name="CornealSize"								Type="3"		
	SequenceEnd
	Sequence="AutorefractionLeftEyeSequence"			Type="1C"	VM="1"	NoCondition=""
		Name="SpherePower"								Type="1"		
		InvokeMacro="CylinderSequenceMacro"
		Name="PupilSize"								Type="3"		
		Name="CornealSize"								Type="3"		
	SequenceEnd
	Name="DistancePupillaryDistance"					Type="3"		
	Name="NearPupillaryDistance"						Type="3"		
ModuleEnd

Module="KeratometryMeasurements"
	Sequence="KeratometryRightEyeSequence"				Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="KeratometricMeasurementsMacro"
	SequenceEnd
	Sequence="KeratometryLeftEyeSequence"				Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="KeratometricMeasurementsMacro"
	SequenceEnd
ModuleEnd

DefineMacro="KeratometricMeasurementsMacro"
	Sequence="SteepKeratometricAxisSequence"			Type="1"	VM="1"
		Name="RadiusOfCurvature"						Type="1"
		Name="KeratometricPower"						Type="1"
		Name="KeratometricAxis"							Type="1"
	SequenceEnd
	Sequence="FlatKeratometricAxisSequence"				Type="1"	VM="1"
		Name="RadiusOfCurvature"						Type="1"
		Name="KeratometricPower"						Type="1"
		Name="KeratometricAxis"							Type="1"
	SequenceEnd
MacroEnd

Module="SubjectiveRefractionMeasurements"
	Sequence="SubjectiveRefractionRightEyeSequence"		Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="SubjectiveRefractionMeasurementsMacro"
	SequenceEnd
	Sequence="SubjectiveRefractionLeftEyeSequence"		Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="SubjectiveRefractionMeasurementsMacro"
	SequenceEnd
	Name="DistancePupillaryDistance"					Type="3"
	Name="NearPupillaryDistance"						Type="3"
	Name="IntermediatePupillaryDistance"				Type="3"
	Name="OtherPupillaryDistance"						Type="3"
ModuleEnd

DefineMacro="SubjectiveRefractionMeasurementsMacro"
	Name="SpherePower"									Type="1"
	InvokeMacro="CylinderSequenceMacro"
	InvokeMacro="PrismSequenceMacro"
	Sequence="AddNearSequence"							Type="1C"	VM="1"	NoCondition=""
		Name="AddPower"									Type="1"
		Name="ViewingDistance"							Type="3"
	SequenceEnd
	Sequence="AddIntermediateSequence"					Type="1C"	VM="1"	NoCondition=""
		Name="AddPower"									Type="1"
		Name="ViewingDistance"							Type="3"
	SequenceEnd
	Sequence="AddOtherSequence"							Type="1C"	VM="1"	NoCondition=""
		Name="AddPower"									Type="1"
		Name="ViewingDistance"							Type="3"
	SequenceEnd
MacroEnd

Module="VisualAcuityMeasurements"
	Name="ViewingDistanceType"							Type="1"	StringEnumValues="ViewingDistanceType"
	Sequence="VisualAcuityTypeCodeSequence"				Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"					DefinedContextID="4216"
	SequenceEnd
	Name="BackgroundColor"								Type="1"	StringDefinedTerms="VisualAcuityMeasurementsBackgroundColor"
	Name="Optotype"										Type="1"	StringDefinedTerms="Optotype"
	Name="OptotypeDetailedDefinition"					Type="1C"	Condition="OptotypeIsLettersNumbersOrPictures"
	Name="OptotypePresentation"							Type="1"	StringEnumValues="OptotypePresentation"
	Sequence="VisualAcuityRightEyeSequence"				Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="VisualAcuityMeasurementsMacro"
	SequenceEnd
	Sequence="VisualAcuityLeftEyeSequence"				Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="VisualAcuityMeasurementsMacro"
	SequenceEnd
	Sequence="VisualAcuityBothEyesOpenSequence"			Type="3"	VM="1"
		InvokeMacro="VisualAcuityMeasurementsMacro"
	SequenceEnd
ModuleEnd

DefineMacro="VisualAcuityMeasurementsMacro"
	Name="DecimalVisualAcuity"							Type="1"
	Name="VisualAcuityModifiers"						Type="3"
MacroEnd

Module="OphthalmicAxialMeasurementsSeries"
	Name="Modality"										Type="1"			StringEnumValues="OphthalmicAxialMeasurementsModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="OphthalmicAxialMeasurements"
	Name="OphthalmicAxialMeasurementsDeviceType"			Type="1"			StringDefinedTerms="OphthalmicAxialMeasurementsDeviceType"
	Sequence="OphthalmicUltrasoundMethodCodeSequence"		Type="1C"	VM="1"	Condition="OphthalmicAxialMeasurementsDeviceTypeIsUltrasound"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="AnteriorChamberDepthDefinitionCodeSequence"	Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="OphthalmicAxialMeasurementsRightEyeSequence"	Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="OphthalmicAxialMeasurementsMacro"
		InvokeMacro="OphthalmicAxialMeasurementsSelectedMacro"
	SequenceEnd
	Sequence="OphthalmicAxialMeasurementsLeftEyeSequence"	Type="1C"	VM="1"	NoCondition=""
		InvokeMacro="OphthalmicAxialMeasurementsMacro"
		InvokeMacro="OphthalmicAxialMeasurementsSelectedMacro"
	SequenceEnd
ModuleEnd

DefineMacro="OphthalmicAxialMeasurementsMacro"
	Sequence="LensStatusCodeSequence"												Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"																		DefinedContextID="4231"
	SequenceEnd
	Name="LensStatusDescription"													Type="3"
	Sequence="VitreousStatusCodeSequence"											Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"																		DefinedContextID="4232"
	SequenceEnd
	Name="VitreousStatusDescription"												Type="3"
	Name="PupilDilated"																Type="2"				StringEnumValues="YesNoFull"
	Name="DegreeOfDilation"															Type="2C"				Condition="PupilDilatedIsYes"
	Sequence="MydriaticAgentSequence"												Type="2C"	VM="0-n"	Condition="PupilDilatedIsYes"
		Sequence="MydriaticAgentCodeSequence"										Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"																	DefinedContextID="4208"
		SequenceEnd
		Name="MydriaticAgentConcentration"											Type="3"
		Sequence="MydriaticAgentConcentrationUnitsSequence"							Type="1C"	VM="1"		Condition="MydriaticAgentConcentrationPresent"
			InvokeMacro="CodeSequenceMacro"																	DefinedContextID="4244"
		SequenceEnd
	SequenceEnd
	Sequence="OphthalmicAxialLengthMeasurementsSequence"							Type="1"	VM="1-n"
		Name="OphthalmicAxialLengthMeasurementsType"								Type="1"				StringEnumValues="OphthalmicAxialLengthMeasurementsType"
		Sequence="OphthalmicAxialLengthMeasurementsTotalLengthSequence"				Type="1C"	VM="1-n"	Condition="OphthalmicAxialLengthMeasurementsTypeIsTotalLength"
			Name="OphthalmicAxialLength"											Type="1"
			Name="OphthalmicAxialLengthMeasurementModified"							Type="1"				StringEnumValues="YesNoFull"
			Sequence="ReferencedOphthalmicAxialLengthMeasurementQCImageSequence"	Type="1"	VM="1"
				InvokeMacro="OphthalmicAxialMeasurementsQualityImageSOPInstanceReferenceMacro"
			SequenceEnd
			InvokeMacro="OphthalmicAxialMeasurementsRelatedInformationMacro"
		SequenceEnd
		Sequence="OphthalmicAxialLengthMeasurementsLengthSummationSequence"			Type="1C"	VM="1-n"	Condition="OphthalmicAxialLengthMeasurementsTypeIsLengthSummation"
			Name="OphthalmicAxialLength"											Type="1"
			Name="OphthalmicAxialLengthMeasurementModified"							Type="1"				StringEnumValues="YesNoFull"
			Sequence="ReferencedOphthalmicAxialLengthMeasurementQCImageSequence"	Type="1"	VM="1"
				InvokeMacro="OphthalmicAxialMeasurementsQualityImageSOPInstanceReferenceMacro"
			SequenceEnd
			Sequence="OphthalmicAxialLengthMeasurementsSegmentalLengthSequence"		Type="1"	VM="1-n"
				InvokeMacro="OphthalmicAxialLengthSegmentalMeasurementsMacro"
			SequenceEnd
		SequenceEnd
		Sequence="OphthalmicAxialLengthMeasurementsSegmentalLengthSequence"			Type="1C"	VM="1-n"	Condition="OphthalmicAxialLengthMeasurementsTypeIsSegmentalLength"
			InvokeMacro="OphthalmicAxialLengthSegmentalMeasurementsMacro"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="OphthalmicAxialLengthSegmentalMeasurementsMacro"
	Name="OphthalmicAxialLength"										Type="1"
	Name="OphthalmicAxialLengthMeasurementModified"						Type="1"				StringEnumValues="YesNoFull"
	Sequence="OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence"	Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	InvokeMacro="OphthalmicAxialMeasurementsRelatedInformationMacro"
MacroEnd

DefineMacro="OphthalmicAxialMeasurementsRelatedInformationMacro"
	Sequence="UltrasoundOphthalmicAxialLengthMeasurementsSequence"		Type="1C"	VM="1"		Condition="OphthalmicAxialMeasurementsDeviceTypeIsUltrasound"
		Name="OphthalmicAxialLengthVelocity"							Type="1"
		Name="ObserverType"												Type="1"				StringEnumValues="OphthalmicAxialMeasurementsObserverType"
		Sequence="OphthalmicAxialLengthDataSourceCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"														DefinedContextID="4240"
		SequenceEnd
		Name="OphthalmicAxialLengthDataSourceDescription"				Type="3"
	SequenceEnd
	Sequence="OpticalOphthalmicAxialLengthMeasurementsSequence"			Type="1C"	VM="1"		Condition="OphthalmicAxialMeasurementsDeviceTypeIsOptical"
		Name="SignalToNoiseRatio"										Type="3"
		Sequence="OphthalmicAxialLengthDataSourceCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"														DefinedContextID="4240"
		SequenceEnd
		Name="OphthalmicAxialLengthDataSourceDescription"				Type="3"
	SequenceEnd
MacroEnd

DefineMacro="OphthalmicAxialMeasurementsSelectedMacro"
	Sequence="UltrasoundSelectedOphthalmicAxialLengthSequence"						Type="1C"	VM="1"		Condition="OphthalmicAxialMeasurementsDeviceTypeIsUltrasound"
		Name="OphthalmicAxialLength"												Type="1"
		Sequence="OphthalmicAxialLengthSelectionMethodCodeSequence"					Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"																	DefinedContextID="4241"
		SequenceEnd
		Sequence="ReferencedOphthalmicAxialLengthMeasurementQCImageSequence"		Type="1"	VM="1"
			InvokeMacro="OphthalmicAxialMeasurementsQualityImageSOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="OphthalmicAxialLengthQualityMetricSequence"						Type="1"	VM="1"
			InvokeMacro="OphthalmicAxialLengthQualityMetricMacro"
		SequenceEnd
		Sequence="SelectedSegmentalOphthalmicAxialLengthSequence"					Type="1C"	VM="1"		Condition="OphthalmicAxialLengthMeasurementsTypeAboveIsLengthSummation"
			Name=OphthalmicAxialLength"												Type="1"
			Sequence="OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence"		Type="1"	VM="1"
				InvokeMacro="CodeSequenceMacro"																DefinedContextID="4233"
			SequenceEnd
		SequenceEnd
	SequenceEnd
	Sequence="OpticalSelectedOphthalmicAxialLengthSequence"							Type="1C"	VM="1-n"	Condition="OphthalmicAxialMeasurementsDeviceTypeIsOptical"
		Sequence="SelectedTotalOphthalmicAxialLengthSequence"						Type="1C"	VM="1"		Condition="OphthalmicAxialLengthMeasurementsTypeAboveIsTotalLength"
			Name="OphthalmicAxialLength"											Type="1"
			Sequence="ReferencedOphthalmicAxialLengthMeasurementQCImageSequence"	Type="1"	VM="1"
				InvokeMacro="OphthalmicAxialMeasurementsQualityImageSOPInstanceReferenceMacro"
			SequenceEnd
			Sequence="OphthalmicAxialLengthQualityMetricSequence"					Type="1"	VM="1"
				InvokeMacro="OphthalmicAxialLengthQualityMetricMacro"
			SequenceEnd
		SequenceEnd
		Sequence="SelectedSegmentalOphthalmicAxialLengthSequence"					Type="1C"	VM="1-n"	Condition="OphthalmicAxialLengthMeasurementsTypeAboveIsSegmentalLength"
			Sequence="OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence"		Type="1"	VM="1"
				InvokeMacro="CodeSequenceMacro"																DefinedContextID="4233"
			SequenceEnd
			Name="OphthalmicAxialLength"											Type="1"
			Sequence="ReferencedOphthalmicAxialLengthMeasurementQCImageSequence"	Type="3"	VM="1"
				InvokeMacro="OphthalmicAxialMeasurementsQualityImageSOPInstanceReferenceMacro"
			SequenceEnd
			Sequence="OphthalmicAxialLengthQualityMetricSequence"					Type="3"	VM="1"
				InvokeMacro="OphthalmicAxialLengthQualityMetricMacro"
			SequenceEnd
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="OphthalmicAxialLengthQualityMetricMacro"
	Sequence="ConceptNameCodeSequence"					Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"										DefinedContextID="4243"
	SequenceEnd
	Name="NumericValue"									Type="1"
	Sequence="MeasurementUnitsCodeSequence"				Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"										DefinedContextID="82"
	SequenceEnd
MacroEnd

Module="IntraocularLensCalculationsSeries"
	Name="Modality"										Type="1"			StringEnumValues="IntraocularLensCalculationsModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="IntraocularLensCalculations"
	Sequence="IntraocularLensCalculationsRightEyeSequence"	Type="1C"	VM="1-n"	NoCondition=""
		InvokeMacro="IntraocularLensCalculationsMacro"
	SequenceEnd
	Sequence="IntraocularLensCalculationsLeftEyeSequence"	Type="1C"	VM="1-n"	NoCondition=""
		InvokeMacro="IntraocularLensCalculationsMacro"
	SequenceEnd
ModuleEnd

DefineMacro="IntraocularLensCalculationsMacro"
	Name="TargetRefraction"											Type="1"
	Name="RefractiveProcedureOccurred"								Type="2"				StringEnumValues="YesNoFull"
	Sequence="RefractiveSurgeryTypeCodeSequence"					Type="2C"	VM="0-n"	Condition="RefractiveProcedureOccurredIsYes"
		InvokeMacro="CodeSequenceMacro"														DefinedContextID="4234"
	SequenceEnd
	Sequence="RefractiveErrorBeforeRefractiveSurgeryCodeSequence"	Type="2C"	VM="0-1"	Condition="RefractiveProcedureOccurredIsYes"
		InvokeMacro="CodeSequenceMacro"														DefinedContextID="4238"
	SequenceEnd
	Sequence="CornealSizeSequence"									Type="3"	VM="1"
		Name="CornealSize"											Type="1"
		Sequence="SourceOfCornealSizeDataCodeSequence"				Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"													DefinedContextID="4240"
		SequenceEnd
		Sequence="ReferencedSOPSequence"							Type="1C"	VM="1"		NoCondition="" # too hard to check that SourceOfLensThicknessDataCodeSequence contains (111784, DCM, "Autorefraction Measurements SOP Instance")
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="LensThicknessSequence"								Type="3"	VM="1"
		Name="LensThickness"										Type="1"
		Sequence="SourceOfLensThicknessDataCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"													DefinedContextID="4240"
		SequenceEnd
		Sequence="ReferencedSOPSequence"							Type="1C"	VM="1"		NoCondition="" # too hard to check that SourceOfLensThicknessDataCodeSequence contains (111782, DCM, "Axial Measurements SOP Instance")
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="AnteriorChamberDepthSequence"							Type="3"	VM="1"
		Name="AnteriorChamberDepth"	Type="1"
		Sequence="SourceOfAnteriorChamberDepthDataCodeSequence"		Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="ReferencedSOPSequence"							Type="1C"	VM="1"		NoCondition="" # too hard to check that SourceOfAnteriorChamberDepthDataCodeSequence contains (111782, DCM, "Axial Measurements SOP Instance")
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="RefractiveStateSequence"								Type="2"	VM="0-1"
		Name="SphericalLensPower"									Type="1"
		Name="CylinderLensPower"									Type="1"
		Name="CylinderAxis"											Type="1"
		Sequence="SourceOfRefractiveMeasurementsSequence"			Type="1"	VM="1"
			Sequence="SourceOfRefractiveMeasurementsCodeSequence"	Type="1"	VM="1"
				InvokeMacro="CodeSequenceMacro"												DefinedContextID="4240"
			SequenceEnd
			Sequence="ReferencedSOPSequence"						Type="1C"	VM="1"		NoCondition="" # too hard to check that SourceOfRefractiveMeasurementsCodeSequence contains (111783, DCM, "Refractive Measurements SOP Instance")
				InvokeMacro="SOPInstanceReferenceMacro"
			SequenceEnd
		SequenceEnd
	SequenceEnd
	InvokeMacro="KeratometryMacro"
	Sequence="IOLFormulaCodeSequence"								Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"														DefinedContextID="4236"
	SequenceEnd
	Name="IOLFormulaDetail"											Type="3"
	InvokeMacro="IOLOphthalmicAxialLengthMacro"
	InvokeMacro="CalculatedIOLMacro"
MacroEnd

DefineMacro="KeratometryMacro"
	Sequence="SteepKeratometricAxisSequence"						Type="1"	VM="1"
		Name="RadiusOfCurvature"									Type="1"
		Name="KeratometricPower"									Type="2"
		Name="KeratometricAxis"										Type="2"
	SequenceEnd
	Sequence="FlatKeratometricAxisSequence"							Type="1"	VM="1"
		Name="RadiusOfCurvature"									Type="1"
		Name="KeratometricPower"									Type="2"
		Name="KeratometricAxis"										Type="2"
	SequenceEnd
	Sequence="KeratometryMeasurementTypeCodeSequence"				Type="2"	VM="1"
		InvokeMacro="CodeSequenceMacro"														DefinedContextID="4235"
	SequenceEnd
	Name="KeratometerIndex"											Type="2"
MacroEnd

DefineMacro="IOLOphthalmicAxialLengthMacro"
	Sequence="OphthalmicAxialLengthSequence"						Type="1"	VM="1"
		Name="OphthalmicAxialLength"								Type="1"
		Sequence="OphthalmicAxialLengthSelectionMethodCodeSequence"	Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"													DefinedContextID="4241"
		SequenceEnd
		Sequence="SourceOfOphthalmicAxialLengthCodeSequence"		Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"													DefinedContextID="4240"
		SequenceEnd
		Sequence="ReferencedSOPSequence"							Type="1C"	VM="1"		NoCondition="" # too hard to check that SourceOfOphthalmicAxialLengthCodeSequence contains (111782, DCM, "Axial Measurements SOP Instance")
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="OphthalmicUltrasoundMethodCodeSequence"			Type="1C"	VM="1"		Condition="OphthalmicAxialMeasurementsDeviceTypeIsUltrasound"
			InvokeMacro="CodeSequenceMacro"													DefinedContextID="4230"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="CalculatedIOLMacro"
	Name="IOLManufacturer"							Type="1"
	Name="ImplantName"								Type="1"
	Sequence="LensConstantSequence"					Type="1"	VM="1-n"
		Sequence="ConceptNameCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"									DefinedContextID="4237"
		SequenceEnd
		Name="NumericValue"	Type="1"
	SequenceEnd
	Sequence="IOLPowerSequence"						Type="1"	VM="1-n"
		Name="IOLPower"								Type="1"
		Name="PredictedRefractiveError"				Type="1"
		Name="ImplantPartNumber"					Type="2"
	SequenceEnd
	Name="IOLPowerForExactEmmetropia"				Type="2"
	Name="IOLPowerForExactTargetRefraction"			Type="2"
MacroEnd

DefineMacro="OphthalmicAxialMeasurementsQualityImageSOPInstanceReferenceMacro"
	Name="ReferencedSOPClassUID"	Type="1"	StringEnumValues="OphthalmicAxialMeasurementsQualityImageSOPClassUIDs"
	Name="ReferencedSOPInstanceUID"	Type="1"
	Name="ReferencedFrameNumber"	Type="1"
MacroEnd

Module="VisualFieldStaticPerimetryMeasurementsSeries"
	Name="Modality"										Type="1"	StringEnumValues="OphthalmicVisualFieldModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="RequestAttributesSequence"				Type="3"	VM="1-n"
		InvokeMacro="RequestAttributesMacro"
	SequenceEnd
	InvokeMacro="PerformedProcedureStepSummaryMacro"
ModuleEnd

Module="VisualFieldStaticPerimetryTestParameters"
	Name="VisualFieldHorizontalExtent"						Type="1"
	Name="VisualFieldVerticalExtent"						Type="1"
	Name="VisualFieldShape"									Type="1"	StringEnumValues="VisualFieldShape"
	Sequence="ScreeningTestModeCodeSequence"				Type="1C"	VM="1"	NoCondition="" mbpo="true"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="MaximumStimulusLuminance"							Type="1"
	Name="BackgroundLuminance"								Type="1"
	Sequence="StimulusColorCodeSequence"					Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="BackgroundIlluminationColorCodeSequence"		Type="1"	VM="1"
	InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="StimulusArea"										Type="1"
	Name="StimulusPresentationTime"							Type="1"
ModuleEnd

Module="VisualFieldStaticPerimetryTestReliability"
	Sequence="FixationSequence"									Type="1"	VM="1"
		Sequence="FixationMonitoringCodeSequence"				Type="1"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="FixationCheckedQuantity"							Type="1C"	NoCondition="" mbpo="true"
		Name="PatientNotProperlyFixatedQuantity"				Type="1C"	NoCondition="" mbpo="true"
		Name="ExcessiveFixationLossesDataFlag"					Type="1"	StringEnumValues="YesNoFull"
		Name="ExcessiveFixationLosses"							Type="1C"	Condition="ExcessiveFixationLossesDataFlagIsYes"
	SequenceEnd
	Sequence="VisualFieldCatchTrialSequence"					Type="1"	VM="1"
		Name="CatchTrialsDataFlag"								Type="1"	StringEnumValues="YesNoFull"
		Name="NegativeCatchTrialsQuantity"						Type="1C"	Condition="CatchTrialsDataFlagIsYes"
		Name="FalseNegativesQuantity"							Type="1C"	Condition="CatchTrialsDataFlagIsYes"
		Name="FalseNegativesEstimateFlag"						Type="1"	StringEnumValues="YesNoFull"
		Name="FalseNegativesEstimate"							Type="1C"	Condition="FalseNegativesEstimateFlagIsYes"
		Name="ExcessiveFalseNegativesDataFlag"					Type="1"	StringEnumValues="YesNoFull"
		Name="ExcessiveFalseNegatives"							Type="1C"	StringEnumValues="YesNoFull" Condition="ExcessiveFalseNegativesDataFlagIsYes"
		Name="PositiveCatchTrialsQuantity"						Type="1C"	Condition="CatchTrialsDataFlagIsYes"
		Name="FalsePositivesQuantity"							Type="1C"	Condition="CatchTrialsDataFlagIsYes"
		Name="FalsePositivesEstimateFlag"						Type="1"	StringEnumValues="YesNoFull"
		Name="FalsePositivesEstimate"							Type="1C"	Condition="FalsePositivesEstimateFlagIsYes"
		Name="ExcessiveFalsePositivesDataFlag"					Type="1"	StringEnumValues="YesNoFull"
		Name="ExcessiveFalsePositives"							Type="1C"	StringEnumValues="YesNoFull" Condition="ExcessiveFalsePositivesDataFlagIsYes"
	SequenceEnd
	Name="StimuliRetestingQuantity"								Type="3"
	Name="PatientReliabilityIndicator"							Type="3"
	Name="CommentsOnPatientPerformanceOfVisualField"			Type="3"
	Sequence="VisualFieldTestReliabilityGlobalIndexSequence"	Type="3"	VM="1-n"
		InvokeMacro="OphthalmicVisualFieldGlobalIndexMacro"
	SequenceEnd
ModuleEnd

DefineMacro="OphthalmicVisualFieldGlobalIndexMacro"
	Sequence="DataObservationSequence"						Type="1"	VM="1"
		InvokeMacro="ContentItemMacro"
	SequenceEnd
	Name="IndexNormalsFlag"									Type="1"	StringEnumValues="YesNoFull"
	Sequence="IndexProbabilitySequence"						Type="1C"	VM="1" Condition="IndexNormalsFlagIsYes"
		Name="IndexProbability"								Type="1"
		InvokeMacro="AlgorithmIdentificationMacro"
	SequenceEnd
MacroEnd

Module="VisualFieldStaticPerimetryTestMeasurements"
	Name="MeasurementLaterality"											Type="1"	StringEnumValues="VisualFieldStaticPerimetryTestMeasurementLaterality"
	Name="PresentedVisualStimuliDataFlag"									Type="1"	StringEnumValues="YesNoFull"
	Name="NumberOfVisualStimuli"											Type="1C"	Condition="PresentedVisualStimuliDataFlagIsYes"
	Name="VisualFieldTestDuration"											Type="1"
	Name="FovealSensitivityMeasured"										Type="1"	StringEnumValues="YesNoFull"
	Name="FovealSensitivity"												Type="1C"	Condition="FovealSensitivityMeasuredIsYes"
	Name="FovealPointNormativeDataFlag"										Type="1"	StringEnumValues="YesNoFull"
	Name="FovealPointProbabilityValue"										Type="1C"	Condition="FovealPointNormativeDataFlagIsYes"
	Name="ScreeningBaselineMeasured"										Type="1"	StringEnumValues="YesNoFull"
	Sequence="ScreeningBaselineMeasuredSequence"							Type="1C"	VM="1-n"	Condition="ScreeningBaselineMeasuredIsYes"
		Name="ScreeningBaselineType"										Type="1"	StringEnumValues="VisualFieldStaticPerimetryTestMeasurementsScreeningBaselineType"
		Name="ScreeningBaselineValue"										Type="1"
	SequenceEnd
	Name="BlindSpotLocalized"												Type="1"	StringEnumValues="YesNoFull"
	Name="BlindSpotXCoordinate"												Type="1C"	Condition="BlindSpotLocalizedIsYes"
	Name="BlindSpotYCoordinate"												Type="1C"	Condition="BlindSpotLocalizedIsYes"
	Name="MinimumSensitivityValue"											Type="1"
	Name="TestPointNormalsDataFlag"											Type="1"	StringEnumValues="YesNoFull"
	Sequence="TestPointNormalsSequence"										Type="1C"	VM="1" Condition="TestPointNormalsDataFlagIsYes"
		InvokeMacro="DataSetIdentificationMacro"
	SequenceEnd
	Sequence="AgeCorrectedSensitivityDeviationAlgorithmSequence"			Type="1C"	VM="1" Condition="TestPointNormalsDataFlagIsYes"
		InvokeMacro="AlgorithmIdentificationMacro"
	SequenceEnd
	Sequence="GeneralizedDefectSensitivityDeviationAlgorithmSequence"		Type="1C"	VM="1" Condition="TestPointNormalsDataFlagIsYes"
		InvokeMacro="AlgorithmIdentificationMacro"
	SequenceEnd
	Sequence="VisualFieldTestPointSequence"									Type="1"	VM="1-n"
		Name="VisualFieldTestPointXCoordinate"								Type="1"
		Name="VisualFieldTestPointYCoordinate"								Type="1"
		Name="StimulusResults"												Type="1"	StringEnumValues="VisualFieldStaticPerimetryTestMeasurementsStimulusResults"
		Name="SensitivityValue"												Type="1C"	NoCondition="" mbpo="true""
		Name="RetestStimulusSeen"											Type="3"	StringEnumValues="YesNoFull"
		Name="RetestSensitivityValue"										Type="3"
		Name="QuantifiedDefect"												Type="3"
		Sequence="VisualFieldTestPointNormalsSequence"								Type="1C"	VM="1-n" Condition="TestPointNormalsDataFlagIsYes"
			Name="AgeCorrectedSensitivityDeviationValue"							Type="1"
			Name="AgeCorrectedSensitivityDeviationProbabilityValue"					Type="1"
			Name="GeneralizedDefectCorrectedSensitivityDeviationFlag"				Type="1"	StringEnumValues="YesNoFull"
			Name="GeneralizedDefectCorrectedSensitivityDeviationValue"				Type="1C"	Condition="GeneralizedDefectCorrectedSensitivityDeviationFlagIsYes"
			Name="GeneralizedDefectCorrectedSensitivityDeviationProbabilityValue"	Type="1C"	Condition="GeneralizedDefectCorrectedSensitivityDeviationFlagIsYes"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="VisualFieldStaticPerimetryTestResults"
	Name="VisualFieldMeanSensitivity"									Type="1C"	NoCondition="" mbpo="true"
	Name="VisualFieldTestNormalsFlag"									Type="1"	StringEnumValues="YesNoFull"
	Sequence="ResultsNormalsSequence"									Type="1C"	VM="1"	Condition="VisualFieldTestNormalsFlagIsYes"
		InvokeMacro="DataSetIdentificationMacro"
		Name="GlobalDeviationFromNormal"								Type="1"
		Name="GlobalDeviationProbabilityNormalsFlag"					Type="1"	StringEnumValues="YesNoFull"
		Sequence="GlobalDeviationProbabilitySequence"					Type="1C"	VM="1"	Condition="GlobalDeviationProbabilityNormalsFlagIsYes"
			Name="GlobalDeviationProbability"							Type="1"
			InvokeMacro="AlgorithmIdentificationMacro"
		SequenceEnd
		Name="LocalizedDeviationFromNormal"								Type="1"
		Name="LocalDeviationProbabilityNormalsFlag"						Type="1"	StringEnumValues="YesNoFull"
		Sequence="LocalizedDeviationProbabilitySequence"				Type="1C"	VM="1"	Condition="LocalDeviationProbabilityNormalsFlagIsYes"
			Name="LocalizedDeviationProbability"						Type="1"
			InvokeMacro="AlgorithmIdentificationMacro"
		SequenceEnd
	SequenceEnd
	Name="ShortTermFluctuationCalculated"								Type="1"	StringEnumValues="YesNoFull"
	Name="ShortTermFluctuation"											Type="1C"	Condition="ShortTermFluctuationCalculatedIsYes"
	Name="ShortTermFluctuationProbabilityCalculated"					Type="1"	StringEnumValues="YesNoFull"
	Name="ShortTermFluctuationProbability"								Type="1C"	Condition="ShortTermFluctuationProbabilityCalculatedIsYes"
	Name="CorrectedLocalizedDeviationFromNormalCalculated"				Type="1"	StringEnumValues="YesNoFull"
	Name="CorrectedLocalizedDeviationFromNormal"						Type="1C"	Condition="CorrectedLocalizedDeviationFromNormalCalculatedIsYes"
	Name="CorrectedLocalizedDeviationFromNormalProbabilityCalculated"	Type="1"	StringEnumValues="YesNoFull"
	Name="CorrectedLocalizedDeviationFromNormalProbability"				Type="1C"	Condition="CorrectedLocalizedDeviationFromNormalProbabilityCalculatedIsYes"
	Sequence="VisualFieldGlobalResultsIndexSequence"					Type="3"	VM="1-n"
		InvokeMacro="OphthalmicVisualFieldGlobalIndexMacro"
	SequenceEnd
ModuleEnd

Module="OphthalmicPatientClinicalInformationandTestLensParameters"
	Sequence="OphthalmicPatientClinicalInformationLeftEyeSequence"	Type="1C"	VM="1"	Condition="MeasurementLateralityLeftOrBoth"
		InvokeMacro="OphthalmicPatientClinicalInformationandTestLensParametersMacro"
	SequenceEnd
	Sequence="OphthalmicPatientClinicalInformationRightEyeSequence"	Type="1C"	VM="1"	Condition="MeasurementLateralityRightOrBoth"
		InvokeMacro="OphthalmicPatientClinicalInformationandTestLensParametersMacro"
	SequenceEnd
ModuleEnd

DefineMacro="OphthalmicPatientClinicalInformationandTestLensParametersMacro"
	Sequence="RefractiveParametersUsedOnPatientSequence"	Type="2"	VM="0-1"
		Name="SphericalLensPower"							Type="1"
		Name="CylinderLensPower"							Type="1"
		Name="CylinderAxis"									Type="1"
	SequenceEnd
	Name="PupilSize"										Type="2"
	Name="PupilDilated"										Type="2"	StringEnumValues="YesNoFull"
	Name="IntraOcularPressure"								Type="3"
	Sequence="VisualAcuityMeasurementSequence"				Type="3"	VM="1"
		InvokeMacro="VisualAcuityMeasurementsMacro"
	SequenceEnd
MacroEnd
Module="Synchronization"
	Name="SynchronizationFrameOfReferenceUID"		Type="1"
	Name="SynchronizationTrigger"					Type="1"	StringEnumValues="SynchronizationTrigger"
	Name="TriggerSourceOrType"						Type="3"
	Name="SynchronizationChannel"					Type="1C"	NoCondition=""	# real world
	Name="AcquisitionTimeSynchronized"				Type="1"	StringEnumValues="YesNoLetter"
	Name="TimeSource"								Type="3"
	Name="TimeDistributionProtocol"					Type="3"	StringEnumValues="TimeDistributionProtocol"
	Name="NTPSourceAddress"							Type="3"
ModuleEnd

Module="WaveformIdentification"
	Name="InstanceNumber"							Type="1"
	Name="ContentDate"								Type="1"
	Name="ContentTime"								Type="1"
	Name="AcquisitionDateTime"						Type="1"
	Sequence="ReferencedInstanceSequence"			Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"	Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="Waveform"
	Sequence="WaveformSequence"							Type="1"	VM="1-n"
		Name="MultiplexGroupTimeOffset"					Type="1C"	Condition="AcquisitionTimeSynchronizedIsY"
		Name="TriggerTimeOffset"						Type="1C"	NoCondition=""	# real world
		Name="TriggerSamplePosition"					Type="3"
		Name="WaveformOriginality"						Type="1"	StringEnumValues="WaveformOriginality"
		Name="NumberOfWaveformChannels"					Type="1"	NotZeroError=""
		Name="NumberOfWaveformSamples"					Type="1"	NotZeroError=""
		Name="SamplingFrequency"						Type="1"
		Name="MultiplexGroupLabel"						Type="3"
		Sequence="ChannelDefinitionSequence"			Type="1"	VM="1-n"
			Name="WaveformChannelNumber"				Type="3"
			Name="ChannelLabel"							Type="3"
			Name="ChannelStatus"						Type="3"	StringDefinedTerms="ChannelStatus"
			Sequence="ChannelSourceSequence"			Type="1"	VM="1"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Sequence="ChannelSourceModifiersSequence"	Type="1C"	VM="1-n"	NoCondition=""
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Sequence="SourceWaveformSequence"			Type="3"	VM="1-n"
				InvokeMacro="SOPInstanceReferenceMacro"
				Name="ReferencedWaveformChannels"		Type="1"
			SequenceEnd
			Name="ChannelDerivationDescription"			Type="3"
			Name="ChannelSensitivity"					Type="1C"	NoCondition=""	# real world
			Sequence="ChannelSensitivityUnitsSequence"	Type="1C"	VM="1"	Condition="ChannelSensitivityIsPresent"
				InvokeMacro="CodeSequenceMacro"						DefinedContextID="3082"
			SequenceEnd
			Name="ChannelSensitivityCorrectionFactor"	Type="1C"	Condition="ChannelSensitivityIsPresent"
			Name="ChannelBaseline"						Type="1C"	Condition="ChannelSensitivityIsPresent"
			Name="ChannelTimeSkew"						Type="1C"	Condition="ChannelSampleSkewNotPresent"
			Name="ChannelSampleSkew"					Type="1C"	Condition="ChannelTimeSkewNotPresent"
			Name="ChannelOffset"						Type="3"
			Name="WaveformBitsStored"					Type="1"
			Name="FilterLowFrequency"					Type="3"
			Name="FilterHighFrequency"					Type="3"
			Name="NotchFilterFrequency"					Type="3"
			Name="NotchFilterBandwidth"					Type="3"
			Name="ChannelMinimumValue"					Type="3"
			Name="ChannelMaximumValue"					Type="3"
		SequenceEnd
		Name="WaveformBitsAllocated"					Type="1"	BinaryEnumValues="BitsAre8Or16"
		Verify="WaveformBitsAllocated"								Condition="WaveformSampleInterpretationNeeds8Bit" BinaryEnumValues="BitsAre8"
		Verify="WaveformBitsAllocated"								Condition="WaveformSampleInterpretationNeeds16Bit" BinaryEnumValues="BitsAre16"
		Name="WaveformSampleInterpretation"				Type="1"	StringEnumValues="WaveformSampleInterpretation"	
		Name="WaveformPaddingValue"						Type="1C"	NoCondition=""	# real world
		Name="WaveformData"								Type="1"
		Name="WaveformDataDisplayScale"						Type="3"	NotZeroError=""
		Name="WaveformDisplayBackgroundCIELabValue"			Type="3"
		Sequence="WaveformPresentationGroupSequence"		Type="3"	VM="1-n"
			Name="PresentationGroupNumber"					Type="1"
			Sequence="ChannelDisplaySequence"				Type="1"	VM="1-n"
				Name="ReferencedWaveformChannels"			Type="1"
				Name="ChannelOffset"						Type="3"
				Name="ChannelRecommendedDisplayCIELabValue"	Type="1"
				Name="ChannelPosition"						Type="1"
				Name="DisplayShadingFlag"					Type="3"	StringEnumValues="DisplayShadingFlag"
				Name="FractionalChannelDisplayScale"		Type="1C"	Condition="AbsoluteChannelDisplayScaleIsNotPresent"
				Name="AbsoluteChannelDisplayScale"			Type="1C"	Condition="FractionalChannelDisplayScaleIsNotPresent"
			SequenceEnd
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="WaveformAnnotation"
	Sequence="WaveformAnnotationSequence"				Type="1"	VM="1-n"
		Name="UnformattedTextValue"						Type="1C"	Condition="ConceptNameCodeSequenceNotPresent"
		Sequence="ConceptNameCodeSequence"				Type="1C"	VM="1"	Condition="UnformattedTextValueNotPresent"
			InvokeMacro="CodeSequenceMacro"
			Sequence="ModifierCodeSequence"				Type="1C"	VM="1-n"	NoCondition=""	# real world
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
		SequenceEnd
		Sequence="ConceptCodeSequence"					Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
			Sequence="ModifierCodeSequence"				Type="1C"	VM="1-n"	NoCondition=""	# real world
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
		SequenceEnd
		Name="NumericValue"								Type="3"
		Sequence="MeasurementUnitsCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"							BaselineContextID="82"
		SequenceEnd
		Name="ReferencedWaveformChannels"				Type="1"
		Name="TemporalRangeType"						Type="1C"	NoCondition=""	StringEnumValues="TemporalRangeTypeForWaveformAnnotation""
		Name="ReferencedSamplePositions"				Type="1C"	Condition="AnnotationNeedsReferencedSamplePositions"
		Name="ReferencedTimeOffsets"					Type="1C"	Condition="AnnotationNeedsReferencedTimeOffsets"
		Name="ReferencedDateTime"						Type="1C"	Condition="AnnotationNeedsReferencedDateTime"
		Name="AnnotationGroupNumber"					Type="3"
	SequenceEnd
ModuleEnd

DefineMacro="HierarchicalSOPInstanceReferenceMacro"
	Name="StudyInstanceUID"									Type="1"
	Sequence="ReferencedSeriesSequence"						Type="1"	VM="1-n"
		InvokeMacro="HierarchicalSeriesReferenceMacro"
	SequenceEnd
MacroEnd

DefineMacro="HierarchicalSOPInstanceReferenceIHEXDSIManifestProfileMacro"
	Name="StudyInstanceUID"									Type="1"
	Sequence="ReferencedSeriesSequence"						Type="1"	VM="1-n"
		InvokeMacro="HierarchicalSeriesReferenceIHEXDSIManifestProfileMacro"
	SequenceEnd
MacroEnd

DefineMacro="HierarchicalSeriesReferenceMacro"
	Name="SeriesInstanceUID"							Type="1"
	Name="RetrieveAETitle"								Type="3"
	Name="RetrieveLocationUID"							Type="3"
	Name="StorageMediaFileSetID"						Type="3"
	Name="StorageMediaFileSetUID"						Type="3"
	Sequence="ReferencedSOPSequence"					Type="1"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"		Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="ReferencedDigitalSignatureSequence"	Type="3"	VM="1-n"
			Name="DigitalSignatureUID"					Type="1"
			Name="Signature"							Type="1"
		SequenceEnd
		Sequence="ReferencedSOPInstanceMACSequence"		Type="3"	VM="1"
			Name="MACCalculationTransferSyntaxUID"		Type="1"
			Name="MACAlgorithm"							Type="1"	StringDefinedTerms="MACAlgorithm"
			Name="DataElementsSigned"					Type="1"
			Name="MAC"									Type="1"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="HierarchicalSeriesReferenceIHEXDSIManifestProfileMacro"
	Name="SeriesInstanceUID"							Type="1"
	Name="RetrieveAETitle"								Type="1"
	Name="RetrieveLocationUID"							Type="1"
	Name="StorageMediaFileSetID"						Type="3"
	Name="StorageMediaFileSetUID"						Type="3"
	Sequence="ReferencedSOPSequence"					Type="1"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"		Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="ReferencedDigitalSignatureSequence"	Type="3"	VM="1-n"
			Name="DigitalSignatureUID"					Type="1"
			Name="Signature"							Type="1"
		SequenceEnd
		Sequence="ReferencedSOPInstanceMACSequence"		Type="3"	VM="1"
			Name="MACCalculationTransferSyntaxUID"		Type="1"
			Name="MACAlgorithm"							Type="1"	StringDefinedTerms="MACAlgorithm"
			Name="DataElementsSigned"					Type="1"
			Name="MAC"									Type="1"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="IdentifiedPersonOrDeviceMacro"
	Name="ObserverType"										Type="1"	StringEnumValues="ObserverType"
	Name="PersonName"										Type="1C"	Condition="ObserverTypeIsPerson"
	Sequence="PersonIdentificationCodeSequence"				Type="2C"	VM="0-1"	Condition="ObserverTypeIsPerson"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="StationName"										Type="2C"	Condition="ObserverTypeIsDevice"
	Name="DeviceUID"										Type="1C"	Condition="ObserverTypeIsDevice"
	Name="Manufacturer"										Type="1C"	Condition="ObserverTypeIsDevice"
	Name="ManufacturerModelName"							Type="1C"	Condition="ObserverTypeIsDevice"
	Name="StationAETitle"									Type="3"
	Name="InstitutionName"									Type="2"
	Sequence="InstitutionCodeSequence"						Type="2"	VM="0-1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="InstitutionalDepartmentName"						Type="3"
	Sequence="InstitutionalDepartmentTypeCodeSequence"		Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"									BaselineContextID="7030"
	SequenceEnd
MacroEnd

DefineMacro="NumericMeasurementMacro"
	Sequence="MeasuredValueSequence"						Type="2"	VM="0-1"
		Name="NumericValue"									Type="1"
		Name="FloatingPointValue"							Type="1C"	NoCondition=""
		Name="RationalNumeratorValue"						Type="1C"	NoCondition=""
		Name="RationalDenominatorValue"						Type="1C"	Condition="RationalNumeratorValueIsPresent" NotZeroError=""
		Sequence="MeasurementUnitsCodeSequence"				Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"								DefinedContextID="82"
		SequenceEnd
	SequenceEnd
	Sequence="NumericValueQualifierCodeSequence"			Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"									DefinedContextID="42"
	SequenceEnd
MacroEnd

DefineMacro="CodeMacro"
	Sequence="ConceptCodeSequence"							Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
MacroEnd

DefineMacro="CompositeObjectReferenceMacro"
	Sequence="ReferencedSOPSequence"								Type="1"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
MacroEnd

DefineMacro="ImageReferenceMacro"
	Sequence="ReferencedSOPSequence"								Type="1"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
		Name="ReferencedFrameNumber"								Type="1C"	NoCondition=""	NotZeroError=""	# cannot just check SOP Class and mbpo false, since may be absent for multi-frame if applies to all frames (including multi-frame SOP Class with only 1 frame) :(
		Verify="ReferencedFrameNumber"											Condition="ReferencedFrameNumberPresentAndReferencedSOPClassUIDIsNotMultiFrame"	ThenErrorMessage="May not be present for Referenced SOP Class that is not multi-frame"
		Name="ReferencedSegmentNumber"								Type="1C"	NoCondition=""	NotZeroError=""	# cannot just check SOP Class and mbpo false, since may be absent for segmentation if applies to all segments :(
		Verify="ReferencedSegmentNumber"										Condition="ReferencedSegmentNumberPresentAndReferencedSOPClassUIDIsNotSegmentationOrSurfaceSegmentation"	ThenErrorMessage="May not be present for Referenced SOP Class that is not segmentation"
		Verify="ReferencedSegmentNumber"										Condition="ReferencedFrameNumberAndReferencedSegmentNumberPresent"	ThenErrorMessage="May not be present when ReferencedFrameNumber is present"
		Sequence="ReferencedSOPSequence"							Type="3"	VM="1"	# presentation states
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="ReferencedRealWorldValueMappingInstanceSequence"	Type="3"	VM="1"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="IconImageSequence"								Type="3"	VM="1"
			InvokeMacro="IconImageSequenceMacro"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="WaveformReferenceMacro"
	Sequence="ReferencedSOPSequence"								Type="1"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
		Name="ReferencedWaveformChannels"							Type="1C"	NoCondition=""  # too hard for multi-channel :(
	SequenceEnd
MacroEnd

DefineMacro="SpatialCoordinatesMacro"
	Name="GraphicData"					Type="1"
	Verify="GraphicData"							VM="2"	Condition="GraphicTypeIsPOINT"
	Verify="GraphicData"							VM="4"	Condition="GraphicTypeIsCIRCLE"
	Verify="GraphicData"							VM="8"	Condition="GraphicTypeIsELLIPSE"
	Name="GraphicType"					Type="1"	StringEnumValues="SRGraphicType"
	Name="PixelOriginInterpretation"	Type="1C"	NoCondition=""	StringEnumValues="PixelOriginInterpretation"
	Name="FiducialUID"					Type="3"
MacroEnd

DefineMacro="SpatialCoordinates3DMacro"
	Name="ReferencedFrameOfReferenceUID"	Type="3"
	Name="GraphicData"						Type="1"
	Verify="GraphicData"								VM="3"	Condition="GraphicTypeIsPOINT"
	Verify="GraphicData"								VM="12"	Condition="GraphicTypeIsELLIPSE"
	Verify="GraphicData"								VM="18"	Condition="GraphicTypeIsELLIPSOID"
	Name="GraphicType"						Type="1"	StringEnumValues="SRGraphicType3D"
	Name="FiducialUID"						Type="3"
MacroEnd

DefineMacro="TemporalCoordinatesMacro"
	Name="TemporalRangeType"			Type="1"	StringEnumValues="TemporalRangeType"
	Name="ReferencedSamplePositions"	Type="1C"	Condition="NoReferencedDateTimeOrReferencedTimeOffsets"
	Name="ReferencedTimeOffsets"		Type="1C"	Condition="NoReferencedDateTimeOrReferencedSamplePositions"
	Name="ReferencedDateTime"			Type="1C"	Condition="NoReferencedTimeOffsetsOrReferencedSamplePositions"
MacroEnd

DefineMacro="ContainerMacro"
	Name="ContinuityOfContent"			Type="1"	StringEnumValues="ContinuityOfContent"
	Sequence="ContentTemplateSequence"	Type="1C"	VM="1"	NoCondition=""
		Name="MappingResource"			Type="1"	StringDefinedTerms="SRTemplateMappingResource"
		Name="MappingResourceUID"		Type="3"	StringDefinedTerms="MappingResourceUIDs"
		Name="TemplateIdentifier"		Type="1"
	SequenceEnd
MacroEnd

DefineMacro="DocumentContentMacro"
	Name="ValueType"								Type="1"	StringEnumValues="SRValueTypes"
	Verify="ValueType"											Condition="BasicTextSRStorageInstance"	StringEnumValues="BasicTextSRValueTypes"
	Verify="ValueType"											Condition="EnhancedSRStorageInstance"	StringEnumValues="EnhancedAndComprehensiveSRValueTypes"
	Verify="ValueType"											Condition="ComprehensiveSRStorageInstance"	StringEnumValues="EnhancedAndComprehensiveSRValueTypes"
	Verify="ValueType"											Condition="KeyObjectSelectionDocumentStorageInstance"	StringEnumValues="KeyObjectSelectionDocumentValueTypes"
	Verify="ValueType"											Condition="MammographyCADSRStorageInstance"	StringEnumValues="MammographyCADSRValueTypes"
	Verify="ValueType"											Condition="ChestCADSRStorageInstance"	StringEnumValues="ChestCADSRValueTypes"
	Verify="ValueType"											Condition="ProcedureLogStorageInstance"	StringEnumValues="ProcedureLogValueTypes"
	Verify="ValueType"											Condition="XRayRadiationDoseSRStorageInstance"	StringEnumValues="XRayRadiationDoseSRValueTypes"
	Sequence="ConceptNameCodeSequence"				Type="1C"	VM="1"	Condition="NeedConceptName"	mbpo="true"	# the mbpo is not correct but avoids incomplete condition issues
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="TextValue"								Type="1C"	Condition="ValueTypeIsText"
	Name="DateTime"									Type="1C"	Condition="ValueTypeIsDateTime"
	Name="Date"										Type="1C"	Condition="ValueTypeIsDate"
	Name="Time"										Type="1C"	Condition="ValueTypeIsTime"
	Name="PersonName"								Type="1C"	Condition="ValueTypeIsPersonName"
	Name="UID"										Type="1C"	Condition="ValueTypeIsUID"
	InvokeMacro="NumericMeasurementMacro"			Type="1C"	Condition="ValueTypeIsNum"
	InvokeMacro="CodeMacro"							Type="1C"	Condition="ValueTypeIsCode"
	InvokeMacro="CompositeObjectReferenceMacro"		Type="1C"	Condition="ValueTypeIsComposite"
	InvokeMacro="ImageReferenceMacro"				Type="1C"	Condition="ValueTypeIsImage"
	InvokeMacro="WaveformReferenceMacro"			Type="1C"	Condition="ValueTypeIsWaveform"
	InvokeMacro="SpatialCoordinatesMacro"			Type="1C"	Condition="ValueTypeIsSpatialCoordinates"
	InvokeMacro="SpatialCoordinates3DMacro"			Type="1C"	Condition="ValueTypeIsSpatialCoordinates3D"
	InvokeMacro="ContainerMacro"					Type="1C"	Condition="ValueTypeIsContainer"
MacroEnd

DefineMacro="DocumentRelationshipMacro"
	Name="ObservationDateTime"								Type="1C"	NoCondition=""	# Real world condition
	Name="ObservationUID"									Type="3"
	Sequence="ContentSequence"								Type="1C"	VM="1-n"	NoCondition=""  # whether or not leaf is real world
		Name="RelationshipType"								Type="1"	StringDefinedTerms="SRRelationshipType"
		InvokeMacro="DocumentRelationshipMacro"				Type="1C"	Condition="RelationshipByValue"
		InvokeMacro="DocumentContentMacro"					Type="1C"	Condition="RelationshipByValue"
		Name="ReferencedContentItemIdentifier"				Type="1C"	Condition="RelationshipByReference"	NotZeroError=""
	SequenceEnd
MacroEnd

Module="SRDocumentSeries"
	Name="Modality"										Type="1"	StringEnumValues="SRModality"
	Name="SeriesInstanceUID"							Type="1"
	Name="SeriesNumber"									Type="1"
	Name="SeriesDate"									Type="3"
	Name="SeriesTime"									Type="3"
	Name="ProtocolName"									Type="3"
	Name="SeriesDescription"							Type="3"
	Sequence="SeriesDescriptionCodeSequence"			Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="2"	VM="0-1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="SRDocumentGeneral"
	Name="InstanceNumber"											Type="1"
	Name="PreliminaryFlag"											Type="3"	StringEnumValues="PreliminaryFlag"
	Name="CompletionFlag"											Type="1"	StringEnumValues="CompletionFlag"
	Name="CompletionFlagDescription"								Type="3"
	Name="VerificationFlag"											Type="1"	StringEnumValues="VerificationFlag"
	Verify="VerificationFlag"													Condition="VerificationFlagIsVerifiedAndCompletionFlagIsNotComplete"	ThenErrorMessage="Only permitted to be VERIFIED if CompletionFlag is COMPLETE"
	Name="ContentDate"												Type="1"
	Name="ContentTime"												Type="1"
	Sequence="VerifyingObserverSequence"							Type="1C"	VM="1-n"	Condition="VerificationFlagIsVerified"
		Name="VerifyingObserverName"								Type="1"
		Sequence="VerifyingObserverIdentificationCodeSequence"		Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="VerifyingOrganization"								Type="1"
		Name="VerificationDateTime"									Type="1"
	SequenceEnd
	Sequence="AuthorObserverSequence"								Type="3"	VM="1-n"
		InvokeMacro="IdentifiedPersonOrDeviceMacro"
	SequenceEnd
	Sequence="ParticipantSequence"									Type="3"	VM="1-n"
		Name="ParticipationType"									Type="1"	StringDefinedTerms="ParticipationType"
		Name="ParticipationDateTime"								Type="2"
		InvokeMacro="IdentifiedPersonOrDeviceMacro"
	SequenceEnd
	Sequence="CustodialOrganizationSequence"						Type="3"	VM="1"
		Name="InstitutionName"										Type="2"
		Sequence="InstitutionCodeSequence"							Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="ResponsibleGroupCodeSequence"						Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"										BaselineContextID="7030"
		SequenceEnd
	SequenceEnd
	Sequence="PredecessorDocumentsSequence"							Type="1C"	VM="1-n"	NoCondition=""	# real world
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="IdenticalDocumentsSequence"							Type="1C"	VM="1-n"	NoCondition=""	# Real world condition
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedRequestSequence"							Type="1C"	VM="1-n"	NoCondition=""	# Real world condition
		Name="StudyInstanceUID"										Type="1"
		Sequence="ReferencedStudySequence"							Type="2"	VM="0-1"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Name="AccessionNumber"										Type="2"
		Sequence="IssuerOfAccessionNumberSequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="PlacerOrderNumberImagingServiceRequest"				Type="2"
		Sequence="OrderPlacerIdentifierSequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="FillerOrderNumberImagingServiceRequest"				Type="2"
		Sequence="OrderFillerIdentifierSequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="RequestedProcedureID"									Type="2"
		Name="RequestedProcedureDescription"						Type="2"
		Sequence="RequestedProcedureCodeSequence"					Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
 		Name="ReasonForTheRequestedProcedure"						Type="3"
		Sequence="ReasonForRequestedProcedureCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="PerformedProcedureCodeSequence"						Type="2"	VM="0-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="CurrentRequestedProcedureEvidenceSequence"			Type="1C"	VM="1-n"	NoCondition=""	# real world
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="PertinentOtherEvidenceSequence"						Type="1C"	VM="1-n"	NoCondition=""	# real world
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedInstanceSequence"							Type="1C"	VM="1"	NoCondition=""	# real world
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"					Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="SRDocumentContent"
	InvokeMacro="DocumentContentMacro"
	Verify="ConceptNameCodeSequence"								Condition="ConceptNameCodeSequenceNotPresent"	ThenErrorMessage="ConceptNameCodeSequence is required for root content item (in top level dataset)"
	InvokeMacro="DocumentRelationshipMacro"
ModuleEnd

Module="KeyObjectDocumentSeries"
	Name="Modality"										Type="1"	StringEnumValues="KOModality"
	Name="SeriesInstanceUID"							Type="1"
	Name="SeriesNumber"									Type="1"
	Name="SeriesDate"									Type="3"
	Name="SeriesTime"									Type="3"
	Name="ProtocolName"									Type="3"
	Name="SeriesDescription"							Type="3"
	Sequence="SeriesDescriptionCodeSequence"			Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="2"	VM="0-1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="KeyObjectDocument"
	Name="InstanceNumber"											Type="1"
	Name="ContentDate"												Type="1"
	Name="ContentTime"												Type="1"
	Sequence="ReferencedRequestSequence"							Type="1C"	VM="1-n"	NoCondition=""	# Real world condition
		Name="StudyInstanceUID"										Type="1"
		Sequence="ReferencedStudySequence"							Type="2"	VM="0-1"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Name="AccessionNumber"										Type="2"
		Sequence="IssuerOfAccessionNumberSequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="PlacerOrderNumberImagingServiceRequest"				Type="2"
		Sequence="OrderPlacerIdentifierSequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="FillerOrderNumberImagingServiceRequest"				Type="2"
		Sequence="OrderFillerIdentifierSequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="RequestedProcedureID"									Type="2"
		Name="RequestedProcedureDescription"						Type="2"
		Sequence="RequestedProcedureCodeSequence"					Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
 		Name="ReasonForTheRequestedProcedure"						Type="3"
		Sequence="ReasonForRequestedProcedureCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="CurrentRequestedProcedureEvidenceSequence"			Type="1"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="IdenticalDocumentsSequence"							Type="1C"	VM="1-n"	NoCondition=""	# real world
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="IHEXDSIManifestProfile"
	Sequence="CurrentRequestedProcedureEvidenceSequence"			Type="1"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceIHEXDSIManifestProfileMacro"
	SequenceEnd
ModuleEnd

Module="IHEREMProfile"
	Name="SeriesDescription"										Type="1"
	Sequence="ReferencedPerformedProcedureStepSequence"				Type="1"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="PerformedProcedureCodeSequence"						Type="1"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="ReferencedRequestSequence"							Type="1C"	VM="1-n"	NoCondition=""	# Real world condition
		Name="StudyInstanceUID"										Type="1"
		Sequence="ReferencedStudySequence"							Type="2"	VM="0-1"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Name="AccessionNumber"										Type="2"
		Sequence="IssuerOfAccessionNumberSequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="PlacerOrderNumberImagingServiceRequest"				Type="2"
		Sequence="OrderPlacerIdentifierSequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="FillerOrderNumberImagingServiceRequest"				Type="2"
		Sequence="OrderFillerIdentifierSequence"					Type="3"	VM="1"
			InvokeMacro="HL7v2HierarchicDesignatorMacro"
		SequenceEnd
		Name="RequestedProcedureID"									Type="2"
		Name="RequestedProcedureDescription"						Type="1"
		Sequence="RequestedProcedureCodeSequence"					Type="2"	VM="0-1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
 		Name="ReasonForTheRequestedProcedure"						Type="1"
		Sequence="ReasonForRequestedProcedureCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="AdmittingDiagnosesDescription"							Type="1"
	Sequence="AdmittingDiagnosesCodeSequence"						Type="1"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="PatientWeight"											Type="1"	NotZeroWarning=""
	Name="PatientSize"												Type="1"	NotZeroWarning=""
	Name="PatientAge"												Type="1"
	Name="PatientSex"												Type="1"
	
ModuleEnd
Module="BitmapDisplayShutter"
	Name="ShutterShape"							Type="1"	StringEnumValues="BitmapShutterShape"
	Name="ShutterOverlayGroup"					Type="1"	BinaryEnumValues="AllPossibleOverlayGroups"
	Name="ShutterPresentationValue"				Type="1"
	Name="ShutterPresentationColorCIELabValue"	Type="3"
ModuleEnd

Module="DisplayedArea"
	Sequence="DisplayedAreaSelectionSequence"		Type="1"	VM="1-n"
		Sequence="ReferencedImageSequence"			Type="1C"	VM="1-n"	NoCondition=""	# realworld
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
		Name="PixelOriginInterpretation"			Type="1C"	Condition="VLWholeSlideMicroscopyImageInstance"	mbpo="true"	StringEnumValues="PixelOriginInterpretation"
		Name="DisplayedAreaTopLeftHandCorner"		Type="1"
		Name="DisplayedAreaBottomRightHandCorner"	Type="1"
		Name="PresentationSizeMode"					Type="1"	StringEnumValues="PresentationSizeMode"
		Name="PresentationPixelSpacing"				Type="1C"	NotZeroError=""	Condition="RequirePresentationPixelSpacing"
		Name="PresentationPixelAspectRatio"			Type="1C"	NotZeroError=""	Condition="RequirePresentationPixelAspectRatio"
		Name="PresentationPixelMagnificationRatio"	Type="1C"	NotZeroError=""	Condition="RequirePresentationPixelMagnificationRatio"
	SequenceEnd
ModuleEnd

Module="GraphicAnnotation"
	Sequence="GraphicAnnotationSequence"					Type="1"	VM="1-n"
		Sequence="ReferencedImageSequence"					Type="1C"	VM="1-n"	NoCondition=""	# realworld
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
		Name="GraphicLayer"									Type="1"
		Sequence="TextObjectSequence"						Type="1C"	VM="1-n"	Condition="RequireTextObjectSequence"
			Name="BoundingBoxAnnotationUnits"				Type="1C"	Condition="BoundingBoxTopLeftHandCornerOrBottomRightHandCornerPresent"	StringEnumValues="AnnotationUnits"
			Name="AnchorPointAnnotationUnits"				Type="1C"	Condition="AnchorPointPresent"	StringEnumValues="AnnotationUnits"
			Name="UnformattedTextValue"						Type="1"
			Name="BoundingBoxTopLeftHandCorner"				Type="1C"	Condition="BoundingBoxNeeded"
			Name="BoundingBoxBottomRightHandCorner"			Type="1C"	Condition="BoundingBoxNeeded"
			Name="BoundingBoxTextHorizontalJustification"	Type="1C"	Condition="BoundingBoxTopLeftHandCornerPresent"	StringEnumValues="BoundingBoxTextHorizontalJustification"
			Name="AnchorPoint"								Type="1C"	Condition="AnchorPointNeeded" mbpo="true"
			Name="AnchorPointVisibility"					Type="1C"	Condition="AnchorPointPresent"	StringEnumValues="YesNoLetter"
			Name="TrackingID"								Type="1C"	Condition="TrackingUIDIsPresent"
			Name="TrackingUID"								Type="1C"	Condition="TrackingIDIsPresent"
		SequenceEnd
		Sequence="GraphicObjectSequence"					Type="1C"	VM="1-n"	Condition="RequireGraphicObjectSequence"
			Name="GraphicAnnotationUnits"					Type="1"	StringEnumValues="AnnotationUnits"
			Name="GraphicDimensions"						Type="1"	BinaryEnumValues="Two"
			Name="NumberOfGraphicPoints"					Type="1"	NotZeroError=""
			Name="GraphicData"								Type="1"
			Verify="GraphicData"										VM="2"	Condition="GraphicTypeIsPOINT"
			Verify="GraphicData"										VM="4"	Condition="GraphicTypeIsCIRCLE"
			Verify="GraphicData"										VM="8"	Condition="GraphicTypeIsELLIPSE"
			Name="GraphicType"								Type="1"	StringEnumValues="GraphicType"
			Name="GraphicFilled"							Type="1C"	NoCondition=""	StringEnumValues="YesNoLetter"	# very hard to check
			Name="TrackingID"								Type="1C"	Condition="TrackingUIDIsPresent"
			Name="TrackingUID"								Type="1C"	Condition="TrackingIDIsPresent"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="SpatialTransformation"
	Name="ImageRotation"					Type="1"	BinaryEnumValues="ImageRotationValues"
	Name="ImageHorizontalFlip"				Type="1"	StringEnumValues="YesNoLetter"
ModuleEnd

Module="GraphicLayer"
	Sequence="GraphicLayerSequence"							Type="1"	VM="1-n"
		Name="GraphicLayer"									Type="1"
		Name="GraphicLayerOrder"							Type="1"
		Name="GraphicLayerRecommendedDisplayGrayscaleValue"	Type="3"
		Name="GraphicLayerRecommendedDisplayCIELabValue"	Type="3"
		Name="GraphicLayerDescription"						Type="3"
	SequenceEnd

ModuleEnd

Module="SoftcopyPresentationLUT"
	Sequence="PresentationLUTSequence"			Type="1C"	VM="1"	Condition="PresentationLUTShapeNotPresent"
		Name="LUTDescriptor"					Type="1"
		Verify="LUTDescriptor"								ValueSelector="2"	BinaryEnumValues="BitsAre8To16"
		Name="LUTExplanation"					Type="3"
		Name="LUTData"							Type="1"
	SequenceEnd
	Name="PresentationLUTShape"					Type="1C"	Condition="PresentationLUTSequenceNotPresent"	StringEnumValues="SoftcopyPresentationLUTShape"
ModuleEnd

Module="OverlayActivation"
	Name="OverlayActivationLayer"				Type="2C"	NoCondition=""	# may require access to referenced image
ModuleEnd

Module="SoftcopyVOILUT"
	Sequence="SoftcopyVOILUTSequence"			Type="1"	VM="1-n"
		Sequence="ReferencedImageSequence"		Type="1C"	VM="1-n"	NoCondition=""	# realworld
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
		InvokeMacro="VOILUTMacro"
	SequenceEnd
ModuleEnd

Module="PresentationSeries"
	Name="Modality"								Type="1"	StringEnumValues="PresentationStateModality"
ModuleEnd

Module="PresentationStateIdentification"
	Name="PresentationCreationDate"				Type="1"
	Name="PresentationCreationTime"				Type="1"
	InvokeMacro="ContentIdentificationMacro"
ModuleEnd

DefineMacro="PresentationStateRelationshipMacro"
	Sequence="ReferencedSeriesSequence"			Type="1"	VM="1-n"
		Name="SeriesInstanceUID"				Type="1"
		Sequence="ReferencedImageSequence"		Type="1"	VM="1-n"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
	SequenceEnd
MacroEnd

Module="PresentationStateRelationship"
	InvokeMacro="PresentationStateRelationshipMacro"
ModuleEnd

Module="PresentationStateShutter"
	Name="ShutterPresentationValue"				Type="1C"	Condition="DisplayOrBitmapDisplayShutterModulePresent"
	Name="ShutterPresentationColorCIELabValue"	Type="1C"	Condition="DisplayOrBitmapDisplayShutterModulePresentAndNotGrayscaleSoftcopyPresentationState"
ModuleEnd

Module="PresentationStateMask"
	Sequence="MaskSubtractionSequence"			Type="1C"	VM="1"	Condition="MaskModulePresent"
		Name="MaskOperation"					Type="1"	StringEnumValues="MaskOperationForPresentationState"
		Name="ContrastFrameAveraging"			Type="1"
	SequenceEnd
	Name="RecommendedViewingMode"				Type="1C"	Condition="MaskModulePresent"	StringEnumValues="RecommendedViewingMode"
ModuleEnd

Module="PresentationStateBlending"
	Sequence="BlendingSequence"								Type="1"	VM="2"
		Name="BlendingPosition"								Type="1"	StringEnumValues="BlendingPosition"
		Name="StudyInstanceUID"								Type="1"
		InvokeMacro="PresentationStateRelationshipMacro"
		InvokeMacro="ModalityLUTMacro"
		Sequence="SoftcopyVOILUTSequence"					Type="1C"	VM="1-n"	NoCondition=""	# real-world "if a VOI LUT is to be applied"
			Sequence="ReferencedImageSequence"				Type="1C"	VM="1-n"	NoCondition=""	# real-world "does not apply to all the images and frames in the enclosing Item"
				InvokeMacro="ImageSOPInstanceReferenceMacro"
			SequenceEnd
			InvokeMacro="VOILUTMacro"
		SequenceEnd
	SequenceEnd
	Name="RelativeOpacity"								Type="1"
	Sequence="ReferencedSpatialRegistrationSequence"	Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="ICCProfile"
	Name="ICCProfile"											Type="1"
	Name="ColorSpace"											Type="3"
ModuleEnd

DefineMacro="HangingProtocolSelectorAttributeContextMacro"
	Name="SelectorSequencePointer"							Type="1C"	NoCondition=""
	Name="FunctionalGroupPointer"							Type="1C"	NoCondition=""
	Name="SelectorSequencePointerPrivateCreator"			Type="1C"	NoCondition=""
	Name="FunctionalGroupPrivateCreator"					Type="1C"	NoCondition=""
	Name="SelectorAttributePrivateCreator"					Type="1C"	NoCondition=""
MacroEnd

DefineMacro="HangingProtocolSelectorAttributeValueMacro"
	Name="SelectorATValue"						Type="1C"	Condition="SelectorAttributeVRIsAT"
	Name="SelectorCSValue"						Type="1C"	Condition="SelectorAttributeVRIsCS"
	Name="SelectorISValue"						Type="1C"	Condition="SelectorAttributeVRIsIS"
	Name="SelectorLOValue"						Type="1C"	Condition="SelectorAttributeVRIsLO"
	Name="SelectorLTValue"						Type="1C"	Condition="SelectorAttributeVRIsLT"
	Name="SelectorPNValue"						Type="1C"	Condition="SelectorAttributeVRIsPN"
	Name="SelectorSHValue"						Type="1C"	Condition="SelectorAttributeVRIsSH"
	Name="SelectorSTValue"						Type="1C"	Condition="SelectorAttributeVRIsST"
	Name="SelectorUTValue"						Type="1C"	Condition="SelectorAttributeVRIsUT"
	Name="SelectorDSValue"						Type="1C"	Condition="SelectorAttributeVRIsDS"
	Name="SelectorFDValue"						Type="1C"	Condition="SelectorAttributeVRIsFD"
	Name="SelectorFLValue"						Type="1C"	Condition="SelectorAttributeVRIsFL"
	Name="SelectorULValue"						Type="1C"	Condition="SelectorAttributeVRIsUL"
	Name="SelectorUSValue"						Type="1C"	Condition="SelectorAttributeVRIsUS"
	Name="SelectorSLValue"						Type="1C"	Condition="SelectorAttributeVRIsSL"
	Name="SelectorSSValue"						Type="1C"	Condition="SelectorAttributeVRIsSS"
	Sequence="SelectorCodeSequenceValue"		Type="1C"	VM="1-n"	Condition="SelectorAttributeVRIsSQ"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
MacroEnd

Module="HangingProtocolDefinition"
	Name="HangingProtocolName"									Type="1"
	Name="HangingProtocolDescription"							Type="1"
	Name="HangingProtocolLevel"									Type="1"	StringEnumValues="HangingProtocolLevel"
	Name="HangingProtocolCreator"								Type="1"
	Name="HangingProtocolCreationDateTime"						Type="1"
	Sequence="HangingProtocolDefinitionSequence"				Type="1"	VM="1-n"
		Name="Modality"											Type="1C"	Condition="AnatomicRegionSequenceNotPresent"	StringDefinedTerms="Modality"
		Sequence="AnatomicRegionSequence"						Type="1C"	VM="1-n"	Condition="ModalityNotPresent"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="Laterality"										Type="2C"	Condition="AnatomicRegionSequencePresent"	StringDefinedTerms="ImageLaterality"
		Sequence="ProcedureCodeSequence"						Type="2"	VM="0-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="ReasonForRequestedProcedureCodeSequence"		Type="2"	VM="0-n"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="NumberOfPriorsReferenced"								Type="1"
	Sequence="ImageSetsSequence"								Type="1"	VM="1-n"
		Sequence="ImageSetSelectorSequence"						Type="1"	VM="1-n"
			Name="ImageSetSelectorUsageFlag"					Type="1"	StringEnumValues="ImageSetSelectorUsageFlag"
			Name="SelectorAttribute"							Type="1"
			Name="SelectorAttributeVR"							Type="1"	StringEnumValues="SelectorAttributeVR"
			InvokeMacro="HangingProtocolSelectorAttributeContextMacro"
			InvokeMacro="HangingProtocolSelectorAttributeValueMacro"
			Name="SelectorValueNumber"							Type="1"
		SequenceEnd
		Sequence="TimeBasedImageSetsSequence"					Type="1"	VM="1-n"
			Name="ImageSetNumber"								Type="1"
			Name="ImageSetSelectorCategory"						Type="1"	StringEnumValues="ImageSetSelectorCategory"
			Name="RelativeTime"									Type="1C"	Condition="ImageSetSelectorCategoryIsRelativeTime"
			Name="RelativeTimeUnits"							Type="1C"	Condition="RelativeTimePresent"	StringEnumValues="RelativeTimeUnits"
			Name="AbstractPriorValue"							Type="1C"	Condition="ImageSetSelectorCategoryIsAbstractPriorAndAbstractPriorCodeSequenceNotPresent"
			Sequence="AbstractPriorCodeSequence"				Type="1C"	VM="1"	Condition="ImageSetSelectorCategoryIsAbstractPriorAndAbstractPriorValueNotPresent"
				InvokeMacro="CodeSequenceMacro"								DefinedContextID="31"
			SequenceEnd
			Name="ImageSetLabel"								Type="3"
		SequenceEnd
	SequenceEnd
	Sequence="HangingProtocolUserIdentificationCodeSequence"	Type="2"	VM="0-1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="HangingProtocolUserGroupName"							Type="3"
	Sequence="SourceHangingProtocolSequence"					Type="3"	VM="1"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="HangingProtocolEnvironment"
	Name="NumberOfScreens"										Type="2"
	Sequence="NominalScreenDefinitionSequence"					Type="2"	VM="0-n"
		InvokeMacro="ScreenSpecificationsMacro"
	SequenceEnd
ModuleEnd

DefineMacro="ScreenSpecificationsMacro"
	Name="NumberOfVerticalPixels"								Type="1"
	Name="NumberOfHorizontalPixels"								Type="1"
	Name="DisplayEnvironmentSpatialPosition"					Type="1"
	Name="ScreenMinimumGrayscaleBitDepth"						Type="1C"	Condition="ScreenMinimumColorBitDepthNotPresent"
	Name="ScreenMinimumColorBitDepth"							Type="1C"	Condition="ScreenMinimumGrayscaleBitDepthNotPresent"
	Name="ApplicationMaximumRepaintTime"						Type="3"
MacroEnd

Module="HangingProtocolDisplay"
	Sequence="DisplaySetsSequence"								Type="1"	VM="1-n"
		Name="DisplaySetNumber"									Type="1"
		Name="DisplaySetLabel"									Type="3"
		Name="DisplaySetPresentationGroup"						Type="1"
		Name="ImageSetNumber"									Type="1"
		Sequence="ImageBoxesSequence"							Type="1"	VM="1-n"	# is sometimes one, and sometimes more than one, depending on whether tiled :(
			Name="ImageBoxNumber"								Type="1"
			Name="DisplayEnvironmentSpatialPosition"			Type="1"
			Name="ImageBoxLayoutType"							Type="1"	StringDefinedTerms="ImageBoxLayoutTypeForHangingProtocol"
			Name="ImageBoxTileHorizontalDimension"				Type="1C"	Condition="ImageBoxLayoutTypeIsTiled"
			Name="ImageBoxTileVerticalDimension"				Type="1C"	Condition="ImageBoxLayoutTypeIsTiled"
			Name="ImageBoxScrollDirection"						Type="1C"	Condition="ImageBoxLayoutTypeIsTiledAndMoreThanOneTile"	StringEnumValues="ImageBoxScrollDirection"
			Name="ImageBoxSmallScrollType"						Type="2C"	Condition="ImageBoxLayoutTypeIsTiledAndMoreThanOneTile"	StringEnumValues="ImageBoxScrollType"
			Name="ImageBoxSmallScrollAmount"					Type="1C"	Condition="ImageBoxSmallScrollTypePresentWithValue"
			Name="ImageBoxLargeScrollType"						Type="2C"	Condition="ImageBoxLayoutTypeIsTiledAndMoreThanOneTile"	StringEnumValues="ImageBoxScrollType"
			Name="ImageBoxLargeScrollAmount"					Type="1C"	Condition="ImageBoxLargeScrollTypePresentWithValue"
			Name="ImageBoxOverlapPriority"						Type="3"	# should check value is between 1 and 100
			Name="PreferredPlaybackSequencing"					Type="1C"	Condition="ImageBoxLayoutTypeIsCine"	BinaryEnumValues="PreferredPlaybackSequencingForHangingProtocol"
			Name="RecommendedDisplayFrameRate"					Type="1C"	Condition="ImageBoxLayoutTypeIsCineAndCineRelativeToRealTimeNotPresent"
			Name="CineRelativeToRealTime"						Type="1C"	Condition="ImageBoxLayoutTypeIsCineAndRecommendedDisplayFrameRateNotPresent"
		SequenceEnd
		Sequence="FilterOperationsSequence"						Type="2"	VM="0-n"
			Name="FilterByCategory"								Type="1C"	Condition="SelectorAttributeNotPresent"	StringDefinedTerms="FilterByCategory"
			Name="FilterByAttributePresence"					Type="1C"	Condition="SelectorAttributePresentAndFilterByOperatorNotPresent"	StringDefinedTerms="FilterByAttributePresence"
			Name="SelectorAttribute"							Type="1C"	Condition="FilterByCategoryNotPresent"
			Name="SelectorAttributeVR"							Type="1C"	Condition="SelectorAttributeOrFilterByCategoryAndFilterByOperatorPresent"
			InvokeMacro="HangingProtocolSelectorAttributeContextMacro"
			InvokeMacro="HangingProtocolSelectorAttributeValueMacro"
			Name="SelectorValueNumber"							Type="1C"	Condition="SelectorAttributeAndFilterByOperatorPresent"
			Name="FilterByOperator"								Type="1C"	Condition="SelectorAttributePresentAndFilterByAttributePresenceNotPresentOrFilterByCategoryPresent"	StringEnumValues="FilterByOperator"
			Name="ImageSetSelectorUsageFlag"					Type="3"	StringEnumValues="ImageSetSelectorUsageFlag"
		SequenceEnd
		Sequence="SortingOperationsSequence"					Type="2"	VM="0-n"
			Name="SelectorAttribute"							Type="1C"	Condition="SortByCategoryNotPresent"
			InvokeMacro="HangingProtocolSelectorAttributeContextMacro"
			Name="SelectorValueNumber"							Type="1C"	Condition="SelectorAttributePresent"
			Name="SortByCategory"								Type="1C"	Condition="SelectorAttributeNotPresent"	StringDefinedTerms="SortByCategory"
			Name="SortingDirection"								Type="1"	StringEnumValues="SortingDirection"
		SequenceEnd
		Name="BlendingOperationType"							Type="3"	StringDefinedTerms="BlendingOperationType"
		Name="ReformattingOperationType"						Type="3"	StringDefinedTerms="ReformattingOperationType"
		Name="ReformattingThickness"							Type="1C"	Condition="ReformattingOperationTypeIsSlabOrMPR"
		Name="ReformattingInterval"								Type="1C"	Condition="ReformattingOperationTypeIsSlabOrMPR"
		Name="ReformattingOperationInitialViewDirection"		Type="1C"	Condition="ReformattingOperationTypeIsMPROr3D"	StringDefinedTerms="ReformattingOperationInitialViewDirection"
		Name="ThreeDRenderingType"								Type="1C"	Condition="ReformattingOperationTypeIs3D"	StringDefinedTerms="ThreeDRenderingType"
		Name="DisplaySetPatientOrientation"						Type="3"
		Name="DisplaySetHorizontalJustification"				Type="3"	StringEnumValues="DisplaySetHorizontalJustification"
		Name="DisplaySetVerticalJustification"					Type="3"	StringEnumValues="DisplaySetVerticalJustification"
		Name="VOIType"											Type="3"	StringDefinedTerms="VOIType"
		Name="PseudoColorType"									Type="3"	StringDefinedTerms="PseudoColorType"
		Name="ShowGrayscaleInverted"							Type="3"	StringDefinedTerms="YesNoFull"
		Name="ShowImageTrueSizeFlag"							Type="3"	StringDefinedTerms="YesNoFull"
		Name="ShowGraphicAnnotationFlag"						Type="3"	StringDefinedTerms="YesNoFull"
		Name="ShowPatientDemographicsFlag"						Type="3"	StringDefinedTerms="YesNoFull"
		Name="ShowAcquisitionTechniquesFlag"					Type="3"	StringDefinedTerms="YesNoFull"
		Name="DisplaySetPresentationGroupDescription"			Type="3"
	SequenceEnd
	Name="PartialDataDisplayHandling"							Type="3"	StringEnumValues="PartialDataDisplayHandling"
	Sequence="SynchronizedScrollingSequence"					Type="3"	VM="1-n"
		Name="DisplaySetScrollingGroup"							Type="1"
	SequenceEnd
	Sequence="NavigationIndicatorSequence"						Type="3"	VM="1-n"
		Name="NavigationDisplaySet"								Type="1C"	NoCondition=""	# real world
		Name="ReferenceDisplaySets"								Type="1"
	SequenceEnd
ModuleEnd

Module="ColorPaletteDefinition"
	InvokeMacro="ContentIdentificationMacro"
ModuleEnd

Module="StructuredDisplay"
	InvokeMacro="ContentIdentificationMacro"
	Name="PresentationCreationDate"								Type="1"
	Name="PresentationCreationTime"								Type="1"
	Name="NumberOfScreens"										Type="1"
	Verify="NumberOfScreens"												BinaryEnumValues="One"	Condition="BasicStructuredDisplayInstance"
	Sequence="NominalScreenDefinitionSequence"					Type="1"	VM="1-n"	# should check length is == NumberOfScreens, but no mechanism for that :(
		InvokeMacro="ScreenSpecificationsMacro"
	SequenceEnd
	Sequence="IconImageSequence"								Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
	Name="StructuredDisplayBackgroundCIELabValue"				Type="3"
	Name="EmptyImageBoxCIELabValue"								Type="3"
	Name="HangingProtocolName"									Type="3"
	Name="HangingProtocolCreator"								Type="3"
ModuleEnd

Module="StructuredDisplayImageBox"
	Sequence="StructuredDisplayImageBoxSequence"				Type="1"	VM="1-n"
		Name="DisplayEnvironmentSpatialPosition"				Type="1"
		Name="ImageBoxNumber"									Type="1"
		Name="ImageBoxLayoutType"								Type="1"	StringDefinedTerms="ImageBoxLayoutTypeForStructuredDisplay"
		Name="ImageBoxOverlapPriority"							Type="3"
		Verify="ImageBoxOverlapPriority"									Condition="ImageBoxOverlapPriorityValueNot1To100"	ThenErrorMessage="Is not a positive integer in the range 1 to 100" ShowValueWithMessage="true"
		Name="DisplaySetHorizontalJustification"				Type="3"	StringEnumValues="DisplaySetHorizontalJustification"
		Name="DisplaySetVerticalJustification"					Type="3"	StringEnumValues="DisplaySetVerticalJustification"
		Name="PreferredPlaybackSequencing"						Type="1C"	Condition="ImageBoxLayoutTypeIsCine"	BinaryEnumValues="PreferredPlaybackSequencingForStructuredDisplay"
		Name="RecommendedDisplayFrameRate"						Type="1C"	Condition="ImageBoxLayoutTypeIsCineAndCineRelativeToRealTimeNotPresent"
		Verify="RecommendedDisplayFrameRate"								Condition="RecommendedDisplayFrameRateNotGreaterThanZero"	ThenErrorMessage="Is not greater than 0" ShowValueWithMessage="true"
		Name="CineRelativeToRealTime"							Type="1C"	Condition="ImageBoxLayoutTypeIsCineAndRecommendedDisplayFrameRateNotPresent"
		Verify="CineRelativeToRealTime"										Condition="CineRelativeToRealTimeNotGreaterThanZero"	ThenErrorMessage="Is not greater than 0" ShowValueWithMessage="true"
		Name="InitialCineRunState"								Type="1C"	Condition="ImageBoxLayoutTypeIsCine"	StringDefinedTerms="InitialCineRunState"
		Name="StartTrim"										Type="2C"	Condition="ImageBoxLayoutTypeIsCine"
		Name="StopTrim"											Type="2C"	Condition="ImageBoxLayoutTypeIsCine"
		Sequence="ReferencedFirstFrameSequence"					Type="2C"	VM="0-1"	Condition="ImageBoxLayoutTypeIsStack"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="ReferencedImageSequence"						Type="2C"	VM="0-n"	Condition="NoReferencedPresentationStateOrStereometricInstanceOrInstance"
			InvokeMacro="ImageSOPInstanceReferenceMacro"
			Sequence="ReferencedPresentationStateSequence"		Type="1C"	VM="1"		NoCondition=""
				InvokeMacro="SOPInstanceReferenceMacro"
			SequenceEnd
		SequenceEnd
		Sequence="ReferencedPresentationStateSequence"			Type="1C"	VM="1"		Condition="NoReferencedImageOrStereometricInstanceOrInstance"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="ReferencedInstanceSequence"					Type="1C"	VM="1"		Condition="NoReferencedPresentationStateOrStereometricInstanceOrImage"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
		Sequence="ReferencedStereometricInstanceSequence"		Type="1C"	VM="1"		Condition="NoReferencedPresentationStateOrInstanceOrImage"
			InvokeMacro="SOPInstanceReferenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="ImageBoxSynchronizationSequence"					Type="1C"	VM="1-n"	NoCondition=""
		Name="SynchronizedImageBoxList"							Type="1"	VM="2-n"
		Name="TypeOfSynchronization"							Type="1"				StringEnumValues="TypeOfSynchronizationBetweenImageBoxes"
	SequenceEnd
ModuleEnd

Module="StructuredDisplayAnnotation"
	Sequence="StructuredDisplayTextBoxSequence"					Type="1"	VM="1-n"
		Name="UnformattedTextValue"								Type="1"
		Name="DisplayEnvironmentSpatialPosition"				Type="1"
		Name="BoundingBoxTextHorizontalJustification"			Type="1"				StringEnumValues="BoundingBoxTextHorizontalJustification"
		Name="GraphicLayerRecommendedDisplayCIELabValue"		Type="3"
	SequenceEnd
ModuleEnd


DefineMacro="CommonCTMRImageDescriptionImageLevelMacro" InformationEntity="Image"
	Name="PixelPresentation"						Type="1"	StringEnumValues="CommonCTMRPixelPresentationImageLevel"
	Verify="PixelPresentation"									Condition="EnhancedMRColorImageInstance"	StringEnumValues="PixelPresentationTrueColor"
	Name="VolumetricProperties"						Type="1"	StringEnumValues="CommonCTMRVolumetricPropertiesImageLevel"
	Name="VolumeBasedCalculationTechnique"			Type="1"	StringDefinedTerms="CommonCTMRVolumeBasedCalculationTechniqueImageLevel"
MacroEnd

DefineMacro="CommonCTMRImageDescriptionFrameLevelMacro" InformationEntity="Image"
	Name="PixelPresentation"						Type="1"	StringEnumValues="CommonCTMRPixelPresentationFrameLevel"
	Name="VolumetricProperties"						Type="1"	StringEnumValues="CommonCTMRVolumetricPropertiesFrameLevel"
	Name="VolumeBasedCalculationTechnique"			Type="1"	StringDefinedTerms="CommonCTMRVolumeBasedCalculationTechniqueFrameLevel"
MacroEnd

DefineMacro="MRImageDescriptionImageLevelMacro" InformationEntity="Image"
	Name="ComplexImageComponent"			Type="1C"	StringEnumValues="EnhancedMRComplexImageComponentImageLevel"	Condition="NotLegacyConvertedMR" mbpo="true"
	Name="AcquisitionContrast"				Type="1C"	StringEnumValues="EnhancedMRAcquisitionContrastImageLevel"		Condition="NotLegacyConvertedMR" mbpo="true"
MacroEnd

DefineMacro="MRImageDescriptionFrameLevelMacro" InformationEntity="Image"
	Name="ComplexImageComponent"			Type="1C"	StringEnumValues="EnhancedMRComplexImageComponentFrameLevel"	Condition="NotLegacyConvertedMR" mbpo="true"
	Name="AcquisitionContrast"				Type="1C"	StringEnumValues="EnhancedMRAcquisitionContrastFrameLevel"		Condition="NotLegacyConvertedMR" mbpo="true"
MacroEnd

DefineMacro="MRSpectroscopyDescriptionImageLevelMacro" InformationEntity="Image"
	Name="VolumetricProperties"					Type="1"	StringEnumValues="CommonCTMRVolumetricPropertiesImageLevel"
	Name="VolumeBasedCalculationTechnique"		Type="1"	StringDefinedTerms="MRSpectroscopyVolumeBasedCalculationTechniqueImageLevel"
	Name="ComplexImageComponent"				Type="1"	StringEnumValues="MRSpectroscopyComplexImageComponentImageLevel"
	Name="AcquisitionContrast"					Type="1"	StringEnumValues="MRSpectroscopyAcquisitionContrastImageLevel"
MacroEnd

DefineMacro="MRSpectroscopyDescriptionFrameLevelMacro" InformationEntity="Image"
	Name="VolumetricProperties"					Type="1"	StringEnumValues="CommonCTMRVolumetricPropertiesFrameLevel"
	Name="VolumeBasedCalculationTechnique"		Type="1"	StringDefinedTerms="MRSpectroscopyVolumeBasedCalculationTechniqueFrameLevel"
	Name="ComplexImageComponent"				Type="1"	StringEnumValues="MRSpectroscopyComplexImageComponentFrameLevel"
	Name="AcquisitionContrast"					Type="1"	StringEnumValues="MRSpectroscopyAcquisitionContrastFrameLevel"
MacroEnd

DefineMacro="MRImageFrameTypeMacro" InformationEntity="FunctionalGroup"
	Sequence="MRImageFrameTypeSequence"			Type="1"	VM="1"
		Name="FrameType"						Type="1"	VM="4"
		Verify="FrameType"									ValueSelector="0"	StringEnumValues="CommonEnhancedFrameType1"
		Verify="FrameType"									ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
		Verify="FrameType"									ValueSelector="2"	StringDefinedTerms="EnhancedMRImageAndFrameType3"
		Verify="FrameType"									ValueSelector="3"	StringDefinedTerms="EnhancedMRFrameType4"
		InvokeMacro="CommonCTMRImageDescriptionFrameLevelMacro"
		InvokeMacro="MRImageDescriptionFrameLevelMacro"
	SequenceEnd
MacroEnd

DefineMacro="MRTimingAndRelatedParametersMacro" InformationEntity="FunctionalGroup"
	Sequence="MRTimingAndRelatedParametersSequence"		Type="1"	VM="1"
		Name="RepetitionTime"							Type="1C"	Condition="Always"	NotZeroWarning=""	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="FlipAngle"								Type="1C"	Condition="Always"	NotZeroWarning=""	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="EchoTrainLength"							Type="1C"	Condition="Always"	NotZeroWarning=""	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="RFEchoTrainLength"						Type="1C"	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="GradientEchoTrainLength"					Type="1C"	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Sequence="SpecificAbsorptionRateSequence"		Type="1C"	VM="1-n"	Condition="Always"	# real world
			Name="SpecificAbsorptionRateDefinition"		Type="1"	StringDefinedTerms="SpecificAbsorptionRateDefinition"
			Name="SpecificAbsorptionRateValue"			Type="1"
		SequenceEnd
		Name="GradientOutputType"						Type="1C"	StringDefinedTerms="GradientOutputType"	Condition="GradientOutputIsPresent"	# real world, but interconnect
		Name="GradientOutput"							Type="1C"	Condition="GradientOutputTypeIsPresent"	# real world, but interconnect
		Sequence="OperatingModeSequence"				Type="1C"	VM="1-n"	Condition="Always"	# real world
			Name="OperatingModeType"					Type="1"	StringDefinedTerms="OperatingModeType"
			Name="OperatingMode"						Type="1"	StringDefinedTerms="OperatingMode"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="MRFOVGeometryMacro" InformationEntity="FunctionalGroup"
	Sequence="MRFOVGeometrySequence"						Type="1"	VM="1"
		Name="InPlanePhaseEncodingDirection"				Type="1C"	StringEnumValues="InplanePhaseEncodingDirection"	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="MRAcquisitionFrequencyEncodingSteps"			Type="1C"	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="MRAcquisitionPhaseEncodingStepsInPlane"		Type="1C"	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="MRAcquisitionPhaseEncodingStepsOutOfPlane"	Type="1C"	NoCondition=""		# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL and /MRAcquisitionType == 3D
		Name="PercentSampling"								Type="1C"	Condition="Always"	NotZeroWarning=""	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="PercentPhaseFieldOfView"						Type="1C"	Condition="Always"	NotZeroWarning=""	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
	SequenceEnd
MacroEnd

DefineMacro="MREchoMacro" InformationEntity="FunctionalGroup"
	Sequence="MREchoSequence"				Type="1"	VM="1"
		Name="EffectiveEchoTime"			Type="1"
	SequenceEnd
MacroEnd

DefineMacro="MRModifierMacro" InformationEntity="FunctionalGroup"
	Sequence="MRModifierSequence"					Type="1"	VM="1"
		Name="InversionRecovery"					Type="1C"	StringEnumValues="YesNoFull"			Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="InversionTimes"						Type="1C"							Condition="InversionRecoveryIsYes"	# also should check FrameType[0] :(
		Name="FlowCompensation"						Type="1C"	StringDefinedTerms="FlowCompensation"		Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="FlowCompensationDirection"			Type="1C"	StringEnumValues="FlowCompensationDirection"	Condition="FlowCompensationNotNone"	# also should check FrameType[0] etc. :(
		Name="Spoiling"								Type="1C"	StringEnumValues="Spoiling"			NoCondition=""	# EchoPulseSequenceGradientOrBoth (macro can't access root list), also should check FrameType[0] etc. :(
		Name="T2Preparation"						Type="1C"	StringEnumValues="YesNoFull"			Condition="Always"	# should check FrameType[0] etc. :(
		Name="SpectrallySelectedExcitation"			Type="1C"	StringEnumValues="SpectrallySelectedExcitation"	Condition="Always"	# should check FrameType[0] etc. :(
		Name="SpatialPresaturation"					Type="1C"	StringEnumValues="SpatialPresaturation"		Condition="Always"	# should check FrameType[0] etc. :(
		Name="PartialFourier"						Type="1C"	StringEnumValues="YesNoFull"			Condition="Always"	# should check FrameType[0] etc. :(
		Name="PartialFourierDirection"				Type="1C"	StringEnumValues="PartialFourierDirection"	Condition="PartialFourierIsYes"	# should check FrameType[0] etc. :(
		Name="ParallelAcquisition"					Type="1C"	StringEnumValues="YesNoFull"			Condition="Always"	# should check FrameType[0] etc. :(
		Name="ParallelAcquisitionTechnique"			Type="1C"	StringEnumValues="ParallelAcquisitionTechnique"	Condition="ParallelAcquisitionIsYes"	# should check FrameType[0] etc. :(
		Name="ParallelReductionFactorInPlane"		Type="1C"							Condition="ParallelAcquisitionIsYes"	# should check FrameType[0] etc. :(
		Name="ParallelReductionFactorOutOfPlane"	Type="1C"							Condition="ParallelAcquisitionIsYes"	# should check FrameType[0] etc. :(
		Name="ParallelReductionFactorSecondInPlane"	Type="1C"							Condition="ParallelAcquisitionIsYes"	# should check is spectroscopy instance and FrameType[0] etc. :(
	SequenceEnd
MacroEnd

DefineMacro="MRImagingModifierMacro" InformationEntity="FunctionalGroup"
	Sequence="MRImagingModifierSequence"			Type="1"	VM="1"
		Name="MagnetizationTransfer"				Type="1C"	StringEnumValues="MagnetizationTransfer"	Condition="Always"	# should check FrameType[0] etc. :(
		Name="BloodSignalNulling"					Type="1C"	StringEnumValues="YesNoFull"			Condition="Always"	# should check FrameType[0] etc. :(
		Name="Tagging"								Type="1C"	StringEnumValues="Tagging"			Condition="Always"	# should check FrameType[0] etc. :(
		Name="TagSpacingFirstDimension"				Type="1C"	NotZeroWarning=""							Condition="TaggingIsGridOrLine"	# should check FrameType[0] etc. :(
		Name="TagSpacingSecondDimension"			Type="1C"	NotZeroWarning=""							Condition="TaggingIsGrid"	# should check FrameType[0] etc. :(
		Name="TagAngleFirstAxis"					Type="1C"							Condition="TaggingIsGridOrLine"	# should check FrameType[0] etc. :(
		Name="TagAngleSecondAxis"					Type="1C"							Condition="TaggingIsGrid"	# should check FrameType[0] etc. :(
		Name="TagThickness"							Type="1C"	NotZeroWarning=""							Condition="TaggingIsGridOrLine"	# should check FrameType[0] etc. :(
		Name="TaggingDelay"							Type="3"
		Name="TransmitterFrequency"					Type="1C"	NotZeroWarning=""							Condition="Always"	# should check FrameType[0] etc. :(
		Name="PixelBandwidth"						Type="1C"	NotZeroWarning=""							Condition="Always"	# should check FrameType[0] etc. :(
	SequenceEnd
MacroEnd

DefineMacro="MRReceiveCoilMacro" InformationEntity="FunctionalGroup"
	Sequence="MRReceiveCoilSequence"			Type="1"	VM="1-n"
		Name="ReceiveCoilName"					Type="1"
		Name="ReceiveCoilManufacturerName"		Type="2"
		Name="ReceiveCoilType"					Type="1"	StringDefinedTerms="ReceiveCoilType"
		Name="QuadratureReceiveCoil"			Type="1"	StringEnumValues="YesNoFull"
		Sequence="MultiCoilDefinitionSequence"	Type="1C"	VM="1-n"					Condition="ReceiveCoilTypeIsMultiCoil"	# should check FrameType[0] etc. :(
			Name="MultiCoilElementName"			Type="1"
			Name="MultiCoilElementUsed"			Type="1"	StringEnumValues="YesNoFull"
		SequenceEnd
		Name="MultiCoilConfiguration"			Type="3"
	SequenceEnd
MacroEnd

DefineMacro="MRTransmitCoilMacro" InformationEntity="FunctionalGroup"
	Sequence="MRTransmitCoilSequence"			Type="1"	VM="1"
		Name="TransmitCoilName"					Type="1"
		Name="TransmitCoilManufacturerName"		Type="2"
		Name="TransmitCoilType"					Type="1"	StringDefinedTerms="TransmitCoilType"
	SequenceEnd
MacroEnd

DefineMacro="MRDiffusionMacro" InformationEntity="FunctionalGroup"
	Sequence="MRDiffusionSequence"						Type="1"	VM="1"
		Name="DiffusionBValue"							Type="1C"	NoCondition=""	# should check FrameType[0] etc. :(
		Name="DiffusionDirectionality"					Type="1C"	StringDefinedTerms="DiffusionDirectionality"	Condition="Always"	# should check FrameType[0] etc. :(
		Sequence="DiffusionGradientDirectionSequence"	Type="1C"	VM="1"				Condition="DiffusionDirectionalityIsDirectional" mbpo="true" # really should check if DiffusionDirectionality is BMATRIX
			Name="DiffusionGradientOrientation"			Type="1"
		SequenceEnd
		Sequence="DiffusionBMatrixSequence"				Type="1C"	VM="1"				Condition="DiffusionDirectionalityIsBMatrix"
			Name="DiffusionBValueXX"					Type="1"
			Name="DiffusionBValueXY"					Type="1"
			Name="DiffusionBValueXZ"					Type="1"
			Name="DiffusionBValueYY"					Type="1"
			Name="DiffusionBValueYZ"					Type="1"
			Name="DiffusionBValueZZ"					Type="1"
		SequenceEnd
		Name="DiffusionAnisotropyType"					Type="1C"	Condition="NeedDiffusionAnisotropyType"	StringDefinedTerms="DiffusionAnisotropyType" mbpo="true" # really shouldn't have mbpo, but account for inadequate condition using ImageType rather than 9current) FraneType
	SequenceEnd
MacroEnd

DefineMacro="MRAveragesMacro" InformationEntity="FunctionalGroup"
	Sequence="MRAveragesSequence"				Type="1"	VM="1"
		Name="NumberOfAverages"					Type="1"	NotZeroWarning=""
	SequenceEnd
MacroEnd

DefineMacro="MRSpatialSaturationMacro" InformationEntity="FunctionalGroup"
	Sequence="MRSpatialSaturationSequence"			Type="2"	VM="0-n"
		Name="SlabThickness"						Type="1"	NotZeroWarning=""
		Name="SlabOrientation"						Type="1"
		Name="MidSlabPosition"						Type="1"
	SequenceEnd
MacroEnd

DefineMacro="MRMetaboliteMapMacro" InformationEntity="FunctionalGroup"
	Sequence="MRMetaboliteMapSequence"							Type="1"	VM="1"
		Name="MetaboliteMapDescription"							Type="1"
		Sequence="MetaboliteMapCodeSequence"					Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="ChemicalShiftSequence"						Type="3"	VM="1-n"
			Name="ChemicalShiftMinimumIntegrationLimitInppm"	Type="1"
			Name="ChemicalShiftMaximumIntegrationLimitInppm"	Type="1"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="MRVelocityEncodingMacro" InformationEntity="FunctionalGroup"
	Sequence="MRVelocityEncodingSequence"		Type="1"	VM="1-n"
		Name="VelocityEncodingDirection"		Type="1"
		Name="VelocityEncodingMinimumValue"		Type="1"
		Name="VelocityEncodingMaximumValue"		Type="1"
	SequenceEnd
MacroEnd

DefineMacro="MRArterialSpinLabelingMacro" InformationEntity="FunctionalGroup"
	Sequence="MRArterialSpinLabelingSequence"	Type="1"	VM="1-n"
		Name="ASLTechniqueDescription"			Type="2"
		Name="ASLContext"						Type="1C"	NoCondition="" mbpo="true" StringEnumValues="ASLContext"	# FrameType is ORIGINAL too hard :(
		Sequence="ASLSlabSequence"				Type="1C"	VM="1-n" Condition="ASLContextIsControlLOrLabel" mbpo="true"
			Name="ASLSlabNumber"				Type="1"
			InvokeMacro="GeneralAnatomyOptionalMacro"
			Name="ASLSlabThickness"				Type="1"
			Name="ASLSlabOrientation"			Type="1"
			Name="ASLMidSlabPosition"			Type="1"
			Name="ASLPulseTrainDuration"		Type="1"
		SequenceEnd
		Name="ASLCrusherFlag"					Type="1"	StringEnumValues="YesNoFull"
		Name="ASLCrusherFlowLimit"				Type="1C"	Condition="ASLCrusherFlagIsYes"
		Name="ASLCrusherDescription"			Type="1C"	Condition="ASLCrusherFlagIsYes"
		Name="ASLBolusCutoffFlag"				Type="1"	StringEnumValues="YesNoFull"
		Sequence="ASLBolusCutoffTimingSequence"	Type="1C"	VM="1" Condition="ASLBolusCutoffFlagIsYes"
			Name="ASLBolusCutoffDelayTime"		Type="1"
			Name="ASLBolusCutoffTechnique"		Type="2"
		SequenceEnd
	SequenceEnd
MacroEnd

DefineMacro="MRImageAndSpectroscopyInstanceMacro" InformationEntity="Image"
	Name="AcquisitionNumber"						Type="3"
	Name="AcquisitionDateTime"						Type="1C"	Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedMR" mbpo="true"
	Name="AcquisitionDuration"						Type="1C"	Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedMR" mbpo="true"
	Sequence="ReferencedRawDataSequence"			Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedWaveformSequence"			Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedImageEvidenceSequence"		Type="1C"	VM="1-n"	Condition="ReferencedImageSequenceIsPresentInFunctionalGroups"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="SourceImageEvidenceSequence"			Type="1C"	VM="1-n"	Condition="SourceImageSequenceIsPresentInFunctionalGroups"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedPresentationStateSequence"	Type="1C"	VM="1-n"	NoCondition=""	# real world
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Name="ContentQualification"						Type="1C"	StringEnumValues="ContentQualification"	Condition="NotLegacyConvertedMR" mbpo="true"
	Name="ResonantNucleus"							Type="1C"	StringDefinedTerms="ResonantNucleus"	Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedMR" mbpo="true"
	Name="KSpaceFiltering"							Type="1C"	StringDefinedTerms="KSpaceFiltering"	Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedMR" mbpo="true"
	Name="MagneticFieldStrength"					Type="1C"	NotZeroWarning=""						Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedMR" mbpo="true"
	Name="ApplicableSafetyStandardAgency"			Type="1C"	StringDefinedTerms="ApplicableSafetyStandardAgency"	Condition="NotLegacyConvertedMR" mbpo="true"
	Name="ApplicableSafetyStandardDescription"		Type="3"
	Name="ImageComments"							Type="3"
	Name="IsocenterPosition"						Type="3"
	Name="B1rms"									Type="3"
MacroEnd

Module="MultiFrameFunctionalGroupsForEnhancedMRImage"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInPerFrameFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="NeedRespiratorySynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRImageFrameTypeMacro"		Condition="MRImageFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRTimingAndRelatedParametersMacro"	Condition="NeedMRTimingAndRelatedParametersMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRFOVGeometryMacro"		Condition="NeedMRFOVGeometryMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MREchoMacro"			Condition="NeedMREchoMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRModifierMacro"			Condition="NeedMRModifierMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRImagingModifierMacro"		Condition="NeedMRImagingModifierMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRReceiveCoilMacro"		Condition="NeedMRReceiveCoilMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRTransmitCoilMacro"		Condition="NeedMRTransmitCoilMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRDiffusionMacro"			Condition="NeedMRDiffusionMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRAveragesMacro"			Condition="NeedMRAveragesMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRSpatialSaturationMacro"		Condition="NeedMRSpatialSaturationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRMetaboliteMapMacro"		Condition="NeedMRMetaboliteMapMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRVelocityEncodingMacro"		Condition="NeedMRVelocityEncodingMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRArterialSpinLabelingMacro"		Condition="NeedMRArterialSpinLabelingMacroInSharedFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"			Condition="TemporalPositionMacroOKInSharedFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInSharedFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequenceAndPhotometricInterpretationIsMonochrome2"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="NeedRespiratorySynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRImageFrameTypeMacro"		Condition="MRImageFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="MRTimingAndRelatedParametersMacro"	Condition="NeedMRTimingAndRelatedParametersMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRFOVGeometryMacro"		Condition="NeedMRFOVGeometryMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MREchoMacro"			Condition="NeedMREchoMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRModifierMacro"			Condition="NeedMRModifierMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRImagingModifierMacro"		Condition="NeedMRImagingModifierMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRReceiveCoilMacro"		Condition="NeedMRReceiveCoilMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRTransmitCoilMacro"		Condition="NeedMRTransmitCoilMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRDiffusionMacro"			Condition="NeedMRDiffusionMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRAveragesMacro"			Condition="NeedMRAveragesMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRSpatialSaturationMacro"		Condition="NeedMRSpatialSaturationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRMetaboliteMapMacro"		Condition="NeedMRMetaboliteMapMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRVelocityEncodingMacro"		Condition="NeedMRVelocityEncodingMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRArterialSpinLabelingMacro"		Condition="NeedMRArterialSpinLabelingMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"			Condition="TemporalPositionMacroOKInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

DefineMacro="MRSpectroscopyFrameTypeMacro" InformationEntity="FunctionalGroup"
	Sequence="MRSpectroscopyFrameTypeSequence"	Type="1"	VM="1"
		Name="FrameType"						Type="1"	VM="4"
		Verify="FrameType"								ValueSelector="0"	StringEnumValues="CommonEnhancedFrameType1"
		Verify="FrameType"								ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
		Verify="FrameType"								ValueSelector="2"	StringDefinedTerms="EnhancedMRSpectroscopyImageAndFrameType3"
		Verify="FrameType"								ValueSelector="3"	StringDefinedTerms="EnhancedMRSpectroscopyFrameType4"
		InvokeMacro="MRSpectroscopyDescriptionFrameLevelMacro"
	SequenceEnd
MacroEnd

DefineMacro="MRSpectroscopyFOVGeometryMacro" InformationEntity="FunctionalGroup"
	Sequence="MRSpectroscopyFOVGeometrySequence"			Type="1"	VM="1"
		Name="SpectroscopyAcquisitionDataColumns"			Type="1C"	NotZeroWarning=""	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="SpectroscopyAcquisitionPhaseRows"				Type="1C"	NotZeroWarning=""	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="SpectroscopyAcquisitionPhaseColumns"			Type="1C"	NotZeroWarning=""	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="SpectroscopyAcquisitionOutOfPlanePhaseSteps"	Type="1C"	NotZeroWarning=""	NoCondition=""		# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL and /MRSpectroscopyAcquisitionType == PLANE
		Name="PercentSampling"								Type="1C"	NotZeroWarning=""	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
		Name="PercentPhaseFieldOfView"						Type="1C"	NotZeroWarning=""	Condition="Always"	# ../MRImageFrameTypeMacro/FrameType[0] == ORIGINAL
	SequenceEnd
MacroEnd

Module="MultiFrameFunctionalGroupsForMRSpectroscopy"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="NeedRespiratorySynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRSpectroscopyFrameTypeMacro"	Condition="MRSpectroscopyFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRTimingAndRelatedParametersMacro"	Condition="NeedMRTimingAndRelatedParametersMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRSpectroscopyFOVGeometryMacro"	Condition="NeedMRSpectroscopyFOVGeometryMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MREchoMacro"			Condition="NeedMREchoMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRModifierMacro"			Condition="NeedMRModifierMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRReceiveCoilMacro"		Condition="NeedMRReceiveCoilMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRTransmitCoilMacro"		Condition="NeedMRTransmitCoilMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRDiffusionMacro"			Condition="NeedMRDiffusionMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRAveragesMacro"			Condition="NeedMRAveragesMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRSpatialSaturationMacro"		Condition="NeedMRSpatialSaturationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MRVelocityEncodingMacro"		Condition="NeedMRVelocityEncodingMacroInSharedFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"			Condition="TemporalPositionMacroOKInSharedFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="NeedRespiratorySynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRSpectroscopyFrameTypeMacro"	Condition="MRSpectroscopyFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="MRTimingAndRelatedParametersMacro"	Condition="NeedMRTimingAndRelatedParametersMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRSpectroscopyFOVGeometryMacro"	Condition="NeedMRSpectroscopyFOVGeometryMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MREchoMacro"			Condition="NeedMREchoMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRModifierMacro"			Condition="NeedMRModifierMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRReceiveCoilMacro"		Condition="NeedMRReceiveCoilMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRTransmitCoilMacro"		Condition="NeedMRTransmitCoilMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRDiffusionMacro"			Condition="NeedMRDiffusionMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRAveragesMacro"			Condition="NeedMRAveragesMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRSpatialSaturationMacro"		Condition="NeedMRSpatialSaturationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRVelocityEncodingMacro"		Condition="NeedMRVelocityEncodingMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"			Condition="TemporalPositionMacroOKInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="EnhancedMRImage"
	InvokeMacro="MRImageAndSpectroscopyInstanceMacro"
	Name="ImageType"								Type="1"	VM="4"
	Verify="ImageType"											ValueSelector="0"	StringEnumValues="CommonEnhancedImageType1"
	Verify="ImageType"											ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
	Verify="ImageType"											ValueSelector="2"	StringDefinedTerms="EnhancedMRImageAndFrameType3"
	Verify="ImageType"											ValueSelector="3"	StringDefinedTerms="EnhancedMRImageType4"
	InvokeMacro="CommonCTMRImageDescriptionImageLevelMacro"
	InvokeMacro="MRImageDescriptionImageLevelMacro"

	Name="SamplesPerPixel"							Type="1"
	Verify="SamplesPerPixel"									Condition="PhotometricInterpretationIsMonochrome"	BinaryEnumValues="SamplesPerPixelIsOne"
	Verify="SamplesPerPixel"									Condition="PhotometricInterpretationIsColor"		BinaryEnumValues="SamplesPerPixelIsThree"

	Name="PhotometricInterpretation"				Type="1"
	Verify="PhotometricInterpretation"							Condition="EnhancedMRImageInstance"      StringEnumValues="PhotometricInterpretationMonochrome2"
	Verify="PhotometricInterpretation"							Condition="EnhancedMRColorImageInstance" StringEnumValues="PhotometricInterpretationRGBOrYBR_FULL_422OrYBR_RCTOrYBR_ICTOrYBR_PARTIAL_420"

	Verify="PhotometricInterpretation"				Condition="UncompressedTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"				Condition="JPEGLSLosslessTransferSyntaxAndThreeSamples"					StringEnumValues="PhotometricInterpretationRGB"
	Verify="PhotometricInterpretation"				Condition="JPEG2000TransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRICT"
	Verify="PhotometricInterpretation"				Condition="JPEG2000LosslessTransferSyntaxAndThreeSamples"				StringEnumValues="PhotometricInterpretationYBRRCT"
	Verify="PhotometricInterpretation"				Condition="MPEG2TransferSyntax"											StringEnumValues="PhotometricInterpretationYBRPartial420"	# regardless of number of samples (required to be 3 by PS 3.5)
	Verify="PhotometricInterpretation"				Condition="JPEGLossyTransferSyntaxAndThreeSamples"						StringEnumValues="PhotometricInterpretationYBRFull422"
	Verify="PhotometricInterpretation"				Condition="RLETransferSyntaxAndThreeSamples"							StringEnumValues="PhotometricInterpretationYBRFullOrRGB"

	Name="BitsAllocated"							Type="1"	
	Verify="BitsAllocated"										Condition="PhotometricInterpretationIsMonochrome"	BinaryEnumValues="BitsAre8Or16"
	Verify="BitsAllocated"										Condition="PhotometricInterpretationIsColor"		BinaryEnumValues="BitsAre8"

	Name="BitsStored"								Type="1"
	Verify="BitsStored"											Condition="PhotometricInterpretationIsMonochrome"	BinaryEnumValues="BitsAre8Or12Or16"
	Verify="BitsStored"											Condition="PhotometricInterpretationIsColor"		BinaryEnumValues="BitsAre8"

	Name="HighBit"									Type="1"
	Verify="HighBit"											Condition="PhotometricInterpretationIsMonochrome"	BinaryEnumValues="BitsAre7Or11Or15"
	Verify="HighBit"											Condition="PhotometricInterpretationIsColor"		BinaryEnumValues="BitsAre7"

	Name="PixelRepresentation"						Type="1"
	Verify="PixelRepresentation"								Condition="PhotometricInterpretationIsMonochrome"	BinaryEnumValues="PixelRepresentation"
	Verify="PixelRepresentation"								Condition="PhotometricInterpretationIsColor"		BinaryEnumValues="PixelRepresentationUnsigned"

	Name="PlanarConfiguration"						Type="1C"	Condition="SamplesPerPixelGreaterThanOne"	BinaryEnumValues="PlanarConfigurationIsColorByPixel"
	
	Name="BurnedInAnnotation"						Type="1C"	Condition="NotLegacyConvertedMR"	StringEnumValues="NoFull"	mbpo="true"
	Name="RecognizableVisualFeatures"				Type="3"	StringEnumValues="YesNoFull"
	Name="LossyImageCompression"					Type="1C"	Condition="NotLegacyConvertedMR"	StringEnumValues="LossyImageCompression"	mbpo="true"
	Name="LossyImageCompressionRatio"				Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"				Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"								Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="PresentationLUTShape"						Type="1"	StringEnumValues="IdentityPresentationLUTShape"
	Sequence="IconImageSequence"					Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
	InvokeMacro="OptionalViewAndSliceProgressionDirectionMacro"
ModuleEnd

Module="MRPulseSequence"
	Name="PulseSequenceName"				Type="1C"	Condition="ImageTypeValue1OriginalOrMixed"
	Name="MRAcquisitionType"				Type="1C"	StringDefinedTerms="EnhancedMRAcquisitionType"		Condition="ImageTypeValue1OriginalOrMixed"
	Name="EchoPulseSequence"				Type="1C"	StringEnumValues="EchoPulseSequence"			Condition="ImageTypeValue1OriginalOrMixed"
	Name="MultipleSpinEcho"					Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixedAndEchoPulseSequenceNotGradient"
	Name="MultiPlanarExcitation"			Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Name="PhaseContrast"					Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Sequence="VelocityEncodingAcquisitionSequence"		Type="1C"	VM="1-n"	Condition="PhaseContrastIsYes"
		Name="VelocityEncodingDirection"				Type="1"
	SequenceEnd
	Name="TimeOfFlightContrast"				Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Name="ArterialSpinLabelingContrast"		Type="1C"	StringEnumValues="ArterialSpinLabelingContrast"				Condition="ImageTypeValue3ASL"
	Name="SteadyStatePulseSequence"			Type="1C"	StringDefinedTerms="SteadyStatePulseSequence"		Condition="ImageTypeValue1OriginalOrMixed"
	Name="EchoPlanarPulseSequence"			Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Name="SaturationRecovery"				Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Name="SpectrallySelectedSuppression"	Type="1C"	StringDefinedTerms="SpectrallySelectedSuppression"	Condition="ImageTypeValue1OriginalOrMixed"
	Name="OversamplingPhase"				Type="1C"	StringEnumValues="OversamplingPhase"			Condition="ImageTypeValue1OriginalOrMixed"
	Name="GeometryOfKSpaceTraversal"		Type="1C"	StringDefinedTerms="GeometryOfKSpaceTraversal"		Condition="ImageTypeValue1OriginalOrMixed"
	Name="RectilinearPhaseEncodeReordering"	Type="1C"	StringDefinedTerms="RectilinearPhaseEncodeReordering"	Condition="ImageTypeValue1OriginalOrMixedAndRectilinear"
	Name="SegmentedKSpaceTraversal"			Type="1C"	StringEnumValues="SegmentedKSpaceTraversal"		Condition="ImageTypeValue1OriginalOrMixed"
	Name="CoverageOfKSpace"					Type="1C"	StringDefinedTerms="CoverageOfKSpace"			Condition="ImageTypeValue1OriginalOrMixedAnd3D"
	Name="NumberOfKSpaceTrajectories"		Type="1C"	Condition="ImageTypeValue1OriginalOrMixed"
ModuleEnd

Module="MRSpectroscopy"
	InvokeMacro="MRImageAndSpectroscopyInstanceMacro"
	Name="ImageType"						Type="1"	VM="4"
	Verify="ImageType"									ValueSelector="0"	StringEnumValues="CommonEnhancedImageType1"
	Verify="ImageType"									ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
	Verify="ImageType"									ValueSelector="2"	StringDefinedTerms="EnhancedMRSpectroscopyImageAndFrameType3"
	Verify="ImageType"									ValueSelector="3"	StringDefinedTerms="EnhancedMRSpectroscopyImageType4"
	InvokeMacro="MRSpectroscopyDescriptionImageLevelMacro"
	Name="TransmitterFrequency"				Type="1C"	Condition="ImageTypeValue1Original"
	Name="SpectralWidth"					Type="1C"	Condition="ImageTypeValue1OriginalOrMixed"
	Name="ChemicalShiftReference"			Type="1C"	Condition="ImageTypeValue1OriginalOrMixed"
	Name="VolumeLocalizationTechnique"		Type="1C"	StringDefinedTerms="VolumeLocalizationTechnique"	Condition="ImageTypeValue1OriginalOrMixed"
	Sequence="VolumeLocalizationSequence"	Type="1C"	VM="1-n"	Condition="VolumeLocalizationTechniqueNotNone"
		Name="SlabThickness"				Type="1"
		Name="SlabOrientation"				Type="1"
		Name="MidSlabPosition"				Type="1"
	SequenceEnd
	Name="Decoupling"						Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Name="DecoupledNucleus"					Type="1C"	StringDefinedTerms="DecoupledNucleus"			Condition="DecouplingIsYes"
	Name="DecouplingFrequency"				Type="1C"								Condition="DecouplingIsYes"
	Name="DecouplingMethod"					Type="1C"	StringDefinedTerms="DecouplingMethod"			Condition="DecouplingIsYes"
	Name="DecouplingChemicalShiftReference"	Type="1C"								Condition="DecouplingIsYes"
	Name="TimeDomainFiltering"				Type="1C"	StringDefinedTerms="TimeDomainFiltering"		Condition="ImageTypeValue1OriginalOrMixed"
	Name="NumberOfZeroFills"				Type="1C"								Condition="ImageTypeValue1OriginalOrMixed"
	Name="BaselineCorrection"				Type="1C"	StringDefinedTerms="BaselineCorrection"			Condition="ImageTypeValue1OriginalOrMixed"
	Name="FrequencyCorrection"				Type="1C"	StringDefinedTerms="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Name="FirstOrderPhaseCorrection"		Type="1C"	StringDefinedTerms="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Name="WaterReferencedPhaseCorrection"	Type="1C"	StringDefinedTerms="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
ModuleEnd

Module="MRSpectroscopyPulseSequence"
	Name="PulseSequenceName"				Type="1C"	Condition="ImageTypeValue1OriginalOrMixed"
	Name="MRSpectroscopyAcquisitionType"	Type="1C"	StringDefinedTerms="MRSpectroscopyAcquisitionType"	Condition="ImageTypeValue1OriginalOrMixed"
	Name="EchoPulseSequence"				Type="1C"	StringEnumValues="EchoPulseSequence"			Condition="ImageTypeValue1OriginalOrMixed"
	Name="MultipleSpinEcho"					Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixedAndEchoPulseSequenceNotGradient"
	Name="MultiPlanarExcitation"			Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Name="SteadyStatePulseSequence"			Type="1C"	StringDefinedTerms="SteadyStatePulseSequence"		Condition="ImageTypeValue1OriginalOrMixed"
	Name="EchoPlanarPulseSequence"			Type="1C"	StringEnumValues="YesNoFull"				Condition="ImageTypeValue1OriginalOrMixed"
	Name="SpectrallySelectedSuppression"	Type="1C"	StringDefinedTerms="SpectrallySelectedSuppression"	Condition="ImageTypeValue1OriginalOrMixed"
	Name="GeometryOfKSpaceTraversal"		Type="1C"	StringDefinedTerms="GeometryOfKSpaceTraversal"		Condition="ImageTypeValue1OriginalOrMixed"
	Name="RectilinearPhaseEncodeReordering"	Type="1C"	StringDefinedTerms="RectilinearPhaseEncodeReordering"	Condition="ImageTypeValue1OriginalOrMixedAndRectilinear"
	Name="SegmentedKSpaceTraversal"			Type="1C"	StringEnumValues="SegmentedKSpaceTraversal"		Condition="ImageTypeValue1OriginalOrMixed"
	Name="CoverageOfKSpace"					Type="1C"	StringDefinedTerms="CoverageOfKSpace"	Condition="ImageTypeValue1OriginalOrMixedAndSpectroscopyVolume"
	Name="NumberOfKSpaceTrajectories"		Type="1C"	Condition="ImageTypeValue1OriginalOrMixed"
ModuleEnd

Module="MRSpectroscopyData"
	Name="Rows"								Type="1"	NotZeroError=""
	Name="Columns"							Type="1"	NotZeroError=""
	Name="DataPointRows"					Type="1"	NotZeroError=""
	Name="DataPointColumns"					Type="1"	NotZeroError=""
	Name="DataRepresentation"				Type="1"	StringEnumValues="MRSpectroscopyDataRepresentation"
	Name="SignalDomainColumns"				Type="1"	StringEnumValues="SpectroscopySignalDomain"
	Name="SignalDomainRows"					Type="1C"	StringEnumValues="SpectroscopySignalDomain"	Condition="DataPointRowsGreaterThanOne"
	Name="FirstOrderPhaseCorrectionAngle"	Type="1C"							Condition="FirstOrderPhaseCorrectionIsYes"
	Name="SpectroscopyData"					Type="1"
ModuleEnd

Module="RawData"
	Name="InstanceNumber"							Type="2"
	Name="ContentDate"								Type="1"
	Name="ContentTime"								Type="1"
	Name="AcquisitionDateTime"						Type="3"
	Name="ContentLabel"								Type="3"
	Name="ContentDescription"						Type="3"
	Sequence="ConceptNameCodeSequence"				Type="3"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="ImageLaterality"							Type="3"	StringEnumValues="ImageLaterality"
	Name="CreatorVersionUID"						Type="1"
	Sequence="ReferencedInstanceSequence"			Type="3"	VM="1-n"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"	Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="MRSeries"
	Name="Modality"										Type="1"	StringEnumValues="MRModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd


Module="MultiFrameFunctionalGroupsForLegacyConvertedEnhancedMRImage"
	Sequence="SharedFunctionalGroupsSequence"				Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"			Condition="PixelValueTransformationSequenceOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="MRImageFrameTypeMacro"					Condition="MRImageFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"					Condition="TemporalPositionMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="UnassignedSharedConvertedAttributesMacro"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"				Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"			Condition="PixelValueTransformationSequenceOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"			Condition="RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRImageFrameTypeMacro"					Condition="MRImageFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"					Condition="TemporalPositionMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="UnassignedPerFrameConvertedAttributesMacro"
		InvokeMacro="ImageFrameConversionSourceMacro"		Condition="ImageFrameConversionSourceMacroPresentInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd


Module="MultiFrameFunctionalGroupsForPrivatePixelMedLegacyConvertedEnhancedMRImage"
	Sequence="SharedFunctionalGroupsSequence"				Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"			Condition="PixelValueTransformationSequenceOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="MRImageFrameTypeMacro"					Condition="MRImageFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="UnassignedSharedConvertedAttributesMacro"
		InvokeMacro="ImageFrameConversionSourceMacro"		Condition="ConversionSourceAttributesSequenceNotInPerFrameFunctionalGroupSequence"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"				Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"			Condition="PixelValueTransformationSequenceOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="MRImageFrameTypeMacro"					Condition="MRImageFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="UnassignedPerFrameConvertedAttributesMacro"
		InvokeMacro="ImageFrameConversionSourceMacro"		Condition="ConversionSourceAttributesSequenceNotInSharedFunctionalGroupSequence"
	SequenceEnd
ModuleEnd


Module="TractographyResultsSeries"
	Name="Modality"										Type="1"	StringEnumValues="MRModality"
	Name="SeriesNumber"									Type="1"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="TractographyResults"
	InvokeMacro="ContentIdentificationMacro"
	Name="ContentDate"									Type="1"
	Name="ContentTime"									Type="1"
	Sequence="TrackSetSequence"							Type="1"	VM="1-n"
		Name="TrackSetNumber"							Type="1"
		Name="TrackSetLabel"							Type="1"
		Name="TrackSetDescription"						Type="3"
		Sequence="TrackSetAnatomicalTypeCodeSequence"	Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
			Sequence="ModifierCodeSequence"				Type="3"	VM="1-n"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
		SequenceEnd
		Sequence="TrackSequence"						Type="1"	VM="1-n"
			Name="PointCoordinatesData"					Type="1"
			Name="RecommendedDisplayCIELabValueList"	Type="1C"	Condition="NeedRecommendedDisplayCIELabValueListInTrackSequence"
			Name="RecommendedDisplayCIELabValue"		Type="1C"	Condition="NeedRecommendedDisplayCIELabValueInTrackSequence"
		SequenceEnd
		Name="RecommendedDisplayCIELabValue"			Type="1C"	Condition="NeedRecommendedDisplayCIELabValueInTrackSetSequence"
		Name="RecommendedLineThickness"					Type="3"
		Sequence="MeasurementsSequence"					Type="3"	VM="1-n"
			Sequence="ConceptNameCodeSequence"			Type="1"	VM="1"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Sequence="MeasurementUnitsCodeSequence"		Type="1"	VM="1"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Sequence="MeasurementValuesSequence"		Type="1"	VM="1-n"
				Name="FloatingPointValues"				Type="1"
				Name="TrackPointIndexList"				Type="1C"	NoCondition=""
			SequenceEnd
		SequenceEnd
		Sequence="TrackStatisticsSequence"				Type="3"	VM="1-n"
			Sequence="ConceptNameCodeSequence"			Type="1"	VM="1"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Sequence="ModifierCodeSequence"				Type="1"	VM="1"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Sequence="MeasurementUnitsCodeSequence"		Type="1"	VM="1"
				InvokeMacro="CodeSequenceMacro"
			SequenceEnd
			Name="FloatingPointValues"					Type="1"
		SequenceEnd
		Sequence="TrackSetStatisticsSequence"			Type="3"	VM="1-n"
			InvokeMacro="TableSummaryStatisticsMacro"
		SequenceEnd
		Sequence="DiffusionAcquisitionCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="DiffusionModelCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="TrackingAlgorithmIdentificationSequence"	Type="1"	VM="1-n"
			InvokeMacro="AlgorithmIdentificationMacro"
		SequenceEnd
	SequenceEnd

	Sequence="ReferencedInstanceSequence"				Type="1C"	VM="1-n"	NoCondition=""
		InvokeMacro="ImageSOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

DefineMacro="TableSummaryStatisticsMacro"
	Sequence="ConceptNameCodeSequence"							Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="ModifierCodeSequence"								Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Sequence="MeasurementUnitsCodeSequence"						Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="FloatingPointValue"									Type="1"
MacroEnd



DefineMacro="CTFrameVOILUTMacro" InformationEntity="FunctionalGroup"
	Sequence="FrameVOILUTSequence"				Type="1"	VM="1"
		Name="WindowCenter"						Type="1" 
		Name="WindowWidth"						Type="1"	NotZeroError=""
		Verify="WindowWidth"								Condition="WindowWidthIsNegative"	ThenErrorMessage="Not permitted to be negative" ShowValueWithMessage="true"
		Name="WindowCenterWidthExplanation"		Type="3"	StringDefinedTerms="EnhancedCTWindowCenterWidthExplanation"
		Name="VOILUTFunction"					Type="3"	StringDefinedTerms="VOILUTFunction"
	SequenceEnd
MacroEnd

Module="CTSeries"
	Name="Modality"										Type="1"	StringEnumValues="CTModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="EnhancedCTImage"
	Name="ImageType"										Type="1"	VM="4"
	Verify="ImageType"													ValueSelector="0"	StringEnumValues="CommonEnhancedImageType1"
	Verify="ImageType"													ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
	Verify="ImageType"													ValueSelector="2"	StringDefinedTerms="EnhancedCTImageAndFrameType3"
	Verify="ImageType"													ValueSelector="3"	StringDefinedTerms="EnhancedCTImageType4"
	Name="MultienergyCTAcquisition"							Type="3"	StringEnumValues="YesNoFull"
	InvokeMacro="CommonCTMRImageDescriptionImageLevelMacro"
	Name="AcquisitionNumber"								Type="3"
	Name="AcquisitionDateTime"								Type="1C"	Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedCT" mbpo="true"
	Name="AcquisitionDuration"								Type="2C"	Condition="ImageTypeValue1OriginalOrMixedAndNotLegacyConvertedCT" mbpo="true"
	Sequence="ReferencedRawDataSequence"					Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedWaveformSequence"					Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedImageEvidenceSequence"				Type="1C"	VM="1-n"	Condition="ReferencedImageSequenceIsPresentInFunctionalGroups"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="SourceImageEvidenceSequence"					Type="1C"	VM="1-n"	Condition="SourceImageSequenceIsPresentInFunctionalGroups"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedPresentationStateSequence"	Type="1C"	VM="1-n"	NoCondition=""	# real world
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Name="SamplesPerPixel"									Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"						Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"									Type="1"	BinaryEnumValues="BitsAre16"
	Name="BitsStored"										Type="1"	BinaryEnumValues="BitsAre12Or16"
	Name="HighBit"											Type="1"	BinaryEnumValues="BitsAre11Or15"
	Name="ContentQualification"								Type="1C"	StringEnumValues="ContentQualification"		Condition="NotLegacyConvertedCT" mbpo="true"
	Name="ImageComments"									Type="3"
	Name="BurnedInAnnotation"								Type="1C"	StringEnumValues="NoFull"					Condition="NotLegacyConvertedCT" mbpo="true"
	Name="RecognizableVisualFeatures"						Type="3"	StringEnumValues="YesNoFull"
	Name="LossyImageCompression"							Type="1C"	StringEnumValues="LossyImageCompression"	Condition="NotLegacyConvertedCT" mbpo="true"
	Name="LossyImageCompressionRatio"						Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"						Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"								Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="PresentationLUTShape"								Type="1"	StringEnumValues="IdentityPresentationLUTShape"
	Sequence="IconImageSequence"							Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
	InvokeMacro="OptionalViewAndSliceProgressionDirectionMacro"
	Name="IsocenterPosition"								Type="3"
	InvokeMacro="RTEquipmentCorrelationMacro"
ModuleEnd

DefineMacro="CTImageFrameTypeMacro" InformationEntity="FunctionalGroup"
	Sequence="CTImageFrameTypeSequence"		Type="1"	VM="1"
		Name="FrameType"					Type="1"	VM="4"
		Verify="FrameType"								ValueSelector="0"	StringEnumValues="CommonEnhancedFrameType1"
		Verify="FrameType"								ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
		Verify="FrameType"								ValueSelector="2"	StringDefinedTerms="EnhancedCTImageAndFrameType3"
		Verify="FrameType"								ValueSelector="3"	StringDefinedTerms="EnhancedCTFrameType4"
		InvokeMacro="CommonCTMRImageDescriptionFrameLevelMacro"
	SequenceEnd
MacroEnd

DefineMacro="CTAcquisitionTypeMacro" InformationEntity="FunctionalGroup"
	Sequence="CTAcquisitionTypeSequence"			Type="1"	VM="1"
		Name="AcquisitionType"						Type="1C"	StringDefinedTerms ="CTAcquisitionType"		Condition="Always"	# ORIGINAL mbpo
		Name="TubeAngle"							Type="1C"	Condition="AcquisitionTypeConstantAngle"				# and ORIGINAL mbpo
		Name="ConstantVolumeFlag"					Type="1C"	StringDefinedTerms ="YesNoFull"			Condition="Always"	# ORIGINAL mbpo
		Name="FluoroscopyFlag"						Type="1C"	StringDefinedTerms ="YesNoFull"			Condition="Always"	# ORIGINAL mbpo
	SequenceEnd
MacroEnd

DefineMacro="CTAcquisitionDetailsMacro" InformationEntity="FunctionalGroup"
	Sequence="CTAcquisitionDetailsSequence"			Type="1"	VM="1-n"
		Name="ReferencedPathIndex"					Type="1C"	Condition="IsMultienergyCTAcquisition"
		Name="RotationDirection"					Type="1C"	StringEnumValues="RotationDirection"		NoCondition=""		# :( cannot check since in sibling functional groups: Frame Type Value 1 of this frame is ORIGINAL and AcquisitionType not CONSTANT_ANGLE; mbpo only if DERIVED and same AcquisitionType
		Name="RevolutionTime"						Type="1C"	NoCondition=""	NotZeroWarning=""								# :( cannot check since in sibling functional groups: Frame Type Value 1 of this frame is ORIGINAL and AcquisitionType not CONSTANT_ANGLE; mbpo only if DERIVED and same AcquisitionType
		Name="SingleCollimationWidth"				Type="1C"	Condition="Always"	NotZeroWarning=""		# ORIGINAL mbpo
		Name="TotalCollimationWidth"				Type="1C"	Condition="Always"	NotZeroWarning=""		# ORIGINAL mbpo
		Name="TableHeight"							Type="1C"	Condition="Always"							# ORIGINAL mbpo
		Name="GantryDetectorTilt"					Type="1C"	Condition="Always"							# ORIGINAL mbpo
		Name="DataCollectionDiameter"				Type="1C"	Condition="Always"	NotZeroWarning=""		# ORIGINAL mbpo
	SequenceEnd
	Verify="CTAcquisitionDetailsSequence"						Condition="CTAcquisitionDetailsSequenceNotOneItemAndNotMultienergyAcquisition"	ThenErrorMessage="Only a single Item is permitted if not a multi-energy acquisition"
MacroEnd

DefineMacro="CTTableDynamicsMacro" InformationEntity="FunctionalGroup"
	Sequence="CTTableDynamicsSequence"			Type="1"	VM="1"
		Name="TableSpeed"						Type="1C"	NoCondition=""	NotZeroWarning=""	# :( cannot check since in sibling functional groups: Frame Type Value 1 of this frame is ORIGINAL and AcquisitionType SPIRAL or CONSTANT_ANGLE; mbpo only if DERIVED and same AcquisitionType
		Name="TableFeedPerRotation"				Type="1C"	NoCondition=""	NotZeroWarning=""	# :( cannot check since in sibling functional groups: Frame Type Value 1 of this frame is ORIGINAL and AcquisitionType SPIRAL or CONSTANT_ANGLE; mbpo only if DERIVED and same AcquisitionType
		Name="SpiralPitchFactor"				Type="1C"	NoCondition=""	NotZeroWarning=""	# :( cannot check since in sibling functional groups: Frame Type Value 1 of this frame is ORIGINAL and AcquisitionType SPIRAL or CONSTANT_ANGLE; mbpo only if DERIVED and same AcquisitionType
	SequenceEnd
MacroEnd

DefineMacro="CTPositionMacro" InformationEntity="FunctionalGroup"
	Sequence="CTPositionSequence"					Type="1"	VM="1"
		Name="TablePosition"						Type="1C"	Condition="Always"							# ORIGINAL mbpo
		Name="DataCollectionCenterPatient"			Type="1C"	Condition="Always"							# ORIGINAL mbpo
		Name="ReconstructionTargetCenterPatient"	Type="1C"	Condition="Always"							# ORIGINAL mbpo
	SequenceEnd
MacroEnd

DefineMacro="CTGeometryMacro" InformationEntity="FunctionalGroup"
	Sequence="CTGeometrySequence"					Type="1"	VM="1-n"
		Name="ReferencedPathIndex"					Type="1C"	Condition="IsMultienergyCTAcquisition"
		Name="DistanceSourceToDetector"				Type="1C"	Condition="Always"	NotZeroWarning=""							# ORIGINAL mbpo
		Name="DistanceSourceToDataCollectionCenter"	Type="1C"	Condition="Always"	NotZeroWarning=""							# ORIGINAL mbpo
	SequenceEnd
	Verify="CTGeometrySequence"						Condition="CTGeometrySequenceNotOneItemAndNotMultienergyAcquisition"	ThenErrorMessage="Only a single Item is permitted if not a multi-energy acquisition"
MacroEnd

DefineMacro="CTReconstructionMacro" InformationEntity="FunctionalGroup"
	Sequence="CTReconstructionSequence"			Type="1"	VM="1"
		Name="ReconstructionAlgorithm"			Type="1C"	StringDefinedTerms ="CTReconstructionAlgorithm"	Condition="Always"	# ORIGINAL mbpo
		Name="ConvolutionKernel"				Type="1C"	Condition="Always"							# ORIGINAL mbpo
		Name="ConvolutionKernelGroup"			Type="1C"	StringDefinedTerms ="CTConvolutionKernelGroup"	Condition="ConvolutionKernelIsPresent"
		Name="ReconstructionDiameter"			Type="1C"	Condition="ReconstructionFieldOfViewAbsent"	NotZeroWarning=""				# ORIGINAL mbpo
		Name="ReconstructionFieldOfView"		Type="1C"	Condition="ReconstructionDiameterAbsent"	NotZeroWarning=""				# ORIGINAL mbpo
		Name="ReconstructionPixelSpacing"		Type="1C"	Condition="Always"	NotZeroWarning=""							# ORIGINAL mbpo
		Name="ReconstructionAngle"				Type="1C"	Condition="Always"							# ORIGINAL mbpo
		Name="ImageFilter"						Type="1C"	Condition="Always"							# ORIGINAL mbpo
	SequenceEnd
MacroEnd

DefineMacro="CTExposureMacro" InformationEntity="FunctionalGroup"
	Sequence="CTExposureSequence"				Type="1"	VM="1-n"
		Name="ReferencedPathIndex"					Type="1C"	Condition="IsMultienergyCTAcquisition"
		Name="ExposureTimeInms"					Type="1C"	Condition="Always"	NotZeroWarning=""							# ORIGINAL frame (or image if multi-energy) )mbpo
		Name="XRayTubeCurrentInmA"				Type="1C"	Condition="Always"	NotZeroWarning=""							# ORIGINAL mbpo
		Name="ExposureInmAs"					Type="1C"	Condition="Always"	NotZeroWarning=""							# ORIGINAL mbpo
		Name="ExposureModulationType"			Type="1C"	StringDefinedTerms ="CTExposureModulationType"	Condition="Always"	# ORIGINAL mbpo
		Name="EstimatedDoseSaving"				Type="2C"	Condition="ExposureModulationTypeIsNotNone"	NotZeroWarning=""				# ORIGINAL mbpo
		Name="CTDIvol"							Type="2C"	NoCondition=""	NotZeroWarning=""
		Verify="CTDIvol"									Condition="CTDIvolIsPresentButCTDIPhantomTypeCodeSequenceIsNot"   ThenWarningMessage="CTDIvol is present but it is uninterpretable without CTDIPhantomTypeCodeSequence, which is absent"
		Sequence="CTDIPhantomTypeCodeSequence"	Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"					DefinedContextID="4052"
		SequenceEnd
		Name="WaterEquivalentDiameter"			Type="3"	NotZeroWarning=""
		Sequence="WaterEquivalentDiameterCalculationMethodCodeSequence"	Type="1C"	VM="1"	Condition="WaterEquivalentDiameterIsPresent"
			InvokeMacro="CodeSequenceMacro"					DefinedContextID="10024"
		SequenceEnd
		Name="ImageAndFluoroscopyAreaDoseProduct"	Type="3"	NotZeroWarning=""
	SequenceEnd
	Verify="CTExposureSequence"						Condition="CTExposureSequenceNotOneItemAndNotMultienergyAcquisition"	ThenErrorMessage="Only a single Item is permitted if not a multi-energy acquisition"
MacroEnd

DefineMacro="CTXRayDetailsMacro" InformationEntity="FunctionalGroup"
	Sequence="CTXRayDetailsSequence"			Type="1"	VM="1-n"
		Name="KVP"								Type="1C"	Condition="Always"	NotZeroWarning=""							# ORIGINAL mbpo
		Name="FocalSpots"						Type="1C"	Condition="Always"							# ORIGINAL mbpo
		Name="FilterType"						Type="1C"	StringDefinedTerms ="CTFilterType"	Condition="Always"	# ORIGINAL mbpo
		Name="FilterMaterial"					Type="1C"	StringDefinedTerms ="CTFilterMaterial"	Condition="Always"	# ORIGINAL mbpo
		Name="CalciumScoringMassFactorPatient"	Type="3"	NotZeroWarning=""
		Name="CalciumScoringMassFactorDevice"	Type="3"	NotZeroWarning=""
		Name="EnergyWeightingFactor"			Type="1C"	NotZeroWarning=""	NoCondition="" mbpo="true"	# FrameTypeValue4IsEnergyProportionalWeighting ... too hard :(
	SequenceEnd
	Verify="CTXRayDetailsSequence"						Condition="CTXRayDetailsSequenceNotOneItemAndNotMultienergyAcquisition"	ThenErrorMessage="Only a single Item is permitted if not a multi-energy acquisition"
MacroEnd

DefineMacro="CTPixelValueTransformationMacro" InformationEntity="FunctionalGroup"
	Sequence="PixelValueTransformationSequence"		Type="1"	VM="1"
		Name="RescaleIntercept"						Type="1" 
		Name="RescaleSlope"							Type="1"	NotZeroError="" 
		Name="RescaleType"							Type="1" 	StringEnumValues="RescaleTypeHounsfieldUnits"	#actually only if not localizer :(
	SequenceEnd
MacroEnd

DefineMacro="CTAdditionalXRaySourceMacro" InformationEntity="FunctionalGroup"
	Sequence="CTAdditionalXRaySourceSequence"		Type="1"	VM="1-n"
		Name="KVP"								Type="1"	NotZeroWarning=""
		Name="XRayTubeCurrentInmA"				Type="1"	NotZeroWarning=""
		Name="DataCollectionDiameter"			Type="1"	NotZeroWarning=""
		Name="FocalSpots"						Type="1"
		Name="FilterType"						Type="1"	StringDefinedTerms ="CTFilterType"
		Name="FilterMaterial"					Type="1"	StringDefinedTerms ="CTFilterMaterial"
		Name="ExposureInmAs"					Type="3"	NotZeroWarning=""
		Name="EnergyWeightingFactor"			Type="1C"	NotZeroWarning=""	NoCondition="" mbpo="true"	# FrameTypeValue4IsEnergyProportionalWeighting ... too hard :(
	SequenceEnd
MacroEnd

DefineMacro="UnassignedSharedConvertedAttributesMacro" InformationEntity="FunctionalGroup"
	Sequence="UnassignedSharedConvertedAttributesSequence"		Type="2"	VM="1"
	SequenceEnd
MacroEnd

DefineMacro="UnassignedPerFrameConvertedAttributesMacro" InformationEntity="FunctionalGroup"
	Sequence="UnassignedPerFrameConvertedAttributesSequence"	Type="2"	VM="1"
	SequenceEnd
MacroEnd

DefineMacro="ImageFrameConversionSourceMacro" InformationEntity="FunctionalGroup"
	Sequence="ConversionSourceAttributesSequence"				Type="1"	VM="1-n"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
	SequenceEnd
MacroEnd

Module="MultiFrameFunctionalGroupsForEnhancedCTImage"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTFrameVOILUTMacro"		Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="NeedRealWorldValueMappingMacroInSharedFunctionalGroupSequenceIfMultienergy"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="NeedRespiratorySynchronizationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"		Condition="IrradiationEventIdentificationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTImageFrameTypeMacro"		Condition="CTImageFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTAcquisitionTypeMacro"		Condition="NeedCTAcquisitionTypeMacroInSharedFunctionalGroupSequence"
		InvokeMacro="CTAcquisitionDetailsMacro"		Condition="NeedCTAcquisitionDetailsMacroInSharedFunctionalGroupSequence"
		InvokeMacro="CTTableDynamicsMacro"		Condition="NeedCTTableDynamicsMacroInSharedFunctionalGroupSequence"
		InvokeMacro="CTPositionMacro"			Condition="NeedCTPositionMacroInSharedFunctionalGroupSequence"
		InvokeMacro="CTGeometryMacro"			Condition="NeedCTGeometryMacroInSharedFunctionalGroupSequence"
		InvokeMacro="CTReconstructionMacro"		Condition="NeedCTReconstructionMacroInSharedFunctionalGroupSequence"
		InvokeMacro="CTExposureMacro"			Condition="NeedCTExposureMacroInSharedFunctionalGroupSequence"
		InvokeMacro="CTXRayDetailsMacro"		Condition="NeedCTXRayDetailsMacroInSharedFunctionalGroupSequence"
		InvokeMacro="CTPixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTAdditionalXRaySourceMacro"		Condition="CTAdditionalXRaySourceMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MultienergyCTProcessingMacro"		Condition="MultienergyCTProcessingMacroInSharedFunctionalGroupSequence"
		InvokeMacro="MultienergyCTCharacteristicsMacro"		Condition="MultienergyCTCharacteristicsMacroInSharedFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"			Condition="TemporalPositionMacroOKInSharedFunctionalGroupSequence"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="CTFrameVOILUTMacro"		Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="NeedRealWorldValueMappingMacroInPerFrameFunctionalGroupSequenceIfMultienergy"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="NeedRespiratorySynchronizationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"		Condition="IrradiationEventIdentificationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="CTImageFrameTypeMacro"		Condition="CTImageFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="CTAcquisitionTypeMacro"		Condition="NeedCTAcquisitionTypeMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTAcquisitionDetailsMacro"		Condition="NeedCTAcquisitionDetailsMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTTableDynamicsMacro"		Condition="NeedCTTableDynamicsMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTPositionMacro"			Condition="NeedCTPositionMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTGeometryMacro"			Condition="NeedCTGeometryMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTReconstructionMacro"		Condition="NeedCTReconstructionMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTExposureMacro"			Condition="NeedCTExposureMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTXRayDetailsMacro"		Condition="NeedCTXRayDetailsMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTPixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="CTAdditionalXRaySourceMacro"		Condition="CTAdditionalXRaySourceMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MultienergyCTProcessingMacro"		Condition="MultienergyCTProcessingMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="MultienergyCTCharacteristicsMacro"		Condition="MultienergyCTCharacteristicsMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"			Condition="TemporalPositionMacroOKInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="MultiFrameFunctionalGroupsForLegacyConvertedEnhancedCTImage"
	Sequence="SharedFunctionalGroupsSequence"				Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CTImageFrameTypeMacro"					Condition="CTImageFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTPixelValueTransformationMacro"		Condition="PixelValueTransformationSequenceOKInSharedFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"					Condition="TemporalPositionMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="UnassignedSharedConvertedAttributesMacro"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"				Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"						Condition="FrameVOILUTMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTImageFrameTypeMacro"					Condition="CTImageFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="CTPixelValueTransformationMacro"		Condition="PixelValueTransformationSequenceOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="TemporalPositionMacro"					Condition="TemporalPositionMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="UnassignedPerFrameConvertedAttributesMacro"
		InvokeMacro="ImageFrameConversionSourceMacro"		Condition="ImageFrameConversionSourceMacroPresentInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd


Module="MultiFrameFunctionalGroupsForPrivatePixelMedLegacyConvertedEnhancedCTImage"
	Sequence="SharedFunctionalGroupsSequence"				Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CTFrameVOILUTMacro"					Condition="FrameVOILUTSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CTImageFrameTypeMacro"					Condition="CTImageFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTPixelValueTransformationMacro"		Condition="PixelValueTransformationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="UnassignedSharedConvertedAttributesMacro"
		InvokeMacro="ImageFrameConversionSourceMacro"		Condition="ConversionSourceAttributesSequenceNotInPerFrameFunctionalGroupSequence"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"				Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"					Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"					Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"					Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"					Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"					Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"			Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"						Condition="FrameAnatomyMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTFrameVOILUTMacro"					Condition="FrameVOILUTSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"				Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"	Condition="IrradiationEventIdentificationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CTImageFrameTypeMacro"					Condition="CTImageFrameTypeSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="CTPixelValueTransformationMacro"		Condition="PixelValueTransformationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="UnassignedPerFrameConvertedAttributesMacro"
		InvokeMacro="ImageFrameConversionSourceMacro"		Condition="ConversionSourceAttributesSequenceNotInSharedFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="MultienergyCTImage"
	Sequence="MultienergyCTAcquisitionSequence"				Type="1"	VM="1"
		Name="MultienergyAcquisitionDescription"			Type="3"
		InvokeMacro="MultienergyCTXRaySourceMacro"
		InvokeMacro="MultienergyCTXRayDetectorMacro"
		InvokeMacro="MultienergyCTPathMacro"
		InvokeMacro="CTExposureMacro"
		InvokeMacro="CTXRayDetailsMacro"
		InvokeMacro="CTAcquisitionDetailsMacro"
		InvokeMacro="CTGeometryMacro"
	SequenceEnd
	Sequence="MultienergyCTProcessingSequence"				Type="3"	VM="1"
		InvokeMacro="MultienergyCTProcessingMacro"
	SequenceEnd
	Sequence="MultienergyCTCharacteristicsSequence"			Type="1C"	VM="1"	Condition="ImageTypeValue4IsVMI"	mbpo="true"
		InvokeMacro="MultienergyCTCharacteristicsMacro"
	SequenceEnd
ModuleEnd

DefineMacro="MultienergyCTXRaySourceMacro"
	Sequence="MultienergyCTXRaySourceSequence"				Type="1"	VM="1-n"
		Name="XRaySourceIndex"								Type="1"
		Name="XRaySourceID"									Type="1"
		Name="MultienergySourceTechnique"					Type="1"	StringDefinedTerms ="MultienergySourceTechnique"
		Name="SourceStartDateTime"							Type="1"
		Name="SourceEndDateTime"							Type="1"
		Name="SwitchingPhaseNumber"							Type="1C"	Condition="MultienergySourceTechniqueIsSWITCHING_SOURCE"
		Name="SwitchingPhaseNominalDuration"				Type="3"
		Name="SwitchingPhaseTransitionDuration"				Type="3"
		Name="GeneratorPower"								Type="3"
	SequenceEnd
MacroEnd

DefineMacro="MultienergyCTXRayDetectorMacro"
	Sequence="MultienergyCTXRayDetectorSequence"			Type="1"	VM="1-n"
		Name="XRayDetectorIndex"							Type="1"
		Name="XRayDetectorID"								Type="1"
		Name="MultienergyDetectorType"						Type="1"	StringDefinedTerms ="MultienergyDetectorType"
		Name="XRayDetectorLabel"							Type="3"
		Name="NominalMaxEnergy"								Type="1C"	Condition="MultienergyDetectorTypeIsPHOTON_COUNTING"
		Name="NominalMinEnergy"								Type="1C"	Condition="MultienergyDetectorTypeIsPHOTON_COUNTING"
		Name="EffectiveBinEnergy"							Type="3"
	SequenceEnd
MacroEnd

DefineMacro="MultienergyCTPathMacro"
	Sequence="MultienergyCTPathSequence"					Type="1"	VM="2-n"
		Name="MultienergyCTPathIndex"						Type="1"
		Name="ReferencedXRaySourceIndex"					Type="1"
		Name="ReferencedXRayDetectorIndex"					Type="1"
	SequenceEnd
MacroEnd

DefineMacro="MultienergyCTCharacteristicsMacro"
	Name="MonoenergeticEnergyEquivalent"					Type="1C"	Condition="ImageTypeValue4IsVMI"	mbpo="true"
	Sequence="DerivationAlgorithmSequence"					Type="3"	VM="1-n"
		InvokeMacro="AlgorithmIdentificationMacro"
	SequenceEnd
	Sequence="PerformedProcessingParametersSequence"		Type="3"	VM="1-n"
		InvokeMacro="ContentItemWithModifiersMacro"
	SequenceEnd
MacroEnd

DefineMacro="MultienergyCTProcessingMacro"
	Name="DecompositionMethod"								Type="1"	StringDefinedTerms="DecompositionMethod"
	Name="DecompositionDescription"							Type="3"
	Sequence="DecompositionAlgorithmIdentificationSequence"	Type="3"	VM="1-n"
		InvokeMacro="AlgorithmIdentificationMacro"
	SequenceEnd
	Sequence="DecompositionMaterialSequence"				Type="3"	VM="1"
		Sequence="MaterialCodeSequence"						Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Sequence="MaterialAttenuationSequence"				Type="3"	VM="2-n"
			Name="PhotonEnergy"								Type="1"
			Name="XRayMassAttenuationCoefficient"			Type="1"
		SequenceEnd
	SequenceEnd
MacroEnd

Module="EnhancedMultienergyCTAcquisition"
	InvokeMacro="MultienergyCTXRaySourceMacro"
	InvokeMacro="MultienergyCTXRayDetectorMacro"
	InvokeMacro="MultienergyCTPathMacro"
ModuleEnd
Module="FramePointers"
	Name="RepresentativeFrameNumber"	Type="3"	NotZeroError=""
	Name="FrameNumbersOfInterest"		Type="3"	NotZeroError=""
	Name="FrameOfInterestDescription"	Type="3"
	Name="FrameOfInterestType"			Type="3"	StringDefinedTerms="FrameOfInterestTypeForUS"

ModuleEnd

Module="Mask"
	Sequence="MaskSubtractionSequence"		Type="1"	VM="1-n"
		Name="MaskOperation"				Type="1"	StringDefinedTerms="MaskOperation"
		Name="SubtractionItemID"			Type="1C"	Condition="SOPClassIsEnhancedXAXRF" mbpo="true"
		Name="ApplicableFrameRange"			Type="1C"	Condition="MaskOperationIsRevTID" mbpo="true"
		Name="MaskFrameNumbers"				Type="1C"	Condition="MaskOperationIsAvgSub"	NotZeroError=""
		Name="ContrastFrameAveraging"		Type="3"
		Name="MaskSubPixelShift"			Type="3"
		Name="TIDOffset"					Type="2C"	Condition="MaskOperationIsTIDOrRevTID"
		Name="MaskOperationExplanation"		Type="3"
		Name="MaskSelectionMode"			Type="3"	StringDefinedTerms="MaskSelectionMode"
	SequenceEnd
	Name="RecommendedViewingMode"			Type="2"	StringDefinedTerms="RecommendedViewingMode"

ModuleEnd

Module="DisplayShutter"
	InvokeMacro="DisplayShutterMacro"
ModuleEnd

Module="Device"
	# need to work in the 3 vs. 2C business for device parameters (C.7.6.12.1)
	Sequence="DeviceSequence"		Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"
		Name="Manufacturer"			Type="3"
		Name="ManufacturerModelName"	Type="3"
		Name="DeviceSerialNumber"	Type="3"
		Name="DeviceID"				Type="3"
		Name="DeviceLength"			Type="3"	NotZeroWarning=""
		Name="DeviceDiameter"		Type="3"	NotZeroWarning=""
		Name="DeviceDiameterUnits"	Type="2C"	Condition="DeviceDiameterIsPresent"	StringEnumValues="DeviceDiameterUnits"
		Name="DeviceVolume"			Type="3"	NotZeroWarning=""
		Name="InterMarkerDistance"	Type="3"
		Name="DeviceDescription"	Type="3"
	SequenceEnd
ModuleEnd

Module="Intervention"
	Sequence="InterventionSequence"					Type="3"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"							BaselineContextID="9"
		Name="InterventionStatus"					Type="2"	StringEnumValues="InterventionStatus"
		Sequence="InterventionDrugCodeSequence"		Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"						BaselineContextID="10"
		SequenceEnd
		Name="InterventionDrugStartTime"			Type="3"
		Name="InterventionDrugStopTime"				Type="3"
		Sequence="AdministrationRouteCodeSequence"	Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"						BaselineContextID="11"
		SequenceEnd
		Name="InterventionDescription"				Type="3"
	SequenceEnd
ModuleEnd

Module="XRayImage"
	Name="FrameIncrementPointer"					Type="1C"	Condition="NeedModuleMultiFrame"	TagEnumValues="XRayFrameIncrementPointerValues"
	Name="LossyImageCompression"					Type="1C"	NoCondition=""	StringEnumValues="LossyImageCompression"
	Name="ImageType"								Type="1"	ValueSelector="2"	StringEnumValues="XRayImageTypeValue3"
	Verify="ImageType"								Condition="ImageTypeValue3MissingOrEmpty"	ThenErrorMessage="A value is required for value 3 in XA/XRF Images"
	Name="PixelIntensityRelationship"				Type="1"	StringDefinedTerms="PixelIntensityRelationship"
	Name="SamplesPerPixel"							Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"				Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"							Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"								Type="1"	BinaryEnumValues="BitsAre8Or10Or12Or16"
	Name="HighBit"									Type="1"	BinaryEnumValues="BitsAre7Or9Or11Or15"
	Name="PixelRepresentation"						Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="ScanOptions"								Type="3"	StringDefinedTerms="XRayImageScanOptions"
	InvokeMacro="GeneralAnatomyOptionalMacro"
	Name="RWavePointer"								Type="3"
	Sequence="ReferencedImageSequence"				Type="1C"	VM="1-n"	Condition="ImageTypeValue3BiplaneAOrB" mbpo="true"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"	Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"			DefinedContextID="7201"
		SequenceEnd
	SequenceEnd
	Name="DerivationDescription"					Type="3"
	Name="AcquisitionDeviceProcessingDescription"	Type="3"
	Name="FrameLabelVector"							Type="3"
	Name="FrameDimensionPointer"					Type="3"	TagEnumValues="XAFrameDimensionPointerValues"
	Name="CalibrationImage"							Type="3"	StringEnumValues="YesNoFull"
ModuleEnd

Module="XRayAcquisition"
	Name="KVP"										Type="2"	NotZeroWarning=""
	Name="RadiationSetting"							Type="1"	StringEnumValues="RadiationSetting"
	Name="XRayTubeCurrent"							Type="2C"	Condition="ExposureNotPresent" mbpo="true"	NotZeroWarning=""
	Name="XRayTubeCurrentInuA"						Type="3"	NotZeroWarning=""
	Verify="XRayTubeCurrentInmA"								Condition="XRayTubeCurrentInmAIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <XRayAcquisition> - use XRayTubeCurrent and/or XRayTubeCurrentInuA instead of"
	
	Name="ExposureTime"								Type="2C"	Condition="ExposureNotPresent" mbpo="true"	NotZeroWarning=""
	Name="ExposureTimeInuS"							Type="3"	NotZeroWarning=""
	Verify="ExposureTimeInms"									Condition="ExposureTimeInmsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <XRayAcquisition> - use ExposureTime and/or ExposureTimeInuS instead of"
	
	Name="Exposure"									Type="2C"	Condition="XRayTubeCurrentAndExposureTimeNotPresent" mbpo="true"	NotZeroWarning=""
	Name="ExposureInuAs"							Type="3"	NotZeroWarning=""
	Verify="ExposureInmAs"										Condition="ExposureInmAsIsPresentAndOthersAreNot" ThenErrorMessage="Attribute should not be used with Module <XRayAcquisition> - use Exposure and/or ExposureInuAs instead of"
	
	Name="Grid"										Type="3"	StringDefinedTerms="Grid"
	Name="AveragePulseWidth"						Type="3"	NotZeroWarning=""
	Name="RadiationMode"							Type="3"	StringDefinedTerms="RadiationMode"
	Name="TypeOfFilters"							Type="3"
	Name="IntensifierSize"							Type="3"
	Name="FieldOfViewShape"							Type="3"	StringDefinedTerms="XRayFieldOfViewShape"
	Name="FieldOfViewDimensions"					Type="3"	NotZeroWarning=""
	Name="ImagerPixelSpacing"						Type="3"	NotZeroError=""
	InvokeMacro="BasicPixelSpacingCalibrationMacro"
	Name="FocalSpots"								Type="3"
	Name="ImageAndFluoroscopyAreaDoseProduct"		Type="3"	NotZeroWarning=""
ModuleEnd

DefineMacro="XRayCollimatorDimensionsMacro" InformationEntity="Image"
	Name="CollimatorLeftVerticalEdge"		Type="1C"	Condition="CollimatorShapeIsRectangular"
	Name="CollimatorRightVerticalEdge"		Type="1C"	Condition="CollimatorShapeIsRectangular"
	Name="CollimatorUpperHorizontalEdge"	Type="1C"	Condition="CollimatorShapeIsRectangular"
	Name="CollimatorLowerHorizontalEdge"	Type="1C"	Condition="CollimatorShapeIsRectangular"
	Name="CenterOfCircularCollimator"		Type="1C"	Condition="CollimatorShapeIsCircular"
	Name="RadiusOfCircularCollimator"		Type="1C"	Condition="CollimatorShapeIsCircular"	NotZeroWarning=""
	Name="VerticesOfThePolygonalCollimator"	Type="1C"	Condition="CollimatorShapeIsPolygonal"
MacroEnd

Module="XRayCollimator"
	Name="CollimatorShape"					Type="1"	StringEnumValues="CollimatorShape"
	InvokeMacro="XRayCollimatorDimensionsMacro"
ModuleEnd

Module="XRayTable"
	Name="TableMotion"					Type="2"	StringDefinedTerms="TableMotion"
	Name="TableVerticalIncrement"		Type="2C"	Condition="TableMotionDynamic"
	Name="TableLongitudinalIncrement"	Type="2C"	Condition="TableMotionDynamic"
	Name="TableLateralIncrement"		Type="2C"	Condition="TableMotionDynamic"
	Name="TableAngle"					Type="3"
ModuleEnd

Module="XAPositioner"
	Name="DistanceSourceToPatient"					Type="3"	NotZeroWarning=""
	Name="DistanceSourceToDetector"					Type="3"	NotZeroWarning=""
	Name="EstimatedRadiographicMagnificationFactor"	Type="3"	NotZeroWarning=""
	Name="PositionerMotion"							Type="2C"	StringDefinedTerms="PositionerMotion"		Condition="NumberOfFramesGreaterThanOne" mbpo="true"
	Verify="PositionerMotion"									StringEnumValues="PositionerMotionStatic"	Condition="PositionerMotionIsPresentAndNumberOfFramesIsAbsentOrOne"		
	Name="PositionerPrimaryAngle"					Type="2"
	Name="PositionerSecondaryAngle"					Type="2"
	Name="PositionerPrimaryAngleIncrement"			Type="2C"	Condition="PositionerMotionDynamic"	NotZeroWarning=""
	Name="PositionerSecondaryAngleIncrement"		Type="2C"	Condition="PositionerMotionDynamic"	NotZeroWarning=""
	Name="DetectorPrimaryAngle"						Type="3"
	Name="DetectorSecondaryAngle"					Type="3"

ModuleEnd

Module="XRFPositioner"
	Name="DistanceSourceToDetector"					Type="3"	NotZeroWarning=""
	Name="DistanceSourceToPatient"					Type="3"	NotZeroWarning=""
	Name="EstimatedRadiographicMagnificationFactor"	Type="3"	NotZeroWarning=""
	Name="ColumnAngulation"							Type="3"
ModuleEnd

Module="XRayTomographyAcquisition"
	Name="TomoLayerHeight"							Type="1"
	Name="TomoAngle"								Type="3"
	Name="TomoTime"									Type="3"
	Name="TomoType"									Type="3"	StringDefinedTerms="TomoType"
	Name="TomoClass"								Type="3"	StringDefinedTerms="TomoClass"
	Name="NumberOfTomosynthesisSourceImages"		Type="3"
ModuleEnd

# enhanced XA/XRF stuff ...

Module="XAXRFSeries"
	Name="Modality"										Type="1"	StringEnumValues="EnhancedXAXRFModality"
	Name="SeriesNumber"									Type="1"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
ModuleEnd

Module="EnhancedXAXRFImage"
	Name="ImageType"										Type="1"	VM="4-n"
	Verify="ImageType"													ValueSelector="0"	StringEnumValues="EnhancedXAXRFImageType1"
	Verify="ImageType"													ValueSelector="1"	StringEnumValues="EnhancedXAXRFImageType2"
	Verify="ImageType"													ValueSelector="2"	StringDefinedTerms="EnhancedXAXRFImageType3"
	Verify="ImageType"													ValueSelector="3"	StringEnumValues="EnhancedXAXRFImageType4"
	Name="PlanesInAcquisition"								Type="1"	StringDefinedTerms="PlaneIdentification"
	Name="PlaneIdentification"								Type="1C"	Condition="PlanesInAcquisitionNotUndefined"	StringDefinedTerms="PlaneIdentification"
	Name="AcquisitionNumber"								Type="3"
	Name="AcquisitionDateTime"								Type="1"
	Name="BitsAllocated"									Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"										Type="1"	BinaryEnumValues="BitsAre8To16"
	Verify="BitsStored"													Condition="BitsAllocatedIs8"	BinaryEnumValues="BitsAre8"
	Verify="BitsStored"													Condition="BitsAllocatedIs16"	BinaryEnumValues="BitsAre9To16"
	Name="HighBit"											Type="1"	BinaryEnumValues="BitsAre7To15"
	Verify="HighBit"													Condition="BitsAllocatedIs8"	BinaryEnumValues="BitsAre7"
	Verify="HighBit"													Condition="BitsAllocatedIs16"	BinaryEnumValues="BitsAre8To15"
	Name="SamplesPerPixel"									Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PixelRepresentation"								Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="PhotometricInterpretation"						Type="1"	StringEnumValues="PhotometricInterpretationMonochrome"
	Name="AcquisitionProtocolName"							Type="3"
	Name="AcquisitionProtocolDescription"					Type="3"
	Name="ScanOptions"										Type="3"	StringDefinedTerms="EnhancedXAXRFScanOptions"
	Name="ContentQualification"								Type="1"	StringEnumValues="ContentQualification"
	Sequence="PatientOrientationCodeSequence"				Type="1C"	VM="1"	Condition="PositionerIsCArmWithTableTopRelationship"
		InvokeMacro="CodeSequenceMacro"									BaselineContextID="19"
		Sequence="PatientOrientationModifierCodeSequence"   Type="1C"	VM="1"	NoCondition=""	# real-world - orientation wrt. gravity
 			InvokeMacro="CodeSequenceMacro"								BaselineContextID="20"
		SequenceEnd
	SequenceEnd
	Sequence="PatientGantryRelationshipCodeSequence"		Type="2C"	VM="0-1"	Condition="PositionerIsCArmWithTableTopRelationship"
		InvokeMacro="CodeSequenceMacro"									BaselineContextID="21"
	SequenceEnd
	Name="ExaminedBodyThickness"							Type="3"	NotZeroWarning=""
	Name="BurnedInAnnotation"								Type="1"	StringEnumValues="NoFull"
	Name="RecognizableVisualFeatures"						Type="3"	StringEnumValues="YesNoFull"
	Name="LossyImageCompression"							Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"						Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"						Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"								Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Sequence="ReferencedOtherPlaneSequence"					Type="1C"	VM="1"	Condition="ImageTypeValue3BiplaneAOrB"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedImageEvidenceSequence"				Type="1C"	VM="1-n"	Condition="ReferencedImageSequenceIsPresentInFunctionalGroups"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="SourceImageEvidenceSequence"					Type="1C"	VM="1-n"	Condition="SourceImageSequenceIsPresentInFunctionalGroups"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedInstanceSequence"					Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"			Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"								DefinedContextID="7004"
		SequenceEnd
	SequenceEnd
	Name="ImageComments"									Type="3"
	Name="QualityControlImage"								Type="3"	StringEnumValues="YesNoFull"
	Sequence="IconImageSequence"							Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
	Name="PresentationLUTShape"								Type="1"	StringEnumValues="IdentityOrInversePresentationLUTShape"
	Verify="PresentationLUTShape"										Condition="PhotometricInterpretationIsMonochrome2"	StringEnumValues="IdentityPresentationLUTShape"
	Verify="PresentationLUTShape"										Condition="PhotometricInterpretationIsMonochrome1"	StringEnumValues="InversePresentationLUTShape"
ModuleEnd

Module="XAXRFAcquisition"
	Name="KVP"												Type="1"	NotZeroWarning=""
	Name="RadiationSetting"									Type="1"	StringEnumValues="EnhancedXAXRFRadiationSetting"
	Name="XRayTubeCurrentInmA"								Type="1C"	Condition="ExposureInmAsNotPresent"	NotZeroWarning=""
	Name="ExposureTimeInms"									Type="1C"	Condition="ExposureInmAsNotPresent"	NotZeroWarning=""
	Name="ExposureInmAs"									Type="1C"	Condition="XRayTubeCurrentInmAOrExposureTimeInmsNotPresent"	NotZeroWarning=""
	Name="AveragePulseWidth"								Type="1"	NotZeroWarning=""
	Name="AcquisitionDuration"								Type="1"	NotZeroWarning=""
	Name="RadiationMode"									Type="1"	StringDefinedTerms="EnhancedXAXRFRadiationMode"
	Name="FocalSpots"										Type="3"
	Name="AnodeTargetMaterial"								Type="3"	StringDefinedTerms="AnodeTargetMaterial"
	Name="RectificationType"								Type="3"	StringDefinedTerms="RectificationType"
	Name="XRayReceptorType"									Type="3"	StringEnumValues="XRayReceptorType"
	Name="DistanceReceptorPlaneToDetectorHousing"			Type="2"	NotZeroWarning=""
	Name="PositionerType"									Type="2"	StringDefinedTerms="EnhancedXAXRFPositionerType"
	Name="CArmPositionerTabletopRelationship"				Type="1C"	Condition="PositionerIsCArm"	StringEnumValues="YesNoFull"
	Name="AcquiredImageAreaDoseProduct"						Type="2"	NotZeroWarning=""
ModuleEnd

Module="XRayImageIntensifier"
	Name="IntensifierSize"									Type="1"	NotZeroWarning=""
	Name="IntensifierActiveShape"							Type="1"	StringEnumValues="IntensifierActiveShape"
	Name="IntensifierActiveDimensions"						Type="1"	NotZeroWarning=""
ModuleEnd

Module="XRayDetector"
	InvokeMacro="DigitalXRayDetectorMacro"
	Name="PhysicalDetectorSize"								Type="1"	NotZeroError=""
	Name="PositionOfIsocenterProjection"					Type="1C"	Condition="IsocenterReferenceSystemSequencePresent"
ModuleEnd

DefineMacro="XRayFrameCharacteristicsMacro" InformationEntity="FunctionalGroup"
	Sequence="XAXRFFrameCharacteristicsSequence"			Type="1"	VM="1"
		Name="DerivationDescription"						Type="3" 
		Sequence="DerivationCodeSequence"					Type="3"	VM="1-n"
			InvokeMacro="CodeSequenceMacro"								DefinedContextID="7203"
		SequenceEnd
		Name="AcquisitionDeviceProcessingDescription"		Type="3"
		Name="AcquisitionDeviceProcessingCode"				Type="3"
	SequenceEnd
MacroEnd

DefineMacro="XRayFieldOfViewMacro" InformationEntity="FunctionalGroup"
	Sequence="FieldOfViewSequence"							Type="1"	VM="1"
		Name="FieldOfViewShape"								Type="3" 	StringEnumValues="FieldOfViewShape"
		Name="FieldOfViewDimensionsInFloat"					Type="3"	NotZeroWarning=""
		Name="FieldOfViewOrigin"							Type="1C"	Condition="XRayReceptorTypeIsDigitalDetector" mbpo="true"
		Name="FieldOfViewRotation"							Type="1"	StringEnumValues="DXFieldOfViewRotation"
		Name="FieldOfViewHorizontalFlip"					Type="1"	StringEnumValues="YesNoFull"
		Name="FieldOfViewDescription"						Type="3"
	SequenceEnd
MacroEnd

DefineMacro="XRayExposureControlSensingRegionsMacro" InformationEntity="FunctionalGroup"
	Sequence="ExposureControlSensingRegionsSequence"				Type="1"	VM="1-n"
		Name="ExposureControlSensingRegionShape"					Type="1" 	StringEnumValues="ExposureControlSensingRegionShape"
		Name="ExposureControlSensingRegionLeftVerticalEdge"			Type="1C" 	Condition="ExposureControlSensingRegionShapeIsRectangular"
		Name="ExposureControlSensingRegionRightVerticalEdge"		Type="1C" 	Condition="ExposureControlSensingRegionShapeIsRectangular"
		Name="ExposureControlSensingRegionUpperHorizontalEdge"		Type="1C" 	Condition="ExposureControlSensingRegionShapeIsRectangular"
		Name="ExposureControlSensingRegionLowerHorizontalEdge"		Type="1C" 	Condition="ExposureControlSensingRegionShapeIsRectangular"
		Name="CenterOfCircularExposureControlSensingRegion"			Type="1C" 	Condition="ExposureControlSensingRegionShapeIsCircular"
		Name="RadiusOfCircularExposureControlSensingRegion"			Type="1C" 	Condition="ExposureControlSensingRegionShapeIsCircular"
		Name="VerticesOfThePolygonalExposureControlSensingRegion"	Type="1C" 	Condition="ExposureControlSensingRegionShapeIsPolygonal"
	SequenceEnd
MacroEnd

DefineMacro="XRayFramePixelDataPropertiesMacro" InformationEntity="FunctionalGroup"
	Sequence="FramePixelDataPropertiesSequence"				Type="1"	VM="1"
		Name="FrameType"									Type="1"	VM="4-n"
		Verify="FrameType"												ValueSelector="0"	StringEnumValues="EnhancedXAXRFImageType1"
		Verify="FrameType"												ValueSelector="1"	StringEnumValues="EnhancedXAXRFImageType2"
		Verify="FrameType"												ValueSelector="2"	StringDefinedTerms="EnhancedXAXRFImageType3"
		Verify="FrameType"												ValueSelector="3"	StringEnumValues="EnhancedXAXRFImageType4"
		Name="PixelIntensityRelationship"					Type="1"	StringDefinedTerms="XAXRFPixelIntensityRelationship"
		Name="PixelIntensityRelationshipSign"				Type="1"	BinaryEnumValues="PixelIntensityRelationshipSign"
		Name="ImagerPixelSpacing"							Type="1C"	NotZeroError=""	Condition="ImageTypeValue1IsOriginal" mbpo="true"
		Name="GeometricalProperties"						Type="1"	StringEnumValues="XAXRFGeometricalProperties"
		Name="GeometricMaximumDistortion"					Type="2C" 	Condition="GeometricalPropertiesIsNonUniform"
		Name="ImageProcessingApplied"						Type="1"	StringDefinedTerms="XAXRFImageProcessingApplied"
	SequenceEnd
MacroEnd

DefineMacro="XRayFrameDetectorParametersMacro" InformationEntity="FunctionalGroup"
	Sequence="FrameDetectorParametersSequence"				Type="1"	VM="1"
		Name="DetectorActiveTime"							Type="3"
		Name="DetectorActivationOffsetFromExposure"			Type="3"
	SequenceEnd
MacroEnd

DefineMacro="XRayCalibrationDeviceUsageMacro" InformationEntity="FunctionalGroup"
	Sequence="CalibrationSequence"							Type="1"	VM="1"
		Name="CalibrationImage"								Type="3"	StringEnumValues="YesNoFull"
	SequenceEnd
MacroEnd

DefineMacro="XRayObjectThicknessMacro" InformationEntity="FunctionalGroup"
	Sequence="ObjectThicknessSequence"							Type="1"	VM="1"
		Name="CalculatedAnatomyThickness"						Type="1"	NotZeroWarning=""
	SequenceEnd
MacroEnd

DefineMacro="XRayFrameAcquisitionMacro" InformationEntity="FunctionalGroup"
	Sequence="FrameAcquisitionSequence"							Type="1"	VM="1"
		Name="KVP"												Type="1"	NotZeroWarning=""
		Name="XRayTubeCurrentInmA"								Type="1"	NotZeroWarning=""
	SequenceEnd
MacroEnd

DefineMacro="XRayProjectionPixelCalibrationMacro" InformationEntity="FunctionalGroup"
	Sequence="ProjectionPixelCalibrationSequence"				Type="1"	VM="1"
		Name="DistanceObjectToTableTop"							Type="2"
		Name="ObjectPixelSpacingInCenterOfBeam"					Type="1C"	NotZeroError=""	Condition="DistanceObjectToTableTopNotEmpty"
		Name="TableHeight"										Type="1C"	Condition="ImageTypeValue1Original"
		Name="BeamAngle"										Type="1C"	Condition="ImageTypeValue1Original"
	SequenceEnd
MacroEnd

DefineMacro="XRayPositionerMacro" InformationEntity="FunctionalGroup"
	Sequence="PositionerPositionSequence"						Type="1"	VM="1"
		Name="PositionerPrimaryAngle"							Type="1C"	Condition="PositionerIsCArm"
		Name="PositionerSecondaryAngle"							Type="1C"	Condition="PositionerIsCArm"
		Name="ColumnAngulationPatient"							Type="1C"	Condition="PositionerIsColumn"
	SequenceEnd
MacroEnd

DefineMacro="XRayTablePositionMacro" InformationEntity="FunctionalGroup"
	Sequence="TablePositionSequence"							Type="1"	VM="1"
		Name="TableTopVerticalPosition"							Type="1"
		Name="TableTopLongitudinalPosition"						Type="1"
		Name="TableTopLateralPosition"							Type="1"
		Name="TableHorizontalRotationAngle"						Type="1"
		Name="TableHeadTiltAngle"								Type="1"
		Name="TableCradleTiltAngle"								Type="1"
	SequenceEnd
MacroEnd

DefineMacro="XRayCollimatorMacro" InformationEntity="FunctionalGroup"
	Sequence="CollimatorShapeSequence"							Type="1"	VM="1"
		Name="CollimatorShape"									Type="1"	StringEnumValues="CollimatorShape"
		Name="CollimatorLeftVerticalEdge"						Type="1C"	Condition="CollimatorShapeIsRectangular"
		Name="CollimatorRightVerticalEdge"						Type="1C"	Condition="CollimatorShapeIsRectangular"
		Name="CollimatorUpperHorizontalEdge"					Type="1C"	Condition="CollimatorShapeIsRectangular"
		Name="CollimatorLowerHorizontalEdge"					Type="1C"	Condition="CollimatorShapeIsRectangular"
		Name="CenterOfCircularCollimator"						Type="1C"	Condition="CollimatorShapeIsCircular"	NotZeroWarning=""
		Name="RadiusOfCircularCollimator"						Type="1C"	Condition="CollimatorShapeIsCircular"	NotZeroWarning=""
		Name="VerticesOfThePolygonalCollimator"					Type="1C"	Condition="CollimatorShapeIsPolygonal"
	SequenceEnd
MacroEnd

DefineMacro="XRayIsocenterReferenceSystemMacro" InformationEntity="FunctionalGroup"
	Sequence="IsocenterReferenceSystemSequence"					Type="1"	VM="1"
		Name="PositionerIsocenterPrimaryAngle"					Type="1"
		Name="PositionerIsocenterSecondaryAngle"				Type="1"
		Name="PositionerIsocenterDetectorRotationAngle"			Type="1"
		Name="TableXPositionToIsocenter"						Type="1"
		Name="TableYPositionToIsocenter"						Type="1"
		Name="TableZPositionToIsocenter"						Type="1"
		Name="TableHorizontalRotationAngle"						Type="1"
		Name="TableHeadTiltAngle"								Type="1"
		Name="TableCradleTiltAngle"								Type="1"
	SequenceEnd
MacroEnd

DefineMacro="XRayGeometryMacro" InformationEntity="FunctionalGroup"
	Sequence="XRayGeometrySequence"								Type="1"	VM="1"
		Name="DistanceSourceToIsocenter"						Type="1"	NotZeroWarning=""
		Name="DistanceSourceToDetector"							Type="1"	NotZeroWarning=""
	SequenceEnd
MacroEnd

Module="XAXRFMultiFramePresentation"
	Name="PreferredPlaybackSequencing"							Type="3"	BinaryEnumValues="PreferredPlaybackSequencing"
	Sequence="FrameDisplaySequence"								Type="3"	VM="1-n"
		Name="StartTrim"										Type="1"
		Name="StopTrim"											Type="1"
		Name="SkipFrameRangeFlag"								Type="1"	StringDefinedTerms="SkipFrameRangeFlag"
		Name="RecommendedDisplayFrameRateInFloat"				Type="1"
		Name="RecommendedViewingMode"							Type="2"	StringDefinedTerms="RecommendedViewingMode"
		Name="DisplayFilterPercentage"							Type="2"
		Name="MaskVisibilityPercentage"							Type="1C"	Condition="RecommendedViewingModeIsSUB"
	SequenceEnd
ModuleEnd


Module="MultiFrameFunctionalGroupsForEnhancedXAImage"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="PixelIntensityRelationshipLUTMacro"		Condition="NeedPixelIntensityRelationshipLUTMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FramePixelShiftMacro"		Condition="FramePixelShiftMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PatientOrientationInFrameMacro"		Condition="NeedPatientOrientationInFrameMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FrameDisplayShutterMacro"		Condition="FrameDisplayShutterMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"			Condition="IrradiationEventIdentificationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFrameCharacteristicsMacro"		Condition="XRayFrameCharacteristicsMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFieldOfViewMacro"		Condition="NeedXRayFieldOfViewMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayExposureControlSensingRegionsMacro"		Condition="XRayExposureControlSensingRegionsMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFramePixelDataPropertiesMacro"			Condition="FramePixelDataPropertiesSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFrameDetectorParametersMacro"		Condition="NeedXRayFrameDetectorParametersMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayCalibrationDeviceUsageMacro"		Condition="XRayCalibrationDeviceUsageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayObjectThicknessMacro"		Condition="XRayObjectThicknessMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFrameAcquisitionMacro"		Condition="XRayFrameAcquisitionMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayProjectionPixelCalibrationMacro"		Condition="NeedXRayProjectionPixelCalibrationMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayPositionerMacro"		Condition="NeedXRayPositionerMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayTablePositionMacro"		Condition="NeedXRayTablePositionMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayCollimatorMacro"		Condition="NeedXRayCollimatorMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayIsocenterReferenceSystemMacro"		Condition="XRayIsocenterReferenceSystemMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayGeometryMacro"		Condition="NeedXRayGeometryMacroInSharedFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelIntensityRelationshipLUTMacro"		Condition="NeedPixelIntensityRelationshipLUTMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FramePixelShiftMacro"		Condition="FramePixelShiftMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PatientOrientationInFrameMacro"		Condition="NeedPatientOrientationInFrameMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameDisplayShutterMacro"		Condition="FrameDisplayShutterMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"			Condition="IrradiationEventIdentificationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFrameCharacteristicsMacro"		Condition="XRayFrameCharacteristicsMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFieldOfViewMacro"		Condition="NeedXRayFieldOfViewMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayExposureControlSensingRegionsMacro"		Condition="XRayExposureControlSensingRegionsMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFramePixelDataPropertiesMacro"			Condition="FramePixelDataPropertiesSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFrameDetectorParametersMacro"		Condition="NeedXRayFrameDetectorParametersMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayCalibrationDeviceUsageMacro"		Condition="XRayCalibrationDeviceUsageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayObjectThicknessMacro"		Condition="XRayObjectThicknessMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFrameAcquisitionMacro"		Condition="XRayFrameAcquisitionMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayProjectionPixelCalibrationMacro"		Condition="NeedXRayProjectionPixelCalibrationMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayPositionerMacro"		Condition="NeedXRayPositionerMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayTablePositionMacro"		Condition="NeedXRayTablePositionMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayCollimatorMacro"		Condition="NeedXRayCollimatorMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayIsocenterReferenceSystemMacro"		Condition="XRayIsocenterReferenceSystemMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayGeometryMacro"		Condition="NeedXRayGeometryMacroInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="MultiFrameFunctionalGroupsForEnhancedXRFImage"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="PixelIntensityRelationshipLUTMacro"		Condition="NeedPixelIntensityRelationshipLUTMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FramePixelShiftMacro"		Condition="FramePixelShiftMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="PatientOrientationInFrameMacro"		Condition="NeedPatientOrientationInFrameMacroInSharedFunctionalGroupSequence"
		InvokeMacro="FrameDisplayShutterMacro"		Condition="FrameDisplayShutterMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"			Condition="IrradiationEventIdentificationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFrameCharacteristicsMacro"		Condition="XRayFrameCharacteristicsMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFieldOfViewMacro"		Condition="NeedXRayFieldOfViewMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayExposureControlSensingRegionsMacro"		Condition="XRayExposureControlSensingRegionsMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFramePixelDataPropertiesMacro"			Condition="FramePixelDataPropertiesSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFrameDetectorParametersMacro"		Condition="NeedXRayFrameDetectorParametersMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayCalibrationDeviceUsageMacro"		Condition="XRayCalibrationDeviceUsageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayObjectThicknessMacro"		Condition="XRayObjectThicknessMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFrameAcquisitionMacro"		Condition="XRayFrameAcquisitionMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRayPositionerMacro"		Condition="NeedXRayPositionerMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayTablePositionMacro"		Condition="NeedXRayTablePositionMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayCollimatorMacro"		Condition="NeedXRayCollimatorMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRayGeometryMacro"		Condition="NeedXRayGeometryMacroInSharedFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelIntensityRelationshipLUTMacro"		Condition="NeedPixelIntensityRelationshipLUTMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FramePixelShiftMacro"		Condition="FramePixelShiftMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PatientOrientationInFrameMacro"		Condition="NeedPatientOrientationInFrameMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameDisplayShutterMacro"		Condition="FrameDisplayShutterMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="IrradiationEventIdentificationMacro"			Condition="IrradiationEventIdentificationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFrameCharacteristicsMacro"		Condition="XRayFrameCharacteristicsMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFieldOfViewMacro"		Condition="NeedXRayFieldOfViewMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayExposureControlSensingRegionsMacro"		Condition="XRayExposureControlSensingRegionsMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFramePixelDataPropertiesMacro"			Condition="FramePixelDataPropertiesSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="XRayFrameDetectorParametersMacro"		Condition="NeedXRayFrameDetectorParametersMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayCalibrationDeviceUsageMacro"		Condition="XRayCalibrationDeviceUsageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayObjectThicknessMacro"		Condition="XRayObjectThicknessMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayFrameAcquisitionMacro"		Condition="XRayFrameAcquisitionMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayPositionerMacro"		Condition="NeedXRayPositionerMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayTablePositionMacro"		Condition="NeedXRayTablePositionMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayCollimatorMacro"		Condition="NeedXRayCollimatorMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRayGeometryMacro"		Condition="NeedXRayGeometryMacroInPerFrameFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="MultiFrameFunctionalGroupsForXRay3DAngiographicImage"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="CardiacSynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="XRay3DFrameTypeMacro"		Condition="XRay3DFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="CardiacSynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"		Condition="RespiratorySynchronizationMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRay3DFrameTypeMacro"		Condition="XRay3DFrameTypeSequenceNotInSharedFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="MultiFrameFunctionalGroupsForXRay3DCraniofacialImage"
	Sequence="SharedFunctionalGroupsSequence"	Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="XRay3DFrameTypeMacro"		Condition="XRay3DFrameTypeSequenceNotInPerFrameFunctionalGroupSequence"
	SequenceEnd
	Sequence="PerFrameFunctionalGroupsSequence"	Type="1"	VM="1-n"
		InvokeMacro="PixelMeasuresMacro"		Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PlanePositionMacro"		Condition="PlanePositionSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"		Condition="PlaneOrientationSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"		Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"		Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameAnatomyMacro"			Condition="FrameAnatomySequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PixelValueTransformationMacro"	Condition="PixelValueTransformationSequenceOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameVOILUTMacro"			Condition="FrameVOILUTSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"	Condition="RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"		Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="XRay3DFrameTypeMacro"		Condition="XRay3DFrameTypeSequenceNotInSharedFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

DefineMacro="CommonCTMRImageDescriptionImageLevelMacroForXRay3DImage" InformationEntity="Image"
	Name="PixelPresentation"						Type="1"	StringEnumValues="CommonCTMRPixelPresentationImageLevel"
	Verify="PixelPresentation"									Condition="EnhancedMRColorImageInstance"	StringEnumValues="PixelPresentationTrueColor"
	Name="VolumetricProperties"						Type="1"	StringEnumValues="CommonCTMRVolumetricPropertiesImageLevel"
	Name="VolumeBasedCalculationTechnique"			Type="1"	StringDefinedTerms="XRay3DImageVolumeBasedCalculationTechniqueImageLevel"
MacroEnd

DefineMacro="CommonCTMRImageDescriptionFrameLevelMacroForXRay3DImage" InformationEntity="Image"
	Name="PixelPresentation"						Type="1"	StringEnumValues="CommonCTMRPixelPresentationFrameLevel"
	Verify="PixelPresentation"									Condition="EnhancedMRColorImageInstance"	StringEnumValues="PixelPresentationTrueColor"
	Name="VolumetricProperties"						Type="1"	StringEnumValues="CommonCTMRVolumetricPropertiesFrameLevel"
	Name="VolumeBasedCalculationTechnique"			Type="1"	StringDefinedTerms="XRay3DImageVolumeBasedCalculationTechniqueFrameLevel"
MacroEnd

Module="XRay3DImage"
	Name="ImageType"										Type="1"	VM="4"
	Verify="ImageType"													ValueSelector="0"	StringEnumValues="CommonEnhancedImageType1"
	Verify="ImageType"													ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
	Verify="ImageType"													Condition="NotBreastTomosynthesisInstance" ValueSelector="2"	StringDefinedTerms="CommonEnhancedImageAndFrameType3"
	Verify="ImageType"													Condition="NotBreastTomosynthesisInstance" ValueSelector="3"	StringEnumValues="XRay3DImageAndFrameType4"
	InvokeMacro="CommonCTMRImageDescriptionImageLevelMacroForXRay3DImage"
	Name="BitsAllocated"									Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"										Type="1"	BinaryEnumValues="BitsAre8To16"
	Name="HighBit"											Type="1"	BinaryEnumValues="BitsAre7To15"
	Name="SamplesPerPixel"									Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"						Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="ContentQualification"								Type="1"	StringEnumValues="ContentQualification"
	Name="BurnedInAnnotation"								Type="1"	StringEnumValues="NoFull"
	Name="RecognizableVisualFeatures"						Type="3"	StringEnumValues="YesNoFull"
	Name="LossyImageCompression"							Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"						Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"						Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"								Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Sequence="ReferencedImageEvidenceSequence"				Type="1C"	VM="1-n"	Condition="ReferencedImageSequenceIsPresentInFunctionalGroups"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Name="ImageComments"									Type="3"
	Name="QualityControlImage"								Type="3"	StringEnumValues="YesNoFull"
	Sequence="IconImageSequence"							Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
	Name="PresentationLUTShape"								Type="1"	StringEnumValues="IdentityPresentationLUTShape"
	Sequence="SourceIrradiationEventSequence"				Type="3"	VM="1-n"
		Name="IrradiationEventUID"							Type="1"
	SequenceEnd
ModuleEnd

Module="XRay3DAngiographicImageContributingSources"
	Sequence="ContributingSourcesSequence"		Type="1"	VM="1-n"
		InvokeMacro="GeneralContributingSourcesMacro"
		InvokeMacro="ContributingImageSourcesMacro"
		Name="AcquisitionDeviceProcessingDescription"		Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
		Name="AcquisitionDeviceProcessingCode"				Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
		Name="PlaneIdentification"							Type="1C"	NoCondition=""	StringEnumValues="PlaneIdentification"	# if present and have an equal value in the contributing SOP Instances :(
		Name="ImagerPixelSpacing"							Type="1C"	NotZeroError=""	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
	SequenceEnd
ModuleEnd

Module="XRay3DCraniofacialImageContributingSources"
	Sequence="ContributingSourcesSequence"		Type="1"	VM="1-n"
		InvokeMacro="GeneralContributingSourcesMacro"
		InvokeMacro="ContributingImageSourcesMacro"
		Name="AcquisitionDeviceProcessingDescription"		Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
		Name="AcquisitionDeviceProcessingCode"				Type="1C"	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
		Name="ImagerPixelSpacing"							Type="1C"	NotZeroError=""	NoCondition=""	# if present and have an equal value in the contributing SOP Instances :(
	SequenceEnd
ModuleEnd

DefineMacro="XRay3DGeneralSharedAcquisitionMacro"
	Sequence="SourceImageSequence"						Type="1C"	VM="1-n"	Condition="SourceImageSequenceIsPresent"		# if if the reconstruction is created from DICOM SOP Instances :(
		InvokeMacro="ImageSOPInstanceReferenceMacro"
	SequenceEnd
	Name="FieldOfViewDimensionsInFloat"					Type="1C"	VM="1-2"	NotZeroWarning=""	Condition="ModalityIsMG" mbpo="true"			# since also real world if present and consistent in contributing instances
	Verify="FieldOfViewDimensionsInFloat"				Type="1C"	VM="2"		Condition="FieldOfViewDimensionsInFloatPresentAndFieldOfViewShapeIsRectangle"
	Verify="FieldOfViewDimensionsInFloat"				Type="1C"	VM="1"		Condition="FieldOfViewDimensionsInFloatPresentAndFieldOfViewShapeIsRound"
	Verify="FieldOfViewDimensionsInFloat"				Type="1C"	VM="1"		Condition="FieldOfViewDimensionsInFloatPresentAndFieldOfViewShapeIsHexagon"
	Name="FieldOfViewOrigin"							Type="1C"	Condition="XRayReceptorTypeIsDigitalDetector"
	Name="FieldOfViewRotation"							Type="1C"	NoCondition=""												# if present and have an equal value in the contributing SOP Instances :(
	Name="FieldOfViewHorizontalFlip"					Type="1C"	NoCondition=""												# if present and have an equal value in the contributing SOP Instances :(
	Name="Grid"											Type="1C"	NoCondition=""	StringDefinedTerms="XRayGrid"				# if present and have an equal value in the contributing SOP Instances :(
	InvokeMacro="XRayGridDescriptionMacro"
	Name="KVP"											Type="1C"	Condition="ModalityIsMG" mbpo="true"	NotZeroWarning=""	# if present and have an equal value in the contributing SOP Instances :(
	Name="XRayTubeCurrentInmA"							Type="1C"	Condition="ModalityIsMG" mbpo="true"	NotZeroWarning=""	# if present and have an equal value in the contributing SOP Instances :(
	Name="ExposureTimeInms"								Type="1C"	Condition="ModalityIsMG" mbpo="true"	NotZeroWarning=""	# if present and have an equal value in the contributing SOP Instances :(
	Name="ExposureInmAs"								Type="1C"	Condition="ModalityIsMG" mbpo="true"	NotZeroWarning=""	# if present and have an equal value in the contributing SOP Instances :(
	Name="ContrastBolusAgent"							Type="1C"	NoCondition=""												# if present and have an equal value in the contributing SOP Instances :(
	Sequence="ContrastBolusAgentSequence"				Type="1C"	VM="1-n"	NoCondition=""									# if present and have an equal value in the contributing SOP Instances etc. :(
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	Name="StartAcquisitionDateTime"						Type="1C"	NoCondition=""												# if present and have an equal value in the contributing SOP Instances :(
	Name="EndAcquisitionDateTime"						Type="1C"	NoCondition=""												# if present and have an equal value in the contributing SOP Instances :(
MacroEnd

DefineMacro="XRay3DGeneralPerProjectionAcquisitionMacro"
	Name="KVP"											Type="1C"	Condition="ModalityIsMG" mbpo="true"	NotZeroWarning=""	# since also if present and have an equal value in the contributing SOP Instances :(
	Name="XRayTubeCurrentInmA"							Type="1C"	Condition="ModalityIsMG" mbpo="true"	NotZeroWarning=""	# since also if present and have an equal value in the contributing SOP Instances :(
	Name="FrameAcquisitionDuration"						Type="1C"	NoCondition=""	NotZeroWarning=""							# if present and have an equal value in the contributing SOP Instances :(
	Name="CollimatorShape"								Type="1C"	NoCondition=""	StringEnumValues="CollimatorShape"			# if present and have an equal value in the contributing SOP Instances :(
	InvokeMacro="XRayCollimatorDimensionsMacro"
MacroEnd

DefineMacro="XRay3DGeneralPositionerMovementMacro"
	Name="PrimaryPositionerScanArc"							Type="1C"	Condition="ModalityIsMG" mbpo="true"						# since also real world if present and consistent in contributing instances
	Name="PrimaryPositionerScanStartAngle"					Type="1C"	Condition="ModalityIsMG" mbpo="true"						# since also real world if present and consistent in contributing instances
	Name="PrimaryPositionerIncrement"						Type="1C"	Condition="ModalityIsMG" mbpo="true"						# since also real world if present and consistent in contributing instances
	Name="SecondaryPositionerScanArc"						Type="1C"	NoCondition=""												# real world if present and consistent in contributing instances
	Name="SecondaryPositionerScanStartAngle"				Type="1C"	NoCondition=""												# real world if present and consistent in contributing instances
	Name="SecondaryPositionerIncrement"						Type="1C"	NoCondition=""												# real world if present and consistent in contributing instances
MacroEnd

Module="XRay3DAngiographicAcquisition"
	Sequence="XRay3DAcquisitionSequence"		Type="1"	VM="1-n"
		Name="FieldOfViewShape"									Type="1C"	NoCondition=""	StringDefinedTerms="FieldOfViewShape"		# if present and have an equal value in the contributing SOP Instances :(
		Name="XRayReceptorType"									Type="1C"	NoCondition=""	StringEnumValues="XRayReceptorTypeAngio"	# if present and have an equal value in the contributing SOP Instances :(
		InvokeMacro="XRay3DGeneralSharedAcquisitionMacro"
		InvokeMacro="DigitalXRayDetectorMacro"
		Name="PhysicalDetectorSize"								Type="1C"	NoCondition=""	NotZeroError=""							# if present and have an equal value in the contributing SOP Instances :(
		Name="PositionOfIsocenterProjection"					Type="1C"	Condition="IsocenterReferenceSystemSequencePresent"		# if present and have an equal value in the contributing SOP Instances :(
		Name="DistanceSourceToPatient"							Type="1C"	NoCondition=""	NotZeroWarning=""						# if present and have an equal value in the contributing SOP Instances :(
		Name="DistanceSourceToDetector"							Type="1C"	NoCondition=""	NotZeroWarning=""						# if present and have an equal value in the contributing SOP Instances :(
		Name="FocalSpots"										Type="1C"	NoCondition=""
		Name="FilterType"										Type="1C"	NoCondition=""	StringDefinedTerms="DXFilterType"		# if present and have an equal value in the contributing SOP Instances :(
		Name="FilterMaterial"									Type="1C"	NoCondition=""	StringDefinedTerms="DXFilterMaterial"	# if present and have an equal value in the contributing SOP Instances :(
		Name="FilterThicknessMaximum"							Type="1C"	NoCondition=""	NotZeroWarning=""						# if present and have an equal value in the contributing SOP Instances :(
		Name="FilterThicknessMinimum"							Type="1C"	NoCondition=""	NotZeroWarning=""						# if present and have an equal value in the contributing SOP Instances :(
		InvokeMacro="XRay3DGeneralPositionerMovementMacro"
		Sequence="PerProjectionAcquisitionSequence"				Type="1C"	VM="1-n"	NoCondition=""								# if present and have an equal value in the contributing SOP Instances :(
			InvokeMacro="XRay3DGeneralPerProjectionAcquisitionMacro"
			Name="PositionerIsocenterPrimaryAngle"				Type="1C"	NoCondition=""											# if present and have an equal value in the contributing SOP Instances :(
			Name="PositionerIsocenterSecondaryAngle"			Type="1C"	NoCondition=""											# if present and have an equal value in the contributing SOP Instances :(
			Name="PositionerIsocenterDetectorRotationAngle"		Type="1C"	NoCondition=""											# if present and have an equal value in the contributing SOP Instances :(
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="XRay3DCraniofacialAcquisition"
	Sequence="XRay3DAcquisitionSequence"		Type="1"	VM="1-n"
		Name="FieldOfViewShape"									Type="1C"	NoCondition=""	StringDefinedTerms="FieldOfViewShape"		# if present and have an equal value in the contributing SOP Instances :(
		Name="XRayReceptorType"									Type="1C"	NoCondition=""	StringEnumValues="XRayReceptorTypeCranio"	# if present and have an equal value in the contributing SOP Instances :(
		InvokeMacro="XRay3DGeneralSharedAcquisitionMacro"
		InvokeMacro="DigitalXRayDetectorMacro"
		Sequence="PerProjectionAcquisitionSequence"				Type="1C"	VM="1-n"	NoCondition=""								# if present and have an equal value in the contributing SOP Instances :(
			InvokeMacro="XRay3DGeneralPerProjectionAcquisitionMacro"
		SequenceEnd
	SequenceEnd
ModuleEnd

Module="XRay3DReconstruction"
	Sequence="XRay3DReconstructionSequence"		Type="1"	VM="1-n"
		Name="ReconstructionDescription"		Type="3"
		Name="ApplicationName"					Type="1"
		Name="ApplicationVersion"				Type="1"
		Name="ApplicationManufacturer"			Type="1"
		Name="AlgorithmType"					Type="1"	StringDefinedTerms="XRay3DReconstructionAlgorithmType"
		Name="AlgorithmDescription"				Type="3"
		Name="AcquisitionIndex "				Type="1"
	SequenceEnd
ModuleEnd

DefineMacro="XRay3DFrameTypeMacro"
	Sequence="XRay3DFrameTypeSequence"				Type="1"	VM="1"
		Name="FrameType"							Type="1"	VM="4"
		Verify="FrameType"										ValueSelector="0"	StringEnumValues="CommonEnhancedFrameType1"
		Verify="FrameType"										ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
		Verify="FrameType"										Condition="NotBreastTomosynthesisInstance"	ValueSelector="2"	StringDefinedTerms="CommonEnhancedImageAndFrameType3"
		Verify="FrameType"										Condition="BreastTomosynthesisInstance"		ValueSelector="2"	StringDefinedTerms="CommonEnhancedImageAndFrameType3AndBreastTomoImageAndFrameType3"
		Verify="FrameType"										Condition="NotBreastTomosynthesisInstance"	ValueSelector="3"	StringEnumValues="XRay3DImageAndFrameType4"
		Verify="FrameType"										Condition="BreastTomosynthesisInstance"	ValueSelector="3"		StringEnumValues="BreastTomoImageAndFrameType4"
		Verify="FrameType"										Condition="BreastTomosynthesisInstance"	ValueSelector="4"		StringEnumValues="BreastTomoImageAndFrameType5"
		InvokeMacro="CommonCTMRImageDescriptionFrameLevelMacroForXRay3DImage"
		Name="ReconstructionIndex"					Type="1C"	Condition="XRay3DReconstructionSequenceIsPresent"
	SequenceEnd
MacroEnd
Module="EnhancedPaletteColorLookupTable"
	Sequence="DataFrameAssignmentSequence"				Type="1"	VM="1-3"
		Name="DataType"									Type="1"
		Name="DataPathAssignment"						Type="1"	StringEnumValues="DataPathAssignment"
		Name="BitsMappedToColorLookupTable"				Type="3"
		InvokeMacro="VOILUTMacro"
	SequenceEnd
	Sequence="BlendingLUT1Sequence"						Type="1C"	VM="1"	Condition="AnyDataPathAssignmentIsOtherThanPrimaryPValues"
		Name="BlendingLUT1TransferFunction"				Type="1"	StringEnumValues="BlendingLUT1TransferFunction"
		Name="BlendingWeightConstant"					Type="1C"	Condition="BlendingLUT1TransferFunctionIsConstant"
		Name="BlendingLookupTableDescriptor"			Type="1C"	Condition="BlendingLUT1TransferFunctionIsTable"
		Verify="BlendingLookupTableDescriptor"						ValueSelector="1"	BinaryEnumValues="Zero"	
		Name="BlendingLookupTableData"					Type="1C"	Condition="BlendingLUT1TransferFunctionIsTable"
	SequenceEnd
	Sequence="BlendingLUT2Sequence"						Type="1C"	VM="1"	Condition="AnyDataPathAssignmentIsOtherThanPrimaryPValues"
		Name="BlendingLUT2TransferFunction"				Type="1"	StringEnumValues="BlendingLUT2TransferFunction"
		Name="BlendingWeightConstant"					Type="1C"	Condition="BlendingLUT2TransferFunctionIsConstant"
		Name="BlendingLookupTableDescriptor"			Type="1C"	Condition="BlendingLUT1TransferFunctionIsTable"
		Verify="BlendingLookupTableDescriptor"						ValueSelector="1"	BinaryEnumValues="Zero"	
		Name="BlendingLookupTableData"					Type="1C"	Condition="BlendingLUT1TransferFunctionIsTable"
	SequenceEnd
	Sequence="EnhancedPaletteColorLookupTableSequence"	Type="1C"	VM="1-2"	Condition="AnyDataPathAssignmentIsOtherThanPrimaryPValues"
		Name="DataPathID"								Type="1"	StringEnumValues="DataPathID"
		Name="RGBLUTTransferFunction"					Type="1"	StringEnumValues="RGBLUTTransferFunction"
		Name="AlphaLUTTransferFunction"					Type="1"	StringEnumValues="AlphaLUTTransferFunction"
		Name="RedPaletteColorLookupTableDescriptor"		Type="1C"	Condition="RGBLUTTransferFunctionIsTable"
		Verify="RedPaletteColorLookupTableDescriptor"				ValueSelector="1"	BinaryEnumValues="Zero"	
		Name="GreenPaletteColorLookupTableDescriptor"	Type="1C"	Condition="RGBLUTTransferFunctionIsTable"
		Verify="GreenPaletteColorLookupTableDescriptor"				ValueSelector="1"	BinaryEnumValues="Zero"	
		Name="BluePaletteColorLookupTableDescriptor"	Type="1C"	Condition="RGBLUTTransferFunctionIsTable"
		Verify="BluePaletteColorLookupTableDescriptor"				ValueSelector="1"	BinaryEnumValues="Zero"	
		Name="AlphaPaletteColorLookupTableDescriptor"	Type="1C"	Condition="RGBLUTTransferFunctionIsTable"
		Verify="AlphaPaletteColorLookupTableDescriptor"				ValueSelector="1"	BinaryEnumValues="Zero"	
		Name="RedPaletteColorLookupTableData"			Type="1C"	Condition="RGBLUTTransferFunctionIsTable"
		Name="GreenPaletteColorLookupTableData"			Type="1C"	Condition="RGBLUTTransferFunctionIsTable"
		Name="BluePaletteColorLookupTableData"			Type="1C"	Condition="RGBLUTTransferFunctionIsTable"
		Name="AlphaPaletteColorLookupTableData"			Type="1C"	Condition="RGBLUTTransferFunctionIsTable"
	SequenceEnd
	Name="ICCProfile"									Type="1C"	Condition="AnyDataPathAssignmentIsOtherThanPrimaryPValues"
	Name="ColorSpace"									Type="3"
ModuleEnd

DefineMacro="PlanePositionVolumeMacro" InformationEntity="FunctionalGroup"
	Sequence="PlanePositionVolumeSequence"			Type="1"	VM="1"
		Name="ImagePositionVolume"					Type="1" 
	SequenceEnd
MacroEnd

DefineMacro="PlaneOrientationVolumeMacro" InformationEntity="FunctionalGroup"
	Sequence="PlaneOrientationVolumeSequence"		Type="1"	VM="1"
		Name="ImageOrientationVolume"				Type="1" 
	SequenceEnd
MacroEnd

DefineMacro="TemporalPositionMacro" InformationEntity="FunctionalGroup"
	Sequence="TemporalPositionSequence"				Type="1"	VM="1"
		Name="TemporalPositionTimeOffset"			Type="1" 
	SequenceEnd
MacroEnd

DefineMacro="ImageDataTypeMacro" InformationEntity="FunctionalGroup"
	Sequence="ImageDataTypeSequence"				Type="1"	VM="1"
		Name="DataType"								Type="1"	StringDefinedTerms="EnhancedUSVolumeDataType"
		Name="AliasedDataType"						Type="1"	StringEnumValues="YesNoFull"
		Name="ZeroVelocityPixelValue"				Type="1C"	Condition="NeedZeroVelocityPixelValue" mbpo="true"
	SequenceEnd
MacroEnd

Module="EnhancedUSSeries"
	Name="Modality"										Type="1"	StringEnumValues="USOrIVUSModality"
	Sequence="ReferencedPerformedProcedureStepSequence"	Type="1C"	VM="1"	Condition="SeriesNeedReferencedPerformedProcedureStepSequence"
		InvokeMacro="SOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="PerformedProtocolCodeSequence"			Type="1C"	VM="1"	NoCondition=""	mbpo="true"
		InvokeMacro="CodeSequenceMacro"
		Sequence="ProtocolContextSequence"				Type="3"	VM="1-n"
			InvokeMacro="ContentItemMacro"
			Sequence="ContentItemModifierSequence"		Type="3"	VM="1-n"
				InvokeMacro="ContentItemMacro"
			SequenceEnd
		SequenceEnd
	SequenceEnd
	Name="PerformedProtocolType"						Type="1C"	Condition="PerformedProtocolCodeSequenceIsPresent"	StringEnumValues="PerformedProtocolType"
ModuleEnd

Module="UltrasoundFrameOfReference"
	Name="VolumeFrameOfReferenceUID"						Type="1"
	Name="UltrasoundAcquisitionGeometry"					Type="1"	StringDefinedTerms="UltrasoundAcquisitionGeometry"
	Name="ApexPosition"										Type="1C"	Condition="UltrasoundAcquisitionGeometryIsApex"
	Name="VolumeToTransducerRelationship"					Type="1C"	NoCondition=""	StringEnumValues="VolumeToTransducerRelationship"
	Name="VolumeToTransducerMappingMatrix"					Type="1"
	Name="PatientFrameOfReferenceSource"					Type="1C"	Condition="NeedPatientFrameOfReferenceSource"	StringEnumValues="PatientFrameOfReferenceSource"
	Name="TableFrameOfReferenceUID"							Type="1C"	Condition="PatientFrameOfReferenceSourceIsTable"
	Name="VolumeToTableMappingMatrix"						Type="1C"	Condition="PatientFrameOfReferenceSourceIsTable"
ModuleEnd

Module="EnhancedUSImage"
	Name="ImageType"										Type="1"	VM="4-n"
	Verify="ImageType"													ValueSelector="0"	StringEnumValues="CommonEnhancedImageType1"
	Verify="ImageType"													ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
	Verify="ImageType"													ValueSelector="2"	StringDefinedTerms="CommonEnhancedImageAndFrameType3"
	Verify="ImageType"													ValueSelector="3"	StringDefinedTerms="CommonEnhancedImageType4"
	Name="SamplesPerPixel"									Type="1"	BinaryEnumValues="SamplesPerPixelIsOne"
	Name="PhotometricInterpretation"						Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2"
	Name="BitsAllocated"									Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="BitsStored"										Type="1"	BinaryEnumValues="BitsAre8Or16"
	Name="HighBit"											Type="1"	BinaryEnumValues="BitsAre7Or15"
	Name="PixelRepresentation"								Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"
	Name="DimensionOrganizationType"						Type="1"	StringEnumValues="DimensionOrganizationType3DOr3DTemporal"
	Name="AcquisitionDateTime"								Type="1"
	Name="AcquisitionDuration"								Type="1"
	Name="PositionMeasuringDeviceUsed"						Type="1C"	Condition="NeedPositionMeasuringDeviceUsed"	StringEnumValues="PositionMeasuringDeviceUsed"	mbpo="true"
	Name="LossyImageCompression"							Type="1"	StringEnumValues="LossyImageCompression"
	Name="LossyImageCompressionRatio"						Type="1C"	Condition="LossyImageCompressionIs01"	NotZeroError=""
	Name="LossyImageCompressionMethod"						Type="1C"	StringDefinedTerms="LossyImageCompressionMethod"	Condition="LossyImageCompressionIs01"
	Verify="LossyImageCompressionMethod"								Condition="LossyImageCompressionMethodInconsistentWithTransferSyntax"	ThenWarningMessage="method inconsistent with transfer syntax" ShowValueWithMessage="true"
	Name="PresentationLUTShape"								Type="1"	StringEnumValues="IdentityPresentationLUTShape"
	Name="RescaleIntercept"									Type="1"	BinaryEnumValues="Zero"
	Name="RescaleSlope"										Type="1"	BinaryEnumValues="One"
	Sequence="SourceImageSequence"							Type="1C"	VM="1-n"	Condition="ImageTypeValue1Derived"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="ReferencedImageSequence"						Type="3"	VM="1-n"
		InvokeMacro="ImageSOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Sequence="ReferencedRawDataSequence"					Type="3"	VM="1-n"
		InvokeMacro="HierarchicalSOPInstanceReferenceMacro"
	SequenceEnd
	Sequence="ReferencedInstanceSequence"					Type="3"	VM="1-n"
		InvokeMacro="SOPInstanceReferenceMacro"
		Sequence="PurposeOfReferenceCodeSequence"			Type="3"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
	SequenceEnd
	Name="NumberOfStages"									Type="1C"	Condition="PerformedProtocolTypeIsStaged"
	Name="StageNumber"										Type="1C"	Condition="PerformedProtocolTypeIsStaged"
	Sequence="StageCodeSequence"							Type="1C"	VM="1"	Condition="PerformedProtocolTypeIsStaged"
		InvokeMacro="CodeSequenceMacro"
	SequenceEnd
	InvokeMacro="MandatoryViewAndSliceProgressionDirectionMacro"
	Sequence="EventTimerSequence"							Type="3"	VM="1-n"
		Name="EventTimeOffset"								Type="1"
		Sequence="EventCodeSequence"						Type="1"	VM="1"
			InvokeMacro="CodeSequenceMacro"
		SequenceEnd
		Name="EventTimerNames"								Type="3"	VM="1"
	SequenceEnd
	InvokeMacro="GeneralAnatomyMandatoryMacro"
	Name="BurnedInAnnotation"								Type="1"	StringEnumValues="NoFull"
	Name="RecognizableVisualFeatures"						Type="3"	StringEnumValues="YesNoFull"
	Sequence="IconImageSequence"							Type="3"	VM="1"
		InvokeMacro="IconImageSequenceMacro"
	SequenceEnd
	Name="TransducerData"									Type="3"
	Sequence="TransducerScanPatternCodeSequence"			Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"									DefinedContextID=12032"
	SequenceEnd
	Sequence="TransducerGeometryCodeSequence"				Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"									DefinedContextID=12033"
	SequenceEnd
	Sequence="TransducerBeamSteeringCodeSequence"			Type="1"	VM="1-n"
		InvokeMacro="CodeSequenceMacro"									DefinedContextID=12034"
	SequenceEnd
	Sequence="TransducerApplicationCodeSequence"			Type="1"	VM="1"
		InvokeMacro="CodeSequenceMacro"									DefinedContextID=12035"
	SequenceEnd
	Name="ProcessingFunction"								Type="3"
	Name="MechanicalIndex"									Type="1"
	Name="BoneThermalIndex"									Type="1"
	Name="CranialThermalIndex"								Type="1"
	Name="SoftTissueThermalIndex"							Type="1"
	Name="DepthsOfFocus"									Type="1"
	Name="DepthOfScanField"									Type="1"
ModuleEnd

Module="IVUSImage"
	Name="IVUSAcquisition"									Type="1"	StringDefinedTerms="IVUSAcquisition"
	Name="IVUSPullbackRate"									Type="1C"	Condition="IVUSAcquisitionIsMotor"
	Name="IVUSGatedRate"									Type="1C"	Condition="IVUSAcquisitionIsGated"
	Name="IVUSPullbackStartFrameNumber"						Type="1C"	Condition="IVUSAcquisitionIsMotorOrGated"	NotZeroError=""
	Name="IVUSPullbackStopFrameNumber"						Type="1C"	Condition="IVUSAcquisitionIsMotorOrGated"	NotZeroError=""
ModuleEnd

Module="ExcludedIntervals"
	Sequence="ExcludedIntervalsSequence"					Type="1C"	VM="1-n"	NoCondition=""
		Name="ExclusionStartDateTime"						Type="1"
		Name="ExclusionDuration"							Type="1"
	SequenceEnd
ModuleEnd

DefineMacro="USImageDescriptionMacro" InformationEntity="FunctionalGroup"
	Sequence="USImageDescriptionSequence"				Type="1"	VM="1"
		Name="FrameType"								Type="1"	VM="4-n"
		Verify="FrameType"											ValueSelector="0"	StringEnumValues="CommonEnhancedFrameType1"
		Verify="FrameType"											ValueSelector="1"	StringEnumValues="CommonEnhancedImageAndFrameType2"
		Verify="FrameType"											ValueSelector="2"	StringEnumValues="CommonEnhancedImageAndFrameType3"
		Verify="FrameType"											ValueSelector="3"	StringEnumValues="CommonEnhancedFrameType4"
		Name="VolumetricProperties"						Type="1"	StringEnumValues="CommonCTMRVolumetricPropertiesImageLevel"
		Name="VolumeBasedCalculationTechnique"			Type="1"	StringDefinedTerms="CommonCTMRVolumeBasedCalculationTechniqueImageLevel"
	SequenceEnd
MacroEnd

DefineMacro="USImageDescriptionMacroForEnhancedUSVolume" InformationEntity="FunctionalGroup"
	Sequence="USImageDescriptionSequence"				Type="1"	VM="1"
		Name="VolumetricProperties"						Type="1"	StringEnumValues="Volume"
		Name="VolumeBasedCalculationTechnique"			Type="1"	StringEnumValues="None"
	SequenceEnd
MacroEnd

Module="MultiFrameFunctionalGroupsForEnhancedUSVolume"
	Sequence="SharedFunctionalGroupsSequence"			Type="1"	VM="1"
		InvokeMacro="PixelMeasuresMacro"				Condition="PixelMeasuresSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"				Condition="PlanePositionSequenceOKInSharedFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"				Condition="PlaneOrientationSequenceOKInSharedFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"				Condition="ReferencedImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"				Condition="DerivationImageMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInSharedFunctionalGroupSequenceRegardlessOfImageType"
		InvokeMacro="FrameVOILUTMacro"					Condition="FrameVOILUTSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"		Condition="RealWorldValueMappingMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"			Condition="NeedContrastBolusUsageMacroInSharedFunctionalGroupSequence"
		InvokeMacro="PatientOrientationInFrameMacro"	Condition="PatientOrientationInFrameMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="FrameDisplayShutterMacro"			Condition="FrameDisplayShutterMacroOKInSharedFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"	Condition="NeedRespiratorySynchronizationMacroInSharedFunctionalGroupSequenceRegardlessOfImageType"
		InvokeMacro="PlaneOrientationVolumeMacro"
		InvokeMacro="TemporalPositionMacro"				Condition="TemporalPositionMacroOKInSharedFunctionalGroupSequenceAndNotCardiacOrRespiratoryEvent"
		InvokeMacro="ImageDataTypeMacro"				Condition="ImageDataTypeSequenceNotInPerFrameFunctionalGroupSequence"
		InvokeMacro="USImageDescriptionMacro"
		InvokeMacro="USImageDescriptionMacroForEnhancedUSVolume"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"			Type="1"	VM="1-n"
		InvokeMacro="FrameContentMacro"
		InvokeMacro="PixelMeasuresMacro"				Condition="PixelMeasuresSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="PlanePositionMacro"				Condition="PlanePositionSequenceOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="PlaneOrientationMacro"				Condition="PlaneOrientationSequenceOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="ReferencedImageMacro"				Condition="ReferencedImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="DerivationImageMacro"				Condition="DerivationImageMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="CardiacSynchronizationMacro"		Condition="NeedCardiacSynchronizationMacroInPerFrameFunctionalGroupSequenceRegardlessOfImageType"
		InvokeMacro="FrameVOILUTMacro"					Condition="FrameVOILUTSequenceNotInSharedFunctionalGroupSequence"
		InvokeMacro="RealWorldValueMappingMacro"		Condition="RealWorldValueMappingMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="ContrastBolusUsageMacro"			Condition="NeedContrastBolusUsageMacroInPerFrameFunctionalGroupSequence"
		InvokeMacro="PatientOrientationInFrameMacro"	Condition="PatientOrientationInFrameMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="FrameDisplayShutterMacro"			Condition="FrameDisplayShutterMacroOKInPerFrameFunctionalGroupSequence"
		InvokeMacro="RespiratorySynchronizationMacro"	Condition="NeedRespiratorySynchronizationMacroInPerFrameFunctionalGroupSequenceRegardlessOfImageType"
		InvokeMacro="PlanePositionVolumeMacro"
		InvokeMacro="TemporalPositionMacro"				Condition="TemporalPositionMacroOKInPerFrameFunctionalGroupSequenceAndNotCardiacOrRespiratoryEvent"
		InvokeMacro="ImageDataTypeMacro"				Condition="ImageDataTypeSequenceNotInSharedFunctionalGroupSequence"
	SequenceEnd
ModuleEnd

Module="QTUSEnhancedUltrasoundVolumeProfilePatient"
	Name="IssuerOfPatientID"								Type="1"
ModuleEnd

Module="QTUSEnhancedUltrasoundVolumeProfileStudy"
	Name="StudyDate"										Type="1"
	Name="StudyTime"										Type="1"
	Name="StudyID"											Type="1"
	Name="AccessionNumber"									Type="1"
	Name="StudyDescription"									Type="1"
	Sequence="ProcedureCodeSequence"						Type="1"	VM="1"
		Name="CodeValue"									Type="1"	StringEnumValues="CodeValueForLOINCBreastUltrasound"
		Name="CodingSchemeDesignator"						Type="1"	StringEnumValues="CodingSchemeDesignatorLOINC"
		Name="CodeMeaning"									Type="1"	StringEnumValues="CodeMeaningForLOINCBreastUltrasound"
	SequenceEnd
	Name="PatientSize"										Type="1"
	Name="PatientWeight"									Type="1"
ModuleEnd

Module="QTUSEnhancedUltrasoundVolumeProfileSeries"
	Name="SeriesNumber"										Type="1"
	Name="Laterality"										Type="1"
	Name="SeriesDate"										Type="1"
	Name="SeriesTime"										Type="1"
	Name="SeriesDescription"								Type="1"
	Name="OperatorsName"									Type="1"
	Name="BodyPartExamined"									Type="1"	StringEnumValues="BodyPartExaminedBreast"
ModuleEnd

Module="QTUSEnhancedUltrasoundVolumeProfileFrameOfReference"
	Name="UltrasoundAcquisitionGeometry"					Type="1"	StringEnumValues="UltrasoundAcquisitionGeometryPatient"
	Name="VolumeToTransducerRelationship"					Type="1"	StringEnumValues="VolumeToTransducerRelationshipFixed"

	Name="VolumeToTransducerMappingMatrix"					Type="1"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="0"	BinaryEnumValues="One"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="1"	BinaryEnumValues="Zero"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="2"	BinaryEnumValues="Zero"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="3"	BinaryEnumValues="Zero"

	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="4"	BinaryEnumValues="Zero"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="5"	BinaryEnumValues="One"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="6"	BinaryEnumValues="Zero"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="7"	BinaryEnumValues="Zero"

	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="8"	BinaryEnumValues="Zero"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="9"	BinaryEnumValues="Zero"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="10"	BinaryEnumValues="One"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="11"	BinaryEnumValues="Zero"

	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="12"	BinaryEnumValues="Zero"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="13"	BinaryEnumValues="Zero"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="14"	BinaryEnumValues="Zero"
	Verify="VolumeToTransducerMappingMatrix"							ValueSelector="15"	BinaryEnumValues="One"

	Name="PatientFrameOfReferenceSource"					Type="1"	StringEnumValues="PatientFrameOfReferenceSourceTable"

	Name="TableFrameOfReferenceUID"							Type="1"
	Name="VolumeToTableMappingMatrix"						Type="1"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="0"	BinaryEnumValues="One"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="1"	BinaryEnumValues="Zero"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="2"	BinaryEnumValues="Zero"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="3"	BinaryEnumValues="Zero"

	Verify="VolumeToTableMappingMatrix"									ValueSelector="4"	BinaryEnumValues="Zero"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="5"	BinaryEnumValues="One"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="6"	BinaryEnumValues="Zero"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="7"	BinaryEnumValues="Zero"

	Verify="VolumeToTableMappingMatrix"									ValueSelector="8"	BinaryEnumValues="Zero"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="9"	BinaryEnumValues="Zero"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="10"	BinaryEnumValues="One"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="11"	BinaryEnumValues="Zero"

	Verify="VolumeToTableMappingMatrix"									ValueSelector="12"	BinaryEnumValues="Zero"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="13"	BinaryEnumValues="Zero"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="14"	BinaryEnumValues="Zero"
	Verify="VolumeToTableMappingMatrix"									ValueSelector="15"	BinaryEnumValues="One"

	Name="SynchronizationFrameOfReferenceUID"				Type="1"
	Name="SynchronizationTrigger"							Type="1"	StringEnumValues="SynchronizationTriggerNoTrigger"
	Name="AcquisitionTimeSynchronized"						Type="1"	StringEnumValues="NoLetter"
ModuleEnd

Module="QTUSEnhancedUltrasoundVolumeProfileEquipment"
	Name="Manufacturer"										Type="1"
	Name="InstitutionName"									Type="1"
	Name="InstitutionAddress"								Type="1"
	Name="StationName"										Type="1"
	Name="InstitutionalDepartmentName"						Type="1"
	Name="ManufacturerModelName"							Type="1"
	Name="DeviceSerialNumber"								Type="1"
	Name="SoftwareVersions"									Type="1"
ModuleEnd

Module="QTUSEnhancedUltrasoundVolumeProfileInstance"
	Name="InstanceNumber"									Type="1"
	Name="ContentDate"										Type="1"
	Name="ContentTime"										Type="1"

	Name="ImageType"										Type="1"	VM="4"
	Verify="ImageType"													ValueSelector="0"	StringEnumValues="ImageType1OriginalOnly"
	Verify="ImageType"													ValueSelector="1"	StringEnumValues="ImageType2PrimaryOnly"
	Verify="ImageType"													ValueSelector="2"	StringEnumValues="QTUSImageAndFrameTypeValue3"
	Verify="ImageType"													ValueSelector="3"	StringEnumValues="EmptyValue"

	Name="AcquisitionNumber"								Type="1"
	Name="AcquisitionDateTime"								Type="1"
	Name="BurnedInAnnotation"								Type="1"
	Name="RecognizableVisualFeatures"						Type="1"
	Name="LossyImageCompression"							Type="1"
	Name="PresentationLUTShape"								Type="1"	StringEnumValues="IdentityPresentationLUTShape"

	Name="BitsAllocated"									Type="1"	BinaryEnumValues="BitsAre16"
	Name="BitsStored"										Type="1"	BinaryEnumValues="BitsAre16"
	Name="HighBit"											Type="1"	BinaryEnumValues="BitsAre15"
	Name="PixelRepresentation"								Type="1"	BinaryEnumValues="PixelRepresentationUnsigned"

	Name="PositionMeasuringDeviceUsed"						Type="1"	StringEnumValues="PositionMeasuringDeviceUsedRigid"

	Sequence="ViewCodeSequence"								Type="1"	VM="1"
		Name="CodeValue"									Type="1"	StringEnumValues="CoronalCodeValue"
		Name="CodingSchemeDesignator"						Type="1"	StringEnumValues="CoronalCodingSchemeDesignator"
		Name="CodeMeaning"									Type="1"	StringEnumValues="CoronalCodeMeaning"
	SequenceEnd

	Sequence="AnatomicRegionSequence"						Type="1"	VM="1"
		Name="CodeValue"									Type="1"	StringEnumValues="BreastCodeValue"
		Name="CodingSchemeDesignator"						Type="1"	StringEnumValues="BreastCodingSchemeDesignator"
		Name="CodeMeaning"									Type="1"	StringEnumValues="BreastCodeMeaning"
	SequenceEnd

	Sequence="TransducerScanPatternCodeSequence"			Type="1"	VM="1"
		Name="CodeValue"									Type="1"	StringEnumValues="TransducerScanPatternCodeSequenceCodeValue"
		Name="CodingSchemeDesignator"						Type="1"	StringEnumValues="TransducerScanPatternCodeSequenceCodingSchemeDesignator"
		Name="CodeMeaning"									Type="1"	StringEnumValues="TransducerScanPatternCodeSequenceCodeMeaning"
	SequenceEnd

	Sequence="TransducerGeometryCodeSequence"				Type="1"	VM="1"
		Name="CodeValue"									Type="1"
		Verify="CodeValue"												Condition="ImageTypeValue3IsSoundSpeedOrAttenuation"	StringEnumValues="TransducerGeometryCodeSequenceCodeValueForTransmission"
		Verify="CodeValue"												Condition="ImageTypeValue3IsTissueIntensity"			StringEnumValues="TransducerGeometryCodeSequenceCodeValueForReflection"
		Name="CodingSchemeDesignator"						Type="1"	StringEnumValues="TransducerGeometryCodeSequenceCodingSchemeDesignator"
		Name="CodeMeaning"									Type="1"
		Verify="CodeMeaning"											Condition="ImageTypeValue3IsSoundSpeedOrAttenuation"	StringEnumValues="TransducerGeometryCodeSequenceCodeMeaningForTransmission"
		Verify="CodeMeaning"											Condition="ImageTypeValue3IsTissueIntensity"			StringEnumValues="TransducerGeometryCodeSequenceCodeMeaningForReflection"
	SequenceEnd

	Sequence="TransducerBeamSteeringCodeSequence"			Type="1"	VM="1"
		Name="CodeValue"									Type="1"	StringEnumValues="TransducerBeamSteeringCodeSequenceCodeValue"
		Name="CodingSchemeDesignator"						Type="1"	StringEnumValues="TransducerBeamSteeringCodeSequenceCodingSchemeDesignator"
		Name="CodeMeaning"									Type="1"	StringEnumValues="TransducerBeamSteeringCodeSequenceCodeMeaning"
	SequenceEnd

	Sequence="TransducerApplicationCodeSequence"			Type="1"	VM="1"
		Name="CodeValue"									Type="1"	StringEnumValues="TransducerApplicationCodeSequenceCodeValue"
		Name="CodingSchemeDesignator"						Type="1"	StringEnumValues="TransducerApplicationCodeSequenceCodingSchemeDesignator"
		Name="CodeMeaning"									Type="1"	StringEnumValues="TransducerApplicationCodeSequenceCodeMeaning"
	SequenceEnd

	Sequence="DimensionOrganizationSequence"				Type="1"	VM="1"
		Name="DimensionOrganizationUID"						Type="1"
	SequenceEnd
	Name="DimensionOrganizationType"						Type="1"	StringEnumValues="DimensionOrganizationType3D"
	Sequence="DimensionIndexSequence"						Type="1"	VM="3"
		Name="DimensionIndexPointer"						Type="1"	TagEnumValues="QTUSDimensionOrganization3DDimensionIndexPointerValues"	# do not have sequence item specific selector mechansism so cannot check per item, but can check one of the expected values:(
		Name="FunctionalGroupPointer"						Type="1"	TagEnumValues="QTUSDimensionOrganization3DFunctionalGroupPointerValues"	# do not have sequence item specific selector mechansism so cannot check per item, but can check one of the expected values:(
		Name="DimensionOrganizationUID"						Type="1"
		Name="DimensionDescriptionLabel"					Type="1"	StringEnumValues="QTUSDimensionDescriptionLabel"	# do not have sequence item specific selector mechansism so cannot check per item, but can check one of the expected values:(
	SequenceEnd

	Name="SpecificCharacterSet"								Type="1"	StringEnumValues="SpecificCharacterSetISOIR100"
	Name="InstanceCreationDate"								Type="1"
	Name="InstanceCreationTime"								Type="1"
	Name="InstanceCreatorUID"								Type="1"
	Name="TimezoneOffsetFromUTC"							Type="1"

	Sequence="SharedFunctionalGroupsSequence"				Type="1"	VM="1"
		InvokeMacro="QTUSPixelMeasuresMacro"
		InvokeMacro="PlaneOrientationMacro"
		InvokeMacro="FrameVOILUTMacro"
		InvokeMacro="QTUSRealWorldValueMappingMacro"
		InvokeMacro="PlaneOrientationVolumeMacro"
		InvokeMacro="TemporalPositionMacro"
		InvokeMacro="QTUSTemporalPositionMacro"
		InvokeMacro="QTUSImageDataTypeMacro"
		InvokeMacro="QTUSUSImageDescriptionMacro"
	SequenceEnd

	Sequence="PerFrameFunctionalGroupsSequence"				Type="1"	VM="1-n"
		InvokeMacro="QTUSFrameContentMacro"
		InvokeMacro="PlanePositionMacro"
		InvokeMacro="PlanePositionVolumeMacro"
	SequenceEnd

ModuleEnd

DefineMacro="QTUSFrameContentMacro" InformationEntity="FunctionalGroup"
	Sequence="FrameContentSequence"							Type="1"	VM="1"
		Name="FrameAcquisitionNumber"						Type="1"
		Name="FrameReferenceDateTime"						Type="1"
		Name="FrameAcquisitionDateTime"						Type="1"
		Name="FrameAcquisitionDuration"						Type="1"
		Name="DimensionIndexValues"							Type="1"
		Name="TemporalPositionIndex"						Type="1"	BinaryEnumValues="One"
		Name="StackID"										Type="1"	StringEnumValues="DigitOne"
		Name="InStackPositionNumber"						Type="1"	NotZeroError=""
	SequenceEnd
MacroEnd

DefineMacro="QTUSPixelMeasuresMacro" InformationEntity="FunctionalGroup"
	Sequence="PixelMeasuresSequence"						Type="1"	VM="1"
		Name="PixelSpacing"									Type="1"	NotZeroError=""
		Name="SliceThickness"								Type="1"	NotZeroError=""
		Name="SpacingBetweenSlices"							Type="1"	NotZeroError=""
	SequenceEnd
MacroEnd

DefineMacro="QTUSRealWorldValueMappingMacro" InformationEntity="FunctionalGroup"
	Sequence="RealWorldValueMappingSequence"		Type="1"	VM="1"
		InvokeMacro="QTUSRealWorldValueMappingItemMacro"
	SequenceEnd
MacroEnd

DefineMacro="QTUSRealWorldValueMappingItemMacro" InformationEntity="FunctionalGroup"
	Name="RealWorldValueFirstValueMapped"		Type="1" 	BinaryEnumValues="Zero"
	Name="RealWorldValueLastValueMapped"		Type="1" 	BinaryEnumValues="FFFF"
	Name="RealWorldValueIntercept"				Type="1" 	BinaryEnumValues="Zero"
	Name="RealWorldValueSlope"					Type="1"	# should check scaled values once decided on ... hard to switch on DataType, since in functional group :(
	Name="LUTExplanation"						Type="1"	StringEnumValues="QTUSRealWorldValueMappingLUTExplanation"	# should check scaled values once decided on ... hard to switch on DataType, since in functional group :(
	Name="LUTLabel"								Type="1"	StringEnumValues="QTUSRealWorldValueMappingLUTLabel"	# should check scaled values once decided on ... hard to switch on DataType, since in functional group :(
	Sequence="MeasurementUnitsCodeSequence"		Type="1"	VM="1"	# should check codes once decided on ... hard to switch on DataType, since in functional group :(
		Name="CodeValue"						Type="1"	StringEnumValues="QTUSRealWorldValueMappingMeasurementUnitsCodeValue"
		Name="CodingSchemeDesignator"			Type="1"	StringEnumValues="CodingSchemeDesignatorUCUM"
		Name="CodeMeaning"						Type="1"	StringEnumValues="QTUSRealWorldValueMappingMeasurementUnitsCodeMeaning"
	SequenceEnd
MacroEnd

DefineMacro="QTUSImageDataTypeMacro" InformationEntity="FunctionalGroup"
	Sequence="ImageDataTypeSequence"				Type="1"	VM="1"
		Name="DataType"								Type="1"	StringEnumValues="QTUSEnhancedUSVolumeDataType"
		Verify="DataType"										Condition="ImageTypeValue3IsSoundSpeed"			StringEnumValues="EnhancedUSVolumeDataTypeSoundSpeed"
		Verify="DataType"										Condition="ImageTypeValue3IsAttenuation"		StringEnumValues="EnhancedUSVolumeDataTypeAttenuation"
		Verify="DataType"										Condition="ImageTypeValue3IsTissueIntensity"	StringEnumValues="EnhancedUSVolumeDataTypeTissueIntensity"

		Name="AliasedDataType"						Type="1"	StringEnumValues="NoFull"
		Name="ZeroVelocityPixelValue"				Type="1C"	Condition="ImageTypeValue3IsSoundSpeed"	BinaryEnumValues="Zero"
	SequenceEnd
MacroEnd

DefineMacro="QTUSTemporalPositionMacro" InformationEntity="FunctionalGroup"
	Sequence="TemporalPositionSequence"				Type="1"	VM="1"
		Name="TemporalPositionTimeOffset"			Type="1"  	BinaryEnumValues="Zero"
	SequenceEnd
MacroEnd

DefineMacro="QTUSUSImageDescriptionMacro" InformationEntity="FunctionalGroup"
	Sequence="USImageDescriptionSequence"				Type="1"	VM="1"
		Name="FrameType"								Type="1"	VM="4"
		Verify="FrameType"											ValueSelector="0"	StringEnumValues="ImageType1OriginalOnly"
		Verify="FrameType"											ValueSelector="1"	StringEnumValues="ImageType2PrimaryOnly"
		Verify="FrameType"											ValueSelector="2"	StringEnumValues="QTUSImageAndFrameTypeValue3"
		Verify="FrameType"											Condition="ImageTypeValue3IsSoundSpeed"			ValueSelector="2"	StringEnumValues="QTUSImageAndFrameTypeValue3SoundSpeed"
		Verify="FrameType"											Condition="ImageTypeValue3IsAttenuation"		ValueSelector="2"	StringEnumValues="QTUSImageAndFrameTypeValue3Attenuation"
		Verify="FrameType"											Condition="ImageTypeValue3IsTissueIntensity"	ValueSelector="2"	StringEnumValues="QTUSImageAndFrameTypeValue3SoundSpeed"
		Verify="FrameType"											ValueSelector="3"	StringEnumValues="EmptyValue"
	SequenceEnd
MacroEnd
