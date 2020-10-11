import re
import pydicom
import pydicom.datadict as Dictionary
import rightdicom.dcmvfy.module_cc as module_cc
import rightdicom.dcmvfy.validate_vr as validate_vr
from numpy import uint32, uint16
from pydicom.dataelem import(
    # FUNCTIONS
    DataElement_from_raw,
    # CLASSES
    DataElement,
    # VARIABLES
    msg,)
from pydicom.dataelem import(
    # FUNCTIONS
    DataElement_from_raw,
    # CLASSES
    DataElement,
    # VARIABLES
    msg,)
from pydicom.dataset import(
    # CLASSES
    Dataset,)
from pydicom.multival import(
    # CLASSES
    MultiValue,)
from pydicom.sequence import(
    # CLASSES
    Sequence,)
from pydicom.tag import(
    # FUNCTIONS
    Tag,)
from pydicom.uid import(
    # CLASSES
    UID,)
from rightdicom.dcmvfy.mesgtext_cc import(
    # FUNCTIONS
    EMsgDC,
    MMsgDC,
    WMsgDC,)
from rightdicom.dcmvfy.sopclc_h import(
    # VARIABLES
    ColorPaletteStorageSOPClassUID,
    HangingProtocolStorageSOPClassUID,
    MediaStorageDirectoryStorageSOPClassUID,
    NuclearMedicineImageStorageSOPClassUID,)


def loopOverListsInSequencesWithLog(a: DataElement, log: list, func) -> bool:
    succeeded = True
    if type(a.value) == Sequence:
        for inner_ds in a.value:
            succeeded = succeeded and func(inner_ds, log)
    elif type(a.value) == Dataset:
        succeeded = succeeded and func(a.value, log)
    return succeeded


def loopOverListsInSequencesWithRootListAndLog(root_ds: Dataset, a: DataElement,
                                               log: list, func) -> bool:
    succeeded = True
    if type(a.value) == Sequence:
        for inner_ds in a.value:
            succeeded = succeeded and func(root_ds, inner_ds, log)
    elif type(a.value) == Dataset:
        succeeded = succeeded and func(root_ds, a.value, log)
    return succeeded


def subcheckScaledNumericValues(coarseName: str,
                                fineName: str,
                                scaleFactor: float,
                                ds: Dataset, log: list):
    success = True
    if coarseName in ds:
        aCoarse = ds[coarseName]
    else:
        return success
    if fineName in ds:
        aFine = ds[fineName]
    else:
        return success
    coarseValue = uint16(aCoarse.value)
    fineValue = float(aFine.value)
    if coarseValue != uint16(fineValue / scaleFactor) and coarseValue != uint16(
            fineValue / scaleFactor):
        message = "{} - {} = {} and {} = {}".format(
            EMsgDC("ScaledNumericValuesForSameConceptAreInconsistent"),
            coarseName, coarseValue, fineName, fineValue)
        log.append(message)
        success = False
    return success


def checkScaledNumericValues(ds: Dataset, log: list):
    success = True
    if not subcheckScaledNumericValues(
            "Exposure", "ExposureInuAs", 1000.0, ds, log):
        success = False
    if not subcheckScaledNumericValues(
            "ExposureTime", "ExposureTimeInuS", 1000.0, ds, log):
        success = False
    if not subcheckScaledNumericValues(
            "XRayTubeCurrent", "XRayTubeCurrentInuA", 1000.0, ds, log):
        success = False
    for(key, elems) in ds.items():
        success = success and loopOverListsInSequencesWithLog(elems, log,
                                                              checkScaledNumericValues)
    return success
# def checkScaledNumericValues ???
def subcheckPatientOrientationValuesForBiped(ds: Dataset, log: list) -> bool:
    success = True
    aPatientOrientation = getElementFromDataset(ds, "PatientOrientation")
    if aPatientOrientation is not None:
        if aPatientOrientation.is_empty:
            return True
        vPatientOrientation = aPatientOrientation.value
        p_orientation = ""
        if type(vPatientOrientation) == MultiValue:
            for i in vPatientOrientation:
                p_orientation += i
        else:
            p_orientation = vPatientOrientation
        regex = '[APRLFH]{2}'
        r = re.match(regex, p_orientation)
        if r is None:
            msg = "{} - {} - only L, R, A, P, H or F permitted".format(
                EMsgDC("IllegalCharacterInPatientOrientation"), p_orientation)
            log.append(msg)
            success = False
        msg = "{} - {}".format(
            EMsgDC(
                "ConflictingDirectionsInPatientOrientationCannotBePresentInSameValue"),
            "{}")
        if 'A' in p_orientation and 'P' in p_orientation:
            log.append(msg.format("A, P"))
            success = False
        if 'R' in p_orientation and 'L' in p_orientation:
            log.append(msg.format("R, L"))
            success = False
        if 'F' in p_orientation and 'H' in p_orientation:
            log.append(msg.format("F, H"))
            success = False
        if p_orientation[0] == p_orientation[1]:
            msg = "{} - /{}/ and /{}/".format(
                EMsgDC("PatientOrientationRowAndColumnDirectionsCannotBeIdentical"),
                p_orientation[0], p_orientation[1])
            log.append(msg)
            success = False
    for(key, elems) in ds.items():
        success = success and loopOverListsInSequencesWithLog(
            elems, log, subcheckPatientOrientationValuesForBiped)
    return success


def checkPatientOrientationValuesForBipedOrQuadruped(ds: Dataset, log: list) -> bool:
    quadruped = False
    aAnatomicalOrientationType = getElementFromDataset(ds, 'AnatomicalOrientationType')
    if aAnatomicalOrientationType is not None:
        if aAnatomicalOrientationType.value == "QUADRUPED":
            quadruped = True
    return subcheckPatientOrientationValuesForQuadruped(ds, log) \
        if quadruped else subcheckPatientOrientationValuesForBiped(ds, log)


def subcheckQuadrupedValidity(direction) -> str:
    if len(direction) <= 0 or len(direction) >= 3:
        return ''
    TwoLetters = ['CD',  # (Cd or Caudal)
                  'CR',  # (Cr or Cranial)
                  'DI',  # (Di or Distal)
                  'LE',  # (Le or Left)
                  'PA',  # (Pa or Palmar)
                  'PL',  # (Pl or Plantar
                  'PR',  # (Pr or Proximal)
                  'RT',  # (Rt or Right)
                  ]
    OneLetter = ['D',  # (Dorsal)
                 'L ',  # (Lateral)
                 'M ',  # (Medial)
                 'R ',  # (Rostral)
                 'V ',  # (Ventra
                 ]
    direction_has_two_letters = False
    direction_has_one_letter = False
    for pos in TwoLetters:
        if pos == direction:
            direction_has_two_letters = True
            break
    if not direction_has_two_letters:
        direction = direction[0]
        for pos in OneLetter:
            if pos == direction:
                direction_has_one_letter = True
                break
    if not(direction_has_one_letter or direction_has_two_letters):
        return ''
    return direction


def subcheckPatientOrientationValuesForQuadruped(ds: Dataset, log: list) -> bool:
    success = True
    aPatientOrientation = getElementFromDataset(ds, "PatientOrientation")
    if aPatientOrientation is not None:
        if aPatientOrientation.is_empty:
            return True
        vPatientOrientation = aPatientOrientation.value
        p_orientation = ""
        if type(vPatientOrientation) == MultiValue:
            for i in vPatientOrientation:
                p_orientation += i
        else:
            p_orientation = vPatientOrientation
        msg = "{} - {} - {}"
        msg_g = msg.format(
            EMsgDC(
                "ConflictingDirectionsInPatientOrientationCannotBePresentInSameValue"),
            "{}", "")
        msg_badval = msg.format(
            EMsgDC("IllegalCharacterInPatientOrientation"), "{}",
            "only CD, CR, D, DI, L, LE, M, PA, PL, PR, R, RT or V permitted for quadruped")
        row_dir = subcheckQuadrupedValidity(p_orientation[0:2])
        if len(row_dir) == 0:
            log.append(msg_badval.format(p_orientation))
            success = False
        col_dir = subcheckQuadrupedValidity(p_orientation[len(row_dir):])
        if len(col_dir) == 0:
            log.append(msg_badval.format(p_orientation))
            success = False
        if col_dir == row_dir:
            msg_eq = msg.format(
                EMsgDC("PatientOrientationRowAndColumnDirectionsCannotBeIdentical"),
                "/{}/".format(col_dir), "/{}/".format({row_dir}))
            success = False
        if col_dir == 'CR' and row_dir == 'CD':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        if col_dir == 'CD' and row_dir == 'CR':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        # -------------------------------------------------------
        if col_dir == 'LE' and row_dir == 'RT':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        if col_dir == 'RT' and row_dir == 'LE':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        # -------------------------------------------------------
        if col_dir == 'L' and row_dir == 'M':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        if col_dir == 'M' and row_dir == 'L':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        # -------------------------------------------------------
        if col_dir == 'D' and row_dir == 'V':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        if col_dir == 'V' and row_dir == 'D':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        # -------------------------------------------------------
        if col_dir == 'DI' and row_dir == 'PR':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        if col_dir == 'PR' and row_dir == 'DI':
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        # -------------------------------------------------------
        if col_dir == "R" and row_dir == "CD":
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        if col_dir == "CD" and row_dir == "R":
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        # -------------------------------------------------------
        if col_dir == "R" and row_dir == "CR":
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        if col_dir == "CR" and row_dir == "R":
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        # -------------------------------------------------------
        if col_dir == "PA" and row_dir == "PL":
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
        if col_dir == "PL" and row_dir == "PA":
            log.append(msg_g.format("{}, {}".format(col_dir, row_dir)))
            success = False
    for(key, elems) in ds.items():
        success = success and loopOverListsInSequencesWithLog(
            elems, log, subcheckPatientOrientationValuesForQuadruped)
    return success


def checkUIDs(ds: Dataset, log: list) -> bool:
    for(key, elems) in ds.items():
        if type(elems.value) == UID:
            unique_id = elems.value
            if len(unique_id) < 2:
                msg = "{} - {} = \\{}\\".format(
                    EMsgDC("IllegalRootForUID"), key, unique_id)
                return False
            if not(unique_id[0:2] == '1.' or unique_id[0:2] == '2.'):
                msg = "{} - {} = \\{}\\".format(
                    EMsgDC("IllegalRootForUID"), key, unique_id)
                return False
            if len(unique_id) > 5:
                if unique_id[0:5] == '2.999':
                    msg = "{} - {} = \\{}\\".format(
                        EMsgDC("ExampleRootForUID"), key, unique_id)
                    log.append(msg)
                    return False
        return loopOverListsInSequencesWithLog(
            elems, log, checkUIDs)
# def checkNoEmptyReferencedFileIDComponents(ds:Dataset, log:list) -> bool:



def checkNoIllegalOddNumberedGroups(ds: Dataset, log: list) -> bool:
    success = True
    for(key, elems) in ds.items():
        group = elems.tag.group
        element = elems.tag.element
        if group == 0x0001 or group == 0x0003 or \
                group == 0x0005 or group == 0x0007:
            msg = "{} - ({}, {})".format(
                EMsgDC("BadGroup", group, element))
            log.append(msg)
            success = False
            if not loopOverListsInSequencesWithLog(
                    elems, log, checkNoIllegalOddNumberedGroups):
                success = False
    return success


def subcheckHasStringValueElseWarning(ds: Dataset, Keyword: str, Label: str,
                                      log: list) -> bool:
    success = True
    if Keyword in ds:
        elem = ds[Keyword]
        if elem.VM == 0:
            success = False
    else:
        success = False
    if not success:
        log.append("{} - {}".format(
            WMsgDC("MissingAttributeValueNeededForDirectory"), Label
       ))
    return success


def checkValuesNeededToBuildDicomDirectoryArePresentAndNotEmpty(ds: Dataset,
                                                                log: list) -> bool:
    success = True
    vSOPClassUID = ""
    aSOPClassUID = getElementFromDataset(ds, "SOPClassUID")
    aDirectoryRecordSequence = getElementFromDataset(ds, "DirectoryRecordSequence")
    if aSOPClassUID is not None:
        vSOPClassUID = aSOPClassUID.value
    if aDirectoryRecordSequence is None and\
           (vSOPClassUID == "" or\
            (vSOPClassUID != HangingProtocolStorageSOPClassUID and\
              vSOPClassUID != ColorPaletteStorageSOPClassUID)):
            success = success and subcheckHasStringValueElseWarning(
                ds, "PatientID", "Patient ID", log) and success
            success = success and subcheckHasStringValueElseWarning(
                ds, "StudyDate", "StudyDate", log) and success
            success = success and subcheckHasStringValueElseWarning(
                ds, "StudyTime", "Study Time", log) and success
            success = success and subcheckHasStringValueElseWarning(
                ds, "StudyID", "Study ID", log) and success
            success = success and subcheckHasStringValueElseWarning(
                ds, "Modality", "Modality", log) and success
            success = success and subcheckHasStringValueElseWarning(
                ds, "SeriesNumber", "Series Number", log) and success
            if "PixelData" in ds:
                success = success and subcheckHasStringValueElseWarning(
                    ds, "InstanceNumber", "Instance Number", log) and success
    return success


def checkPresentationStateDisplayedAreaSelectionValuesAreValid(ds: Dataset,
                                                               log: list) -> bool:
    success = True
    imageRotation = uint16(0)
    kw = "ImageRotation"
    if kw in ds:
        aImageRotation = ds[kw]
    imageHorizontalFlip = False
    kw = "ImageHorizontalFlip"
    if kw in ds:
        aImageHorizontalFlip = ds[kw]
        if aImageHorizontalFlip == "Y":
            imageHorizontalFlip = True
    kw = "DisplayedAreaSelectionSequence"
    if kw in ds:
        aDisplayedAreaSelectionSequence = ds[kw]
        for item in aDisplayedAreaSelectionSequence:
            kw = "DisplayedAreaTopLeftHandCorner"
            if kw in ds:
                aDisplayedAreaTopLeftHandCorner = ds[kw]
            else:
                aDisplayedAreaTopLeftHandCorner = None
            kw = "DisplayedAreaBottomRightHandCorner"
            if kw in ds:
                aDisplayedAreaBottomRightHandCorner = ds[kw]
            else:
                aDisplayedAreaBottomRightHandCorner = None
            if aDisplayedAreaBottomRightHandCorner is not None and \
                    aDisplayedAreaBottomRightHandCorner.VM == 2 and \
                    aDisplayedAreaTopLeftHandCorner is not None and \
                    aDisplayedAreaTopLeftHandCorner.VM == 2:
                tlhcX = aDisplayedAreaTopLeftHandCorner[0]
                tlhcY = aDisplayedAreaTopLeftHandCorner[1]
                brhcX = aDisplayedAreaBottomRightHandCorner[0]
                brhcY = aDisplayedAreaBottomRightHandCorner[1]
                if imageRotation != 0 and imageHorizontalFlip:
                    minX = tlhcX if tlhcX < brhcX else brhcX
                    maxX = tlhcX if tlhcX > brhcX else brhcX
                    minY = tlhcY if tlhcY < brhcY else brhcY
                    maxY = tlhcY if tlhcY > brhcY else brhcY
                    x = int32([minX, maxX, maxX, minX])
                    y = int32([minY, minY, maxY, maxY])
                    useRotation = uint16(imageRotation % 360)
                    nNinety = uint16(useRotation / 90)
                    if nNinety > 0:
                        for r in range(0, nNinety):
                            holdX = x[3]
                            holdY = y[3]
                            for corner in range(3, 0, -1):
                                x[corner] = x[corner - 1]
                                y[corner] = y[corner - 1]
                            x[0] = holdX
                            y[0] = holdY
                    tlhcXExpected = x[1] if imageHorizontalFlip else x[0]
                    tlhcYExpected = y[1] if imageHorizontalFlip else y[0]
                    brhcXExpected = x[3] if imageHorizontalFlip else x[2]
                    brhcYExpected = y[3] if imageHorizontalFlip else y[2]
                    msg = '{} - DisplayedAreaTopLeftHandCorner = ({}, {}) ' \
                          'does not match expected value after rotation of {} ' \
                          'degrees and {} horizontal flip ({}, {})'
                    if tlhcX != tlhcXExpected or tlhcY != tlhcYExpected:
                        msg = msg.format(
                            EMsgDC(
                                "DisplayedAreaSelectionSequenceInternallyInconsistent"),
                            tlhcX, tlhcY, imageRotation,
                            "" if imageHorizontalFlip else "no",
                            tlhcXExpected, tlhcYExpected)
                        log.append(msg)
                        success = False
                    if brhcX != brhcXExpected or brhcY != brhcYExpected:
                        msg = msg.format(
                            EMsgDC(
                                "DisplayedAreaSelectionSequenceInternallyInconsistent"),
                            brhcX, brhcY, imageRotation,
                            "" if imageHorizontalFlip else "no",
                            brhcXExpected, brhcYExpected)
                        log.append(msg)
                        success = False
                elif tlhcX >= brhcX or tlhcY >= brhcY:
                    msg = '{} - DisplayedAreaTopLeftHandCorner = ({}, {}) ' \
                          'is not above the left of ' \
                          'DisplayedAreaBottomRightHandCorner = ({}, {})'
                    msg = msg.format(
                        EMsgDC(
                            "DisplayedAreaSelectionSequenceInternallyInconsistent"),
                        tlhcX, tlhcY, brhcX, brhcY)
                    log.append(msg)
                    success = False
    return success


def checkWaveformSequenceIsInternallyConsistent(ds: Dataset, log: list) -> bool:
    success = True
    kw = "WaveformSequence"
    if kw in ds:
        aWaveformSequence = ds[kw]
        for multiplexGroup in aWaveformSequence:
            kw = "NumberOfWaveformChannels"
            if kw in ds:
                aNumberOfWaveformChannels = ds[kw]
            else:
                aNumberOfWaveformChannels = None
            kw = "ChannelDefinitionSequence"
            if kw in ds:
                aChannelDefinitionSequence = ds[kw]
            else:
                aChannelDefinitionSequence = None
            if aNumberOfWaveformChannels is not None and \
                    aChannelDefinitionSequence is not None:
                if aNumberOfWaveformChannels != len(aChannelDefinitionSequence):
                    success = False
                    msg = '{} - NumberOfWaveformChannels = {} but number of ' \
                          'ChannelDefinitionSequence Items = {}'
                    msg = msg.format(
                        EMsgDC("WaveformSequenceInternallyInconsistent"),
                        aNumberOfWaveformChannels.value,
                        len(aChannelDefinitionSequence)
                   )
                    log.append(msg)
    return success


def getElementFromDataset(ds: Dataset, keyword: str) -> DataElement:
    if keyword in ds:
        return ds[keyword]
    else:
        return None


def getAttributeValue(ds: Dataset, keyword: str, default=0):
    attrib = getElementFromDataset(ds, keyword)
    if attrib is None:
        return default
    else:
        if type(attrib) == MultiValue:
            return attrib.value[0]
        else:
            return attrib.value


def checkPixelDataIsTheCorrectLength(ds: Dataset, log: list) -> bool:
    success = True
    aPixelData = getElementFromDataset(ds, "PixelData")
    if aPixelData is not None:
        vl = uint32(len(aPixelData.value))
        vRows = uint16(getAttributeValue(ds, "Rows"))
        vColumns = uint16(getAttributeValue(ds, "Columns"))
        vBitsAllocated = uint16(getAttributeValue(ds, "BitsAllocated"))
        vBitsStored = uint16(getAttributeValue(ds, "BitsStored"))
        vSamplesPerPixel = uint16(getAttributeValue(ds, "SamplesPerPixel", 1))
        vNumberOfFrames = uint16(getAttributeValue(ds, "NumberOfFrames", 1))
        useBits = (16 if vBitsStored == 0 else((vBitsStored - 1) / 8 + 1) * 8) \
            if vBitsAllocated == 0 else vBitsAllocated
        if useBits % 8 == 0:
            useBytes = useBits / 8
            expectedLength = uint32(uint32(vRows) * uint32(vColumns) *
                                    useBytes * vNumberOfFrames * vSamplesPerPixel)
        else:
            expectedLength = uint32(
               (uint32(vRows) * uint32(vColumns) * useBits *
                 vNumberOfFrames * vSamplesPerPixel - 1) / 8 + 1)
        if expectedLength % 2 == 1:
            + +expectedLength  # odd lengths are always padded by one byte to even ([bugs.dicom3tools] (000113))
        if vl != expectedLength:
            msg = "{} - {} {} - {} {}".format(
                EMsgDC("PixelDataIncorrectVL"), MMsgDC("Expected"),
                expectedLength, MMsgDC("Got"), vl)
            log.append(msg)
            success = False
    return success


def checkPixelAspectRatioValidIfPresent(ds: Dataset, log: list) -> bool:
    success = True
    aPixelAspectRatio = getElementFromDataset(ds, "PixelAspectRatio")
    if aPixelAspectRatio is not None:
        value = aPixelAspectRatio.value
        length = len(value)
        if length == 2:
            if value[0] == value[1]:
                msg = '{} - - values are {}\\{}'.format(
                    EMsgDC("PixelAspectRatioNotPermittedWhenOneToOne"),
                    value[0], value[1])
                log.append(msg)
                success = False
    return success


def checkEstimatedRadiographicMagnificationFactorIfPresent(ds: Dataset,
                                                           log: list) -> bool:
    success = True
    aEstimatedRadiographicMagnificationFactor = \
        getElementFromDataset(ds, "EstimatedRadiographicMagnificationFactor")
    aDistanceSourceToDetector = getElementFromDataset(ds,
                                                      "DistanceSourceToDetector")
    aDistanceSourceToPatient = getElementFromDataset(ds,
                                                     "DistanceSourceToPatient")
    if aEstimatedRadiographicMagnificationFactor is not None and \
            aDistanceSourceToDetector is not None and \
            aDistanceSourceToPatient is not None:
        vEstimatedRadiographicMagnificationFactor = \
            aEstimatedRadiographicMagnificationFactor.value
        vDistanceSourceToDetector = aDistanceSourceToDetector.value
        vDistanceSourceToPatient = aDistanceSourceToPatient.value
        if vDistanceSourceToPatient > 0 and \
                abs(vDistanceSourceToDetector / vDistanceSourceToPatient - \
                    vEstimatedRadiographicMagnificationFactor) > 0.0001:
            msg = "{} - values are {}, {}, {}".format(
                WMsgDC(
                    "EstimatedRadiographicMagnificationFactorDoesNot"
                    "MatchRatioOfDistanceSourceTo"
                    "DetectorAndDistanceSourceToPatient"),
                vEstimatedRadiographicMagnificationFactor,
                vDistanceSourceToDetector,
                vDistanceSourceToPatient)
            log.append(msg)
    return success


def subcheckUnitVector(elem: DataElement, valueOffset: int, whichVector: str,
                       tagName: str, log: list) -> bool:
    success = True
    a = elem.value
    if type(a) == MultiValue:
        length = len(a)
        if valueOffset + 2 < length:
            x = a[valueOffset]
            y = a[valueOffset + 1]
            z = a[valueOffset + 2]
            sumOfSquares = x * x + y * y + z * z
            if abs(sumOfSquares - 1) > 0.0001:
                success = False
                msg = '{} for {} vector of {} - values are {}\\{}\\{}'
                msg = msg.format(EMsgDC('OrientationVectorIsNotUnitVector'),
                                 whichVector, tagName, x, y, z)
                log.append(msg)
    return success


def subcheckOrthogonal(elem1: DataElement, valueOffset1: int, whichVector1: str,
                       tagName1: str,
                       elem2: DataElement, valueOffset2: int, whichVector2: str,
                       tagName2: str
                      , log: list) -> bool:
    success = True
    a1 = elem1.value
    a2 = elem2.value
    if type(a1) == MultiValue and type(a2) == MultiValue:
        length1 = len(a1)
        length2 = len(a2)
        if valueOffset1 + 2 < length1 and valueOffset2 + 2 < length2:
            x1 = a1[valueOffset1]
            y1 = a1[valueOffset1 + 1]
            z1 = a1[valueOffset1 + 2]
            x2 = a2[valueOffset2]
            y2 = a2[valueOffset2 + 1]
            z2 = a2[valueOffset2 + 2]
            dotProduct = x1 * x2 + y1 * y2 + z1 * z2
            if abs(dotProduct) > 0.0001:
                success = False
                msg = '{} for {} vector of {} - values are {}\\{}\\{}' \
                      ' and for {} vector of {} - values are {}\\{}\\{}'
                msg = msg.format(EMsgDC("OrientationVectorsAreNotOrthogonal"),
                                 whichVector1, tagName1, x1, y1, z1,
                                 whichVector2, tagName2, x2, y2, z2)
                log.append(msg)
    return success


def checkOrientationsAreOrthogonal(ds: Dataset, log: list) -> bool:
    success = True
    aImageOrientationPatient = getElementFromDataset(ds,
                                                     "ImageOrientationPatient")
    if aImageOrientationPatient is not None:
        success = success and subcheckOrthogonal(
            aImageOrientationPatient, 0, 'row', 'ImageOrientationPatient',
            aImageOrientationPatient, 3, 'column', 'ImageOrientationPatient',
            log)
    aImageOrientation = getElementFromDataset(ds,
                                              "ImageOrientation")
    if aImageOrientation is not None:
        success = success and subcheckOrthogonal(
            aImageOrientation, 0, 'row', 'ImageOrientation',
            aImageOrientation, 0, 'column', 'ImageOrientation',
            log)
    for(key, elems) in ds.items():
        success = success and loopOverListsInSequencesWithLog(
            elems, log, checkOrientationsAreOrthogonal)
    return success


def checkOrientationsAreUnitVectors(ds: Dataset, log: list) -> bool:
    success = True
    aImageOrientationPatient = getElementFromDataset(ds,
                                                     "ImageOrientationPatient")
    if aImageOrientationPatient is not None:
        success = success and subcheckUnitVector(
            aImageOrientationPatient, 0, 'row', 'ImageOrientationPatient', log)
        success = success and subcheckUnitVector(
            aImageOrientationPatient, 3, 'column', 'ImageOrientationPatient',
            log)
    # ---------------------------------------------------------------------------
    aImageOrientation = getElementFromDataset(ds,
                                              "ImageOrientation")
    if aImageOrientation is not None:
        success = success and subcheckUnitVector(
            aImageOrientation, 0, 'row', 'ImageOrientation', log)
        success = success and subcheckUnitVector(
            aImageOrientation, 3, 'column', 'ImageOrientation',
            log)
    # ---------------------------------------------------------------------------
    aImageOrientationSlide = getElementFromDataset(ds,
                                                   "ImageOrientationSlide")
    if aImageOrientationSlide is not None:
        success = success and subcheckUnitVector(
            aImageOrientationSlide, 0, 'row', 'ImageOrientationSlide', log)
        success = success and subcheckUnitVector(
            aImageOrientationSlide, 3, 'column', 'ImageOrientationSlide',
            log)
    # ---------------------------------------------------------------------------
    aControlPointOrientation = getElementFromDataset(ds,
                                                     "ControlPointOrientation")
    if aControlPointOrientation is not None:
        success = success and subcheckUnitVector(
            aControlPointOrientation, 0, '', 'ControlPointOrientation', log)
    # ---------------------------------------------------------------------------
    aSlabOrientation = getElementFromDataset(ds,
                                             "SlabOrientation")
    if aSlabOrientation is not None:
        success = subcheckUnitVector(
            aSlabOrientation, 0, '', 'SlabOrientation', log)
    # ---------------------------------------------------------------------------
    aVelocityEncodingDirection = getElementFromDataset(ds,
                                                       "VelocityEncodingDirection")
    if aVelocityEncodingDirection is not None:
        success = success and subcheckUnitVector(
            aVelocityEncodingDirection, 0, '', 'VelocityEncodingDirection', log)
    for(key, elems) in ds.items():
        success = success and loopOverListsInSequencesWithLog(
            elems, log, checkOrientationsAreUnitVectors)
    return success


def checkPixelSpacingCalibration(ds: Dataset, log: list) -> bool:
    success = True
    aPixelSpacing = getElementFromDataset(ds, "PixelSpacing")
    aImagerPixelSpacing = getElementFromDataset(ds, "ImagerPixelSpacing")
    aNominalScannedPixelSpacing = getElementFromDataset(ds,
                                                        "NominalScannedPixelSpacing")
    aPixelSpacingCalibrationType = getElementFromDataset(ds,
                                                         "PixelSpacingCalibrationType")
    if aPixelSpacing is not None and aPixelSpacingCalibrationType is not None:
        vPixelSpacingRow = aPixelSpacing.value[0]
        vPixelSpacingCol = aPixelSpacing.value[1]
        if aImagerPixelSpacing is not None:
            vImagerPixelSpacingRow = aImagerPixelSpacing.value[0]
            vImagerPixelSpacingCol = aImagerPixelSpacing.value[1]
            if vPixelSpacingRow != vImagerPixelSpacingRow or \
                    vPixelSpacingCol != vImagerPixelSpacingCol:
                msg = "{} - PixelSpacing = {}\\{} versus ImagerPixelSpacing = {}\\{}"
                msg = msg.format(
                    WMsgDC("PixelSpacingDoesNotMatchImagerPixel"
                           "SpacingButPixelSpacingCalibrationTypeNotPresent"),
                    vPixelSpacingRow, vPixelSpacingCol,
                    vImagerPixelSpacingRow, vImagerPixelSpacingCol)
                log.append(msg)
        if aNominalScannedPixelSpacing is not None:
            vNominalScannedPixelSpacingRow = aNominalScannedPixelSpacing.value[
                0]
            vNominalScannedPixelSpacingCol = aNominalScannedPixelSpacing.value[
                1]
            if vPixelSpacingRow != vNominalScannedPixelSpacingRow or \
                    vPixelSpacingCol != vNominalScannedPixelSpacingCol:
                msg = "{} - PixelSpacing = {}\\{} versus NominalScannedPixelSpacing = {}\\{}"
                msg = msg.format(
                    WMsgDC("PixelSpacingDoesNotMatchNominalScannedPixel"
                           "SpacingButPixelSpacingCalibrationTypeNotPresent"),
                    vPixelSpacingRow, vPixelSpacingCol,
                    vNominalScannedPixelSpacingRow,
                    vNominalScannedPixelSpacingCol)
                log.append(msg)
    return success


def checkSpacingBetweenSlicesIsNotNegative(ds: Dataset, log: list) -> bool:
    success = True
    aSpacingBetweenSlices = getElementFromDataset(ds, "SpacingBetweenSlices")
    if aSpacingBetweenSlices is not None:
        vSpacingBetweenSlices = aSpacingBetweenSlices.value
        if vSpacingBetweenSlices < 0:
            aSOPClassUID = getElementFromDataset(ds, "SOPClassUID")
            if aSOPClassUID is not None:
                if aSOPClassUID.value != NuclearMedicineImageStorageSOPClassUID:
                    msg = "{} - SpacingBetweenSlices = {}"
                    msg = msg.format(EMsgDC("IllegalNegativeValue"),
                                     vSpacingBetweenSlices)
                    log.append(msg)
                    success = False
    return success


def checkFrameIncrementPointerValuesValid(ds: Dataset, log: list) -> bool:
    success = True
    aFrameIncrementPointer = getElementFromDataset(ds, "FrameIncrementPointer")
    if aFrameIncrementPointer is not None:
        for(value, i) in zip(aFrameIncrementPointer.value,
                              range(len(aFrameIncrementPointer.value))):
            if type(value) == Tag:
                if value not in ds:
                    success = False
                    msg = "{} - for value {} which is ({}, {})"
                    msg = msg.format(
                        EMsgDC("FrameIncrementPointerValueNotPresentInDataset"),
                        i, value.group, velue.element)
                    log.append(msg)
    return success


def checkFrameVectorCountsValid(ds: Dataset, log: list) -> bool:
    success = True
    aNumberOfFrames = getElementFromDataset(ds, "NumberOfFrames")
    if aNumberOfFrames is not None:
        vNumberOfFrames = aNumberOfFrames.value
    else:
        vNumberOfFrames = 1
    vectorTags = [
        "EnergyWindowVector",
        "DetectorVector",
        "PhaseVector",
        "RotationVector",
        "RRIntervalVector",
        "TimeSlotVector",
        "SliceVector",
        "AngularViewVector"
    ]
    numberTags = [
        "NumberOfEnergyWindows",
        "NumberOfDetectors",
        "NumberOfPhases",
        "NumberOfRotations",
        "NumberOfRRIntervals",
        "NumberOfTimeSlots",
        "NumberOfSlices",
        "TimeSliceVector"
    ]
    nTags = len(numberTags)
    for i in range(0, nTags):
        aVector = getElementFromDataset(ds, vectorTags[i])
        if aVector is not None:
            nValues = len(aVector.value)
            if nValues != vNumberOfFrames:
                msg = "{} for Attribute {} = ({}, {}), which has {} " \
                      "values though Number of Frames is {}"
                msg = msg.format(
                    EMsgDC("NumberOfValuesInVectorDoesNotMatchNumberOfFrames"),
                    vectorTags[i], aVector.tag.group, aVector.tag.element,
                    nValues, vNumberOfFrames)
                log.append(msg)
                success = False
            aNumber = getElementFromDataset(ds, numberTags[i])
            if aNumber is not None:
                vNumber = aNumber.value
                if nValues > 0:
                    lowestValueFound = min(aVector.value)
                    highestValueFound = max(aVector.value)
                    if highestValueFound != vNumber:
                        msg = "{} for Attribute {} = ({}, {}), which has value" \
                              " {}, whereas the highest value found in " \
                              "{} = ({}, {}) is {}"
                        msg = msg.format(
                            EMsgDC(
                                "SpecifiedNumberOfVectorValuesDoesNotMatchActualValuesInVector"),
                            numberTags[i], aNumber.tag.group,
                            aNumber.tag.element, vNumber,
                            vectorTags[i], aVector.tag.group,
                            aVector.tag.element, highestValueFound)
                        log.append(msg)
                        success = False
                    if lowestValueFound != 1:
                        msg = "{} for Attribute {} = ({}, {}), but rather is {}"
                        msg = msg.format(
                            EMsgDC("LowestValueInVectorIsNotOne"),
                            vectorTags[i], aVector.tag.group,
                            aVector.tag.element,
                            lowestValueFound)
                        log.append(msg)
                        success = False
    return success


def checkMetaInformationMatchesSOPInstance(ds: Dataset, log: list) -> bool:
    success = True
    aMediaStorageSOPInstanceUID = getElementFromDataset(
        ds, "MediaStorageSOPInstanceUID")
    aMediaStorageSOPClassUID = getElementFromDataset(ds,
                                                     "MediaStorageSOPClassUID")
    aSOPInstanceUID = getElementFromDataset(ds, "SOPInstanceUID")
    aSOPClassUID = getElementFromDataset(ds, "SOPClassUID")
    aDirectoryRecordSequence = getElementFromDataset(ds,
                                                     "DirectoryRecordSequence")
    if aMediaStorageSOPInstanceUID is not None:
        if aSOPInstanceUID is not None:
            vMediaStorageSOPInstanceUID = aMediaStorageSOPInstanceUID.value
            vSOPInstanceUID = aSOPInstanceUID.value
            #
            # v = a.value
            if vMediaStorageSOPInstanceUID != vSOPInstanceUID:
                success = False
                log.append(EMsgDC(
                    "MediaStorageSOPInstanceUIDDifferentFromSOPInstanceUID"))
        elif aDirectoryRecordSequence is None:
            success = False
            log.append(EMsgDC("MediaStorageSOPInstanceUID"
                              "ButMissingSOPInstanceUIDAndNotADirectory"))
    if aMediaStorageSOPClassUID is not None:
        vMediaStorageSOPClassUID = aMediaStorageSOPClassUID.value
        if aSOPClassUID is not None:
            vSOPClassUID = aSOPClassUID.value
            if vMediaStorageSOPClassUID != vSOPClassUID:
                success = False
                log.append(EMsgDC("MediaStorageSOPClass"
                                  "UIDDifferentFromSOPClassUID"))
        elif vMediaStorageSOPClassUID != MediaStorageDirectoryStorageSOPClassUID:
            success = False
            log.append(EMsgDC("MediaStorageSOPClassUIDNot"
                              "MediaStorageDirectoryStorageSOPClassUID"))
        else:
            success = False
            log.append(EMsgDC("MediaStorageSOPClassUID"
                              "ButMissingSOPClassUIDAndNotADirectory"))
    return success


def subcheckLUTDataValuesMatchSpecifiedRange(ds: Dataset, descriptorTag: str,
                                             dataTag: str, message: str,
                                             log: str) -> bool:
    success = True
    aLUTDescriptor = getElementFromDataset(ds, descriptorTag)
    aLUTData = getElementFromDataset(ds, dataTag)
    if aLUTDescriptor is not None:
        if aLUTDescriptor.VM == 3:
            numberOfEntries = aLUTDescriptor.value[0]
            numberOfBits = aLUTDescriptor.value[2]
            foundValuesToCheck = False
            actualNumberOfEntries = 0x10000 if numberOfEntries == 0 \
                else(uint32(numberOfEntries) & 0xffff)
            wantMaxValueMax = uint16((uint32(1) << numberOfBits) - 1)
            wantMaxValueMin = uint16(uint32(1) <<(numberOfBits - 1))
            if aLUTData is not None:
                maxValue = uint16(0)
                nLUTData = len(aLUTData.value)
                if nLUTData == 0:
                    foundValuesToCheck = False
                else:
                    foundValuesToCheck = True
                if numberOfBits > 8:
                    maxValue = max(aLUTData.value)
                    if foundValuesToCheck:
                        if nLUTData != actualNumberOfEntries:
                            msg = "{} - {} - LUT Descriptor number of entries = {}  " \
                                  "but number of 16 bit values = {} "
                            msg = msg.format(EMsgDC("LUTDataWrongLength"),
                                             message,
                                             actualNumberOfEntries,
                                             nLUTData)
                            log.append(msg)
                            success = False
                else:
                    for item in aLUTData.value:
                        lowbyte = item & 0xff
                        maxValue = lowbyte if lowbyte > maxValue else maxValue
                        highbyte = (item >> 8) & 0xff
                        maxValue = highbyte if highbyte > maxValue else maxValue
                        if foundValuesToCheck:
                            if nLUTData * 2 != actualNumberOfEntries:
                                msg = "{} - {} - LUT Descriptor number of entries = {}  " \
                                      "but number of 8 bit values = {} " \
                                      "packed into {} 16 bit words"
                                msg = msg.format(EMsgDC("LUTDataWrongLength"),
                                                 message,
                                                 actualNumberOfEntries,
                                                 nLUTData * 2,
                                                 nLUTData)
                                log.append(msg)
                                success = False
            if foundValuesToCheck:
                if maxValue < wantMaxValueMin or maxValue > wantMaxValueMax:
                    msg = "{} - {} - LUT Descriptor number of bits = {} but maximum LUT Data value is 0x{:04x}"
                    msg = msg.format(EMsgDC("LUTDataBad"), message,
                                     numberOfBits, maxValue)
                    log.append(msg)
                    success = False
    return success


def subcheckLUTDataValuesMatchSpecifiedRange_seq(ds: Dataset, sequenceTag: str,
                                                 descriptorTag: str,
                                                 dataTag: str, message: str,
                                                 log: str) -> bool:
    success = True
    a = getElementFromDataset(ds, sequenceTag)
    if a is not None:
        if type(a.value) == Sequence:
            for item in a.value:
                partial_success = subcheckLUTDataValuesMatchSpecifiedRange(
                    item, descriptorTag, dataTag, message, log)
                success = success and partial_success
    return success


def checkLUTDataValuesInIconImageSequenceMatchSpecifiedRange(
        ds: Dataset, log: list) -> bool:
    success = False
    aIconImageSequence = getElementFromDataset(ds, "IconImageSequence")
    if aIconImageSequence is not None:
        if type(aIconImageSequence.value) == Sequence:
            for item in aIconImageSequence.value:
                success = success and subcheckLUTDataValuesMatchSpecifiedRange(
                    item, "RedPaletteColorLookupTableDescriptor",
                    "RedPaletteColorLookupTableData",
                    "Icon Image Sequence - Red Palette Color LUT", log)
                success = success and subcheckLUTDataValuesMatchSpecifiedRange(
                    item, "GreenPaletteColorLookupTableDescriptor",
                    "GreenPaletteColorLookupTableData",
                    "Icon Image Sequence - Green Palette Color LUT", log)
                success = success and subcheckLUTDataValuesMatchSpecifiedRange(
                    item, "BluePaletteColorLookupTableDescriptor",
                    "BluePaletteColorLookupTableData",
                    "Icon Image Sequence - Blue Palette Color LUT", log)
    return success


def checkLUTDataValuesMatchSpecifiedRange(
        ds: Dataset, log: list) -> bool:
    success = True
    success = success and subcheckLUTDataValuesMatchSpecifiedRange_seq(
        ds, "ModalityLUTSequence", "LUTDescriptor", "LUTData",
        "Modality LUT", log)
    success = success and subcheckLUTDataValuesMatchSpecifiedRange_seq(
        ds, "VOILUTSequence", "LUTDescriptor", "LUTData", "VOI LUT", log)
    success = success and subcheckLUTDataValuesMatchSpecifiedRange_seq(
        ds, "PresentationLUTSequence", "LUTDescriptor", "LUTData",
        "Presentation LUT", log)
    aSoftcopyVOILUTSequence = getElementFromDataset(ds,
                                                    "SoftcopyVOILUTSequence")
    if aSoftcopyVOILUTSequence is not None:
        if type(aSoftcopyVOILUTSequence).value == Sequence:
            for item in aSoftcopyVOILUTSequence:
                success = success and subcheckLUTDataValuesMatchSpecifiedRange_seq(
                    item, "VOILUTSequence", "LUTDescriptor", "LUTData",
                    "Softcopy VOI LUT", log)
    success = success and subcheckLUTDataValuesMatchSpecifiedRange(
        ds, "RedPaletteColorLookupTableDescriptor",
        "RedPaletteColorLookupTableData",
        "Red Palette Color LUT", log)
    success = success and subcheckLUTDataValuesMatchSpecifiedRange(
        ds, "GreenPaletteColorLookupTableDescriptor",
        "GreenPaletteColorLookupTableData",
        "Green Palette Color LUT", log)
    success = success and subcheckLUTDataValuesMatchSpecifiedRange(
        ds, "BluePaletteColorLookupTableDescriptor",
        "BluePaletteColorLookupTableData",
        "Blue Palette Color LUT", log)
    success = success and checkLUTDataValuesInIconImageSequenceMatchSpecifiedRange(
        ds, log)
    aDirectoryRecordSequence = getElementFromDataset(ds,
                                                     "DirectoryRecordSequence")
    if aDirectoryRecordSequence is not None:
        if type(aDirectoryRecordSequence.value) == Sequence:
            for item in aDirectoryRecordSequence.value:
                success = success and checkLUTDataValuesInIconImageSequenceMatchSpecifiedRange(
                    item, log)
    return success


def checkCodeValuesDoNotContainInappropriateCharacters(ds: Dataset,
                                                       log: list) -> bool:
    success = True
    for(key, a) in ds.items():
        if type(a.value) == Sequence:
            for item in a:
                aCodeValue = getElementFromDataset(item, "CodeValue")
                aCodingSchemeDesignator = getElementFromDataset(
                    item, "CodingSchemeDesignator")
                if aCodeValue is not None and aCodingSchemeDesignator is not None:
                    if aCodingSchemeDesignator.VM > 1:
                        vCodingSchemeDesignator = \
                            aCodingSchemeDesignator.value[0]
                    else:
                        vCodingSchemeDesignator = aCodingSchemeDesignator.value
                    isSNOMED = (vCodingSchemeDesignator == "SRT" or
                                vCodingSchemeDesignator == "SNM3" or
                                vCodingSchemeDesignator == "99SDM")
                    isDICOM = vCodingSchemeDesignator == "DCM"
                    if isSNOMED or isDICOM:
                        if type(aCodeValue.value) != MultiValue:
                            vCodeValue = [aCodeValue.value]
                        else:
                            vCodeValue = aCodeValue.value
                        for v in vCodeValue:
                            bad = False
                            snomed_regex = "[A-Z][A-Z0-9]{0,2}-[0-9A-Z]{4,5}"
                            dcm_regex = "[A-Z0-9]*"
                            if isSNOMED and re.match(snomed_regex, v) is None:
                                bad = True
                            if isDICOM and re.match(dcm_regex, v) is None:
                                bad = True
                            if bad:
                                msg = "{} - value is <{}> - coding scheme is <{}>"
                                msg = msg.format(
                                    WMsgDC("CodeValueContainsInvalid"
                                           "CharactersForCodingScheme"),
                                    v, vCodingSchemeDesignator
                               )
                                log.append(msg)
        success = success and loopOverListsInSequencesWithLog(
            a, log, checkCodeValuesDoNotContainInappropriateCharacters)
    return success


def checkLongCodeValuesAreLongEnough(ds: Dataset, log: list) -> bool:
    success = True
    for(key, a) in ds.items():
        if type(a.value) == Sequence:
            for item in a:
                aLongCodeValue = getElementFromDataset(item, "LongCodeValue")
                if aLongCodeValue is not None:
                    if type(aLongCodeValue.value) != MultiValue:
                        vLongCodeValue = [aLongCodeValue.value]
                    else:
                        vLongCodeValue = aLongCodeValue.value
                    for v in vLongCodeValue:
                        if len(v) < 16:
                            msg = "{} - value is <{}> - length is {}"
                            msg = msg.format(EMsgDC("LongCodeValueTooShort"),
                                             v, len(v))
                            log.append(msg)
                            success = False
        success = success and loopOverListsInSequencesWithLog(
            a, log, checkLongCodeValuesAreLongEnough)
    return success


def checkCodeMeaningsForMeasurementUnitsDoNotContainInappropriateQuotes(
        ds: Dataset, log: list) -> bool:
    success = True
    for(key, a) in ds.items():
        if type(a.value) == Sequence:
            for item in a:
                aMeasurementUnitsCodeSequence = getElementFromDataset(
                    item, "MeasurementUnitsCodeSequence")
                if aMeasurementUnitsCodeSequence is not None:
                    aCodeMeaning = getElementFromDataset(item, "CodeMeaning")
                    if aCodeMeaning is not None:
                        if type(aCodeMeaning.value) != MultiValue:
                            vCodeMeaning = [aCodeMeaning.value]
                        else:
                            vCodeMeaning = aCodeMeaning.value
                        for v in vCodeMeaning:
                            if v[0] == '\'' or v[-1] == '\'' or v[0] == '\"' or \
                                    v[-1] == '\"':
                                msg = "{} - meaning is <{}>"
                                msg = msg.format(
                                    WMsgDC("CodeMeaningForMeasurementUnits"
                                           "BeginsOrEndsWith"
                                           "QuotationCharacters"), v)
                                log.append(msg)
        success = success and loopOverListsInSequencesWithLog(
            a, log,
            checkCodeMeaningsForMeasurementUnitsDoNotContainInappropriateQuotes)
    return success


def checkCodingSchemeDesignatorForMeasurementUnits(ds: Dataset,
                                                   log: list) -> bool:
    success = True
    for(key, a) in ds.items():
        if type(a.value) == Sequence:
            seq_kw = a.keyword
            isInsideUnitsCodeSequence = \
                seq_kw == "MeasurementUnitsCodeSequence" or \
                seq_kw == "ChannelSensitivityUnitsSequence" or \
                seq_kw == "MydriaticAgentConcentrationUnitsSequence" or \
                seq_kw == "MeasuringUnitsSequence"
            for item in a:
                aCodingSchemeDesignator = getElementFromDataset(
                    item, "CodingSchemeDesignator")
                if aCodingSchemeDesignator is not None:
                    if type(aCodingSchemeDesignator.value) == MultiValue:
                        vCodingSchemeDesignator = aCodingSchemeDesignator.value
                    else:
                        vCodingSchemeDesignator = [
                            aCodingSchemeDesignator.value]
                    for v in vCodingSchemeDesignator:
                        if v == "UCUM" and not isInsideUnitsCodeSequence and \
                                seq_kw != "CodingSchemeIdentificationSequence":
                            msg = '{} - {} = ({}, {})'
                            msg = msg.format(
                                WMsgDC(
                                    "UCUMCodingSchemeDesignatorIsUsedInSequenceOtherThanUnitsCodeSequence"),
                                seq_kw, a.tag.group, a.tag.element)
                            log.append(msg)
                        elif v != "UCUM" and isInsideUnitsCodeSequence:
                            msg = '{} - is {} instead - {} = ({}, {})'
                            msg = msg.format(
                                WMsgDC(
                                    "CodingSchemeDesignatorInUnitsCodeSequenceIsNotUCUM"),
                                v, seq_kw, a.tag.group, a.tag.element)
                            log.append(msg)
        success = success and loopOverListsInSequencesWithLog(
            a, log,
            checkCodingSchemeDesignatorForMeasurementUnits)
    return success


def checkPerFrameFunctionalGroupsSequencesAreNotAlreadyPresentInSharedFunctionalGroup(
        ds: Dataset, log: list) -> bool:
    # [\t\s]*\/\/.*
    success = True
    aSharedFunctionalGroupsSequence = getElementFromDataset(
        ds, "SharedFunctionalGroupsSequence")
    aPerFrameFunctionalGroupsSequence = getElementFromDataset(
        ds, "PerFrameFunctionalGroupsSequence")
    if aSharedFunctionalGroupsSequence is not None and \
            aPerFrameFunctionalGroupsSequence is not None:
        vSharedFunctionalGroupsSequence = aSharedFunctionalGroupsSequence.value
        vPerFrameFunctionalGroupsSequence = aPerFrameFunctionalGroupsSequence.value
        nPerFrameFunctionalGroupsSequence = len(
            vPerFrameFunctionalGroupsSequence)
        if len(vSharedFunctionalGroupsSequence) == 1:
            for(item, i) in \
                    zip(vPerFrameFunctionalGroupsSequence,
                        range(0, nPerFrameFunctionalGroupsSequence)):
                for(key, attrib) in item.items():
                    if type(attrib.value) is Sequence:
                        kw = attrib.keyword
                        if kw in vSharedFunctionalGroupsSequence:
                            msg = "{} - ({}, {}) {} in Per-frame " \
                                  "Functional Groups Sequence Item #{}"
                            msg = msg.format(
                                EMsgDC("FunctionalGroupSequenceAlready"
                                       "UsedInSharedFunctionalGroupsSequence"),
                                attrib.tag.group, attrib.tag.element, i + 1)
                            log.append(msg)
                            success = False
    return success


def checkCountOfDimensionIndexValuesMatchesDimensionIndexSequence(
        ds: Dataset, log: list) -> bool:
    success = True
    nDimensionIndexSequenceSequenceItems = int(0)
    aDimensionIndexSequence = getElementFromDataset(ds,
                                                    "DimensionIndexSequence")
    if aDimensionIndexSequence is not None:
        if type(aDimensionIndexSequence.value) == Sequence:
            nDimensionIndexSequenceSequenceItems = \
                len(aDimensionIndexSequence.value)
    aPerFrameFunctionalGroupsSequence = getElementFromDataset(
        ds, "PerFrameFunctionalGroupsSequence")
    if aPerFrameFunctionalGroupsSequence is not None:
        f = 0
        for frame in aPerFrameFunctionalGroupsSequence.value:
            aFrameContentSequence = \
                getElementFromDataset(frame, "FrameContentSequence")
            if aFrameContentSequence is not None:
                vFrameContentSequence = aFrameContentSequence.value[0]
                aDimensionIndexValues = getElementFromDataset(
                    vFrameContentSequence, "DimensionIndexValues")
                if aDimensionIndexSequence is not None:
                    nDimensionIndexValues = len(aDimensionIndexValues)
                    if nDimensionIndexSequenceSequenceItems != \
                            nDimensionIndexValues:
                        msg = "{} for frame {} got {} - expected {}"
                        msg = msg.format(
                            EMsgDC(
                                "NumberOfDimensionIndexValuesDoesNotMatchNumberOfDimensions"),
                            f + 1, nDimensionIndexValues,
                            nDimensionIndexSequenceSequenceItems)
                        log.append(msg)
                        success = False
            f += 1
    return success


def checkDimensionIndexValuesMatchInStackPositionNumberAndTemporalPositionIndex(
        ds: Dataset, log: list) -> bool:
    success = True
    indexValueThatIsInStackPositionNumber = int(-1)
    indexValueThatIsTemporalPositionIndex = int(-1)
    nDimensionIndexSequenceSequenceItems = int(0)
    aDimensionIndexSequence = getElementFromDataset(
        ds, "DimensionIndexSequence")
    if aDimensionIndexSequence is not None:
        i = 0
        for item in aDimensionIndexSequence.value:
            aDimensionIndexPointer = getElementFromDataset(
                item, "DimensionIndexPointer")
            if aDimensionIndexSequence is not None:
                vDimensionIndexPointer = aDimensionIndexPointer.value
                if vDimensionIndexPointer == \
                        Dictionary.tag_for_keyword("InStackPositionNumber"):
                    indexValueThatIsInStackPositionNumber = i
                elif vDimensionIndexPointer == \
                        Dictionary.tag_for_keyword("TemporalPositionIndex"):
                    indexValueThatIsTemporalPositionIndex = i
            i = + 1
    aPerFrameFunctionalGroupsSequence = getElementFromDataset(
        ds, "PerFrameFunctionalGroupsSequence")
    if aPerFrameFunctionalGroupsSequence is not None:
        f = 0
        for frame in aPerFrameFunctionalGroupsSequence.value:
            aFrameContentSequence = getElementFromDataset(
                frame, "FrameContentSequence")
            if aFrameContentSequence is not None:
                vFrameContentSequence = aFrameContentSequence.value[0]
                aDimensionIndexValues = getElementFromDataset(
                    vFrameContentSequence, "DimensionIndexValues")
                if aDimensionIndexValues is None:
                    nDimensionIndexValues = 0
                else:
                    nDimensionIndexValues = len(aDimensionIndexValues.value)
                aInStackPositionNumber = getElementFromDataset(
                    vFrameContentSequence, "InStackPositionNumber")
                if indexValueThatIsInStackPositionNumber != -1:
                    if aInStackPositionNumber is None or \
                            aInStackPositionNumber.VM == 0:
                        log.append(
                            "{} for frame {} ".fromat(
                                EMsgDC(
                                    "MissingInStackPositionNumberUsedAsDimensionIndex"),
                                f + 1
                           ))
                        success = False
                    else:
                        vInStackPositionNumber = aInStackPositionNumber.value
                        if indexValueThatIsInStackPositionNumber < nDimensionIndexValues:
                            vDimensionIndexValue = aDimensionIndexValues.value[
                                indexValueThatIsInStackPositionNumber]
                            if vDimensionIndexValue != vInStackPositionNumber:
                                msg = "{} for frame {} - got DimensionIndexValue {} - " \
                                      "expected same value as " \
                                      "InStackPositionNumber  {}"
                                msg = msg.format(
                                    EMsgDC("DimensionIndexValueForInStack"
                                           "PositionNumberDoesNotEqualValue"
                                           "OfInStackPositionNumber"), f + 1,
                                    vDimensionIndexPointer,
                                    vInStackPositionNumber)
                                log.append(msg)
                                success = False
                            else:
                                log.append("{} for frame {} ".format(
                                    EMsgDC("MissingDimensionIndexValue"
                                           "ForInStackPositionNumber"), f + 1
                               ))
                aTemporalPositionIndex = getElementFromDataset(
                    vFrameContentSequence, "TemporalPositionIndex")
                if indexValueThatIsTemporalPositionIndex != -1:
                    if aTemporalPositionIndex is None or \
                            aTemporalPositionIndex.VM == 0:
                        log.append("{} for frame {}".format(
                            EMsgDC(
                                "MissingTemporalPositionIndexUsedAsDimensionIndex"),
                            f + 1
                       ))
                        success = False
                    else:
                        vTemporalPositionIndex = aTemporalPositionIndex.value[0]
                        if indexValueThatIsTemporalPositionIndex < \
                                nDimensionIndexValues:
                            vDimensionIndexValue = aDimensionIndexValues.value[
                                indexValueThatIsTemporalPositionIndex]
                            if vDimensionIndexValue != vTemporalPositionIndex:
                                msg = " for frame {} - got DimensionIndexValue {} - expected same value as TemporalPositionIndex {}"
                                msg = msg.format(
                                    EMsgDC(
                                        "DimensionIndexValueForTemporalPositionIndexDoesNotEqualValueOfTemporalPositionIndex"),
                                    f + 1, vDimensionIndexValue,
                                    vTemporalPositionIndex)
                                log.append(msg)
                                success = False
                        else:
                            log.append("{} for frame {}".format(
                                EMsgDC("MissingDimensionIndexValueFor"
                                       "TemporalPositionIndex"), f + 1))
            f += 1
    return success


def checkCountPerFrameFunctionalGroupsMatchesNumberOfFrames(
        ds: Dataset, log: list) -> bool:
    success = True
    aPerFrameFunctionalGroupsSequence = getElementFromDataset(
        ds, "PerFrameFunctionalGroupsSequence")
    if aPerFrameFunctionalGroupsSequence is not None:
        nPerFrameFunctionalGroupsSequence = \
            len(aPerFrameFunctionalGroupsSequence.value)
        if nPerFrameFunctionalGroupsSequence > 0:
            aNumberOfFrames = getElementFromDataset(ds, "NumberOfFrames")
            if aNumberOfFrames is None:
                vNumberOfFrames = 1
            else:
                vNumberOfFrames = aNumberOfFrames.value
            if nPerFrameFunctionalGroupsSequence != vNumberOfFrames:
                msg = "{} - have {} items - but {} frames".format(
                    EMsgDC(
                        "NumberOfPerFrameFunctionalGroupsSequenceItemsDoesNotMatchNumberOfFrames"),
                    nPerFrameFunctionalGroupsSequence, vNumberOfFrames
               )
                log.append(msg)
                success = False
    return success


def checkSegmentNumbersMonotonicallyIncreasingFromOneByOne(ds: Dataset,
                                                           log: list) -> bool:
    success = True
    aSegmentSequence = getElementFromDataset(ds, "SegmentSequence")
    if aSegmentSequence is not None:
        s = 0
        for item in aSegmentSequence.value:
            aSegmentNumber = getElementFromDataset(item, "SegmentNumber")
            if aSegmentSequence is not None:
                vSegmentNumber = aSegmentNumber.value
                if vSegmentNumber != s + 1:
                    msg = "{} - have SegmentSequence item number {} " \
                          "(from one) with SegmentNumber of {}"
                    msg = msg.format(
                        EMsgDC(
                            "SegmentNumberNotMonotonicallyIncreasingFromOneByOne"),
                        s + 1, vSegmentNumber)
                    log.append(msg)
                    success = False
                    break
            s += 1
    return success


def checkReferencedSegmentNumbersHaveTarget(ds: Dataset, log: list) -> bool:
    success = True
    aSegmentSequence = getElementFromDataset(ds, "SegmentSequence")
    segmentNumberTargets = []
    if aSegmentSequence is not None:
        for item in aSegmentSequence.value:
            aSegmentNumber = getElementFromDataset(item, "SegmentNumber")
            if aSegmentSequence is not None:
                segmentNumberTargets.append(aSegmentNumber.value)
        aPerFrameFunctionalGroupsSequence = getElementFromDataset(
            ds, "PerFrameFunctionalGroupsSequence")
        if aPerFrameFunctionalGroupsSequence is not None:
            f = 0
            for frame in aPerFrameFunctionalGroupsSequence:
                aSegmentIdentificationSequence = getElementFromDataset(
                    ds, "SegmentIdentificationSequence")
                if aSegmentIdentificationSequence is not None:
                    if len(aSegmentIdentificationSequence.value) > 0:
                        segmentIdentificationSequenceDataset = \
                            aSegmentIdentificationSequence.value[0]
                        aReferencedSegmentNumber = getElementFromDataset(
                            segmentIdentificationSequenceDataset,
                            "ReferencedSegmentNumber")
                        if aReferencedSegmentNumber is not None:
                            vReferencedSegmentNumber = aReferencedSegmentNumber.value
                            if vReferencedSegmentNumber not in segmentNumberTargets:
                                msg = "{} - have ReferencedSegmentNumber  {} in SegmentIdentificationSequence for frame {}"
                                msg = msg.format(
                                    EMsgDC(
                                        "ReferencedSegmentNumberNotPresentInSegmentSequence"),
                                    vReferencedSegmentNumber, f + 1)
                                log.append(msg)
                                success = False
                f += 1
    return success


def checkCoordinateContentItemsHaveAppropriateChildren(ds: Dataset,
                                                       log: list) -> bool:
    success = True
    aValueType = getElementFromDataset(ds, "ValueType")
    if aValueType is not None:
        vValueType = aValueType.value
        if vValueType == "SCOORD" or vValueType == "TCOORD":
            foundAppropriateChildOrIsByReferenceRelationship = False
            aContentSequence = getElementFromDataset(ds, "ContentSequence")
            if aContentSequence is not None:
                for item in aContentSequence.value:
                    aChildValueType = getElementFromDataset(item, 'ValueType')
                    if aChildValueType is not None:
                        vChildValueType = aChildValueType.value
                        if(
                                vValueType == "SCOORD" and vChildValueType == "IMAGE") or \
                               (
                                        vValueType == "TCOORD" and vChildValueType == "SCOORD" or \
                                        vChildValueType == "IMAGE" or vChildValueType == "WAVEFORM"):
                            foundAppropriateChildOrIsByReferenceRelationship = True
                    else:
                        aReferencedContentItemIdentifier = getElementFromDataset(
                            item, 'ReferencedContentItemIdentifier')
                        if aReferencedContentItemIdentifier is not None:
                            if aReferencedContentItemIdentifier.VM > 0:
                                foundAppropriateChildOrIsByReferenceRelationship = True
                    foundAppropriateRelationship = False
                    aRelationshipType = getElementFromDataset(item,
                                                              "RelationshipType")
                    if aRelationshipType is not None:
                        vRelationshipType = aRelationshipType.value
                        if vRelationshipType == "SELECTED FROM":
                            foundAppropriateRelationship = True
                    if foundAppropriateRelationship:
                        msg = "{} for {} got {} expected {}"
                        msg = msg.format(
                            EMsgDC(
                                "CoordinatesContentItemMissingOrIncorrectRequiredChildContentItem"),
                            vChildValueType if vChildValueType else "no child",
                            vValueType,
                            "IMAGE" if vValueType == "SCOORD" else "SCOORD, IMAGE or WAVEFORM")
                        log.append(msg)
                        success = False
    for(key, a) in ds.items():
        success = success and loopOverListsInSequencesWithLog(
            a, log, checkCoordinateContentItemsHaveAppropriateChildren)
    return success


def findInstanceInHierarchicalEvidenceSequence(
        aEvidenceSequence: DataElement, vSOPInstanceUID: UID) -> Dataset:
    if aEvidenceSequence is not None:
        if type(aEvidenceSequence.value) == Sequence:
            for study in aEvidenceSequence.value:
                aReferencedSeriesSequence = getElementFromDataset(
                    study, "ReferencedSeriesSequence")
                if aReferencedSeriesSequence is not None:
                    for series in aReferencedSeriesSequence.value:
                        aReferencedSOPSequence = getElementFromDataset(
                            series, "ReferencedSOPSequence")
                        if aReferencedSOPSequence is not None:
                            for sop in aReferencedSeriesSequence.value:
                                aReferencedSOPInstanceUID = getElementFromDataset(
                                    sop, "ReferencedSOPInstanceUID")
                                if aReferencedSOPInstanceUID is not None:
                                    if vSOPInstanceUID == aReferencedSOPInstanceUID.value:
                                        return sop
    return None


def findInstanceInHierarchicalEvidenceSequences(
        ds: Dataset, vSOPInstanceUID: UID, vSOPClassUID: UID, vValueType: str,
        subType: str, log: list) -> bool:
    success = False
    aCurrentRequestedProcedureEvidenceSequence = getElementFromDataset(ds,
                                                                       "CurrentRequestedProcedureEvidenceSequence")
    aPertinentOtherEvidenceSequence = getElementFromDataset(ds,
                                                            "PertinentOtherEvidenceSequence")
    if aCurrentRequestedProcedureEvidenceSequence is not None:
        foundList = findInstanceInHierarchicalEvidenceSequence(
            aCurrentRequestedProcedureEvidenceSequence, vSOPInstanceUID)
    if foundList is not None and aPertinentOtherEvidenceSequence is not None:
        foundList = findInstanceInHierarchicalEvidenceSequence(
            aPertinentOtherEvidenceSequence, vSOPInstanceUID)
    if foundList is not None:
        success = True
        aReferencedSOPClassUID = getElementFromDataset(ds,
                                                       "ReferencedSOPClassUID")
        if aReferencedSOPClassUID is not None:
            vReferencedSOPClassUID = aReferencedSOPClassUID.value
            if vSOPClassUID != vReferencedSOPClassUID:
                msg = "{} for  {}{}  ReferencedSOPInstanceUID  {} {} ReferencedSOPClassUID is {} but evidence ReferencedSOPClassUID is {}"
                msg.format(EMsgDC(
                    "SOPClassInCurrentRequestedProcedureOrPertinentOtherEvidenceSequenceDoesNotMatchReference"),
                           vValueType,
                           " " + subType if subType != "" else subType,
                           vSOPInstanceUID if vSOPInstanceUID != "" else "missing or empty SOPInstanceUID",
                           vValueType, vSOPClassUID, vReferencedSOPClassUID)
                log.append(msg)
                success = False
    else:
        msg = " but have {}{} {} ReferencedSOPInstanceUID {}"
        msg.format(
            EMsgDC(
                "NotListedInCurrentRequestedProcedureOrPertinentOtherEvidenceSequence"),
            vValueType, " " + subType if subType != "" else subType,
            vSOPInstanceUID if vSOPInstanceUID != "" else "missing or empty SOPInstanceUID"
       )
        log.append(msg)
    return success


def precheckInstanceReferencesAreIncludedInHierarchicalEvidenceSequences(
        root_ds: Dataset, ds: Dataset, log: list) -> bool:
    success = True
    aValueType = getElementFromDataset(ds, "ValueType")
    # a = getElementFromDataset(ds, "")

    if aValueType is not None:
        vValueType = aValueType.value
        if vValueType == "IMAGE" or vValueType == "COMPOSITE" or vValueType == "WAVEFORM":
            vReferencedSOPInstanceUID = ""
            vReferencedSOPClassUID = ""
            vPresentationStateReferencedSOPInstanceUID = ""
            vPresentationStateReferencedSOPClassUID = ""
            vRealWorldValueReferencedSOPInstanceUID = ""
            vRealWorldValueReferencedSOPClassUID = ""
            aReferencedSOPSequence = getElementFromDataset(ds,
                                                           "ReferencedSOPSequence")
            if aReferencedSOPSequence is not None:
                for item in aReferencedSOPSequence.value:
                    aReferencedSOPInstanceUID = getElementFromDataset(ds,
                                                                      "ReferencedSOPInstanceUID")
                    if aReferencedSOPInstanceUID is not None:
                        vReferencedSOPInstanceUID = aReferencedSOPInstanceUID.value
                    aReferencedSOPClassUID = getElementFromDataset(ds,
                                                                   "ReferencedSOPClassUID")
                    if aReferencedSOPClassUID is not None:
                        vReferencedSOPClassUID = aReferencedSOPClassUID.value
                        aPresentationStateReferencedSOPSequence = getElementFromDataset(
                            item, "ReferencedSOPSequence")
                        if aPresentationStateReferencedSOPSequence is not None:
                            for sop in aPresentationStateReferencedSOPSequence.value:
                                aPresentationStateReferencedSOPInstanceUID = getElementFromDataset(
                                    sop, "ReferencedSOPInstanceUID")
                                if aPresentationStateReferencedSOPInstanceUID is not None:
                                    vPresentationStateReferencedSOPInstanceUID = aPresentationStateReferencedSOPInstanceUID.value
                                aPresentationStateReferencedSOPClassUID = getElementFromDataset(
                                    sop, "ReferencedSOPClassUID")
                                if aPresentationStateReferencedSOPClassUID is not None:
                                    vPresentationStateReferencedSOPClassUID = aPresentationStateReferencedSOPClassUID.value
                        aReferencedRealWorldValueMappingInstanceSequence = \
                            getElementFromDataset(item,
                                                  "ReferencedRealWorldValueMappingInstanceSequence")
                        if aReferencedSOPSequence is not None:
                            for rwvm_item in aReferencedRealWorldValueMappingInstanceSequence.value:
                                aRealWorldValueReferencedSOPInstanceUID = getElementFromDataset(
                                    rwvm_item, "ReferencedSOPInstanceUID")
                                if aRealWorldValueReferencedSOPInstanceUID is not None:
                                    vRealWorldValueReferencedSOPInstanceUID = aRealWorldValueReferencedSOPInstanceUID.value
                                aRealWorldValueReferencedSOPClassUID = getElementFromDataset(
                                    rwvm_item, "ReferencedSOPClassUID")
                                if aRealWorldValueReferencedSOPClassUID is not None:
                                    vRealWorldValueReferencedSOPClassUID = aRealWorldValueReferencedSOPClassUID.value
            success = success and findInstanceInHierarchicalEvidenceSequences(
                root_ds, vReferencedSOPInstanceUID, vReferencedSOPClassUID,
                vValueType, "", log)
            if vPresentationStateReferencedSOPInstanceUID != "" and \
                    not findInstanceInHierarchicalEvidenceSequences(
                        root_ds, vPresentationStateReferencedSOPInstanceUID,
                        vPresentationStateReferencedSOPClassUID, vValueType,
                        "PresentationState", log):
                success = False
            if vRealWorldValueReferencedSOPInstanceUID != "" and \
                    not findInstanceInHierarchicalEvidenceSequences(
                        root_ds, vRealWorldValueReferencedSOPInstanceUID,
                        vRealWorldValueReferencedSOPClassUID, vValueType,
                        "RealWorldValueMapping", log):
                success = False
    for(key, a) in ds.items():
        loopOverListsInSequencesWithRootListAndLog(
            root_ds, a, log,
            precheckInstanceReferencesAreIncludedInHierarchicalEvidenceSequences)


def validatePrivate(ds: Dataset, log: list) -> bool:
    success = True
    for(key, a) in ds.items():
        success = success and loopOverListsInSequencesWithLog(a, log,
                                                              validatePrivate)
        g = a.tag.group
        e = a.tag.element
        if(g % 2) == 1 and not((g % 2) == 1 and g > 0x0007 and g != 0xffff):
            msg = "{} - ({},{})".format(
                EMsgDC("AttributeIsNotInALegalPrivateGroup"),
                g, e)
            log.append(msg)
            success = False
    return success


def validateRetired(ds: Dataset, log: list) -> bool:
    success = True
    for(key, a) in ds.items():
        success = success and loopOverListsInSequencesWithLog(a, log,
                                                              validateRetired)
        g = a.tag.group
        e = a.tag.element
        if Dictionary.dictionary_has_tag(a.tag):
            if Dictionary.dictionary_is_retired(a.tag):
                msg = "{} - {}".format(
                    EMsgDC("RetiredAttribute"), validate_vr.tag2str(a.tag))
                log.append(msg)
                success = False
    return success


def validateVR(ds: Dataset, log: list) -> bool:
    success = True
    attrib = getElementFromDataset(ds, "SpecificCharacterSet")
    if attrib is None:
        char_set = pydicom.charset.convert_encodings(["ISO_IR 6"])
    elif type(attrib.value) == MultiValue:
        char_set = pydicom.charset.convert_encodings(attrib.value)
    else:
        char_set = pydicom.charset.convert_encodings([attrib.value])
    for(key, a) in ds.items():
        success = success and loopOverListsInSequencesWithLog(a, log,
                                                              validateVR)
        try:
            if a.is_raw:
                a = DataElement_from_raw(a)
            # if a.VR == "UN":
            #     print(a)

            x = getattr(validate_vr, "validateVR_" + a.VR)
            x(a, log, char_set)
        except AttributeError as err:
            # print("Couldn't find validateVR_" + a.VR)
            # print(err)
            pass
        try:
            kw = a.keyword
        except AttributeError:
            kw = ""
        if Dictionary.dictionary_has_tag(a.tag):
            kw = Dictionary.keyword_for_tag(a.tag)
            success = success and module_cc.verifyVR(a, "", kw, False, log)
    return success


def isRepeatingGroup(t:Tag) -> bool:
    g = t.group
    return(g >= 0x5000 and g <= 0x501e) or\
        (g >= 0x6000 and g <= 0x601e)


def isLengthElementOrLengthToEnd(t:Tag) -> bool:
    e = t.element
    g = t.group
    return e == 0x0000 or(
        g == 0x0008 and e == 0x0001
   )


def getRepeatingBase(t:Tag):
    g = t.group
    e = t.element
    gMASKEDff00 = g&0xff00
    eMASKEDff00 = e&0xff00
    eMASKEDff0f = e&0xff0f
    # Transformations must match those in dictionary ... see elmdict.awk,elmdict.tpl,attrtag.cc

    # Note that some are from element 0xxx00 and others from 0xxx10

    if g == 0x0020:
        if eMASKEDff00 == 0x3100:
            e = 0x3100			# 0x31xx - PS 300 - Source Image IDs

    elif g == 0x0028:
        if eMASKEDff0f == 0x0400 and e != 0x0400:
            e = 0x0410	# 0x04x0 - PS 2 - RowsForNthOrderCoefficients
        elif eMASKEDff0f == 0x0401 and e != 0x0401:
             e = 0x0411	# 0x04x1 - PS 2 - ColumnsForNthOrderCoefficients
        elif eMASKEDff0f == 0x0402 and e != 0x0402:
             e = 0x0412	# 0x04x2 - PS 2 - CoefficientCoding
        elif eMASKEDff0f == 0x0403 and e != 0x0403:
             e = 0x0413	# 0x04x3 - PS 2 - CoefficientCodingPointers

        elif eMASKEDff0f == 0x0800:
             e = 0x0800			# 0x08x0 - PS 2 - CodeLabel
        elif eMASKEDff0f == 0x0802:
             e = 0x0802			# 0x08x2 - PS 2 - NumberOfTables
        elif eMASKEDff0f == 0x0803:
             e = 0x0803			# 0x08x3 - PS 2 - CodeTableLocation
        elif eMASKEDff0f == 0x0804:
             e = 0x0804			# 0x08x4 - PS 2 - BitsForCodeWord
        elif eMASKEDff0f == 0x0808:
             e = 0x0808			# 0x08x8 - PS 2 - ImageDataLocation

    elif g == 0x1000:
        if eMASKEDff0f == 0x0000 and e != 0x0000:
             e = 0x0010	# 0x00x0 - PS 2 - Escape Triplet
        elif eMASKEDff0f == 0x0001 and e != 0x0001:
             e = 0x0011	# 0x00x1 - PS 2 - Run Length Triplet
        elif eMASKEDff0f == 0x0002 and e != 0x0002:
             e = 0x0012	# 0x00x2 - PS 2 - Huffman Table Size
        elif eMASKEDff0f == 0x0003 and e != 0x0003:
             e = 0x0013	# 0x00x3 - PS 2 - Huffman Table Triplet
        elif eMASKEDff0f == 0x0004 and e != 0x0004:
             e = 0x0014	# 0x00x4 - PS 2 - Shift Table Size
        elif eMASKEDff0f == 0x0005 and e != 0x0005:
             e = 0x0015	# 0x00x5 - PS 2 - Shift Table Triplet

    elif g == 0x1010:
        if 0x0004 <= e <= 0xfffe:
             e = 0x0004			# PS 2 - Zonal Map

    elif gMASKEDff00 == 0x5000:
        g = 0x5001 if(g%2) == 0  else 0x5000		# 0x50xx - PS 3 - Curve stuff
    elif gMASKEDff00 == 0x6000:
        g = 0x6001 if(g%2) == 0  else 0x6000		# 0x60xx - PS 3 and earlier - Overlay stuff
    elif gMASKEDff00 == 0x7000:
        g = 0x7001 if(g%2) == 0  else 0x7000		# 0x70xx - Private DLX TextAnnotation etc.
    elif gMASKEDff00 == 0x7f00 and g != 0x7fe0:
        g = 0x7f00		# 0x7Fxx - PS 2 - VariablePixelData

    return Tag(g, e)


def AfterVerificationValidateUsed(ds: Dataset, log: list) -> bool:
    succeeded = True
    for key, a in ds.items():
        try:
            a = (ds[key])
            # a.__class__= rightdicom.dcmvfy.data_elementx.DataElementX
        except KeyError as err:
            if not key.is_private:
                if not Dictionary.dictionary_has_tag(key):
                    log.append("{} - {}".format(
                        EMsgDC("AttributeIsNotARecognizedStandardAttribute"),
                        validate_vr.tag2str(key)))
                    succeeded == False
                    continue
        if(not key.is_private and
        key != Dictionary.tag_for_keyword("ModifiedAttributesSequence") and
        key != Dictionary.tag_for_keyword("UnassignedSharedConvertedAttributesSequence") and
        key != Dictionary.tag_for_keyword("UnassignedPerFrameConvertedAttributesSequence")
       ):
            if not loopOverListsInSequencesWithLog(a, log, AfterVerificationValidateUsed):
                    succeeded = False
        used = a.used_in_verification
        if not used and isRepeatingGroup(key):
            tt = getRepeatingBase(key)
            if getRepeatingBase(tt) in ds:
                used = ds[tt].used_in_verification
        if not used and not key.is_private:
            log.append('{} - {}'.format(WMsgDC("AttributeIsNotUsedInIOD"),
            validate_vr.tag2str(key)))
            succeeded = False

