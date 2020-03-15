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

DefineMacro="CodeSequenceMeaningOptionalMacro"
	Name="CodeValue"						Type="1"
	Verify="CodeValue"									Condition="CodeValueIllegalOrDeprecated"	ThenErrorMessage="Code Value is illegal or deprecated" ShowValueWithMessage="true"
	Name="CodingSchemeDesignator"			Type="1"	StringDefinedTerms="MiscellaneousCodingSchemeDesignators"
	Verify="CodingSchemeDesignator"						Condition="CodingSchemeDesignatorDeprecated"	ThenWarningMessage="Coding Scheme Designator is deprecated" ShowValueWithMessage="true"
	Name="CodingSchemeVersion"				Type="1C"	Condition="CodingSchemeVersionRequired"
	Name="CodeMeaning"						Type="3"
	Verify="CodeMeaning"								Condition="CodeMeaningEmptyOrNotPresent"	ThenWarningMessage="Code Meaning is missing or empty, which is legal but undesirable"
	Name="ContextIdentifier"				Type="3"
	Name="ContextUID"						Type="3"
	Name="MappingResource"					Type="1C"	Condition="ContextIdentifierIsPresent"
	Name="ContextGroupVersion"				Type="1C"	Condition="ContextIdentifierIsPresent"
	Name="ContextGroupExtensionFlag"		Type="3"	StringEnumValues="YesNoLetter"
	Name="ContextGroupLocalVersion"			Type="1C"	Condition="ExtendedCodingScheme"
	Name="ContextGroupExtensionCreatorUID"	Type="1C"	Condition="ExtendedCodingScheme"
MacroEnd

DefineMacro="CodeSequence99SDMMacro"
	Name="CodeValue"						Type="1"
	Verify="CodeValue"									Condition="CodeValueIllegalOrDeprecated"	ThenErrorMessage="Code Value is illegal or deprecated" ShowValueWithMessage="true"
	Name="CodingSchemeDesignator"			Type="1"	StringEnumValues="CodingSchemeDesignatorForSNOMEDDICOMMicroglossary"
	Name="CodingSchemeVersion"				Type="1C"	Condition="CodingSchemeVersionRequired"
	Name="CodeMeaning"						Type="3"
	Verify="CodeMeaning"								Condition="CodeMeaningEmptyOrNotPresent"	ThenWarningMessage="Code Meaning is missing or empty, which is legal but undesirable"
	Name="ContextIdentifier"				Type="3"
	Name="ContextUID"						Type="3"
	Name="MappingResource"					Type="1C"	Condition="ContextIdentifierIsPresent"
	Name="ContextGroupVersion"				Type="1C"	Condition="ContextIdentifierIsPresent"
	Name="ContextGroupExtensionFlag"		Type="3"	StringEnumValues="YesNoLetter"
	Name="ContextGroupLocalVersion"			Type="1C"	Condition="ExtendedCodingScheme"
	Name="ContextGroupExtensionCreatorUID"	Type="1C"	Condition="ExtendedCodingScheme"
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
	Name="PhotometricInterpretation"	Type="1"	StringEnumValues="PhotometricInterpretationMonochrome2OrRGBorYBR_FULL_422orYBR_RCTorYBR_ICTorYBR_PARTIAL_420"
	Verify="PhotometricInterpretation"				Condition="JPEGTransferSyntaxButNotYBR_FULL_422"			ThenErrorMessage="JPEG transfer syntax is required to have Photometric Interpretation of YBR_FULL422" ShowValueWithMessage="true"
	Verify="PhotometricInterpretation"				Condition="JPEG2000LosslessTransferSyntaxButNotYBR_RCT"		ThenErrorMessage="JPEG 2000 reversible transfer syntax is required to have Photometric Interpretation of YBR_RCT" ShowValueWithMessage="true"
	Verify="PhotometricInterpretation"				Condition="JPEG2000TransferSyntaxButNotYBR_RCTorYBR_ICT"	ThenErrorMessage="JPEG 2000 transfer syntax is required to have Photometric Interpretation of YBR_RCT or YBR_ICT" ShowValueWithMessage="true"
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
