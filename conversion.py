import logging
import numpy
import os
import pydicom
import re
import common.common_tools as ctools
from highdicom.legacy.sop import(
    # CLASSES
    FrameSet,
    FrameSetCollection,
    LegacyConvertedEnhancedCTImage,
    LegacyConvertedEnhancedMRImage,
    LegacyConvertedEnhancedPETImage,
)
import highdicom.legacy.sop as sop
from pydicom.filereader import(
    # FUNCTIONS
    dcmread,
)
from pydicom.filewriter import(
    # FUNCTIONS
    dcmwrite,
)
from pydicom.uid import(
    # FUNCTIONS
    generate_uid,
    # VARIABLES
    ExplicitVRLittleEndian,
)
from rightdicom.dcmvfy.sopclc_h import(
    # VARIABLES
    CTImageStorageSOPClassUID,
    MRImageStorageSOPClassUID,
    PETImageStorageSOPClassUID,
)
floating_point_tolerance = 0.001
supported_sop_class_uids = [
    MRImageStorageSOPClassUID,
    CTImageStorageSOPClassUID,
    PETImageStorageSOPClassUID
    ]
import logging


def ConvertByPixelMed(pixel_med_jars: str, input_dcm_folder: str,
                      output_dcm_folder: str,
                      conversin_output_file: str,
                      conversion_error_file: str, log=[]):
    command = ['java', "-Xmx768m", "-Xms768m", "-cp", pixel_med_jars,
               "com.pixelmed.dicom.MultiFrameImageFactory",
               input_dcm_folder, output_dcm_folder]
    ctools.RunExe(command, conversion_error_file,
                  conversin_output_file, log=log)
    print('running pixelmed on {}'.format(input_dcm_folder))


class ParentChildDicoms:

    def __init__(self, parent_sop_instanc_uid: list,
                 child_study_instance_uid: str,
                 child_series_instance_uid: str,
                 child_sop_instance_uid: str,
                 child_dicom_file_path: str) -> None:
        if isinstance(parent_sop_instanc_uid, str):
            parent_sop_instanc_uid = [parent_sop_instanc_uid]
        self.parent_sop_instanc_uid = parent_sop_instanc_uid
        self.child_sop_instance_uid = child_sop_instance_uid
        self.child_study_instance_uid = child_study_instance_uid
        self.child_series_instance_uid = child_series_instance_uid
        self.child_dicom_file = child_dicom_file_path
    
    @staticmethod
    def GetQueryHeader() -> str:
        header = '''
            INSERT INTO `{0}`.ORIGINATED_FROM
                VALUES {1};
        '''
        return header

    def GetQuery(self, parent_table_name,
                 child_table_name) -> list:
        logger = logging.getLogger(__name__)
        whole_query = []
        q = """(
                {}, --PARENT_TABLE
                {}, --PARENT_SOP_INSATANCE_UID
                {}, --CHILD_TABLE
                {} --CHILD_SOP_INSATANCE_UID
                )
        """
        str_ = ''
        for i, parent_uid in enumerate(self.parent_sop_instanc_uid):
            whole_query.append(
                (
                    q.format(
                        self.GetValue(parent_table_name),
                        self.GetValue(str(parent_uid)),
                        self.GetValue(child_table_name),
                        self.GetValue(str(self.child_sop_instance_uid))
                    ),
                    (
                        parent_table_name,  # PARENT_TABLE
                        str(parent_uid),  # PARENT_SOP_INSATANCE_UID
                        child_table_name,  # CHILD_TABLE
                        str(self.child_sop_instance_uid),  # CHILD_SOP_INSATANCE_UID
                    )
                )
            )
        return whole_query

    def GetQuery_Old(self, parent_table_name,
                 child_table_name) -> str:
        whole_query = ''
        q = """
        CALL `{{0}}`.ADD_DICOM_ORIGIN(
            {},  --PARENT_TABLE
            {},  --PARENT_SOP_INSATANCE_UID
            {},  --CHILD_TABLE
            {}  --CHILD_SOP_INSATANCE_UID
            );
        """
        for parent_uid in self.parent_sop_instanc_uid:
            whole_query += q.format(
                self.GetValue(parent_table_name),
                self.GetValue(str(parent_uid)),
                self.GetValue(child_table_name),
                self.GetValue(str(self.child_sop_instance_uid))
            )
        return whole_query

    def GetValue(self, v):
            if v is None:
                return "NULL"
            elif type(v) == str:
                return '"{}"'.format(v)
            else:
                return v


class PositionBaseCategoryElement:
    StepSize = 0
    DicomDataset = []

    def AddNewCandidate(self, new_touple):
        success = False
        new_pos = new_touple[1]
        if abs(self.DicomDataset[0][1] - new_pos - self.StepSize) < \
            floating_point_tolerance and \
                new_pos < self.DicomDataset[0][1]:
            success = True
            self.DicomDataset.insert(0, new_touple)
        elif abs(new_pos - self.DicomDataset[-1][1] - self.StepSize) < \
            floating_point_tolerance and \
                new_pos > self.DicomDataset[-1][1]:
            success = True
            self.DicomDataset.append(new_touple)
        return success

    def __init__(self, step: float, ds_pos_elem1: tuple):
        self.StepSize = step
        self.DicomDataset = [ds_pos_elem1]

    def Print(self, Indent=0):
        Prefix = ""
        for i in range(0, Indent):
            Prefix += "\t"
        print(Prefix + " == == == == == == == == == == == == == == ==  ")
        print(Prefix + "step size = {}".format(self.StepSize))
        print(Prefix + " == == == == == == == == == == == == == == ==  ")
        for el in self.DicomDataset:
            print(Prefix + "---> position {}".format(el[1]))


def GetSopClassCategory(ds_list):
    sop_classes = {}
    for ds in ds_list:
        sop_class = ds.SOPClassUID
        if sop_class in sop_classes:
            sop_classes[sop_class].append(ds)
        else:
            sop_classes[sop_class] = [ds]
    return sop_classes


def GetStudyCategory(ds_list):
    studies = {}
    for ds in ds_list:
        if(ds.StudyInstanceUID in studies):
            studies[ds.StudyInstanceUID].append(ds)
        else:
            studies[ds.StudyInstanceUID] = [ds]
    return studies.items()


def GetSeriesCategory(ds_list):
    series = {}
    for ds in ds_list:
        if(ds.SeriesInstanceUID in series):
            series[ds.SeriesInstanceUID].append(ds)
        else:
            series[ds.SeriesInstanceUID] = [ds]
    return series.items()


def GetSpacingCategory(ds_list):
    series = []
    for ds in ds_list:
        spacing = [ds.PixelSpacing[0], ds.PixelSpacing[1], ds.SliceThickness]
        if len(series) == 0:
            series.append((spacing, [ds]))
        else:
            found_match = False
            for s in series:
                if ctools.GetVectorDistance(s[0], ds.PixelSpacing) < \
                        floating_point_tolerance:
                    found_match = True
                    s[1].append(ds)
                    break
            if not found_match:
                series.append((spacing, [ds]))
    return series


def GetOrientationCategory(ds_list):
    series = []
    for ds in ds_list:
        orientation = ds.ImageOrientationPatient
        if len(series) == 0:
            series.append((orientation, [ds]))
        else:
            found_match = False
            for s in series:
                if ctools.GetVectorDistance(
                    s[0], ds.ImageOrientationPatient) < \
                         floating_point_tolerance:
                    found_match = True
                    s[1].append(ds)
                    break
            if not found_match:
                series.append((orientation, [ds]))
    return series


def GetSlicePosition(ds):
    dirr = ds.ImageOrientationPatient
    poss = ds.ImagePositionPatient
    a = numpy.array(dirr[: 3])
    b = numpy.array(dirr[3:])
    c = numpy.cross(a, b)
    output = float(c.dot(numpy.array(poss)))
    return output


def ClassifySeriesByPosition(ds_list):
    sorted_ds = []
    ds_pairs = []
    for ds_element in ds_list:
        ds_pairs.append((ds_element, GetSlicePosition(ds_element)))
    if len(ds_list) == 1:
        return [PositionBaseCategoryElement(1, ds_pairs[0])]
    i = 0
    for sorted_key in sorted(ds_pairs, key=lambda x: x[1]):
        sorted_ds.append(sorted_key)
        i += 1
        # print('Slice# {} --pos--> {}'.format(i, sorted_key[1]))
    category = [
        PositionBaseCategoryElement(
            sorted_ds[1][1] - sorted_ds[0][1], sorted_ds[0])]
    for(ds, idx) in zip(sorted_ds[1:], range(1, len(sorted_ds))):
        if not category[-1].AddNewCandidate(ds):
            if idx == len(sorted_ds) - 1:
                category.append(PositionBaseCategoryElement(1, ds))
            else:
                category.append(
                    PositionBaseCategoryElement(
                        sorted_ds[idx + 1][1] - ds[1], ds))
    return category


def GetFrameSetsFromFiles(single_frame_folder_or_list):
    if isinstance(single_frame_folder_or_list, str):
        if os.path.exists(single_frame_folder_or_list):
            Files = ctools.Find(single_frame_folder_or_list, 1, ctools.is_dicom)
    elif isinstance(single_frame_folder_or_list, list):
        Files = single_frame_folder_or_list
    else:
        return []
    Output = []
    err_counter = 1
    all_ds = []
    n = 1
    for f in Files:
        try:
            ds = dcmread(f)
        except BaseException as err:
            msg_pattern = "Input Err # {} type {} -> {}"
            err_message = msg_pattern.format(err_counter, type(err), err)
            Output.append((False, err_message))
            continue
        all_ds.append(ds)
        # if ds.Modality in Mo
    return all_ds


def ConvertFrameset(frameset: FrameSet, OutputFileName: str,
                    multi_frame_study_instance_uid: str = None,
                    multi_frame_series_instance_uid: str = None,
                    multi_frame_sop_instance_uid: str=None):
    logger = logging.getLogger(__name__)
    ref_ds = frameset.frames[0]
    if multi_frame_sop_instance_uid is None:
        multi_frame_sop_instance_uid = generate_uid()
    if multi_frame_series_instance_uid is None:
        multi_frame_series_instance_uid = generate_uid()
    if multi_frame_study_instance_uid is None:
        multi_frame_study_instance_uid = generate_uid()
    try:
        sop_class = frameset.frames[0].SOPClassUID
        if sop_class == CTImageStorageSOPClassUID:
            m = 'CT'
        elif sop_class == MRImageStorageSOPClassUID:
            m = 'MR'
        elif sop_class == PETImageStorageSOPClassUID:
            m = 'PET'
        LegacyConverterClass = getattr(
                    sop,
                    "LegacyConvertedEnhanced{}Image".format(m)
                )
        x = LegacyConverterClass(
            frameset.frames,
            series_instance_uid = multi_frame_series_instance_uid,
            series_number = ref_ds.SeriesNumber,
            sop_instance_uid = multi_frame_sop_instance_uid,
            instance_number = 1,
            )
        dcmwrite(
            filename = OutputFileName, dataset = x, write_like_original=False)
        pr_ch = ParentChildDicoms(
            frameset.get_sop_instance_uid_list(),
            frameset.StudyInstanceUID,
            multi_frame_series_instance_uid,
            multi_frame_sop_instance_uid,
            OutputFileName)
    except BaseException as err:
        logger.error(err, exc_info=True)
        pr_ch = None
    return pr_ch


def ConvertByHighDicomNew(single_frame_folder_or_list,
                          OutputPrefix, log=[]) -> list:
    all_datasets = GetFrameSetsFromFiles(single_frame_folder_or_list)
    framesets = FrameSetCollection(all_datasets).frame_sets
    multi_frame_study_instance_uid = all_datasets[0].StudyInstanceUID
    parent_child_uids = []
    multi_frame_series_instance_uid = generate_uid()
    mf_dir = os.path.join(OutputPrefix, '{}'.format(
        multi_frame_series_instance_uid))
    for n, frameset in enumerate(framesets, 1):
        ref_ds = frameset.frames[0]
        sop_class_uid = frameset.get_sop_class_uid()
        if sop_class_uid not in supported_sop_class_uids:
            continue
        # try:
        multi_frame_sop_instance_uid = generate_uid()
        mf_prefix = os.path.join(mf_dir, '{}.dcm'.format(
            multi_frame_sop_instance_uid))
        if not os.path.exists(mf_dir):
            os.makedirs(mf_dir)
        pr_ch = ConvertFrameset(
            frameset, mf_prefix, multi_frame_study_instance_uid,
            multi_frame_series_instance_uid)
        parent_child_uids.append(pr_ch)
    return parent_child_uids


def ConvertByHighDicom(SingleFrameDir, OutputPrefix, log=[]):
    Files = ctools.Find(SingleFrameDir, 1, ctools.is_dicom)
    Output = []
    err_counter = 1
    all_ds = []
    for f in Files:
        try:
            ds = dcmread(f)
        except BaseException as err:
            err_message = "Input Err # {} type {} -> {}".format(
                err_counter, type(err), err)
            Output.append((False, err_message))
            continue
        all_ds.append(ds)
        # if ds.Modality in ModalityCategory:
        #     ModalityCategory[ds.Modality].append(ds)
        # else:
        #     ModalityCategory[ds.Modality] = [ds]
    n = 0
    supported_sop_classes = {
        sop_class_uids.MRImageStorageSOPClassUID: "MR",
        sop_class_uids.CTImageStorageSOPClassUID: "CT",
        sop_class_uids.PETImageStorageSOPClassUID: "PET"}
    SOPClassCategory = GetSopClassCategory(all_ds)
    for SOPClassUID, SOPClassDatasets in SOPClassCategory.items():
        if SOPClassUID not in supported_sop_classes:
            err_message = " MODALITY ERROR: Modality name {} is not "\
                "supported".format(supported_sop_classes[SOPClassUID])
            Output.append((False, err_message))
            continue
        Modality_Studies = GetStudyCategory(SOPClassDatasets)
        for stdy_UID, stdy_ds in Modality_Studies:
            Modality_Series = GetSeriesCategory(stdy_ds)
            for sris_UID, sris_ds in Modality_Series:
                spacing_categories = GetSpacingCategory(sris_ds)
                for spacing_element in spacing_categories:
                    orientation_categories = \
                        GetOrientationCategory(spacing_element[1])
                    for orientation_element in orientation_categories:
                        equally_positioned_classes = \
                            ClassifySeriesByPosition(orientation_element[1])
                        for uniform_class in equally_positioned_classes:
                            final_ds = []
                            # success = True
                            err_message = "Input folder {} \n \t\tNumber"\
                                " of files = {}". \
                                format(SingleFrameDir,
                                       len(uniform_class.DicomDataset))
                            Modality = supported_sop_classes[SOPClassUID]
                            ModalityConvertorClass = getattr(
                                sop, ("LegacyConvertedEnhanced" +
                                      Modality + "Image"))
                            log.append("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
                                       "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            log.extend(
                                re.split(
                                    '\n',
                                    "Distinguish Series ({}): \n\t\tSource"
                                    "StudyUID: ".format(n, stdy_UID) +
                                    "\n\t\tSourceSeriesUID {}\n\t\t"
                                    "PixelSpacing = [{}\t{}\t{}]".format(
                                        sris_UID, spacing_element[0][0],
                                        spacing_element[0][1],
                                        spacing_element[0][2]) +
                                        "\n\t\tImageOrientation ="
                                        " \n\t\t\t\t\trow_vector = "
                                        "[{}\t{}\t{}]\n\t\t\t\t\tcol_vector "
                                        "= [{}\t{}\t{}]".format(
                                            orientation_element[0][0],
                                            orientation_element[0][1],
                                            orientation_element[0][2],
                                            orientation_element[0][3],
                                            orientation_element[0][4],
                                            orientation_element[0][5])))
                            for dds in uniform_class.DicomDataset:
                                final_ds.append(dds[0])
                            uniform_class.Print(3)
                            # try:
                            ModalityConvertorObj = ModalityConvertorClass(
                                egacy_datasets = final_ds,
                                series_instance_uid = generate_uid(),
                                series_number = final_ds[0].SeriesNumber,
                                sop_instance_uid = generate_uid(),
                                instance_number = final_ds[0].InstanceNumber)
                            id = "_%02d_.dcm" % n
                            FileName = os.path.join(OutputPrefix,
                                                    Modality + id)
                            folder = os.path.dirname(FileName)
                            if not os.path.exists(folder):
                                os.makedirs(folder)
                            # x.file_meta['']
                            dcmwrite(filename = FileName,
                                     dataset = ModalityConvertorObj,
                                     write_like_original=False)
                            log.append("File " + FileName +
                                       " was successfully written ...")
                            n += 1
                            # except BaseException as err:
                            #     err_message = "Conversion error for input
                            # folder \n\t\t{} \n \t\tNumber of files = {} \
                            # n\tError type {}: --> {}".\
                            #         format(SingleFrameDir, len(final_ds),
                            # type(err), err)
                            #     print(err_message)
                            #     log.append(err_message)
                            #     success = False
                            # Output.append((success, err_message))
    return tuple(SOPClassCategory)