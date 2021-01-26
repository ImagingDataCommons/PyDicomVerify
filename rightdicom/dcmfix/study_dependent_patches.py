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
from rightdicom.dcmvfy.condn_h import (
    Condition_LateralityRequired as checkLaterality)

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
        new_bpe, new_ars = CorrectAnatomicInfo(old_bpe, old_ars)
    
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
    AddLaterality(ds, log)



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
    return old_bpe, old_ars_val

def AddLaterality(ds: Dataset, log: list):
    needlaterality = checkLaterality(ds, 0, ds)
    old_laterality = None if "Laterality" not in ds else ds['Laterality'].value
    AddImageLateralityForBoth = False
    if needlaterality:
        if old_laterality is None:
            AddImageLateralityForBoth = True
        if old_laterality is not None:
            if old_laterality not in ['L', 'R']:
                if old_laterality.lower() == 'left':
                    new_laterality = 'L'
                elif old_laterality.lower() == 'right':
                    new_laterality = 'R'
                else:
                    new_laterality = None
                if new_laterality is not None:
                    msg = ErrorInfo()
                    msg.msg = 'General Fix - {}'.format(
                        "<Laterality> holds wrong value")
                    msg.fix = "fixed by setting the <Laterality>"\
                        "from {} to '{}'".format(old_laterality, new_laterality)
                    log.append(msg.getWholeMessage())
                    ds['Laterlaity'].value = new_laterality
                    return
                else:
                    AddImageLateralityForBoth = True
            else:
                return
    if 'Laterality' in ds:
        del ds['Laterality']
    if AddImageLateralityForBoth:
        kw = 'ImageLaterality'
        tg = tag_for_keyword(kw)
        imglaterality = DataElement(tg, 'CS', 'B')
        ds[tg] = imglaterality
        msg = ErrorInfo()
        msg.msg = 'General Fix - {}'.format(
                        "<Laterality> doesn't exist or holds wrong value")
        msg.fix = "fixed by changing the <Laterality>"\
            "to <{}> with value '{}' for both".format(kw, 'B')
        log.append(msg.getWholeMessage())


def fix_SOPReferencedMacro(
        ds: Dataset, log: list, suggested_SOPClassUID: dict = {}):
    kw = 'ReferencedStudySequence'
    tg = tag_for_keyword(kw)
    if tg not in ds:
        return
    val = ds[tg].value
    if len(val) == 0:
        del ds[tg]
        return
    i = 0
    
    while i < len(val):
        item = val[i]
        msg = ErrorInfo()
        if 'ReferencedSOPInstanceUID' not in item:
            msg.msg = 'General Fix - item {}/{} <ReferencedStudySequence>'\
                ' lacks <ReferencedSOPInstanceUID> attribute'.format(i + 1, len(val))
            msg.fix = 'fixed by removint the item'
            log.append(msg.getWholeMessage())
            val.pop(i)
            continue
        if item['ReferencedSOPInstanceUID'].is_empty:
            msg.msg = 'General Fix - item {}/{} <ReferencedStudySequence>'\
                ' holds an empty <ReferencedSOPInstanceUID> attribute'.format(i + 1, len(val))
            msg.fix = 'fixed by removint the item'
            log.append(msg.getWholeMessage())
            val.pop(i)
            continue
        if 'ReferencedSOPClassUID' not in item or\
                item['ReferencedSOPClassUID'].is_empty:
            uid = item['ReferencedSOPInstanceUID'].value
            msg.msg = 'General Fix - item {}/{} <ReferencedStudySequence>'\
                ' lacks <ReferencedSOPClassUID> attribute'.format(i + 1, len(val))
            if uid not in suggested_SOPClassUID:
                msg.fix = 'fixed by removint the item'
                log.append(msg.getWholeMessage())
                val.pop(i)
                continue
            else:
                msg.fix = 'fixed by querying the attribute '\
                    'ReferencedSOPClassUID filling it with {}'.format(
                        suggested_SOPClassUID[uid]
                    )
                log.append(msg.getWholeMessage())
                item['ReferencedSOPClassUID'].value = suggested_SOPClassUID[uid]
        i += 1
    if len(val) == 0:
        msg = ErrorInfo()
        msg.msg = 'General Fix - Attribute <{}> is empty '.format(kw)
        msg.fix = 'fixed by removint the attribute'
        log.append(msg.getWholeMessage())
        del ds[tg]
    return
    
    

