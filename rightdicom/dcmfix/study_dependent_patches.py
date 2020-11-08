from pydicom import Dataset, DataElement
from pydicom.datadict import tag_for_keyword, keyword_for_tag, dictionary_VR
from pydicom.sequence import Sequence as DicomSequence
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
    old_bpe, old_ars = get_old_anatomy(ds)
    if old_bpe is None:
        if check_consistency:
            new_bpe, new_ars = \
                CorrectAnatomicInfo(
                    BodyPartExamined_value, AnatomicRegionSequence_value)
        else:
            new_bpe, new_ars = (
                BodyPartExamined_value, AnatomicRegionSequence_value)
    else:
        new_bpe = old_bpe
        new_ars = old_ars     
    if old_bpe != new_bpe and new_bpe is not None:
        bpe_a = DataElement(bpe, dictionary_VR(bpe), new_bpe)
        old_bpe_txt = old_bpe if bpe not in ds else ds[bpe].value
        ds[bpe] = bpe_a
        msg = ErrorInfo()
        msg.msg = 'General Fix - {}'.format(
            "<BodyPartExamined> is absent")
        msg.fix = "fixed by setting the <BodyPartExamined>"\
            "from {} to '{}'".format(old_bpe_txt, new_bpe)
        log.append(msg.getWholeMessage())
    if is_accurate_code_seq(new_ars) and not is_code_equal(old_ars, new_ars):
        code_value, code_meaning, coding_scheme_designator = new_ars
        if ars in ds:
            old_item_text = subfix_CodeSeqItem2txt(ds[ars], 0)
        else:
            old_item_text = 'None'
        new_item = CodeSeqItemGenerator(
            str(code_value), code_meaning, coding_scheme_designator)
        ars_a = DataElement(ars, 'SQ', DicomSequence([new_item,]))
        ds[ars] = ars_a
        msg = ErrorInfo()
        msg.msg = 'General Fix - {}'.format(
            "<AnatomicRegionSequence> is absent")
        msg.fix = "fixed by setting the <AnatomicRegionSequence>"\
            "from {} to '{}'".format(
                old_item_text,
                subfix_CodeSeqItem2txt(ars_a, 0))
        log.append(msg.getWholeMessage())



def CorrectAnatomicInfo(BodyPartexamined_, AnatomicRegion_):
    if BodyPartexamined_ is None and not is_accurate_code_seq(AnatomicRegion_):
        return (None, (None, None, None))
    bpe = None
    ars = (None, None, None)
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


def is_code_equal(code1 , code2) -> bool:
    if not (type(code1) == tuple and type(code2) == tuple):
        return False
    if not (len(code1) > 2 and len(code2) > 2):
        return False
    for i in range(0,3):
        if code1[i] != code2[i]:
            return False
    return True   


def get_old_anatomy(ds):
    bpe = tag_for_keyword('BodyPartExamined')
    ars = tag_for_keyword('AnatomicRegionSequence')
    old_bpe = None if bpe not in ds else ds[bpe].value
    old_ars_seq = None if ars not in ds else ds[bpe].value
    old_ars_val = (None, None, None)
    if old_ars_seq is not None:
        if len(old_ars_seq) > 0:
            old_ars_item = old_ars_seq[0]
            cm = None if CodeValue not in old_ars_item else \
                old_ars_item[CodeValue].value
            cv = None if CodeMeaning not in old_ars_item else \
                old_ars_item[CodeMeanin].value
            cs = None if CodingSchemeDesignator not in old_ars_item else \
                old_ars_item[CodingSchemeDesignato].value
            old_ars_val = (cv, cm, cs)
    return CorrectAnatomicInfo(old_bpe, old_ars_val)
    

