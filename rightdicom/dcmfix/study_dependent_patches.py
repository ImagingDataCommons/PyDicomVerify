from pydicom import Dataset, DataElement
from pydicom.datadict import tag_for_keyword, keyword_for_tag, dictionary_VR
from rightdicom.dcmvfy.mesgtext_cc import (
    # CLASSES
    ErrorInfo,
    ErrorType,
)
from rightdicom.dcmfix.fix_tools import *
def add_anatomy(ds: Dataset,
                BodyPartExamined_value: str,
                AnatomicRegionSequence_value: tuple, log: list):
    bpe = tag_for_keyword('BodyPartExamined')
    if bpe not in ds and BodyPartExamined_value is not None:
        bpe_a = DataElement(bpe, dictionary_VR(bpe), BodyPartExamined_value)
        ds[bpe] = bpe_a
        msg = ErrorInfo()
        msg.msg = 'General Fix - {}'.format(
            "<BodyPartExamined> is absent")
        msg.fix = "fixed by setting the <BodyPartExamined>"\
            " to '{}'".format(BodyPartExamined_value)
        log.append(msg.getWholeMessage())
    
    ars = tag_for_keyword('AnatomicRegionSequence')
    if ars not in ds and AnatomicRegionSequence_value is not None:
        if len(AnatomicRegionSequence_value) < 3:
            return
        code_value, code_meaning, coding_scheme_designator =\
            AnatomicRegionSequence_value
        item = CodeSeqItemGenerator(
            code_value, code_meaning, coding_scheme_designator)
        ars_a = DataElement(ars, 'SQ', [item])
        ds[ars] = ars_a
        msg = ErrorInfo()
        msg.msg = 'General Fix - {}'.format(
            "<AnatomicRegionSequence> is absent")
        msg.fix = "fixed by setting the <AnatomicRegionSequence>"\
            " to '{}'".format(subfix_CodeSeqItem2txt(ars_a, 0))
        log.append(msg.getWholeMessage())

