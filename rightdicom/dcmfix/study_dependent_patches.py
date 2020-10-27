from pydicom import Dataset, DataElement
from pydicom.datadict import tag_for_keyword, keyword_for_tag, dictionary_VR
from rightdicom.dcmvfy.mesgtext_cc import (
    # CLASSES
    ErrorInfo,
    ErrorType,
)
from rightdicom.dcmfix.fix_tools import *
from rightdicom.dcmfix.anatomy import *

def add_anatomy(ds: Dataset,
                BodyPartExamined_value: str,
                AnatomicRegionSequence_value: tuple, log: list,
                check_consistency: bool = True):
    bpe = tag_for_keyword('BodyPartExamined')
    ars = tag_for_keyword('AnatomicRegionSequence')
    if check_consistency:
        BodyPartExamined_value, AnatomicRegionSequence_value = \
            CorrectAnatomicInfo(
                BodyPartExamined_value, AnatomicRegionSequence_value) 
    if BodyPartExamined_value is not None:
        correct_bpe = True
        if bpe in ds:
            ds[bpe].value == BodyPartExamined_value
            correct_bpe = False
        if correct_bpe:
            bpe_a = DataElement(bpe, dictionary_VR(bpe), BodyPartExamined_value)
            ds[bpe] = bpe_a
            msg = ErrorInfo()
            msg.msg = 'General Fix - {}'.format(
                "<BodyPartExamined> is absent")
            msg.fix = "fixed by setting the <BodyPartExamined>"\
                " to '{}'".format(BodyPartExamined_value)
            log.append(msg.getWholeMessage())
    if is_accurate_code_seq(AnatomicRegionSequence_value):
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



def CorrectAnatomicInfo(BodyPartexamined_, AnatomicRegion_):
    if BodyPartexamined_ is None and not is_accurate_code_seq(AnatomicRegion_):
        return (None, (None, None, None))
    bpe = BodyPartexamined_
    ars = AnatomicRegion_
    if is_accurate_code_seq(AnatomicRegion_):
        cv, cm, cs = AnatomicRegion_
        if cs == 'SCT':
            if cv in SCT2BodyPartExamined:
                bpe = SCT2BodyPartExamined[cv]
                ars = BodyPartExamined2SCT[bpe]
        else:
            if cv in SRT2BodyPartExamined:
                bpe = SRT2BodyPartExamined[cv]
                ars = BodyPartExamined2SCT[bpe]
    else:
        if BodyPartexamined_ in BodyPartExamined2SCT:
            ars = BodyPartExamined2SCT[BodyPartexamined_]
            bpe = BodyPartexamined_
    return (bpe, ars)
    


def is_accurate_code_seq(code_sequence_item: tuple):
    if not isinstance(code_sequence_item, tuple):
        return False
    if len(code_sequence_item) < 3:
        return False
    for i in code_sequence_item:
        if i is None:
            return False
    return True
