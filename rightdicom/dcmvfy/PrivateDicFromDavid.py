
from  pydicom.datadict import add_private_dict_entry
add_private_dict_entry(
    "AEGIS_DICOM_2.00",
    0x00030000,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "ELSCINT1",
    0x00030001,
    'OW',
    "Offset List Structure",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00030008,
    'US',
    "ISI Command Field",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00030011,
    'US',
    "Attach ID Application Code",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00030012,
    'UL',
    "Attach ID Message Count",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00030013,
    'DA',
    "Attach ID Date",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00030014,
    'TM',
    "Attach ID Time",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00030020,
    'US',
    "Message Type",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00030030,
    'DA',
    "Max Waiting Date",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00030031,
    'TM',
    "Max Waiting Time",
    '1')
add_private_dict_entry(
    "AEGIS_DICOM_2.00",
    0x00050000,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090000,
    'LT',
    "Data Object Recognition Code",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00090000,
    'UL',
    "File Location",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090000,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON:1.2.840.113680.1.0:0910",
    0x00090000,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "AEGIS_DICOM_2.00",
    0x00090000,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "BioPri",
    0x00090000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090000,
    'CS',
    "Analysis Type",
    '1')
add_private_dict_entry(
    "DCMTK_ANONYMIZER",
    0x00090000,
    'SQ',
    "Anonymizer UID Map",
    '1')
add_private_dict_entry(
    "EMAGEON STUDY HOME",
    0x00090000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "EMAGEON JPEG2K INFO",
    0x00090000,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "HMC - CT - ID",
    0x00090000,
    'OB',
    "Image ID Information Patient Name ID",
    '1')
add_private_dict_entry(
    "MERGE TECHNOLOGIES, INC.",
    0x00090000,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00090000,
    'LT',
    "Original File Name",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00090000,
    'DS',
    "Number of Measurements",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INSTANCE MANIFEST",
    0x00090000,
    'SQ',
    "Temporary Original Header Sequence",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_OT3",
    0x00090000,
    'LO',
    "HIS/RIS Study ID",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00090001,
    'UL',
    "File Size",
    '1')
add_private_dict_entry(
    "BrainLAB_Conversion",
    0x00090001,
    'LO',
    "Export Platform Name",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090001,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON:1.2.840.113680.1.0:0910",
    0x00090001,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "BioPri",
    0x00090001,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "DicomUtils 20100512",
    0x00090001,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090001,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "EMAGEON JPEG2K INFO",
    0x00090001,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "EMAGEON STUDY HOME",
    0x00090001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x00090001,
    'LO',
    "Full Fidelity",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090001,
    'LO',
    "Implementation Version Name",
    '2')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090001,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090001,
    'UL',
    "Rate Vector",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00090001,
    'LO',
    "Technologist",
    '1')
add_private_dict_entry(
    "HMC - CT - ID",
    0x00090001,
    'OB',
    "Image ID Information Patient Comment",
    '1')
add_private_dict_entry(
    "SECTRA_Ident_01",
    0x00090001,
    'SH',
    "Request number",
    '1')
add_private_dict_entry(
    "FFP DATA",
    0x00090001,
    'UN',
    "CR Header Information",
    '1')
add_private_dict_entry(
    "ISI",
    0x00090001,
    'UN',
    "SIENET General Purpose IMGEF",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00090001,
    'UN',
    "RIS Patient Info IMGEF",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00090001,
    'US',
    "SIENET Command Field",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00090001,
    'SQ',
    "Event Timer Sequence",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00090001,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "BrainLAB_Conversion",
    0x00090002,
    'OB',
    "Export Platform Data",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090002,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON:1.2.840.113680.1.0:0910",
    0x00090002,
    'LO',
    "Patient Registration Custom Field 1",
    '1')
add_private_dict_entry(
    "BioPri",
    0x00090002,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtImage",
    0x00090002,
    'IS',
    "LINAC Energy",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090002,
    'SQ',
    "Pulser Equipment Sequence",
    '1')
add_private_dict_entry(
    "DicomUtils 20100512",
    0x00090002,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090002,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090002,
    'LO',
    "Patient ID",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x00090002,
    'SH',
    "Suite Id",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090002,
    'UL',
    "Count Vector",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00090002,
    'LO',
    "Scheduled Study DateTime",
    '1')
add_private_dict_entry(
    "SECTRA_Ident_01",
    0x00090002,
    'SH',
    "Examination number",
    '1')
add_private_dict_entry(
    "POLYTRON-SMS 2.5",
    0x00090002,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00090002,
    'FD',
    "Event Time Interval",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00090002,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "ACUSON",
    0x00090003,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON:1.2.840.113680.1.0:0910",
    0x00090003,
    'LO',
    "Patient Registration Custom Field 2",
    '1')
add_private_dict_entry(
    "BioPri",
    0x00090003,
    'LO',
    "?",
    '1-n')
add_private_dict_entry(
    "DicomUtils 20100512",
    0x00090003,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090003,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090003,
    'SH',
    "Patient Compatible Version",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090003,
    'UL',
    "Time Vector",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00090003,
    'OB',
    "Study App Data",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00090003,
    'SQ',
    "Event Code Sequence",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00090003,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090004,
    'LO',
    "Image Data Consistency",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090004,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON:1.2.840.113680.1.0:0910",
    0x00090004,
    'LO',
    "Indications",
    '1')
add_private_dict_entry(
    "BioPri",
    0x00090004,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Camtronics image level data",
    0x00090004,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090004,
    'LO',
    "Segment Name",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090004,
    'CS',
    "Pulser Type",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtImage",
    0x00090004,
    'IS',
    "LINAC Output",
    '1')
add_private_dict_entry(
    "DicomUtils 20100512",
    0x00090004,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090004,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00090004,
    'SH',
    "Image Control Unit",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x00090004,
    'SH',
    "Product Id",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090004,
    'SH',
    "Patient Software Version",
    '1')
add_private_dict_entry(
    "SECTRA_Ident_01",
    0x00090004,
    'LO',
    "Series Identifier",
    '1')
add_private_dict_entry(
    "POLYTRON-SMS 2.5",
    0x00090004,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00090004,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "ACUSON",
    0x00090005,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "BioPri",
    0x00090005,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090005,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00090005,
    'OW',
    "Image UID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090005,
    'DT',
    "Patient DateTime",
    '1')
add_private_dict_entry(
    "SECTRA_Ident_01",
    0x00090005,
    'LO',
    "Series Order",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090006,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Camtronics image level data",
    0x00090006,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090006,
    'LT',
    "Pulser Notes",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00090006,
    'OW',
    "Route Image UID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090006,
    'SL',
    "Patient Type",
    '1')
add_private_dict_entry(
    "SECTRA_Ident_01",
    0x00090006,
    'LO',
    "File Name",
    '1')
add_private_dict_entry(
    "POLYTRON-SMS 2.5",
    0x00090006,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090007,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "BioPri",
    0x00090007,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090007,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090007,
    'UI',
    "Exam ID",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090007,
    'UL',
    "Angle Vector",
    '1-n')
add_private_dict_entry(
    "SECTRA_Ident_01",
    0x00090007,
    'LO',
    "Image Data ID",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00090008,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090008,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090008,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "BioPri",
    0x00090008,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090008,
    'SQ',
    "Receiver Equipment Sequence",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090008,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00090008,
    'UL',
    "Image Display Information Version Number",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090008,
    'SH',
    "Exam Compatible Version",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090008,
    'US',
    "Camera Shape",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090009,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "BioPri",
    0x00090009,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Camtronics image level data",
    0x00090009,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00090009,
    'UL',
    "Patient Information Version Number",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090009,
    'SH',
    "Exam Software Version",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x0009000A,
    'CS',
    "Amplifier Type",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x0009000a,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009000a,
    'UI',
    "Scan ID",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x0009000b,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009000b,
    'SH',
    "Scan Compatible Version",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x0009000C,
    'LT',
    "Receiver Notes",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x0009000C,
    'OW',
    "Film UID",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x0009000c,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009000c,
    'SH',
    "Scan Software Version",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x0009000d,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009000d,
    'DT',
    "Scan Date Time",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x0009000E,
    'SQ',
    "Pre-Amplifier Equipment Sequence",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x0009000e,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009000e,
    'DT',
    "Scan Ready",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x0009000F,
    'LT',
    "Pre-Amplifier Notes",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x0009000f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON:1.2.840.113680.1.0:0910",
    0x0009000f,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009000f,
    'ST',
    "Scan Description",
    '1')
add_private_dict_entry(
    "PHILIPS MR",
    0x00090010,
    'LO',
    "SPI Release",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00090010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART 12",
    0x00090010,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090010,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00090010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "BioPri",
    0x00090010,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090010,
    'SQ',
    "Transmit Transducer Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/ComponentSeries",
    0x00090010,
    'ST',
    "Actual Environmental Conditions",
    '1')
add_private_dict_entry(
    "DCMTK_ANONYMIZER",
    0x00090010,
    'UI',
    "Anonymizer UID Key",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00090010,
    'CS',
    "Exposure Unit Type Code",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090010,
    'LO',
    "Study Name",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090010,
    'LO',
    "Hospital Name",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x00090010,
    'SQ',
    "GE Private Image Thumbnail Sequence",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090010,
    'US',
    "Whole Body Spots",
    '1')
add_private_dict_entry(
    "MeVis eatDicom",
    0x00090010,
    'LO',
    "eatDicom Version",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00090010,
    'LT',
    "Original File Location",
    '1')
add_private_dict_entry(
    "SPI RELEASE 1",
    0x00090010,
    'LO',
    "Comments",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00090010,
    'LO',
    "Comments",
    '1')
add_private_dict_entry(
    "SPI",
    0x00090010,
    'LO',
    "Comments",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00090010,
    'CS',
    "Storage Mode",
    '1')
add_private_dict_entry(
    "SIEMENS DICOM",
    0x00090010,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INSTANCE MANIFEST",
    0x00090010,
    'AE',
    "syngo Index Source AE Title",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  LAB",
    0x00090010,
    'LO',
    "Generator Identification Label",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  IDE",
    0x00090010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00090010,
    'LO',
    "Recognition Code",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090011,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00090011,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtDetector",
    0x00090011,
    'DS',
    "Internal Detector Frame Time",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxDetector",
    0x00090011,
    'DS',
    "Internal Detector Frame Time",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090011,
    'SQ',
    "Receive Transducer Sequence",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090011,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090011,
    'LO',
    "Scanner Description",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090011,
    'SL',
    "Study Flags",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090011,
    'US',
    "Worklist Flag",
    '1')
add_private_dict_entry(
    "MeVis eatDicom",
    0x00090011,
    'ST',
    "eatDicom Options",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  LAB",
    0x00090011,
    'LO',
    "Gantry Identification Label",
    '1')
add_private_dict_entry(
    "PHILIPS MR",
    0x00090012,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090012,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090012,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090012,
    'DS',
    "Pre-procedure Catheter Size",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtDetector",
    0x00090012,
    'DS',
    "Number of Frames Integrated",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxDetector",
    0x00090012,
    'DS',
    "Number of Frames Integrated",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090012,
    'US',
    "Number of Elements",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090012,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x00090012,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090012,
    'LO',
    "Manufacturer",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090012,
    'SL',
    "Study Type",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090012,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00090012,
    'UL',
    "Evaluation Mask - Image",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  LAB",
    0x00090012,
    'LO',
    "X-Ray Tube Identification Label",
    '1')
add_private_dict_entry(
    "SIEMENS DICOM",
    0x00090012,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090013,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00090013,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090013,
    'DS',
    "Pre-procedure Reference Diameter",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090013,
    'CS',
    "Element Shape",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090013,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090013,
    'UI',
    "FOR Identifier",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090013,
    'ST',
    "Sequence Type",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  LAB",
    0x00090013,
    'LO',
    "Detector Identification Label",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090014,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00090014,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090014,
    'DS',
    "Pre-procedure Minimum Lumen Diameter",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090014,
    'DS',
    "Element Dimension A",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090014,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090014,
    'LO',
    "Landmark Name",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090014,
    'ST',
    "Sequence Name",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00090014,
    'LO',
    "Receiver PLA",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  LAB",
    0x00090014,
    'LO',
    "DAS Identification Label",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090015,
    'LO',
    "Unique Identifier",
    '1')
add_private_dict_entry(
    "ACUSON",
    0x00090015,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00090015,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090015,
    'DS',
    "Pre-procedure Average Diameter",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090015,
    'DS',
    "Element Dimension B",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090015,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090015,
    'SH',
    "Landmark Abbrev",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090015,
    'UL',
    "Average RR Time Vector",
    '1-n')
add_private_dict_entry(
    "SPI RELEASE 1",
    0x00090015,
    'LO',
    "UID",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00090015,
    'LO',
    "UID",
    '1')
add_private_dict_entry(
    "SPI",
    0x00090015,
    'LO',
    "UID",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  LAB",
    0x00090015,
    'LO',
    "SMI Identification Label",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090016,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Camtronics image level data",
    0x00090016,
    'AE',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090016,
    'DS',
    "Pre-procedure Stenosis Length",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090016,
    'DS',
    "Element Pitch",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090016,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090016,
    'SL',
    "Patient Position",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090016,
    'UL',
    "Low Limit Vector",
    '1-n')
add_private_dict_entry(
    "SIENET",
    0x00090016,
    'US',
    "Transfer Priority",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  LAB",
    0x00090016,
    'LO',
    "CPU Identification Label",
    '1')
add_private_dict_entry(
    "Camtronics image level data",
    0x00090017,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090017,
    'DS',
    "Pre-procedure Stenosis %",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090017,
    'DS',
    "Measured Beam Dimension A",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090017,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090017,
    'SL',
    "Scan Perspective",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x00090017,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090017,
    'UL',
    "High Limit Vector",
    '1-n')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090018,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090018,
    'DS',
    "Pre-procedure Geometric Area Reduction %",
    '1')
add_private_dict_entry(
    "Camtronics image level data",
    0x00090018,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090018,
    'DS',
    "Measured Beam Dimension B",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090018,
    'SL',
    "Scan Type",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090018,
    'UL',
    "Begin Index Vector",
    '1-n')
add_private_dict_entry(
    "PAPYRUS",
    0x00090018,
    'LT',
    "Data Set Identifier",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x00090019,
    'DS',
    "Location of Measured Beam Diameter",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090019,
    'SL',
    "Scan Mode",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090019,
    'UL',
    "End Index Vector",
    '1-n')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x0009001A,
    'DS',
    "Nominal Frequency",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009001a,
    'SL',
    "Start Condition",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x0009001a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x0009001a,
    'UL',
    "Raw Time Vector",
    '1-n')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x0009001B,
    'DS',
    "Measured Center Frequency",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009001b,
    'SL',
    "Start Condition Data",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x0009001b,
    'LO',
    "Image Type String",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipment",
    0x0009001C,
    'DS',
    "Measured Bandwidth",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009001c,
    'SL',
    "Sel Stop Condition",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009001d,
    'SL',
    "Sel Stop Condition Data",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x0009001d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009001e,
    'SL',
    "Collect Deadtime",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0009001e,
    'UI',
    "Dataset UID",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x0009001e,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009001f,
    'SL',
    "Collect Singles",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090020,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/ComponentStudy",
    0x00090020,
    'DA',
    "Expiry Date",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtDetector",
    0x00090020,
    'SQ',
    "Detector Temperature Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxDetector",
    0x00090020,
    'SQ',
    "Detector Temperature Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090020,
    'SQ',
    "Pulser Settings Sequence",
    '1')
add_private_dict_entry(
    "DCMTK_ANONYMIZER",
    0x00090020,
    'UI',
    "Anonymizer UID Value",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090020,
    'LO',
    "Series Object Name",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090020,
    'SL',
    "Collect Count Rate",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x00090020,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090020,
    'DA',
    "Object Insertion Date",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  ORI",
    0x00090020,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  LAB",
    0x00090020,
    'SH',
    "Header Version",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090021,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "Brainlab-S9-History",
    0x00090021,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090021,
    'SL',
    "Series Flags",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090021,
    'SL',
    "Count Rate Period",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090022,
    'DS',
    "Post-procedure Catheter Size",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtDetector",
    0x00090022,
    'DS',
    "Sensor Name",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxDetector",
    0x00090022,
    'DS',
    "Sensor Name",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090022,
    'DS',
    "Pulse Width",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090022,
    'SH',
    "User Orientation",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090022,
    'SL',
    "Delayed Events",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090022,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090023,
    'DS',
    "Post-procedure Reference Diameter",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090023,
    'SL',
    "Initiation Type",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090023,
    'SL',
    "Delayed Bias",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090023,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Brainlab-S9-History",
    0x00090024,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090024,
    'DS',
    "Post-procedure Minimum Lumen Diameter",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtDetector",
    0x00090024,
    'DS',
    "Horizontal Offset of Sensor",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxDetector",
    0x00090024,
    'DS',
    "Horizontal Offset of Sensor",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090024,
    'DS',
    "Excitation Frequency",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00090024,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090024,
    'SL',
    "Initiation Delay",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090024,
    'SL',
    "Word Size",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090025,
    'DS',
    "Post-procedure Average Diameter",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090025,
    'SL',
    "Initiation Count Rate",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090025,
    'SL',
    "Axial Acceptance",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00090025,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090026,
    'DS',
    "Post-procedure Stenosis Length",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090026,
    'CS',
    "Modulation Type",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtDetector",
    0x00090026,
    'DS',
    "Vertical Offset of Sensor",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxDetector",
    0x00090026,
    'DS',
    "Vertical Offset of Sensor",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090026,
    'SL',
    "Number Energy Sets",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090026,
    'SL',
    "Axial Angle 3D",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00090026,
    'DA',
    "Last Move Date",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090027,
    'DS',
    "Post-procedure Stenosis %",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x00090027,
    'SL',
    "Image Actual Date",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090027,
    'SL',
    "Number Detectors",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090027,
    'SL',
    "Theta Compression",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00090027,
    'TM',
    "Last Move Time",
    '1')
add_private_dict_entry(
    "QCA Results",
    0x00090028,
    'DS',
    "Post-procedure Geometric Area Reduction %",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtDetector",
    0x00090028,
    'DS',
    "Sensor Temperature",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxDetector",
    0x00090028,
    'DS',
    "Sensor Temperature",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090028,
    'DS',
    "Damping",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090028,
    'SL',
    "Number RR Windows",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090028,
    'SL',
    "Axial Compression",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090029,
    'FL',
    "Gantry Tilt Angle",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090029,
    'SL',
    "Number MG Time Slots",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00090029,
    'LO',
    "Actual User",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0009002a,
    'SL',
    "Number View Sets",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009002a,
    'SL',
    "Collimation",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0009002b,
    'LO',
    "Trigger History UID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009002b,
    'SL',
    "Scan FOV",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0009002c,
    'LO',
    "Series Comments",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009002c,
    'SL',
    "Axial FOV",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0009002d,
    'SL',
    "Track Beat Average",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009002d,
    'SL',
    "Event Separation",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0009002e,
    'FD',
    "Distance Prescribed",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009002e,
    'SL',
    "Mask Width",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0009002f,
    'SL',
    "Table Direction",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009002f,
    'SL',
    "Binning Mode",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x0009002f,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090030,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Brainlab-S9-History",
    0x00090030,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090030,
    'SQ',
    "Receiver Settings Sequence",
    '1')
add_private_dict_entry(
    "DCMTK_ANONYMIZER",
    0x00090030,
    'SQ',
    "Anonymizer Patient ID Map",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090030,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x00090030,
    'SH',
    "Service Id",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090030,
    'SL',
    "Trig Rej Method",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x00090030,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00090030,
    'US',
    "Byte Offset of Original Header",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  IDE",
    0x00090030,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  ORI",
    0x00090030,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090030,
    'SQ',
    "Instance Object States",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090031,
    'LT',
    "PACS Unique Identifier",
    '1')
add_private_dict_entry(
    "Brainlab-S9-History",
    0x00090031,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090031,
    'DS',
    "Acquired Soundpath Length",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x00090031,
    'SH',
    "Mobile Location Number",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090031,
    'SL',
    "Number For Reject",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00090031,
    'UL',
    "Length of Original Header",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  IDE",
    0x00090031,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090031,
    'SQ',
    "Series Object States",
    '1')
add_private_dict_entry(
    "Brainlab-S9-History",
    0x00090032,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090032,
    'CS',
    "Acquisition Compression Type",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090032,
    'SL',
    "Lower Reject Limit",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  IDE",
    0x00090032,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "Brainlab-S9-History",
    0x00090033,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090033,
    'IS',
    "Acquisition Sample Size",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090033,
    'FD',
    "Rotational Continuous Speed",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090033,
    'SL',
    "Upper Reject Limit",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090034,
    'LT',
    "Cluster Unique Identifier",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090034,
    'DS',
    "Rectifier Smoothing",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090034,
    'SL',
    "Gantry Motion Type (Retired)",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090034,
    'SL',
    "Triggers Acquired",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  IDE",
    0x00090034,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090035,
    'SQ',
    "DAC Sequence",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090035,
    'SL',
    "Gantry Locus Type",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090035,
    'SL',
    "Triggers Rejected",
    '1')
add_private_dict_entry(
    "BioscanMedisoScivisNanoSPECT",
    0x00090035,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090036,
    'CS',
    "DAC Type",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090036,
    'LO',
    "Tracer Name",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x00090036,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090037,
    'LO',
    "Batch Description",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090037,
    'SL',
    "Starting Heart Rate",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090038,
    'LT',
    "System Unique Identifier",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090038,
    'DS',
    "DAC Gain Points",
    '1-n')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090038,
    'FL',
    "Tracer Activity",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090038,
    'SL',
    "RR Window Width",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090039,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090039,
    'DT',
    "Measured Date Time",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090039,
    'SL',
    "RR Window Offset",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090039,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x0009003A,
    'DS',
    "DAC Time Points",
    '1-n')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009003a,
    'FL',
    "Pre Inj Volume",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0009003a,
    'SL',
    "Percent Cycle Imaged",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009003b,
    'DT',
    "Administered Date Time",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x0009003C,
    'DS',
    "DAC Amplitude",
    '1-n')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009003c,
    'FL',
    "Post Injected Activity",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009003d,
    'DT',
    "Post Injected Date Time",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009003e,
    'SH',
    "Radio Nuclide Name",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0009003e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009003f,
    'FL',
    "Half Life",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0009003f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090040,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00090040,
    'SQ',
    "Alternate Image Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090040,
    'SQ',
    "Dark Current Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090040,
    'SQ',
    "Dark Current Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090040,
    'SQ',
    "Pre-Amplifier Settings Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/ComponentSeries",
    0x00090040,
    'ST',
    "Environmental Conditions",
    '1')
add_private_dict_entry(
    "DCMTK_ANONYMIZER",
    0x00090040,
    'LO',
    "Anonymizer Patient ID Key",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090040,
    'FL',
    "Positron Fraction",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090040,
    'PN',
    "Patient Object Name",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090040,
    'DA',
    "?",
    '1')
add_private_dict_entry(
    "SPI RELEASE 1",
    0x00090040,
    'US',
    "Data Object Type",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00090040,
    'US',
    "Data Object Type",
    '1')
add_private_dict_entry(
    "SPI",
    0x00090040,
    'US',
    "Data Object Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00090040,
    'US',
    "Byte Offset of Pixelmatrix",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090040,
    'DT',
    "Last Access Time",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  IDE",
    0x00090040,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090041,
    'SL',
    "Patient Flags",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090041,
    'SL',
    "Source 1 Holder",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090041,
    'TM',
    "?",
    '1')
add_private_dict_entry(
    "SPI RELEASE 1",
    0x00090041,
    'SH',
    "Data Object Subtype",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00090041,
    'SH',
    "Data Object Subtype",
    '1')
add_private_dict_entry(
    "SPI",
    0x00090041,
    'SH',
    "Data Object Subtype",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00090041,
    'UL',
    "Length of Pixelmatrix In Bytes",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090041,
    'CS',
    "Delete Protected Status",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090042,
    'DA',
    "Patient Creation Date",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090042,
    'FL',
    "Source 1 Activity",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00090042,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090042,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090042,
    'CS',
    "Received from Archive Status",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  IDE",
    0x00090042,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090043,
    'DT',
    "Source 1 Meas DT",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090043,
    'TM',
    "Patient Creation Time",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00090043,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090043,
    'CS',
    "Archive Status",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090044,
    'SH',
    "Source 1 Radio Nuclide",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090044,
    'SL',
    "Num Views Acquired (Retired)",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090044,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090044,
    'AE',
    "Location",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090045,
    'FL',
    "Source 1 Half Life",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090045,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090045,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090045,
    'CS',
    "Logical Deleted Status",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090046,
    'SL',
    "Source 2 Holder",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00090046,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090046,
    'DT',
    "Insert Time",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090047,
    'FL',
    "Source 2 Activity",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090047,
    'IS',
    "Visible Instances on Series Level",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090048,
    'DT',
    "Source 2 Meas DT",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00090048,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090048,
    'LO',
    "Protocol Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090048,
    'IS',
    "Unarchived Instances",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090049,
    'SH',
    "Source 2 Radio Nuclide",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090049,
    'IS',
    "Visible Instances on Study Level",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009004a,
    'FL',
    "Source 2 Half Life",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009004b,
    'SL',
    "Source Speed",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009004c,
    'FL',
    "Source Location",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009004d,
    'SL',
    "Emission Present",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009004e,
    'SL',
    "Lower Axial Acc",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0009004e,
    'LO',
    "CMS Body Part Examined",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009004f,
    'SL',
    "Upper Axial Acc",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0009004f,
    'LO',
    "Is Protected",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090050,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090050,
    'OX',
    "Dark Current Counts",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090050,
    'OX',
    "Dark Current Counts",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090050,
    'SQ',
    "Transmit Transducer Settings Sequence",
    '1')
add_private_dict_entry(
    "DCMTK_ANONYMIZER",
    0x00090050,
    'LO',
    "Anonymizer Patient ID Value",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090050,
    'SL',
    "Lower Coinc Limit",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090050,
    'CS',
    "CMS Patient Position",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x00090050,
    'CS',
    "Hidden Instance",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  IDE",
    0x00090050,
    'DA',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00090050,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS AX INSPACE_EP",
    0x00090050,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090051,
    'LT',
    "Study Unique Identifier",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090051,
    'SQ',
    "Receive Transducer Settings Sequence",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090051,
    'SL',
    "Upper Coinc Limit",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090051,
    'LO',
    "CMI Contrast Bolus Agent",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00090051,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  IDE",
    0x00090051,
    'TM',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS AX INSPACE_EP",
    0x00090051,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090052,
    'DS',
    "Incident Angle",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090052,
    'SL',
    "Coinc Delay Offset",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090052,
    'LO',
    "CMS institution Name",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090053,
    'SL',
    "Coinc Output Mode",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090053,
    'LO',
    "CMS Institutional Department Name",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090054,
    'ST',
    "Coupling Technique",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090054,
    'SL',
    "Upper Energy Limit",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090054,
    'LO',
    "CMS Series Description",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090055,
    'SL',
    "Lower Energy Limit",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090055,
    'LO',
    "CMS Operators Name",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090056,
    'ST',
    "Coupling Medium",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090056,
    'UI',
    "Normal Cal ID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090056,
    'LO',
    "CMS Performing Physicians Name",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090057,
    'DS',
    "Coupling Velocity",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090057,
    'UI',
    "Normal 2D Cal ID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090057,
    'ST',
    "CMS Institution Address",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090058,
    'DS',
    "Crystal Center Location X",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090058,
    'UI',
    "Blank Cal ID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090058,
    'LO',
    "CMI Image Comments",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090059,
    'DS',
    "Crystal Center Location Z",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090059,
    'UI',
    "WC Cal ID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00090059,
    'LO',
    "CMI Instance Creation DateTime",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x0009005A,
    'DS',
    "Sound Path Length",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0009005A,
    'LO',
    "MPPS Step Status",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009005a,
    'SL',
    "Derived",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0009005B,
    'IS',
    "Filmed Count",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009005b,
    'LO',
    "Contrast Agent",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x0009005C,
    'ST',
    "Delay Law Identifier",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0009005C,
    'LO',
    "Is Allow Cascade Save",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009005c,
    'UI',
    "frame_id",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0009005D,
    'LO',
    "Is Allow Cascade Protect",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009005d,
    'UI',
    "scan_id",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0009005E,
    'LO',
    "Is Deleted",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009005e,
    'UI',
    "exam_id",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009005f,
    'LO',
    "patient_id",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090060,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090060,
    'SQ',
    "Gain Correction Reference Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090060,
    'SQ',
    "Gain Correction Reference Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090060,
    'SQ',
    "Gate Settings Sequence",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090060,
    'SH',
    "compatible_version",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090061,
    'LT',
    "Series Unique Identifier",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090061,
    'SH',
    "software_version",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090062,
    'DS',
    "Gate Threshold",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090062,
    'ST',
    "where_is_frame",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090063,
    'SL',
    "frame_size",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090064,
    'DS',
    "Velocity of Sound",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090064,
    'SL',
    "file_exists",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090065,
    'SL',
    "patient_entry",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090066,
    'FL',
    "table_height",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090067,
    'FL',
    "table_z_position",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090068,
    'DT',
    "landmark_datetime",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090069,
    'SL',
    "slice_count",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009006a,
    'FL',
    "start_location",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009006b,
    'SL',
    "acq_delay",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009006c,
    'DT',
    "acq_start",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009006d,
    'SL',
    "acq_duration",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009006e,
    'SL',
    "acq_bin_dur",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009006f,
    'SL',
    "acq_bin_start",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090070,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090070,
    'OX',
    "Air Counts",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090070,
    'OX',
    "Air Counts",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090070,
    'SQ',
    "Calibration Settings Sequence",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090070,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090070,
    'SL',
    "actual_stop_cond",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00090070,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090071,
    'DS',
    "KV Used in Gain Calibration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090071,
    'DS',
    "KV Used in Gain Calibration",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090071,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090071,
    'FD',
    "total_prompts",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00090071,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090072,
    'DS',
    "MA Used in Gain Calibration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090072,
    'DS',
    "MA Used in Gain Calibration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090072,
    'ST',
    "Calibration Procedure",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090072,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090072,
    'FD',
    "total_delays",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00090072,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090073,
    'DS',
    "Number of Frames Used for Integration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090073,
    'DS',
    "Number of Frames Used for Integration",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090073,
    'SL',
    "frame_valid",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00090073,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090074,
    'LO',
    "Filter Material Used in Gain Calibration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090074,
    'LO',
    "Filter Material Used in Gain Calibration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090074,
    'SH',
    "Procedure Version",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x00090074,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090074,
    'SL',
    "validity_info",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00090074,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090075,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090075,
    'DS',
    "Filter Thickness Used in Gain Calibration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090075,
    'DS',
    "Filter Thickness Used in Gain Calibration",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090075,
    'SL',
    "archived",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00090075,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090076,
    'DA',
    "Date of Gain Calibration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090076,
    'DA',
    "Date of Gain Calibration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090076,
    'DA',
    "Procedure Creation Date",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090076,
    'SL',
    "compression",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090077,
    'TM',
    "Time of Gain Calibration",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090077,
    'TM',
    "Time of Gain Calibration",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090077,
    'SL',
    "uncompressed_size",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x00090078,
    'DA',
    "Procedure Expiration Date",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090078,
    'SL',
    "accum_bin_dur",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090079,
    'SH',
    "Image Set Compatible Version",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x0009007A,
    'DA',
    "Procedure Last Modified Date",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x0009007a,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009007a,
    'SH',
    "Image Set Software Version",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009007b,
    'DT',
    "Image Set Date Time",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x0009007C,
    'TM',
    "Calibration Time",
    '1-n')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009007c,
    'SL',
    "Image Set Source",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009007d,
    'SL',
    "Image Set Contents",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeUsEquipmentSettings",
    0x0009007E,
    'DA',
    "Calibration Date",
    '1-n')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009007e,
    'SL',
    "Image Set Type",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009007f,
    'DS',
    "Image Set Reference",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090080,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090080,
    'OB',
    "Bad Pixel Image",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090080,
    'OB',
    "Bad Pixel Image",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00090080,
    'LO',
    "Kanji Hospital Name",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090080,
    'SL',
    "Multi Patient",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00090080,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090081,
    'SL',
    "Number of Normals",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090082,
    'UI',
    "Color Map ID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090083,
    'SL',
    "Window Level Type",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090084,
    'FL',
    "Rotate",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090085,
    'SL',
    "Flip",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090086,
    'FL',
    "Zoom",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090087,
    'SL',
    "PanX",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090088,
    'SL',
    "PanY",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090089,
    'FL',
    "Window Level Min",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009008a,
    'FL',
    "Window Level Max",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009008b,
    'SL',
    "ReconMethod",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009008c,
    'SL',
    "Attenuation",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009008d,
    'FL',
    "Attenuation Coefficient",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009008e,
    'SL',
    "BP Filter",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009008f,
    'FL',
    "BP Filter Cutoff",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00090090,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00090090,
    'ST',
    "Distribution Code",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090090,
    'SL',
    "BP Filter Order",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00090091,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090091,
    'FL',
    "BP Filter Center I",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00090092,
    'SH',
    "Kanji Department Name",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090092,
    'FL',
    "BP Filter Center P",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090093,
    'SL',
    "Atten Smooth",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090094,
    'SL',
    "Atten Smooth Param",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090095,
    'SL',
    "Angle Smooth Param",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090096,
    'UI',
    "Well CounterCal ID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090097,
    'UI',
    "Trans Scan ID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090098,
    'UI',
    "Norm Cal ID",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeCtCalibrationData",
    0x00090099,
    'LT',
    "Calibration Notes",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeDxCalibrationData",
    0x00090099,
    'LT',
    "Calibration Notes",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00090099,
    'UI',
    "Blnk Cal ID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009009a,
    'FL',
    "CAC Edge Threshold",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009009b,
    'FL',
    "CAC Skull Offset",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009009c,
    'UI',
    "Emiss Sub ID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009009d,
    'SS',
    "Radial Filter 3D",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009009e,
    'FL',
    "Radial Cutoff 3D",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0009009f,
    'SL',
    "Axial Filter 3D",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO INDEX SERVICE",
    0x000900A0,
    'LO',
    "Sender System Device Name",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x000900a0,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a0,
    'FL',
    "Axial Cutoff 3D",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x000900a1,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a1,
    'FL',
    "Axial Start",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x000900a2,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a2,
    'FL',
    "Axial Spacing",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a3,
    'SL',
    "Axial Angles Used",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a4,
    'SH',
    "compatible_version",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a5,
    'SH',
    "software_version",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a6,
    'SL',
    "slice_number",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a7,
    'FL',
    "total_counts",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a8,
    'OB',
    "other_atts",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900a9,
    'SL',
    "other_atts_size",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900aa,
    'SL',
    "archived",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900ab,
    'FL',
    "bp_center_x",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900ac,
    'FL',
    "bp_center_y",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900ad,
    'UI',
    "trans_frame_id",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900ae,
    'UI',
    "tpluse_frame_id",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900b1,
    'FL',
    "profile_spacing",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900b2,
    'SS',
    "IR Num Iterations",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900b3,
    'SS',
    "IR Num Subsets",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900b4,
    'FL',
    "IR Recon FOV",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900b5,
    'SS',
    "IR Corr Model",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900b6,
    'SS',
    "IR Loop Filter",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900b7,
    'FL',
    "IR Pre Filt Param",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900b8,
    'FL',
    "IR Loop Filt Param",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900b9,
    'FL',
    "Response Filt Param",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900ba,
    'SS',
    "Post Filter",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900bb,
    'FL',
    "Post Filter Param",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900bc,
    'SS',
    "IR Regularize",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900bd,
    'FL',
    "IR Regularize Param",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900be,
    'SS',
    "AC BP Filter",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900bf,
    'FL',
    "AC BP Filt Cutoff",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x000900c0,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c0,
    'SL',
    "AC BP Filt Order",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900c0,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x000900c1,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c1,
    'SS',
    "AC Img Smooth",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900c1,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c2,
    'FL',
    "AC Img Smooth Parm",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c3,
    'SL',
    "Scatter Method",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c4,
    'SS',
    "Scatter Num Iter",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900c4,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c5,
    'FL',
    "Scatter Parm",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c6,
    'FL',
    "seg_qc_parm",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c7,
    'SL',
    "overlap",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c8,
    'UI',
    "ovlp_frm_id",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900c9,
    'UI',
    "ovlp_trans_frm_id",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900ca,
    'UI',
    "ovlp_tpulse_frm_id",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900cb,
    'FL',
    "vqc_x_axis_trans",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900cc,
    'FL',
    "vqc_x_axis_tilt",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900cd,
    'FL',
    "vqc_y_axis_trans",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900ce,
    'FL',
    "vqc_y_axis_swivel",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900cf,
    'FL',
    "vqc_z_axis_trans",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d0,
    'FL',
    "vqc_z_axis_roll",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d1,
    'LO',
    "ctac_conv_scale",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d2,
    'UI',
    "image_set_id",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900d2,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d3,
    'SL',
    "contrast_route",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d4,
    'LO',
    "ctac_conv_scale",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d5,
    'FL',
    "loop_filter_parm",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900d5,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d6,
    'FL',
    "image_one_loc",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d7,
    'FL',
    "image_index_loc",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d8,
    'SL',
    "frame_number",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900d9,
    'SL',
    "list_file_exists",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900da,
    'ST',
    "where_is_list_frame",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900db,
    'SL',
    "ir_z_filter_flag",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900dc,
    'FL',
    "ir_z_filter_ratio",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900dc,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900dd,
    'US',
    "num_of_rr_interval",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900de,
    'US',
    "num_of_time_slots",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900de,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900df,
    'US',
    "num_of_slices",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900df,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e0,
    'US',
    "num_of_time_slices",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900e0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e1,
    'SL',
    "unlisted_scan",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900e1,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e2,
    'SL',
    "rest_stress",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x000900e2,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e3,
    'FL',
    "phase percentage",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x000900e3,
    'UI',
    "Equipment UID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e4,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e5,
    'FL',
    "left shift",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e6,
    'FL',
    "posterior shift",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x000900e6,
    'SH',
    "Genesis Version Now",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900e6,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e7,
    'FL',
    "superior shift",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x000900e7,
    'UL',
    "Exam Record Checksum",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e8,
    'SL',
    "acq_bin_num",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x000900e8,
    'UL',
    "Series Suite ID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900e9,
    'FL',
    "acq_bin_dur_percent",
    '1')
add_private_dict_entry(
    "GEMS_IDEN_01",
    0x000900e9,
    'SL',
    "Actual Series Data Time Stamp",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900e9,
    'UI',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900ea,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900eb,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x000900ec,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900ee,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900ef,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x000900F0,
    'CS',
    "Blackening Process Flag",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900f0,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x000900F1,
    'LO',
    "Processing Information Flag",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x000900f1,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900f1,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x000900f2,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900f2,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x000900f3,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900f3,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x000900f4,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x000900f5,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x000900f5,
    'LO',
    "PDM EFID Placeholder",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x000900f6,
    'LO',
    "PDM Data Object Type Extension",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x000900f7,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x000900f7,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x000900f8,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DZDICOM 4.3.0",
    0x000900f9,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900fa,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x000900fb,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900fb,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x000900fb,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "INSTRU_PRIVATE_IDENT_CODE",
    0x000D0000,
    'OB',
    "Image Xml Data",
    '1')
add_private_dict_entry(
    "SCANORA_PRIVATE_IDENT_CODE",
    0x000D0000,
    'OB',
    "Image Xml Data",
    '1')
add_private_dict_entry(
    "MEDCON",
    0x000d0002,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MEDCON",
    0x000d0007,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MEDCON",
    0x000d0063,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "IDEXX",
    0x00110000,
    'LO',
    "Breed Name",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00110000,
    'OB',
    "Hx Questionnaire",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00110000,
    'OB',
    "Hx Questionnaire",
    '1')
add_private_dict_entry(
    "IDEXX",
    0x00110001,
    'LO',
    "Species Name",
    '1')
add_private_dict_entry(
    "V1",
    0x00110001,
    'OB',
    "User Data",
    '1')
add_private_dict_entry(
    "DLX_PATNT_01",
    0x00110001,
    'LT',
    "Patient DOB",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00110001,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00110001,
    'LO',
    "Is Rapid Registration",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110001,
    'LT',
    "Encrypted Instance Creator ID",
    '1')
add_private_dict_entry(
    "MDDX",
    0x00110001,
    'UT',
    "AES Encrypted Values",
    '1')
add_private_dict_entry(
    "METAEMOTION GINKGO RETINAL",
    0x00110001,
    'LT',
    "KeyFile Indicator",
    '1')
add_private_dict_entry(
    "METAEMOTION GINKGO",
    0x00110001,
    'LT',
    "KeyFile Indicator",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x00110001,
    'ST',
    "Reprocessing Info",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00110001,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x00110001,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "V1",
    0x00110002,
    'DS',
    "Normalization Coefficient",
    '1')
add_private_dict_entry(
    "IDEXX",
    0x00110002,
    'PN',
    "Owner",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00110002,
    'LO',
    "Is Protected",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110002,
    'LT',
    "Encrypted SOP Instance UID",
    '1')
add_private_dict_entry(
    "MDDX",
    0x00110002,
    'LO',
    "Allup Version Details",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110002,
    'UC',
    "Strain Description",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x00110002,
    'CS',
    "Data Role Type",
    '1-n')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00110002,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x00110002,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "V1",
    0x00110003,
    'DS',
    "Receiving Gain",
    '1-n')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110003,
    'UI',
    "Processed Series UID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00110003,
    'IS',
    "Filmed Count",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110003,
    'LT',
    "Encrypted Accession Number",
    '1')
add_private_dict_entry(
    "MDDX",
    0x00110003,
    'LO',
    "Mask Id",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110003,
    'LO',
    "Strain Nomenclature",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00110003,
    'LO',
    "Patient UID",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x00110003,
    'ST',
    "Data Role Name",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x00110003,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "V1",
    0x00110004,
    'DS',
    "Mean Image Noise",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110004,
    'CS',
    "Acquisition Type",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00110004,
    'OB',
    "Application Data",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110004,
    'LT',
    "Encrypted Institution Name",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110004,
    'LO',
    "Strain Stock Number",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00110004,
    'LO',
    "Patient ID",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x00110004,
    'SL',
    "Rescan Name",
    '1')
add_private_dict_entry(
    "V1",
    0x00110005,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110005,
    'UI',
    "Acquisition UID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00110005,
    'LO',
    "Is Allow Cascade Save",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110005,
    'LT',
    "Encrypted Institution Address",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110005,
    'SQ',
    "Strain Source Registry Code Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x00110005,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "V1",
    0x00110006,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110006,
    'DS',
    "Image Dose",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00110006,
    'LO',
    "Is Allow Cascade Protect",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110006,
    'LT',
    "Encrypted Referring Physician's Name",
    '1')
add_private_dict_entry(
    "MEDISO-1",
    0x00110006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110006,
    'SQ',
    "Strain Stock Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x00110006,
    'ST',
    "Cardiac Type Name",
    '1')
add_private_dict_entry(
    "V1",
    0x00110007,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110007,
    'FL',
    "Study Dose",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00110007,
    'LO',
    "Is Deleted",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110007,
    'LT',
    "Encrypted Referring Physician's Address",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110007,
    'LO',
    "Strain Source",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x00110007,
    'ST',
    "Cardiac Type Name L2",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110008,
    'FL',
    "Study DAP",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110008,
    'LT',
    "Encrypted Station Name",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110008,
    'UT',
    "Strain Additional Information",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x00110008,
    'ST',
    "Misc Indicator",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x00110008,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110009,
    'SL',
    "Non-Digital Exposures",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110009,
    'LT',
    "Encrypted Study Description",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x00110009,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x0011000A,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011000a,
    'SL',
    "Series Type",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x0011000a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x0011000a,
    'LO',
    "Case ID",
    '1')
add_private_dict_entry(
    "METAEMOTION GINKGO RETINAL",
    0x0011000B,
    'LT',
    "Serialized Diagnose and Markers",
    '1')
add_private_dict_entry(
    "METAEMOTION GINKGO",
    0x0011000B,
    'LT',
    "Serialized Diagnose and Markers",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x0011000B,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011000b,
    'SL',
    "Effective Series Duration",
    '1')
add_private_dict_entry(
    "METAEMOTION GINKGO RETINAL",
    0x0011000C,
    'UN',
    "Virtual Aneritra Contrast Image",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x0011000C,
    'ST',
    "Split Bagging Name",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011000c,
    'SL',
    "Num Beats",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x0011000D,
    'ST',
    "Split Sub Bagging Name",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011000d,
    'LO',
    "Radio Nuclide Name",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x0011000E,
    'ST',
    "Stage Sub Bagging Name",
    '1')
add_private_dict_entry(
    "SIEMENS MR DATAMAPPING ATTRIBUTES",
    0x0011000F,
    'ST',
    "Is Internal Data Role",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00110010,
    'LT',
    "Patient Entry ID",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110010,
    'LO',
    "Dataset Object Name",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110010,
    'SL',
    "Total Exposures",
    '1')
add_private_dict_entry(
    "GEMS_PATI_01",
    0x00110010,
    'SS',
    "Patient Status",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110010,
    'LT',
    "Encrypted Series Description",
    '1')
add_private_dict_entry(
    "SPI RELEASE 1",
    0x00110010,
    'LO',
    "Organ",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00110010,
    'LO',
    "Organ",
    '1')
add_private_dict_entry(
    "SPI",
    0x00110010,
    'LO',
    "Organ",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00110010,
    'DA',
    "Registration Date",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00110010,
    'LO',
    "Patient UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00110010,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x00110010,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00110011,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110011,
    'LT',
    "ROI",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110011,
    'SL',
    "Dataset Modified",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110011,
    'LT',
    "Encrypted Institutional Department Name",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00110011,
    'TM',
    "Registration Time",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00110011,
    'LO',
    "Patient ID",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x00110011,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110012,
    'LO',
    "Dataset Name",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110012,
    'LT',
    "Patient Size String",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110012,
    'LT',
    "Encrypted Physicians of Record",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x00110012,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110013,
    'SL',
    "Dataset Type",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110013,
    'UI',
    "SPS UID",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110013,
    'LT',
    "Encrypted Performing Physician's Name",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110014,
    'LO',
    "Completion Time",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110014,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110014,
    'LT',
    "Encrypted Name of Physicians Reading Study",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110015,
    'DS',
    "Detector ARC Gain",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110015,
    'SL',
    "Detector Number",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110015,
    'LT',
    "Encrypted Operator's Name",
    '1')
add_private_dict_entry(
    "SPI RELEASE 1",
    0x00110015,
    'LO',
    "Allergy Indication",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00110015,
    'LO',
    "Allergy Indication",
    '1')
add_private_dict_entry(
    "SPI",
    0x00110015,
    'LO',
    "Allergy Indication",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110016,
    'LT',
    "Processing Debug Info",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110016,
    'SL',
    "Energy Number",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110016,
    'LT',
    "Encrypted Admitting Diagnoses Description",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110017,
    'CS',
    "Override Mode",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110017,
    'SL',
    "RR Interval Window Number",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110017,
    'LT',
    "Encrypted Referenced SOP Instance UID",
    '1')
add_private_dict_entry(
    "SPI-P Release 2;1",
    0x00110018,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00110018,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110018,
    'SL',
    "MG Bin Number",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110018,
    'LT',
    "Encrypted Derivation Description",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x00110018,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110019,
    'DS',
    "Film Speed Selection",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110019,
    'FD',
    "Radius Of Rotation",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110019,
    'LT',
    "Encrypted Patient's Name",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x00110019,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011001a,
    'SL',
    "Detector Count Zone",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x0011001a,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011001b,
    'SL',
    "Num Energy Windows",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x0011001b,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011001c,
    'SL',
    "Energy Offset",
    '4')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x0011001c,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011001d,
    'SL',
    "Energy Range",
    '1')
add_private_dict_entry(
    "ULTRAVISUAL_TAG_SET1",
    0x0011001d,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011001e,
    'SL',
    "Energy Width (Retired)",
    '4')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011001f,
    'SL',
    "Image Orientation",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00110020,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "AgilityRuntime",
    0x00110020,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110020,
    'LT',
    "Encrypted Patient's ID",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110020,
    'SQ',
    "Strain Code Sequence",
    '1')
add_private_dict_entry(
    "SPI RELEASE 1",
    0x00110020,
    'LO',
    "Pregnancy",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00110020,
    'LO',
    "Pregnancy",
    '1')
add_private_dict_entry(
    "SPI",
    0x00110020,
    'LO',
    "Pregnancy",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00110020,
    'DA',
    "Patient Registration Date",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00110020,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x00110020,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00110021,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "AgilityRuntime",
    0x00110021,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110021,
    'DS',
    "Acq Zoom (Retired)",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110021,
    'LT',
    "Encrypted Patient's Birth Date",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00110021,
    'TM',
    "Patient Registration Time",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00110022,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "AgilityRuntime",
    0x00110022,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110022,
    'DS',
    "Acq Pan (Retired)",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110022,
    'LT',
    "Encrypted Patient's Birth Time",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00110022,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00110022,
    'LO',
    "Request ID",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110023,
    'ST',
    "CAD File Format",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110023,
    'SL',
    "Use FOV Mask",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110023,
    'LT',
    "Encrypted Patient's Sex",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00110023,
    'DS',
    "Used Patient Weight",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00110023,
    'LO',
    "Examination UID",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110024,
    'ST',
    "Component Reference System",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110024,
    'SL',
    "FOV Mask Y Cutoff Angle",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110024,
    'LT',
    "Encrypted Other Patient IDs",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x00110024,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110025,
    'ST',
    "Component Manufacturing Procedure",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110025,
    'SL',
    "FOV Mask Cutoff Angle",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110025,
    'LT',
    "Encrypted Other Patient Names",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00110025,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110026,
    'SL',
    "Table Orientation",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110026,
    'LT',
    "Encrypted Patient's Age",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00110026,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110027,
    'SL',
    "ROI Top Left",
    '2')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110027,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110027,
    'LT',
    "Encrypted Patient's Size",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110028,
    'ST',
    "Component Manufacturer",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110028,
    'SL',
    "ROI Bottom Right",
    '2')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110028,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110028,
    'LT',
    "Encrypted Patient's Weight",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00110028,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00110028,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110029,
    'SL',
    "Uniformity Mean",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110029,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110029,
    'LT',
    "Encrypted Medical Record Locator",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00110029,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00110029,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011002a,
    'FD',
    "Phase Duration (Retired)",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0011002a,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0011002a,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0011002b,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0011002b,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011002c,
    'FD',
    "View X Adjustment",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0011002c,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0011002c,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011002d,
    'FD',
    "View Y Adjustment",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011002e,
    'SL',
    "Pixel Overflow Flag",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011002f,
    'SL',
    "Overflow Level",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00110030,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110030,
    'DS',
    "Material Thickness",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110030,
    'LO',
    "Picture Object Name",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110030,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110030,
    'LT',
    "Encrypted Ethnic Group",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x00110030,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00110030,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00110030,
    'PN',
    "Patientname RIS",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00110031,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110031,
    'IS',
    "Detected Field of View",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110031,
    'LO',
    "Acquisition Parent UID",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110031,
    'LT',
    "Encrypted Occupation",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00110031,
    'LO',
    "Patientprename RIS",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x00110031,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00110032,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110032,
    'DS',
    "Material Pipe Diameter",
    '1-n')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110032,
    'IS',
    "Adjusted Field of View",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110032,
    'LO',
    "Processing Parent UID",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110032,
    'LT',
    "Encrypted Additional Patient's History",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x00110032,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110033,
    'DS',
    "Detector Exposure Index",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110033,
    'LO',
    "Energy Correct Name",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110033,
    'LT',
    "Encrypted Patient Comments",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110034,
    'DS',
    "Material Isolation Diameter",
    '1-n')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110034,
    'DS',
    "Compensated Detector Exposure",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110034,
    'LO',
    "Spatial Correct Name",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110034,
    'LT',
    "Encrypted Device Serial Number",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110035,
    'DS',
    "Uncompensated Detector Exposure",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110035,
    'LO',
    "Tuning Calib Name",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110035,
    'LT',
    "Encrypted Protocol Name",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00110035,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110036,
    'DS',
    "Median Anatomy Count Value",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110036,
    'LO',
    "Uniformity Correct Name",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110036,
    'LT',
    "Encrypted Study Instance UID",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110037,
    'DS',
    "DEI Lower & Upper Limit Values",
    '2')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110037,
    'LT',
    "Acquisition Specific Correct Name",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110037,
    'LT',
    "Encrypted Series Instance UID",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110038,
    'SL',
    "Byte Order",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110038,
    'SL',
    "Shift Vector for Pasting",
    '6')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110038,
    'LT',
    "Encrypted Study ID",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110039,
    'CS',
    "Image Number in Pasting",
    '6')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110039,
    'SL',
    "Compression Type",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110039,
    'LT',
    "Encrypted Frame of Reference UID",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x00110039,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011003a,
    'SL',
    "Picture Format",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x0011003a,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011003b,
    'FD',
    "Pixel Scale",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011003c,
    'FD',
    "Pixel Offset",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011003d,
    'SL',
    "Energy Peak (Retired)",
    '4')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011003e,
    'SL',
    "FOV Shape",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011003f,
    'SL',
    "Dataset Flags",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110040,
    'LO',
    "Viewing Object Name",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110040,
    'SL',
    "Pasting Overlap",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110040,
    'LT',
    "Encrypted Synchronization Frame of Reference UID",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00110040,
    'IS',
    "Organ Code",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00110040,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00110040,
    'LO',
    "Patient Hospital Status",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110041,
    'IS',
    "Sub-image Collimator Vertices",
    '24')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110041,
    'SL',
    "Orientation Angle",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110041,
    'LT',
    "Encrypted Image Comments",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00110041,
    'LO',
    "Medical Alerts",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110042,
    'ST',
    "Material Grade",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110042,
    'FD',
    "Rotation Angle",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110042,
    'LO',
    "View IP",
    '1')
add_private_dict_entry(
    "Hipaa Private Creator",
    0x00110042,
    'LT',
    "Encrypted UID",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00110042,
    'LO',
    "Contrast Allergies",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110043,
    'IS',
    "Keystone Coordinates",
    '24')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110043,
    'SL',
    "Window Inverse Flag",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110044,
    'ST',
    "Material Properties File ID",
    '1-n')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110044,
    'CS',
    "Receptor Type",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110044,
    'FD',
    "Threshold Center",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110045,
    'ST',
    "Material Properties File Format",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110045,
    'FD',
    "Threshold Width",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110046,
    'LT',
    "Material Notes",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110046,
    'LO',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110046,
    'SL',
    "Interpolation Type",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110047,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110050,
    'CS',
    "Component Shape",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110050,
    'LO',
    "Where Object Name",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110050,
    'LO',
    "Cell Line Designation",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110051,
    'SQ',
    "Cell Line Tissue of Origin Code Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110052,
    'CS',
    "Curvature Type",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110052,
    'SQ',
    "Cell Line Histologic Type Code Sequence",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110053,
    'SQ',
    "Cell Line Species of Origin Code Sequence",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110054,
    'DS',
    "Outer Diameter",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110054,
    'UL',
    "Cell Line Number of Passages",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110055,
    'FD',
    "Period",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/Component",
    0x00110056,
    'DS',
    "Inner Diameter",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110056,
    'FD',
    "ElapsedTime",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110057,
    'FD',
    "FOV",
    '2')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110059,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x00110060,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110061,
    'SL',
    "Image Size",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110062,
    'FD',
    "Linear FOV",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110063,
    'FD',
    "Spatial Offset",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110064,
    'FD',
    "Spatial Orientation",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110065,
    'LO',
    "Reference Dataset UID",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110066,
    'SH',
    "Starcam Reference Dataset",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110067,
    'SL',
    "Reference Frame Number",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110068,
    'SL',
    "Cursor Length",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110069,
    'SL',
    "Number of Cursors",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011006a,
    'SL',
    "Cursor Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011006b,
    'SL',
    "Recon Options Flag",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011006c,
    'FD',
    "Motion Threshold",
    '1')
add_private_dict_entry(
    "GEMS_GDXE_FALCON_04",
    0x0011006d,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011006d,
    'UI',
    "Motion Curve UID",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011006e,
    'SL',
    "Recon Type",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011006f,
    'SL',
    "Pre Filter Type",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110071,
    'SL',
    "Back Proj Filter Type",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110071,
    'SQ',
    "Source Patient Group Identification Sequence",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110072,
    'SL',
    "Recon Arc",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110072,
    'SQ',
    "Group of Patients Identification Sequence",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110073,
    'FD',
    "Recon Pan AP Offset",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00110073,
    'US',
    "Subject Relative Position in Image",
    '3')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110074,
    'FD',
    "Recon Pan LR Offset",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110075,
    'FD',
    "Recon Area",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110076,
    'SL',
    "Start View",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110077,
    'SL',
    "Attenuation Type",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110078,
    'SL',
    "Dua lEnergy Processing",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110079,
    'SH',
    "Pre Filter Param",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011007a,
    'SH',
    "Pre Filter Param 2",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011007b,
    'SH',
    "Back Proj Filter Param",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011007c,
    'SH',
    "Back Proj Filter Param 2",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011007d,
    'SH',
    "Attenuation Coef",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011007e,
    'SL',
    "Ref Slice Width",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011007f,
    'FD',
    "Ref Trans Pixel Volume",
    '1')
add_private_dict_entry(
    "GEMS_DL_PATNT_01",
    0x00110080,
    'UI',
    "Patient Instance Uid",
    '1')
add_private_dict_entry(
    "GEMS_DL_PATNT_01",
    0x00110081,
    'IS',
    "Last Study Number",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110081,
    'SH',
    "Attenuation Threshold",
    '1')
add_private_dict_entry(
    "GEMS_DL_PATNT_01",
    0x00110082,
    'CS',
    "Patient Repaired",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110082,
    'FD',
    "Interpolation Distance",
    '1')
add_private_dict_entry(
    "GEMS_DL_PATNT_01",
    0x00110083,
    'CS',
    "Lock Demographics",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110083,
    'FD',
    "Interpolation Center X",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110084,
    'FD',
    "Interpolation Center Y",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110085,
    'SL',
    "Quant Filter Flag",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110086,
    'SL',
    "Head Conversion",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110087,
    'SL',
    "Slice Width Pixels",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110088,
    'SL',
    "Rfmtr Trans Ref",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00110089,
    'FD',
    "Rfmtr Trans Ref mm",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011008a,
    'SL',
    "Two Line Trans Ref",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011008b,
    'SL',
    "Three-D Zero",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011008c,
    'SL',
    "Three-D Zero Length",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0011008d,
    'SL',
    "Three-D Zero In",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x001100a1,
    'DA',
    "Patient Registration Date",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x001100a2,
    'TM',
    "Patient Registration Time",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x001100b0,
    'LO',
    "Patient Last Name",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x001100b2,
    'LO',
    "Patient First Name",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x001100b4,
    'LO',
    "Patient Hospital Status",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x001100bc,
    'TM',
    "Current Location Time",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x001100c0,
    'LO',
    "Patient Insurance Status",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x001100d0,
    'LO',
    "Patient Billing Type",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x001100d0,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x001100d2,
    'LO',
    "Patient Billing Address",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x001100e0,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x001100e1,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x001100e2,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x001100e3,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x001100e4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x001100e5,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00130000,
    'LO',
    "IVA Results Flag",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00130000,
    'LO',
    "IVA Results Flag",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130000,
    'PN',
    "Modifying Physician",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00130001,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130010,
    'FD',
    "Digital FOV",
    '2')
add_private_dict_entry(
    "CTP",
    0x00130010,
    'LO',
    "Project Name",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130010,
    'DA',
    "Modification Date",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130011,
    'SL',
    "Source Translator",
    '1')
add_private_dict_entry(
    "CTP",
    0x00130011,
    'LO',
    "Trial Name",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130012,
    'SL',
    "RAL Flags",
    '1')
add_private_dict_entry(
    "CTP",
    0x00130012,
    'LO',
    "Site Name",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130012,
    'TM',
    "Modification Time",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130013,
    'SQ',
    "eNTEGRA Frame Sequence",
    '1')
add_private_dict_entry(
    "CTP",
    0x00130013,
    'LO',
    "Site ID",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130014,
    'SL',
    "Original Image Number",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130015,
    'FD',
    "Fscalar",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130016,
    'SL',
    "AutoTrack Peak",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130017,
    'SL',
    "AutoTrack Width",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130018,
    'FD',
    "Transmission Scan Time",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130019,
    'FD',
    "Transmission Mask Width",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0013001a,
    'FD',
    "Copper Attenuator Thickness",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0013001b,
    'FD',
    "Det Ang Separation",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0013001c,
    'SL',
    "Axial Acceptance Angle",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0013001d,
    'SL',
    "Theta Acceptance Value",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0013001e,
    'FD',
    "Tomo View Offset",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130020,
    'FD',
    "Accepted Beats Time",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130020,
    'PN',
    "Patient Name",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130021,
    'FD',
    "Threshold",
    '2')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130022,
    'FD',
    "Linear Depth",
    '2')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130022,
    'LO',
    "Patient Id",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130023,
    'LO',
    "Unif Date Time",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130024,
    'SL',
    "Series Accepted Beats",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130025,
    'SL',
    "Series Rejected Beats",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00130026,
    'LT',
    "Study Comments",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130030,
    'DA',
    "Patient Birthdate",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130031,
    'DS',
    "Patient Weight",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130032,
    'LO',
    "Patients Maiden Name",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130033,
    'LO',
    "Referring Physician",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130034,
    'LO',
    "Admitting Diagnosis",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130035,
    'LO',
    "Patient Sex",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130040,
    'LO',
    "Procedure Description",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130042,
    'LO',
    "Patient Rest Direction",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130044,
    'LO',
    "Patient Position",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130046,
    'LO',
    "View Direction",
    '1')
add_private_dict_entry(
    "CTP",
    0x00130050,
    'LO',
    "Study Year",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130050,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130051,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130052,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130053,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130054,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130055,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00130056,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ESOFT_DICOM_ECAT_OWNERCODE",
    0x00150000,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "DLX_EXAMS_01",
    0x00150001,
    'DS',
    "Stenosis Calibration Ratio",
    '1')
add_private_dict_entry(
    "DLX_EXAMS_01",
    0x00150002,
    'DS',
    "Stenosis Magnification",
    '1')
add_private_dict_entry(
    "DLX_EXAMS_01",
    0x00150003,
    'DS',
    "Cardiac Calibration Ratio",
    '1')
add_private_dict_entry(
    "INFINITT_FMX",
    0x00150010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00150010,
    'SL',
    "Frame Termination Condition",
    '1')
add_private_dict_entry(
    "INFINITT_FMX",
    0x00150011,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00150011,
    'SL',
    "Frame Termination Value",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00150012,
    'SL',
    "Num ECT Phases",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00150013,
    'SL',
    "Num WB Scans",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00150014,
    'SL',
    "ECT Phase Num",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00150015,
    'SL',
    "WB Scan Num",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00150016,
    'SL',
    "Comb Head Number",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00150017,
    'UL',
    "Preceding Beat",
    '1')
add_private_dict_entry(
    "MATAKINA_10",
    0x00150028,
    'LO',
    "Volpara Density Grade",
    '1')
add_private_dict_entry(
    "MATAKINA_10",
    0x00150029,
    'LT',
    "Volpara Run Information",
    '1')
add_private_dict_entry(
    "MATAKINA_10",
    0x00150030,
    'LO',
    "Volpara Density Grade Cutoffs",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150080,
    'DS',
    "Study Dose",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150081,
    'DS',
    "Study Total Dap",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150082,
    'DS',
    "Fluoro Dose Area Product",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150083,
    'IS',
    "Study Fluoro Time",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150084,
    'DS',
    "Cine Dose Area Product",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150085,
    'IS',
    "Study Record Time",
    '1')
add_private_dict_entry(
    "GEMS_DL_SERIES_01",
    0x00150085,
    'LO',
    "Series File Name",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150086,
    'IS',
    "Last XA Number",
    '1')
add_private_dict_entry(
    "GEMS_DL_SERIES_01",
    0x00150087,
    'IS',
    "Number of Images",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150088,
    'PN',
    "Def Operator Name",
    '1-n')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150089,
    'PN',
    "Def Performing Physician Name",
    '1-n')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x0015008A,
    'CS',
    "Def Patient Orientation",
    '2')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x0015008B,
    'IS',
    "Last Sc Number",
    '1')
add_private_dict_entry(
    "GEMS_DL_SERIES_01",
    0x0015008C,
    'CS',
    "Sent Flag",
    '1')
add_private_dict_entry(
    "GEMS_DL_SERIES_01",
    0x0015008D,
    'US',
    "Item Locked",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x0015008E,
    'UI',
    "Common Series Instance UID",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x0015008F,
    'IS',
    "Study Number",
    '1')
add_private_dict_entry(
    "DL_INTERNAL_USE",
    0x0015008f,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150092,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150093,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150094,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150095,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150096,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150097,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150098,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x00150099,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x0015009a,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x0015009b,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x0015009c,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_STUDY_01",
    0x0015009d,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Version",
    0x00170000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00170000,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00170000,
    'LO',
    "Extended Body Part",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00170001,
    'UI',
    "correction_cal_id",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Version",
    0x00170001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00170002,
    'SH',
    "compatible_version",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00170003,
    'SH',
    "software_version",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00170004,
    'DT',
    "cal_datetime",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00170005,
    'LO',
    "cal_datetime",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00170006,
    'SL',
    "cal_type",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00170007,
    'ST',
    "where_is_corr",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00170008,
    'SL',
    "corr_file_size",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00170009,
    'LO',
    "scan_id",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0017000a,
    'DT',
    "scan_datetime",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017000a,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0017000b,
    'LO',
    "norm_2d_cal_id",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017000b,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0017000c,
    'SH',
    "hosp_identifier",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017000c,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0017000d,
    'SL',
    "archived",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017000d,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017000e,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017000f,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170010,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00170010,
    'LO',
    "Extended View Position",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170011,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170011,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170011,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170012,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170012,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170014,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170014,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170014,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170015,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170015,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170016,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170016,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170017,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170018,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170018,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170019,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017001a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017001b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017001c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017001e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017001f,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170020,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00170020,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00170020,
    'SQ',
    "Scheduled Procedure Step List",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170021,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170021,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170022,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170022,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170023,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170023,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170024,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170024,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170025,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170025,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170025,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170026,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170026,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170027,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170027,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170027,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170028,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170029,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170029,
    'IS',
    "Edge Enhancement %",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x0017002a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170030,
    'IS',
    "Harmonization %",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170030,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170031,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170031,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170032,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170032,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170033,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170033,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170035,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170037,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170037,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170038,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170038,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170041,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170043,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170044,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170045,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170046,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170047,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170048,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170048,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170049,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170049,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x0017004a,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017004d,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017004e,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017004f,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170050,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170051,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170051,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170052,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170052,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170053,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170054,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170055,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017005c,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170061,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170062,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170064,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170066,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170067,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170068,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00170070,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170071,
    'IS',
    "Landmark",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170071,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170072,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170072,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170073,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170073,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170074,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170074,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170077,
    'DS',
    "Pixel Shift horizontal",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170078,
    'DS',
    "Pixel Shift vertical",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170079,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x00170079,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x0017007a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x0017007a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x0017007b,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00170080,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170080,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170083,
    'LO',
    "Left Marker",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x00170084,
    'LO',
    "Right Marker",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170085,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170086,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170087,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170088,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x00170089,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017008a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017008b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017008c,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017008d,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017008e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x0017008f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x001700a0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700a0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x001700a0,
    'IS',
    "Fixed Grid System",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x001700a1,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700a1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700a2,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x001700a2,
    'SH',
    "Image Name Extension 1",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 MANIPULATED",
    0x001700a3,
    'SH',
    "Image Name Extension 2",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700a3,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700a4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700a5,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700a6,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700aa,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700b0,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS_FLCOMPACT_VA01A_PROC",
    0x001700c0,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x001700c1,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DFR.01 ORIGINAL",
    0x001700c2,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x001700f0,
    'IS',
    "Images SOP Class",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00190000,
    'CS',
    "Image Blanking Shape",
    '1')
add_private_dict_entry(
    "PHILIPS MR R5.5/PART",
    0x00190000,
    'DS',
    "Field of View",
    '1')
add_private_dict_entry(
    "PHILIPS MR R5.6/PART",
    0x00190000,
    'DS',
    "Field of View",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190000,
    'DS',
    "Field of View",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART 7",
    0x00190000,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190000,
    'IS',
    "Number of Stacks",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x00190000,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DiDi Release 1",
    0x00190000,
    'LT',
    "Post Mode String",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190000,
    'UN',
    "Physiological Data Type",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00190000,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "AEGIS_DICOM_2.00",
    0x00190000,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190000,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SET WINDOW",
    0x00190000,
    'SH',
    "Set Window Image Filter",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00190000,
    'UT',
    "Report Data",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00190000,
    'UT',
    "Report Data",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0019",
    0x00190000,
    'FD',
    "Calibration",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00190000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190000,
    'US',
    "Review Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190000,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190000,
    'SH',
    "Private Creator Version",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190000,
    'IS',
    "AEC Field",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190001,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190001,
    'IS',
    "Stack Type",
    '1-n')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DiDi Release 1",
    0x00190001,
    'LT',
    "Post Data",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190001,
    'UN',
    "Physiological Data Channel And Kind",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190001,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190001,
    'DS',
    "Angle Value L Arm",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190001,
    'UI',
    "wc_cal_id",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190001,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190001,
    'LO',
    "Proc Type",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190001,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SET WINDOW",
    0x00190001,
    'US',
    "Set Window Magnification Power",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190001,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "LODOX_STATSCAN",
    0x00190001,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "MeVis BreastCare",
    0x00190001,
    'LO',
    "Annotation Version",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0019",
    0x00190001,
    'FD',
    "Depth Conversion",
    '1')
add_private_dict_entry(
    "SIEMENS SIENET",
    0x00190001,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00190001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190001,
    'US',
    "Anatomical Background Percent",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00190001,
    'UL',
    "AEC Coordinates",
    '1-n')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00190001,
    'FD',
    "Focus Depth(s)",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190001,
    'IS',
    "AEC Film Screen",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x00190001,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00190001,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190002,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00190002,
    'IS',
    "Image Blanking Left Vertical Edge",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x00190002,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190002,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190002,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190002,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190002,
    'US',
    "Sample Bits Allocated",
    '1')
add_private_dict_entry(
    "ADAC_IMG",
    0x00190002,
    'IS',
    "ADAC Pegasys File Size",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190002,
    'DS',
    "Angle Value P Arm",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190002,
    'SH',
    "compatible_version",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190002,
    'SL',
    "Number Of Cells In Detector",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190002,
    'LO',
    "Plane",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190002,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190002,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190002,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "LODOX_STATSCAN",
    0x00190002,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190002,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0019",
    0x00190002,
    'FD',
    "Stepsize",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00190002,
    'LO',
    "Total Dose Area Product uGy*cm*cm",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190002,
    'US',
    "Number of Phases",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00190002,
    'US',
    "AEC Coordinates Size",
    '2')
add_private_dict_entry(
    "SVISION",
    0x00190002,
    'IS',
    "AEC Density",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x00190002,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00190002,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190003,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x00190003,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190003,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190003,
    'US',
    "Sample Bits Stored",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190003,
    'DS',
    "Cell Number At Theta",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190003,
    'DS',
    "Angle Value C Arm",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190003,
    'SH',
    "software_version",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190003,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190003,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190003,
    'SH',
    "Is Snap Shot Series",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190003,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190003,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "LODOX_STATSCAN",
    0x00190003,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190003,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0019",
    0x00190003,
    'SL',
    "Warning",
    '1-n')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190003,
    'US',
    "Apply Anatomical Background",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00190003,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190003,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190003,
    'FD',
    "Frame Rate",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00190003,
    'SQ',
    "Excluded Intervals Sequence",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x00190003,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00190004,
    'IS',
    "Image Blanking Right Vertical Edge",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x00190004,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190004,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190004,
    'US',
    "Sample High Bit",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190004,
    'CS',
    "Angle Label L Arm",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190004,
    'DS',
    "Cell Spacing",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190004,
    'DT',
    "cal_datetime",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190004,
    'DS',
    "Max Fscalor",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190004,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190004,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190004,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "LODOX_STATSCAN",
    0x00190004,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190004,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0019",
    0x00190004,
    'ST',
    "DataID",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00190004,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190004,
    'SS',
    "Pixel Shift Array",
    '4-n')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00190004,
    'DT',
    "Exclusion Start Datetime",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x00190004,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190005,
    'DS',
    "CC Angulation",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x00190005,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190005,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190005,
    'US',
    "Sample Representation",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190005,
    'ST',
    "Cassette Data Stream",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190005,
    'CS',
    "Angle Label P Arm",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190005,
    'SL',
    "cal_type",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190005,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190005,
    'LO',
    "Series Category Type",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190005,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190005,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "LODOX_STATSCAN",
    0x00190005,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190005,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190005,
    'US',
    "Brightness",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00190005,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00190005,
    'FD',
    "Exclusion Duration",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x00190005,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190006,
    'DS',
    "AP Angulation",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00190006,
    'IS',
    "Image Blanking Upper Horizontal Edge",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190006,
    'UN',
    "Smallest Sample Value",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190006,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190006,
    'CS',
    "Angle Label C Arm",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190006,
    'LO',
    "cal_description",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190006,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190006,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190006,
    'LO',
    "Paddle ID",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190006,
    'LO',
    "Paddle ID",
    '1')
add_private_dict_entry(
    "LODOX_STATSCAN",
    0x00190006,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190006,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00190006,
    'FD',
    "Table Object Distance",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190006,
    'US',
    "Contrast",
    '1')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190006,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00190006,
    'SQ',
    "US Image Description Sequence",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x00190006,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190007,
    'DS',
    "LR Angulation",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190007,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190007,
    'UN',
    "Largest Sample Value",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x00190007,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190007,
    'LO',
    "cal_hardware",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190007,
    'ST',
    "Procedure Name",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190007,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190007,
    'LO',
    "Image Contrast Bolus Agent",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190007,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190007,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190007,
    'SH',
    "Paddle Position",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190007,
    'SH',
    "Paddle Position",
    '1')
add_private_dict_entry(
    "LODOX_STATSCAN",
    0x00190007,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190007,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00190007,
    'FD',
    "Table Detector Distance",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190007,
    'US',
    "Enabled Shutters",
    '1')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190007,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00190007,
    'SQ',
    "Image Data Type Sequence",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x00190007,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00190008,
    'IS',
    "Image Blanking Lower Horizontal Edge",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190008,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190008,
    'IS',
    "Patient Orientation 1",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190008,
    'IS',
    "Patient Position",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190008,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190008,
    'UN',
    "Number Of Samples",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190008,
    'OB',
    "coefficients",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190008,
    'ST',
    "Exam Name",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190008,
    'DS',
    "Image Slice Thickness",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190008,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190008,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190008,
    'LO',
    "Collimation Size",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190008,
    'LO',
    "Collimation Size",
    '1')
add_private_dict_entry(
    "LODOX_STATSCAN",
    0x00190008,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190008,
    'US',
    "Native Edge Enhancement Percent Gain",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00190008,
    'US',
    "Ortho Step Distance",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190008,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190008,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00190008,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00190008,
    'CS',
    "Data Type",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x00190008,
    'LT',
    "Orientation Head Feet",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00190009,
    'DS',
    "Main Magnetic Field",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190009,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190009,
    'IS',
    "Patient Orientation",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190009,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190009,
    'UN',
    "Sample Data",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x00190009,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190009,
    'FL',
    "activity_factor_hr",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190009,
    'SH',
    "Patient Size",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190009,
    'DS',
    "Image Reconstruction Diameter",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190009,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190009,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190009,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190009,
    'SS',
    "Native Edge Enhancement LUT Index",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190009,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00190009,
    'SQ',
    "Transducer Scan Geometry Code Sequence",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x00190009,
    'LT',
    "View Direction",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x0019000A,
    'IS',
    "Record View",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019000A,
    'SS',
    "Native Edge Enhancement Kernel Size",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0019000A,
    'US',
    "Number of Images in Mosaic",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019000a,
    'IS',
    "Slice Orientation",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x0019000a,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x0019000a,
    'UN',
    "Sample Rate",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0019000a,
    'FL',
    "activity_factor_hs",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019000a,
    'LO',
    "Image Echo Time",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x0019000a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019000a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x0019000a,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x0019000a,
    'LT',
    "Orientation Supine Prone",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019000B,
    'DS',
    "FOV Dimension Double",
    '1-2')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019000B,
    'US',
    "Subtracted Edge Enhancement Percent Gain",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0019000B,
    'DS',
    "Slice Measurement Duration",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0019000B,
    'CS',
    "Aliased Data Type",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019000b,
    'DS',
    "LR Offcenter",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019000b,
    'DS',
    "LR Offcenter",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x0019000b,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0019000b,
    'FL',
    "activity_factor_3d",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019000b,
    'DS',
    "Image Repetition Time",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019000b,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019000b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x0019000b,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x0019000b,
    'DS',
    "Location",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019000C,
    'SS',
    "Subtracted Edge Enhancement LUT Index",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0019000C,
    'IS',
    "B Value",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019000C,
    'US',
    "Burned in Graphics",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0019000C,
    'CS',
    "Position Measuring Device Used",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019000c,
    'DS',
    "CC Offcenter",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019000c,
    'DS',
    "CC Offcenter",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x0019000c,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0019000c,
    'LO',
    "scan_id",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019000c,
    'LO',
    "Sequence Type",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019000c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x0019000c,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019000c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x0019000c,
    'CS',
    "Scan View Direction",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019000D,
    'SS',
    "Subtracted Edge Enhancement Kernel Size",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0019000D,
    'CS',
    "Diffusion Directionality",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019000D,
    'SH',
    "SieClear Index",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0019000D,
    'SQ',
    "Transducer Scanning Configuration Code Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019000d,
    'DS',
    "AP Offcenter",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019000d,
    'DS',
    "AP Offcenter",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0019000d,
    'DT',
    "scan_datetime",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019000d,
    'LO',
    "Task UID",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019000d,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x0019000d,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019000d,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x0019000d,
    'TM',
    "Time",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019000E,
    'US',
    "Fade Percent",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0019000E,
    'FD',
    "Diffusion Gradient Direction",
    '3')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019000E,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0019000E,
    'SQ',
    "Transducer Beam Steering Code Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019000e,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x0019000e,
    'IS',
    "Flow Compensation",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0019000e,
    'SH',
    "hosp_identifier",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019000e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019000e,
    'OB',
    "Series App Data",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019000e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x0019000e,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019000e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_CT_1.0",
    0x0019000e,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019000F,
    'US',
    "Flipped Before Laterality Applied",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0019000F,
    'SL',
    "Siemens ICON Data Type",
    '1-n')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0019000F,
    'SQ',
    "Transducer Access Code Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019000f,
    'IS',
    "Number of Slices",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019000f,
    'DS',
    "Horizontal Frame Of Reference",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x0019000f,
    'FL',
    "meas_activity",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019000f,
    'IS',
    "Multi Slice Number",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019000f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x0019000f,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0019000f,
    'SH',
    "Gradient Mode",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190010,
    'DS',
    "Slice Factor",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00190010,
    'IS',
    "Center of Circular Image Blanking",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190010,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART 6",
    0x00190010,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DiDi Release 1",
    0x00190010,
    'LT',
    "Image Header",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-DCI Release 1",
    0x00190010,
    'LT',
    "Video Beam Boost",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190010,
    'UN',
    "Physiological Data Type 2",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DCI Release 1",
    0x00190010,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00190010,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190010,
    'US',
    "Mains Frequency",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x00190010,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190010,
    'ST',
    "Image Processing Parameters",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x00190010,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "1.2.840.113681",
    0x00190010,
    'ST',
    "CR Image Params Common",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190010,
    'DS',
    "Injector Delay",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190010,
    'DT',
    "meas_datetime",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190010,
    'LO',
    "Image Scan Time",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190010,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190010,
    'DS',
    "Source Side Collimator Aperture",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190010,
    'DS',
    "Total Measurement Time Nominal",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00190010,
    'IS',
    "Net Frequency",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190010,
    'IS',
    "Distance Source To Source Side Collimator",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190010,
    'US',
    "Apply Fade",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  ACQU",
    0x00190010,
    'LO',
    "Parameter File Name",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190010,
    'LO',
    "Measurement Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00190010,
    'ST',
    "Derivation Description",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190010,
    'IS',
    "Patient Thickness",
    '1')
add_private_dict_entry(
    "CureMetrix",
    0x00191000,
    'UT',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00191027,
    'DS',
    "Image chain FWHM psf mm min",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00191028,
    'DS',
    "Image chain FWHM psf mm max",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190011,
    'DS',
    "Echo Times",
    '1-n')
add_private_dict_entry(
    "PHILIPS-MR-1",
    0x00190011,
    'IS',
    "Chemical Shift Number",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190011,
    'UN',
    "Physiological Data Channel And Kind 2",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DCI Release 1",
    0x00190011,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00190011,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-DCI Release 1",
    0x00190011,
    'US',
    "Channel Generating Video Sync",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190011,
    'LO',
    "Identification Data",
    '1')
add_private_dict_entry(
    "1.2.840.113681",
    0x00190011,
    'ST',
    "CR Image IP Params Single",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190011,
    'CS',
    "Auto Inject",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190011,
    'SL',
    "axial_filter_3d",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190011,
    'SS',
    "Series Contrast",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190011,
    'LO',
    "Is Protected",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190011,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190011,
    'DS',
    "Detector Side Collimator Aperture",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190011,
    'DS',
    "Total Measurement Time Current",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190011,
    'IS',
    "Distance Source To Detector Side Collimator",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  ACQU",
    0x00190011,
    'LO',
    "Sequence File Name",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190011,
    'LO',
    "Image Type",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190011,
    'SH',
    "Flow Compensation",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190011,
    'US',
    "Reference Images Taken Flag",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00190012,
    'IS',
    "Radius of Circular Image Blanking",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190012,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS-MR-1",
    0x00190012,
    'IS',
    "Phase Number",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DCI Release 1",
    0x00190012,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00190012,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190012,
    'US',
    "Sample Bits Allocated 2",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-DCI Release 1",
    0x00190012,
    'US',
    "Video Gain",
    '1')
add_private_dict_entry(
    "1.2.840.113681",
    0x00190012,
    'ST',
    "CR Image IP Params Left",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190012,
    'FL',
    "axial_cutoff_3d",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190012,
    'SS',
    "Last Pseq",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190012,
    'IS',
    "Image Increment",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190012,
    'TM',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190012,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190012,
    'DS',
    "Magnetic Field Strength",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190012,
    'DS',
    "Start Delay Time",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190012,
    'US',
    "Zoom",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  ACQU",
    0x00190012,
    'LO',
    "Sequence File Owner",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190012,
    'SL',
    "Table Position Origin",
    '3')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190013,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DCI Release 1",
    0x00190013,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190013,
    'US',
    "Sample Bits Stored 2",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-DCI Release 1",
    0x00190013,
    'US',
    "Video Offset",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190013,
    'LO',
    "Sensitometry Name",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x00190013,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "1.2.840.113681",
    0x00190013,
    'ST',
    "CR Image IP Params Right",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190013,
    'SL',
    "default_flag",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190013,
    'SS',
    "Start Number For Baseline",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190013,
    'LO',
    "MPPS Step Status",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190013,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190013,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190013,
    'DS',
    "Dwell Time",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190013,
    'SS',
    "Pan X",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  ACQU",
    0x00190013,
    'LO',
    "Sequence Description",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190013,
    'SL',
    "Ima Abs Table Position",
    '3')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190014,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x00190014,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DCI Release 1",
    0x00190014,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190014,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190014,
    'US',
    "Sample High Bit 2",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190014,
    'ST',
    "Window Level List",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190014,
    'IS',
    "Acquisition Mode",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190014,
    'SL',
    "archived",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190014,
    'SS',
    "End Number For Baseline",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190014,
    'IS',
    "Storage Committed Count",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190014,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190014,
    'DS',
    "ADC Voltage",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190014,
    'IS',
    "Number of Phases",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190014,
    'SS',
    "Pan Y",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190014,
    'IS',
    "Ima Rel Table Position",
    '3')
add_private_dict_entry(
    "SIEMENS CM VA0  ACQU",
    0x00190014,
    'LO',
    "EPI File Name",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190015,
    'IS',
    "Dynamic Study",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DCI Release 1",
    0x00190015,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190015,
    'US',
    "Sample Representation 2",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190015,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "AGFA",
    0x00190015,
    'LO',
    "Dose Monitoring",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x00190015,
    'DS',
    "?",
    '2')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190015,
    'LO',
    "Kanji Body Part for Exposure",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190015,
    'CS',
    "Camera Rotation Enabled",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190015,
    'SL',
    "wc_cal_rec_method",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190015,
    'SS',
    "Start Number For Enhanced Scans",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190015,
    'IS',
    "Archived Count",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190015,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190015,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190015,
    'SS',
    "Native Edge Enhancement Adv Percent Gain",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190015,
    'FD',
    "Slice Position PCS",
    '3')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190015,
    'LO',
    "Software Version",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190015,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190015,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190016,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190016,
    'UN',
    "Smallest Sample Value 2",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DCI Release 1",
    0x00190016,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190016,
    'LO',
    "Other Info",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x00190016,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190016,
    'CS',
    "Reverse Sweep",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190016,
    'SL',
    "activity_factor_2d",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190016,
    'SS',
    "End Number For Enhanced Scans",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190016,
    'IS',
    "Transferred Count",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190016,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190016,
    'DS',
    "Paddle Angle",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190016,
    'DS',
    "Paddle Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190016,
    'DS',
    "ADC Offset",
    '2')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190016,
    'SS',
    "Subtracted Edge Enhancement Adv Percent Gain",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190016,
    'UL',
    "Sequence Control Mask",
    '2')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190016,
    'DS',
    "Time After Start",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00190016,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190016,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190017,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190017,
    'UN',
    "Largest Sample Value 2",
    '1')
add_private_dict_entry(
    "SPI-P-Private-DCI Release 1",
    0x00190017,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x00190017,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190017,
    'IS',
    "User Spatial Filter Strength",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00190017,
    'SL',
    "isotope",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190017,
    'SS',
    "Series Plane",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190017,
    'LO',
    "Is Allow Cascade Save",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190017,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190017,
    'US',
    "Invert Flag",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190017,
    'DS',
    "Slice Resolution",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190018,
    'DS',
    "Heartbeat Interval",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x00190018,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190018,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190018,
    'UN',
    "Number Of Samples 2",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x00190018,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190018,
    'IS',
    "User Zoom Factor",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190018,
    'LO',
    "First Scan RAS",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190018,
    'LO',
    "Is Allow Cascade Protect",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190018,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190018,
    'UL',
    "Measurement Status Mask",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190018,
    'IS',
    "Real Dwell Time",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190018,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190018,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190018,
    'IS',
    "Beam Distance",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190019,
    'DS',
    "Repetition Time FFE",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x00190019,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00190019,
    'UN',
    "Sample Data 2",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x00190019,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190019,
    'DS',
    "First Scan Location",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190019,
    'IS',
    "X Zoom Center",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00190019,
    'LO',
    "Is Deleted",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190019,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190019,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190019,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x0019001A,
    'IS',
    "Y Zoom Center",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019001A,
    'UI',
    "Characterized Image Instance UID",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019001A,
    'OB',
    "Quant 1K Overlay",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019001a,
    'DS',
    "FFE Flip Angle",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x0019001a,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x0019001a,
    'UN',
    "Sample Rate 2",
    '1')
add_private_dict_entry(
    "AGFA",
    0x0019001a,
    'LO',
    "Clipped Exposure Deviation",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x0019001a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019001a,
    'LO',
    "Last Scan RAS",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019001a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019001a,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019001a,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x0019001B,
    'DS',
    "Focus",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019001B,
    'IS',
    "Characterized Image Count",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019001B,
    'US',
    "Original Resolution",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019001b,
    'IS',
    "Number of Scans",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x0019001b,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x0019001b,
    'LO',
    "Logarithmic PLT Full Scale",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x0019001b,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019001b,
    'DS',
    "Last Scan Location",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019001b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019001b,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019001b,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x0019001C,
    'CS',
    "Dose",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019001C,
    'LO',
    "Internal Window Width",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019001C,
    'DS',
    "Auto Window Center",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019001c,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x0019001c,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x0019001c,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019001c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019001c,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019001c,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x0019001D,
    'IS',
    "Side Mark",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019001D,
    'LO',
    "Internal Window Level",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019001D,
    'DS',
    "Auto Window Width",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019001d,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE Release 1",
    0x0019001d,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019001d,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019001d,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019001d,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x0019001E,
    'IS',
    "Percentage Landscape",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0019001E,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019001E,
    'IS',
    "Auto Window Correct Value",
    '2')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019001e,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x0019001e,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019001e,
    'DS',
    "Display Field Of View",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019001e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x0019001e,
    'DS',
    "?",
    '3')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019001e,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019001e,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x0019001F,
    'DS',
    "Exposure Duration",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x0019001F,
    'DS',
    "Sigmoid Window Parameter",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x0019001f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019001f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x0019001f,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019001f,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019001f,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019001f,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-DCI Release 1",
    0x00190020,
    'DS',
    "RTD Data Compression Factor",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190020,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x00190020,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00190020,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190020,
    'TM',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190020,
    'LO',
    "Ip Address",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190020,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190020,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190020,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190020,
    'DS',
    "Transmitter Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190020,
    'IS',
    "Number of Possible Channels",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190020,
    'IS',
    "Exposure Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190020,
    'IS',
    "Number of Fourier Lines Nominal",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190020,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190020,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190020,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00190020,
    'CS',
    "Measurement Mode",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190020,
    'LO',
    "MPM Code",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190020,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190020,
    'SH',
    "B-Mode Submode",
    '1')
add_private_dict_entry(
    "Siemens Ultrasound Miscellaneous",
    0x00190020,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190020,
    'IS',
    "Workstation Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190021,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190021,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190021,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x00190021,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ADAC_IMG",
    0x00190021,
    'US',
    "Number of ADAC Headers",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x00190021,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Canon Inc.",
    0x00190021,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190021,
    'DS',
    "Table position Z (vertical) first frame",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190021,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190021,
    'IS',
    "Mean Channel Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190021,
    'IS',
    "Exposure Current",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190021,
    'IS',
    "Number of Transmitter Amplitudes",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190021,
    'IS',
    "Number of Fourier Lines Current",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190021,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190021,
    'FD',
    "B-Mode Dynamic Range",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190021,
    'LO',
    "Latitude",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190022,
    'DS',
    "Dynamic Scan Time Begin",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190022,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190022,
    'LO',
    "Route AET",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190022,
    'DS',
    "Table position X (longitudinal) first frame",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190022,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190022,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190022,
    'DS',
    "Detector Spacing",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190022,
    'DS',
    "Transmitter Attenuator",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190022,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190022,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190022,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190022,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190022,
    'FD',
    "B-Mode Overall Gain",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190022,
    'LO',
    "Sensitivity",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190023,
    'DS',
    "PCR Print Scale",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190023,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190023,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190023,
    'DS',
    "Table Speed [mm/rotation]",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190023,
    'DS',
    "Table position Y (lateral) first frame",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190023,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190023,
    'DS',
    "Detector Center",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190023,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190023,
    'LO',
    "EDR",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190023,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190023,
    'US',
    "B-Mode Resolution/Speed Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190024,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190024,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190024,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190024,
    'ST',
    "PCR Print Job End",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190024,
    'DS',
    "Mid Scan Time [sec]",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190024,
    'DS',
    "Lambda cm Pincushion Distortion",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190024,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190024,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190024,
    'DS',
    "Reading Integration Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190024,
    'DS',
    "Transmitter Calibration",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190024,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190024,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190024,
    'LO',
    "L Fix",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190024,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190024,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190024,
    'US',
    "B-Mode Edge Enhance Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190025,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190025,
    'IS',
    "PCR No Film Copies",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190025,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190025,
    'LO',
    "Original Pixel Data Quality",
    '1-n')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190025,
    'DS',
    "LV Regression Slope Coefficient",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190025,
    'SS',
    "Mid Scan Flag",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190025,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190025,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190025,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190025,
    'DS',
    "KVP Generator Power Current",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190025,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190025,
    'LO',
    "S Fix",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190025,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190025,
    'US',
    "B-Mode Persistence Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190026,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190026,
    'IS',
    "PCR Film Layout Position",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190026,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "DLX_SERIE_01",
    0x00190026,
    'DS',
    "LV Regression Intercept Coefficient",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190026,
    'SL',
    "Tube Azimuth [degrees]",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190026,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190026,
    'LO',
    "Paddle ID Description",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190026,
    'LO',
    "Paddle ID Description",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190026,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190026,
    'DS',
    "Generator Voltage",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190026,
    'DS',
    "Transmitter Reference",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190026,
    'IS',
    "Number of Fourier Lines after Zero",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190026,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190026,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190026,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190026,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190026,
    'LO',
    "Preset Mode",
    '1')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190026,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190026,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190026,
    'US',
    "B-Mode Map Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190027,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190027,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190027,
    'ST',
    "PCR Print Report Name",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190027,
    'DS',
    "Rotation Speed (Gantry Period)",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190027,
    'SH',
    "Paddle Position Description",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190027,
    'SH',
    "Paddle Position Description",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190027,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190027,
    'FD',
    "B Matrix",
    '6')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190027,
    'LO',
    "Region",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190027,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190027,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190028,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190028,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x00190028,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190028,
    'LO',
    "Collimation Size Description",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190028,
    'LO',
    "Collimation Size Description",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190028,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190028,
    'IS',
    "First Measured Fourier Line",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190028,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190028,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190028,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190028,
    'FD',
    "Bandwidth per Pixel Phase Encode",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190028,
    'LO',
    "Subregion",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190028,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190028,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190028,
    'IS',
    "Tube Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190029,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190029,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190029,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190029,
    'LO',
    "AEC User Density Scale Factor Description",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190029,
    'LO',
    "AEC User Density Scale Factor Description",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00190029,
    'FD',
    "Mosaic Ref Acq Times",
    '1-n')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190029,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190029,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190029,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019002A,
    'US',
    "B-Mode Tint Type",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019002a,
    'DS',
    "Xray On Position",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019002a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019002a,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019002a,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019002a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019002a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019002B,
    'FL',
    "Distance to table top",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019002b,
    'DS',
    "Xray Off Position",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019002b,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019002c,
    'SL',
    "Number of Triggers",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019002c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019002c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019002c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019002D,
    'US',
    "B-Mode Tint Index",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x0019002D,
    'US',
    "B-mode Tint Index",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019002d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019002d,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019002d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019002E,
    'SH',
    "ClarifyVE Index",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019002e,
    'DS',
    "Angle Of First View",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019002e,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019002e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019002e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019002e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019002e,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019002f,
    'DS',
    "Trigger Frequency",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019002f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00190030,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190030,
    'LO',
    "?",
    '1-n')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00190030,
    'UL',
    "Maximum Image Frame Size",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190030,
    'US',
    "ECG Triggering",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x00190030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190030,
    'ST',
    "Data stream from cassette",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190030,
    'ST',
    "Set of destination types",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190030,
    'LO',
    "Menu Character String",
    '1')
add_private_dict_entry(
    "GE ??? From Adantage Review CS",
    0x00190030,
    'LO',
    "CR EDR Mode",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190030,
    'LO',
    "Image File Name",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190030,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190030,
    'US',
    "AEC User Density Scale Factor",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190030,
    'US',
    "AEC User Density Scale Factor",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190030,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190030,
    'IS',
    "Acquisition Columns",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00190030,
    'CS',
    "Calculation Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190030,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190030,
    'LO',
    "Orientation",
    '1')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190030,
    'IS',
    "Bucky Grid",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190031,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00190031,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190031,
    'UN',
    "ECG 1 Offset",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190031,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190031,
    'IS',
    "Default Spatial Filter Family",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190031,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190031,
    'US',
    "AEC System Density Scale Factor",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190031,
    'US',
    "AEC System Density Scale Factor",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190031,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190031,
    'IS',
    "Reconstruction Columns",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190031,
    'LO',
    "Mark On Film",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190031,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190031,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190031,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190032,
    'UN',
    "ECG 2 Offset 1",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190032,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190032,
    'LO',
    "Kanji Menu Name",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190032,
    'IS',
    "Default Spatial Filter Strength",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190032,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190032,
    'US',
    "AEC Calculated mAs",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190032,
    'US',
    "AEC Calculated mAs",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190032,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190032,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190032,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190032,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190032,
    'LO',
    "Rotation On DRC",
    '1')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190032,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190033,
    'UN',
    "ECG 2 Offset 2",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190033,
    'DS',
    "Min Saturation Dose",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190033,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190033,
    'US',
    "AEC Auto Pixel 1",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190033,
    'US',
    "AEC Auto Pixel 1",
    '1')
add_private_dict_entry(
    "NNT",
    0x00190033,
    'DS',
    "?",
    '8')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190033,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190034,
    'DS',
    "Detector Gain",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190034,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190034,
    'US',
    "AEC Auto Pixel 2",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190034,
    'US',
    "AEC Auto Pixel 2",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190034,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190034,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190034,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190034,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190034,
    'IS',
    "Focus",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190035,
    'DS',
    "Patient Dose Limit",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190035,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190035,
    'US',
    "AEC Sensor",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190035,
    'US',
    "AEC Sensor",
    '1')
add_private_dict_entry(
    "SIEMENS Selma",
    0x00190035,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190036,
    'DS',
    "Preproc Image Rate Max",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190036,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190036,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190036,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190036,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190037,
    'CS',
    "Sensor Roi Shape",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190037,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190037,
    'LO',
    "NPT Mode",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190037,
    'LO',
    "NPT Mode",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190038,
    'DS',
    "Sensor Roi x Position",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190038,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190038,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190038,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190038,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190038,
    'IS',
    "Age Group",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190039,
    'DS',
    "Sensor Roi y Position",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190039,
    'SS',
    "Scan FOV Type",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x00190039,
    'SS',
    "Axial Type",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190039,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019003A,
    'DS',
    "Sensor Roi x Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019003A,
    'US',
    "Image Flag",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019003a,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019003a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019003a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019003a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019003a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019003a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019003B,
    'DS',
    "Sensor Roi y Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019003B,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019003b,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019003b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019003b,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019003c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019003c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019003c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019003c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019003c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019003D,
    'DS',
    "Noise Sensitivity",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019003d,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019003E,
    'DS',
    "Sharp Sensitivity",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019003e,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019003e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019003e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019003e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019003e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019003F,
    'DS',
    "Contrast Sensitivity",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019003f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019003f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x00190040,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00190040,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190040,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190040,
    'ST',
    "Set of destination Ids",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190040,
    'CS',
    "Image Processing Type",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190040,
    'DS',
    "Lag Sensitivity",
    '1')
add_private_dict_entry(
    "GE ??? From Adantage Review CS",
    0x00190040,
    'LO',
    "CR Latitude",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190040,
    'SS',
    "Stat Recon Flag",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190040,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190040,
    'DS',
    "Skin Edge",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190040,
    'DS',
    "Skin Edge",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190040,
    'IS',
    "Array Coil Element Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190040,
    'UL',
    "Master Control Mask",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190040,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190040,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190040,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190040,
    'LO',
    "Reader Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190040,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190040,
    'SH',
    "Color Flow State",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190040,
    'IS',
    "Collimator Distance X",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190041,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "ADAC_IMG",
    0x00190041,
    'IS',
    "ADAC Header/Image Size",
    '1-n')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190041,
    'CS',
    "Tube",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190041,
    'SS',
    "Compute Type",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190041,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190041,
    'DS',
    "Exposure Index",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190041,
    'DS',
    "Exposure Index",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190041,
    'UL',
    "Array Coil Element Select Mask",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190041,
    'LO',
    "Sub Modality",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190041,
    'SL',
    "Dispayed Area Top Left Hand Corner",
    '2')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190041,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190041,
    'US',
    "Color Flow Wall Filter Index",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190041,
    'IS',
    "Collimator Distance Y",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190042,
    'IS',
    "?",
    '2')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190042,
    'SS',
    "Segment Number",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190042,
    'US',
    "Detector Size Rows",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190042,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190042,
    'IS',
    "Exposure Index Target",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190042,
    'UL',
    "Array Coil Element Data Mask",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190042,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190042,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190042,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190042,
    'US',
    "Processing Mask",
    '5')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190042,
    'LO',
    "Reader Serial Number",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190042,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190042,
    'SH',
    "Color Flow Submode",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  VIEW 1.0",
    0x00190042,
    'SL',
    "Dispayed Area Bottom Right Hand Corner",
    '2')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190043,
    'IS',
    "?",
    '2')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190043,
    'SS',
    "Total Segments Required",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190043,
    'US',
    "Detector Size Columns",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190043,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190043,
    'DS',
    "Short Index Ratio",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190043,
    'IS',
    "Array Coil Element To ADC Connect",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190043,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190043,
    'FD',
    "Color Flow Overall Gain",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190044,
    'DS',
    "Interscan Delay",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190044,
    'DS',
    "Min Object Size",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190044,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190044,
    'DS',
    "Scout kVp",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190044,
    'DS',
    "Array Coil Element Noise Level",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190044,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190044,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190044,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190044,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190044,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190044,
    'US',
    "Color Flow Resolution/Speed Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190045,
    'IS',
    "Reconstruction Resolution",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190045,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190045,
    'DS',
    "Max Object Size",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190045,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190045,
    'IS',
    "Scout mA",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190045,
    'IS',
    "Array Coil ADC Pair Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190045,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190046,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190046,
    'DS',
    "Max Object Speed",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190046,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190046,
    'IS',
    "Scout mAs",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190046,
    'UL',
    "Array Coil Combination Mask",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190046,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190046,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190046,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190046,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190046,
    'US',
    "Color Flow Smooth Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190047,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190047,
    'CS',
    "Object Back Motion",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190047,
    'SS',
    "View Compression Factor",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190047,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190047,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190047,
    'US',
    "Color Flow Persistence Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190048,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190048,
    'UL',
    "Exposure Trajectory Family",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190048,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190048,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190048,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190048,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190048,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190048,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190048,
    'US',
    "Color Flow Map Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190049,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190049,
    'DS',
    "Window Time Duration",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190049,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190049,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190049,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190049,
    'US',
    "Color Flow Priority Index",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019004A,
    'CS',
    "Positioner Angle Display Mode",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019004a,
    'SS',
    "Total Number Of Ref Channels",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019004a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019004a,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019004a,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019004a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019004B,
    'IS',
    "Detector Origin",
    '2')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019004b,
    'SL',
    "Data Size For Scan Data",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019004b,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019004C,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_SERIES_01",
    0x0019004c,
    'CS',
    "Internal Label",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019004c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019004c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019004c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019004c,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_DL_SERIES_01",
    0x0019004d,
    'CS',
    "Browser Hide",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019004E,
    'DS',
    "Default Brightness and Contrast",
    '2')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019004e,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019004e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019004e,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019004F,
    'DS',
    "User Brightness and Contrast",
    '2')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019004f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190050,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190050,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190050,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00190050,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190050,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190050,
    'US',
    "Video Scan Mode",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190050,
    'ST',
    "Set of processing codes",
    '1')
add_private_dict_entry(
    "FOEM 1.0",
    0x00190050,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190050,
    'CS',
    "EDR Mode",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190050,
    'IS',
    "Source Series Number",
    '1')
add_private_dict_entry(
    "GE ??? From Adantage Review CS",
    0x00190050,
    'LO',
    "CR Group Number",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190050,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190050,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190050,
    'DS',
    "Display Minimum OD",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190050,
    'DS',
    "Display Minimum OD",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190050,
    'DS',
    "Detector Alignment",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190050,
    'DS',
    "Receiver Total Gain",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00190050,
    'IS',
    "Noise Level",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190050,
    'IS',
    "Number of Averages Current",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190050,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190050,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190050,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190050,
    'LO',
    "Cassette Scale",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190050,
    'IS',
    "Bucky Height",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190051,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190051,
    'US',
    "Video LineRate",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190051,
    'IS',
    "Source Image Number",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190051,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190051,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190051,
    'DS',
    "Dispaly Maximum OD",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190051,
    'DS',
    "Dispaly Maximum OD",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190051,
    'DS',
    "Receiver Amplifier Gain",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190051,
    'LO',
    "Cassette Matrix",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190052,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190052,
    'IS',
    "Source Frame Number",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190052,
    'SS',
    "Recon Post Processing Flag",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190052,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190052,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190052,
    'IS',
    "Display Minimum Nits",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190052,
    'IS',
    "Display Minimum Nits",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190052,
    'DS',
    "? ",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190052,
    'DS',
    "Receiver Preamplifier Gain",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190052,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190052,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190052,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190052,
    'LO',
    "Cassette Submatrix",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190053,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190053,
    'UI',
    "Source Series Item Id",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190053,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190053,
    'IS',
    "Display Maximum Nits",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190053,
    'IS',
    "Display Maximum Nits",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190053,
    'LO',
    "Barcode",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190054,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190054,
    'UI',
    "Source Image Item Id",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190054,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190054,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190054,
    'DS',
    "? ",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190054,
    'DS',
    "Receiver Cable Attenuation",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190054,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190054,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190054,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190054,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190054,
    'FD',
    "Color Flow Maximum Velocity",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190055,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190055,
    'UI',
    "Source Frame Item Id",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190055,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190055,
    'DS',
    "Receiver Reference Gain",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190056,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190056,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190056,
    'DS',
    "Receiver Filter Frequency",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190056,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190056,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190056,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190057,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190057,
    'SS',
    "CT Water Number",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190057,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190058,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190058,
    'SS',
    "CT Bone Number",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190058,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190058,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190058,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190058,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190059,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190059,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019005a,
    'FL',
    "Acquisition Duration",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019005a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019005a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019005a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019005a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019005a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019005b,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019005b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019005c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019005c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019005c,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019005c,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019005c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019005d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019005d,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019005e,
    'SL',
    "Number Of Channels 1 To 512",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019005e,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019005e,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019005e,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019005f,
    'SL',
    "Increment Between Channels",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0019005f,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019005f,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019005f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190060,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190060,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x00190060,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190060,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190060,
    'US',
    "Xray Technique",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190060,
    'US',
    "Total Number Series",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190060,
    'US',
    "Number of series in study",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190060,
    'SH',
    "Radiographer's Code",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190060,
    'SL',
    "Starting View",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190060,
    'US',
    "Number of Points Before Acquisition",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190060,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190060,
    'LT',
    "Geometry Calibration",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190060,
    'LT',
    "Geometry Calibration",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190060,
    'DS',
    "Focus Alignment",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190060,
    'DS',
    "Reconstruction Scale Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190060,
    'DS',
    "Flip Angle",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00190060,
    'IS',
    "Number of Data Bytes",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190060,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190060,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190060,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190060,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190060,
    'FD',
    "Doppler Dynamic Range",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190060,
    'LO',
    "GT - Contrast Type",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190060,
    'IS',
    "Bucky Angle",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190061,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190061,
    'DS',
    "Image Identifier Fromat",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190061,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190061,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ADAC_IMG",
    0x00190061,
    'OB',
    "ADAC Pegasys Headers",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190061,
    'SH',
    "Session Number",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190061,
    'US',
    "Session Number",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190061,
    'SL',
    "Number Of Views",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190061,
    'OW',
    "Curve Data Before Acquisition",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190061,
    'OB',
    "3D IP Parameters",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190061,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190061,
    'FD',
    "Doppler Overall Gain",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190061,
    'LO',
    "GA - Rotation Amount",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190062,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190062,
    'US',
    "Iris Diaphragm",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190062,
    'SH',
    "ID Station Name",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190062,
    'SH',
    "ID station name",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190062,
    'SL',
    "Increment Between Views",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190062,
    'US',
    "Number of Points Trigger",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190062,
    'LT',
    "2D IP Parameters",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190062,
    'DS',
    "Reference Scale Factor",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190062,
    'IS',
    "Number of Virtuell Channels",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190062,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190062,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190062,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190062,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190062,
    'FD',
    "Doppler Wall Filter",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190062,
    'LO',
    "GC - Rotation Center",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190063,
    'CS',
    "Filter",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190063,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190063,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190063,
    'OW',
    "Curve Data Trigger",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190063,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190063,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190063,
    'FD',
    "Doppler Gate Size",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190063,
    'LO',
    "GS - Density Shift",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190064,
    'CS',
    "Cine Parallel",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190064,
    'DS',
    "Repetition Time SE",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190064,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190064,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190064,
    'SH',
    "ECG Synchronization",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190064,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190064,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190064,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190064,
    'US',
    "RN - Frequency Rank",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190064,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190065,
    'CS',
    "Cine Master",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190065,
    'DS',
    "Repetition Time IR",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190065,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190065,
    'US',
    "Number of Images in Study to be Transmitted",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190065,
    'SH',
    "ECG Delay Mode",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190065,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190065,
    'UL',
    "Focal Spot Deflection Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190065,
    'LO',
    "RE - Frequency Enhancement",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190065,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190065,
    'US',
    "Doppler Map Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190066,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190066,
    'IS',
    "ECG Delay Vector",
    '1-n')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190066,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190066,
    'UL',
    "Focal Spot Deflection Phase",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190066,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190066,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190066,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190066,
    'LO',
    "RT - Frequency Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190066,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190066,
    'SH',
    "Doppler Submode",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190067,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190067,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190067,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190067,
    'UL',
    "Focal Spot Deflection Offset",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190067,
    'LO',
    "Kernel Length",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190067,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190067,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190068,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190068,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190068,
    'UL',
    "Kernel Mode",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190068,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190068,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190068,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190068,
    'IS',
    "C-Arm Angle",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190069,
    'IS',
    "Number of Phases",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190069,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190069,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190069,
    'UL',
    "Convolution Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190069,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190069,
    'US',
    "Doppler Time/Freq Res Index",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190069,
    'IS',
    "Collimator Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019006A,
    'US',
    "Doppler Trace Inverted",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019006a,
    'IS',
    "Cardiac Frequency",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019006a,
    'SS',
    "Dependant On Number Of Views Processed",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019006a,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x0019006a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019006a,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019006a,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019006a,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019006a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019006b,
    'DS',
    "Inversion Delay",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019006b,
    'SS',
    "Field Of View In Detector Cells",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019006b,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x0019006C,
    'US',
    "Doppler Tint Type",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019006c,
    'DS',
    "Gate Delay",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x0019006c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019006c,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019006c,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x0019006c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019006d,
    'DS',
    "Gate Width",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x0019006d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019006e,
    'DS',
    "Trigger Delay Time",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x0019006e,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019006e,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019006e,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190070,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190070,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190070,
    'ST',
    "RAD Protocol Printer",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190070,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190070,
    'US',
    "Exposure Channel",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190070,
    'US',
    "Total Number Images",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190070,
    'US',
    "Number of images in series",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190070,
    'IS',
    "Split Exposure Format",
    '1')
add_private_dict_entry(
    "GE ??? From Adantage Review CS",
    0x00190070,
    'LO',
    "CR Image Serial Number",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190070,
    'SS',
    "Value Of Back Projection Button",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190070,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190070,
    'LO',
    "Frame of Reference ID",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190070,
    'LO',
    "Frame of Reference ID",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190070,
    'DS',
    "Water Scaling Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190070,
    'DS',
    "Phase Gradient Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00190070,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190070,
    'IS',
    "Number of Readings",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190070,
    'IS',
    "Number of Prescans",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190070,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190070,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190070,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190070,
    'LO',
    "PLA Source",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190070,
    'IS',
    "Filter Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190071,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190071,
    'ST',
    "RAD Protocol Medium",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190071,
    'UN',
    "Exposure Channel First Image",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190071,
    'US',
    "Break condition",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190071,
    'IS',
    "Number of Split Exposure Frames",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190071,
    'SS',
    "Set If Fatq Estimates Were Used",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190071,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190071,
    'CS',
    "Paired Position",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190071,
    'CS',
    "Paired Position",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190071,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190071,
    'DS',
    "Interpolation Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190071,
    'DS',
    "Readout Gradient Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190071,
    'LO',
    "PLA Destination",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190072,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190072,
    'US',
    "Processing Channel",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190072,
    'US',
    "Wait (or Hold) flag",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190072,
    'DS',
    "Z Channel Avg Over Views",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190072,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190072,
    'DS',
    "Selection Gradient Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190072,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190072,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190072,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190072,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190072,
    'US',
    "Doppler Tint Index",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x00190072,
    'US',
    "Doppler Tint Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190073,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190073,
    'US',
    "ScanRes flag",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190073,
    'DS',
    "Avg Of Left Ref Channels Over Views",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190073,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190074,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190074,
    'SH',
    "Operation code",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190074,
    'DS',
    "Max Left Channel Over Views",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190074,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190074,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190074,
    'IS',
    "Number of Projections",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190074,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190074,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190074,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SVISION",
    0x00190074,
    'IS',
    "Filter Material 1",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190075,
    'DS',
    "Avg Of Right Ref Channels Over Views",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190075,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190075,
    'IS',
    "Number of Bytes",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190075,
    'LO',
    "UID Original Image",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190075,
    'IS',
    "Filter Material 2",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190076,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190076,
    'DS',
    "Max Right Channel Over Views",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190076,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190076,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190076,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190076,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190076,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190077,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190078,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190078,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190078,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190078,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190078,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190078,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190078,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SVISION",
    0x00190078,
    'DS',
    "Filter Thickness 1",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190079,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190079,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190079,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190079,
    'PN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190079,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190079,
    'DS',
    "Filter Thickness 2",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019007A,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019007a,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019007a,
    'PN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x0019007a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019007a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019007a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019007a,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019007B,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019007b,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019007b,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019007C,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x0019007c,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019007c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019007c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019007c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019007c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019007c,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019007d,
    'DS',
    "Second Echo",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019007d,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x0019007d,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019007d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019007e,
    'SS',
    "Number Of Echos",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019007e,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019007e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019007e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019007e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019007e,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019007f,
    'DS',
    "Table Delta",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x0019007f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x0019007f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190080,
    'DS',
    "Acquisition Delay",
    '1')
add_private_dict_entry(
    "PHILIPS MR SPECTRO;1",
    0x00190080,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190080,
    'IS',
    "Number of Chemical Shifts",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190080,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x00190080,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190080,
    'ST',
    "Geometrical Transformations",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190080,
    'IS',
    "Reading Position Specification",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190080,
    'DS',
    "Image Dose",
    '1')
add_private_dict_entry(
    "GE ??? From Adantage Review CS",
    0x00190080,
    'LO',
    "CR Bar Code Number",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190080,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190080,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190080,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190080,
    'SH',
    "Detector Image Offset",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190080,
    'SH',
    "Detector Image Offset",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190080,
    'DS',
    "Gradient Delay Time",
    '3')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00190080,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190080,
    'LO',
    "Reconstruction Algorithm Set",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190080,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190080,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190080,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190080,
    'CS',
    "Patient Region",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190080,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190080,
    'LT',
    "Reader Header",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190080,
    'US',
    "M-Mode Dynamic Range",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190080,
    'IS',
    "Bucky Format",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190081,
    'DS',
    "Chemical Shift",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190081,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190081,
    'UN',
    "Relative Image Time",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190081,
    'ST',
    "Roam Origin",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190081,
    'IS',
    "Reading Sensitivity Center",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190081,
    'SS',
    "Contiguous",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190081,
    'US',
    "Calibration Frame",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190081,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190081,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190081,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190081,
    'LO',
    "Reconstruction Algorithm Index",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190081,
    'CS',
    "Filter Type for Raw Data",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190081,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190081,
    'US',
    "M-Mode Overall Gain",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190081,
    'IS',
    "Object Position",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190082,
    'US',
    "Zoom Factor",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190082,
    'CS',
    "Calibration Object",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190082,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190082,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190082,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190082,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190082,
    'DS',
    "Total Gradient Delay Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190082,
    'DS',
    "Filter Parameter for Raw Data",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190082,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190082,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190082,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190082,
    'CS',
    "Patient Phase of Life",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190082,
    'LO',
    "Regeneration Software Version",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190082,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190082,
    'US',
    "M-Mode Edge Enhance Index",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190083,
    'DS',
    "Calibration Object Size mm",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190083,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190083,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190083,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0",
    0x00190083,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190083,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190083,
    'CS',
    "Filter Type for Image Data",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190083,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190083,
    'US',
    "M-Mode Map Index",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190084,
    'IS',
    "Number of Rows",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190084,
    'DS',
    "Peak SAR",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190084,
    'FL',
    "Calibration Factor",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190084,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190084,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190084,
    'DS',
    "Filter Parameter for Image Data",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190084,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190084,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190084,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190085,
    'IS',
    "Number of Samples",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190085,
    'DA',
    "Calibration Date",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190085,
    'SS',
    "Monitor SAR",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190085,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190085,
    'SH',
    "Image Source",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190085,
    'CS',
    "Filter Type for Phase Correction",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190086,
    'TM',
    "Calibration Time",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190086,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190086,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190086,
    'DS',
    "Filter Parameter for Phase Correction",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190086,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190086,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190086,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190086,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190086,
    'US',
    "M-Mode Tint Type",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190087,
    'DS',
    "Cardiac Repetition Time",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190087,
    'US',
    "Calibration Accuracy",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190087,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190087,
    'LO',
    "Marker Text",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190087,
    'CS',
    "Normalization Filter Type for Image Data",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190087,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190087,
    'SH',
    "M-Mode Submode",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190088,
    'CS',
    "Calibration Extended",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190088,
    'SS',
    "Images Per Cardiac Cycle",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190088,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190088,
    'LO',
    "Marker Tech Initials",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190088,
    'DS',
    "Normalization Filter Parameter for Image Data",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00190088,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190088,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190088,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190088,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190088,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190088,
    'US',
    "M-Mode Tint Index",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x00190088,
    'US',
    "M-mode Tint Index",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190089,
    'IS',
    "Exposure Index",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190089,
    'US',
    "Calibration Image Original",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190089,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190089,
    'DS',
    "Marker Location",
    '2')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x00190089,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019008A,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x0019008A,
    'IS',
    "Collimator X",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019008A,
    'US',
    "Calibration Frame Original",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x0019008A,
    'SQ',
    "Marker Sequence",
    '2')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019008a,
    'SS',
    "Actual Receive Gain Analog",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x0019008a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019008a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019008a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019008a,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019008B,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x0019008B,
    'IS',
    "Collimator Y",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019008B,
    'US',
    "Calibration nb points uif",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019008b,
    'SS',
    "Actual Receive Gain Digital",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019008C,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x0019008C,
    'LO',
    "Print Marker",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019008C,
    'US',
    "Calibration Points Row",
    '1-n')
add_private_dict_entry(
    "Harmony R2.0",
    0x0019008c,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019008c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019008c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019008c,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019008D,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x0019008D,
    'LO',
    "RGDV Name",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019008D,
    'US',
    "Calibration Points Column",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019008d,
    'DS',
    "Delay After Trigger",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x0019008d,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019008E,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x0019008E,
    'LO',
    "Acqd Sensitivity",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019008E,
    'FL',
    "Calibration Magnification Ratio",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019008e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019008e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019008e,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0019008F,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x0019008F,
    'LO',
    "Processing Category",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019008F,
    'LO',
    "Calibration Software Version",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019008f,
    'SS',
    "Swap Phase Frequency",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x0019008f,
    'SS',
    "Swap Phase Frequency",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x0019008f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00190090,
    'CS',
    "Video White Compression",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190090,
    'LO',
    "Unprocessed Flag",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00190090,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x00190090,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190090,
    'SH',
    "Film Annotation Character String 1",
    '1')
add_private_dict_entry(
    "GE ??? From Adantage Review CS",
    0x00190090,
    'LO',
    "CR Film Output Exposures",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190090,
    'LO',
    "Extended Calibration Software Version",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190090,
    'SS',
    "Pause Interval",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190090,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190090,
    'DS',
    "Conventional Tomo Angle",
    '1')
add_private_dict_entry(
    "LORAD Selenia",
    0x00190090,
    'DS',
    "Conventional Tomo Angle",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190090,
    'DS',
    "Osteo Offset",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190090,
    'IS',
    "Number of Saturation Regions",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190090,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190090,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00190090,
    'LO',
    "PLA of Secondary Destination",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190090,
    'LO',
    "Sensitivity Correction Label",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00190090,
    'LO',
    "Desk Command",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190091,
    'DS',
    "Key Values",
    '1-n')
add_private_dict_entry(
    "FDMS 1.0",
    0x00190091,
    'SH',
    "Film Annotation Character String 2",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190091,
    'DS',
    "Pause Time",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190091,
    'IS',
    "Calibration Return Code",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C2",
    0x00190091,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190091,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190091,
    'DS',
    "Saturation Phase Encoding Vector Coronal Component",
    '6')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190091,
    'DS',
    "Saturation Phase Encoding Vector Sagittal Component",
    '6')
add_private_dict_entry(
    "SVISION",
    0x00190091,
    'IS',
    "Central Beam X",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00190092,
    'LO',
    "Destination Postprocessing Function",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190092,
    'DS',
    "Detector Rotation Angle",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190092,
    'SL',
    "Slice Offset On Frequency Axis",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190092,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190092,
    'DS',
    "Osteo Regression Line Slope",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x00190092,
    'DS',
    "Saturation Readout Vector Coronal Component",
    '6')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190092,
    'DS',
    "Saturation Readout Vector Sagittal Component",
    '6')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190092,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190092,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190092,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SVISION",
    0x00190092,
    'IS',
    "Central Beam Y",
    '1')
add_private_dict_entry(
    "AGFA",
    0x00190093,
    'CS',
    "Status",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190093,
    'CS',
    "Spatial Change",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190093,
    'DS',
    "Auto Prescan Center Frequency",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190093,
    'DS',
    "?",
    '2')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190093,
    'DS',
    "Osteo Regression Line Intercept",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190093,
    'IS',
    "EPI Stimulation Monitor Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00190093,
    'SL',
    "?",
    '2')
add_private_dict_entry(
    "SVISION",
    0x00190093,
    'IS',
    "Tube Turn Angle",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190094,
    'LO',
    "Magnetization Transfer Contrast",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190094,
    'CS',
    "Inconsistent Flag",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190094,
    'SS',
    "Auto Prescan Transmit Gain",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190094,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190094,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190094,
    'DS',
    "Image Rotation Angle",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190094,
    'IS',
    "Osteo Standardization Code",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190094,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190094,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190094,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SVISION",
    0x00190094,
    'IS',
    "Stand Drive Level",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190095,
    'LO',
    "Spectral Presaturation With Inversion Recovery",
    '1')
add_private_dict_entry(
    "AGFA_ADC_Compact",
    0x00190095,
    'CS',
    "Image quality",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190095,
    'CS',
    "Horizontal and Vertical Image Flip",
    '2')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190095,
    'SS',
    "Auto Prescan Analog Receiver Gain",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190095,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190095,
    'LO',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x00190095,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000",
    0x00190095,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190096,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190096,
    'CS',
    "Internal Label Image",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190096,
    'SS',
    "Auto Prescan Digital Receiver Gain",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190096,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190096,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x00190096,
    'IS',
    "Osteo Phantom Number",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190096,
    'UL',
    "Coil ID Mask",
    '3')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190096,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190096,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190096,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00190097,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190097,
    'DS',
    "Angle 1 increment",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190097,
    'SL',
    "Bitmap Defining CVs",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190097,
    'IS',
    "?",
    '2')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190097,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190097,
    'SH',
    "Markers Burned Into Image",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190097,
    'UL',
    "Coil Class Mask",
    '2')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190098,
    'DS',
    "Angle 2 increment",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190098,
    'SS',
    "Center Frequency Method",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x00190098,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "HOLOGIC,Inc.",
    0x00190098,
    'LO',
    "Grid Line Correction",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00190098,
    'DS',
    "Coil Position",
    '3')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x00190098,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x00190098,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00190098,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x00190099,
    'DS',
    "Angle 3 increment",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x00190099,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R2.0",
    0x00190099,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019009a,
    'DS',
    "Sensor Feedback",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019009a,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019009a,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019009a,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019009B,
    'CS',
    "Grid",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019009b,
    'SS',
    "Pulse Sequence Mode",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019009C,
    'FL',
    "Default Mask Pixel Shift",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019009c,
    'LO',
    "Pulse Sequence Name",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x0019009c,
    'SS',
    "Pulse Sequence Name",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019009c,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019009c,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019009c,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019009D,
    'CS',
    "Applicable Review Mode",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019009d,
    'DT',
    "Pulse Sequence Date",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019009E,
    'DS',
    "Log LUT Control Points",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019009e,
    'LO',
    "Internal Pulse Sequence Name",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x0019009e,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x0019009e,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x0019009e,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x0019009F,
    'DS',
    "Exp LUT SUB Control Points",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x0019009f,
    'SS',
    "Transmitting Coil",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x0019009f,
    'SS',
    "Coil Type",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A0,
    'LO',
    "Version",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A0,
    'DS',
    "ABD Value",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900a0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x001900a0,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x001900a0,
    'US',
    "Angulation",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x001900a0,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900a0,
    'SS',
    "Surface Coil Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a0,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x001900a0,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x001900a0,
    'DS',
    "EPI Reconstruction Phase",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900a0,
    'IS',
    "RF Watchdog Mask",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900a0,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900a0,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES",
    0x001900a0,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x001900a0,
    'DS',
    "Extended Exposure Time",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A1,
    'LO',
    "Ranging Mode",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A1,
    'DS',
    "Subtraction Window Center",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900a1,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900a1,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x001900a1,
    'US',
    "Rotation",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x001900a1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x001900a1,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900a1,
    'SS',
    "Extremity Coil Flag",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a1,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x001900a1,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900a1,
    'DS',
    "EPI Reconstruction Slope",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x001900a1,
    'DS',
    "EPI Reconstruction Slope",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x001900a1,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x001900a1,
    'DS',
    "Actual Exposure Time",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A2,
    'DS',
    "Abdomen Brightness",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A2,
    'DS',
    "Subtraction Window Width",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x001900a2,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x001900a2,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900a2,
    'SL',
    "Raw Data Run Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a2,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900a2,
    'DS',
    "RF Power Error Indicator",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900a2,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900a2,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900a2,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A3,
    'DS',
    "Fixed Brightness",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A3,
    'DS',
    "Image Rotation",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900a3,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900a3,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x001900a3,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x001900a3,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900a3,
    'UL',
    "Calibrated Field Strength",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a3,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x001900a3,
    'SL',
    "?",
    '2')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A4,
    'DS',
    "Detail Contrast",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A4,
    'CS',
    "Auto Injection Enabled",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900a4,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900a4,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x001900a4,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900a4,
    'SS',
    "SAT Fat Water Bone",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x001900a4,
    'SS',
    "SAT Fat Water Bone",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a4,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900a4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900a4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900a4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A5,
    'DS',
    "Contrast Balance",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A5,
    'CS',
    "Injection Phase",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x001900A5,
    'SS',
    "Number of Repeats per Phase",
    '1-n')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900a5,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900a5,
    'DS',
    "Receive Bandwidth",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a5,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900a5,
    'DS',
    "Specific Absorption Rate Whole Body",
    '3')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900a5,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A6,
    'DS',
    "Structure Boost",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A6,
    'DS',
    "Injection Delay",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x001900A6,
    'SS',
    "Cycles per Repeat",
    '1-n')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900a6,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900a6,
    'DS',
    "Specific Energy Dose",
    '3')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a6,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900a6,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900a6,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900a6,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A7,
    'DS',
    "Structure Preference",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A7,
    'IS',
    "Reference Injection Frame Number",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x001900A7,
    'SL',
    "Repeat Start Time",
    '1-n')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900a7,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900a7,
    'DS',
    "User Data 0",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a7,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900a7,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A8,
    'DS',
    "Noise Robustness",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A8,
    'DS',
    "Injection Duration",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x001900A8,
    'SL',
    "Repeat Stop Time",
    '1-n')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900a8,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900a8,
    'DS',
    "User Data 1",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900a8,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900a8,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a8,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900a8,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x001900a8,
    'DS',
    "Extended X-ray Tube Current",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900A9,
    'DS',
    "Noise Dose Limit",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900A9,
    'DS',
    "EPT",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x001900A9,
    'SL',
    "Effective Repeat Time",
    '1-n')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900a9,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900a9,
    'DS',
    "User Data 2",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900a9,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900a9,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900AA,
    'DS',
    "Noise Dose Step",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900AA,
    'CS',
    "Can Downscan 512",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x001900AA,
    'SS',
    "Acquired Cycles per Repeat",
    '1-n')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900aa,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900aa,
    'DS',
    "User Data 3",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900aa,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900aa,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900aa,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900aa,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900AB,
    'DS',
    "Noise Frequency Limit",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900AB,
    'IS',
    "Current Spatial Filter Strength",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900ab,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900ab,
    'DS',
    "User Data 4",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900ab,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900ab,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900AC,
    'DS',
    "Weak Contrast Limit",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900AC,
    'DS',
    "Brightness Sensitivity",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900ac,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900ac,
    'DS',
    "User Data 5",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900ac,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900ac,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900ac,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900ac,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900AD,
    'DS',
    "Strong Contrast Limit",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900AD,
    'DS',
    "Exp LUT NOSUB Control Points",
    '1-n')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900ad,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900ad,
    'DS',
    "User Data 6",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900ad,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900ad,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900AE,
    'DS',
    "Structure Boost Offset",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900ae,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900ae,
    'DS',
    "User Data 7",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900ae,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900ae,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900ae,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900AF,
    'LO',
    "Smooth Gain",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900AF,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900af,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900af,
    'DS',
    "User Data 8",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900af,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900B0,
    'LO',
    "Measure Field 1",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x001900b0,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b0,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b0,
    'DS',
    "User Data 9",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900b0,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900b0,
    'DS',
    "Feed per Rotation",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900b0,
    'UL',
    "Adjustment Status Mask",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x001900b0,
    'IS',
    "Dose Indicator",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900B1,
    'LO',
    "Measure Field 2",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900b1,
    'IS',
    "Minimum RR Interval",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x001900b1,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b1,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b1,
    'DS',
    "User Data 10",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900b1,
    'LO',
    "Acquisition Mode Description",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900b1,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x001900b1,
    'IS',
    "Shift Reference Value",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900B2,
    'IS',
    "Key Percentile 1",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900b2,
    'IS',
    "Maximum RR Interval",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b2,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b2,
    'DS',
    "User Data 11",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900b2,
    'LO',
    "Acquisition Mode Description Label",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b2,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b2,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900B3,
    'IS',
    "Key Percentile 2",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900b3,
    'IS',
    "Number of Rejections",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b3,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b3,
    'DS',
    "User Data 12",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900b3,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b3,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b3,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900B4,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900B4,
    'IS',
    "Density LUT",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b4,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900b4,
    'IS',
    "Number of RR Intervals",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b4,
    'DS',
    "User Data 13",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900B5,
    'DS',
    "Brightness",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900B5,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b5,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900b5,
    'IS',
    "Arrhythmia Rejection",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b5,
    'DS',
    "User Data 14",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b5,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b5,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x001900B6,
    'DS',
    "Gamma",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900B6,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b6,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b6,
    'DS',
    "User Data 15",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b6,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b6,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900B7,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b7,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b7,
    'DS',
    "User Data 16",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b7,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b7,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b8,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b8,
    'DS',
    "User Data 17",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900b8,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b8,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b8,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900b9,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900b9,
    'DS',
    "User Data 18",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900b9,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900b9,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-PCR Release 2",
    0x001900ba,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900ba,
    'CS',
    "Acquisition Region",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900ba,
    'DS',
    "User Data 19",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900bb,
    'CS',
    "Acquisition SUB Mode",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900bb,
    'DS',
    "User Data 20",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900bb,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900bb,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900bc,
    'DS',
    "User Data 21",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900bc,
    'FL',
    "Table Cradle Angle",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900bc,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900bc,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900bd,
    'CS',
    "Table Rotation Status Vector",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900bd,
    'DS',
    "User Data 22",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900bd,
    'IS',
    "Pulmo Trigger Level",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900bd,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900bd,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900be,
    'DS',
    "Projection Angle",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900be,
    'FL',
    "Source to Image Distance per Frame Vector",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900be,
    'DS',
    "Expiratoric Reserve Volume",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900be,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900be,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900bf,
    'DS',
    "Vital Capacity",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900bf,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900bf,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900c0,
    'DS',
    "Trigger Delay Times",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900c0,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c0,
    'SS',
    "Saturation Planes",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x001900c0,
    'SS',
    "Bitmap Of SAT Selections",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900c0,
    'DS',
    "Pulmo Water",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c0,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c0,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c1,
    'SS',
    "Surface Coil Intensity Correction Flag",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x001900c1,
    'SS',
    "Surface Coil Intensity Correction Flag",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900c1,
    'DS',
    "Pulmo Air",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900c1,
    'DS',
    "EPI Capacity",
    '6')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c1,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c1,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900c2,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c2,
    'SS',
    "SAT Location R",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900c2,
    'DA',
    "Pulmo Date",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900c2,
    'DS',
    "EPI Inductance",
    '3')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c2,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c2,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900c3,
    'FL',
    "Table Rotation Angle Increment",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c3,
    'SS',
    "SAT Location L",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900c3,
    'IS',
    "EPI Switch Configuration Code",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900c3,
    'TM',
    "Pulmo Time",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x001900c3,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c3,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c3,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900c4,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c4,
    'SS',
    "SAT Location A",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900c4,
    'IS',
    "EPI Switch Hardware Code",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900c4,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c4,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c4,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c5,
    'SS',
    "SAT Location P",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900c5,
    'DS',
    "EPI Switch Delay Time",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  COAD",
    0x001900c5,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c5,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c5,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900c6,
    'IS',
    "Cycled Multiple Slice",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c6,
    'SS',
    "SAT Location H",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c6,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c6,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900c7,
    'CS',
    "Patient Position per Image",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c7,
    'SS',
    "SAT Location F",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c7,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c7,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900c8,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c8,
    'SS',
    "SAT Thickness R L",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c8,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c8,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900c9,
    'IS',
    "Foldover Direction Transverse",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900c9,
    'SS',
    "SAT Thickness A P",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900c9,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900c9,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900ca,
    'IS',
    "Foldover Direction Sagittal",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900ca,
    'SS',
    "SAT Thickness H F",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900ca,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900ca,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900cb,
    'IS',
    "Foldover Direction Coronal",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900cb,
    'SS',
    "PhaseContrast Flow Axis",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x001900cb,
    'SS',
    "Phase Contrast Flow Axis",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900cb,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900cb,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900cc,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900cc,
    'SS',
    "Velocity Encoding",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x001900cc,
    'SS',
    "Phase Contrast Velocity Encoding",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900cc,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900cc,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900cd,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900cd,
    'SS',
    "Thickness Disclaimer",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900cd,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900cd,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900ce,
    'IS',
    "REST",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900ce,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900ce,
    'SS',
    "Prescan Type",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900ce,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900ce,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900cf,
    'IS',
    "Number of Echoes",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900cf,
    'SS',
    "Prescan Status",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900cf,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900cf,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900d0,
    'IS',
    "Scan Resolution",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900d0,
    'SH',
    "Raw Data Type",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900D1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900d1,
    'DS',
    "Flow Sensitivity",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900d1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900d1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900d2,
    'LO',
    "Water Fat Shift",
    '2')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900d2,
    'SS',
    "Projection Algorithm",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900d2,
    'CS',
    "Calculation Submode",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900d2,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900d2,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900D3,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900d3,
    'SH',
    "Projection Algorithm Name",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900d3,
    'DS',
    "Field of View Ratio",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900d3,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900d3,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900d4,
    'IS',
    "Artifact Reduction",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900d4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900d4,
    'IS',
    "Base Raw Matrix Size",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900d4,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900d4,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900d5,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900d5,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900d5,
    'SS',
    "Fractional Echo",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x001900d5,
    'SS',
    "Fractional Echo",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900d5,
    'IS',
    "2D Oversampling Lines",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900d5,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900d5,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900d6,
    'IS',
    "Fourier Interpolation",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900d6,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900d6,
    'SS',
    "Prep Pulse",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900d6,
    'IS',
    "3D Phase Oversampling Partitions",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900d6,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900d6,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900d7,
    'DS',
    "Scan Percentage",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900d7,
    'SS',
    "Cardiac Phases",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900d7,
    'FL',
    "Table X Position to Iso‐center Increment",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900d7,
    'IS',
    "Echo Line Position",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900d7,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900d7,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900d8,
    'IS',
    "Halfscan",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900d8,
    'SS',
    "Variable Echo Flag",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900d8,
    'FL',
    "Table Y Position to Iso‐center Increment",
    '1-n')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x001900d8,
    'SS',
    "Variable Echo Flag",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900d8,
    'IS',
    "Echo Column Position",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900d8,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900d8,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900d9,
    'IS',
    "EPI Factor",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900d9,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900d9,
    'DS',
    "Concatenated Sat or DTI Diffusion Direction",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x001900d9,
    'DS',
    "Concatenated Sat",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900d9,
    'FL',
    "Table Z Position to Iso‐center Increment",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900d9,
    'IS',
    "Lines Per Segment",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900d9,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900d9,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900da,
    'IS',
    "Turbo Factor",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900da,
    'SS',
    "Reference Channel Used",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900da,
    'FL',
    "Table Head Tilt Angle Increment",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR VA0  COAD",
    0x001900da,
    'CS',
    "Phase Coding Direction",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900da,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900da,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900db,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900db,
    'DS',
    "Back Projector Coefficient",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900db,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900db,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900dc,
    'SS',
    "Primary Speed Correction Used",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900dc,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900dc,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900dc,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900dd,
    'SS',
    "Overrange Correction Used",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900dd,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900dd,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900dd,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900de,
    'CS',
    "Acquisition Plane",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900de,
    'DS',
    "Dynamic Z Alpha Value",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900de,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900de,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900df,
    'DS',
    "User Data 23 or DTI Diffusion Direction",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900df,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900df,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900e0,
    'IS',
    "Prepulse",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900e0,
    'IS',
    "Percentage of Scan Completed",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900e0,
    'IS',
    "Prepulse Type",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900e0,
    'DS',
    "User Data 24 or DTI Diffusion Direction",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900e0,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE A",
    0x001900e0,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA PLANE B",
    0x001900e0,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900e1,
    'DS',
    "Prepulse Delay",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900e1,
    'DS',
    "Prepulse Delay",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900e1,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900e1,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900e2,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900e2,
    'DS',
    "Velocity Encode Scale",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900e3,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900e3,
    'DS',
    "Phase Contrast Velocity",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900e3,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900E4,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900e4,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900e4,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900E5,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900e5,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900e5,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900e6,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900e6,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900e7,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900e8,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900e8,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900e9,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900e9,
    'FL',
    "Source to Detector Distance per Frame Vector",
    '1-n')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900e9,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900ea,
    'FL',
    "Table Rotation Angle",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900ea,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900eb,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900eb,
    'FL',
    "Table X Position to Iso‐center",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900eb,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900ec,
    'FL',
    "Table Y Position to Iso‐center",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900ec,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900ec,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900ed,
    'FL',
    "Table Z Position to Iso‐center",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900ed,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900ee,
    'FL',
    "Table Head Tilt Angle",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900ee,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_IMG_01",
    0x001900ef,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900ef,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900F0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900f0,
    'LT',
    "WS Protocol String 1",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900f0,
    'LO',
    "User Defined field 1",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900f0,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900f0,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x001900f0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900f1,
    'LT',
    "WS Protocol String 2",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900f1,
    'LO',
    "User Defined field 2",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900f1,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900f1,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900f2,
    'LT',
    "WS Protocol String 3",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900f2,
    'LO',
    "User Defined field 3",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900f2,
    'SS',
    "Fast Phases",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x001900f2,
    'SS',
    "Number Of Phases",
    '1')
add_private_dict_entry(
    "Harmony R1.0 C3",
    0x001900f2,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x001900f3,
    'LT',
    "WS Protocol String 4",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900f3,
    'LO',
    "User Defined field 4",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900f3,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900f4,
    'LO',
    "User Defined field 5",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900f4,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900f5,
    'CS',
    "Cassette Orientation",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900F6,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900f6,
    'DS',
    "Plate Sensitivity",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900F7,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900f7,
    'DS',
    "Plate Erasability",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900F8,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900f8,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900F9,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACQU_01",
    0x001900f9,
    'DS',
    "Transmit Gain",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900FA,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900fa,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900FB,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900FC,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x001900fc,
    'IS',
    "Resonance Frequency",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900fc,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900fd,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Agfa ADC NX",
    0x001900fe,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x001900ff,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210000,
    'DA',
    "Scan Date",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210000,
    'DA',
    "Series Date",
    '1')
add_private_dict_entry(
    "SPI-P-CTBE-Private Release 1",
    0x00210000,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00210000,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210000,
    'IS',
    "Reconstruction Number",
    '1')
add_private_dict_entry(
    "SPI-P-Private-CWS Release 1",
    0x00210000,
    'LT',
    "Window Of Images ID",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210000,
    'SQ',
    "Person Information Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210000,
    'US',
    "Acquisition Type",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210000,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210000,
    'CS',
    "Sequence Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED ECAT FILE INFO",
    0x00210000,
    'OB',
    "ECAT_Main_Header",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00210000,
    'OB',
    "ECAT_Main_Header",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound S2000",
    0x00210000,
    'US',
    "Nipple Position",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210000,
    'DS',
    "Noise Reduction",
    '1')
add_private_dict_entry(
    "SPI-P-Private-CWS Release 1",
    0x00210001,
    'CS',
    "Window Of Images Type",
    '1')
add_private_dict_entry(
    "PHILIPS-MR-1",
    0x00210001,
    'IS',
    "Reconstruction Number",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210001,
    'LO',
    "Person ID",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00210001,
    'US',
    "raw_data_type",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00210001,
    'LT',
    "Image Analysis Data in XML",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00210001,
    'LT',
    "Image Analysis Data in XML",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210001,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00210001,
    'SQ',
    "Unassigned Shared Converted Attributes Sequence",
    '1')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Change Item Creator ID",
    0x00210001,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Change List Creator ID",
    0x00210001,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Note List Creator ID",
    0x00210001,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210001,
    'IS',
    "Vector Size Original",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210001,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210001,
    'US',
    "Acquisition Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210001,
    'FD',
    "Transmitter Reference Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS MR PS 04",
    0x00210001,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR CM 03",
    0x00210001,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210001,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210001,
    'IS',
    "Used Patient Weight",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210001,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR FOR 06",
    0x00210001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED ECAT FILE INFO",
    0x00210001,
    'OB',
    "ECAT_Image_Subheader",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00210001,
    'OB',
    "ECAT_Image_Subheader",
    '1')
add_private_dict_entry(
    "SIEMENS MR IMA",
    0x00210001,
    'SQ',
    "MR Image Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR PHOENIX ATTRIBUTES",
    0x00210001,
    'UL',
    "Mds Mode Mask",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210001,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210001,
    'US',
    "Number of Images in Mosaic",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound S2000",
    0x00210001,
    'US',
    "ABVS Clip Derived From Volume",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00210001,
    'FD',
    "Image Position (Volume)",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210001,
    'DS',
    "Contrast Amplification",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00210001,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS-MR-1",
    0x00210002,
    'IS',
    "Slice Number",
    '1')
add_private_dict_entry(
    "SPI-P-Private-CWS Release 1",
    0x00210002,
    'IS',
    "WindowOfImagesScope",
    '1-n')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210002,
    'PN',
    "Person Name",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210002,
    'IS',
    "Coordinate System Number of Axes ",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210002,
    'SQ',
    "Evaluator Sequence",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00210002,
    'UL',
    "raw_data_size",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00210002,
    'SQ',
    "Unassigned Per-Frame Converted Attributes Sequence",
    '1')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Change List Creator ID",
    0x00210002,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Note List Creator ID",
    0x00210002,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Change Item Creator ID",
    0x00210002,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210002,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210002,
    'IS',
    "Vector Size Extended",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210002,
    'US',
    "Footswitch Index",
    '1')
add_private_dict_entry(
    "SIEMENS MR CM 03",
    0x00210002,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210002,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210002,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210002,
    'DS',
    "SAR Whole Body",
    '3')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210002,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210002,
    'FD',
    "Slice Normal Vector",
    '3')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210002,
    'US',
    "Hamming Filter Width",
    '1')
add_private_dict_entry(
    "SIEMENS MR PHOENIX ATTRIBUTES",
    0x00210002,
    'US',
    "Dixon",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00210002,
    'FD',
    "Image Orientation (Volume)",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210002,
    'DS',
    "Edge Contrast Boosting",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00210002,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210003,
    'LO',
    "Person Role",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210003,
    'SS',
    "Series From Which Prescribed",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00210003,
    'SQ',
    "Conversion Source Attributes Sequence",
    '1')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Change Item Creator ID",
    0x00210003,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210003,
    'DS',
    "Acquired Spectral Range",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210003,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210003,
    'US',
    "Acquisition Room",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210003,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210003,
    'DS',
    "Slice Measurement Duration",
    '1')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210003,
    'FD',
    "CSI Gridshift Vector",
    '3')
add_private_dict_entry(
    "SIEMENS MR PHOENIX ATTRIBUTES",
    0x00210003,
    'LT',
    "Sequence File Name",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210003,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210003,
    'OB',
    "MR Protocol",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210003,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210003,
    'DS',
    "Latitude Reduction",
    '1')
add_private_dict_entry(
    "TOSHIBA_MEC_1.0",
    0x00210003,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210004,
    'SH',
    "Person Home Phone",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210004,
    'IS',
    "Evaluator Number",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210004,
    'SQ',
    "Coordinate System Axes Sequence",
    '1')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Change Item Creator ID",
    0x00210004,
    'PN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210004,
    'DS',
    "VOI Position",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210004,
    'SL',
    "Current Time Product",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210004,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210004,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210004,
    'DS',
    "Time After Start",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210004,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210004,
    'DS',
    "Slice Array Concatenations",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210004,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210004,
    'FD',
    "Mixing Time",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210005,
    'SH',
    "Person Work Phone",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210005,
    'SH',
    "Genesis Version Now",
    '1')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Change Item Creator ID",
    0x00210005,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210005,
    'DS',
    "VOI Size",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210005,
    'SL',
    "Imager Receptor Dose",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210005,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210005,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210005,
    'IS',
    "B Value",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210005,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210005,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210005,
    'IS',
    "Rel Table Position",
    '3')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210006,
    'SH',
    "Person Cell Phone",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210006,
    'PN',
    "Evaluator Name",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210006,
    'ST',
    "Coordinate System Axis Description",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210006,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210006,
    'IS',
    "CSI Matrix Size Original",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210006,
    'SL',
    "Skin Dose Percent",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210006,
    'LO',
    "ICE Dims",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210006,
    'LO',
    "Coil For Gradient",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210007,
    'SH',
    "Person Pager Phone",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210007,
    'UL',
    "Series Record Checksum",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210007,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210007,
    'IS',
    "CSI Matrix Size Extended",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210007,
    'SL',
    "Skin Dose Accumulation",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210007,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210007,
    'LO',
    "Long Model Name",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210007,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00210007,
    'CS',
    "Ultrasound Acquisition Geometry",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210008,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210008,
    'SH',
    "Person Fax Phone",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210008,
    'CS',
    "Coordinate System Data Set Mapping",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210008,
    'IS',
    "Evaluation Attempt",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210008,
    'DS',
    "Spatial Grid Shift",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210008,
    'SL',
    "Skin Dose Rate",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210008,
    'US',
    "Auto Window Flag",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210008,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210008,
    'SH',
    "Gradient Mode",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210008,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00210008,
    'US',
    "Auto Window Flag",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00210008,
    'FD',
    "Apex Position",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210009,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210009,
    'LO',
    "Person EMail",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210009,
    'DS',
    "Signal Limits Minimum",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210009,
    'SL',
    "Auto Window Center",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210009,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210009,
    'LO',
    "PAT Mode Text",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210009,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00210009,
    'SL',
    "Auto Window Center",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210009,
    'UL',
    "Impac Filename",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00210009,
    'FD',
    "Volume to Transducer Mapping Matrix",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x0021000A,
    'ST',
    "Person Address",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x0021000A,
    'IS',
    "Coordinate System Axis Number",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021000A,
    'UL',
    "Copper Filter",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000A,
    'DS',
    "SW Correction Factor",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x0021000A,
    'SL',
    "Auto Window Width",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0021000A,
    'FD',
    "Volume to Table Mapping Matrix",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0021000a,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x0021000a,
    'SL',
    "Auto Window Width",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000a,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021000a,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x0021000B,
    'LO',
    "Person Password",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021000B,
    'US',
    "Measuring Field",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000B,
    'DS',
    "RF Power Error Indicator",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x0021000B,
    'SS',
    "Filter ID",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x0021000b,
    'SS',
    "Filter ID",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x0021000C,
    'SH',
    "Person Emergency Phone",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x0021000C,
    'CS',
    "Coordinate System Axis Type",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021000C,
    'SS',
    "Post Blanking Circle",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000C,
    'SH',
    "Positive PCS Directions",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0021000C,
    'CS',
    "Patient Frame of Reference Source",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x0021000c,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000c,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021000c,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x0021000D,
    'LO',
    "Physician ID",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021000D,
    'SS',
    "Dyna Angles",
    '2-n')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000D,
    'US',
    "Protocol Change History",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0021000D,
    'FD',
    "Temporal Position Time Offset",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x0021000d,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021000d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x0021000E,
    'CS',
    "Coordinate System Axis Units",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021000E,
    'SS',
    "Total Steps",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000E,
    'LO',
    "Data File Name",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0021000E,
    'SQ',
    "Plane Position (Volume) Sequence",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x0021000e,
    'US',
    "Dose Control Value",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021000F,
    'SL',
    "Dyna X-Ray Info",
    '4-n')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000F,
    'DS',
    "Stimlim",
    '3')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0021000F,
    'SQ',
    "Plane Orientation (Volume) Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x0021000f,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x0021000f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021000f,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021000f,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00210010,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210010,
    'IS',
    "Image Type",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210010,
    'TM',
    "Scan Time",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210010,
    'OB',
    "Coordinate System Axis Values",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00210010,
    'CS',
    "FCR Image ID",
    '1')
add_private_dict_entry(
    "MeVis eD: Absolute Temporal Positions",
    0x00210010,
    'LT',
    "Timepoint DateTime",
    '1')
add_private_dict_entry(
    "MeVis eD: Timepoint Information",
    0x00210010,
    'LT',
    "Timepoint DateTime",
    '1')
add_private_dict_entry(
    "MeVis eD: Slice Information",
    0x00210010,
    'UI',
    "Slice SOP Instance UIDs",
    '1-n')
add_private_dict_entry(
    "MeVis eD: Geometry Information",
    0x00210010,
    'UN',
    "Geometry Scanner Origin",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210010,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00210010,
    'DS',
    "Zoom",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210010,
    'DS',
    "Signal Limits Maximum",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210010,
    'IS',
    "Rotation Angle",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  RAW",
    0x00210010,
    'UL',
    "Creation Mask",
    '2')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210010,
    'US',
    "Modality LUT Input Gamma",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210010,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210010,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210010,
    'IS',
    "MR Protocol Version",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210010,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00210010,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00210010,
    'SQ',
    "Temporal Position Sequence",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210010,
    'LO',
    "Find Range Algorithm",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210011,
    'LO',
    "Original Patient ID",
    '1')
add_private_dict_entry(
    "MeVis eD: Absolute Temporal Positions",
    0x00210011,
    'CS',
    "Timepoint DateTime Type",
    '1')
add_private_dict_entry(
    "MeVis eD: Timepoint Information",
    0x00210011,
    'CS',
    "Timepoint DateTime Type",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210011,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210011,
    'DS',
    "Spec Info Mask",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00210011,
    'DS',
    "Target",
    '2')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210011,
    'IS',
    "Start Angle",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210011,
    'US',
    "Modality LUT Output Gamma",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210011,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210011,
    'DS',
    "Phase Gradient Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210011,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210011,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00210011,
    'CS',
    "Dimension Organization Type",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210011,
    'DS',
    "Threshold C-Algorithm",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00210012,
    'LT',
    "Series Unique Identifier",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210012,
    'UI',
    "Original Study Instance UID",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210012,
    'SQ',
    "Indication Sequence",
    '1')
add_private_dict_entry(
    "MeVis eD: Absolute Temporal Positions",
    0x00210012,
    'UN',
    "Timepoint Series Description",
    '1')
add_private_dict_entry(
    "MeVis eD: Timepoint Information",
    0x00210012,
    'UN',
    "Timepoint Series Description",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210012,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210012,
    'DS',
    "EPI Time Rate of Change of Magnitude",
    '1')
add_private_dict_entry(
    "SIEMENS MED",
    0x00210012,
    'IS',
    "Tube Angle",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210012,
    'OB',
    "SH_STPAR",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210012,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210012,
    'FD',
    "Readout OS",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210012,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210012,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210013,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00210013,
    'IS',
    "Image Sequence Number",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210013,
    'UI',
    "Original Series Instance UID",
    '1')
add_private_dict_entry(
    "MeVis eD: Absolute Temporal Positions",
    0x00210013,
    'UN',
    "Timepoint Gradient Directions",
    '1')
add_private_dict_entry(
    "MeVis eD: Timepoint Information",
    0x00210013,
    'UN',
    "Timepoint Gradient Directions",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210013,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210013,
    'DS',
    "EPI Time Rate of Change of X Component",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210013,
    'US',
    "Acquisition Zoom",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210013,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210013,
    'DS',
    "tpuls max",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210013,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210013,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00210014,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210014,
    'LO',
    "Master Accession Number",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210014,
    'IS',
    "Indication Number ",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210014,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210014,
    'DS',
    "EPI Time Rate of Change of Y Component",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210014,
    'SS',
    "Dyna Angulation Step",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210014,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210014,
    'IS',
    "Number of Prescans",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210014,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00210014,
    'US',
    "Anatomic Correct View",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210014,
    'US',
    "Anatomic Correct View",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210015,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210015,
    'LO',
    "Order Category",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210015,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210015,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210015,
    'DS',
    "EPI Time Rate of Change of Z Component",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00210015,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210015,
    'US',
    "DDO Value",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210015,
    'FL',
    "Measurement Index",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00210015,
    'SS',
    "Auto Window Shift",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210015,
    'SS',
    "Auto Window Shift",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210016,
    'LO',
    "Patient ICN",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210016,
    'SH',
    "Indication Label",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210016,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210016,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210016,
    'DS',
    "EPI Time Rate of Change Legal Limit 1",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210016,
    'US',
    "DR Single Flag",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210016,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210016,
    'DS',
    "dBdt Threshold",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210016,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00210016,
    'DS',
    "Auto Window Expansion",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210016,
    'DS',
    "Auto Window Expansion",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210017,
    'LO',
    "Patient DFS",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210017,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210017,
    'IS',
    "EPI Operation Mode Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210017,
    'SL',
    "Source to Isocenter",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210017,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210017,
    'DS',
    "Selection Gradient Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210017,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00210017,
    'LO',
    "System Type",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210017,
    'LO',
    "System Type",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210018,
    'LO',
    "Patient Class",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210018,
    'ST',
    "Indication Description",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210018,
    'SH',
    "Genesis Version Now",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210018,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210018,
    'DS',
    "EPI Field Calculation Safety Factor",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210018,
    'US',
    "Pressure Data",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210018,
    'LO',
    "Detector Type",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210018,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210018,
    'SH',
    "RF SWD Most Critical Aspect",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210018,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210019,
    'LO',
    "Patient Type",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210019,
    'UL',
    "Acq Recon Record Checksum",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210019,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210019,
    'DS',
    "EPI Legal Limit 1 of Change Value",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210019,
    'SL',
    "ECG Index Array",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210019,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210019,
    'OB',
    "MR Phoenix Protocol",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210019,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x0021001A,
    'CS',
    "Indication Type",
    '1-n')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021001A,
    'US',
    "FD Flag",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001A,
    'LO',
    "Coil String",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021001A,
    'SH',
    "RF SWD Data Type",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x0021001a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021001a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021001a,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021001B,
    'OB',
    "SH_ZOOM",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001B,
    'DS',
    "Slice Resolution",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021001B,
    'US',
    "MoCoQ Measure",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x0021001b,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001b,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021001b,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x0021001C,
    'CS',
    "Indication Disposition",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021001C,
    'OB',
    "SH_COLPAR",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001C,
    'DS',
    "Stim max online",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021001C,
    'IS',
    "Phase Encoding Direction Positive",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x0021001c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001c,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021001c,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021001c,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021001D,
    'US',
    "K-Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001D,
    'IS',
    "Operation Mode Flag",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021001D,
    'OB',
    "Pixel File",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x0021001d,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001d,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021001d,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x0021001E,
    'SQ',
    "Indication ROI Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021001E,
    'US',
    "EVE",
    '8')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001E,
    'FL',
    "Auto Align Matrix",
    '16')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x0021001e,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x0021001F,
    'LT',
    "Generic String",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021001F,
    'SL',
    "Total Scene Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001F,
    'DS',
    "Coil Tuning Reflection",
    '2')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021001F,
    'IS',
    "FMRI Stimul Info",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x0021001f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021001f,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021001f,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021001f,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00210020,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210020,
    'IS',
    "Slice Number",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00210020,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210020,
    'LO',
    "QC Study Assigned By",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210020,
    'SQ',
    "Coordinate System Transform Sequence",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210020,
    'DS',
    "Table Start Location",
    '1')
add_private_dict_entry(
    "GEMS_XR3DCAL_01",
    0x00210020,
    'LT',
    "Generalized Calibration",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210020,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210020,
    'DS',
    "EPI Legal Limit 2 of Change Value",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210020,
    'DS',
    "FoV",
    '2')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210020,
    'IS',
    "Phase Correction Rows Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210020,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  RAW",
    0x00210020,
    'UL',
    "Evaluation Mask",
    '2')
add_private_dict_entry(
    "SIEMENS MED",
    0x00210020,
    'US',
    "ROI Mask",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00210020,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210020,
    'US',
    "Restore Flag",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210020,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210020,
    'DS',
    "Voxel in Plane Rot",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210020,
    'UI',
    "Representative Image",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210020,
    'LO',
    "Sensometric Curve",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00210021,
    'DS',
    "Slice Gap",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210021,
    'IS',
    "Slice Gap",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210021,
    'LO',
    "QC Study Split By",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210021,
    'DS',
    "EPI Rise Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210021,
    'IS',
    "Phase Correction Columns Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210021,
    'US',
    "Stand Movement Flag",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210021,
    'CS',
    "Diffusion Directionality 4MF",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00210022,
    'DS',
    "Stack Radial Angle",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210022,
    'LO',
    "QC Study Moved By",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210022,
    'ST',
    "Transform Description",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210022,
    'DS',
    "Image Magnification Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210022,
    'IS',
    "Phase Correction Rows Reconstruction",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210022,
    'US',
    "FD Rows",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210022,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210022,
    'DS',
    "Voxel Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210022,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210022,
    'SH',
    "Sequence File Owner",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210022,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210023,
    'LO',
    "QC Study Edited By",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210023,
    'US',
    "FD Columns",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210023,
    'FD',
    "B Matrix",
    '6')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210023,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210023,
    'IS',
    "RF Watchdog Mask",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210023,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210024,
    'LO',
    "QC Series Split By",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210024,
    'IS',
    "Transform Number of Axes",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210024,
    'DS',
    "Image Scroll Offset",
    '2')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210024,
    'IS',
    "Phase Correction Columns Reconstruction",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210024,
    'US',
    "Table Movement Flag",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210024,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210024,
    'IS',
    "Multistep Index",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210024,
    'LO',
    "Post Proc Protocol",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210025,
    'LO',
    "QC Series Moved By",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00210025,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210025,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210025,
    'LT',
    "Comp Adjusted Param",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210025,
    'SL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210025,
    'SL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210025,
    'SL',
    "Table Position Origin",
    '3')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210026,
    'LO',
    "QC Series Edited By",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210026,
    'IS',
    "Transform Order of Axes",
    '1-n')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210026,
    'IS',
    "Image Pixel Offset",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210026,
    'DS',
    "Crispy XPI Filter Value",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210026,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210026,
    'IS',
    "Comp Algorithm",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210026,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210026,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210026,
    'IS',
    "Misc Sequence Param",
    '32')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210027,
    'LO',
    "QC Image Moved By",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210027,
    'US',
    "IC Stent Flag",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210027,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210027,
    'DS',
    "Voxel NormalC or",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210027,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210027,
    'US',
    "Isocentered",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00210027,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210027,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210028,
    'LO',
    "QC Image Edited By",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x00210028,
    'CS',
    "Transformed Axis Units",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210028,
    'SQ',
    "Gamma LUT Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00210028,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210029,
    'DS',
    "Acquisition Scene Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210029,
    'SH',
    "Flow Encoding Direction String",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x0021002A,
    'DS',
    "Coordinate System Transform Rotation and Scale Matrix",
    '1-n')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021002A,
    'IS',
    "3D Cardiac Phase Center",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021002A,
    'DS',
    "Voxel Normal Sag",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002A,
    'IS',
    "Coil ID",
    '1-n')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021002a,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002a,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021002a,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021002B,
    'IS',
    "3D Cardiac Phase Width",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021002B,
    'DS',
    "Voxel Position Sag",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002B,
    'ST',
    "Pat Rein Pattern",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021002b,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002b,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021002b,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NDEGeometry",
    0x0021002C,
    'DS',
    "Coordinate System Transform Translation Matrix",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021002C,
    'DS',
    "Voxel Normal Tra",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002C,
    'DS',
    "SED",
    '3')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021002c,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002c,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021002c,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021002D,
    'DS',
    "Voxel Position Tra",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002D,
    'DS',
    "SAR Most Critical Aspect",
    '3')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021002d,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021002d,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002d,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002E,
    'IS',
    "Stimm on mode",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021002E,
    'UL',
    "Used Channel Mask",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002e,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021002e,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021002e,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021002F,
    'DS',
    "Repetition Time Effective",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002F,
    'DS',
    "Gradient Delay Time",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021002f,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021002f,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00210030,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210030,
    'IS',
    "Echo Number",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210030,
    'LO',
    "QC Done Time",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210030,
    'SQ',
    "Indication Physical Property Sequence",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00210030,
    'CS',
    "Set Number",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210030,
    'CS',
    "View Direction",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210030,
    'DS',
    "Array Coil ADC Offset",
    '16')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210030,
    'IS',
    "Topogram Tube Position",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210030,
    'IS',
    "Number of 3D Raw Partitions Nominal",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210030,
    'OB',
    "Organ Program Info",
    '1')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00210030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  RAW",
    0x00210030,
    'US',
    "Extended Processing Mask",
    '7')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210030,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210030,
    'DS',
    "Readout Gradient Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210030,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210030,
    'DS',
    "CSI Image Orientation Patient",
    '6')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00210030,
    'SH',
    "Anatomic Sort Number",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210030,
    'SQ',
    "Background Color DR Sequence",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210030,
    'US',
    "Anatomic Sort Number",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210030,
    'DS',
    "Lower Window Offset",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210031,
    'DS',
    "Patient Reference ID",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210031,
    'LO',
    "QC Last Modification Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210031,
    'DS',
    "Array Coil Preamplifier Gain",
    '16')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210031,
    'IS',
    "Number of 3D Raw Partitions Current",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210031,
    'DS',
    "Background Color",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210031,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210031,
    'IS',
    "Abs Table Position",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210031,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Lab Settings",
    0x00210031,
    'SH',
    "AcquisitionSortNumber",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Post Processing",
    0x00210031,
    'US',
    "Acquisition Sort Number",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210031,
    'DS',
    "Upper Window Offset",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210032,
    'LO',
    "QC Image Accepted By",
    '1')
add_private_dict_entry(
    "astm.org/diconde/iod/NdeIndication",
    0x00210032,
    'SH',
    "Property Label",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210032,
    'CS',
    "Patient Rest Direction",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210032,
    'DS',
    "Length of Topogram",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210032,
    'DS',
    "CSI Slice Location",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210032,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210032,
    'SS',
    "RF SWD Operation Mode",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210032,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210033,
    'LO',
    "QC Image Rejected By",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210033,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210033,
    'IS',
    "Echo Column Position",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210033,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210033,
    'SH',
    "Coil for Gradient2",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210033,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210034,
    'DA',
    "QC Done Date",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210034,
    'DA',
    "QC Last Modification Date",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210034,
    'DS',
    "Topogram Correction Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210034,
    'IS',
    "Number of 3D Image Partitions",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210034,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210034,
    'DS',
    "Stim Factor",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210034,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210034,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210034,
    'FD',
    "Flow VENC",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210035,
    'IS',
    "Chemical Shift Number",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210035,
    'SS',
    "Series From Which Prescribed",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210035,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210035,
    'DS',
    "Stim max ges norm online",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210035,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210035,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210035,
    'IS',
    "Measured Fourier Lines",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210036,
    'SS',
    "Image From Which Prescribed",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210036,
    'DS',
    "Maximum Table Position",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210036,
    'IS',
    "Actual 3D Image Partition Number",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210036,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210036,
    'DS',
    "dBdt max",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210036,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210036,
    'SH',
    "LQ Algorithm",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210036,
    'SQ',
    "Field Map DR Sequence",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210037,
    'SS',
    "Screen Format",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210037,
    'CS',
    "Visible",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210037,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210037,
    'DS',
    "Voxel Position Cor",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210038,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210038,
    'DS',
    "Transmitter Calibration",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x00210038,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210038,
    'DS',
    "Tinting Color",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210038,
    'IS',
    "Filter2",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210039,
    'DS',
    "Slab Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210039,
    'CS',
    "Tinting Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210039,
    'FD',
    "FMRI Stimul Level",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210039,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210039,
    'OB',
    "MR EVA Protocol",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021003A,
    'DS',
    "Voxel Readout FOV",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021003A,
    'IS',
    "DDO Kernel size",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021003A,
    'LO',
    "Volume ID",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021003a,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021003B,
    'IS',
    "mAs Modulation",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021003B,
    'DS',
    "dBdt Limit",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021003B,
    'IS',
    "Normalize Manipulated",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021003B,
    'LO',
    "Volume ID As Bound",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021003b,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SERIES SHADOW ATTRIBUTES",
    0x0021003b,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021003b,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021003C,
    'DT',
    "3D R-Peak Reference Time",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021003C,
    'FD',
    "RBMoCoRot",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021003C,
    'OB',
    "VF Model Info",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021003c,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021003D,
    'SL',
    "ECG Frame Time Vector",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021003D,
    'CS',
    "Phase Slice Oversampling",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021003D,
    'IS',
    "Comp Manual Adjusted",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021003d,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021003E,
    'SL',
    "ECG Start Time of Run",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021003E,
    'OB',
    "VF Settings",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021003F,
    'SH',
    "Spectrum Text Region Label",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x0021003F,
    'UT',
    "Auto Align Data",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021003f,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210040,
    'IS',
    "Phase Number",
    '1')
add_private_dict_entry(
    "SPI-P-Private_CDS Release 1",
    0x00210040,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00210040,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00210040,
    'IS',
    "Image Number in the Set",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210040,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210040,
    'IS',
    "Table Move Direction Code",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210040,
    'IS',
    "Number of Slices Nominal",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  RAW",
    0x00210040,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS RA GEN",
    0x00210040,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210040,
    'US',
    "Gamma LUT Descriptor",
    '3')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210040,
    'CS',
    "Series Protocol Instance",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210040,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210040,
    'DS',
    "Voxel Phase FOV",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210040,
    'UT',
    "FMRI Model Parameters",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210040,
    'DS',
    "Minimal Printable Density",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210041,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210041,
    'IS',
    "Number of Slices Current",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210041,
    'LO',
    "Gamma LUT Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  RAW",
    0x00210041,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210041,
    'CS',
    "Spectro Result Type",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210041,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210041,
    'SH',
    "GSWD Data Type",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210041,
    'SQ',
    "Floating MPR Color LUT DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210041,
    'UT',
    "FMRI Model Info",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210041,
    'DS',
    "Maximal Printable Density",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210042,
    'IS',
    "Current Slice Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  RAW",
    0x00210042,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210042,
    'US',
    "Gamma LUT Data",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210042,
    'CS',
    "Spectro Result Extend Type",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210042,
    'DS',
    "RGBA LUT",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210042,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210042,
    'IS',
    "Real Dwell Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210042,
    'UT',
    "FMRI External Parameters",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210043,
    'IS',
    "Current Group Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  RAW",
    0x00210043,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210043,
    'CS',
    "Post Proc Protocol",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210043,
    'DS',
    "Blend Factor",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210043,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210043,
    'LT',
    "Comp Job ID",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210043,
    'US',
    "Global Gain",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210043,
    'UT',
    "FMRI External Info",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210044,
    'DS',
    "Current Slice Distance Factor",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  RAW",
    0x00210044,
    'UL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210044,
    'CS',
    "Rescan Level",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210044,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210044,
    'DS',
    "B1 RMS",
    '2')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210044,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210044,
    'IS',
    "Comp Blended",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210044,
    'SQ',
    "RGBA LUT Data Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210044,
    'US',
    "Global Offset",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210045,
    'IS',
    "VOI Start Row",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210045,
    'IS',
    "MIP Start Row",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210045,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210045,
    'CS',
    "B1 RMS Supervision",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210045,
    'OB',
    "Color LUT",
    '1')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210045,
    'OF',
    "Spectro Algo Result",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210045,
    'SL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210045,
    'SL',
    "Ima Abs Table Position",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210045,
    'US',
    "DIPP Mode",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210046,
    'IS',
    "VOI Stop Row",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210046,
    'IS',
    "MIP Stop Row",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210046,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210046,
    'DS',
    "Tales Reference Power",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210046,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210046,
    'FD',
    "Diffusion Gradient Direction",
    '3')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210046,
    'OF',
    "Spectro Display Params",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210046,
    'US',
    "Artis System Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210047,
    'IS',
    "VOI Start Column",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210047,
    'IS',
    "MIP Start Column",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210047,
    'CS',
    "Safety Standard",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210047,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210047,
    'IS',
    "Voxel Number",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210047,
    'IS',
    "Flow Encoding Direction",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210047,
    'US',
    "Artis Table Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210048,
    'IS',
    "VOI Stop Column",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210048,
    'IS',
    "MIP Stop Column",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210048,
    'CS',
    "DICOM Image Flavor",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210048,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210048,
    'IS',
    "Echo Partition Position",
    '1')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210048,
    'SQ',
    "APR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210048,
    'US',
    "Artis Table Top Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210049,
    'IS',
    "VOI Start Slice",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210049,
    'IS',
    "MIP Start Slice",
    '1')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x00210049,
    'CS',
    "Sync Data",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210049,
    'CS',
    "DICOM Acquisition Contrast",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210049,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210049,
    'IS',
    "Echo Line Position",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210049,
    'US',
    "Water Value",
    '1')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x0021004A,
    'CS',
    "Post Proc Detailed Protocol",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021004A,
    'SQ',
    "Ortho MPR ColorLUT DR Sequence",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x0021004a,
    'LO',
    "Anatomical Reference For Scout",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x0021004a,
    'IS',
    "VOI Stop Slice",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x0021004a,
    'IS',
    "MIP Stop Slice",
    '1')
add_private_dict_entry(
    "SIEMENS MR MRS 05",
    0x0021004B,
    'CS',
    "Spectro Result Extend Type Detailed",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021004B,
    'LT',
    "Comp Auto Param",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021004B,
    'SQ',
    "VRT Color LUT DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021004b,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021004C,
    'IS',
    "Original Image Number",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021004C,
    'SQ',
    "Pwl Transfer Function Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021004D,
    'IS',
    "Original Series Number",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021004D,
    'SQ',
    "Pwl Transfer Function Data Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021004E,
    'DS',
    "Pwl Vertex Index",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021004E,
    'IS',
    "Actual 3D Ima Part Number",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x0021004e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021004e,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021004F,
    'LO',
    "Ima Coil String",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x0021004f,
    'SS',
    "Locations In Acquisition",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x0021004f,
    'CS',
    "Order of Slices",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021004f,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210050,
    'IS',
    "Dynamic Scan Number",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00210050,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210050,
    'LO',
    "QC Deletion Requested",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00210050,
    'CS',
    "Pair Processing Information",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210050,
    'SS',
    "Graphically Prescribed",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210050,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210050,
    'IS',
    "Vector Start Row",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210050,
    'UL',
    "Signal Mask",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  RAW",
    0x00210050,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210050,
    'DS',
    "CSI Pixel Spacing",
    '2')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210050,
    'LO',
    "Saturation Type",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210050,
    'SQ',
    "Pwl Vertex Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210050,
    'US',
    "RF Echo Train Length 4MF",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210050,
    'DS',
    "Minimal Window Latitude",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210051,
    'DS',
    "Rotation From Source X Rot",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210051,
    'DS',
    "3D Positioner Primary Start Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210051,
    'DS',
    "Saturation Normal Vector",
    '3')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210051,
    'IS',
    "Vector Row Step",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210051,
    'SQ',
    "Floating MPR Render DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210051,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210051,
    'UL',
    "Sequence Mask",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210051,
    'US',
    "Gradient Echo Train Length 4MF",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210051,
    'DS',
    "Maximal Window Latitude",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210052,
    'DS',
    "Rotation From Source Y Rot",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210052,
    'DS',
    "3D Positioner Secondary Start Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210052,
    'DS',
    "Saturation Position Vector",
    '3')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210052,
    'IS',
    "Vector Start Column",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210052,
    'IS',
    "Delay After Trigger",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210052,
    'CS',
    "Primary Show Hide",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210052,
    'LO',
    "Version Info",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210052,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210052,
    'US',
    "Image Group",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210052,
    'DS',
    "Relative Window Alignment",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210053,
    'DS',
    "Rotation From Source Z Rot",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210053,
    'DS',
    "Saturation Thickness",
    '6')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210053,
    'IS',
    "Vector Column Step",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210053,
    'IS',
    "RR Interval",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210053,
    'SS',
    "Stand Position",
    '3')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210053,
    'CS',
    "Secondary Show Hide",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x00210053,
    'CS',
    "Laterality 4MF",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210053,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210053,
    'FD',
    "Bandwidth Per Pixel Phase Encode",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210054,
    'SH',
    "Image Position",
    '3')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210054,
    'DS',
    "Number of Trigger Pulses",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210054,
    'DS',
    "Saturation Width",
    '6')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210054,
    'SS',
    "Rotation Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210054,
    'LO',
    "Primary Shading Index",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210054,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210054,
    'US',
    "Non Planar Image",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210055,
    'SH',
    "Image Orientation",
    '6')
add_private_dict_entry(
    "SIEMENS MR VA0  RAW",
    0x00210055,
    'DS',
    "Saturation Distance",
    '6')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210055,
    'US',
    "Image Rotation",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210055,
    'LO',
    "Secondary Shading Index",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210055,
    'OB',
    "Pixel File Name",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210056,
    'SL',
    "Num 3D slabs",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210056,
    'DS',
    "Repetition Time Effective",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210056,
    'SS',
    "Table Coordinates",
    '3')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210056,
    'CS',
    "Alpha Dependent Fieldmap",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210056,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210056,
    'LO',
    "Ima PAT Mode Text",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210057,
    'SL',
    "Locs per 3D slab",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210057,
    'SS',
    "Isocenter Table Position",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210057,
    'DS',
    "CSI Image Position Patient",
    '3')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210057,
    'LO',
    "Volume Filter",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210057,
    'LO',
    "Gate Phase",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210058,
    'SL',
    "Overlaps",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210058,
    'DS',
    "Gate Threshold",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210058,
    'DS',
    "Table Object Distance",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210058,
    'DS',
    "Bounding Box Color",
    '3')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210058,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210058,
    'SH',
    "Acquisition Matrix Text",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210059,
    'SL',
    "Image Filtering 0.5/0.2T",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210059,
    'DS',
    "Gated Ratio",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210059,
    'CS',
    "Scene Interaction On",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210059,
    'FL',
    "Carm Coordinate System",
    '12-n')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x00210059,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210059,
    'IS',
    "Ima Rel Table Position",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021005A,
    'FD',
    "RBMoCoTrans",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021005A,
    'FL',
    "Robot Axes",
    '6-n')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021005A,
    'SQ',
    "Ortho MPR Render DR Sequence",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x0021005a,
    'SL',
    "Diffusion direction",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021005a,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021005B,
    'FD',
    "Slice Position PCS",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021005B,
    'FL',
    "Table Coordinate System",
    '12')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021005B,
    'SQ',
    "VRT Render DR Sequence",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x0021005b,
    'DS',
    "Tagging Flip Angle",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021005b,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021005C,
    'DS',
    "CSI Slice Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021005C,
    'FL',
    "Patient Coordinate System",
    '12')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x0021005c,
    'DS',
    "Tagging Orientation",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021005D,
    'SS',
    "Angulation",
    '1-n')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x0021005d,
    'DS',
    "Tag Spacing",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021005E,
    'IS',
    "Protocol Slice Number",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x0021005E,
    'SS',
    "Orbital",
    '1-n')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x0021005e,
    'DS',
    "RTIA_timer",
    '1')
add_private_dict_entry(
    "SIEMENS IMAGE SHADOW ATTRIBUTES",
    0x0021005e,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x0021005F,
    'IS',
    "Filter1",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x0021005f,
    'DS',
    "Fps",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00210060,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210060,
    'IS',
    "Number of Rows In Object",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210060,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210060,
    'DS',
    "Image Position",
    '3')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210060,
    'IS',
    "Range Type Code",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210060,
    'IS',
    "Number of Interpolated Images",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210060,
    'SH',
    "Transmitting Coil",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210060,
    'SQ',
    "Clip Plane DR Sequence",
    '6')
add_private_dict_entry(
    "SVISION",
    0x00210060,
    'IS',
    "Decomposition Layer",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210061,
    'IS',
    "Row Number",
    '1-n')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210061,
    'DS',
    "Image Normal",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210061,
    'SS',
    "Large Volume Overlap",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210061,
    'DS',
    "Number of Averages N4",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210061,
    'DS',
    "Plane Center",
    '3')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00210062,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210062,
    'IS',
    "Reference Type Code",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210062,
    'US',
    "Reconstruction Preset",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210062,
    'DS',
    "Plane Normal",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210062,
    'FD',
    "Mosaic Ref Acq Times",
    '1-n')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210063,
    'DS',
    "Image Distance",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210063,
    'SS',
    "3D Start Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210063,
    'DS',
    "Plane Scale",
    '2')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210063,
    'IS',
    "Auto Inline Image Filter Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210064,
    'SL',
    "3D Planned Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210064,
    'CS',
    "Plane Enable GL Clip",
    '1')
add_private_dict_entry(
    "Mayo/IBM Archive Project",
    0x00210065,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210065,
    'SL',
    "3D Rotation Plane Alpha",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210065,
    'US',
    "Image Positioning History Mask",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210065,
    'DS',
    "Plane Handle Ratio",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210065,
    'FD',
    "QC Data",
    '1-n')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210066,
    'SL',
    "3D Rotation Plane Beta",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210066,
    'DS',
    "Plane Bounding Points",
    '24')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210066,
    'LT',
    "Exam Landmarks",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210067,
    'SL',
    "3D First Image Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210067,
    'DS',
    "Plane Motion Matrix",
    '16')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210067,
    'ST',
    "Exam Data Role",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210068,
    'SS',
    "3D Trigger Angle",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210068,
    'DS',
    "Plane Shift Velocity",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210068,
    'OB',
    "MR Diffusion",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210069,
    'CS',
    "Plane Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210069,
    'OB',
    "Real World Value Mapping",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021006A,
    'DS',
    "Plane Rotate Velocity",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x0021006a,
    'DS',
    "Image Row",
    '3')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021006B,
    'CS',
    "Plane Show Graphics",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x0021006b,
    'DS',
    "Image Column",
    '3')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021006C,
    'DS',
    "Offset",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021006D,
    'CS',
    "Ortho MPR At Bounding Box",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021006E,
    'CS',
    "Plane MPR Locked",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021006F,
    'CS',
    "Plane Scaling Disabled",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00210070,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00210070,
    'IS',
    "Film Number within the Series",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210070,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0021",
    0x00210070,
    'FD',
    "Distance Base Plane to Template",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210070,
    'CS',
    "Patient Orientation Set1",
    '3')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210070,
    'DS',
    "Object Orientation",
    '3')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210070,
    'IS',
    "Number of Echoes",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210070,
    'OB',
    "Data Set Info",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210070,
    'SQ',
    "Split Plane DR Sequence",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210071,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "MeVis eD: Absolute Temporal Positions",
    0x00210071,
    'UN',
    "Timepoint Empty Frames",
    '1')
add_private_dict_entry(
    "MeVis eD: Timepoint Information",
    0x00210071,
    'UN',
    "Timepoint Empty Frames",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0021",
    0x00210071,
    'FD',
    "Volume to Patient Matrix",
    '16')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210071,
    'CS',
    "Patient Orientation Set2",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210071,
    'DS',
    "Detector Rotation",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210071,
    'SQ',
    "Floating MPR DR Sequence",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210071,
    'UT',
    "Used Channel String",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0021",
    0x00210072,
    'FD',
    "Patient to World Matrix",
    '16')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210072,
    'DS',
    "Second Echo Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210072,
    'DS',
    "Second Repetition Time",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210072,
    'DS',
    "Light Orientation",
    '3')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210072,
    'CS',
    "Phase ContrastN4",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210072,
    'SQ',
    "Ortho MPR DR Sequence",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210072,
    'SS',
    "Physical Detector Rotation",
    '1-n')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0021",
    0x00210073,
    'SL',
    "Base Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210073,
    'DS',
    "Second Repetition Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210073,
    'CS',
    "Plane Single Selection Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210073,
    'UT',
    "MR Velocity Encoding",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0021",
    0x00210074,
    'SL',
    "Reference Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210074,
    'CS',
    "Plane Alignment",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210074,
    'FD',
    "Velocity Encoding Direction N4",
    '3')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0021",
    0x00210075,
    'SL',
    "Apex Plane",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210075,
    'DS',
    "Light Brightness",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210075,
    'CS',
    "Plane Selected",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210075,
    'CS',
    "Image Type 4MF",
    '1-n')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_0021",
    0x00210076,
    'FD',
    "Base Plane Offset",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x00210076,
    'DS',
    "Light Contrast",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210076,
    'LO',
    "Image History",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210076,
    'SQ',
    "Clustering DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210077,
    'DS',
    "Cluster Size",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210077,
    'LO',
    "SequenceI nfo",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210078,
    'CS',
    "Clustering Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210078,
    'CS',
    "Image Type Visible",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210079,
    'CS',
    "Distortion Correction Type",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210079,
    'LO',
    "Cluster Mask Vol ID",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x0021007a,
    'IS',
    "Overlay Threshold",
    '2')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x0021007b,
    'IS',
    "Surface Threshold",
    '2')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x0021007c,
    'IS',
    "Grey Scale Threshold",
    '2')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00210080,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00210080,
    'CS',
    "Equipment Type-Specific Information",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210080,
    'IS',
    "Cardiac Code",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x00210080,
    'CS',
    "Image Filter Type",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210080,
    'LO',
    "Study Name",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210080,
    'SQ',
    "Head Masking DR Sequence",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210081,
    'DS',
    "Auto Window Level Alpha",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210081,
    'DS',
    "Masking Range",
    '2')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210081,
    'SS',
    "Table Tilt",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210082,
    'DS',
    "Auto Window Level Beta",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210082,
    'CS',
    "Mask Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00210082,
    'SH',
    "Study Type",
    '3')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210082,
    'SS',
    "Table Rotation",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210083,
    'DS',
    "Auto Window Level Window",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210083,
    'SQ',
    "Brain Masking DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x00210083,
    'SS',
    "Table Cradle Tilt",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210084,
    'DS',
    "Auto Window Level Level",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210084,
    'SQ',
    "Masking Status DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210085,
    'SQ',
    "VRT Masking DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210086,
    'SQ',
    "Ortho MPR Masking DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210087,
    'SQ',
    "Floating MPR Masking DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210088,
    'SQ',
    "Align DR Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210089,
    'DS',
    "Registration Matrix",
    '16')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00210090,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210090,
    'AE',
    "Original Sender AE Title",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00210090,
    'CS',
    "LUT Number",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210090,
    'SS',
    "Tube Focal Spot Position",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210090,
    'SQ',
    "Functional Evaluation DR Sequence",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210090,
    'DS',
    "Brightness",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210091,
    'LO',
    "Software Title",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210091,
    'SS',
    "Biopsy Position",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210091,
    'DS',
    "Saturation Phase Encoding Vector Transverse Component",
    '6')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210091,
    'DS',
    "Frame Acquition Numbers",
    '1-n')
add_private_dict_entry(
    "SVISION",
    0x00210091,
    'DS',
    "Contrast",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210092,
    'SH',
    "Software Version",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210092,
    'FL',
    "Biopsy T Location",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210092,
    'DS',
    "Saturation Readout Vector Transverse Component",
    '6')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210092,
    'CS',
    "Show Cursor",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00210092,
    'DS',
    "Shape Factor",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x00210093,
    'LO',
    "Serial Number",
    '1')
add_private_dict_entry(
    "GEMS_RELA_01",
    0x00210093,
    'FL',
    "Biopsy Ref Location",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210093,
    'DS',
    "EPI Change Value of Magnitude",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210093,
    'DS',
    "Current Frame",
    '1')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210094,
    'DS',
    "EPI Change Value of X Component",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210094,
    'DS',
    "Plot Area",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210095,
    'DS',
    "EPI Change Value of Y Component",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210095,
    'DS',
    "Plot Text Position",
    '2')
add_private_dict_entry(
    "SIEMENS MR VA0  GEN",
    0x00210096,
    'DS',
    "EPI Change Value of Z Component",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210096,
    'DS',
    "Base Line Points",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210097,
    'DS',
    "Active Points",
    '1-n')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210098,
    'CS',
    "Show Label",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x00210099,
    'CS',
    "Mean Plot",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021009A,
    'CS',
    "Motion Plot",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021009B,
    'CS',
    "Activate Normallized Curve",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x0021009C,
    'DS',
    "Plot Size",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x002100A0,
    'OB',
    "Crispy1 Container",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A0,
    'SQ',
    "PlotDR Sequence",
    '4')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x002100a0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100a0,
    'SQ',
    "Object Action Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x002100a0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A1,
    'LO',
    "Title",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x002100a1,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100a1,
    'ST',
    "Object Action",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A2,
    'CS',
    "Auto Scale",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x002100a2,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100a2,
    'DA',
    "Object Action Date",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x002100a2,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x002100A3,
    'SQ',
    "3D Cardiac Trigger Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A3,
    'DS',
    "Fixed Scale",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x002100a3,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100a3,
    'TM',
    "Object Action Time",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x002100A4,
    'DT',
    "3D Frame Reference Date Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A4,
    'DS',
    "Background Color",
    '3')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x002100a4,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "KINETDX_GRAPHICS",
    0x002100a4,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x002100A5,
    'FD',
    "3D Cardiac Trigger Delay Time",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A5,
    'LO',
    "Label X",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100a5,
    'AE',
    "Local AE Title",
    '1')
add_private_dict_entry(
    "KINETDX",
    0x002100a5,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ACQ 1.0",
    0x002100A6,
    'FD',
    "3D R-R Interval Time Measured",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A6,
    'LO',
    "Label Y",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100a6,
    'SH',
    "Local IP Address",
    '1')
add_private_dict_entry(
    "KINETDX",
    0x002100a6,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A7,
    'CS',
    "Legend",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100a7,
    'AE',
    "Remote AE Title",
    '1')
add_private_dict_entry(
    "SIEMENS CT VA0  GEN",
    0x002100a7,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A8,
    'CS',
    "Scroll Bar X",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100a8,
    'SH',
    "Remote IP Address",
    '1')
add_private_dict_entry(
    "KINETDX",
    0x002100a8,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100A9,
    'CS',
    "Scroll Bar Y",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100AA,
    'LO',
    "Connect Scroll X",
    '1')
add_private_dict_entry(
    "KINETDX",
    0x002100aa,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100AB,
    'LO',
    "Plot ID",
    '1')
add_private_dict_entry(
    "KINETDX",
    0x002100ab,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100AC,
    'DS',
    "Plot Position",
    '1')
add_private_dict_entry(
    "KINETDX",
    0x002100ac,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "syngoDynamics_Reporting",
    0x002100AD,
    'OB',
    "Data",
    '1')
add_private_dict_entry(
    "syngoDynamics",
    0x002100ae,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B0,
    'SQ',
    "Curve DR Sequence",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x002100b0,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100b0,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "syngoDynamics",
    0x002100b0,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B1,
    'LO',
    "Curve ID",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100b1,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "syngoDynamics",
    0x002100b1,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B2,
    'LO',
    "Plot Type",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100b2,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B3,
    'DS',
    "Curve Values",
    '1-n')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100b3,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B4,
    'DS',
    "Line Color",
    '3')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100b4,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "KINETDX",
    0x002100b4,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B5,
    'DS',
    "Marker Color",
    '3')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100b5,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B6,
    'CS',
    "Line Filled",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100b6,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B7,
    'LO',
    "Label",
    '1')
add_private_dict_entry(
    "BRIT Systems,Inc.",
    0x002100b7,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B8,
    'CS',
    "Show Marker",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100B9,
    'LO',
    "Marker Shape",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100BA,
    'LO',
    "Smoothing Algo",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100BB,
    'DS',
    "Marker Size",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100BC,
    'LO',
    "Line Style",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100BD,
    'LO',
    "Line Pattern",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100BE,
    'DS',
    "Line Width",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100C0,
    'SQ',
    "VRT Filter DR Sequence",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x002100c0,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100C1,
    'LO',
    "Filter Type",
    '1')
add_private_dict_entry(
    "SIEMENS MR N3D",
    0x002100C2,
    'CS',
    "Current Active Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MR PHOENIX ATTRIBUTES",
    0x002100F1,
    'UL',
    "Count of Pseudo Attributes",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDI 02",
    0x002100FE,
    'SQ',
    "Siemens MR SDI Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x002100FE,
    'SQ',
    "Siemens MR SDS Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR SDS 01",
    0x002100fe,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230000,
    'DS',
    "CR DRE",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230000,
    'DS',
    "CR DRE",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230000,
    'LO',
    "CR Exposure Menu Code",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230000,
    'LO',
    "CR Exposure Menu Code",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230000,
    'US',
    "CR S Shift",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230000,
    'US',
    "CR S Shift",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00230000,
    'LO',
    "Encoding Scheme Version",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00230000,
    'LO',
    "Encoding Scheme Version",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  QUANT 1.0",
    0x00230000,
    'DS',
    "Horizontal Calibration Pixel Size",
    '2')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Image Stamp",
    0x00230000,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00230000,
    'LO',
    "Image Laterality",
    '1')
add_private_dict_entry(
    "AMICAS0",
    0x00230001,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_PETD_01",
    0x00230001,
    'OB',
    "raw_data_blob",
    '1')
add_private_dict_entry(
    "GEMS_STDY_01",
    0x00230001,
    'SL',
    "Number Of Series In Study",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230001,
    'SQ',
    "X-Ray Marker Sequence",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00230001,
    'LO',
    "P File Name",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00230001,
    'LO',
    "P File Name",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  QUANT 1.0",
    0x00230001,
    'DS',
    "Vertical Calibration Pixel Size",
    '2')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00230001,
    'US',
    "DICOM Reader flag",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Image Stamp",
    0x00230001,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00230001,
    'IS',
    "Letter Position",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230002,
    'SH',
    "Marker ID",
    '1')
add_private_dict_entry(
    "GEMS_STDY_01",
    0x00230002,
    'SL',
    "Number Of Unarchived Series",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00230002,
    'OB',
    "P File Data",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00230002,
    'OB',
    "P File Data",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  QUANT 1.0",
    0x00230002,
    'LO',
    "Calibration Object",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Image Stamp",
    0x00230002,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00230002,
    'IS',
    "Burned In Annotation",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230003,
    'CS',
    "Marker Type",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00230003,
    'UL',
    "P File Length",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00230003,
    'UL',
    "P File Length",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  QUANT 1.0",
    0x00230003,
    'DS',
    "Calibration Object Size",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Image Stamp",
    0x00230003,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00230003,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230004,
    'FL',
    "Marker Size",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00230004,
    'OB',
    "R File Data",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00230004,
    'OB',
    "R File Data",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  QUANT 1.0",
    0x00230004,
    'LO',
    "Calibration Method",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Image Stamp",
    0x00230004,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230005,
    'US',
    "Marker Color CIELab Value",
    '3')
add_private_dict_entry(
    "HOLOGIC",
    0x00230005,
    'UL',
    "R File Length",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00230005,
    'UL',
    "R File Length",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  QUANT 1.0",
    0x00230005,
    'ST',
    "Filename",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230006,
    'LO',
    "Marker Label",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  QUANT 1.0",
    0x00230006,
    'IS',
    "Frame Number",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230007,
    'CS',
    "Marker Visible State",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  QUANT 1.0",
    0x00230007,
    'IS',
    "Calibration Factor Multiplicity",
    '2')
add_private_dict_entry(
    "AMICAS0",
    0x00230008,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230008,
    'LO',
    "Marker Description",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  QUANT 1.0",
    0x00230008,
    'IS',
    "Calibration Table Object Distance",
    '1')
add_private_dict_entry(
    "SPI-P Release 2;1",
    0x0023000d,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 2;1",
    0x0023000e,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "AMICAS0",
    0x00230010,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00230010,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230010,
    'DS',
    "CR C Shift",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230010,
    'LO',
    "CR Exposure Menu String",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230010,
    'LO',
    "CR Exposure Menu String",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230010,
    'LO',
    "CR C Shift",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230010,
    'SQ',
    "Marker Points Sequence",
    '1')
add_private_dict_entry(
    "GEMS_STDY_01",
    0x00230010,
    'SS',
    "Reference Image Field",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230010,
    'US',
    "CR DRN",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230010,
    'US',
    "CR DRN",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230011,
    'SH',
    "Marker Point ID",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230012,
    'FL',
    "Marker Point Position",
    '3')
add_private_dict_entry(
    "EMAGEON JPEG2K INFO",
    0x00230013,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230013,
    'FL',
    "Marker Point Size",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230014,
    'US',
    "Marker Point Color CIELab Value",
    '3')
add_private_dict_entry(
    "EMAGEON JPEG2K INFO",
    0x00230015,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "AMICAS0",
    0x00230016,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "EMAGEON JPEG2K INFO",
    0x00230016,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230016,
    'CS',
    "Marker Point Visible State",
    '1')
add_private_dict_entry(
    "EMAGEON JPEG2K INFO",
    0x00230017,
    'FL',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230017,
    'IS',
    "Marker Point Order",
    '1')
add_private_dict_entry(
    "EMAGEON JPEG2K INFO",
    0x00230018,
    'FL',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230018,
    'FL',
    "Volume Manual Registration",
    '3')
add_private_dict_entry(
    "EMAGEON JPEG2K INFO",
    0x00230019,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "FDMS 1.0",
    0x00230020,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230020,
    'DS',
    "CR GT",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230020,
    'DS',
    "CR ORE",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230020,
    'DS',
    "CR ORE",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230020,
    'IS',
    "Volumes Threshold",
    '1-n')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230020,
    'LO',
    "CR EDR Mode",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230020,
    'LO',
    "CR EDR Mode",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230020,
    'LO',
    "CR GT",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230025,
    'CS',
    "Cut Plane Activation Flag",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230026,
    'IS',
    "Cut Plane Position Value",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230027,
    'FL',
    "Cut Plane Normal Value",
    '3')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230028,
    'FL',
    "Volume Scaling Factor",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230029,
    'FL',
    "ROI to Table Top Distance",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00230030,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230030,
    'DS',
    "CR GA",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230030,
    'DS',
    "CR GA",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230030,
    'IS',
    "DRR Threshold",
    '1-n')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230030,
    'LO',
    "CR Latitude",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230030,
    'LO',
    "CR Latitude",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230030,
    'US',
    "CR ORN",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230030,
    'US',
    "CR ORN",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230031,
    'FL',
    "Volume Table Position",
    '3')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230032,
    'IS',
    "Rendering Mode",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230033,
    'IS',
    "3D Object Opacity",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230034,
    'IS',
    "Invert Image",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230035,
    'IS',
    "Enhance Full",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230036,
    'FL',
    "Zoom",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230037,
    'IS',
    "Roam",
    '2')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230038,
    'IS',
    "Window Level",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230039,
    'IS',
    "Window Width",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230040,
    'CS',
    "BMC Setting",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230040,
    'DS',
    "CR GC",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230040,
    'DS',
    "CR GC",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230040,
    'LO',
    "CR Group Number",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230040,
    'LO',
    "CR Group Number",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230040,
    'US',
    "CR ORD",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230040,
    'US',
    "CR ORD",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230041,
    'CS',
    "Back View Setting",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230042,
    'CS',
    "Sub Volume Visibility",
    '1-n')
add_private_dict_entry(
    "AMICAS0",
    0x00230043,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230043,
    'CS',
    "3D Landmarks Visibility",
    '1')
add_private_dict_entry(
    "GEMS_3D_INTVL_01",
    0x00230044,
    'CS',
    "Ablation Point Visibility",
    '1')
add_private_dict_entry(
    "AMICAS0",
    0x00230045,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230050,
    'DS',
    "CR GS",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230050,
    'DS',
    "CR GS",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230050,
    'LO',
    "CR Cassette Size",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230050,
    'LO',
    "CR Cassette Size",
    '1')
add_private_dict_entry(
    "GEMS_STDY_01",
    0x00230050,
    'SS',
    "Summary Image",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230050,
    'US',
    "CR Image Serial Number",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230050,
    'US',
    "CR Image Serial Number",
    '1')
add_private_dict_entry(
    "AMICAS0",
    0x00230054,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230060,
    'DS',
    "CR RT",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230060,
    'LO',
    "CR Bar Code Number",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230060,
    'LO',
    "CR Machine ID",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230060,
    'LO',
    "CR Bar Code Number",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230060,
    'LO',
    "CR RT",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230060,
    'LO',
    "CR Machine ID",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230070,
    'DS',
    "CR RE",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230070,
    'DS',
    "CR RE",
    '1')
add_private_dict_entry(
    "GEMS_STDY_01",
    0x00230070,
    'FD',
    "Start Time Secs In First Axial",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230070,
    'LO',
    "CR Film Output Exposure",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230070,
    'LO',
    "CR Machine Type",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230070,
    'LO',
    "CR Film Output Exposure",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230070,
    'LO',
    "CR Machine Type",
    '1')
add_private_dict_entry(
    "GEMS_STDY_01",
    0x00230074,
    'SL',
    "Number Of Updates To Header",
    '1')
add_private_dict_entry(
    "GEMS_STDY_01",
    0x0023007d,
    'SS',
    "Indicates If Study Has Complete Info",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230080,
    'LO',
    "CR Film Format",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230080,
    'LO',
    "CR Technician Code",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230080,
    'LO',
    "CR Film Format",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230080,
    'LO',
    "CR Technician Code",
    '1')
add_private_dict_entry(
    "GEMS_STDY_01",
    0x00230080,
    'SQ',
    "Has MPPS Related Tags",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230080,
    'US',
    "CR RN",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230080,
    'US',
    "CR RN",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK2",
    0x00230090,
    'DS',
    "CR DRT",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK2",
    0x00230090,
    'DS',
    "CR DRT",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK1",
    0x00230090,
    'LO',
    "CR S Shift String",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_1.0 BLOCK3",
    0x00230090,
    'LO',
    "CR Energy Subtraction Parameters",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK1",
    0x00230090,
    'LO',
    "CR S Shift String",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x00230090,
    'LO',
    "CR Energy Subtraction Parameters",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x002300f0,
    'LO',
    "CR Distribution Code",
    '1')
add_private_dict_entry(
    "SVISION",
    0x002300f0,
    'IS',
    "Image SOP Class",
    '1')
add_private_dict_entry(
    "GEMS_ACRQA_2.0 BLOCK3",
    0x002300ff,
    'US',
    "CR Shutters Applied",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250000,
    'SS',
    "Raw Image Amplification",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250000,
    'US',
    "View Native",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250000,
    'IS',
    "Original Image",
    '1')
add_private_dict_entry(
    "SIEMENS MR EXTRACTED CSA HEADER",
    0x00250001,
    'SQ',
    "Extracted MR Header Information Sequence",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250001,
    'SS',
    "Gamma LUT",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250001,
    'US',
    "Original Series Number",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250001,
    'IS',
    "Not Processed Image",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250002,
    'IS',
    "Frame ID",
    '1')
add_private_dict_entry(
    "SIEMENS MR EXTRACTED CSA HEADER",
    0x00250002,
    'LO',
    "Extracted MR Header Creator Identification Code",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250002,
    'US',
    "Original Image Number",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250002,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250002,
    'IS',
    "Cut Out Image",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250003,
    'DS',
    "Distance Source to Detector",
    '1')
add_private_dict_entry(
    "SIEMENS MR EXTRACTED CSA HEADER",
    0x00250003,
    'AT',
    "Extracted MR Header Tag",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250003,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250003,
    'US',
    "Win Center",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250003,
    'IS',
    "Duplicated Image",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250004,
    'DS',
    "Distance Source to Patient",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250004,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250004,
    'US',
    "Win Width",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250004,
    'IS',
    "Stored Image",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250005,
    'DS',
    "Distance Source to Skin",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250005,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250005,
    'US',
    "Win Brightness",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250005,
    'IS',
    "Retrieved Image",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250006,
    'DS',
    "Positioner Primary Angle",
    '1')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x00250006,
    'SS',
    "Last Pulse Sequence Used",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250006,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250006,
    'US',
    "Win Contrast",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250006,
    'IS',
    "New Image",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250007,
    'DS',
    "Positioner Secondary Angle",
    '1')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x00250007,
    'SL',
    "Images In Series",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250007,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250007,
    'US',
    "Original Frame Number",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250007,
    'IS',
    "Media Stored Image",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250008,
    'IS',
    "Beam Orientation",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250008,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250008,
    'US',
    "Original Mask Frame Number",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250008,
    'IS',
    "Image State",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250009,
    'DS',
    "L Arm Angle",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250009,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250009,
    'US',
    "Opac",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250009,
    'IS',
    "Image Stitched Manually",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025000A,
    'SQ',
    "Frame Sequence",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025000a,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x0025000a,
    'US',
    "Original Number of Frames",
    '1')
add_private_dict_entry(
    "SVISION",
    0x0025000a,
    'IS',
    "Image Stitched Automatically",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x0025000b,
    'DS',
    "Original Scene Duration",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025000b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025000C,
    'SS',
    "Harmonization Kernel",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x0025000c,
    'LO',
    "Identifier LOID",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025000D,
    'FL',
    "Harmonization Gain",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x0025000d,
    'SS',
    "Original Scene VFR Info",
    '1-n')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025000E,
    'SS',
    "Edge Enhancement Kernel",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x0025000e,
    'SS',
    "Original Frame ECG Position",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025000F,
    'FL',
    "Edge Enhancement Gain",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x0025000f,
    'SS',
    "Original ECG 1st Frame Offset",
    '1')
add_private_dict_entry(
    "FOEM 1.0",
    0x00250010,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250010,
    'US',
    "Relative Light Emission Amount Sk",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250010,
    'DS',
    "Pivot Angle",
    '1')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x00250010,
    'SL',
    "Landmark Counter",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250010,
    'LT',
    "Internal Value",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250010,
    'SS',
    "Zoom Flag",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250011,
    'US',
    "Term of Correction for Each IP Type St",
    '1')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x00250011,
    'SS',
    "Number Of Acquisitions",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250011,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250011,
    'US',
    "Flexible Pixel Shift",
    '1')
add_private_dict_entry(
    "FOEM 1.0",
    0x00250012,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250012,
    'US',
    "Reading Gain Gp",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250012,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250012,
    'US',
    "Number of Mask Frames",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250013,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250013,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250013,
    'US',
    "Number of Fill Frames",
    '1')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x00250014,
    'SL',
    "Indicates Number Of Updates To Header",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250014,
    'IS',
    "Series Number",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250014,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250015,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250015,
    'IS',
    "Image Number",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250015,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0",
    0x00250016,
    'IS',
    "Ready Processing Status",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250016,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x00250017,
    'SL',
    "Series Complete Flag",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250017,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x00250018,
    'SL',
    "Number Of Images Archived",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250018,
    'US',
    "Auto Gain",
    '1')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x00250019,
    'SL',
    "Last Instance Number Used",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250019,
    'US',
    "Ortho Subsampling",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025001A,
    'DS',
    "Arc Angle",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025001A,
    'US',
    "Image Crop Upper Left",
    '2')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x0025001a,
    'SH',
    "Primary Receiver Suite And Host",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025001B,
    'DS',
    "Table Vertical Position",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025001B,
    'US',
    "Image Crop Upper Right",
    '2')
add_private_dict_entry(
    "GEMS_SERS_01",
    0x0025001b,
    'OB',
    "Protocol Data Block (compressed)",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025001C,
    'DS',
    "Table Longitudinal Position",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025001C,
    'US',
    "Image Crop Lower Left",
    '2')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025001D,
    'DS',
    "Table Lateral Position",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x0025001D,
    'US',
    "Image Crop Lower Right",
    '2')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025001E,
    'IS',
    "Beam Cover Area",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025001F,
    'DS',
    "kVP Actual",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250020,
    'US',
    "?",
    '2')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250020,
    'DS',
    "mAS Actual",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250020,
    'LO',
    "Source Image File",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250021,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250021,
    'DS',
    "PW Actual",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00250021,
    'LO',
    "Source UID",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250022,
    'DS',
    "Kvp Commanded",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250023,
    'DS',
    "Mas Commanded",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250024,
    'DS',
    "Pw Commanded",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250025,
    'CS',
    "Grid",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250026,
    'DS',
    "Sensor Feedback",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250027,
    'DS',
    "Target Entrance Dose",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250028,
    'DS',
    "Cnr Commanded",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250029,
    'DS',
    "Contrast Commanded",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025002A,
    'DS',
    "EPT Actual",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025002B,
    'IS',
    "Spectral Filter Znb",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025002C,
    'DS',
    "Spectral Filter Weight",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025002D,
    'DS',
    "Spectral Filter Density",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025002E,
    'IS',
    "Spectral Filter Thickness",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025002F,
    'IS',
    "Spectral Filter Status",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250030,
    'IS',
    "FOV Dimension",
    '2')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250030,
    'US',
    "Manual Cropping",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250031,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250031,
    'SS',
    "Gamma LUT Parameter 1",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250032,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250032,
    'DS',
    "Gamma LUT Parameter 2",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250033,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250033,
    'IS',
    "FOV Origin",
    '2')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250033,
    'SS',
    "Gamma LUT Parameter 3",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250034,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250034,
    'IS',
    "Collimator Left Vertical Edge",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250034,
    'SS',
    "Gamma LUT Parameter 4",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250035,
    'IS',
    "Collimator Right Vertical Edge",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250035,
    'LO',
    "Gamma LUT Name",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250036,
    'IS',
    "Collimator Up Horizontal Edge",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250036,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250037,
    'IS',
    "Collimator Low Horizontal Edge",
    '1')
add_private_dict_entry(
    "Siemens: Thorax/Multix FD Raw Image Settings",
    0x00250037,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250038,
    'IS',
    "Vertices Polygonal Collimator",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x00250039,
    'IS',
    "Contour Filter Distance",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025003A,
    'UL',
    "Contour Filter Angle",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025003B,
    'CS',
    "Table Rotation Status",
    '1')
add_private_dict_entry(
    "GEMS_DL_FRAME_01",
    0x0025003C,
    'CS',
    "Internal Label Frame",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250040,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250041,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250042,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250042,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250043,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250050,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250051,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250052,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250053,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250060,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250061,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250062,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250063,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250070,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250071,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250072,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250072,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250073,
    'US',
    "?",
    '6')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250074,
    'US',
    "?",
    '6')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250080,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250081,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250081,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250081,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250082,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250082,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250082,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250083,
    'US',
    "?",
    '6')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250083,
    'US',
    "?",
    '6')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250084,
    'US',
    "?",
    '6')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250084,
    'US',
    "?",
    '6')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250084,
    'US',
    "?",
    '6')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250090,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250091,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250092,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250093,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250094,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250095,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00250096,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002500a0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002500a0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002500a0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002500a1,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002500a1,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002500a2,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002500a2,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002500a3,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002500a3,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00270000,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00270000,
    'IS',
    "Number of Series",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ENHANCED IDATASET API",
    0x00270001,
    'CS',
    "Business Unit Code",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00270001,
    'IS',
    "Number of Studies",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ENHANCED IDATASET API",
    0x00270002,
    'LO',
    "Application Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ENHANCED IDATASET API",
    0x00270003,
    'SQ',
    "Application Attributes Sequence",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270006,
    'SL',
    "Image Archive Flag",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00270010,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270010,
    'SS',
    "Scout Type",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00270010,
    'DT',
    "Oldest Series",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00270011,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "APEX_PRIVATE",
    0x00270011,
    'DS',
    "Bed Position",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00270011,
    'DT',
    "Newest Series",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00270012,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SVISION",
    0x00270012,
    'DT',
    "Oldest Study",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00270013,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SVISION",
    0x00270013,
    'DT',
    "Newest Study",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00270014,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00270015,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00270016,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x0027001c,
    'SL',
    "Vma Mamp",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x0027001d,
    'SS',
    "Vma Phase",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x0027001e,
    'SL',
    "Vma Mod",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x0027001f,
    'SL',
    "Vma Clip or Noise Index by 10",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00270020,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270020,
    'SS',
    "Smart Scan On Off Flag",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00270030,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270030,
    'SH',
    "Foreign Image Revision",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270031,
    'SS',
    "Imaging Mode",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270032,
    'SS',
    "Pulse Sequence",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270033,
    'SL',
    "Imaging Options",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270035,
    'SS',
    "Plane Type",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270036,
    'SL',
    "Oblique Plane",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00270040,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270040,
    'SH',
    "RAS Letter Of Image Location",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270041,
    'FL',
    "Image Location",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270042,
    'FL',
    "Center R Coord Of Plane Image",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270043,
    'FL',
    "Center A Coord Of Plane Image",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270044,
    'FL',
    "Center S Coord Of Plane Image",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270045,
    'FL',
    "Normal R Coord",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270046,
    'FL',
    "Normal A Coord",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270047,
    'FL',
    "Normal S Coord",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270048,
    'FL',
    "R Coord Of Top Right Corner",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270049,
    'FL',
    "A Coord Of Top Right Corner",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x0027004a,
    'FL',
    "S Coord Of Top Right Corner",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x0027004b,
    'FL',
    "R Coord Of Bottom Right Corner",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x0027004c,
    'FL',
    "A Coord Of Bottom Right Corner",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x0027004d,
    'FL',
    "S Coord Of Bottom Right Corner",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00270050,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270050,
    'FL',
    "Table Start Location (Scout)",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270051,
    'FL',
    "Table End Location (Scout)",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270052,
    'SH',
    "RAS Letter For Side Of Image",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270053,
    'SH',
    "RAS Letter For Anterior Posterior",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270054,
    'SH',
    "RAS Letter For Scout Start Loc",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270055,
    'SH',
    "RAS Letter For Scout End Loc",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00270060,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270060,
    'FL',
    "Image Dimension X",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270061,
    'FL',
    "Image Dimension Y",
    '1')
add_private_dict_entry(
    "GEMS_IMAG_01",
    0x00270062,
    'FL',
    "Number Of Excitations",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00270070,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00270080,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a1,
    'CS',
    "?",
    '2')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a1,
    'CS',
    "?",
    '2')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a2,
    'CS',
    "?",
    '2')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a2,
    'CS',
    "?",
    '2')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a2,
    'CS',
    "?",
    '2')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a3,
    'SS',
    "?",
    '1-n')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a3,
    'SS',
    "?",
    '1-n')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a3,
    'SS',
    "?",
    '1-n')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a3,
    'SS',
    "?",
    '1-n')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a3,
    'SS',
    "?",
    '1-n')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a3,
    'SS',
    "?",
    '1-n')
add_private_dict_entry(
    "FDMS 1.0",
    0x002700a3,
    'SS',
    "?",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290000,
    'DS',
    "?",
    '2')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290000,
    'DS',
    "?",
    '4')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x00290000,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00290000,
    'LT',
    "Zoom ID",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;2",
    0x00290000,
    'LT',
    "Subtraction Mask ID",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x00290000,
    'LT',
    "Image Enhancement ID",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x00290000,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00290000,
    'SQ',
    "Edge Enhancement Sequence",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;3",
    0x00290000,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_CDS Release 1",
    0x00290000,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "AEGIS_DICOM_2.00",
    0x00290000,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "1.2.840.113663.1",
    0x00290000,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00290000,
    'OB',
    "Graph Bitmap Data",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00290000,
    'OB',
    "Graph Bitmap Data",
    '1')
add_private_dict_entry(
    "Silhouette Graphics Export V1.0",
    0x00290000,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290000,
    'CS',
    "Rotation",
    '1')
add_private_dict_entry(
    "MITRA OBJECT DOCUMENT 1.0",
    0x00290000,
    'OB',
    "IMPAX Object Document",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290000,
    'OB',
    "Markup1",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290000,
    'CS',
    "Presentation Name",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290000,
    'LT',
    "Dual Energy Algorithm Parameters",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL TMP DATAMODEL",
    0x00290000,
    'OB',
    "CT Task Common DataModel",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00290000,
    'SQ',
    "Edge Enhancement Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290000,
    'US',
    "Translucent Mode",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL EVIDENCEDOCUMENT",
    0x00290000,
    'UT',
    "Private Task Datamodel",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL MEASUREMENT",
    0x00290000,
    'UT',
    "Oncology Segmentation Measurement Values",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00290000,
    'IS',
    "Key Note Instance UID",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290001,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00290001,
    'DS',
    "Zoom Rectangle",
    '1-n')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x00290001,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x00290001,
    'LT',
    "Image Enhancement",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;3",
    0x00290001,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00290001,
    'US',
    "Convolution Kernel Size",
    '2')
add_private_dict_entry(
    "MEDIFACE",
    0x00290001,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "1.2.840.113663.1",
    0x00290001,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290001,
    'IS',
    "Slice Number",
    '1')
add_private_dict_entry(
    "HOLOGIC",
    0x00290001,
    'UL',
    "Graph Bitmap Size",
    '1')
add_private_dict_entry(
    "Hologic",
    0x00290001,
    'UL',
    "Graph Bitmap Size",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290001,
    'FD',
    "Image Compression Fraction",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290001,
    'LO',
    "Window Width",
    '1')
add_private_dict_entry(
    "MITRA OBJECT DOCUMENT 1.0",
    0x00290001,
    'OB',
    "IMPAX Markup XML Stored",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290001,
    'OB',
    "Markup2",
    '1-n')
add_private_dict_entry(
    "SCHICK TECHNOLOGIES - Image Security Creator ID",
    0x00290001,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SECTRA_ImageInfo_01",
    0x00290001,
    'OB',
    "Image info",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290001,
    'CS',
    "Presentation Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290001,
    'FD',
    "Translucent Window Size",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO FUNCTION ASSIGNMENT",
    0x00290001,
    'LO',
    "Data Reference",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO TIME POINT SERVICE",
    0x00290001,
    'LO',
    "Time Point ID",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL MEASUREMENT",
    0x00290001,
    'ST',
    "Oncology Measurement Recist Standard",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290001,
    'US',
    "Valid CT Volume MBox Tasks",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00290001,
    'US',
    "Convolution Kernel Size",
    '2')
add_private_dict_entry(
    "SIEMENS IKM CKS CXRCAD FINDINGS",
    0x00290001,
    'UT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS IKM CKS LUNGCAD BMK",
    0x00290001,
    'UT',
    "?",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00290001,
    'SQ',
    "Data Frame Assignment Sequence",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00290001,
    'IS',
    "Storage State",
    '1')
add_private_dict_entry(
    "PMTF INFORMATION DATA",
    0x00290001,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290002,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x00290002,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x00290002,
    'LT',
    "Convolution ID",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00290002,
    'US',
    "Convolution Kernel Coefficients",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00290002,
    'IS',
    "Phase Number",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290002,
    'FD',
    "Image Quality",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290002,
    'LO',
    "Window Centre",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290002,
    'OB',
    "Markup3",
    '1-n')
add_private_dict_entry(
    "SECTRA_ImageInfo_01",
    0x00290002,
    'CS',
    "Marking",
    '1')
add_private_dict_entry(
    "SHS MagicView 300",
    0x00290002,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO TIME POINT SERVICE",
    0x00290002,
    'LO',
    "Time Point Information",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290002,
    'LT',
    "Scan Options",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290002,
    'SQ',
    "Advanced Presentation Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290002,
    'US',
    "Panoramic Mode",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00290002,
    'US',
    "Convolution Kernel Coefficients",
    '1-n')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00290002,
    'CS',
    "Data Path Assignment",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00290002,
    'IS',
    "Referenced Image SOP Class",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00290003,
    'DS',
    "Zoom Factor",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00290003,
    'FL',
    "Edge Enhancement Gain",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x00290003,
    'LT',
    "Convolution Type",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x00290003,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290003,
    'LO',
    "Proc Type",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290003,
    'FD',
    "Image Bytes Transferred",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290003,
    'IS',
    "Invert",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290003,
    'OB',
    "Markup4",
    '1-n')
add_private_dict_entry(
    "SECTRA_ImageInfo_01",
    0x00290003,
    'LO',
    "No decompression",
    '1')
add_private_dict_entry(
    "SHS MagicView 300",
    0x00290003,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290003,
    'FD',
    "Panoramic Inner Width",
    '1')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x00290003,
    'FL',
    "Edge Enhancement Gain",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290003,
    'SQ',
    "Time Point Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290003,
    'ST',
    "Acquisition Date and Time",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00290003,
    'US',
    "Bits Mapped to Color Lookup Table",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00290003,
    'IS',
    "Referenced Image Instance UID",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x00290004,
    'LT',
    "Convolution Kernel Size ID",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x00290004,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;2",
    0x00290004,
    'UN',
    "Masking Function",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290004,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00290004,
    'US',
    "Zoom Function",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290004,
    'SL',
    "Lower Range Of Pixels",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290004,
    'LO',
    "Stopwatch Time",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290004,
    'IS',
    "Has Tabstop",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290004,
    'OB',
    "Markup5",
    '1-n')
add_private_dict_entry(
    "SECTRA_ImageInfo_01",
    0x00290004,
    'OB',
    "Image info new",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x00290004,
    'CS',
    "Photometric Interpretation",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290004,
    'SQ',
    "Base Image Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290004,
    'ST',
    "Acquisition Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290004,
    'US',
    "Display Unseen Areas",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00290004,
    'SQ',
    "Opacity 1 LUT Sequence",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00290004,
    'IS',
    "Related Presentation State Number",
    '1')
add_private_dict_entry(
    "TELEMIS",
    0x00290004,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x00290005,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x00290005,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x00290005,
    'US',
    "Convolution Kernel Size",
    '2')
add_private_dict_entry(
    "3DHISTECH REGION MAPS",
    0x00290005,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290005,
    'DS',
    "Lower Range Of Pixels",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290005,
    'LO',
    "Plane",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290005,
    'CS',
    "Smooth Rotation",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290005,
    'OB',
    "Markup6",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290005,
    'SQ',
    "Overlay Image Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290005,
    'ST',
    "Dynamic Data",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290005,
    'US',
    "Unseen Areas Color",
    '4')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00290005,
    'CS',
    "Opacity 1 LUT Transfer Function",
    '1')
add_private_dict_entry(
    "SVISION",
    0x00290005,
    'IS',
    "Related Presentation State UID",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x00290006,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x00290006,
    'US',
    "Convolution Kernel",
    '1-n')
add_private_dict_entry(
    "3DHISTECH REGION MAPS",
    0x00290006,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290006,
    'DS',
    "Lower Range Of Pixels",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290006,
    'LO',
    "Scan Time",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290006,
    'OB',
    "Markup7",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290006,
    'DS',
    "Image Orientation Patient",
    '6')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290006,
    'SQ',
    "Registration Instance Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290006,
    'US',
    "Display Tagged Data",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00290006,
    'FD',
    "Opacity Constant",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290007,
    'SL',
    "Lower Range Of Pixels",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290007,
    'OB',
    "Markup8",
    '1-n')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290007,
    'LT',
    "Frame Of Reference Uid",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290007,
    'SQ',
    "Real World Value Mapping Instance Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290007,
    'US',
    "Tagged Color",
    '4')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00290007,
    'US',
    "Opacity Lookup Table Descriptor",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290008,
    'SH',
    "Lower Range Of Pixels",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290008,
    'LO',
    "Dual Slice Flag",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290008,
    'OB',
    "Markup9",
    '1-n')
add_private_dict_entry(
    "SIEMENS CSA HEADER",
    0x00290008,
    'CS',
    "CSA Image Header Type",
    '1')
add_private_dict_entry(
    "SIEMENS CSA NON-IMAGE",
    0x00290008,
    'CS',
    "CSA Data Type",
    '1')
add_private_dict_entry(
    "SIEMENS CSA REPORT",
    0x00290008,
    'CS',
    "Report Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00290008,
    'CS',
    "Modality Image Header Type",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290008,
    'CS',
    "MedCom Header Type",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM OOG",
    0x00290008,
    'CS',
    "MedCom OOG Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290008,
    'LT',
    "Patient Position",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290008,
    'SQ',
    "Measurement Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO 3D FUSION MATRIX",
    0x00290008,
    'UI',
    "Object Series Instance UID",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290008,
    'UL',
    "Tagged Sample Thickness",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00290008,
    'OW',
    "Opacity Lookup Table Data",
    '1')
add_private_dict_entry(
    "TOSHIBA COMAPL HEADER",
    0x00290008,
    'CS',
    "COMAPL Header Type",
    '1')
add_private_dict_entry(
    "TOSHIBA COMAPL OOG",
    0x00290008,
    'CS',
    "COMAPL OOG Type",
    '1')
add_private_dict_entry(
    "TOSHIBA MDW HEADER",
    0x00290008,
    'CS',
    "Image Header Type",
    '1')
add_private_dict_entry(
    "TOSHIBA MDW NON-IMAGE",
    0x00290008,
    'CS',
    "Non-Image Header Type",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290009,
    'SH',
    "Lower Range Of Pixels",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290009,
    'LO',
    "SSP Ratio",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290009,
    'OB',
    "Markup10",
    '1-n')
add_private_dict_entry(
    "SIEMENS CSA HEADER",
    0x00290009,
    'LO',
    "CSA Image Header Version",
    '1')
add_private_dict_entry(
    "SIEMENS CSA NON-IMAGE",
    0x00290009,
    'LO',
    "CSA Data Version",
    '1')
add_private_dict_entry(
    "SIEMENS CSA REPORT",
    0x00290009,
    'LO',
    "Report Version",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00290009,
    'LO',
    "Modality Image Header Version",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290009,
    'LO',
    "MedCom Header Version",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM OOG",
    0x00290009,
    'LO',
    "MedCom OOG Version",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290009,
    'LT',
    "Convolution Kernel",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290009,
    'SL',
    "Tagged Threshold",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO 3D FUSION MATRIX",
    0x00290009,
    'UI',
    "Model Series Instance UID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290009,
    'UI',
    "Measurement UID",
    '1')
add_private_dict_entry(
    "TOSHIBA COMAPL HEADER",
    0x00290009,
    'LO',
    "COMAPL Header Version",
    '1')
add_private_dict_entry(
    "TOSHIBA COMAPL OOG",
    0x00290009,
    'LO',
    "COMAPL OOG Version",
    '1')
add_private_dict_entry(
    "TOSHIBA MDW HEADER",
    0x00290009,
    'LO',
    "Image Header Version",
    '1')
add_private_dict_entry(
    "TOSHIBA MDW NON-IMAGE",
    0x00290009,
    'LO',
    "Non-Image Header Version",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x0029000a,
    'SS',
    "Lower Range Of Pixels",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029000a,
    'LO',
    "Gating Signal Source",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0029000B,
    'SQ',
    "Enhanced Palette Color Lookup Table Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029000b,
    'LO',
    "Rephase",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0029000C,
    'SQ',
    "Opacity 2 LUT Sequence",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x0029000c,
    'DS',
    "Enhancement Gain",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;2",
    0x0029000c,
    'UN',
    "Proprietary Masking Parameters",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029000c,
    'LO',
    "Half Echo",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0029000D,
    'CS',
    "Opacity 2 LUT Transfer Function",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029000d,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029000d,
    'LO',
    "Rect FOV Ratio",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0029000E,
    'CS',
    "Data Path ID",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x0029000e,
    'CS',
    "Zoom Enable Status",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029000e,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029000e,
    'LO',
    "Half Scan",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x0029000F,
    'CS',
    "RGB LUT Transfer Function",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x0029000f,
    'CS',
    "Zoom Select Status",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x0029000f,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029000f,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029000f,
    'LO',
    "Num Shots",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290010,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290010,
    'DS',
    "FP Min",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290010,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00290010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_CDS Release 1",
    0x00290010,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290010,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MEDIFACE",
    0x00290010,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "3DHISTECH REGION MAPS",
    0x00290010,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290010,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "CAMTRONICS IP",
    0x00290010,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "CAMTRONICS",
    0x00290010,
    'LT',
    "Commentline",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x00290010,
    'UL',
    "Shift Count",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290010,
    'LO',
    "Contrast Agent",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290010,
    'CS',
    "J2c Parameter Type",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290010,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290010,
    'OB',
    "Markup11",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x00290010,
    'US',
    "Rows of Submatrix",
    '1')
add_private_dict_entry(
    "SIEMENS MED HG",
    0x00290010,
    'US',
    "List of Group Numbers",
    '1')
add_private_dict_entry(
    "SIEMENS MED MG",
    0x00290010,
    'US',
    "List of Group Numbers",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290010,
    'CS',
    "Window Style",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL MEASUREMENT",
    0x00290010,
    'CS',
    "DualEnergy ROI Annotation Mode",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO PRINT SERVICE",
    0x00290010,
    'IS',
    "Sheet Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290010,
    'LT',
    "Kvp",
    '1')
add_private_dict_entry(
    "SIEMENS CSA ENVELOPE",
    0x00290010,
    'OB',
    "syngo Report Data",
    '1')
add_private_dict_entry(
    "SIEMENS CSA HEADER",
    0x00290010,
    'OB',
    "CSA Image Header Info",
    '1')
add_private_dict_entry(
    "SIEMENS CSA NON-IMAGE",
    0x00290010,
    'OB',
    "CSA Data Info",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00290010,
    'OB',
    "Modality Image Header Info",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290010,
    'OB',
    "MedCom Header Info",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM OOG",
    0x00290010,
    'OB',
    "MedCom OOG Info",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290010,
    'SQ',
    "Segmentation Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO FRAME SET",
    0x00290010,
    'SQ',
    "Image Frame Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO 3D FUSION MATRIX",
    0x00290010,
    'UI',
    "Matrix Referenced Series Instance UID",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL PRESENTATION",
    0x00290010,
    'US',
    "Kernel Filter",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00290010,
    'CS',
    "Alpha LUT Transfer Function",
    '1')
add_private_dict_entry(
    "TOSHIBA COMAPL HEADER",
    0x00290010,
    'OB',
    "COMAPL Header Info",
    '1')
add_private_dict_entry(
    "TOSHIBA COMAPL OOG",
    0x00290010,
    'OB',
    "COMAPL OOG Info",
    '1')
add_private_dict_entry(
    "TOSHIBA MDW HEADER",
    0x00290010,
    'OB',
    "Image Header Info",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290011,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290011,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290011,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "MEDIFACE",
    0x00290011,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "AgilityRuntime",
    0x00290011,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290011,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290011,
    'LO',
    "Echo Allocation",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290011,
    'US',
    "J2c Pixel Representation",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290011,
    'IS',
    "Annotation Name",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290011,
    'IS',
    "Line Name",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290011,
    'IS',
    "ROI Name",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290011,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290011,
    'OB',
    "Markup12",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x00290011,
    'US',
    "Columns of Submatrix",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290011,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290011,
    'LT',
    "Reconstruction Diameter",
    '1')
add_private_dict_entry(
    "SIEMENS CSA ENVELOPE",
    0x00290011,
    'OB',
    "syngo Report Presentation",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290011,
    'UI',
    "Segmentation UID",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290012,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290012,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290012,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "AgilityRuntime",
    0x00290012,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290012,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x00290012,
    'UL',
    "Offset",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290012,
    'LO',
    "Num Echo Shift",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290012,
    'US',
    "J2c Bits Allocated",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290012,
    'LT',
    "Annotation Font",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290012,
    'LT',
    "Line Name Font",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290012,
    'LT',
    "ROI Name Font",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290012,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290012,
    'OB',
    "Markup13",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO FRAME SET",
    0x00290012,
    'CS',
    "Type of Progression",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290012,
    'LT',
    "Rescale Intercept",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290012,
    'SQ',
    "Navigation Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290012,
    'US',
    "Slices",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290013,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "AgilityRuntime",
    0x00290013,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290013,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290013,
    'LO',
    "Fat Sat",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290013,
    'US',
    "J2c Pixel Shift Value",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290013,
    'LT',
    "Annotation Text Foreground Color",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290013,
    'LT',
    "ROI Normal Color",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290013,
    'UL',
    "Line Name Display",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290013,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290013,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "MITRA PRESENTATION 1.0",
    0x00290013,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290013,
    'OB',
    "Markup14",
    '1-n')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290013,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290013,
    'CS',
    "Navigation Name",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290013,
    'LT',
    "Rescale Slope",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290014,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "AgilityRuntime",
    0x00290014,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ShowcaseAppearance",
    0x00290014,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x00290014,
    'UL',
    "Actual Frame Number",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290014,
    'LO',
    "MTC",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290014,
    'US',
    "J2c Planar Configuration",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290014,
    'LT',
    "Annotation Text Background Color",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290014,
    'LT',
    "Line Normal Color",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290014,
    'UL',
    "ROI Fill Pattern",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290014,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290014,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "MITRA MARKUP 1.0",
    0x00290014,
    'OB',
    "Markup14",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290014,
    'CS',
    "Auto Navigation Direction",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO FRAME SET",
    0x00290014,
    'IS',
    "Representation Level",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290014,
    'LT',
    "Slice Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290014,
    'OB',
    "Volume Histogram",
    '1')
add_private_dict_entry(
    "Kodak Image Information",
    0x00290015,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "CARESTREAM IMAGE INFORMATION",
    0x00290015,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290015,
    'SL',
    "Lower Range Of Pixels1",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290015,
    'LO',
    "Num Pre Sat",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290015,
    'DS',
    "J2c Rescale Intercept",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290015,
    'UL',
    "Annotation Text Backing Mode",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290015,
    'UL',
    "Line Type",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290015,
    'UL',
    "ROI Bp Seg",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290015,
    'DS',
    "Auto Navigation Frame Rate",
    '1')
add_private_dict_entry(
    "SIEMENS MED HG",
    0x00290015,
    'LO',
    "List of Shadow Owner Codes",
    '1')
add_private_dict_entry(
    "SIEMENS MED MG",
    0x00290015,
    'LO',
    "List of Shadow Owner Codes",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290015,
    'LT',
    "Table Height",
    '1')
add_private_dict_entry(
    "SIEMENS CSA REPORT",
    0x00290015,
    'US',
    "SR Variant",
    '1')
add_private_dict_entry(
    "Kodak Image Information",
    0x00290016,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "CARESTREAM IMAGE INFORMATION",
    0x00290016,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290016,
    'SL',
    "Upper Range Of Pixels1",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290016,
    'LO',
    "Target Velocity",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290016,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290016,
    'UL',
    "Annotation Text Justification",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290016,
    'UL',
    "Line Thickness",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290016,
    'UN',
    "ROI Bp Seg Pairs",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290016,
    'CS',
    "Auto Navigation Mode",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290016,
    'LT',
    "Gantry Detector Tilt",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO FRAME SET",
    0x00290016,
    'SQ',
    "Representation Information Sequence",
    '1')
add_private_dict_entry(
    "Kodak Image Information",
    0x00290017,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "CARESTREAM IMAGE INFORMATION",
    0x00290017,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290017,
    'SL',
    "Lower Range Of Pixels2",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290017,
    'LO',
    "VENC Axis",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290017,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290017,
    'UL',
    "Annotation Text Location",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290017,
    'UL',
    "Line Style",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290017,
    'UL',
    "ROI Seed Space",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290017,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290017,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290017,
    'DS',
    "Auto Navigation Realtime Speed",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290017,
    'LT',
    "Pixel Spacing",
    '1')
add_private_dict_entry(
    "SIEMENS CSA REPORT",
    0x00290017,
    'UI',
    "SC SOP Instance UID",
    '1')
add_private_dict_entry(
    "Kodak Image Information",
    0x00290018,
    'UT',
    "?",
    '1')
add_private_dict_entry(
    "CARESTREAM IMAGE INFORMATION",
    0x00290018,
    'UT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290018,
    'SL',
    "Upper Range Of Pixels2",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290018,
    'LO',
    "Num VENC Direction",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290018,
    'LT',
    "Annotation Text String",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290018,
    'UL',
    "Line Dash Length",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290018,
    'UN',
    "ROI Seeds",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290018,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290018,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CSA HEADER",
    0x00290018,
    'CS',
    "CSA Series Header Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290018,
    'CS',
    "Auto Navigation Strategy",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO FRAME SET",
    0x00290018,
    'IS',
    "Number of Representations",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290018,
    'IS',
    "Volume Level",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290018,
    'ST',
    "Volume PatientPosition Not Equal",
    '1')
add_private_dict_entry(
    "TOSHIBA MDW HEADER",
    0x00290018,
    'CS',
    "Series Header Type",
    '1')
add_private_dict_entry(
    "Kodak Image Information",
    0x00290019,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "CARESTREAM IMAGE INFORMATION",
    0x00290019,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290019,
    'UL',
    "Annotation Text Attach Mode",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290019,
    'UL',
    "Line Interactivity",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290019,
    'UL',
    "ROI Line Thickness",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290019,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290019,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290019,
    'CS',
    "Auto Navigation Realtime Flag",
    '1')
add_private_dict_entry(
    "SIEMENS CSA HEADER",
    0x00290019,
    'LO',
    "CSA Series Header Version",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290019,
    'ST',
    "Volume LossyImageCompression Not Equal",
    '1')
add_private_dict_entry(
    "TOSHIBA MDW HEADER",
    0x00290019,
    'LO',
    "Series Header Version",
    '1')
add_private_dict_entry(
    "Kodak Image Information",
    0x0029001a,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "CARESTREAM IMAGE INFORMATION",
    0x0029001a,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x0029001a,
    'SL',
    "Length Of Total Header In Bytes",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x0029001a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x0029001a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029001b,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "CARESTREAM IMAGE INFORMATION",
    0x0029001b,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x0029001b,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x0029001b,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029001c,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029001c,
    'LO',
    "Is Scalable Window Level",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x0029001c,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x0029001c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029001d,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029001d,
    'LO',
    "Three D Setting Line Angle",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x0029001d,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x0029001d,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;2",
    0x0029001e,
    'CS',
    "Subtraction Mask Enable Status",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x0029001e,
    'CS',
    "Image Enhancement Enable Status",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029001e,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029001e,
    'LO',
    "MPG Total Axis",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x0029001e,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x0029001e,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;2",
    0x0029001f,
    'CS',
    "Subtraction Mask Select Status",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;3",
    0x0029001f,
    'CS',
    "Image Enhancement Select Status",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x0029001f,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "AgilityRuntime",
    0x0029001f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AgilityRuntime",
    0x0029001f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029001f,
    'LO',
    "MPG Axis Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290020,
    'DS',
    "FP Max",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290020,
    'DS',
    "Pixel Aspect Ratio",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x00290020,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290020,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290020,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290020,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "MEDIFACE",
    0x00290020,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "3DHISTECH ZOOMLEVEL REGION MAP",
    0x00290020,
    'UL',
    "?",
    '2')
add_private_dict_entry(
    "CAMTRONICS",
    0x00290020,
    'DS',
    "Edge Enhancement Coefficient",
    '1')
add_private_dict_entry(
    "CAMTRONICS IP",
    0x00290020,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "2.16.840.1.114059.1.1.6.1.50.1",
    0x00290020,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "FOEM 1.0",
    0x00290020,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00290020,
    'CS',
    "Image Scanning Direction",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290020,
    'IS',
    "Multi Echo Number",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290020,
    'LO',
    "MD5Sum",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290020,
    'LT',
    "Line Measurement Color",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290020,
    'UL',
    "Annotation Text Cursor Mode",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290020,
    'UL',
    "ROI Line Style",
    '1')
add_private_dict_entry(
    "SIEMENS MED HG",
    0x00290020,
    'US',
    "List of Element Numbers",
    '1')
add_private_dict_entry(
    "SIEMENS MED MG",
    0x00290020,
    'US',
    "List of Element Numbers",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290020,
    'CS',
    "Pixel Quality Code",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290020,
    'IS',
    "Index Navigation Current Index",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO FRAME SET",
    0x00290020,
    'IS',
    "Representation Pixel Offset",
    '1')
add_private_dict_entry(
    "SIEMENS CSA HEADER",
    0x00290020,
    'OB',
    "CSA Series Header Info",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290020,
    'OB',
    "MedCom History Information",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290020,
    'ST',
    "Volume ConvolutionKernel Not Equal",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x00290020,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "TOSHIBA COMAPL HEADER",
    0x00290020,
    'OB',
    "COMAPL History Information",
    '1')
add_private_dict_entry(
    "TOSHIBA MDW HEADER",
    0x00290020,
    'OB',
    "Series Header Info",
    '1')
add_private_dict_entry(
    "TOSHIBA MDW NON-IMAGE",
    0x00290020,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290021,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x00290021,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290021,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MEDIFACE",
    0x00290021,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "2.16.840.1.114059.1.1.6.1.50.1",
    0x00290021,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290021,
    'DS',
    "Navi Average Gate Width",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290021,
    'US',
    "Histogram Percentile Labels",
    '1-n')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290021,
    'LT',
    "Line Measurement Font",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290021,
    'UL',
    "Annotation Text Shadow Offset X",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290021,
    'UL',
    "ROI Line Dash Length",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290021,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290021,
    'IS',
    "Index Auto Navigation Skipping Degree",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290021,
    'ST',
    "Volume PixelSpacing Not Equal",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x00290021,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290022,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MEDIFACE",
    0x00290022,
    'DS',
    "?",
    '2')
add_private_dict_entry(
    "2.16.840.1.114059.1.1.6.1.50.1",
    0x00290022,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290022,
    'ST',
    "Shim Compensate Value",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS",
    0x00290022,
    'FD',
    "Histogram Percentile Values",
    '1-n')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290022,
    'UL',
    "Annotation Text Shadow Offset Y",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290022,
    'UL',
    "Line Measurement Dash Length",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290022,
    'UL',
    "ROI Interactivity",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290022,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290022,
    'IS',
    "Pixel Quality Value",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290022,
    'DS',
    "Volume Navigation Minimum Pixel Spacing",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290022,
    'ST',
    "Volume Kvp Not Equal",
    '1')
add_private_dict_entry(
    "2.16.840.1.114059.1.1.6.1.50.1",
    0x00290023,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290023,
    'LO',
    "GC Offset",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290023,
    'LT',
    "Annotation Line Color",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290023,
    'UL',
    "Line Point Space",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290023,
    'UL',
    "ROI Name Position",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290023,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290023,
    'CS',
    "Volume Navigation Scroll Unit",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290023,
    'ST',
    "Volume ReconstructionDiameter Not Equal",
    '1')
add_private_dict_entry(
    "2.16.840.1.114059.1.1.6.1.50.1",
    0x00290024,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290024,
    'DS',
    "Navi Max Gate Width",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290024,
    'FD',
    "Line Points",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290024,
    'UL',
    "Annotation Line Thickness",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290024,
    'UL',
    "ROI Name Display",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290024,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "RadWorksMarconi",
    0x00290024,
    'US',
    "Key Frame Indices",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290024,
    'DS',
    "Volume Navigation Step Size",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290024,
    'ST',
    "Volume TableHeight Not Equal",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290025,
    'LO',
    "Processed Pixel Data Quality",
    '1-n')
add_private_dict_entry(
    "2.16.840.1.114059.1.1.6.1.50.1",
    0x00290025,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00290025,
    'CS',
    "Image Rotation/Reversal Information",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290025,
    'DS',
    "Navi Min Gate Width",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290025,
    'LT',
    "ROI Label",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290025,
    'UL',
    "Annotation Line Type",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290025,
    'UL',
    "Line Control Point Size",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290025,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290025,
    'DS',
    "Volume Navigation Jump Size",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290025,
    'ST',
    "Volume Has Gaps",
    '1')
add_private_dict_entry(
    "2.16.840.1.114059.1.1.6.1.50.1",
    0x00290026,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290026,
    'SS',
    "Version Of Header Structure",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290026,
    'DS',
    "Navi Max Gate Position",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290026,
    'UL',
    "Annotation Line Style",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290026,
    'UL',
    "Line Control Point Space",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290026,
    'UL',
    "ROI Shape",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290026,
    'IS',
    "Referenced Registration Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290026,
    'ST',
    "Volume Number Of Missing Images",
    '1')
add_private_dict_entry(
    "2.16.840.1.114059.1.1.6.1.50.1",
    0x00290027,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290027,
    'DS',
    "Navi Min Gate Position",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290027,
    'FD',
    "Line Control Points",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290027,
    'FD',
    "ROI Shape Tilt",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290027,
    'UL',
    "Annotation Line Dash Length",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290027,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290027,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290027,
    'ST',
    "Volume Max Gap",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290027,
    'UI',
    "Real World Value Mapping UID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290028,
    'DS',
    "Time Duration",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290028,
    'LT',
    "Line Label",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290028,
    'UL',
    "Annotation Line Attach Mode",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290028,
    'UL',
    "ROI Shape Points Count",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290028,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290028,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290028,
    'DS',
    "Channel Alpha Value",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290028,
    'LT',
    "Volume Position Of Gaps",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290029,
    'DS',
    "Table Position",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290029,
    'UL',
    "Annotation Line Point Count",
    '1')
add_private_dict_entry(
    "Silhouette Line V1.0",
    0x00290029,
    'UL',
    "Line Don't Save",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290029,
    'UL',
    "ROI Shape Points Space",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290029,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290029,
    'FD',
    "Calibration Factor",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x0029002A,
    'CS',
    "Flash Mode",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029002a,
    'DS',
    "Navi Initial Gate Width",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x0029002B,
    'LT',
    "Warnings",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029002b,
    'DS',
    "Navi Final Gate Width",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x0029002C,
    'ST',
    "Volume HighBit Not Equal",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029002c,
    'DS',
    "Navi Initial Gate Position",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x0029002D,
    'ST',
    "Volume ImageType Not Equal",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029002d,
    'DS',
    "Navi Final Gate Position",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x0029002E,
    'ST',
    "ImageType 0",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029002e,
    'DS',
    "Navi Average Gate Position",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x0029002F,
    'ST',
    "ImageType 1",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x0029002f,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029002f,
    'OB',
    "Image App Data",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290030,
    'DS',
    "Scaled Minimum",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290030,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290030,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x00290030,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00290030,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "MEDIFACE",
    0x00290030,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "CAMTRONICS IP",
    0x00290030,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00290030,
    'CS',
    "Extended Reading Size Value",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290030,
    'FD',
    "Diffusion BValue",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290030,
    'FD',
    "Annotation Line Points",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290030,
    'FD',
    "ROI Shape Points",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290030,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290030,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED HG",
    0x00290030,
    'US',
    "List of Total Display Length",
    '1')
add_private_dict_entry(
    "SIEMENS MED MG",
    0x00290030,
    'US',
    "List of Total Display Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290030,
    'DS',
    "Voxel Spacing",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290030,
    'LO',
    "Measurement Application Name",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290030,
    'ST',
    "ImageType 2",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290031,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290031,
    'DS',
    "?",
    '2')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00290031,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290031,
    'SQ',
    "Shared Functional Groups Sequence",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290031,
    'UL',
    "Annotation Line Control Size",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290031,
    'UL',
    "ROI Shape Control Points Count",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290031,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SEGAMI_HEADER",
    0x00290031,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "DIGISCAN IMAGE",
    0x00290031,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290031,
    'LO',
    "PMTF Information 1",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290031,
    'SQ',
    "Measurement Data Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290031,
    'ST',
    "ImageType 3",
    '1')
add_private_dict_entry(
    "PMTF INFORMATION DATA",
    0x00290031,
    'LO',
    "PMTF Information 1",
    '1')
add_private_dict_entry(
    "TOSHIBA COMAPL HEADER",
    0x00290031,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x00290032,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290032,
    'DS',
    "?",
    '2')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00290032,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290032,
    'SQ',
    "Per Frame Functional Groups Sequence",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290032,
    'LT',
    "Annotation Marker Color",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290032,
    'UL',
    "ROI Shape Control Points Space",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290032,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SEGAMI_HEADER",
    0x00290032,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "DIGISCAN IMAGE",
    0x00290032,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290032,
    'DS',
    "Volume Position (Patient)",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290032,
    'LO',
    "Measurement Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290032,
    'ST',
    "PhotometricInterpretation not MONOCHROME2",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290032,
    'UL',
    "PMTF Information 2",
    '1')
add_private_dict_entry(
    "PMTF INFORMATION DATA",
    0x00290032,
    'UL',
    "PMTF Information 2",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00290033,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290033,
    'DS',
    "Lossy Image Compression Ratio",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290033,
    'FD',
    "ROI Shape Control Points",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290033,
    'UL',
    "Annotation Marker Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290033,
    'DA',
    "First Acquisition Date",
    '1')
add_private_dict_entry(
    "DIGISCAN IMAGE",
    0x00290033,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290033,
    'UI',
    "Measurement Frame of Reference UID",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290033,
    'UL',
    "PMTF Information 3",
    '1')
add_private_dict_entry(
    "PMTF INFORMATION DATA",
    0x00290033,
    'UL',
    "PMTF Information 3",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00290034,
    'US',
    "Mag./Reduc. Ratio",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290034,
    'SL',
    "Advantage Comp Overflow",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290034,
    'UI',
    "Instance Creator UID",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290034,
    'UL',
    "Annotation Marker Size",
    '1')
add_private_dict_entry(
    "Silhouette ROI V1.0",
    0x00290034,
    'UL',
    "ROI Don't Save",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290034,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290034,
    'CS',
    "PMTF Information 4",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290034,
    'DA',
    "Last Acquisition Date",
    '1')
add_private_dict_entry(
    "DIGISCAN IMAGE",
    0x00290034,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290034,
    'UI',
    "Measurement UID",
    '1')
add_private_dict_entry(
    "PMTF INFORMATION DATA",
    0x00290034,
    'CS',
    "PMTF Information 4",
    '1')
add_private_dict_entry(
    "TOSHIBA COMAPL HEADER",
    0x00290034,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "3DHISTECH ZOOMLEVEL REGION MAP",
    0x00290035,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_IMPS_01",
    0x00290035,
    'SL',
    "Advantage Comp Underflow",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290035,
    'UI',
    "Related General SOPClass UID",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290035,
    'FD',
    "Annotation Marker Location",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290035,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290035,
    'IS',
    "Measurement Application Number",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290035,
    'TM',
    "First Acquisition Time",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290035,
    'UL',
    "PMTF Information 5",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290036,
    'UI',
    "Original Specialized SOPClass UID",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290036,
    'UL',
    "Annotation Marker Attach Mode",
    '1')
add_private_dict_entry(
    "Silhouette VRS 3.0",
    0x00290036,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290036,
    'ST',
    "Measurement Application Number Prefix Text",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290036,
    'TM',
    "Last Acquisition Time",
    '1')
add_private_dict_entry(
    "3DHISTECH ZOOMLEVEL REGION MAP",
    0x00290037,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290037,
    'SH',
    "Timezone Offset From UTC",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290037,
    'LT',
    "Annotation Geom Color",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290037,
    'CS',
    "Measurement Graphic Is Visible Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290037,
    'DS',
    "Volume Orientation (Patient)",
    '9')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290037,
    'ST',
    "Internal Data",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290038,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "3DHISTECH ZOOMLEVEL REGION MAP",
    0x00290038,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290038,
    'CS',
    "SOPInstance Status",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290038,
    'UL',
    "Annotation Geom Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290038,
    'ST',
    "Ranges SOM7",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290038,
    'UI',
    "Referenced Syngo UID",
    '4')
add_private_dict_entry(
    "MMCPrivate",
    0x00290039,
    'DT',
    "SOPAuthorization Dateand Time",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290039,
    'UL',
    "Annotation Geom Line Style",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290039,
    'LT',
    "Calculated Gantry Detector Tilt",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290039,
    'UI',
    "Clinical Finding UID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029003A,
    'CS',
    "Measurement Evaluation String Value",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029003a,
    'LT',
    "SOPAuthorization Comment",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029003B,
    'IS',
    "Measurement Evaluation Integer Value",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029003b,
    'LO',
    "Authorization Equipment Certification Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029003C,
    'FL',
    "Measurement Evaluation Decimal Value",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029003c,
    'UL',
    "Concatenation Frame Offset Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029003D,
    'CS',
    "Measurement Line Show Center Flag",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029003d,
    'US',
    "Representative Frame Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029003E,
    'CS',
    "Measurement Angle Show ArrowTip Flag",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029003e,
    'UI',
    "Concatenation UID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029003F,
    'SQ',
    "Camera Home Settings Sequence",
    '1')
add_private_dict_entry(
    "SPI-P-XSB-VISUB Release 1",
    0x0029003f,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029003f,
    'US',
    "In Concatenation Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290040,
    'DS',
    "Scaled Maximum",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00290040,
    'LT',
    "Magnifying Glass ID",
    '1')
add_private_dict_entry(
    "3DHISTECH ZOOMLEVEL REGION MAP",
    0x00290040,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "CAMTRONICS IP",
    0x00290040,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290040,
    'CS',
    "Cardiac Synchronization Technique",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290040,
    'UL',
    "Annotation Geom Dash Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290040,
    'CS',
    "Resampling Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290040,
    'DS',
    "Camera Zoom",
    '1')
add_private_dict_entry(
    "SIEMENS MED HG",
    0x00290040,
    'LO',
    "List of Display Prefix",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED MG",
    0x00290040,
    'LO',
    "List of Display Prefix",
    '1-n')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290040,
    'SQ',
    "Application Header Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290040,
    'ST',
    "Volume Slice Distance",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00290041,
    'DS',
    "Magnifying Glass Rectangle",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00290041,
    'CS',
    "Cardiac Signal Source",
    '1')
add_private_dict_entry(
    "Silhouette Sequence Ids V1.0",
    0x00290041,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290041,
    'UL',
    "Annotation Geom Fill Pattern",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290041,
    'CS',
    "Application Header Type",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290041,
    'DS',
    "First Slice Z Coordinate ",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290041,
    'DS',
    "Camera Position",
    '3')
add_private_dict_entry(
    "MMCPrivate",
    0x00290042,
    'FD',
    "Cardiac RRInterval Specified",
    '1')
add_private_dict_entry(
    "Silhouette Sequence Ids V1.0",
    0x00290042,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290042,
    'UL',
    "Annotation Interactivity",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290042,
    'CS',
    "Normalization Flag",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290042,
    'DS',
    "Last Slice Z Coordinate ",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290042,
    'DS',
    "Camera Orientation",
    '4')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290042,
    'LO',
    "Application Header ID",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00290043,
    'DS',
    "Magnifying Glass Factor",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290043,
    'CS',
    "Cardiac Beat Rejection Technique",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290043,
    'FD',
    "Annotation Arrow Length",
    '1')
add_private_dict_entry(
    "Silhouette Sequence Ids V1.0",
    0x00290043,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290043,
    'DS',
    "Content DateTime",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290043,
    'DS',
    "Camera Far Clip Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290043,
    'LO',
    "Application Header Version",
    '1')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x00290044,
    'US',
    "Magnifying Glass Function",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00290044,
    'CS',
    "Line Density Code",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290044,
    'IS',
    "Low RR Value",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290044,
    'FD',
    "Annotation Arrow Angle",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290044,
    'DS',
    "Delta Time",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290044,
    'DS',
    "Camera Near Clip Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290044,
    'OB',
    "Application Header Info",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290044,
    'SQ',
    "SubVolume Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290045,
    'IS',
    "High RR Value",
    '1')
add_private_dict_entry(
    "Silhouette Annot V1.0",
    0x00290045,
    'UL',
    "Annotation Don't Save",
    '1')
add_private_dict_entry(
    "SIEMENS CT APPL DATASET",
    0x00290045,
    'DS',
    "Frame Count",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290045,
    'DS',
    "Camera Thickness",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290046,
    'IS',
    "Intervals Acquired",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290046,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290046,
    'DS',
    "Camera ViewPort Size",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290046,
    'UL',
    "Histogram Number Of Bins",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290047,
    'IS',
    "Intervals Rejected",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290047,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290047,
    'DS',
    "Camera Aspect Ratio",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO VOLUME",
    0x00290047,
    'OB',
    "Volume Histogram Data",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290048,
    'CS',
    "Respiratory Motion Compensation Technique",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290048,
    'LO',
    "Camera Projection Type",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290049,
    'CS',
    "Respiratory Signal Source",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290049,
    'DS',
    "Camera Field of View",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029004A,
    'DS',
    "Camera Image Plane Distance",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029004a,
    'CS',
    "Bulk Motion Compensation Technique",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029004B,
    'DS',
    "Camera Image Maximum Height",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029004b,
    'CS',
    "Bulk Motion Signal Source",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029004C,
    'DS',
    "Camera Image Minimum Height",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029004c,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029004c,
    'CS',
    "Pixel Presentation",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029004D,
    'DS',
    "Parallel Shift Interval MM",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029004d,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029004d,
    'CS',
    "Volumetric Properties",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029004E,
    'DS',
    "Parallel Shift BoundingBox Minimum",
    '3')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x0029004e,
    'CS',
    "Magnifying Glass Enable Status",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029004e,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029004e,
    'CS',
    "Volume Based Calculation Technique",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029004F,
    'DS',
    "Parallel Shift BoundingBox Maximum",
    '3')
add_private_dict_entry(
    "SPI-P Release 1;1",
    0x0029004f,
    'CS',
    "Magnifying Glass Select Status",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029004f,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029004f,
    'ST',
    "Acquisition Context Description",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;5",
    0x00290050,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290050,
    'DS',
    "Window Minimum",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290050,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290050,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "3DHISTECH ZOOMLEVEL REGION MAP",
    0x00290050,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "CAMTRONICS",
    0x00290050,
    'LT',
    "Scene Text",
    '1')
add_private_dict_entry(
    "FDMS 1.0",
    0x00290050,
    'CS',
    "Data Compression Code",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290050,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x00290050,
    'US',
    "Origin of Submatrix",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290050,
    'CS',
    "Archive Code",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290050,
    'CS',
    "Renderer Vertex Is Characteristic Flag",
    '1')
add_private_dict_entry(
    "SIEMENS MED HG",
    0x00290050,
    'LO',
    "List of Display Postfix",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED MG",
    0x00290050,
    'LO',
    "List of Display Postfix",
    '1-n')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290050,
    'LO',
    "Workflow Control Flags",
    '8')
add_private_dict_entry(
    "SIEMENS SYNGO TIME POINT SERVICE",
    0x00290050,
    'SQ',
    "Studies in Time Point Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290051,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290051,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290051,
    'LO',
    "LUTDescriptor",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290051,
    'CS',
    "Exposure Code",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290051,
    'CS',
    "Archive Management Flag Keep Online",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290051,
    'CS',
    "Renderer Thickness Usage Flag",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290052,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290052,
    'LO',
    "LUTExplanation",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290052,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290052,
    'IS',
    "Sort Code",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290052,
    'CS',
    "Archive Management Flag Do Not Archive",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290052,
    'DS',
    "Renderer Threshold",
    '4')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x00290053,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290053,
    'LO',
    "LUTData",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290053,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290053,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290053,
    'CS',
    "Image Location Status",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290053,
    'DS',
    "Renderer Material",
    '4')
add_private_dict_entry(
    "MMCPrivate",
    0x00290054,
    'CS',
    "Presentation LUT Shape",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290054,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290054,
    'DS',
    "Estimated Retrieve Time",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290054,
    'DS',
    "Renderer DirectionalLight Color",
    '4')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;5",
    0x00290055,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290055,
    'SQ',
    "Frame Anatomy Sequence",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290055,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290055,
    'DS',
    "Data Size of Retrieved Images",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290055,
    'DS',
    "Renderer DirectionalLight Direction",
    '3')
add_private_dict_entry(
    "MMCPrivate",
    0x00290056,
    'CS',
    "Frame Laterality",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290056,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290056,
    'CS',
    "Renderer DirectionalLight TwoSide Usage Flag",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290057,
    'SQ',
    "Anatomic Region Sequence",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290057,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290057,
    'SQ',
    "Renderer PWL TransferFunction Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290058,
    'SH',
    "Anatomic Region Code Value",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290058,
    'IS',
    "Renderer PWL Vertex Index",
    '0-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00290059,
    'SH',
    "Anatomic Region Coding Scheme Designator",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290059,
    'DS',
    "Renderer PWL Vertex Color",
    '0-n')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029005A,
    'CS',
    "Renderer Is Camera Required Flag",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029005a,
    'SH',
    "Anatomic Region Coding Scheme Version",
    '1')
add_private_dict_entry(
    "SIEMENS MED MAMMO",
    0x0029005a,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029005B,
    'CS',
    "Renderer Do Depth Test Flag ",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029005b,
    'LO',
    "Anatomic Region Code Meaning",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029005C,
    'CS',
    "Renderer Directional Light Usage Flag",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029005c,
    'SQ',
    "Pixel Value Transformation Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029005D,
    'SQ',
    "Renderer Thickness Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029005d,
    'LO',
    "Rescale Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029005E,
    'SQ',
    "Renderer Slice Spacing Sequence",
    '0-n')
add_private_dict_entry(
    "MMCPrivate",
    0x0029005e,
    'SQ',
    "Cardiac Synchronization Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029005F,
    'DS',
    "Renderer Sampling Distance",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029005f,
    'FD',
    "Trigger Delay Time",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290060,
    'DS',
    "Window Maximum",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290060,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "CAMTRONICS",
    0x00290060,
    'LT',
    "Image Text",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290060,
    'SQ',
    "Frame VOILUTSequence",
    '1')
add_private_dict_entry(
    "SPI RELEASE 1",
    0x00290060,
    'LO',
    "Compression Algorithm",
    '1')
add_private_dict_entry(
    "SPI Release 1",
    0x00290060,
    'LO',
    "Compression Algorithm",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00290060,
    'LO',
    "Splash",
    '1')
add_private_dict_entry(
    "SIEMENS MED HG",
    0x00290060,
    'US',
    "List of Text Position",
    '1')
add_private_dict_entry(
    "SIEMENS MED MG",
    0x00290060,
    'US',
    "List of Text Position",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290060,
    'DS',
    "Renderer Initial Sampling Distance",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER2",
    0x00290060,
    'LO',
    "Series Work Flow Status",
    '1')
add_private_dict_entry(
    "SPI",
    0x00290060,
    'LO',
    "Compression Algorithm",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290061,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290061,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "3DHISTECH ZOOMLEVEL REGION MAP",
    0x00290061,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290061,
    'LO',
    "Window Center and Width Explanation",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290061,
    'SQ',
    "Segmentation Display Data Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290062,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290062,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290062,
    'UI',
    "Segmentation Display Data UID",
    '0-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00290063,
    'SQ',
    "MRModifier Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290063,
    'SQ',
    "Segmentation Display Parameter Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290064,
    'CS',
    "Parallel Acquisition Technique",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290064,
    'LO',
    "Segmentation Display Parameter Type",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290065,
    'FD',
    "Parallel Reduction Factor Sec In",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290065,
    'LO',
    "Segmentation Display Visibility",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290066,
    'CS',
    "Inversion Recovery",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290066,
    'DS',
    "Segmentation Display Color",
    '4')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290067,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290067,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290067,
    'CS',
    "Flow Compensation",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290067,
    'CS',
    "Segmentation Display is Selected Flag ",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290068,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290068,
    'CS',
    "Flow Compensation Direction",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290068,
    'OB',
    "Segmentation Additional Information Blob",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290069,
    'CS',
    "Spatial PreSaturation",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290069,
    'ST',
    "Hash Code Value",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029006A,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029006A,
    'LO',
    "Segmentation Version Identifier",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x0029006a,
    'CS',
    "Partial Fourier",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x0029006B,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029006b,
    'CS',
    "Partial Fourier Direction",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290070,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290070,
    'LT',
    "Window ID",
    '1')
add_private_dict_entry(
    "3DHISTECH ZOOMLEVEL REGION MAP",
    0x00290070,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "CAMTRONICS",
    0x00290070,
    'IS',
    "Pixel Shift Horizontal",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290070,
    'SQ',
    "MR Receive Coil Sequence",
    '1')
add_private_dict_entry(
    "ISG shadow",
    0x00290070,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290070,
    'DS',
    "Segmentation Volume Size",
    '3')
add_private_dict_entry(
    "SIEMENS MED HG",
    0x00290070,
    'LO',
    "List of Text Concatenation",
    '1')
add_private_dict_entry(
    "SIEMENS MED MG",
    0x00290070,
    'LO',
    "List of Text Concatenation",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290070,
    'SQ',
    "Siemens Link Sequence",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290071,
    'CS',
    "Video Invert Subtracted",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290071,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290071,
    'LO',
    "Receive Coil Manufacturer Name",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290071,
    'AT',
    "Referenced Tag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290071,
    'UI',
    "Registration Referenced Frames",
    '1-n')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290072,
    'CS',
    "Video Invert Nonsubtracted",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290072,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290072,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290072,
    'CS',
    "Receive Coil Type",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290072,
    'CS',
    "Referenced Tag Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290072,
    'UI',
    "Registration Referenced Registrations",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00290073,
    'CS',
    "Quadrature Receive Coil",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290073,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290073,
    'LO',
    "Registration Creation Algorithm Name",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290073,
    'UL',
    "Referenced Value Length",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290074,
    'LO',
    "Multi Coil Configuration",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290074,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290074,
    'CS',
    "Referenced Object Device Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290074,
    'CS',
    "ECG Graphic Type",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290075,
    'CS',
    "Complex Image Component",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290075,
    'OB',
    "Referenced Object Device Location",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290076,
    'SH',
    "Pulse Sequence Name",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290076,
    'OB',
    "Referenced Object ID",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290077,
    'CS',
    "Window Select Status",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290077,
    'CS',
    "Echo Pulse Sequence",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290077,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MEDCOM HEADER",
    0x00290077,
    'UL',
    "Referenced Object Offset",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290078,
    'LT',
    "ECG Display Printing ID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290078,
    'CS',
    "Multiple Spin Echo",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290078,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290079,
    'CS',
    "ECG Display Printing",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290079,
    'CS',
    "Multi Planar Excitation",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029007A,
    'DS',
    "Segmentation Volume Storage Data Type",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029007a,
    'CS',
    "Phase Contrast",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029007B,
    'FL',
    "Segmentation Volume Model Matrix",
    '16')
add_private_dict_entry(
    "MMCPrivate",
    0x0029007b,
    'CS',
    "Time of Flight Contrast",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029007c,
    'CS',
    "Steady State Pulse Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029007d,
    'CS',
    "Echo Planar Pulse Sequence",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x0029007e,
    'CS',
    "ECG Display Printing Enable Status",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029007e,
    'CS',
    "Spectrally Selected Suppression",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x0029007f,
    'CS',
    "ECG Display Printing Select Status",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029007f,
    'CS',
    "Oversampling Phase",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290080,
    'IS',
    "View Center",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00290080,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290080,
    'LT',
    "Physiological Display ID",
    '1')
add_private_dict_entry(
    "CAMTRONICS",
    0x00290080,
    'IS',
    "Pixel Shift Vertical",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290080,
    'CS',
    "Segmented KSpace Traversal",
    '1')
add_private_dict_entry(
    "ISG shadow",
    0x00290080,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x00290080,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290080,
    'DS',
    "Camera Rotation Axis",
    '3')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290081,
    'IS',
    "View Size",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290081,
    'US',
    "Preferred Physiological Channel Display",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290081,
    'CS',
    "Coverage of KSpace",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290081,
    'SL',
    "Overlay Hidden Display Attributes",
    '0-n')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290082,
    'IS',
    "View Zoom",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290082,
    'SQ',
    "MR Timing and Related Parameters Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290082,
    'LO',
    "Presentation State Group Identifier",
    '1')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00290083,
    'IS',
    "View Transform",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290083,
    'US',
    "RF Echo Train Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290083,
    'US',
    "Temporary Smallest Image Pixel Value",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290084,
    'US',
    "Gradient Echo Train Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290084,
    'DS',
    "Camera Rotation Center",
    '3')
add_private_dict_entry(
    "MMCPrivate",
    0x00290085,
    'CS',
    "Gradient Output Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290085,
    'CS',
    "Camera Rotation Center Usage Flag",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290086,
    'FD',
    "Gradient Output",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290086,
    'DS',
    "Camera Parallel Epiped",
    '12')
add_private_dict_entry(
    "MMCPrivate",
    0x00290087,
    'SQ',
    "MRFOVGeometry Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290087,
    'DS',
    "Camera Max Zoom In Factor",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290088,
    'US',
    "MRAcquisition Frequency Encoding Steps",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290088,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290088,
    'DS',
    "Camera Min Zoom In Factor",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290089,
    'US',
    "MRAcquisition Phase Encoding Steps In Plane",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290089,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290089,
    'US',
    "Temporary Largest Image Pixel Value",
    '1')
add_private_dict_entry(
    "PMTF INFORMATION DATA",
    0x00290089,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029008A,
    'CS',
    "Camera Rotation Axis Usage Flag",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029008a,
    'US',
    "MRAcquisitionPhase Encoding Steps Out of Plane",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029008B,
    'DS',
    "Measurement Surface Normal",
    '3')
add_private_dict_entry(
    "MMCPrivate",
    0x0029008b,
    'SQ',
    "MR Transmit Coil Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029008C,
    'FL',
    "Measurement Ellipsoid Model Matrix",
    '16')
add_private_dict_entry(
    "MMCPrivate",
    0x0029008c,
    'SH',
    "Transmit Coil Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029008D,
    'LO',
    "Measurement Evaluation DataRole ID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029008d,
    'LO',
    "Transmit Coil Manufacturer Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029008E,
    'LO',
    "Measurement Algorithm Type",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x0029008e,
    'CS',
    "Physiological Display Enable Status",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029008e,
    'CS',
    "Transmit Coil Type",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x0029008f,
    'CS',
    "Physiological Display Select Status",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029008f,
    'SQ',
    "MR Echo Sequence",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290090,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x00290090,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "CAMTRONICS",
    0x00290090,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290090,
    'FD',
    "Effective Echo Time",
    '1')
add_private_dict_entry(
    "ISG shadow",
    0x00290090,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290090,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "PMTF INFORMATION DATA",
    0x00290090,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1",
    0x00290091,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x00290091,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290091,
    'SQ',
    "MR Metabolite Map Sequence",
    '1')
add_private_dict_entry(
    "Silhouette V1.0",
    0x00290091,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290091,
    'SQ',
    "Measurement Evaluation DataRole Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290092,
    'ST',
    "Metabolite Map Description",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290092,
    'CS',
    "Measurement Evaluation DataRole Item",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290093,
    'SQ',
    "Metabolite Map Code Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290093,
    'SQ',
    "Measurement Evaluation Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290094,
    'SH',
    "Metabolite Map Code Value",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290094,
    'DS',
    "Measurement Evaluation Value",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290095,
    'SH',
    "Metabolite Map Coding Scheme Designator",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290095,
    'CS',
    "Measurement Evaluation ID",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290096,
    'SH',
    "Metabolite Map Coding Scheme Version",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290096,
    'FL',
    "Measurement Data Points",
    '0-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00290097,
    'LO',
    "Metabolite Map Code Meaning",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290097,
    'FL',
    "Measurement Data Angles",
    '0-n')
add_private_dict_entry(
    "MMCPrivate",
    0x00290098,
    'SQ',
    "MR Imaging Modifier Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290098,
    'LO',
    "Measurement Data Slice",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x00290099,
    'CS',
    "Magnetization Transfer",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY 0000",
    0x00290099,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x00290099,
    'LO',
    "Shutter Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY 0001",
    0x00290099,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x00290099,
    'FL',
    "Measurement Data Slice Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029009A,
    'SQ',
    "Measurement Referenced Frames Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029009a,
    'CS',
    "Blood Signal Nulling",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029009B,
    'DS',
    "Measurement Evaluation Longest Distance",
    '0-n')
add_private_dict_entry(
    "MMCPrivate",
    0x0029009b,
    'CS',
    "Tagging",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029009C,
    'DS',
    "Measurement Evaluation Centroid",
    '0-n')
add_private_dict_entry(
    "MMCPrivate",
    0x0029009c,
    'FD',
    "Tag Spacing First Dimension",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029009D,
    'FL',
    "Measurement Data Bounding Box ",
    '6')
add_private_dict_entry(
    "MMCPrivate",
    0x0029009d,
    'FD',
    "Tag Spacing Second Dimension",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029009E,
    'LO',
    "Measurement Text",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029009e,
    'FD',
    "Tag Angle First Axis",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x0029009F,
    'IS',
    "Measurement Diameter",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x0029009f,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x0029009f,
    'SS',
    "Tag Angle Second Axis",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900A0,
    'DS',
    "Image Rotation Fractional",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900a0,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x002900a0,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a0,
    'FD',
    "Tag Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x002900a0,
    'US',
    "Rows of Rectangular Shutter",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY 0001",
    0x002900a0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900A1,
    'LO',
    "Preset Name",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x002900a1,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900a1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a1,
    'FD',
    "Tagging Delay",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x002900a1,
    'US',
    "Columns of Rectangular Shutter",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY 0001",
    0x002900a1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900A2,
    'SQ',
    "Fusion LUT Sequence",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x002900a2,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a2,
    'FD',
    "Transmitter Frequency",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x002900a2,
    'US',
    "Origin of Rectangular Shutter",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY 0001",
    0x002900a2,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900A3,
    'CS',
    "Fusion LUT Is Active Flag",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x002900a3,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a3,
    'DS',
    "Pixel Bandwidth",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a4,
    'SQ',
    "MRVelocity Encoding Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900A5,
    'UI',
    "Syngo UID",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x002900a5,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a5,
    'FD',
    "Velocity Encoding Direction",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900A6,
    'UI',
    "Presentation Version Identifier",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x002900a6,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a6,
    'FD',
    "Velocity Encoding Minimum Value",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900A7,
    'SQ',
    "Presentation Module Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a7,
    'FD',
    "Velocity Encoding Maximum Value",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900A8,
    'LO',
    "Presentation Module Type",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a8,
    'SQ',
    "MR Image Frame Type Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900A9,
    'SQ',
    "Presentation State Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900a9,
    'CS',
    "Frame Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900AA,
    'CS',
    "LUT Inverted Flag",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900aa,
    'CS',
    "Pixel Presentation",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900AB,
    'IS',
    "Softcopy VOI LUT Viewing Index",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900ab,
    'CS',
    "Volumetric Properties",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900AC,
    'FD',
    "Displayed Area Bottom Right Hand Corner Fractional",
    '2')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x002900AC,
    'FL',
    "Displayed Area Bottom Right Hand Corner Fractional",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900ac,
    'CS',
    "Volume Based Calculation Technique",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900AD,
    'FD',
    "Displayed Area Top Left Hand Corner Fractional",
    '2')
add_private_dict_entry(
    "CARDIO-D.R. 1.0",
    0x002900AD,
    'FL',
    "Displayed Area Top Left Hand Corner Fractional",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900ad,
    'IS',
    "Filmed Count",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900AE,
    'FL',
    "Measurement Alpha",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900ae,
    'LO',
    "Is Transferred",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900AF,
    'OB',
    "Measurement Bitmap",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900af,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900af,
    'LO',
    "Is Archived",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900B0,
    'US',
    "Current Frame Number",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900b0,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b0,
    'LO',
    "MPPS Step Status",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x002900b0,
    'US',
    "Radius of Circular Shutter",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY 0000",
    0x002900b0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900B1,
    'LO',
    "Image Text View Name",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900b1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b1,
    'LO',
    "Commitment Status",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900B2,
    'SQ',
    "Image Text View Content Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b2,
    'LO',
    "Is Storage Committed",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x002900b2,
    'US',
    "Origin of Circular Shutter",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY 0000",
    0x002900b2,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900B3,
    'LO',
    "Image Text Line Names",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b3,
    'LO',
    "Is Dicom",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900B4,
    'LO',
    "ImageText Line Values",
    '1-n')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b4,
    'LO',
    "Is Allow Cascade Save",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900B5,
    'SQ',
    "Measurement Evaluation Text Position Sequence",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b5,
    'LO',
    "Is Allow Cascade Protect",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900B6,
    'CS',
    "Measurement Link Evaluation Text Flag",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b6,
    'LO',
    "Is Deleted",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900B7,
    'DS',
    "Measurement Evaluation Text Position Vector",
    '3')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b7,
    'OB',
    "Application Data",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900B8,
    'OB',
    "Image Text Alpha Blending Line Value",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b8,
    'LO',
    "Is Allow Cascade Save",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900b9,
    'LO',
    "Is Allow Cascade Protect",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900ba,
    'LO',
    "Is Deleted",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900bb,
    'IS',
    "VOI 1",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900bc,
    'IS',
    "VOI 2",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900bd,
    'DS',
    "Mixing Time",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900be,
    'FD',
    "Selective IR Position",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900bf,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900bf,
    'FD',
    "Selective IR Row",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900c0,
    'LT',
    "Functional Shutter ID",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900c0,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900c0,
    'FD',
    "Selective IR Column",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900C1,
    'SQ',
    "Task Data Sequence",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900c1,
    'US',
    "Field Of Shutter",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900c1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900c1,
    'FD',
    "Selective IR Orientation",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY",
    0x002900c1,
    'US',
    "Contour of Irregular Shutter",
    '1')
add_private_dict_entry(
    "SIEMENS MED DISPLAY 0000",
    0x002900c1,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900C2,
    'CS',
    "Task Data Type",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900c2,
    'DS',
    "Selective IR Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900C3,
    'LO',
    "Task Data Version",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x002900c3,
    'IS',
    "Scan Resolution",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900c3,
    'CS',
    "Rephase Order Slice",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900C4,
    'ST',
    "Task Data Description",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x002900c4,
    'IS',
    "Field of View",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900c4,
    'CS',
    "Rephase Order Phase",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900C5,
    'OB',
    "Task Data",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900c5,
    'LT',
    "Field Of Shutter Rectangle",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900c5,
    'CS',
    "Rephase Order Freq",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900C6,
    'IS',
    "Task Data Size",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900C9,
    'SQ',
    "Clip Plane Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900CA,
    'DS',
    "Clip Plane Center",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900CB,
    'DS',
    "Clip Plane Normal",
    '3')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900cb,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900CC,
    'DS',
    "Clip Plane Scale",
    '2')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900cc,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900CD,
    'CS',
    "Clip Plane Use Thickness Flag",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900cd,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900CE,
    'DS',
    "Clip Plane Thickness",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900ce,
    'CS',
    "Shutter Enable Status",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900CF,
    'SQ',
    "Image Sequence",
    '1')
add_private_dict_entry(
    "SPI-P Release 1",
    0x002900cf,
    'CS',
    "Shutter Select Status",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900D0,
    'CS',
    "Clip Plane Enable Clip",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x002900d0,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900d0,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900d0,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900D1,
    'DS',
    "Clip Plane Handle Ratio",
    '1')
add_private_dict_entry(
    "SPI-P-GV-CT Release 1",
    0x002900d1,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900d1,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900D2,
    'DS',
    "Clip Plane Bounding Points",
    '24')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900d2,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900D3,
    'DS',
    "Clip Plane Motion Matrix",
    '16')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900d3,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900d3,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900D4,
    'DS',
    "Clip Plane Shift Velocity",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900d4,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900D5,
    'CS',
    "Clip Plane Enabled Flag",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900d5,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR/PART",
    0x002900d5,
    'LT',
    "Slice Thickness",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900d5,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900D6,
    'DS',
    "Clip Plane Rotate Velocity",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;4",
    0x002900d6,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;1",
    0x002900d6,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900d6,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900D7,
    'CS',
    "Clip Plane Show Graphics Flag",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;4",
    0x002900d7,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "MMCPrivate",
    0x002900d7,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;4",
    0x002900d8,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;4",
    0x002900d9,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;2",
    0x002900d9,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;4",
    0x002900da,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;4",
    0x002900dc,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;4",
    0x002900dd,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900E0,
    'DS',
    "Crop Box Size",
    '3')
add_private_dict_entry(
    "SPI-P-Private_ICS Release 1;4",
    0x002900e0,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900E1,
    'CS',
    "Crop Box Enabled Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900E2,
    'DS',
    "Crop Box Absolute Origin",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900E3,
    'CS',
    "Crop Box Show Graphics Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900F1,
    'DS',
    "Curved Camera Coordinates",
    '0-n')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900F2,
    'DS',
    "Curved Camera Point of Interest",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900F3,
    'CS',
    "Curved Camera Point of Interest Usage Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900F4,
    'DS',
    "Curved Camera Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900F5,
    'DS',
    "Curved Camera Extrusion Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900F6,
    'CS',
    "Curved Camera Rotation Axis Mode",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900F7,
    'DS',
    "Curved Camera Roll Rotation Axis",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900F8,
    'DS',
    "Curved Camera View Port Height",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900F9,
    'DS',
    "Curved Camera Cut Direction",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900FA,
    'DS',
    "Curved Camera Pan Vector",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900FB,
    'LO',
    "Clinical Finding ID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900FC,
    'CS',
    "Measurement Is Circle Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ADVANCED PRESENTATION",
    0x002900FD,
    'LO',
    "Measurement Application Type ID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "AGFA PACS Archive Mirroring 1.0",
    0x00310000,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310001,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "AGFA PACS Archive Mirroring 1.0",
    0x00310001,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310001,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310003,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310004,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310005,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310005,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310007,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310008,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310008,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310009,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310009,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031000a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031000a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031000b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031000c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031000c,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0031000c,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031000d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031000e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031000e,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031000f,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0031000f,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310010,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310010,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00310010,
    'LO',
    "Request UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310010,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310010,
    'SQ',
    "SOP Class Packing Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310010,
    'UI',
    "Internal Patient UID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310011,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310011,
    'PN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310011,
    'SH',
    "Patients Death Indicator",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310012,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310012,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310012,
    'DA',
    "Patients Death Date",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00310012,
    'LO',
    "Examination Reason",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310012,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310013,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310013,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310013,
    'TM',
    "Patients Death Time",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310014,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310014,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310014,
    'SH',
    "VIP Indicator",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310014,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310015,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310015,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310015,
    'SL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310015,
    'US',
    "Emergency Flag",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310016,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310016,
    'SL',
    "?",
    '1-n')
add_private_dict_entry(
    "KONICA1.0",
    0x00310017,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310017,
    'SS',
    "?",
    '1-n')
add_private_dict_entry(
    "KONICA1.0",
    0x00310018,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310019,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031001a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031001a,
    'PN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031001b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031001b,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031001c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031001c,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031001d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031001e,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310020,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "MITRA LINKED ATTRIBUTES 1.0",
    0x00310020,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310020,
    'CS',
    "Packing Version",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310020,
    'SH',
    "Internal Visit UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310020,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310021,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310021,
    'PN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310021,
    'CS',
    "Packing Originator",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00310021,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310022,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310022,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310023,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310023,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310024,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310024,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310025,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310025,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310025,
    'SH',
    "Internal ISR UID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310026,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310026,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310027,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310027,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310028,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310028,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310029,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310029,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031002a,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031002a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031002b,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031002b,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031002c,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031002c,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031002d,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x0031002d,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031002e,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031002f,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00310030,
    'DA',
    "Requested Date",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310030,
    'UI',
    "Original SOP Class UID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310031,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310031,
    'UI',
    "Original Study Instance UID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310032,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "NUMACALC-INVENTORY",
    0x00310032,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00310032,
    'TM',
    "Worklist Request Start Time",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310032,
    'SH',
    "Control State",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310032,
    'UI',
    "Original Series Instance UID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310033,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00310033,
    'TM',
    "Worklist Request End Time",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310033,
    'UI',
    "Original SOP Instance UID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310034,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310034,
    'UI',
    "Original Transfer Syntax UID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310034,
    'US',
    "Local Flag",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310035,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310036,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310036,
    'UI',
    "Referenced Studies",
    '1-n')
add_private_dict_entry(
    "KONICA1.0",
    0x00310037,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310038,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310039,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031003a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031003b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031003c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031003d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031003e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031003f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310040,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310040,
    'AT',
    "Attributes to Set to Zero Length",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310040,
    'LO',
    "Workflow ID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310041,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310041,
    'AT',
    "Attributes to Remove",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310041,
    'LO',
    "Workflow Description",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310042,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310042,
    'LO',
    "Workflow Control State",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310043,
    'US',
    "Workflow Ad Hoc Flag",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310044,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310044,
    'US',
    "Hybrid Flag",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310045,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00310045,
    'LO',
    "Requesting Physician",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310046,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310047,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310048,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310049,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031004a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x0031004a,
    'TM',
    "Requested Time",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031004b,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031004c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031004d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031004e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031004f,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310050,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00310050,
    'LO',
    "Requested Physician",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310050,
    'LO',
    "Workitem ID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310050,
    'US',
    "Original Rows",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310051,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310051,
    'LO',
    "Workitem Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310051,
    'US',
    "Original Columns",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310052,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310052,
    'LO',
    "Workitem Type",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310053,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310053,
    'LO',
    "Workitem Roles",
    '1-n')
add_private_dict_entry(
    "KONICA1.0",
    0x00310054,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310054,
    'LO',
    "Workitem Description",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310055,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310055,
    'LO',
    "Workitem Control State",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310056,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310056,
    'LO',
    "Claiming User",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310057,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310057,
    'LO',
    "Claiming Host",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310058,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310058,
    'CS',
    "Original Image Type",
    '2-n')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310058,
    'LO',
    "Taskflow ID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310059,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310059,
    'LO',
    "Taskflow Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x0031005A,
    'US',
    "Failed Flag",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031005a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x0031005B,
    'DT',
    "Scheduled Time",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031005b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x0031005C,
    'US',
    "Workitem Ad Hoc Flag",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031005c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x0031005D,
    'US',
    "Patient Update Pending Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x0031005E,
    'US',
    "Patient Mixup Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310060,
    'CS',
    "Original Modality",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310060,
    'LO',
    "Client ID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310061,
    'LO',
    "Template ID",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310062,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310063,
    'US',
    "?",
    '3')
add_private_dict_entry(
    "KONICA1.0",
    0x0031006b,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310070,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310070,
    'SQ',
    "Sequence of Original StreamCchunks",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310071,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310071,
    'AT',
    "Start Tag of a Stream Chunk",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310072,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310072,
    'AT',
    "End Tag of a Stream Chunk",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310073,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310073,
    'CS',
    "Stream Chunk is a Payload",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310074,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310075,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310077,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310078,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310079,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031007a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031007b,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031007c,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031007d,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031007e,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031007f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310080,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00310080,
    'LO',
    "Requested Location",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO SOP CLASS PACKING",
    0x00310080,
    'OB',
    "Stream Chunk",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310081,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310081,
    'LO',
    "Institution Name",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310082,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310082,
    'ST',
    "Institution Address",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310083,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO WORKFLOW",
    0x00310083,
    'SQ',
    "Institution Code Sequence",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310084,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310085,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310086,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310087,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310088,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310089,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031008a,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031008b,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031008c,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031008d,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031008e,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x0031008f,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310090,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310091,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310092,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310093,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310094,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x00310095,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SEGAMI MIML",
    0x00310098,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100a1,
    'IS',
    "?",
    '2')
add_private_dict_entry(
    "KONICA1.0",
    0x003100a2,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100a5,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100a6,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100a7,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100a8,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100aa,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100ab,
    'DA',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100ac,
    'TM',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100ad,
    'DA',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100ae,
    'TM',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b2,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b3,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b5,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b6,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b7,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b8,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100b9,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100ba,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100bc,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100be,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100bf,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c0,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c1,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c2,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c3,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c4,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c5,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c6,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c7,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c8,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100c9,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100ca,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100cb,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100cc,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100cd,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100ce,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100cf,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d0,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d1,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d2,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d3,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d4,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d5,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d6,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d7,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d8,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100d9,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100da,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100db,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100dc,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100dd,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100de,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100df,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100e0,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100e1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100e2,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100e3,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100e4,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100e5,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100e6,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100f0,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "KONICA1.0",
    0x003100ff,
    'SQ',
    "Private Data Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330000,
    'FL',
    "Flood Correction Matrix Detector 1",
    '1-n')
add_private_dict_entry(
    "GEMS_GNHD_01",
    0x00330001,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330001,
    'FL',
    "Flood Correction Matrix Detector 2",
    '1-n')
add_private_dict_entry(
    "GEMS_CTHD_01",
    0x00330002,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GNHD_01",
    0x00330002,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT ATTRIBUTES 1.0",
    0x00330002,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x00330002,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x00330004,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT ATTRIBUTES 1.0",
    0x00330004,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_YMHD_01",
    0x00330005,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_YMHD_01",
    0x00330006,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT ATTRIBUTES 1.0",
    0x00330006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x00330006,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330007,
    'LO',
    "Original SOP Instance UID",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330008,
    'CS',
    "eNTEGRA Data Object Type",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330008,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT ATTRIBUTES 1.0",
    0x00330008,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x00330008,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT ATTRIBUTES 1.0",
    0x0033000a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x0033000a,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x0033000c,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x0033000e,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330010,
    'SL',
    "Modified",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330010,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330010,
    'FL',
    "COR Data for Detector 1",
    '1-n')
add_private_dict_entry(
    "SIEMENS RIS",
    0x00330010,
    'LO',
    "Patient Study UID",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330011,
    'LO',
    "Name",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330011,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330011,
    'FL',
    "COR Data for Detector 2",
    '1-n')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x00330013,
    'PN',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x00330014,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330014,
    'FL',
    "MHR (Y-Shift) data for detector 1",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x00330015,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330015,
    'FL',
    "MHR (Y-Shift) data for detector 2",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330016,
    'LO',
    "Protocol Data UID",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330016,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x00330016,
    'PN',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330017,
    'SH',
    "Date",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330017,
    'DA',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330018,
    'SH',
    "Time",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330018,
    'TM',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330018,
    'FL',
    "NCO Data for detector 1",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330019,
    'UL',
    "Protocol Data Flags",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330019,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "MITRA OBJECT UTF8 ATTRIBUTES 1.0",
    0x00330019,
    'PN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330019,
    'FL',
    "NCO Data for detector 2",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0033001A,
    'FL',
    "?",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0033001a,
    'UL',
    "Protocol Name",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x0033001a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0033001b,
    'LO',
    "Relevant Data UID",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x0033001b,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0033001c,
    'LO',
    "Bulk Data",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x0033001c,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0033001d,
    'SL',
    "Int Data",
    '1-n')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x0033001d,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0033001e,
    'FD',
    "Double Data",
    '1-n')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x0033001e,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x0033001f,
    'OB',
    "String Data",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x0033001f,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330020,
    'LT',
    "Bulk Data Format",
    '1-n')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330020,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330020,
    'FL',
    "Bed correction angle",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330021,
    'LT',
    "Int Data Format",
    '1-n')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330021,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330021,
    'FL',
    "Gantry correction angle",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330022,
    'LT',
    "Double Data Format",
    '1-n')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330022,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330022,
    'SS',
    "Bed U/D correction data",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330023,
    'LT',
    "String Data Format",
    '1-n')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330023,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330023,
    'SS',
    "Gantry L/R Correction Data",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330024,
    'LT',
    "Description",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330024,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330024,
    'FL',
    "BackProjection Correction angle head 1",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330025,
    'FL',
    "BackProjection Correction angle head 2",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330028,
    'SL',
    "MHR calibrations",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330029,
    'FL',
    "Crystal thickness",
    '1-n')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330030,
    'UL',
    "Allocate Trigger Buffer",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330030,
    'LO',
    "Preset name used for acquisition",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330031,
    'FL',
    "Camera Config Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330032,
    'LO',
    "Crystal Type",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330033,
    'UL',
    "Number of Triggers",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330033,
    'SL',
    "Coin Gantry Step",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330034,
    'UL',
    "Trigger Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330034,
    'FL',
    "Wholebody bed step",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330035,
    'UL',
    "Trigger Data Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330035,
    'FL',
    "Weight Factor Table For Coincidence Acquisitions",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00330036,
    'OB',
    "Trigger Data",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330036,
    'FL',
    "Coincidence weight factor table",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330037,
    'SL',
    "Starburst flags at image acq time",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00330038,
    'FL',
    "Pixel Scale factor",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330070,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330071,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_XELPRV_01",
    0x00330072,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SEGAMI__PAGE",
    0x00330097,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "SEGAMI__PAGE",
    0x00330098,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "AGFA KOSD 1.0",
    0x00350000,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00350000,
    'LO',
    "Specialized Tomo Type",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00350001,
    'FD',
    "Start Angle",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00350001,
    'LO',
    "Energy Window Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00350002,
    'SS',
    "Start and End Row Illuminated By Wind Position",
    '1')
add_private_dict_entry(
    "AGFA KOSD 1.0",
    0x00350003,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00350003,
    'LO',
    "Blank Scan Image For Profile",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00350004,
    'SS',
    "Repeat Number of the Original Dynamic SPECT",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00350005,
    'SS',
    "Phase Number of the Original Dynamic SPECT",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00350006,
    'LO',
    "Siemens Profile 2 Image Subtype",
    '1')
add_private_dict_entry(
    "SEGAMI__MEMO",
    0x00350097,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SEGAMI__MEMO",
    0x00350098,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00370000,
    'OW',
    "Flood correction matrix Detector 1",
    '1')
add_private_dict_entry(
    "MAROTECH Inc.",
    0x00370001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DRS_1",
    0x00370010,
    'LO',
    "ReferringDepartment",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370010,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x0037001b,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DRS_1",
    0x00370020,
    'US',
    "ScreenNumber",
    '1')
add_private_dict_entry(
    "MAROTECH Inc.",
    0x00370021,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MAROTECH Inc.",
    0x00370022,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "MAROTECH Inc.",
    0x00370023,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370030,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DRS_1",
    0x00370040,
    'SH',
    "LeftOrientation",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370040,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DRS_1",
    0x00370042,
    'SH',
    "RightOrientation",
    '1')
add_private_dict_entry(
    "GEMS_DRS_1",
    0x00370050,
    'CS',
    "Inversion",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370050,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_DRS_1",
    0x00370060,
    'US',
    "DSA",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370060,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370070,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370071,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370072,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370073,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370078,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00370080,
    'OW',
    "Flood correction matrix Detector 2",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370090,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00370092,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00390000,
    'LT',
    "Toshiba CBF Activity Results",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390000,
    'UN',
    "Release Version",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00390001,
    'LT',
    "Related CT Series Instance UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED OCS PUBLIC RT PLAN ATTRIBUTES",
    0x00390001,
    'UT',
    "External Attributes",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390003,
    'UN',
    "Volume Acquisition Duration",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390004,
    'UN',
    "Volume Raw Data Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390005,
    'UN',
    "Scan Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390006,
    'UN',
    "Z Lateral Min",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390007,
    'UN',
    "Z Lateral Span",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390008,
    'UN',
    "Z Radius of Curvature",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390009,
    'UN',
    "Wobble Correction",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390010,
    'UN',
    "Scale Along Width",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390011,
    'UN',
    "Scale Along Height",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390012,
    'UN',
    "Scale Along Depth",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390013,
    'UN',
    "Buffer Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390014,
    'UN',
    "Acquisition Rate",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390015,
    'UN',
    "Depth Min cm",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390016,
    'UN',
    "Is Left Right Flipped Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390017,
    'UN',
    "Is Up Down Flipped Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390018,
    'UN',
    "Is Volume Geom Accurate",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390019,
    'UN',
    "BByte Mask Offset",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390020,
    'UN',
    "BByte Mask Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390022,
    'UN',
    "Acq Plane Rotation Deg",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390023,
    'UN',
    "Beam Axial Span",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390024,
    'UN',
    "Beam Lateral Min",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390025,
    'UN',
    "Beam Lateral Span",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390026,
    'UN',
    "Beam Axial Min",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390027,
    'UN',
    "Num Display Samples",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390028,
    'UN',
    "DVolume Width",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390029,
    'UN',
    "DVolume Depth",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390030,
    'UN',
    "DVolume Height",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390031,
    'UN',
    "DVolume Pos X",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390032,
    'UN',
    "DVolume Pos Y",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390033,
    'UN',
    "DVolume Pos Z",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390034,
    'UN',
    "DBeam Axial Min",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390035,
    'UN',
    "DBeam Axial Span",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390037,
    'UN',
    "DBeam Lateral Span",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390038,
    'UN',
    "Number of Volumes in Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390039,
    'UN',
    "DByte Mask Offset",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390040,
    'UN',
    "DByte Mask Size",
    '1')
add_private_dict_entry(
    "GEMS_AWSoft_SB1",
    0x00390050,
    'UI',
    "Reference to Study UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390050,
    'LO',
    "Private Creator Version of Bookmark",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390050,
    'LO',
    "Private Creator Version of Bookmark",
    '1')
add_private_dict_entry(
    "GEMS_AWSoft_SB1",
    0x00390051,
    'UI',
    "Reference to Series UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390051,
    'US',
    "BCut Plane Enable",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390051,
    'US',
    "BCut Plane Enable",
    '1')
add_private_dict_entry(
    "GEMS_AWSoft_SB1",
    0x00390052,
    'IS',
    "Reference to Original Instance Number",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390052,
    'US',
    "BMpr Color Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390052,
    'US',
    "BMpr Color Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390053,
    'US',
    "BMpr Dynamic Range Db",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390053,
    'US',
    "BMpr Dynamic Range Db",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390054,
    'US',
    "BMpr Gray Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390054,
    'US',
    "BMpr Gray Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390055,
    'US',
    "BVolume Render Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390055,
    'US',
    "BVolume Render Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390056,
    'US',
    "BVr Brightness",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390056,
    'US',
    "BVr Brightness",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390057,
    'US',
    "BVr Contrast",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390057,
    'US',
    "BVr Contrast",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390058,
    'US',
    "BVr Color Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390058,
    'US',
    "BVr Color Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390059,
    'US',
    "BVr Dynamic Range Db",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390059,
    'US',
    "BVr Dynamic Range Db",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039005a,
    'US',
    "BVr Gray Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039005a,
    'US',
    "BVr Gray Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039005b,
    'US',
    "BVr Gray Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039005b,
    'US',
    "BVr Gray Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039005c,
    'US',
    "BVr Threshold High",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039005c,
    'US',
    "BVr Threshold High",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039005d,
    'US',
    "BVr Threshold Low",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039005d,
    'US',
    "BVr Threshold Low",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039005e,
    'US',
    "BPre Process Filter Mix",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039005e,
    'US',
    "BPre Process Filter Mix",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039005f,
    'US',
    "CCut Plane Enable",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039005f,
    'US',
    "CCut Plane Enable",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390060,
    'US',
    "CFront Clip Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390060,
    'US',
    "CFront Clip Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390061,
    'US',
    "CMpr Color Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390061,
    'US',
    "CMpr Color Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390062,
    'US',
    "CMpr Color Flow Priority Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390062,
    'US',
    "CMpr Color Flow Priority Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390063,
    'US',
    "CVolume Render Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390063,
    'US',
    "CVolume Render Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390064,
    'US',
    "CVr Color Map Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390064,
    'US',
    "CVr Color Map Index",
    '1')
add_private_dict_entry(
    "GEMS_AWSOFT_CD1",
    0x00390065,
    'UI',
    "Reference to Study UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390065,
    'US',
    "CVr Color Flow Priority Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390065,
    'US',
    "CVr Color Flow Priority Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390066,
    'US',
    "CVr Opacity",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390066,
    'US',
    "CVr Opacity",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390067,
    'US',
    "CVr Threshold High",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390067,
    'US',
    "CVr Threshold High",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390068,
    'US',
    "CVr Threshold Low",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390068,
    'US',
    "CVr Threshold Low",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390069,
    'US',
    "Voi Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390069,
    'US',
    "Voi Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039006a,
    'US',
    "Voi Rotation Offset Deg",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039006a,
    'US',
    "Voi Rotation Offset Deg",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039006b,
    'FD',
    "Voi Size Ratio X",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039006b,
    'FD',
    "Voi Size Ratio X",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039006c,
    'FD',
    "Voi Size Ratio Y",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039006c,
    'FD',
    "Voi Size Ratio Y",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039006d,
    'FD',
    "Voi Size Ratio Z",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039006d,
    'FD',
    "Voi Size Ratio Z",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039006e,
    'US',
    "Voi Sync Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039006e,
    'US',
    "Voi Sync Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039006f,
    'US',
    "Voi View Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039006f,
    'US',
    "Voi View Mode",
    '1')
add_private_dict_entry(
    "GEMS_AWSOFT_CD1",
    0x00390070,
    'UI',
    "Reference to Series UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390070,
    'FD',
    "Vr Orientation A",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390070,
    'FD',
    "Vr Orientation A",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390071,
    'FD',
    "Mpr Orientation A",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390071,
    'FD',
    "Mpr Orientation A",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390072,
    'FD',
    "Vr Offset Vector",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390072,
    'FD',
    "Vr Offset Vector",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390073,
    'FD',
    "Blending Ratio",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390073,
    'FD',
    "Blending Ratio",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390074,
    'US',
    "Fusion Blend Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390074,
    'US',
    "Fusion Blend Mode",
    '1')
add_private_dict_entry(
    "GEMS_AWSOFT_CD1",
    0x00390075,
    'IS',
    "Reference to Original Instance Number",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390075,
    'FD',
    "Quality Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390075,
    'FD',
    "Quality Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MED OCS BEAM DISPLAY INFO",
    0x00390076,
    'CS',
    "Beam Display Properties",
    '1')
add_private_dict_entry(
    "SIEMENS MED OCS SS VERSION INFO",
    0x00390076,
    'LO',
    "Structure Set Predecessor",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390076,
    'US',
    "Renderer Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390076,
    'US',
    "Renderer Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390077,
    'US',
    "Slice Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390077,
    'US',
    "Slice Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390078,
    'US',
    "Active Quad",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390078,
    'US',
    "Active Quad",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390079,
    'US',
    "Screen Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390079,
    'US',
    "Screen Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039007a,
    'US',
    "Cut Plane Side",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039007a,
    'US',
    "Cut Plane Side",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039007b,
    'US',
    "Wireframe Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039007b,
    'US',
    "Wireframe Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039007c,
    'US',
    "Crossmark Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039007c,
    'US',
    "Crossmark Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039007d,
    'US',
    "Mpr Display Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039007d,
    'US',
    "Mpr Display Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039007e,
    'US',
    "Volume Display Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039007e,
    'US',
    "Volume Display Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039007f,
    'US',
    "Last Reset",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039007f,
    'US',
    "Last Reset",
    '1')
add_private_dict_entry(
    "GEMS_AWSOFT_CD1",
    0x00390080,
    'IS',
    "DPO Number",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_DPO",
    0x00390080,
    'IS',
    "Private Entity Number",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390080,
    'US',
    "Last Non Full Screen Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390080,
    'US',
    "Last Non Full Screen Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390081,
    'US',
    "Mpr Tool Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390081,
    'US',
    "Mpr Tool Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390082,
    'US',
    "Voi Tool Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390082,
    'US',
    "Voi Tool Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390083,
    'US',
    "Tool Loop Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390083,
    'US',
    "Tool Loop Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390084,
    'US',
    "Volume Arb Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390084,
    'US',
    "Volume Arb Mode",
    '1')
add_private_dict_entry(
    "GEMS_AWSOFT_CD1",
    0x00390085,
    'DA',
    "DPO Date",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_DPO",
    0x00390085,
    'DA',
    "Private Entity Date",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390085,
    'US',
    "Mpr Zoom Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390085,
    'US',
    "Mpr Zoom Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390086,
    'US',
    "Is Volume Zoom Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390086,
    'US',
    "Is Volume Zoom Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390087,
    'SS',
    "Zoom Level Mpr",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390087,
    'SS',
    "Zoom Level Mpr",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390088,
    'SS',
    "Zoom Level Volume",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390088,
    'SS',
    "Zoom Level Volume",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390089,
    'US',
    "Is Auto Rotate Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390089,
    'US',
    "Is Auto Rotate Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039008a,
    'US',
    "Auto Rotate Axis",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039008a,
    'US',
    "Auto Rotate Axis",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039008b,
    'US',
    "Auto Rotate Range Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039008b,
    'US',
    "Auto Rotate Range Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039008c,
    'US',
    "Auto Rotate Speed Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039008c,
    'US',
    "Auto Rotate Speed Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039008d,
    'US',
    "CVr Brightness",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039008d,
    'US',
    "CVr Brightness",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039008e,
    'US',
    "CFlow State Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039008e,
    'US',
    "CFlow State Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039008f,
    'US',
    "BSubmode Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039008f,
    'US',
    "BSubmode Index",
    '1')
add_private_dict_entry(
    "GEMS_AWSOFT_CD1",
    0x00390090,
    'TM',
    "DPO Time",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_DPO",
    0x00390090,
    'TM',
    "Private Entity Time",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390090,
    'US',
    "CSubmode Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390090,
    'US',
    "CSubmode Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390091,
    'US',
    "Cut Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390091,
    'US',
    "Cut Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390092,
    'US',
    "Bookmark Chunk Id",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390092,
    'US',
    "Bookmark Chunk Id",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390093,
    'US',
    "Sequence Min Chunk Id",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390093,
    'US',
    "Sequence Min Chunk Id",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390094,
    'US',
    "Sequence Max Chunk Id",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390094,
    'US',
    "Sequence Max Chunk Id",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_DPO1",
    0x00390095,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_AWSOFT_CD1",
    0x00390095,
    'LO',
    "DPO Invocation String",
    '1')
add_private_dict_entry(
    "GEMS_AWSoft_SB1",
    0x00390095,
    'LO',
    "Private Entity Launch Command",
    '1')
add_private_dict_entry(
    "GEMS_0039",
    0x00390095,
    'LO',
    "SR Application Name",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_DPO",
    0x00390095,
    'LO',
    "Private Entity Launch Command",
    '1')
add_private_dict_entry(
    "REPORT_FROM_APP",
    0x00390095,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x00390095,
    'FD',
    "Volume Rate Hz",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x00390095,
    'FD',
    "Volume Rate Hz",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039009a,
    'FD',
    "Voi Position Offset X",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039009a,
    'FD',
    "Voi Position Offset X",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039009b,
    'FD',
    "Voi Position Offset Y",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039009b,
    'FD',
    "Voi Position Offset Y",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039009c,
    'FD',
    "Voi Position Offset Z",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039009c,
    'FD',
    "Voi Position Offset Z",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039009d,
    'US',
    "Vr Tool Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039009d,
    'US',
    "Vr Tool Index",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039009e,
    'US',
    "Shading Percent",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039009e,
    'US',
    "Shading Percent",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x0039009f,
    'US',
    "Volume Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x0039009f,
    'US',
    "Volume Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900a0,
    'US',
    "Vr Quad Display Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900a0,
    'US',
    "Vr Quad Display Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900a1,
    'FD',
    "Mpr Center Location",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900a1,
    'FD',
    "Mpr Center Location",
    '1-n')
add_private_dict_entry(
    "GEMS_AWSOFT_CD1",
    0x003900AA,
    'CS',
    "DPO Type",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_DPO",
    0x003900AA,
    'CS',
    "Private Entity Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e0,
    'US',
    "Slice Range Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e0,
    'US',
    "Slice Range Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e1,
    'US',
    "Slice MPR Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e1,
    'US',
    "Slice MPR Plane",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e2,
    'US',
    "Slice Layout",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e2,
    'US',
    "Slice Layout",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e3,
    'FD',
    "Slice Spacing",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e3,
    'FD',
    "Slice Spacing",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e4,
    'US',
    "Thin Vr Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e4,
    'US',
    "Thin Vr Mode",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e5,
    'US',
    "Thin Vr Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e5,
    'US',
    "Thin Vr Thickness",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e6,
    'FD',
    "Curved TOP VOI Pivot X",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e6,
    'FD',
    "Curved TOP VOI Pivot X",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e7,
    'FD',
    "Curved TOP VOI Pivot Y",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e7,
    'FD',
    "Curved TOP VOI Pivot Y",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e8,
    'FD',
    "Curved TOP VOI Pivot Z",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e8,
    'FD',
    "Curved TOP VOI Pivot Z",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900e9,
    'US',
    "Curved TOP VOI Quadrant",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900e9,
    'US',
    "Curved TOP VOI Quadrant",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900ea,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900ea,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900ed,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900ed,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900ee,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900ee,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900ef,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900ef,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900f0,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900f0,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900f1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900f1,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900f2,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900f2,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900f3,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900f3,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900f4,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900f4,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900f5,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900f5,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG ANTARES 3D VOLUME",
    0x003900f6,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SMS USG S2000 3D VOLUME",
    0x003900f6,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_AWSOFT_CD1",
    0x003900FF,
    'OB',
    "DPO Data",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410000,
    'LT',
    "Papyrus Comments",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410000,
    'LT',
    "Papyrus Comments",
    '1-n')
add_private_dict_entry(
    "QUASAR_INTERNAL_USE",
    0x00410001,
    'UT',
    "?",
    '1')
add_private_dict_entry(
    "PixelMed Publishing",
    0x00410001,
    'SQ',
    "Quantity Definition Code Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MI RWVM SUV",
    0x00410001,
    'CS',
    "SUV Decay Correction Method",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410001,
    'SL',
    "Whole Body Tomo Position Index",
    '1')
add_private_dict_entry(
    "WG12 Supplement 43",
    0x00410001,
    'CS',
    "Performed Protocol Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00410002,
    'SH',
    "Reason for the Requested Procedure",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410002,
    'SL',
    "Whole Body Tomo Number of Positions",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410003,
    'FL',
    "Horizontal Table Position of CT scan",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410004,
    'FL',
    "Effective Energy fo CT Scan",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410005,
    'FD',
    "Long Linear Drive Information for Detector 1",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410006,
    'FD',
    "Long Linear Drive Information for Detector 2",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00410007,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410007,
    'FD',
    "Trunnion Information for Detector 1",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410008,
    'FD',
    "Trunnion Information for Detector 2",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR/LAST",
    0x00410009,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410009,
    'FL',
    "Broad Beam Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0041000A,
    'FD',
    "Original Wholebody Position",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0041000B,
    'FD',
    "Wholebody Scan Range",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410010,
    'SQ',
    "Pointer Sequence",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410010,
    'US',
    "Folder Type",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00410010,
    'US',
    "Number of Hardcopies",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410010,
    'FL',
    "Effective Emission Energy",
    '1-3')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410011,
    'UL',
    "Image Pointer",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410011,
    'LT',
    "Patient Folder Data Set ID",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410011,
    'FL',
    "Gated Frame Duration",
    '1-n')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410012,
    'UL',
    "Pixel Offset",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410013,
    'SQ',
    "Image Identifier Sequence",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410014,
    'SQ',
    "External File Reference Sequence",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410015,
    'US',
    "Number of Images",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410020,
    'LT',
    "Folder Name",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00410020,
    'LO',
    "Film Format",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410021,
    'UI',
    "Referenced SOP Class UID",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410022,
    'UI',
    "Referenced SOP Instance UID",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410030,
    'DA',
    "Creation Date",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00410030,
    'LO',
    "Film Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410030,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410031,
    'LT',
    "Referenced File Name",
    '1')
add_private_dict_entry(
    "SIEMENS DLR.01",
    0x00410031,
    'LO',
    "Full Film Format",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410032,
    'LT',
    "Referenced File Path",
    '1-n')
add_private_dict_entry(
    "PAPYRUS",
    0x00410032,
    'TM',
    "Creation Time",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00410032,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410034,
    'DA',
    "Modified Date",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410036,
    'TM',
    "Modified Time",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410040,
    'LT',
    "Owner Name",
    '1-n')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410041,
    'UI',
    "Referenced Image SOP Class UID",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410042,
    'UI',
    "Referenced Image SOP Instance UID",
    '1')
add_private_dict_entry(
    "PAPYRUS 3.0",
    0x00410050,
    'SQ',
    "Image Sequence",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410050,
    'LT',
    "Folder Status",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410060,
    'UL',
    "Number of Images",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x00410062,
    'UL',
    "Number of Other",
    '1')
add_private_dict_entry(
    "PAPYRUS",
    0x004100a0,
    'LT',
    "External Folder Element DSID",
    '1-n')
add_private_dict_entry(
    "PAPYRUS",
    0x004100a1,
    'US',
    "External Folder Element Data Set Type",
    '1-n')
add_private_dict_entry(
    "PAPYRUS",
    0x004100a2,
    'LT',
    "External Folder Element File Location",
    '1-n')
add_private_dict_entry(
    "PAPYRUS",
    0x004100a3,
    'UL',
    "External Folder Element Length",
    '1-n')
add_private_dict_entry(
    "PAPYRUS",
    0x004100b0,
    'LT',
    "Internal Folder Element DSID",
    '1-n')
add_private_dict_entry(
    "PAPYRUS",
    0x004100b1,
    'US',
    "Internal Folder Element Data Set Type",
    '1-n')
add_private_dict_entry(
    "PAPYRUS",
    0x004100b2,
    'UL',
    "Internal Offset To Data Set",
    '1-n')
add_private_dict_entry(
    "PAPYRUS",
    0x004100b3,
    'UL',
    "Internal Offset To Image",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430001,
    'SS',
    "Bitmap Of Prescan Options",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00430001,
    'FL',
    "Detector View Angle",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430002,
    'SS',
    "Gradient Offset In X",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00430002,
    'FD',
    "Transformation Matrix",
    '1-16')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430003,
    'SS',
    "Gradient Offset In Y",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00430003,
    'FL',
    "View Dependent Y Shift MHR For Detector 1",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430004,
    'SS',
    "Gradient Offset In Z",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00430004,
    'FL',
    "View Dependent Y Shift MHR For Detector 2",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430005,
    'SS',
    "Image Is Original Or Unoriginal",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430006,
    'SS',
    "Number Of EPI Shots",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430007,
    'SS',
    "Views Per Segment",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430008,
    'SS',
    "Respiratory Rate In BPM",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430009,
    'SS',
    "Respiratory Trigger Point",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043000a,
    'SS',
    "Type Of Receiver Used",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043000b,
    'DS',
    "dB/dt Peak Rate Of Change Of Gradient Field",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043000c,
    'DS',
    "dB/dt Limits In Units Of Percent",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043000d,
    'DS',
    "PSD Estimated Limit",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043000e,
    'DS',
    "PSD Estimated Limit In Tesla Per Second",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043000f,
    'DS',
    "SAR Avg Head",
    '1')
add_private_dict_entry(
    "dcm4che/archive",
    0x00430010,
    'OB',
    "Patient Pk",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430010,
    'US',
    "Window Value",
    '1')
add_private_dict_entry(
    "dcm4che/archive",
    0x00430011,
    'OB',
    "Study Pk",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430011,
    'US',
    "Total Input Views",
    '1')
add_private_dict_entry(
    "dcm4che/archive",
    0x00430012,
    'OB',
    "Series Pk",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430012,
    'SS',
    "Xray Chain",
    '3')
add_private_dict_entry(
    "dcm4che/archive",
    0x00430013,
    'OB',
    "Instance Pk",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430013,
    'SS',
    "Recon Kernel Parameters",
    '5')
add_private_dict_entry(
    "dcm4che/archive",
    0x00430014,
    'AE',
    "Calling AE Title",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430014,
    'SS',
    "Calibration Parameters",
    '3')
add_private_dict_entry(
    "dcm4che/archive",
    0x00430015,
    'AE',
    "Called AE Title",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430015,
    'SS',
    "Total Output Views",
    '3')
add_private_dict_entry(
    "dcm4che/archive",
    0x00430016,
    'DT',
    "Instance Updated",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430016,
    'SS',
    "Number Of Overranges",
    '5')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430017,
    'DS',
    "IBH Image Scale Factors",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430018,
    'DS',
    "BBH Coefficients",
    '3')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430019,
    'SS',
    "Number Of BBH Chains To Blend",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043001a,
    'SL',
    "Starting Channel Number",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043001b,
    'SS',
    "PPScan Parameters",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043001c,
    'SS',
    "GE Image Integrity",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043001d,
    'SS',
    "Level Value",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043001e,
    'DS',
    "Delta Start Time",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x0043001e,
    'DS',
    "Delta Start Time",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043001f,
    'SL',
    "Max Overranges In A View",
    '1')
add_private_dict_entry(
    "dcm4che/archive",
    0x00430020,
    'SQ',
    "Work Item Sequence",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430020,
    'DS',
    "Avg Overranges All Views",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430021,
    'SS',
    "Corrected Afterglow Terms",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430025,
    'SS',
    "Reference Channels",
    '6')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430026,
    'US',
    "No Views Ref Channels Blocked",
    '6')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430027,
    'SH',
    "Scan Pitch Ratio",
    '1')
add_private_dict_entry(
    "GE_GENESIS_REV3.0",
    0x00430027,
    'SH',
    "Scan Pitch Ratio",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430028,
    'OB',
    "Unique Image Identifier",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430029,
    'OB',
    "Histogram Tables",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043002a,
    'OB',
    "User Defined Data",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043002b,
    'SS',
    "Private Scan Options",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043002c,
    'SS',
    "Effective Echo Spacing",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043002d,
    'SH',
    "Filter Mode",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043002e,
    'SH',
    "String Slop Field 2",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043002f,
    'SS',
    "Image Type (Real,Imaginary,Phase,Magnitude)",
    '1')
add_private_dict_entry(
    "dcm4che/archive",
    0x00430030,
    'UI',
    "Dcm4che URI Referenced Transfer Syntax UID",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430030,
    'SS',
    "Vas Collapse Flag",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430031,
    'DS',
    "Recon Center Coordinates",
    '2')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430032,
    'SS',
    "Vas Flags",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430033,
    'FL',
    "Neg Scan Spacing",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430034,
    'IS',
    "Offset Frequency",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430035,
    'UL',
    "User Usage Tag",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430036,
    'UL',
    "User Fill Map MSW",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430037,
    'UL',
    "User Fill Map LSW",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430038,
    'FL',
    "User 25 To User 48",
    '24')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430039,
    'IS',
    "Slop Integer 6 To Slop Integer 9",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430040,
    'FL',
    "Trigger On Position",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430041,
    'FL',
    "Degree Of Rotation",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430042,
    'SL',
    "DAS Trigger Source",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430043,
    'SL',
    "DAS Fpa Gain",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430044,
    'SL',
    "DAS Output Source",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430045,
    'SL',
    "DAS Ad Input",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430046,
    'SL',
    "DAS Cal Mode",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430047,
    'SL',
    "DAS Cal Frequency",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430048,
    'SL',
    "DAS Reg Xm",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430049,
    'SL',
    "DAS Auto Zero",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043004a,
    'SS',
    "Starting Channel Of View",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043004b,
    'SL',
    "DAS Xm Pattern",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043004c,
    'SS',
    "TGGC Trigger Mode",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043004d,
    'FL',
    "Start Scan To Xray On Delay",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043004e,
    'FL',
    "Duration Of Xray On",
    '4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430060,
    'IS',
    "Slop Integer 10 To Slop Integer 17",
    '8')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430061,
    'UI',
    "Scanner Study Entity UID",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430062,
    'SH',
    "Scanner Study ID",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430063,
    'SH',
    "Raw Data ID",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430064,
    'CS',
    "Recon Filter",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430065,
    'US',
    "Motion Correction Indicator",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430066,
    'US',
    "Helical Correction Indicator",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430067,
    'US',
    "IBO Correction Indicator",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430068,
    'US',
    "XT Correction Indicator",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430069,
    'US',
    "Q-cal Correction Indicator",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043006a,
    'US',
    "AV Correction Indicator",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043006b,
    'US',
    "L-MDK Correction Indicator",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043006c,
    'IS',
    "Detector Row",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043006d,
    'US',
    "Area Size",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043006e,
    'SH',
    "Auto mA Mode",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043006f,
    'DS',
    "Scanner Table Entry + Gradient Coil Selected",
    '3-4')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430070,
    'LO',
    "Paradigm Name",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430071,
    'ST',
    "Paradigm Description",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430072,
    'UI',
    "Paradigm UID",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430073,
    'US',
    "Experiment Type",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430074,
    'US',
    "Number of Rest Volumes",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430075,
    'US',
    "Number of Active Volumes",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430076,
    'US',
    "Number of Dummy Scans",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430077,
    'SH',
    "Application Name",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430078,
    'SH',
    "Application Version",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430079,
    'US',
    "Slices Per Volume",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043007a,
    'US',
    "Expected Time Points",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043007b,
    'FL',
    "Regressor Values",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043007c,
    'FL',
    "Delay After Slice Group",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043007d,
    'US',
    "Recon Mode Flag Word",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043007e,
    'LO',
    "PACC Specific Information",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043007f,
    'DS',
    "Reserved",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430080,
    'LO',
    "Coil ID Data",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430081,
    'LO',
    "GE Coil Name",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430082,
    'LO',
    "System Configuration Information",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430083,
    'DS',
    "Asset R Factors",
    '1-2')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430084,
    'LO',
    "Additional Asset Data",
    '5')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430085,
    'UT',
    "Debug Data (Text Format)",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430086,
    'OB',
    "Debug Data (Binary Format)",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430087,
    'UT',
    "Reserved",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430088,
    'UI',
    "PURE Acquisition Calibration Series UID",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430089,
    'LO',
    "Governing Body,dB/dt,and SAR definition",
    '3')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043008a,
    'CS',
    "Private In-Plane Phase Encoding Direction",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043008b,
    'OB',
    "FMRI Binary Data Block",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043008c,
    'DS',
    "Voxel Location",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043008d,
    'DS',
    "SAT Band Locations",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043008e,
    'DS',
    "Spectro Prescan Values",
    '3')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043008f,
    'DS',
    "Spectro Parameters",
    '3')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430090,
    'LO',
    "SAR Definition",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430091,
    'DS',
    "SAR Value",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430092,
    'LO',
    "Image Error Text",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430093,
    'DS',
    "Spectro Quantitation Values",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430094,
    'DS',
    "Spectro Ratio Values",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430095,
    'LO',
    "Prescan Reuse String",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430096,
    'CS',
    "Content Qualification",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430097,
    'LO',
    "Image Filtering Parameters",
    '8')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430098,
    'UI',
    "ASSET Acquisition Calibration Series UID",
    '1')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x00430099,
    'LO',
    "Extended Options",
    '1-n')
add_private_dict_entry(
    "GEMS_PARM_01",
    0x0043009a,
    'IS',
    "Rx Stack Identification",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450001,
    'LO',
    "Digital Senograph Configuration",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450001,
    'SS',
    "Number of Macro Rows in Detector",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00450001,
    'LO',
    "Planar Processing String",
    '1-n')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450002,
    'FL',
    "Macro width at ISO Center",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450002,
    'LT',
    "System Series Description",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450003,
    'CS',
    "Track",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450003,
    'SS',
    "DAS type",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450004,
    'CS',
    "AES",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450004,
    'CS',
    "Exposure Status",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450004,
    'SS',
    "DAS gain",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450005,
    'SS',
    "DAS Temprature",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450006,
    'CS',
    "Table Direction",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450006,
    'DS',
    "Angulation",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450007,
    'DS',
    "Compression Thickness",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450007,
    'FL',
    "Z smoothing Factor",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450008,
    'DS',
    "Compression Force",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450008,
    'SS',
    "View Weighting Mode",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450009,
    'DS',
    "Real Magnification Factor",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450009,
    'SS',
    "Sigma Row number",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x0045000A,
    'FL',
    "Minimum DAS value",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045000a,
    'DS',
    "Displayed Magnification Factor",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x0045000B,
    'FL',
    "Maximum Offset Value",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045000b,
    'CS',
    "Senograph Type",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x0045000C,
    'SS',
    "Number of Views shifted",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045000c,
    'DS',
    "Integration Time",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x0045000D,
    'SS',
    "Z tracking Flag",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045000d,
    'DS',
    "ROI Origin X and Y",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x0045000E,
    'FL',
    "Mean Z error",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045000e,
    'CS',
    "Correction Type",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x0045000F,
    'FL',
    "Z tracking Error",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045000f,
    'CS',
    "Acquisition Type",
    '1')
add_private_dict_entry(
    "GEMS_IT_US_REPORT",
    0x00450111,
    'OW',
    "Vivid excel file",
    '1')
add_private_dict_entry(
    "GEMS_IT_US_REPORT",
    0x00450112,
    'OW',
    "Vivid CHM file",
    '1')
add_private_dict_entry(
    "GEMS_IT_US_REPORT",
    0x00450113,
    'OW',
    "Vivid PDF file",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450010,
    'DS',
    "CCD Temperature",
    '2')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450010,
    'SS',
    "Start View 2A",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450011,
    'DS',
    "Receptor Size cm X and Y",
    '2')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450011,
    'SS',
    "Number of Views 2A",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450012,
    'IS',
    "Receptor Size Pixels X and Y",
    '2')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450012,
    'SS',
    "Start View 1A",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450013,
    'SS',
    "Sigma Mode",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450013,
    'ST',
    "Screen",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450014,
    'DS',
    "Pixel Pitch Microns",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450014,
    'SS',
    "Number of Views 1A",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450015,
    'IS',
    "Pixel Depth Bits",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450015,
    'SS',
    "Start View 2B",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450016,
    'IS',
    "Binning Factor X and Y",
    '2')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450016,
    'SS',
    "Number Views 2B",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450017,
    'DS',
    "Quantum Gain",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450017,
    'SS',
    "Start View 1B",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450018,
    'DS',
    "Electron/EDU Ratio",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450018,
    'SS',
    "Number of Views 1B",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450019,
    'DS',
    "Electronic Gain",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045001A,
    'OB',
    "IDS Data Buffer",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045001B,
    'LO',
    "Clinical View",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045001C,
    'CS',
    "Breast Laterality",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045001D,
    'DS',
    "Mean Of Raw Gray Levels",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045001E,
    'DS',
    "Mean Of Offset Gray Levels",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045001F,
    'DS',
    "Mean Of Corrected Gray Levels",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450020,
    'DS',
    "Mean Of Region Gray Levels",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450021,
    'DS',
    "Mean Of Log Region Gray Levels",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450021,
    'SS',
    "Iterbone Flag",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450022,
    'DS',
    "Standard Deviation Of Raw Gray Levels",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450022,
    'SS',
    "Peristaltic Flag",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450023,
    'DS',
    "Standard Deviation Of Corrected Gray Levels",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450024,
    'DS',
    "Standard Deviation Of Region Gray Levels",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450025,
    'DS',
    "Standard Deviation Of Log Region Gray Levels",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450026,
    'OB',
    "MAO Buffer",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450027,
    'IS',
    "Set Number",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450028,
    'CS',
    "WindowingType (LINEAR or GAMMA)",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450029,
    'DS',
    "WindowingParameters",
    '1-n')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045002a,
    'IS',
    "Crosshair Cursor X Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045002b,
    'IS',
    "Crosshair Cursor Y Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045002c,
    'DS',
    "Reference Landmark A X 3D Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045002d,
    'DS',
    "Reference Landmark A Y 3D Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045002e,
    'DS',
    "Reference Landmark A Z 3D Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045002f,
    'IS',
    "Reference Landmark A X Image Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450030,
    'CS',
    "Cardiac Recon Algorithm",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450030,
    'IS',
    "Reference Landmark A Y Image Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450031,
    'CS',
    "Avg Heart Rate For Image",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450031,
    'DS',
    "Reference Landmark B X 3D Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450032,
    'DS',
    "Reference Landmark B Y 3D Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450032,
    'FL',
    "Temporal Resolution",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450033,
    'CS',
    "Pct Rpeak Delay",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450033,
    'DS',
    "Reference Landmark B Z 3D Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450034,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450034,
    'IS',
    "Reference Landmark B X Image Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450035,
    'IS',
    "Reference Landmark B Y Image Coordinates",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450036,
    'CS',
    "Ekg Full Ma Start Phase",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450036,
    'DS',
    "X-Ray Source X Location",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450037,
    'CS',
    "Ekg Full Ma End Phase",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450037,
    'DS',
    "X-Ray Source Y Locatio",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450038,
    'CS',
    "Ekg Modulation Max Ma",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450038,
    'DS',
    "X-Ray Source Z Locatio",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450039,
    'CS',
    "Ekg Modulation Min Ma",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450039,
    'US',
    "Vignette Rows",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045003a,
    'US',
    "Vignette Columns",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x0045003B,
    'LO',
    "Noise Reduction Image Filter Desc",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045003b,
    'US',
    "Vignette Bits Allocated",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045003c,
    'US',
    "Vignette Bits Stored",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045003d,
    'US',
    "Vignette High Bit",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045003e,
    'US',
    "Vignette Pixel Representation",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x0045003f,
    'OB',
    "Vignette Pixel Data",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450049,
    'DS',
    "Radiological Thickness",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450050,
    'FD',
    "Temporal Center View Angle",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450050,
    'UI',
    "Fallback Instance UID (CR or SC)",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450051,
    'FD',
    "Recon Center View Angle",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450051,
    'UI',
    "Fallback Series UID (CR or SC)",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450052,
    'CS',
    "WideCone Masking",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450052,
    'IS',
    "Raw Diagnostic Low",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450053,
    'FD',
    "WideCone Corner Blending Radius",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450053,
    'IS',
    "Raw Diagnostic High",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450054,
    'DS',
    "Exponent",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450054,
    'FD',
    "WideCone Corner Blending Radius Offset",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450055,
    'CS',
    "Internal Recon Algorithm",
    '1')
add_private_dict_entry(
    "GEMS_FALCON_03",
    0x00450055,
    'DS',
    "A_Coefficients used in Multiresolution Algorithm",
    '8')
add_private_dict_entry(
    "GEMS_SEND_02",
    0x00450055,
    'DS',
    "A_Coefficients used in Multiresolution Algorithm",
    '8')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450055,
    'IS',
    "A Coefficients",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450056,
    'DS',
    "Noise Reduction Sensitivity",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450057,
    'DS',
    "Noise Reduction Threshold",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450058,
    'DS',
    "Mu",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450059,
    'IS',
    "Threshold",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450060,
    'FL',
    "Patient Centering",
    '1-n')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450060,
    'IS',
    "Breast ROI X",
    '4')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450061,
    'FL',
    "Patient Attenuation",
    '1-n')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450061,
    'IS',
    "Breast ROI Y",
    '4')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450062,
    'FL',
    "Water Equivalent Diameter",
    '1-n')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450062,
    'IS',
    "User Window Center",
    '1')
add_private_dict_entry(
    "GEMS_FALCON_03",
    0x00450062,
    'IS',
    "User Window Center",
    '1')
add_private_dict_entry(
    "GEMS_SEND_02",
    0x00450062,
    'IS',
    "User Window Center",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450063,
    'FL',
    "Projection Measure",
    '1-n')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450063,
    'IS',
    "User Window Width",
    '1')
add_private_dict_entry(
    "GEMS_FALCON_03",
    0x00450063,
    'IS',
    "User Window Width",
    '1')
add_private_dict_entry(
    "GEMS_SEND_02",
    0x00450063,
    'IS',
    "User Window Width",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450064,
    'FL',
    "Oval Ratio",
    '1-n')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450064,
    'IS',
    "Segmentation Threshold",
    '1')
add_private_dict_entry(
    "GEMS_HELIOS_01",
    0x00450065,
    'FL',
    "Ellipse Orientation",
    '1-n')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450065,
    'IS',
    "Detector Entrance Dose",
    '1')
add_private_dict_entry(
    "GEMS_FALCON_03",
    0x00450065,
    'IS',
    "Requested Detector Entrance Dose",
    '1')
add_private_dict_entry(
    "GEMS_SEND_02",
    0x00450065,
    'IS',
    "Requested Detector Entrance Dose",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450066,
    'IS',
    "Asymmetrical Collimation Information",
    '1')
add_private_dict_entry(
    "GEMS_FALCON_03",
    0x00450067,
    'DS',
    "VOI LUT Assymmetry Parameter Beta",
    '3')
add_private_dict_entry(
    "GEMS_SEND_02",
    0x00450067,
    'DS',
    "VOI LUT Assymmetry Parameter Beta",
    '3')
add_private_dict_entry(
    "GE LUT Asymmetry Parameter",
    0x00450067,
    'DS',
    "LUT Assymetry",
    '1')
add_private_dict_entry(
    "GEMS_FALCON_03",
    0x00450069,
    'IS',
    "Collimator Rotation",
    '1')
add_private_dict_entry(
    "GEMS_SEND_02",
    0x00450069,
    'IS',
    "Collimator Rotation",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450071,
    'OB',
    "STX Buffer",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450072,
    'DS',
    "Image Crop Point",
    '2')
add_private_dict_entry(
    "GEMS_FALCON_03",
    0x00450072,
    'IS',
    "Collimator Width",
    '1')
add_private_dict_entry(
    "GEMS_SEND_02",
    0x00450072,
    'IS',
    "Collimator Width",
    '1')
add_private_dict_entry(
    "GEMS_FALCON_03",
    0x00450073,
    'IS',
    "Collimator Height",
    '1')
add_private_dict_entry(
    "GEMS_SEND_02",
    0x00450073,
    'IS',
    "Collimator Height",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x00450090,
    'SH',
    "Premium View Beta",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500A0,
    'DS',
    "Signal Average Factor",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500A1,
    'DS',
    "Organ Dose for Source Images",
    '2-n')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500A2,
    'DS',
    "Entrance dose in mGy for Source Images",
    '2-n')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500A4,
    'DS',
    "Organ Dose in dGy for Complete DBT Sequence",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500A6,
    'UI',
    "SOP Instance UID for Lossy Compression",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500A7,
    'LT',
    "Reconstruction Parameters",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500A8,
    'DS',
    "Entrance Dose in dGy for Complete DBT Sequence",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500A9,
    'DS',
    "Replacement Image",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500AA,
    'SQ',
    "Replaced Image Sequence",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500AB,
    'DS',
    "Cumulative Organ Dose in dGy",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500AC,
    'DS',
    "Cumulative Entrance dose in mGy",
    '1')
add_private_dict_entry(
    "GEMS_SENO_02",
    0x004500AD,
    'LO',
    "Paddle Properties",
    '1-n')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470001,
    'SQ',
    "Reconstruction Parameters Sequence",
    '1')
add_private_dict_entry(
    "GEMS_IQTB_IDEN_47",
    0x00470002,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_VXTL_USERDATA_01",
    0x00470011,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470050,
    'UL',
    "Volume Voxel Count",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470051,
    'UL',
    "Volume Segment Count",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470053,
    'US',
    "Volume Slice Size",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470054,
    'US',
    "Volume Slice Count",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470055,
    'SL',
    "Volume Threshold Value",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470057,
    'DS',
    "Volume Voxel Ratio",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470058,
    'DS',
    "Volume Voxel Size",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470059,
    'US',
    "Volume Z Position Size",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470060,
    'DS',
    "Volume Base Line",
    '9')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470061,
    'DS',
    "Volume Center Point",
    '3')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470063,
    'SL',
    "Volume Skew Base",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470064,
    'DS',
    "Volume Registration Transform Rotation Matrix",
    '9')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470065,
    'DS',
    "Volume Registration Transform Translation Vector",
    '3')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470070,
    'DS',
    "KVP List",
    '1-n')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470071,
    'IS',
    "XRay Tube Current List",
    '1-n')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470072,
    'IS',
    "Exposure List",
    '1-n')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470080,
    'LO',
    "Acquisition DLX Identifier",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470085,
    'SQ',
    "Acquisition DLX 2D Series Sequence",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470089,
    'DS',
    "Contrast Agent Volume List",
    '1-n')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x0047008A,
    'US',
    "Number Of Injections",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x0047008B,
    'US',
    "Frame Count",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470091,
    'LO',
    "XA 3D Reconstruction Algorithm Name",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470092,
    'CS',
    "XA 3D Reconstruction Algorithm Version",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470093,
    'DA',
    "DLX Calibration Date",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470094,
    'TM',
    "DLX Calibration Time",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470095,
    'CS',
    "DLX Calibration Status",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470096,
    'IS',
    "Used Frames",
    '1-n')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470098,
    'US',
    "Transform Count",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x00470099,
    'SQ',
    "Transform Sequence",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x0047009A,
    'DS',
    "Transform Rotation Matrix",
    '9')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x0047009B,
    'DS',
    "Transform Translation Vector",
    '3')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x0047009C,
    'LO',
    "Transform Label",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700B0,
    'SQ',
    "Wireframe List",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700B1,
    'US',
    "Wireframe Count",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700B2,
    'US',
    "Location System",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700B5,
    'LO',
    "Wireframe Name",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700B6,
    'LO',
    "Wireframe Group Name",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700B7,
    'LO',
    "Wireframe Color",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700B8,
    'SL',
    "Wireframe Attributes",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700B9,
    'SL',
    "Wireframe Point Count",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700BA,
    'SL',
    "Wireframe Timestamp",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700BB,
    'SQ',
    "Wireframe Point List",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700BC,
    'DS',
    "Wireframe Points Coordinates",
    '3')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700C0,
    'DS',
    "Volume Upper Left High Corner RAS",
    '3')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700C1,
    'DS',
    "Volume Slice To RAS Rotation Matrix",
    '9')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700C2,
    'DS',
    "Volume Upper Left High Corner TLOC",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700D1,
    'OB',
    "Volume Segment List",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700D2,
    'OB',
    "Volume Gradient List",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700D3,
    'OB',
    "Volume Density List",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700D4,
    'OB',
    "Volume Z Position List",
    '1')
add_private_dict_entry(
    "GEMS_ADWSoft_3D1",
    0x004700D5,
    'OB',
    "Volume Original Index List",
    '1')
add_private_dict_entry(
    "GEMS_3DSTATE_001",
    0x004700e9,
    'FL',
    "?",
    '3')
add_private_dict_entry(
    "GEMS_3DSTATE_001",
    0x004700ea,
    'DS',
    "?",
    '3')
add_private_dict_entry(
    "GEMS_3DSTATE_001",
    0x004700eb,
    'DS',
    "?",
    '3')
add_private_dict_entry(
    "GEMS_3DSTATE_001",
    0x004700ec,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_3DSTATE_001",
    0x004700ed,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490001,
    'SQ',
    "CT Cardiac Sequence",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490002,
    'CS',
    "Heart Rate At Confirm",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490003,
    'FL',
    "Avg Heart Rate Prior To Confirm",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490004,
    'CS',
    "Min Heart Rate Prior To Confirm",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490005,
    'CS',
    "Max Heart Rate Prior To Confirm",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490006,
    'FL',
    "Std Dev Heart Rate Prior To Confirm",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490007,
    'US',
    "Num Heart Rate Samples Prior To Confirm",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490008,
    'CS',
    "Auto Heart Rate Detect Predict",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490009,
    'CS',
    "System Optimized Heart Rate",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x0049000A,
    'ST',
    "Ekg Monitor Type",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x0049000B,
    'CS',
    "Num Recon Sectors",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x0049000C,
    'FL',
    "Rpeak Time Stamps",
    '256')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490016,
    'SH',
    "Ekg Gating Type",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x0049001b,
    'FL',
    "Ekg Wave Time Off First Data Point",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490022,
    'CS',
    "Temporal Alg",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490023,
    'CS',
    "Phase Location",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490024,
    'OW',
    "Pre Blended Cycle 1",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490025,
    'OW',
    "Pre Blended Cycle 2",
    '1')
add_private_dict_entry(
    "GEMS_CT_CARDIAC_001",
    0x00490026,
    'CS',
    "Compression Alg",
    '1')
add_private_dict_entry(
    "GEMS_CT_HINO_01",
    0x004B0001,
    'DS',
    "Beam Thickess",
    '1-n')
add_private_dict_entry(
    "GEMS_CT_HINO_01",
    0x004B0002,
    'DS',
    "R Time",
    '1-n')
add_private_dict_entry(
    "GEMS_CT_HINO_01",
    0x004B0003,
    'IS',
    "HBC Number",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x004B0013,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x004B0015,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x00510001,
    'LO',
    "Group Name",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x00510002,
    'LO',
    "Function Name",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x00510003,
    'SL',
    "Bias",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x00510004,
    'FL',
    "Scale",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x00510005,
    'SL',
    "Parameter Count",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x00510006,
    'LT',
    "Parameters",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x00510007,
    'LO',
    "Version",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x00510008,
    'SL',
    "Color Ramp Index",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510008,
    'CS',
    "CSA Image Header Type",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x00510009,
    'SL',
    "Window Width",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510009,
    'LO',
    "CSA Image Header Version",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x0051000a,
    'SL',
    "Window Level",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0051000a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x0051000b,
    'FL',
    "B-Value",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0051000b,
    'SH',
    "Acquisition Matrix Text",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x0051000c,
    'SL',
    "Wizard State Data Size",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0051000c,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x0051000d,
    'OB',
    "Wizard State",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0051000d,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_FUNCTOOL_01",
    0x0051000e,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0051000e,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x0051000f,
    'LO',
    "Coil String",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510010,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS CM VA0  CMS",
    0x00510010,
    'LO',
    "Image Text",
    '1-n')
add_private_dict_entry(
    "GEMS_CT_VES_01",
    0x00511001,
    'SQ',
    "CTVESequence",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510011,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510012,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510013,
    'SH',
    "Positive PCS Directions",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510015,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510016,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510017,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510018,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MR HEADER",
    0x00510019,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510020,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510021,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510032,
    'DS',
    "?",
    '3')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510037,
    'DS',
    "?",
    '6')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510050,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510060,
    'DS',
    "Primary Positioner Scan Arc",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510061,
    'DS',
    "Secondary Positioner Scan Arc",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510062,
    'DS',
    "Primary Positioner Scan Start Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510063,
    'DS',
    "Secondary Positioner Scan Start Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510064,
    'DS',
    "Primary Positioner Increment",
    '1')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00510065,
    'DS',
    "Secondary Positioner Increment",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530020,
    'IS',
    "Shuttle Flag",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530020,
    'IS',
    "Table Speed Not Reaches Target Flag",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530040,
    'SH',
    "Iterative Recon Annotation",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530041,
    'SH',
    "Iterative Recon Mode",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530042,
    'LO',
    "Iterative Recon Configuration",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530043,
    'SH',
    "Iterative Recon Level",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530060,
    'SH',
    "Recon Flip Rotate Anno",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530061,
    'SH',
    "High Resolution Flag",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530062,
    'SH',
    "Respiratory Flag",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530064,
    'IS',
    "Shutter Mode",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530065,
    'IS',
    "Shutter Mode Percent",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530066,
    'LO',
    "Image Browser Annotation",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530067,
    'IS',
    "Overlapped Recon Flag",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x00530068,
    'IS',
    "Row Number Anotation Flag",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x0053006a,
    'IS',
    "ODM Flag",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x0053006b,
    'IS',
    "ODM Reduction Percent",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x0053007d,
    'LO',
    "SubOptimal IQ String",
    '1')
add_private_dict_entry(
    "GEHC_CT_ADVAPP_001",
    0x0053009d,
    'LO',
    "MARs Annotation",
    '1')
add_private_dict_entry(
    "GEMS_SENOCRYSTAL_V1",
    0x00550000,
    'CS',
    "Clinical View",
    '1')
add_private_dict_entry(
    "GEMS_SENOCRYSTAL_V1",
    0x00550001,
    'IS',
    "Exposure Dose",
    '1')
add_private_dict_entry(
    "PMOD_1",
    0x00550001,
    'FD',
    "Frame Start Times Vector",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED SP DXMG WH AWS 1",
    0x00550001,
    'LO',
    "Projection View Display String",
    '1')
add_private_dict_entry(
    "GEMS_SENOCRYSTAL_V1",
    0x00550002,
    'IS',
    "Implant Displacement",
    '1')
add_private_dict_entry(
    "PMOD_1",
    0x00550002,
    'FD',
    "Frame Positions Vector",
    '3-n')
add_private_dict_entry(
    "GEMS_SENOCRYSTAL_V1",
    0x00550003,
    'IS',
    "Paddle Type",
    '1')
add_private_dict_entry(
    "PMOD_1",
    0x00550003,
    'FD',
    "Frame Orientations Vector",
    '6-n')
add_private_dict_entry(
    "GEMS_SENOCRYSTAL_V1",
    0x00550004,
    'IS',
    "Processing Type",
    '1')
add_private_dict_entry(
    "PMOD_1",
    0x00550004,
    'FD',
    "Frame Durations Vector",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550004,
    'SS',
    "Prompt Window Width",
    '1')
add_private_dict_entry(
    "GEMS_SENOCRYSTAL_V1",
    0x00550005,
    'IS',
    "Windowing Type",
    '1')
add_private_dict_entry(
    "PMOD_1",
    0x00550005,
    'FD',
    "Frame Rescale Slope Vector",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550005,
    'SS',
    "Random Window Width",
    '1')
add_private_dict_entry(
    "GEMS_SENOCRYSTAL_V1",
    0x00550006,
    'IS',
    "Saturation",
    '1')
add_private_dict_entry(
    "GEMS_SENOCRYSTAL_V1",
    0x00550007,
    'IS',
    "Clip",
    '1')
add_private_dict_entry(
    "VEPRO VIM 5.0 DATA",
    0x00550010,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00550012,
    'SQ',
    "eNTEGRA Energy Window Information Sequence",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00550013,
    'SQ',
    "eNTEGRA Energy Window Range Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550020,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "VEPRO VIF 3.0 DATA",
    0x00550020,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "VEPRO VIM 5.0 DATA",
    0x00550020,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00550022,
    'SQ',
    "eNTEGRA Detector Information Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550022,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550024,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550030,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "VEPRO VIF 3.0 DATA",
    0x00550030,
    'OB',
    "Icon Data",
    '1')
add_private_dict_entry(
    "VEPRO VIM 5.0 DATA",
    0x00550030,
    'OB',
    "Icon Data",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550032,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550034,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550040,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550042,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550044,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x00550046,
    'LO',
    "Current Ward",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0055004c,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0055004d,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550051,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "VEPRO VIM 5.0 DATA",
    0x00550051,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00550052,
    'SQ',
    "eNTEGRA Rotation Information Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550052,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550053,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00550055,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0055005c,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00550062,
    'SQ',
    "eNTEGRA Gated Information Sequence",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00550063,
    'SQ',
    "eNTEGRA Data Information Sequence",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00550064,
    'SQ',
    "SDO Double Data Sequence",
    '1')
add_private_dict_entry(
    "GEMS_GENIE_1",
    0x00550065,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "VEPRO VIF 3.0 DATA",
    0x00550065,
    'OB',
    "Image Hash Value",
    '1')
add_private_dict_entry(
    "VEPRO VIM 5.0 DATA",
    0x00550065,
    'OB',
    "Image Hash Value",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0055006d,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0055007e,
    'FL',
    "Collimator Thickness mm",
    '2')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0055007f,
    'FL',
    "Collimator Angular Resolution radians",
    '2')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x005500a8,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x005500C0,
    'SS',
    "Useful Field of View",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x005500c2,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x005500c3,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x005500c4,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x005500d0,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00570001,
    'LO',
    "Syngo MI DICOM Original Image Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00570002,
    'FL',
    "Dose Calibration Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00570003,
    'LO',
    "Units",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00570004,
    'LO',
    "Decay Correction",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00570005,
    'SL',
    "Radionuclide Half Life",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00570006,
    'FL',
    "Rescale Intercept",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00570007,
    'FL',
    "Rescale Slope",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00570008,
    'FL',
    "Frame Reference Time",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00570009,
    'SL',
    "Number of Radiopharmaceutical Information Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0057000A,
    'FL',
    "Decay Factor",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0057000B,
    'LO',
    "Counts Source",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0057000C,
    'SL',
    "Radionuclide Positron Fraction",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0057000E,
    'US',
    "Trigger Time of CT Slice",
    '1-n')
add_private_dict_entry(
    "VEPRO BROKER 1.0",
    0x00570010,
    'SQ',
    "Data Replace Sequence",
    '1')
add_private_dict_entry(
    "VEPRO BROKER 1.0 DATA REPLACE",
    0x00570020,
    'SQ',
    "Original Data Sequence",
    '1')
add_private_dict_entry(
    "VEPRO BROKER 1.0 DATA REPLACE",
    0x00570030,
    'SQ',
    "Replaced Data Sequence",
    '1')
add_private_dict_entry(
    "VEPRO BROKER 1.0 DATA REPLACE",
    0x00570040,
    'DA',
    "Date of Data Replacement",
    '1')
add_private_dict_entry(
    "VEPRO BROKER 1.0 DATA REPLACE",
    0x00570041,
    'TM',
    "Time of Data Replacement",
    '1')
add_private_dict_entry(
    "VEPRO BROKER 1.0 DATA REPLACE",
    0x00570042,
    'LO',
    "Dicom Receive Node",
    '1')
add_private_dict_entry(
    "VEPRO BROKER 1.0 DATA REPLACE",
    0x00570043,
    'LO',
    "Application Name",
    '1')
add_private_dict_entry(
    "VEPRO BROKER 1.0 DATA REPLACE",
    0x00570044,
    'LO',
    "Computer Name",
    '1')
add_private_dict_entry(
    "VEPRO DICOM TRANSFER 1.0",
    0x00590010,
    'SQ',
    "Dicom Transfer Info",
    '1')
add_private_dict_entry(
    "VEPRO DICOM RECEIVE DATA 1.0",
    0x00590040,
    'DA',
    "Receive Date",
    '1')
add_private_dict_entry(
    "VEPRO DICOM RECEIVE DATA 1.0",
    0x00590041,
    'TM',
    "Receive Time",
    '1')
add_private_dict_entry(
    "VEPRO DICOM RECEIVE DATA 1.0",
    0x00590042,
    'ST',
    "Receive Node",
    '1')
add_private_dict_entry(
    "VEPRO DICOM RECEIVE DATA 1.0",
    0x00590043,
    'ST',
    "Receive Application",
    '1')
add_private_dict_entry(
    "VEPRO DICOM RECEIVE DATA 1.0",
    0x00590050,
    'ST',
    "Receive Local Computer",
    '1')
add_private_dict_entry(
    "VEPRO DICOM RECEIVE DATA 1.0",
    0x00590051,
    'ST',
    "Receive Local AE Title",
    '1')
add_private_dict_entry(
    "VEPRO DICOM RECEIVE DATA 1.0",
    0x00590060,
    'ST',
    "Receive Remote Computer",
    '1')
add_private_dict_entry(
    "VEPRO DICOM RECEIVE DATA 1.0",
    0x00590061,
    'ST',
    "Receive Remote AE Title",
    '1')
add_private_dict_entry(
    "VEPRO DICOM RECEIVE DATA 1.0",
    0x00590070,
    'UI',
    "Receive Original Transfer Syntax",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610001,
    'FL',
    "X Principal Ray Offset",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610005,
    'FL',
    "Y Principal Ray Offset",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610009,
    'FL',
    "X Principal Ray Angle",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061000A,
    'FL',
    "Y Principal Ray Angle",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061000B,
    'FL',
    "X Short Focal Length",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061000C,
    'FL',
    "Y Short Focal Length",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061000D,
    'FL',
    "X Long Focal Length",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061000E,
    'FL',
    "Y Long Focal Length",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061000F,
    'FL',
    "X Focal Scaling",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610010,
    'FL',
    "Y Focal Scaling",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610011,
    'FL',
    "X Motion Correction Shift",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610015,
    'FL',
    "Y Motion Correction Shift",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610019,
    'FL',
    "X Heart Center",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061001A,
    'FL',
    "Y Heart Center",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061001B,
    'FL',
    "Z Heart Center",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061001C,
    'LO',
    "Image Pixel Content Type",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061001D,
    'SS',
    "Auto Save Corrected Series",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061001E,
    'LT',
    "Distorted Series Instance UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610021,
    'SS',
    "Recon Range",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610022,
    'LO',
    "Recon Orientation",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610023,
    'FL',
    "Recon Selected Angular Range",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610024,
    'FL',
    "Recon Transverse Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610025,
    'FL',
    "Recon Sagittal Angle",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610026,
    'FL',
    "Recon X Mask Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610027,
    'FL',
    "Recon Y Mask Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610028,
    'FL',
    "Recon X Image Center",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610029,
    'FL',
    "Recon Y Image Center",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061002A,
    'FL',
    "Recon Z Image Center",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061002B,
    'FL',
    "Recon X Zoom",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061002C,
    'FL',
    "Recon Y Zoom",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061002D,
    'FL',
    "Recon Threshold",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061002E,
    'FL',
    "Recon Output Pixel Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061002F,
    'LO',
    "Scatter Estimation Method",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610030,
    'LO',
    "Scatter Estimation Method Mode",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610031,
    'FL',
    "Scatter Estimation Lower Window Weights",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610032,
    'FL',
    "Scatter Estimation Upper Window Weights",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610033,
    'LO',
    "Scatter Estimation Window Mode",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610034,
    'LO',
    "Scatter Estimation Filter",
    '1-n')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610035,
    'LO',
    "Recon RawTomo Input UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610036,
    'LO',
    "Recon CT Input UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610037,
    'FL',
    "Recon Z Mask Size",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610038,
    'FL',
    "Recon X Mask Center",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610039,
    'FL',
    "Recon Y Mask Center",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x0061003A,
    'FL',
    "Recon Z Mask Center",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610051,
    'LT',
    "Raw Tomo Series UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610052,
    'LT',
    "LowRes CT Series UID",
    '1')
add_private_dict_entry(
    "SIEMENS MED NM",
    0x00610053,
    'LT',
    "HighRes CT Series UID",
    '1')
add_private_dict_entry(
    "Brainlab-S32-SO",
    0x00630001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x0063000c,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "Brainlab-S32-SO",
    0x00630010,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x00630020,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x00630021,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "BioPri3D",
    0x00630035,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Viewing Protocol",
    0x00650093,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Brainlab-S14-SSO",
    0x00670004,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710000,
    'SQ',
    "Graphic Object Sequence",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710001,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS INTELEVIEWER",
    0x00710001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "MeVis BreastCare",
    0x00710001,
    'LO',
    "XML Formatted Text Value",
    '1')
add_private_dict_entry(
    "SIEMENS WH SR 1.0",
    0x00710001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710001,
    'SL',
    "Fill Style Version",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710002,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS INTELEVIEWER",
    0x00710002,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710002,
    'FL',
    "Fill Background Color",
    '4')
add_private_dict_entry(
    "SIEMENS WH SR 1.0",
    0x00710002,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710003,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS INTELEVIEWER",
    0x00710003,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710003,
    'FL',
    "Fill Foreground Color",
    '4')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS INTELEVIEWER",
    0x00710004,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710004,
    'SL',
    "Fill Mode",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710005,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS INTELEVIEWER",
    0x00710005,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710005,
    'OB',
    "Fill Pattern",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710006,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS INTELEVIEWER",
    0x00710006,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710006,
    'SL',
    "Line Style Version",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710007,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS INTELEVIEWER",
    0x00710007,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710007,
    'FL',
    "Line Background Color",
    '4')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710008,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710008,
    'FL',
    "Line Foreground Color",
    '4')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710009,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710009,
    'DS',
    "Line Type",
    '1')
add_private_dict_entry(
    "INTELERAD MEDICAL SYSTEMS INTELEVIEWER",
    0x0071000A,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071000a,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710010,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710010,
    'DS',
    "Line Thickness",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710011,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710011,
    'DS',
    "Line Shadow X Offset",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710012,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710012,
    'DS',
    "Line Shadow Y Offset",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710013,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710013,
    'DS',
    "Shadow Style",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710014,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710014,
    'FL',
    "Shadow Color",
    '4')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710015,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710015,
    'DS',
    "Stipple Pattern",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710016,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710016,
    'DS',
    "Line Anti Aliasing",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710017,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710017,
    'CS',
    "Line-Z-Blend Flag",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710018,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00710018,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710018,
    'SL',
    "Text Style Version",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00710019,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710019,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710019,
    'FL',
    "Text Color",
    '4')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x0071001a,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071001b,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x0071001c,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071001c,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071001d,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x0071001e,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00710020,
    'FL',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710020,
    'SL',
    "Text Horizontal Align",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO REGISTRATION",
    0x00710020,
    'SQ',
    "Registered Image Sequence",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00710021,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO REGISTRATION",
    0x00710021,
    'CS',
    "Registration Is Validated Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710021,
    'SL',
    "Text Vertical Align",
    '1')
add_private_dict_entry(
    "SIEMENS MED PT",
    0x00710021,
    'UI',
    "Registration Matrix UID",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00710022,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710022,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710022,
    'DS',
    "Text Shadow X Offset",
    '1')
add_private_dict_entry(
    "SIEMENS MED PT",
    0x00710022,
    'DT',
    "Decay Correction DateTime",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00710023,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710023,
    'DS',
    "Text Shadow Y Offset",
    '1')
add_private_dict_entry(
    "SIEMENS MED PT",
    0x00710023,
    'US',
    "Volume Index",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00710024,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED PT",
    0x00710024,
    'IS',
    "Time Slice Duration",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710024,
    'SL',
    "Text Shadow Style",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710025,
    'FL',
    "Text Shadow Color",
    '4')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710026,
    'CS',
    "Text Log Font",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710027,
    'CS',
    "Text-Z-Blend Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710028,
    'OB',
    "Graphic Bit Mask",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710029,
    'CS',
    "Visiblility Flag",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x0071002b,
    'FD',
    "?",
    '1-n')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x0071002c,
    'FD',
    "?",
    '3')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071002c,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x0071002d,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071002d,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071002e,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710030,
    'SL',
    "Graphic Sensitivity",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710031,
    'SL',
    "Graphic Pick Mode Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710032,
    'SL',
    "Graphic Layer",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710033,
    'SL',
    "Graphic Object Version",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710034,
    'SL',
    "Graphic Coordinate System",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710035,
    'CS',
    "Graphic Custom Attributes",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710036,
    'CS',
    "Graphic Custom Attributes Key",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710037,
    'CS',
    "Graphic Custom Attributes Value",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710038,
    'CS',
    "Graphic View Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710039,
    'DS',
    "Graphic Data",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710040,
    'CS',
    "Graphic Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710041,
    'US',
    "Number of Graphic Points",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710042,
    'DS',
    "Axis Main Tick Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710043,
    'DS',
    "Axis Detail Tick Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710044,
    'DS',
    "Axis Main Tick Spacing",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710045,
    'DS',
    "Axis Detail Tick Spacing",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710046,
    'DS',
    "Axis Main Tick Count",
    '1')
add_private_dict_entry(
    "SIEMENS MED PT WAVEFORM",
    0x00710046,
    'UN',
    "Starting Respiratory Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710047,
    'DS',
    "Axis Detail Tick Count",
    '1')
add_private_dict_entry(
    "SIEMENS MED PT WAVEFORM",
    0x00710047,
    'UN',
    "Starting Respiratory Phase",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710048,
    'SL',
    "Axis Tick Behavior",
    '1')
add_private_dict_entry(
    "SIEMENS MED PT WAVEFORM",
    0x00710048,
    'UN',
    "Ending Respiratory Amplitude",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710049,
    'SL',
    "Axis Tick Aligment",
    '1')
add_private_dict_entry(
    "SIEMENS MED PT WAVEFORM",
    0x00710049,
    'UN',
    "Ending Respiratory Phase",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710050,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS MED PT WAVEFORM",
    0x00710050,
    'CS',
    "Respiratory Trigger Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710050,
    'DS',
    "Axis Step",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710051,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710051,
    'SL',
    "Axis Step Index",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710052,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710052,
    'CS',
    "Axis Text Format",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710053,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710053,
    'CS',
    "Axis Show Center Text Flag",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710054,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710054,
    'CS',
    "Axis Show Tick Text Flag",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710055,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710055,
    'DS',
    "Bitmap X Orientation",
    '3')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710056,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710056,
    'DS',
    "Bitmap Y Orientation",
    '3')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710057,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710057,
    'OB',
    "Graphic Blob",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710058,
    'CS',
    "Graphic Interpolation",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710059,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710059,
    'DS',
    "Graphic Angle",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071005a,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071005b,
    'FL',
    "?",
    '2')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071005c,
    'FL',
    "?",
    '4')
add_private_dict_entry(
    "AgilityOverlay",
    0x0071005d,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "AgilityOverlay",
    0x00710060,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710060,
    'DS',
    "Graphic Size",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710061,
    'CS',
    "Cut Line Side",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710062,
    'DS',
    "Graphic Tip Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710063,
    'DS',
    "Cut Line Arrow Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710064,
    'DS',
    "Line Gap Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710065,
    'DS',
    "Graphic Circle Radius",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710066,
    'DS',
    "Line Distance Move",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710067,
    'DS',
    "Line Marker Length",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710068,
    'DS',
    "Graphic Center",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710069,
    'DS',
    "Range Center Area Top Left",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710070,
    'DS',
    "Range Center Area Bottom Right",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710071,
    'DS',
    "Range Tilt",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710072,
    'DS',
    "Range Minimum Tilt",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710073,
    'DS',
    "Range Maximum Tilt",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710074,
    'DS',
    "Graphic Width",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710075,
    'DS',
    "Range Minimum Width",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710076,
    'DS',
    "Range Maximum Width",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710077,
    'DS',
    "Graphic Height",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710078,
    'DS',
    "Range Feed",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710079,
    'CS',
    "Range Direction",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710080,
    'CS',
    "Range Show Scans",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710081,
    'DS',
    "Range Minimum Scan Distance",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710082,
    'CS',
    "Range Orthogonal Height",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710083,
    'DS',
    "Graphic Position",
    '3')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710084,
    'CS',
    "Graphic Closed Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710085,
    'SL',
    "Range Line Tip Mode",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710086,
    'SL',
    "Graphic List Count",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710087,
    'CS',
    "Axis Flip Text Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710088,
    'CS',
    "Curve Diagram Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710089,
    'DS',
    "Graphic Start Angle",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710090,
    'DS',
    "Graphic End Angle",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710091,
    'IS',
    "Live Wire Smoothness",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710092,
    'CS',
    "Live Wire Spline Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710093,
    'CS',
    "Ellipse Circle Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710094,
    'CS',
    "Graphic Square Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710095,
    'DS',
    "Curve Section Start Index",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710096,
    'DS',
    "Curve Section End Index",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710097,
    'DS',
    "Marker Alpha",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710098,
    'IS',
    "Table Row Count",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x00710099,
    'IS',
    "Table Column Count",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x0071009A,
    'DS',
    "Table Row Height",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x0071009B,
    'DS',
    "Table Column Width",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x0071009C,
    'IS',
    "Rectangle Selection Segment Offset",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x0071009D,
    'CS',
    "Graphic Text",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A0,
    'SL',
    "Axis Tick Spacing Coordinate System",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A1,
    'CS',
    "Axis Diagram Grid Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A2,
    'SL',
    "Polar Plot Circle Count",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A3,
    'SL',
    "Polar Plot Lines-per-Circle",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A4,
    'SL',
    "Polar Plot Compartment Count",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A5,
    'SL',
    "Polar Plot Radius Weight",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A6,
    'DS',
    "Circle Segment Outer Radius",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A7,
    'CS',
    "Circle Segment Clockwise Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A8,
    'CS',
    "Axis Diagram Auto Resize Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100A9,
    'DS',
    "Axis Diagram Step Start",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100B0,
    'CS',
    "Group Root",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100B1,
    'ST',
    "Group Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100B2,
    'SQ',
    "Graphic Annotation Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100B3,
    'SL',
    "Text Minimum Height",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100B4,
    'DS',
    "Text Font Scaling Factor",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100B5,
    'SL',
    "Text Maximum Extensions",
    '2')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100B6,
    'CS',
    "Text Segment Size",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO OBJECT GRAPHICS",
    0x007100B7,
    'SL',
    "Graphic Object Reference Label",
    '1')
add_private_dict_entry(
    "STENTOR",
    0x00730001,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730002,
    'US',
    "Hanging Protocol Excellence Rank",
    '1')
add_private_dict_entry(
    "STENTOR",
    0x00730002,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "STENTOR",
    0x00730003,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730004,
    'CS',
    "Template Data Role ID",
    '1')
add_private_dict_entry(
    "STENTOR",
    0x00730004,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730006,
    'CS',
    "Data Sharing Flag",
    '1')
add_private_dict_entry(
    "STENTOR",
    0x00730006,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730008,
    'SQ',
    "Bagging Operations Sequence",
    '1')
add_private_dict_entry(
    "Brainlab-S23-ProjectiveFusion",
    0x00730010,
    'SQ',
    "Projective Registration Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730010,
    'LO',
    "Synchronization Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730012,
    'LO',
    "Custom Filter Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730014,
    'LO',
    "Custom Sorter Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730016,
    'CS',
    "Reference Template Data Role ID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730018,
    'CS',
    "Model Template Data Role ID",
    '1')
add_private_dict_entry(
    "GEMS_IDI_01",
    0x00730020,
    'DS',
    "Height Map Plane Distance",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730020,
    'DT',
    "Selector DT Value",
    '1-n')
add_private_dict_entry(
    "GEMS_IDI_01",
    0x00730021,
    'DS',
    "Height Map Plane Offset",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730022,
    'DA',
    "Selector DA Value",
    '1-n')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00730023,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00730024,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730024,
    'TM',
    "Selector TM Value",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730026,
    'UI',
    "Selector UI Value",
    '1-n')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00730028,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730028,
    'CS',
    "Referenced Template Data Role",
    '1')
add_private_dict_entry(
    "GEMS_IDI_01",
    0x00730030,
    'OW',
    "Height Map Plane Indices",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730030,
    'SQ',
    "Custom Property Sequence",
    '1')
add_private_dict_entry(
    "GEMS_IDI_01",
    0x00730031,
    'OW',
    "X Map Plane Indices",
    '1')
add_private_dict_entry(
    "GEMS_IDI_01",
    0x00730032,
    'OW',
    "Y Map Plane Indices",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730032,
    'CS',
    "Custom Property Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730034,
    'LO',
    "Custom Property Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730036,
    'LO',
    "Custom Property Value",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730038,
    'SQ',
    "Layout Property Sequence",
    '1')
add_private_dict_entry(
    "GEMS_IDI_01",
    0x00730040,
    'DS',
    "Central Projection Detector Secondary Angle",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730040,
    'SQ',
    "Synchronization Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730042,
    'CS',
    "Presentation Creator Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730044,
    'CS',
    "Cine Navigation Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730046,
    'CS',
    "Internal Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730048,
    'LO',
    "Semantic Naming Strategy",
    '1')
add_private_dict_entry(
    "GEMS_IDI_01",
    0x00730050,
    'DS',
    "Detector Active Dimensions",
    '2')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730050,
    'LO',
    "Parameter String",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730052,
    'CS',
    "Sorting Order",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730054,
    'CS',
    "syngo Template Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730056,
    'CS',
    "Sorter Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730058,
    'SH',
    "Data Display Protocol Version",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073005A,
    'CS',
    "Timepoint Value",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073005B,
    'CS',
    "Sharing Group Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073005C,
    'CS',
    "Template Selector Operator",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073005D,
    'CS',
    "Sharing Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730060,
    'SQ',
    "Viewport Definitions Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730062,
    'CS',
    "Protocol Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730064,
    'SQ',
    "Template Selector Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730066,
    'CS',
    "Default Template",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730068,
    'CS',
    "Is Preferred",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073006A,
    'SQ',
    "Timepoint Initial Value Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073006C,
    'CS',
    "Timepoint Variable",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730070,
    'SH',
    "Display Protocol Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730072,
    'LO',
    "Display Protocol Description",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730074,
    'CS',
    "Display Protocol Level",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730076,
    'LO',
    "Display Protocol Creator",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730078,
    'DT',
    "Display Protocol Creation Datetime",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073007A,
    'UI',
    "Referenced Data Protocol",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073007C,
    'US',
    "Display Protocol Excellence Rank",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073007E,
    'SQ',
    "Layout Sequence",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00730080,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730080,
    'US',
    "Layout Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730082,
    'LO',
    "Layout Description",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730084,
    'SQ',
    "Segment Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730086,
    'US',
    "Segment Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730088,
    'LO',
    "Segment Description",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073008A,
    'CS',
    "Segment Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073008C,
    'US',
    "Tile Horizontal Dimension",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073008E,
    'US',
    "Tile Vertical Dimension",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730090,
    'CS',
    "Fill Order",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730092,
    'CS',
    "Segment Small Scroll Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730094,
    'US',
    "Segment Small Scroll Amount",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730096,
    'CS',
    "Segment Large Scroll Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x00730098,
    'US',
    "Segment Large Scroll Amount",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073009A,
    'US',
    "Segment Overlap Priority",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073009C,
    'SQ',
    "Data Role View Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x0073009E,
    'US',
    "Data Role View Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300A2,
    'US',
    "Referenced Data Role",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300A4,
    'CS',
    "Sharing Enabled",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300A8,
    'US',
    "Referenced Data Role Views",
    '2-n')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300B0,
    'SH',
    "Data Protocol Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300B2,
    'LO',
    "Data Protocol Description",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300B4,
    'CS',
    "Data Protocol Level",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300B6,
    'LO',
    "Data Protocol Creator",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300B8,
    'DT',
    "Data Protocol Creation Datetime",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300BA,
    'US',
    "Data Protocol Excellence Rank",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300BC,
    'SQ',
    "Data Protocol Definition Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300BE,
    'SQ',
    "Data Role Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300C0,
    'US',
    "Data Role Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300C2,
    'SH',
    "Data Role Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300C6,
    'SQ',
    "Selector Operations Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300C8,
    'CS',
    "Selector Usage Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300CA,
    'CS',
    "Select by Attribute Presence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300CC,
    'CS',
    "Select by Category",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300CE,
    'CS',
    "Select by Operator",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300D0,
    'LO',
    "Custom Selector Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300D2,
    'CS',
    "Selector Operator",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300D4,
    'CS',
    "Reformatting Required",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300D6,
    'SQ',
    "Registration Data Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300D8,
    'US',
    "Reference Data Role Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300DA,
    'SQ',
    "Model Data Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300DC,
    'US',
    "Model Data Role Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300DE,
    'SQ',
    "Fusion Display Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300E0,
    'FD',
    "Transparency",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300E2,
    'CS',
    "Time Point",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300E4,
    'LO',
    "First Time Point Token",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300E6,
    'LO',
    "Last Time Point Token",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300E8,
    'LO',
    "Intermediate Time Point Token",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300EA,
    'SQ',
    "Data Processor Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300EC,
    'LO',
    "Data Processor Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300EE,
    'SQ',
    "Template Data Role Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300F0,
    'SQ',
    "View Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300F4,
    'LO',
    "View Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300F6,
    'LO',
    "Custom Bagging Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300F8,
    'US',
    "Referenced Display Segment Number",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300FA,
    'LO',
    "Data Role Type",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300FC,
    'CS',
    "Unassigned Flag",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300FE,
    'CS',
    "Initial Display Scroll Position",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO LAYOUT PROTOCOL",
    0x007300FF,
    'LO',
    "VRT Preset",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00750010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770010,
    'LO',
    "Evidence Document Template Name",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770010,
    'UI',
    "Original Series/Study UID",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770011,
    'DS',
    "Evidence Document Template Version",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770012,
    'UI',
    "Original SOP UID",
    '1-n')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770014,
    'LO',
    "Referenced Volume ID",
    '1-n')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770016,
    'CS',
    "Binary Data Name SCS",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770020,
    'OB',
    "Clinical Finding Data",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770020,
    'LO',
    "Binary Data Name",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770021,
    'OB',
    "Metadata",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770022,
    'CS',
    "Number of SOP Instance UID",
    '1-n')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770024,
    'CS',
    "Number of Series Instance UID",
    '1-n')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770026,
    'US',
    "Number of Binary Data",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770028,
    'CS',
    "Binary Data Type",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770030,
    'DS',
    "Implementation Version",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770030,
    'UL',
    "Binary Data Size",
    '1-n')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770032,
    'LO',
    "Binary Data SubType",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770040,
    'OB',
    "Predecessor",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770040,
    'LO',
    "Additional Information",
    '1-n')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770050,
    'LO',
    "Logical ID",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770050,
    'OB',
    "First Binary Data",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770060,
    'OB',
    "Application Data",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770060,
    'OB',
    "First Thumbnail",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770070,
    'LO',
    "Owner Clinical Task Name",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770070,
    'LO',
    "Algorithm ID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770071,
    'LO',
    "Owner Task Name",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770072,
    'OB',
    "Owner Supported Templates",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO EVIDENCE DOCUMENT DATA",
    0x00770080,
    'OB',
    "Volume Catalog",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770080,
    'LO',
    "Volume ID",
    '1')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770084,
    'LO',
    "COF Object UID",
    '1-n')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770086,
    'LO',
    "Workflow Scene Status",
    '1-n')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770088,
    'UI',
    "Reference SOP Instance UIDs",
    '1-n')
add_private_dict_entry(
    "TERARECON AQUARIUS",
    0x00770090,
    'FL',
    "COF Refinement Level",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790000,
    'LO',
    "Analgesia",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790001,
    'LO',
    "Anesthesia",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790002,
    'IS',
    "Bed Motion",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790003,
    'LO',
    "Food Access",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790004,
    'DS',
    "Histogram Version",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790006,
    'DS',
    "Injection Decay Correction",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790007,
    'LO',
    "Isotope",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790008,
    'LO',
    "Other Drugs",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790009,
    'IS',
    "RebinningType",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x0079000A,
    'DS',
    "Rebinning Version",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x0079000B,
    'IS',
    "Reconstruction",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x0079000C,
    'DS',
    "ReconstructionVersion",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x0079000D,
    'LO',
    "Injected Compounds",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x0079000E,
    'LO',
    "Study Model",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x0079000F,
    'LO',
    "Subject Genus",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790010,
    'LO',
    "Subject Phenotype",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790011,
    'DS',
    "Version",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790012,
    'LO',
    "Water Access",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790013,
    'DS',
    "X Offset",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790014,
    'DS',
    "Y Offset",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790015,
    'DS',
    "Zoom",
    '1')
add_private_dict_entry(
    "SMIL_PB79",
    0x00790017,
    'IS',
    "Subject Orientation",
    '1')
add_private_dict_entry(
    "SMIO_PB7B",
    0x007B0000,
    'LO',
    "Units",
    '1')
add_private_dict_entry(
    "SMIO_PB7D",
    0x007D0001,
    'UL',
    "Geometry",
    '1')
add_private_dict_entry(
    "SMIO_PB7D",
    0x007D0002,
    'FL',
    "Spacing",
    '1')
add_private_dict_entry(
    "SMIO_PB7D",
    0x007D0003,
    'FL',
    "Origin",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00870001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00870002,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00870003,
    'SL',
    "?",
    '2')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00870004,
    'SL',
    "?",
    '2')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00870005,
    'FD',
    "?",
    '2')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00870006,
    'FD',
    "?",
    '2')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00870007,
    'FD',
    "?",
    '2')
add_private_dict_entry(
    "AGFA-AG_HPState",
    0x00870008,
    'FD',
    "?",
    '2')
add_private_dict_entry(
    "1.2.840.113708.794.1.1.2.0",
    0x00870010,
    'CS',
    "Media Type",
    '1')
add_private_dict_entry(
    "1.2.840.113708.794.1.1.2.0",
    0x00870010,
    'CS',
    "Media Type",
    '1')
add_private_dict_entry(
    "1.2.840.113708.794.1.1.2.0",
    0x00870020,
    'CS',
    "Media Location",
    '1')
add_private_dict_entry(
    "1.2.840.113708.794.1.1.2.0",
    0x00870020,
    'CS',
    "Media Location",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ENCAPSULATED DOCUMENT DATA",
    0x00870020,
    'OB',
    "Study Model",
    '1')
add_private_dict_entry(
    "1.2.840.113708.794.1.1.2.0",
    0x00870030,
    'ST',
    "Storage File ID",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ENCAPSULATED DOCUMENT DATA",
    0x00870030,
    'OB',
    "Report XML Schema",
    '1')
add_private_dict_entry(
    "1.2.840.113708.794.1.1.2.0",
    0x00870040,
    'DS',
    "Study or Image Size in MB",
    '1')
add_private_dict_entry(
    "SIEMENS SYNGO ENCAPSULATED DOCUMENT DATA",
    0x00870040,
    'OB',
    "Report Identifier",
    '1')
add_private_dict_entry(
    "1.2.840.113708.794.1.1.2.0",
    0x00870050,
    'IS',
    "Estimated Retrieve Time",
    '1')
add_private_dict_entry(
    "1.2.840.113708.794.1.1.2.0",
    0x00870050,
    'IS',
    "Estimated Retrieve Time",
    '1')
add_private_dict_entry(
    "DIDI TO PCR 1.1",
    0x00890010,
    'SQ',
    "Stamp Image Sequence",
    '1')
add_private_dict_entry(
    "POLYTRON-SMS 2.5",
    0x00890010,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "PMS-THORA-5.1",
    0x00890020,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00910020,
    'PN',
    "RIS Patient Name",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00930002,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00950001,
    'LO',
    "Examination Folder ID",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00950004,
    'UL',
    "Folder Reported Status",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00950005,
    'LO',
    "Folder Reporting Radiologist",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00950007,
    'LO',
    "SIENET ISA PLA",
    '1')
add_private_dict_entry(
    "SIENET",
    0x0095000c,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00950020,
    'PN',
    "RIS Patient Name",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00970003,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00970005,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "QTUltrasound",
    0x00990000,
    'SS',
    "Breast Density Value",
    '1')
add_private_dict_entry(
    "NQHeader",
    0x00990001,
    'UI',
    "Version",
    '1')
add_private_dict_entry(
    "SYNARC_1.0",
    0x00990001,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "NQHeader",
    0x00990002,
    'UI',
    "Analyzed Series UID",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00990002,
    'SL',
    "Data Object Attributes",
    '1')
add_private_dict_entry(
    "SYNARC_1.0",
    0x00990002,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "NQHeader",
    0x00990003,
    'LT',
    "License",
    '1')
add_private_dict_entry(
    "SYNARC_1.0",
    0x00990003,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "NQHeader",
    0x00990004,
    'SS',
    "Return Code",
    '1')
add_private_dict_entry(
    "SYNARC_1.0",
    0x00990004,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "NQHeader",
    0x00990005,
    'LT',
    "Return Message",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00990005,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "SYNARC_1.0",
    0x00990005,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "NQHeader",
    0x00990010,
    'FL',
    "MI",
    '1')
add_private_dict_entry(
    "NQHeader",
    0x00990020,
    'SH',
    "Units",
    '1')
add_private_dict_entry(
    "NQHeader",
    0x00990021,
    'FL',
    "ICV",
    '1')
add_private_dict_entry(
    "SIENET",
    0x00A50005,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10001,
    'US',
    "Data Dictionary Version",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10005,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10006,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10007,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10014,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10018,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10021,
    'DS',
    "DLP Total",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10022,
    'DS',
    "Presentation Relative Center",
    '2')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10023,
    'DS',
    "Presentation Relative Part",
    '2')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10024,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10025,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10030,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10031,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10032,
    'US',
    "?",
    '2')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10037,
    'DS',
    "Total Dose Savings",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10039,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E1003E,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E1003F,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10040,
    'SH',
    "Image Label",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10041,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10042,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10043,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10050,
    'DS',
    "Acquisition Duration",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10051,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10060,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10061,
    'LO',
    "Protocol File Name",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10062,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10063,
    'SH',
    "Patient Language",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E10065,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E1006A,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E1006B,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E100A0,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E100C2,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E100C4,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E100CF,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E100EB,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x00E100EC,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PM",
    0x01010005,
    'LO',
    "Image Enhancement Parameter File",
    '1-n')
add_private_dict_entry(
    "PM",
    0x01010006,
    'IS',
    "Original Sigmoid Ratio",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170010,
    'SQ',
    "Parameter Sequence",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170012,
    'CS',
    "Parameter Type",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170014,
    'LO',
    "Parameter Name",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170016,
    'LO',
    "Parameter Description",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170018,
    'DS',
    "Floating Parameter Value",
    '1-n')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170019,
    'IS',
    "Integer Parameter Value",
    '1-n')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x0117001a,
    'LO',
    "String Parameter Value",
    '1-n')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170020,
    'SQ',
    "VOILPS",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170022,
    'SQ',
    "OMIT Region Sequence",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170024,
    'SQ',
    "QC Sequence",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170030,
    'IS',
    "Total phases",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170031,
    'DS',
    "Acquisition Duration",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170032,
    'DS',
    "Acquisition Start Times",
    '1-n')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170033,
    'TM',
    "Injection Time",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170034,
    'DS',
    "Effective Acquisition Delay",
    '1-n')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170035,
    'IS',
    "Signal Enhancement Ratio (SER) Timing Indices",
    '3')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x0117003a,
    'LO',
    "Timing Information Method",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x0117003b,
    'LT',
    "Timing Information Comments",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170041,
    'IS',
    "VOILPS ROI Flag",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170042,
    'DS',
    "VOILPS Center",
    '3')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170043,
    'DS',
    "VOILPS HalfWidth",
    '3')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170044,
    'DS',
    "VOILPS HalfHeight",
    '3')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170045,
    'DS',
    "VOILPS HalfDepth",
    '3')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170046,
    'CS',
    "VOILPS Type",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170050,
    'US',
    "Projected ROI Number of Pixels",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170051,
    'IS',
    "Projection Axis",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170052,
    'IS',
    "Projected ROI Transpose Flag",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170053,
    'US',
    "Projected ROI X Vertices",
    '3-n')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170054,
    'US',
    "Projected ROI Y Vertices",
    '3-n')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170055,
    'US',
    "Projected ROI Z Range",
    '2')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170056,
    'CS',
    "Projected ROI Type",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x01170057,
    'LO',
    "Projected ROI Label",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700a1,
    'US',
    "VOI Pixel Start",
    '3')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700a2,
    'US',
    "VOI Pixel End",
    '3')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700b0,
    'SQ',
    "Functional Tumor Volume (FTV) Results Sequence",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700b1,
    'DS',
    "Signal Enhancement Ratio (SER) Minimum",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700b2,
    'DS',
    "Signal Enhancement Ratio (SER) Maximum",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700b3,
    'IS',
    "Voxel Count",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700b4,
    'DS',
    "Volume (cc)",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700b5,
    'LO',
    "Label",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700c0,
    'CS',
    "QC Type",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700c1,
    'LO',
    "QC Factor",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700c2,
    'DS',
    "QC Value",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700c3,
    'CS',
    "QC Meaning",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700c4,
    'LT',
    "QC Comment",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700c5,
    'CS',
    "Protocol Compliance",
    '1')
add_private_dict_entry(
    "UCSF BIRP PRIVATE CREATOR 011710xx",
    0x011700c6,
    'LO',
    "Protocol Non-compliance Reasons",
    '1-n')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190000,
    'LO',
    "Acoustic Meta Information Version",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190001,
    'OB',
    "Common Acoustic Meta Information",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190002,
    'SQ',
    "Multi Stream Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190003,
    'SQ',
    "Acoustic Data Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190004,
    'OB',
    "Per Transaction Acoustic Control Information",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190005,
    'UL',
    "Acoustic Data Offset",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190006,
    'UL',
    "Acoustic Data Length",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190007,
    'UL',
    "Footer Offset",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190008,
    'UL',
    "Footer Length",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190009,
    'SS',
    "Acoustic Stream Number",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190010,
    'SH',
    "Acoustic Stream Type",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190011,
    'UN',
    "Stage Timer Time",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190012,
    'UN',
    "Stop Watch Time",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190013,
    'IS',
    "Volume Rate",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01190021,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290000,
    'SQ',
    "MPR View Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290002,
    'UI',
    "Bookmark UID",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290003,
    'UN',
    "Plane Origin Vector",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290004,
    'UN',
    "Row Vector",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290005,
    'UN',
    "Column Vector",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290006,
    'SQ',
    "Visualization Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290007,
    'UI',
    "Bookmark UID",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290008,
    'OB',
    "Visualization Information",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290009,
    'SQ',
    "Application State Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290010,
    'OB',
    "Application State Information",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290011,
    'SQ',
    "Referenced Bookmark Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290012,
    'UI',
    "Referenced Bookmark UID",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290020,
    'SQ',
    "Cine Parameters Sequence",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290021,
    'OB',
    "Cine Parameters Schema",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290022,
    'OB',
    "Values of Cine Parameters",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290029,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01290030,
    'CS',
    "Raw Data Object Type",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01390001,
    'SL',
    "Physio Capture ROI",
    '1')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01490001,
    'FD',
    "Vector of BROI Points",
    '1-n')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01490002,
    'FD',
    "Start/End Timestamps of Strip Stream",
    '1-n')
add_private_dict_entry(
    "SIEMENS Ultrasound SC2000",
    0x01490003,
    'FD',
    "Timestamps of Visible R-waves",
    '1-n')
add_private_dict_entry(
    "SIEMENS ISI",
    0x01930002,
    'DS',
    "RIS Key",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990001,
    'FL',
    "Left Cortical White Matter",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990002,
    'FL',
    "Left Cortical Gray Matter",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990003,
    'FL',
    "Left 3rd Ventricle",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990004,
    'FL',
    "Left 4th Ventricle",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990005,
    'FL',
    "Left 5th Ventricle",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990006,
    'FL',
    "Left Lateral Ventricle",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990007,
    'FL',
    "Left Inferior Lateral Ventricle",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990008,
    'FL',
    "Left Inferior CSF",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990009,
    'FL',
    "Left Cerebellar White Matter",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199000a,
    'FL',
    "Left Cerebellar Gray Matter",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199000b,
    'FL',
    "Left Hippocampus",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199000c,
    'FL',
    "Left Amygdala",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199000d,
    'FL',
    "Left Thalamus",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199000e,
    'FL',
    "Left Caudate",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199000f,
    'FL',
    "Left Putamen",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990010,
    'FL',
    "Left Pallidum",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990011,
    'FL',
    "Left Ventral Diencephalon",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990012,
    'FL',
    "Left Nucleus Accumbens",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990013,
    'FL',
    "Left Brain Stem",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990014,
    'FL',
    "Left Exterior CSF",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990015,
    'FL',
    "Left WM Hypo",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990016,
    'FL',
    "Left Other",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990017,
    'FL',
    "Left Cortex Unkown",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990018,
    'FL',
    "Left Cortex Bankssts",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990019,
    'FL',
    "Left Cortex Caudal Anterior Cingulate",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199001a,
    'FL',
    "Left Cortex Caudal Middle Frontal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199001b,
    'FL',
    "Left Cortex Corpus Callosum",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199001c,
    'FL',
    "Left Cortex Cuneus",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199001d,
    'FL',
    "Left Cortex Entorhinal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199001e,
    'FL',
    "Left Cortex Fusiform",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199001f,
    'FL',
    "Left Cortex Inferior Parietal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990020,
    'FL',
    "Left Cortex Inferior Temporal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990021,
    'FL',
    "Left Cortex Isthmus Cingulate",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990022,
    'FL',
    "Left Cortex Lateral Occipital",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990023,
    'FL',
    "Left Cortex Lateral Orbito Frontal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990024,
    'FL',
    "Left Cortex Lingual",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990025,
    'FL',
    "Left Cortex Medial Orbito Frontal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990026,
    'FL',
    "Left Cortex Middle Temporal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990027,
    'FL',
    "Left Cortex Parahippocampal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990028,
    'FL',
    "Left Cortex Paracentral",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990029,
    'FL',
    "Left Cortex Pars Opercularis",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199002a,
    'FL',
    "Left Cortex Pars Orbitalis",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199002b,
    'FL',
    "Left Cortex Pars Triangularis",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199002c,
    'FL',
    "Left Cortex Pericalcarine",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199002d,
    'FL',
    "Left Cortex Postcentral",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199002e,
    'FL',
    "Left Cortex Posterior Cingulate",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199002f,
    'FL',
    "Left Cortex Precentral",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990030,
    'FL',
    "Left Cortex Precuneus",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990031,
    'FL',
    "Left Cortex Rostral Anterior Cingulate",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990032,
    'FL',
    "Left Cortex Rostral Middle Frontal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990033,
    'FL',
    "Left Cortex Superior Frontal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990034,
    'FL',
    "Left Cortex Superior Parietal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990035,
    'FL',
    "Left Cortex Superior Temporal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990036,
    'FL',
    "Left Cortex Supramarginal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990037,
    'FL',
    "Left Cortex Frontal Pole",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990038,
    'FL',
    "Left Cortex Temporal Pole",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x01990039,
    'FL',
    "Left Cortex Transvere Temporal",
    '1')
add_private_dict_entry(
    "NQLeft",
    0x0199003a,
    'FL',
    "Left Meningie",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01E10018,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01E10021,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01E10026,
    'CS',
    "Phantom Type",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01E10034,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01E10040,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01E10041,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01E10055,
    'SQ',
    "Reference Sequence",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01E10056,
    'CS',
    "Reference Type",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01E10057,
    'CS',
    "Reference Level",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10001,
    'CS',
    "Acquisition Type",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10002,
    'CS',
    "Focal Spot Resolution",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10003,
    'CS',
    "Concurrent Slices Generation",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10004,
    'CS',
    "Angular Sampling Density",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10005,
    'DS',
    "Reconstruction Arc",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10007,
    'DS',
    "Table Velocity",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10008,
    'DS',
    "Acquisition Length",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1000A,
    'US',
    "Edge Enhancement Weight",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1000C,
    'DS',
    "Scanner Relative Center",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1000D,
    'DS',
    "Rotation Angle",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1000E,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10026,
    'DS',
    "Pitch",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10027,
    'DS',
    "Rotation Time",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10028,
    'DS',
    "Table Increment",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10030,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10032,
    'CS',
    "Image View Convention",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10033,
    'DS',
    "Cycle Time",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10036,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10037,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10038,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10039,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10040,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10042,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10043,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10044,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10045,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10046,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10047,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10049,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1004A,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1004B,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1004C,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1004D,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1004E,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F1004F,
    'US',
    "Detectors Layers",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F10053,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30001,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30002,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30003,
    'FL',
    "?",
    '2')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30004,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30011,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30012,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30013,
    'FL',
    "?",
    '2')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30014,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30015,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30016,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30017,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30018,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30019,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30023,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F30024,
    'IS',
    "?",
    '2')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70010,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70011,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70013,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70014,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70015,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70016,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70017,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70018,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70019,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7001A,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7001B,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7001C,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7001E,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7001F,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70022,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70023,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70025,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70026,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70027,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70028,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70029,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7002B,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7002C,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7002D,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7002E,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70030,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70031,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7005C,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70070,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70073,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70074,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F70075,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7007F,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F7009B,
    'IS',
    "iDose Level",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F700CB,
    'DS',
    "keV",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F700CC,
    'ST',
    "SBI Version",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F700CD,
    'CS',
    "SC CT Equivalent",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F700CE,
    'LT',
    "Reference SBI Type",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F700D3,
    'LT',
    "Burned Spectral Annotations",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F700D4,
    'SH',
    "Head Body",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F700D6,
    'IS',
    "Spectral Level",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F90001,
    'LO',
    "SP Filter",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F90004,
    'IS',
    "Adaptive Filter",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F90005,
    'IS',
    "Recon Increment",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F90008,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x01F90009,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Riverain Medical",
    0x02030000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Riverain Medical",
    0x02030001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Riverain Medical",
    0x02030002,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Riverain Medical",
    0x02030003,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Riverain Medical",
    0x02030010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Riverain Medical",
    0x020300f0,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "Riverain Medical",
    0x020300f1,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990001,
    'FL',
    "Right Cortical White Matter",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990002,
    'FL',
    "Right Cortical Gray Matter",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990003,
    'FL',
    "Right 3rd Ventricle",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990004,
    'FL',
    "Right 4th Ventricle",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990005,
    'FL',
    "Right 5th Ventricle",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990006,
    'FL',
    "Right Lateral Ventricle",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990007,
    'FL',
    "Right Inferior Lateral Ventricle",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990008,
    'FL',
    "Right Inferior CSF",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990009,
    'FL',
    "Right Cerebellar White Matter",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299000a,
    'FL',
    "Right Cerebellar Gray Matter",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299000b,
    'FL',
    "Right Hippocampus",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299000c,
    'FL',
    "Right Amygdala",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299000d,
    'FL',
    "Right Thalamus",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299000e,
    'FL',
    "Right Caudate",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299000f,
    'FL',
    "Right Putamen",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990010,
    'FL',
    "Right Pallidum",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990011,
    'FL',
    "Right Ventral Diencephalon",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990012,
    'FL',
    "Right Nucleus Accumbens",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990013,
    'FL',
    "Right Brain Stem",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990014,
    'FL',
    "Right Exterior CSF",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990015,
    'FL',
    "Right WM Hypo",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990016,
    'FL',
    "Right Other",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990017,
    'FL',
    "Right Cortex Unkown",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990018,
    'FL',
    "Right Cortex Bankssts",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990019,
    'FL',
    "Right Cortex Caudal Anterior Cingulate",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299001a,
    'FL',
    "Right Cortex Caudal Middle Frontal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299001b,
    'FL',
    "Right Cortex Corpus Callosum",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299001c,
    'FL',
    "Right Cortex Cuneus",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299001d,
    'FL',
    "Right Cortex Entorhinal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299001e,
    'FL',
    "Right Cortex Fusiform",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299001f,
    'FL',
    "Right Cortex Inferior Parietal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990020,
    'FL',
    "Right Cortex Inferior Temporal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990021,
    'FL',
    "Right Cortex Isthmus Cingulate",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990022,
    'FL',
    "Right Cortex Lateral Occipital",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990023,
    'FL',
    "Right Cortex Lateral Orbito Frontal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990024,
    'FL',
    "Right Cortex Lingual",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990025,
    'FL',
    "Right Cortex Medial Orbito Frontal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990026,
    'FL',
    "Right Cortex Middle Temporal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990027,
    'FL',
    "Right Cortex Parahippocampal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990028,
    'FL',
    "Right Cortex Paracentral",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990029,
    'FL',
    "Right Cortex Pars Opercularis",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299002a,
    'FL',
    "Right Cortex Pars Orbitalis",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299002b,
    'FL',
    "Right Cortex Pars Triangularis",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299002c,
    'FL',
    "Right Cortex Pericalcarine",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299002d,
    'FL',
    "Right Cortex Postcentral",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299002e,
    'FL',
    "Right Cortex Posterior Cingulate",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299002f,
    'FL',
    "Right Cortex Precentral",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990030,
    'FL',
    "Right Cortex Precuneus",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990031,
    'FL',
    "Right Cortex Rostral Anterior Cingulate",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990032,
    'FL',
    "Right Cortex Rostral Middle Frontal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990033,
    'FL',
    "Right Cortex Superior Frontal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990034,
    'FL',
    "Right Cortex Superior Parietal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990035,
    'FL',
    "Right Cortex Superior Temporal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990036,
    'FL',
    "Right Cortex Supramarginal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990037,
    'FL',
    "Right Cortex Frontal Pole",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990038,
    'FL',
    "Right Cortex Temporal Pole",
    '1')
add_private_dict_entry(
    "NQRight",
    0x02990039,
    'FL',
    "Right Cortex Transvere Temporal",
    '1')
add_private_dict_entry(
    "NQRight",
    0x0299003a,
    'FL',
    "Right Meningie",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x03070001,
    'UN',
    "RIS Worklist IMGEF",
    '1')
add_private_dict_entry(
    "SIEMENS ISI",
    0x03090001,
    'UN',
    "RIS Report IMGEF",
    '1')
add_private_dict_entry(
    "Philips PET Private Group",
    0x05110000,
    'US',
    "Private Data",
    '1')
add_private_dict_entry(
    "Philips PET Private Group",
    0x05110001,
    'US',
    "Private Data",
    '1')
add_private_dict_entry(
    "Philips PET Private Group",
    0x05110002,
    'OB',
    "Private Data",
    '1')
add_private_dict_entry(
    "Philips PET Private Group",
    0x05110003,
    'OB',
    "Private Data",
    '1')
add_private_dict_entry(
    "Philips PET Private Group",
    0x05110032,
    'DS',
    "Private Data",
    '1')
add_private_dict_entry(
    "Philips PET Private Group",
    0x05110050,
    'DS',
    "Private Data",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x06010000,
    'SH',
    "Implementation Version",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x06010020,
    'DS',
    "Relative Table Position",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x06010021,
    'DS',
    "Relative Table Height",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x06010030,
    'SH',
    "Surview Direction",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x06010031,
    'DS',
    "Surview Length",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x06010050,
    'SH',
    "Image View Type",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x06010070,
    'DS',
    "Batch Number",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x06010071,
    'DS',
    "Batch Size",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x06010072,
    'DS',
    "Batch Slice Number",
    '1')
add_private_dict_entry(
    "PI Private Block (0781:3000 - 0781:30FF)",
    0x07810001,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PI Private Block (0781:3000 - 0781:30FF)",
    0x07810002,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PI Private Block (0781:3000 - 0781:30FF)",
    0x07810005,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "PI Private Block (0781:3000 - 0781:30FF)",
    0x07810009,
    'FL',
    "?",
    '4')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10002,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10007,
    'US',
    "?",
    '3')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10008,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10009,
    'OW',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1000A,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1000C,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10011,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10012,
    'FL',
    "?",
    '1-n')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10013,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10016,
    'FL',
    "?",
    '1-n')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10018,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10019,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1001C,
    'FL',
    "?",
    '1-n')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1002A,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1002B,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10036,
    'AE',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1003D,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10040,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10042,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10043,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10045,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10047,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1004A,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10050,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10056,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10058,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1005D,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1005F,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10070,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10071,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10075,
    'LO',
    "?",
    '2')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10076,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10085,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10087,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10088,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1008C,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10094,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10096,
    'DA',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10097,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A10098,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A1009F,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A100D0,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30003,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30005,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30006,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30009,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30013,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30014,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30015,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30017,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A3001B,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A3001F,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30022,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30023,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30034,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30043,
    'DS',
    "?",
    '1-n')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30055,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A3005C,
    'ST',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30061,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30062,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30063,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30064,
    'IS',
    "?",
    '1-n')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30065,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30066,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30080,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A3008F,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30092,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30093,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A30099,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A3009C,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A3009F,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300B9,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300BB,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300C0,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300C1,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300C2,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300C3,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300C4,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300C5,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300C8,
    'AE',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300C9,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300CB,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300CC,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300E3,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300F2,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300F5,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300FA,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A300FB,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A50000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A50054,
    'DT',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A50056,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A50059,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A50062,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A50069,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A500AE,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "ELSCINT1",
    0x07A500C8,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Nautilus Medical",
    0x08570000,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Nautilus Medical",
    0x08570001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Nautilus Medical",
    0x08570002,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Nautilus Medical",
    0x08570003,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "ETIAM DICOMDIR",
    0x08590040,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630010,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630010,
    'SL',
    "Image Type",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630023,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630023,
    'SL',
    "Calibration Flag",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630026,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630026,
    'UL',
    "Attribute Version",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630027,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630027,
    'SL',
    "Resizing Flag",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630028,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630028,
    'SL',
    "Logarithm Flag",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630032,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630032,
    'SL',
    "Left Collimator Edge",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630033,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630033,
    'SL',
    "Right Collimator Edge",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630034,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630034,
    'FL',
    "Distance Source to Patient of Biplane Pair",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630035,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630035,
    'SL',
    "Line Correction Flag",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630036,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630036,
    'SL',
    "Contrast Enhancement Flag",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630037,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630037,
    'SL',
    "Calibre Value",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630038,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630038,
    'SL',
    "High Frequency Line Correction Max Threshold",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630039,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630039,
    'SL',
    "High Frequency Line Correction Min Threshold",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630040,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630040,
    'FL',
    "Greater Limit",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630041,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630041,
    'FL',
    "Lower Limit",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630042,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630042,
    'FL',
    "Frontal Detector Blades Opening",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630043,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630043,
    'FL',
    "Frontal Tube Blades Opening",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630044,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630044,
    'FL',
    "Lateral Detector Blades Opening",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630045,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630045,
    'FL',
    "Lateral Tube Blades Opening",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630046,
    'DS',
    "ThreeD Calibration Parameters",
    '1-n')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630046,
    'DS',
    "?",
    '11')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630047,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630048,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630049,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630057,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Biospace Med : EOS Tag",
    0x08630057,
    'CS',
    "Image Horizontal Flip",
    '1')
add_private_dict_entry(
    "GEIIS PACS",
    0x09030010,
    'US',
    "Reject Image Flag",
    '1')
add_private_dict_entry(
    "GEIIS PACS",
    0x09030011,
    'US',
    "Significant Flag",
    '1')
add_private_dict_entry(
    "GEIIS PACS",
    0x09030012,
    'US',
    "Confidential Flag",
    '1')
add_private_dict_entry(
    "GEIIS PACS",
    0x09030020,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x09050030,
    'LO',
    "Assigning Authority For Patient ID",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x09070010,
    'UI',
    "Original Study Instance UID",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x09070020,
    'UI',
    "Original Series Instance UID",
    '1')
add_private_dict_entry(
    "GEIIS PACS",
    0x09070021,
    'US',
    "Prefetch Algorithm",
    '1')
add_private_dict_entry(
    "GEIIS PACS",
    0x09070022,
    'US',
    "Limit Recent Studies",
    '1')
add_private_dict_entry(
    "GEIIS PACS",
    0x09070023,
    'US',
    "Limit Oldest Studies",
    '1')
add_private_dict_entry(
    "GEIIS PACS",
    0x09070024,
    'US',
    "Limit Recent Months",
    '1')
add_private_dict_entry(
    "GEIIS",
    0x09070030,
    'UI',
    "Original SOP Instance UID",
    '1')
add_private_dict_entry(
    "GEIIS PACS",
    0x09070031,
    'UI',
    "Exclude Study UIDs",
    '1-n')
add_private_dict_entry(
    "Philips Imaging DD 124",
    0x10010003,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100A0,
    'SQ',
    "Marker Sequence",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100A1,
    'SL',
    "Marker Type",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100A2,
    'SL',
    "Marker Number",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100A3,
    'FD',
    "Marker 3D Position",
    '3')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B0,
    'SL',
    "Distance Unit",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B1,
    'SL',
    "Dose Unit",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B2,
    'SL',
    "Normalisation Mode",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B3,
    'FD',
    "Normalisation Factor",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B4,
    'FD',
    "F-Value",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B5,
    'FD',
    "Prescribed Dose",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B6,
    'FD',
    "Absolute Dose Factor",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B7,
    'SL',
    "Decoupled sk",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B8,
    'FD',
    "Absolute Time Factor",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100B9,
    'FD',
    "Total Treatment Time",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100BA,
    'SL',
    "TG 43 Model",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100BB,
    'SL',
    "3D Dose Grid Size",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100BC,
    'FD',
    "Dose Grid Corner 1",
    '3')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100BD,
    'FD',
    "Dose Grid Corner 2",
    '3')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100BE,
    'FD',
    "Patient Data Conversion",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100BF,
    'FD',
    "Volume Data Conversion",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C0,
    'FD',
    "Volume Data Vector",
    '3')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C1,
    'SL',
    "Optimization Method",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C2,
    'SL',
    "Display Method",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C3,
    'SL',
    "Geometrical Method",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C3,
    'SQ',
    "VOI Based Optimization Settings Sequence",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C5,
    'SL',
    "VOI Number",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C5,
    'SL',
    "VOI Number",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C6,
    'LO',
    "VOI Name",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C6,
    'LO',
    "VOI Name",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C7,
    'SL',
    "VOI Type",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C7,
    'SL',
    "VOI Type",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C8,
    'SL',
    "VOI Class",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C8,
    'SL',
    "VOI Class",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100C9,
    'SL',
    "VOI Priority",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100CA,
    'SL',
    "No of Points",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100CB,
    'FD',
    "Percent On Surface",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100CC,
    'FD',
    "Surface Margin",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100CD,
    'SL',
    "Selected",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100CE,
    'FD',
    "Dose Limit",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100CF,
    'FD',
    "Importance Factor",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D0,
    'FD',
    "Importance Factor From",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D1,
    'FD',
    "Importance Factor To",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D2,
    'FD',
    "Focus",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D3,
    'SL',
    "Surface Sampling Method",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D4,
    'FD',
    "Number of Sampling Points Per ccm",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D5,
    'SL',
    "Convergence Accuracy",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D6,
    'SL',
    "Max No of Convergence Iterations",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D7,
    'FD',
    "Weight Smoothing",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D8,
    'SL',
    "Steps Per Importance Factor",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100D9,
    'FD',
    "Constraints PTVDmax",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100DA,
    'FD',
    "Constraints NTDmax",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100DB,
    'SL',
    "Algorithmic Population Size",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100DC,
    'SL',
    "Algorithmic Generations",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100DD,
    'SL',
    "Algorithmic Initializations",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100DE,
    'SL',
    "Min No Of SDP",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100DF,
    'SL',
    "Depth Method",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100E0,
    'SL',
    "Depth Defined On",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100E1,
    'FD',
    "Depth",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100E2,
    'SQ',
    "VOI Based Placement Settings Sequence",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100E7,
    'SL',
    "VOI Selected",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100E8,
    'FD',
    "Margin",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100E9,
    'SL',
    "Selection Method",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100EA,
    'FD',
    "Selection Distance",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100EB,
    'FD',
    "WBT On Contour Spacing",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100EC,
    'FD',
    "WBT Urethra Margin",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100ED,
    'FD',
    "WBT Searching Radius PTV",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100EE,
    'FD',
    "WBT Searching Radius OAR",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100EF,
    'FD',
    "WBT Starting Point",
    '3')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100F0,
    'FD',
    "WBT Surface",
    '4')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100F1,
    'FD',
    "WBT No of Interior Catheters",
    '4')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100F2,
    'FD',
    "WBT Relative Radius",
    '4')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1001",
    0x100100F3,
    'SL',
    "Sorting Method",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030001,
    'UN',
    "Number Of Probes",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030010,
    'UN',
    "US Probe Sequence",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030011,
    'UN',
    "Identifier",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030012,
    'UN',
    "Probe Name",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030013,
    'UN',
    "Depth",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030014,
    'UN',
    "Frequency",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030015,
    'UN',
    "",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030016,
    'UN',
    "Power",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030017,
    'UN',
    "Dynamic Range",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030018,
    'UN',
    "Frame Averaging",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030019,
    'UN',
    "Field Of View",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030020,
    'UN',
    "TGC",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x1003002A,
    'UN',
    "Number Of Focus Sets",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x1003002B,
    'UN',
    "Current Focus Set",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x1003002C,
    'UN',
    "Image Enhancement Filter Index",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x1003002D,
    'UN',
    "Rejection Filter Low",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x1003002E,
    'UN',
    "Rejection Filter High",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x1003002F,
    'UN',
    "Brightness",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030030,
    'UN',
    "Contrast",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030031,
    'UN',
    "Gamma",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030032,
    'UN',
    "Speckle Enabled",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030033,
    'UN',
    "Speckle Level",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030040,
    'UN',
    "Focus Set Sequence",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030041,
    'UN',
    "Identifier",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030042,
    'UN',
    "Number Of Focus Zone",
    '1')
add_private_dict_entry(
    "PRIVATE_CODE_STRING_1003",
    0x10030043,
    'UN',
    "Focus",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350000,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350001,
    'OB',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350002,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350006,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350007,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350008,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350009,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350010,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350013,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350014,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350016,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350017,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350018,
    'UN',
    "?",
    '1')
add_private_dict_entry(
    "Voxar 2.16.124.113543.6003.1999.12.20.12.5.0",
    0x11350021,
    'UL',
    "?",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Biopsy Private Code",
    0x12690001,
    'IS',
    "Biopsy Image",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Biopsy Private Code",
    0x12690010,
    'IS',
    "Biopsy Markers X",
    '1-n')
add_private_dict_entry(
    "IMS s.r.l. Biopsy Private Code",
    0x12690011,
    'IS',
    "Biopsy Markers Y",
    '1-n')
add_private_dict_entry(
    "IMS s.r.l. Biopsy Private Code",
    0x12690012,
    'IS',
    "Biopsy Markers Number",
    '1-n')
add_private_dict_entry(
    "IMS s.r.l. Biopsy Private Code",
    0x12690020,
    'IS',
    "Biopsy Area Left Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Biopsy Private Code",
    0x12690021,
    'IS',
    "Biopsy Area Right Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Biopsy Private Code",
    0x12690022,
    'IS',
    "Biopsy Area Top Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Biopsy Private Code",
    0x12690023,
    'IS',
    "Biopsy Area Bottom Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Biopsy Private Code",
    0x12690024,
    'IS',
    "Biopsy Number",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710001,
    'IS',
    "Threshold 1",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710002,
    'IS',
    "Threshold 2",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710010,
    'IS',
    "Segmentation Left Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710011,
    'IS',
    "Segmentation Right Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710012,
    'IS',
    "Segmentation Top Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710013,
    'IS',
    "Segmentation Bottom Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710020,
    'IS',
    "Compressor Status",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710021,
    'IS',
    "Collimator Type",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710022,
    'IS',
    "Biopsy Specimen",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710030,
    'IS',
    "Printer Segmentation",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710031,
    'IS',
    "Printer 8x10 Format",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710032,
    'FD',
    "Printer 8x10 Size X",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710033,
    'FD',
    "Printer 8x10 Size Y",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710034,
    'IS',
    "Printer 8x10 Area Left Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710035,
    'IS',
    "Printer 8x10 Area Right Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710036,
    'IS',
    "Printer 8x10 Area Top Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710037,
    'IS',
    "Printer 8x10 Area Bottom Border",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710038,
    'LO',
    "Rotation And Inclination Sensor Presence",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710039,
    'US',
    "Window Center For For Processing Images",
    '1-n')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710040,
    'US',
    "Window Width For For Processing Images",
    '1-n')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710041,
    'LO',
    "Window Center and Width Explanation For For Processing Images",
    '1-n')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710042,
    'LT',
    "Processing Information",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710043,
    'LT',
    "Filename",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710044,
    'LT',
    "Contrast View",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710045,
    'IS',
    "Threshold 3",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710046,
    'IS',
    "Threshold 4",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710047,
    'IS',
    "Threshold 5",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710048,
    'IS',
    "Threshold 6",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710049,
    'IS',
    "Threshold 7",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710050,
    'IS',
    "Threshold 8",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710051,
    'IS',
    "Threshold 9",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710052,
    'IS',
    "Threshold 9",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710053,
    'IS',
    "Scaling Factor For Processing",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710054,
    'IS',
    "ConfirmX Image",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710055,
    'IS',
    "Background counts",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710056,
    'IS',
    "WL Roi Area X",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710057,
    'IS',
    "WL Roi Area Y",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710060,
    'IS',
    "Second Processing Image",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710061,
    'IS',
    "S Filter",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710062,
    'IS',
    "U Filter",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710063,
    'IS',
    "Anonymous",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710070,
    'IS',
    "Tomo SAD",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710071,
    'IS',
    "Tomo Detector YAW",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710072,
    'IS',
    "Tomo Detector Pitch",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710073,
    'IS',
    "Tomo Detector Roll",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710074,
    'IS',
    "Tomo Focal Spot X",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710075,
    'IS',
    "Tomo Focal Spot Y",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710076,
    'IS',
    "Tomo Xray Start Angle",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710077,
    'IS',
    "Tomo Xray End Angle",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710078,
    'IS',
    "Tomo Xray Angle",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710079,
    'IS',
    "Tomo Exposure Counter",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710080,
    'IS',
    "Tomo Exposure Number",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710081,
    'IS',
    "Tomo WL Modified",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710082,
    'IS',
    "Tomo Projection",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710083,
    'IS',
    "Key Object Selection Title Code",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710084,
    'IS',
    "Rejected for Quality Reasons Code",
    '1')
add_private_dict_entry(
    "IMS s.r.l. Mammography Private Code",
    0x12710085,
    'IS',
    "?",
    '1')
add_private_dict_entry(
    "AEGIS_DICOM_2.00",
    0x13690000,
    'US',
    "?",
    '1-n')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550000,
    'OW',
    "ELI Interpretation Vector",
    '1')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550001,
    'UN',
    "Custom ID",
    '1')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550002,
    'UT',
    "Race",
    '1')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550003,
    'UT',
    "Social Security Number",
    '1')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550004,
    'UT',
    "Attending Physician",
    '1')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550005,
    'UT',
    "Procedural Diagnosis",
    '1')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550006,
    'UT',
    "Note 1",
    '1')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550007,
    'UT',
    "Note 2",
    '1')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550008,
    'LO',
    "Order Request Number",
    '1')
add_private_dict_entry(
    "Mortara_Inc",
    0x14550010,
    'LO',
    "Manufacturer Name",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 129",
    0x20010000,
    'SQ',
    "Presentation State Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010001,
    'FL',
    "Chemical Shift",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010001,
    'FL',
    "Chemical Shift",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 129",
    0x20010001,
    'SQ',
    "PresentationStateSequence",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010001,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010002,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010002,
    'IS',
    "Chemical Shift Number MR",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010002,
    'IS',
    "Chemical Shift Number MR",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010003,
    'FL',
    "Diffusion B-Factor",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010003,
    'FL',
    "Diffusion B-Factor",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010004,
    'CS',
    "Diffusion Direction",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010004,
    'CS',
    "Diffusion Direction",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010005,
    'SS',
    "Graphic Annotation ParentID",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010005,
    'SS',
    "Graphic Annotation ParentID",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010006,
    'CS',
    "Image Enhanced",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010006,
    'CS',
    "Image Enhanced",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010007,
    'CS',
    "Image Type End Diastole or End Systole",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010007,
    'CS',
    "Image Type End Diastole or End Systole",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010008,
    'IS',
    "Phase Number",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010008,
    'IS',
    "Phase Number",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010009,
    'FL',
    "Image Prepulse Delay",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010009,
    'FL',
    "Image Prepulse Delay",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001000a,
    'IS',
    "Image Plane Number",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001000a,
    'IS',
    "Slice Number",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001000b,
    'CS',
    "Image Orientation",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001000b,
    'CS',
    "Slice Orientation",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001000c,
    'CS',
    "Arrhythmia Rejection",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001000c,
    'CS',
    "Arrhythmia Rejection",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001000e,
    'CS',
    "Cardiac Cycled",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001000e,
    'CS',
    "Cardiac Cycled",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001000f,
    'SS',
    "Cardiac Gate Width",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001000f,
    'SS',
    "Cardiac Gate Width",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010010,
    'CS',
    "Cardiac Sync",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010010,
    'CS',
    "Cardiac Sync",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010011,
    'FL',
    "Diffusion Echo Time",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010011,
    'FL',
    "Diffusion Echo Time",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010012,
    'CS',
    "Dynamic Series",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010012,
    'CS',
    "Dynamic Series",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010013,
    'SL',
    "EPI Factor",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010013,
    'SL',
    "EPI Factor",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010013,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010014,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010014,
    'SL',
    "Number of Echoes",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010014,
    'SL',
    "Number of Echoes",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010015,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010015,
    'SS',
    "Number of Locations",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010015,
    'SS',
    "Number of Locations",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010016,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010016,
    'SS',
    "Number of PC Directions",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010016,
    'SS',
    "Number of PC Directions",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010017,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010017,
    'SL',
    "Number of Phases",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010017,
    'SL',
    "Number of Phases",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010018,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010018,
    'SL',
    "Number of Slices",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010018,
    'SL',
    "Number of Slices",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010019,
    'CS',
    "Partial Matrix Scanned",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010019,
    'CS',
    "Partial Matrix Scanned",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010019,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001001a,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001001a,
    'FL',
    "PC Velocity",
    '3')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001001a,
    'FL',
    "PC Velocity",
    '3')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001001b,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001001b,
    'FL',
    "Prepulse Delay",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001001b,
    'FL',
    "Prepulse Delay",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001001c,
    'CS',
    "Prepulse Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001001c,
    'CS',
    "Prepulse Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001001c,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001001d,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001001d,
    'IS',
    "Reconstruction Number",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001001d,
    'IS',
    "Reconstruction Number",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001001e,
    'CS',
    "Reformat Accuracy",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001001e,
    'CS',
    "Reformat Accuracy",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001001e,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001001f,
    'CS',
    "Respiration Sync",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001001f,
    'CS',
    "Respiration Sync",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001001f,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010020,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010020,
    'LO',
    "Scanning Technique",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010020,
    'LO',
    "Scanning Technique",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010021,
    'CS',
    "SPIR",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010021,
    'CS',
    "SPIR",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010021,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010022,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010022,
    'FL',
    "Water-Fat Shift",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010022,
    'FL',
    "Water-Fat Shift",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010023,
    'DS',
    "Flip Angle",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010023,
    'DS',
    "Flip Angle",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010023,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010024,
    'CS',
    "Series is Interactive",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010024,
    'CS',
    "Series is Interactive",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010024,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010025,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010025,
    'SH',
    "Echo Time Display",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010025,
    'SH',
    "Echo Time Display",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010026,
    'CS',
    "Presentation State Subtraction Active",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010026,
    'CS',
    "Presentation State Subtraction Active",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010026,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010027,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010028,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010029,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010029,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010029,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001002a,
    'US',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001002b,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001002b,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001002b,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001002c,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001002d,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001002d,
    'SS',
    "Number of Slices in Stack",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001002d,
    'SS',
    "Number of Slices in Stack",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001002e,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001002f,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010030,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010031,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010032,
    'FL',
    "Stack Radial Angle",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010032,
    'FL',
    "Stack Radial Angle",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010032,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010033,
    'CS',
    "Stack Radial Axis",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010033,
    'CS',
    "Stack Radial Axis",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010033,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010034,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010035,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010035,
    'SS',
    "Stack Slice Number",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010035,
    'SS',
    "Stack Slice Number",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010036,
    'CS',
    "Stack Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010036,
    'CS',
    "Stack Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010036,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010037,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010039,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010039,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010039,
    'FL',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001003a,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001003b,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001003c,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001003d,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001003d,
    'UL',
    "Contour Fill Color",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001003d,
    'UL',
    "Contour Fill Color",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001003e,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001003f,
    'CS',
    "Displayed Area Zoom Interpolation Method",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001003f,
    'CS',
    "Displayed Area Zoom Interpolation Method",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001003f,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010040,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010043,
    'IS',
    "Ellipse Display Shutter Major Axis First End Point",
    '2')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010043,
    'IS',
    "Ellipse Display Shutter Major Axis First End Point",
    '2')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010044,
    'IS',
    "Ellipse Display Shutter Major Axis Second End Point",
    '2')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010044,
    'IS',
    "Ellipse Display Shutter Major Axis Second End Point",
    '2')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010045,
    'IS',
    "Ellipse Display Shutter Other Axis First End Point",
    '2')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010045,
    'IS',
    "Ellipse Display Shutter Other Axis First End Point",
    '2')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010046,
    'CS',
    "Graphic Line Style",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010046,
    'CS',
    "Graphic Line Style",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010047,
    'FL',
    "Graphic Line Width",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010047,
    'FL',
    "Graphic Line Width",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010048,
    'SS',
    "Graphic Annotation ID",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010048,
    'SS',
    "Graphic Annotation ID",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001004b,
    'CS',
    "Interpolation Method",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001004b,
    'CS',
    "Interpolation Method",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001004c,
    'CS',
    "Poly Line Begin Point Style",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001004c,
    'CS',
    "Poly Line Begin Point Style",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001004d,
    'CS',
    "Poly Line End Point Style",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001004d,
    'CS',
    "Poly Line End Point Style",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001004e,
    'CS',
    "Window Smoothing Taste",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001004e,
    'CS',
    "Window Smoothing Taste",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010050,
    'LO',
    "Graphic Marker Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010050,
    'LO',
    "Graphic Marker Type",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010051,
    'IS',
    "Overlay Plane ID",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010051,
    'IS',
    "Overlay Plane ID",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010052,
    'UI',
    "Image Presentation State UID",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010052,
    'UI',
    "Image Presentation State UID",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010053,
    'CS',
    "Presentation GL Transform Invert",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010053,
    'CS',
    "Presentation GL Transform Invert",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010054,
    'FL',
    "Contour Fill Transparency",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010054,
    'FL',
    "Contour Fill Transparency",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010055,
    'UL',
    "Graphic Line Color",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010055,
    'UL',
    "Graphic Line Color",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010056,
    'CS',
    "Graphic Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010056,
    'CS',
    "Graphic Type",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010058,
    'UL',
    "Contrast Transfer Taste",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010058,
    'UL',
    "Contrast Transfer Taste",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001005a,
    'ST',
    "Graphic Annotation Model",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001005a,
    'ST',
    "Graphic Annotation Model",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001005d,
    'ST',
    "Measurement Text Units",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001005d,
    'ST',
    "Measurement Text Units",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001005e,
    'ST',
    "Measurement Text Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001005e,
    'ST',
    "Measurement Text Type",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001005f,
    'SQ',
    "Stack Sequence",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001005f,
    'SQ',
    "Stack Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010060,
    'SL',
    "Number of Stacks",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010060,
    'SL',
    "Number of Stacks",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010061,
    'CS',
    "Series Transmitted",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010061,
    'CS',
    "Series Transmitted",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010062,
    'CS',
    "Series Committed",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010062,
    'CS',
    "Series Committed",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010063,
    'CS',
    "Examination Source",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010063,
    'CS',
    "Examination Source",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010064,
    'SH',
    "Text Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010064,
    'SH',
    "Text Type",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010065,
    'SQ',
    "Graphic Overlay Plane",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010065,
    'SQ',
    "Graphic Overlay Plane",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010067,
    'CS',
    "Linear Presentation GL Transform Shape Sub",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010067,
    'CS',
    "Linear Presentation GL Transform Shape Sub",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010068,
    'SQ',
    "Linear Modality GL Transform",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010068,
    'SQ',
    "Linear Modality GL Transform",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010069,
    'SQ',
    "Display Shutter",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010069,
    'SQ',
    "Display Shutter",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001006a,
    'SQ',
    "Spatial Transformation",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001006a,
    'SQ',
    "Spatial Transformation",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x2001006b,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001006b,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001006b,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001006d,
    'LO',
    "Text Font",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001006d,
    'LO',
    "Text Font",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001006e,
    'SH',
    "Series Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001006e,
    'SH',
    "Series Type",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010071,
    'CS',
    "Graphic Constraint",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010071,
    'CS',
    "Graphic Constraint",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010072,
    'FL',
    "?",
    '2')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010072,
    'IS',
    "Ellipse Display Shutter Other Axis Second End Point",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010072,
    'IS',
    "Ellipse Display Shutter Other Axis Second End Point",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 002",
    0x20010073,
    'FL',
    "?",
    '2')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010074,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010074,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010075,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010075,
    'DS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010076,
    'UL',
    "Number of Frames",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010076,
    'UL',
    "Number of Frames",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010077,
    'CS',
    "GL Transform Type",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010077,
    'CS',
    "GL Transform Type",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001007a,
    'FL',
    "Window Rounding Factor",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001007a,
    'FL',
    "Window Rounding Factor",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001007b,
    'IS',
    "Acquisition Number",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001007b,
    'IS',
    "Acquisition Number",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001007c,
    'US',
    "Frame Number",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001007c,
    'US',
    "Frame Number",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010080,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010080,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010081,
    'IS',
    "Number of Dynamic Scans",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010081,
    'IS',
    "Number of Dynamic Scans",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010082,
    'IS',
    "Echo Train Length",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010082,
    'IS',
    "Echo Train Length",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010083,
    'DS',
    "Imaging Frequency",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010083,
    'DS',
    "Imaging Frequency",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010084,
    'DS',
    "Inversion Time",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010084,
    'DS',
    "Inversion Time",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010085,
    'DS',
    "Magnetic Field Strength",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010085,
    'DS',
    "Magnetic Field Strength",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010086,
    'IS',
    "Number of Phase Encoding Steps",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010086,
    'IS',
    "Number of Phase Encoding Steps",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010087,
    'SH',
    "Imaged Nucleus",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010087,
    'SH',
    "Imaged Nucleus",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010088,
    'DS',
    "Number of Averages",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010088,
    'DS',
    "Number of Averages",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010089,
    'DS',
    "Phase FOV Percent",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010089,
    'DS',
    "Phase FOV Percent",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001008a,
    'DS',
    "Sampling Percent",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001008a,
    'DS',
    "Sampling Percent",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001008b,
    'SH',
    "Transmitting Coil",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001008b,
    'SH',
    "Transmitting Coil",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010090,
    'LO',
    "Text Foreground Color",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010090,
    'LO',
    "Text Foreground Color",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010091,
    'LO',
    "Text Background Color",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010091,
    'LO',
    "Text Background Color",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010092,
    'LO',
    "Text Shadow Color",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010092,
    'LO',
    "Text Shadow Color",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x20010093,
    'LO',
    "Text Style",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x20010093,
    'LO',
    "Text Style",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001009a,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001009a,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001009b,
    'UL',
    "Graphic Number",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001009b,
    'UL',
    "Graphic Number",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001009c,
    'LO',
    "Graphic Annotation Label",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001009c,
    'LO',
    "Graphic Annotation Label",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x2001009f,
    'US',
    "Pixel Processing Kernel Size",
    '2')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x2001009f,
    'US',
    "Pixel Processing Kernel Size",
    '2')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100a1,
    'CS',
    "Is Raw Image",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100a1,
    'CS',
    "Is Raw Image",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100a3,
    'UL',
    "Text Color Foreground",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100a3,
    'UL',
    "Text Color Foreground",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100a4,
    'UL',
    "Text Color Background",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100a4,
    'UL',
    "Text Color Background",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100a5,
    'UL',
    "Text Color Shadow",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100a5,
    'UL',
    "Text Color Shadow",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100c1,
    'LO',
    "Linear Modality GL Transform",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100c1,
    'LO',
    "Linear Modality GL Transform",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100c8,
    'LO',
    "Exam Card Name",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100c8,
    'LO',
    "Exam Card Name",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100cc,
    'ST',
    "Derivation Description",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100cc,
    'ST',
    "Derivation Description",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100da,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100da,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100f1,
    'FL',
    "Prospective Motion Correction",
    '1-n')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100f1,
    'FL',
    "Prospective Motion Correction",
    '6')
add_private_dict_entry(
    "PHILIPS IMAGING DD 001",
    0x200100f2,
    'FL',
    "Retrospective Motion Correction",
    '1-n')
add_private_dict_entry(
    "Philips Imaging DD 001",
    0x200100f2,
    'FL',
    "Retrospective Motion Correction",
    '6')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030000,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030001,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030002,
    'FD',
    "?",
    '3')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030003,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030006,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030009,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030010,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030011,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030012,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030013,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030014,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030015,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030016,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030017,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030018,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030019,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030022,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030024,
    'FD',
    "?",
    '4')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030025,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030026,
    'SL',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030027,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030028,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030029,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x2003002a,
    'LO',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x2003002b,
    'FD',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x2003002c,
    'SH',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x2003002d,
    'SL',
    "?",
    '1-n')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x2003002e,
    'SQ',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030030,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030031,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "Philips X-ray Imaging DD 001",
    0x20030032,
    'UI',
    "?",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050000,
    'CS',
    "Volume View Enabled",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050000,
    'FL',
    "Image Angulation AP",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050000,
    'FL',
    "Image Angulation AP",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050000,
    'SS',
    "Spectrum Extra Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050000,
    'UL',
    "Number of SOP Common",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050001,
    'FL',
    "Image Angulation FH",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050001,
    'FL',
    "Image Angulation FH",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050001,
    'SS',
    "Spectrum Kx Coordinate",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050001,
    'UL',
    "Number of Film Consumption",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050001,
    'UL',
    "Number of Study Reference",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050002,
    'FL',
    "Image Angulation RL",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050002,
    'FL',
    "Image Angulation RL",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050002,
    'SQ',
    "SPS Code",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050002,
    'SS',
    "Spectrum Ky Coordinate",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050003,
    'IS',
    "Image Annotation Count",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050003,
    'SS',
    "Spectrum Location Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050003,
    'UL',
    "Number of SPS Codes",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050004,
    'CS',
    "Image Display Orientation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050004,
    'CS',
    "Image Display Orientation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050004,
    'SS',
    "Spectrum Mix Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050004,
    'SS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050005,
    'CS',
    "Synergy Reconstruction Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050005,
    'CS',
    "Synergy Reconstruction Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050005,
    'SS',
    "Spectrum X Coordinate",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050006,
    'SS',
    "Spectrum Y Coordinate",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050006,
    'SS',
    "Number of PS Specific Character Sets",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050007,
    'FL',
    "Spectrum DC Level",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050007,
    'IS',
    "Image Line Count",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050007,
    'SS',
    "Number of Specific Character Set",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050008,
    'FL',
    "Image Offcenter AP",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050008,
    'FL',
    "Image Offcenter AP",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050008,
    'FL',
    "Spectrum Noise Level",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050009,
    'DS',
    "Rescale Intercept Original",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050009,
    'FL',
    "Image Offcenter FH",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050009,
    'FL',
    "Image Offcenter FH",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050009,
    'FL',
    "Spectrum Begin Time",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005000a,
    'DS',
    "Rescale Slope Original",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005000a,
    'FL',
    "Image OffCentre RL",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005000a,
    'FL',
    "Image OffCentre RL",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005000b,
    'FL',
    "Max FP",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005000b,
    'FL',
    "Max FP",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005000b,
    'LO',
    "Rescale Type Original",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005000c,
    'FL',
    "Min FP",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005000c,
    'FL',
    "Min FP",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005000d,
    'FL',
    "Scale Intercept",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005000d,
    'FL',
    "Scale Intercept",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005000e,
    'FL',
    "Scale Slope",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005000e,
    'FL',
    "Scale Slope",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005000e,
    'SQ',
    "Private Shared Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005000f,
    'DS',
    "Window Center",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005000f,
    'DS',
    "Window Center",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005000f,
    'SQ',
    "Private Per-Frame Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050010,
    'DS',
    "Window Width",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050010,
    'DS',
    "Window Width",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050010,
    'FL',
    "Spectrum Echo Time",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050010,
    'IS',
    "MF Conv Treat Spectro Mix Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050011,
    'CS',
    "Image Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050011,
    'CS',
    "Image Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050011,
    'UI',
    "MF Private Referenced SOP Instance UID",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050012,
    'CS',
    "Cardiac Gating",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050012,
    'CS',
    "Cardiac Gating",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050012,
    'FL',
    "Spectrum Inversion Time",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050012,
    'IS',
    "Diffusion B Value Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050013,
    'CS',
    "Development Mode",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050013,
    'CS',
    "Development Mode",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050013,
    'IS',
    "Gradient Orientation Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050013,
    'SS',
    "Spectrum Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050013,
    'UL',
    "Number of Codes",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050014,
    'CS',
    "Diffusion",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050014,
    'CS',
    "Diffusion",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050014,
    'SL',
    "Number of Diffusion B Values",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050014,
    'SS',
    "Spectrum Number of Averages",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050015,
    'CS',
    "Fat Saturation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050015,
    'CS',
    "Fat Saturation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050015,
    'LO',
    "User Name",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050015,
    'SL',
    "Number of Diffusion Gradient Orientations",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050015,
    'SS',
    "Spectrum Number of Samples",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050016,
    'CS',
    "Flow Compensation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050016,
    'CS',
    "Flow Compensation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050016,
    'CS',
    "Plan Mode",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050016,
    'LO',
    "Pass Word",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050016,
    'SS',
    "Spectrum Scan Sequence Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050017,
    'CS',
    "Fourier Interpolation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050017,
    'CS',
    "Fourier Interpolation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050017,
    'FD',
    "Diffusion B Matrix",
    '3')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050017,
    'LO',
    "Server Name",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050017,
    'SS',
    "Spectrum Number of Peaks",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050018,
    'CS',
    "Operating Mode Type",
    '3')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050018,
    'LO',
    "Hardcopy Protocol",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050018,
    'LO',
    "Hardcopy Protocol",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050018,
    'LO',
    "Data Base Name",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050018,
    'SQ',
    "Spectrum Peak",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050019,
    'CS',
    "Inverse Reconstructed",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050019,
    'CS',
    "Inverse Reconstructed",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050019,
    'CS',
    "Operating Mode",
    '3')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050019,
    'FL',
    "Spectrum Peak Intensity",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050019,
    'LO',
    "RootName",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005001a,
    'CS',
    "Fat Saturation Technique",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005001a,
    'SS',
    "Label Syntax",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005001a,
    'SS',
    "Label Syntax",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005001b,
    'CS',
    "Magnetization Prepared",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005001b,
    'CS',
    "Magnetization Prepared",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005001b,
    'IS',
    "Version Number Deleted Images",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005001c,
    'CS',
    "Magnetization Transfer Contrast",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005001c,
    'CS',
    "Magnetization Transfer Contrast",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005001c,
    'IS',
    "Version Number Deleted Spectra",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005001d,
    'IS',
    "Version Number Deleted Blobsets",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005001d,
    'SS',
    "Measurement Scan Resolution",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005001d,
    'SS',
    "Measurement Scan Resolution",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005001e,
    'SH',
    "MIP Protocol",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005001e,
    'SH',
    "MIP Protocol",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005001e,
    'UL',
    "LUT1 Offset",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005001f,
    'SH',
    "MPR Protocol",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005001f,
    'SH',
    "MPR Protocol",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005001f,
    'UL',
    "LUT1 Range",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050020,
    'LO',
    "DMI Application Name",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050020,
    'LO',
    "Spectrum Peak Label",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050020,
    'SL',
    "Number of Chemical Shift",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050020,
    'SL',
    "Number of Chemical Shifts",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050020,
    'UL',
    "LUT1 Begin Color",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050021,
    'FL',
    "Spectrum Peak Phase",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050021,
    'SS',
    "Number of Mixes",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050021,
    'SS',
    "Number of Mixes",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050021,
    'UL',
    "LUT1 End Color",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050022,
    'FL',
    "Spectrum Peak Position",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050022,
    'IS',
    "Number of References",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050022,
    'IS',
    "Number of References",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050022,
    'UL',
    "LUT2 Offset",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050023,
    'CS',
    "Spectrum Peak Type",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050023,
    'SS',
    "Number of Slabs",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050023,
    'SS',
    "Number of Slabs",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050023,
    'UL',
    "LUT2 Range",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050024,
    'FL',
    "Spectrum Peak Width",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050024,
    'UL',
    "LUT2 Begin Color",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050025,
    'CS',
    "Spectro SI B0 Correction",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050025,
    'SS',
    "Number of Volumes",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050025,
    'SS',
    "Number of Volumes",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050025,
    'UL',
    "LUT2 End Color",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050026,
    'CS',
    "Over Sampling Phase",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050026,
    'CS',
    "Over Sampling Phase",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050026,
    'CS',
    "Viewing Hardcopy Only",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050026,
    'FL',
    "Spectro B0 Echo Top Position",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050027,
    'CS',
    "Package Mode",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050027,
    'CS',
    "Package Mode",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050027,
    'CS',
    "Spectro Complex Component",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050027,
    'CS',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050028,
    'CS',
    "Partial Fourier Frequency",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050028,
    'CS',
    "Partial Fourier Frequency",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050028,
    'CS',
    "Spectro Data Origin",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050028,
    'SL',
    "Number of Label Types",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050029,
    'CS',
    "PartialFourierPhase",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050029,
    'CS',
    "PartialFourierPhase",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050029,
    'CS',
    "Label Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050029,
    'FL',
    "Spectro Echo Top Position",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005002a,
    'CS',
    "Exam Print Status",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005002a,
    'IS',
    "Patient Reference ID",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005002a,
    'IS',
    "Patient Reference ID",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005002b,
    'CS',
    "Exam Export Status",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005002b,
    'SS',
    "Percent Scan Complete",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005002b,
    'SS',
    "Percent Scan Complete",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005002c,
    'CS',
    "Phase Encode Reordering",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005002c,
    'CS',
    "Phase Encode Reordering",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005002c,
    'CS',
    "Exam Storage Commit Status",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x2005002D,
    'LO',
    "Root Id",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005002d,
    'CS',
    "Exam Media Write Status",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005002d,
    'IS',
    "PlanScan Survey Number of Images",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005002d,
    'IS',
    "PlanScan Survey Number of Images",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005002e,
    'CS',
    "PPG PPU Gating",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005002e,
    'CS',
    "PPG PPU Gating",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005002e,
    'FL',
    "dBdt",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005002f,
    'CS',
    "Spatial Presaturation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005002f,
    'CS',
    "Spatial Presaturation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005002f,
    'FL',
    "Proton SAR",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050030,
    'CS',
    "InPlane Transforms",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050030,
    'FL',
    "Non Proton SAR",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050030,
    'FL',
    "Repetition Time",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050030,
    'FL',
    "Repetition Time",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050031,
    'CS',
    "Respiratory Gating",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050031,
    'CS',
    "Respiratory Gating",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050031,
    'FL',
    "Local SAR",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050031,
    'SS',
    "Number of Spectra Acquired",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050032,
    'CS',
    "Sample Representation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050032,
    'CS',
    "Sample Representation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050032,
    'CS',
    "Safety Override Mode",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050032,
    'SQ',
    "Blob Data Object Array",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050033,
    'DT',
    "EV DVD Job In Params Datetime",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050033,
    'FL',
    "Acquisition Duration",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050033,
    'FL',
    "Acquisition Duration",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050033,
    'FL',
    "Phase Encoding Echo Top Positions",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050034,
    'CS',
    "Segmented KSpace",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050034,
    'CS',
    "Segmented KSpace",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050034,
    'CS',
    "Physical Quantity for Chemical Shift",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050034,
    'DT',
    "DVD Job In Params Volume Label",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050034,
    'LT',
    "Series Transaction UID",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050034,
    'SL',
    "Number of Image Per Series Ref",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050035,
    'CS',
    "Data Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050035,
    'CS',
    "Data Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050035,
    'CS',
    "Physical Quantity Spatial",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050035,
    'CS',
    "Spectro Examcard",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050035,
    'IS',
    "Parent ID",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050036,
    'CS',
    "Is Cardiac",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050036,
    'CS',
    "Is Cardiac",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050036,
    'FL',
    "Reference Frequency",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050036,
    'LO',
    "Parent Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050036,
    'UI',
    "Referenced Series Instance UID",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050037,
    'CS',
    "Is Spectro",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050037,
    'CS',
    "Is Spectro",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050037,
    'CS',
    "Color LUT Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050037,
    'FL',
    "Sample Offset",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050037,
    'LO',
    "Blob Name",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050038,
    'CS',
    "Spoiled",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050038,
    'CS',
    "Spoiled",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050038,
    'FL',
    "Sample Pitch",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050038,
    'LO',
    "Application Name",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050038,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050039,
    'CS',
    "Steady State",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050039,
    'CS',
    "Steady State",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050039,
    'LO',
    "Type Name",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050039,
    'LT',
    "?",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050039,
    'SS',
    "Search Interval for Peaks",
    '2')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005003a,
    'LT',
    "Data Dictionary Contents Version",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005003a,
    'SH',
    "Sub Anatomy",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005003a,
    'SH',
    "Sub Anatomy",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005003b,
    'CS',
    "Time Reversed Steady State",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005003b,
    'CS',
    "Time Reversed Steady State",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005003b,
    'CS',
    "Is Coil Survey",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005003c,
    'CS',
    "Tilt Optimized Nonsaturated Excitation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005003c,
    'CS',
    "Tilt Optimized Nonsaturated Excitation",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005003c,
    'FL',
    "Stack Table Position Longitudinal",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005003d,
    'FL',
    "Stack Table Position Lateral",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005003d,
    'SS',
    "Number of RR Interval Ranges",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005003d,
    'SS',
    "Number of RR Interval Ranges",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005003e,
    'FL',
    "Stack Posterior Coil Position",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005003e,
    'SL',
    "RR Intervals Distribution",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005003e,
    'SL',
    "RR Intervals Distribution",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005003f,
    'CS',
    "Active Implantable Medical Device Limits Applied",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005003f,
    'SL',
    "PlanScan Acquisition Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005003f,
    'SL',
    "PlanScan Acquisition Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050040,
    'CS',
    "Signal Domain for Chemical Shift",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050040,
    'FL',
    "Active Implantable Medical Device Head SAR Limit",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050040,
    'LO',
    "Version String",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050040,
    'SL',
    "PlanScan Survey Chemical Shift Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050041,
    'CS',
    "Signal Domain Spatial",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050041,
    'FL',
    "Active Implantable Medical Device Whole Body SAR Limit",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050041,
    'LO',
    "Comment String",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050041,
    'SL',
    "PlanScan Survey Dynamic Scan Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050042,
    'CS',
    "Blob In File",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050042,
    'CS',
    "Signal Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050042,
    'FL',
    "Active Implantable Medical Device B1 RMS Limit",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050042,
    'SL',
    "PlanScan Survey Echo Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050043,
    'CS',
    "Spectro Additional Rotations",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050043,
    'CS',
    "PlanScan Survey Image Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050043,
    'FL',
    "Active Implantable Medical Device dbDt Limit",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050043,
    'SL',
    "Actual Blob Size",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050043,
    'SS',
    "No Date of Last Calibration",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050044,
    'IS',
    "TFE Factor",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050044,
    'OW',
    "Blob Data",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050044,
    'SL',
    "PlanScan Survey Phase Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050044,
    'SS',
    "No Time of Last Calibration",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050044,
    'SS',
    "Spectro Display Ranges",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050045,
    'CS',
    "Spectro Echo Acquisition",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050045,
    'CS',
    "Attenuation Correction",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050045,
    'LO',
    "Blob Filename",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050045,
    'SL',
    "PlanScan Survey Reconstruction Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050045,
    'SS',
    "Number of Software Version",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050046,
    'CS',
    "Spectro Frequency Unit",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050046,
    'CS',
    "PlanScan Survey Scanning Sequence",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050046,
    'FL',
    "FWHM Shim",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050046,
    'SL',
    "Blob Offset",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 002",
    0x20050047,
    'CS',
    "Blob Flag",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050047,
    'FL',
    "Spectro Gamma",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050047,
    'FL',
    "Power Optimization",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050047,
    'SL',
    "PlanScan Survey Slice Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050047,
    'SS',
    "Number of Patient Other Names",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050048,
    'CS',
    "Spectro Hidden Line Removal",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050048,
    'FL',
    "Coil Q",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050048,
    'IS',
    "Referenced Acquisition Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050048,
    'IS',
    "Referenced Acquisition Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050048,
    'SS',
    "Number of Req Recipe of Results",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050049,
    'FL',
    "Spectro Horizontal Shift",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050049,
    'FL',
    "Receiver Gain",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050049,
    'IS',
    "Referenced Chemical Shift Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050049,
    'IS',
    "Referenced Chemical Shift Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050049,
    'SS',
    "Number of Series Operators Name",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005004a,
    'FL',
    "Data Window Duration",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005004a,
    'IS',
    "Referenced Dynamic Scan Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005004a,
    'IS',
    "Referenced Dynamic Scan Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005004b,
    'FL',
    "Mixing Time",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005004b,
    'IS',
    "Referenced Echo Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005004b,
    'IS',
    "Referenced Echo Number",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005004c,
    'CS',
    "Referenced Entity",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005004c,
    'CS',
    "Referenced Entity",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005004c,
    'FL',
    "First Echo Time",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005004d,
    'CS',
    "Is B0 Series",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005004d,
    'CS',
    "Referenced Image Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005004d,
    'CS',
    "Referenced Image Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005004e,
    'CS',
    "Is B1 Series",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005004e,
    'FL',
    "Slab FOV RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005004e,
    'FL',
    "Slab FOV RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005004f,
    'CS',
    "Volume Select",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005004f,
    'FL',
    "Slab Offcentre AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005004f,
    'FL',
    "Slab Offcentre AP",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050050,
    'FL',
    "Slab Offcentre FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050050,
    'FL',
    "Slab Offcentre FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050050,
    'FL',
    "Spectro Horizontal Window",
    '2')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050050,
    'SS',
    "Number of Series Performing Physicians Name",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050050,
    'SS',
    "Number of Patient Other IDs",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050051,
    'FL',
    "Slab Offcentre RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050051,
    'FL',
    "Slab Offcentre RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050051,
    'IS',
    "Original Series Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050051,
    'SS',
    "Number of Study Admitting Diagnostic Description",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050051,
    'SS',
    "Spectro Number of Display Ranges",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050052,
    'CS',
    "Slab Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050052,
    'CS',
    "Slab Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050052,
    'SS',
    "Number of Study Patient Contrast Allergies",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050052,
    'SS',
    "Spectro Number of Echo Pulses",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050052,
    'UI',
    "Original Series Instance UID",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050053,
    'CS',
    "Split Series Job Params",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050053,
    'CS',
    "Slab View Axis",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050053,
    'CS',
    "Slab View Axis",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050053,
    'FL',
    "MRE Frequency",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050053,
    'LO',
    "Spectro Processing History",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050053,
    'SS',
    "Number of Study Patient Medical Alerts",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050054,
    'CS',
    "Spectro Scan Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050054,
    'FL',
    "MRE Amplitude",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050054,
    'FL',
    "Volume Angulation AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050054,
    'FL',
    "Volume Angulation AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050054,
    'SS',
    "Number of Study Physicians of Record",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050054,
    'SS',
    "Preferred Dimension for Splitting",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050055,
    'FD',
    "Velocity Encoding Direction",
    '3')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050055,
    'FL',
    "MREMEG Frequency",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050055,
    'FL',
    "Volume Angulation FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050055,
    'FL',
    "Volume Angulation FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050055,
    'FL',
    "Spectro SI CS Intervals",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050055,
    'SS',
    "Number of Study Physicians Reading Study",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050056,
    'CS',
    "Spectro SI Mode",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050056,
    'FL',
    "MREMEG Pairs",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050056,
    'FL',
    "Volume Angulation RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050056,
    'FL',
    "Volume Angulation RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050056,
    'SS',
    "Number of SC Software Versions",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050056,
    'SS',
    "Contrast/Bolus Number of Injections",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050057,
    'CS',
    "MREMEG Direction",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050057,
    'FL',
    "Volume FOV AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050057,
    'FL',
    "Volume FOV AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050057,
    'LT',
    "Contrast/Bolus Agent Code",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050057,
    'SS',
    "Number of Running Attributes",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050057,
    'SS',
    "Spectro Spectral BW",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050058,
    'FL',
    "MREMEG Amplitude",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050058,
    'FL',
    "Volume FOV FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050058,
    'FL',
    "Volume FOV FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050058,
    'LO',
    "Spectro Title Line",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050058,
    'LT',
    "Contrast/Bolus Administration Route Code",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050059,
    'DS',
    "Contrast/Bolus Volume",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050059,
    'FL',
    "Spectro Turbo Echo Spacing",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050059,
    'FL',
    "MRE Number of Phase Delays",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050059,
    'FL',
    "Volume FOV RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050059,
    'FL',
    "Volume FOV RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005005a,
    'DS',
    "Contrast/Bolus Ingredient Concentration",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005005a,
    'FL',
    "Volume Offcentre AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005005a,
    'FL',
    "Volume Offcentre AP",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005005b,
    'FL',
    "Volume Offcentre FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005005b,
    'FL',
    "Volume Offcentre FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005005b,
    'IS',
    "Contrast/Bolus Dynamic Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005005c,
    'FL',
    "Volume Offcentre RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005005c,
    'FL',
    "Volume Offcentre RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005005c,
    'SQ',
    "Contrast/Bolus Sequence",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005005d,
    'CS',
    "Volume Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005005d,
    'CS',
    "Volume Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x2005005d,
    'IS',
    "Contrast/Bolus ID",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005005e,
    'CS',
    "Volume View Axis",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005005e,
    'CS',
    "Volume View Axis",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005005f,
    'CS',
    "Study Origin",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005005f,
    'CS',
    "Study Origin",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 005",
    0x20050060,
    'CS',
    "LUT to RGB Job Params",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050060,
    'FL',
    "Spectro Vertical Shift",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050060,
    'IS',
    "Study Sequence Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050060,
    'IS',
    "Study Sequence Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050060,
    'IS',
    "MRE Number of Motion Cycles",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050061,
    'CS',
    "Prepulse Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050061,
    'CS',
    "Prepulse Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050061,
    'FL',
    "MRE Motion MEG Phase Delay",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050061,
    'FL',
    "Spectro Vertical Window",
    '2')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050062,
    'FL',
    "Spectro Offset",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050062,
    'LT',
    "MRE Inversion Algorithm Version",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050063,
    'CS',
    "Sagittal Slice Order",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050063,
    'FL',
    "Spectrum Pitch",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050063,
    'SS',
    "fMRI Status Indication",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050063,
    'SS',
    "fMRI Status Indication",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050064,
    'CS',
    "Volume Selection",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050064,
    'CS',
    "Coronal Slice Order",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050064,
    'IS',
    "Reference Phase Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050064,
    'IS',
    "Reference Phase Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050065,
    'CS',
    "Transversal Slice Order",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050065,
    'IS',
    "Reference Reconstruction Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050065,
    'IS',
    "Reference Reconstruction Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050066,
    'CS',
    "Series Orientation",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050066,
    'CS',
    "Reference Scanning Sequence",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050066,
    'CS',
    "Reference Scanning Sequence",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050067,
    'IS',
    "MR Stack Reverse",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050067,
    'IS',
    "Reference Slice Number",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050067,
    'IS',
    "Reference Slice Number",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050068,
    'CS',
    "Reference Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050068,
    'CS',
    "Reference Type",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050068,
    'IS',
    "MRE Phase Delay Number",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050069,
    'FL',
    "Slab Angulation AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050069,
    'FL',
    "Slab Angulation AP",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005006a,
    'FL',
    "Slab Angulation FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005006a,
    'FL',
    "Slab Angulation FH",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005006b,
    'FL',
    "Slab Angulation RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005006b,
    'FL',
    "Slab Angulation RL",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005006c,
    'FL',
    "Slab FOV AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005006c,
    'FL',
    "Slab FOV AP",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005006d,
    'FL',
    "Slab FOV FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005006d,
    'FL',
    "Slab FOV FH",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005006e,
    'CS',
    "Scanning Sequence",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005006e,
    'CS',
    "Scanning Sequence",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005006f,
    'CS',
    "Acquisition Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005006f,
    'CS',
    "Acquisition Type",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050070,
    'LO',
    "Hardcopy Protocol EasyVision",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050070,
    'LO',
    "Hardcopy Protocol EasyVision",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 003",
    0x20050070,
    'OW',
    "Spectrum Pixel Data",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050070,
    'SS',
    "Number Mixes Spectro",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050071,
    'FL',
    "Stack Angulation AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050071,
    'FL',
    "Stack Angulation AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050071,
    'IS',
    "Number of Inversion Delays",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050071,
    'SQ',
    "Series SP Mix",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050072,
    'FL',
    "Inversion Delay Time",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050072,
    'FL',
    "Stack Angulation FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050072,
    'FL',
    "Stack Angulation FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050072,
    'SS',
    "SP Mix T Resolution",
    '1-2')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050073,
    'FL',
    "Stack Angulation RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050073,
    'FL',
    "Stack Angulation RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050073,
    'IS',
    "Inversion Delay Number",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050073,
    'SS',
    "SP Mix KX Resolution",
    '1-2')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050074,
    'DS',
    "Max DB DT",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050074,
    'FL',
    "Stack FOV AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050074,
    'FL',
    "Stack FOV AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050074,
    'SS',
    "SP Mix KY Resolution",
    '1-2')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050075,
    'DS',
    "Max SAR",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050075,
    'FL',
    "Stack FOV FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050075,
    'FL',
    "Stack FOV FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050075,
    'SS',
    "SP Mix F Resolution",
    '1-2')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050076,
    'FL',
    "Stack FOV RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050076,
    'FL',
    "Stack FOV RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050076,
    'LT',
    "SAR Type",
    '1')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050076,
    'SS',
    "SP Mix X Resolution",
    '1-2')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050077,
    'SS',
    "SP Mix Y Resolution",
    '1-2')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050078,
    'CS',
    "Metal Implant Status",
    '1')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050078,
    'FL',
    "Stack Offcentre AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050078,
    'FL',
    "Stack Offcentre AP",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050078,
    'SS',
    "SP Mix Number of Spectra Intended",
    '1-2')
add_private_dict_entry(
    "Philips MR Imaging DD 006",
    0x20050079,
    'CS',
    "Orientation Mirror Flip",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x20050079,
    'FL',
    "Stack Offcentre FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x20050079,
    'FL',
    "Stack Offcentre FH",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 004",
    0x20050079,
    'SS',
    "SP Mix Number of Averages",
    '1-2')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005007a,
    'FL',
    "Stack Offcentre RL",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005007a,
    'FL',
    "Stack Offcentre RL",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005007b,
    'CS',
    "Stack Preparation Direction",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    0x2005007b,
    'CS',
    "Stack Preparation Direction",
    '1-n')
add_private_dict_entry(
    "PHILIPS MR IMAGING DD 001",
    0x2005007e,
    'FL',
    "Stack Slice Distance",
    '1-n')
add_private_dict_entry(
    "Philips MR Imaging DD 001",
    'FL',