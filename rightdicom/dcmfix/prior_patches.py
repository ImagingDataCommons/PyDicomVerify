import pydicom.datadict as Dictionary
import rightdicom.dcmvfy.mesgtext_cc as mesgtext_cc
import rightdicom.dcmvfy.validate_vr as validate_vr
from pydicom.dataset import (
    # CLASSES
    Dataset,
)
from pydicom.sequence import (
    # CLASSES
    Sequence,
)
from rightdicom.dcmvfy.mesgtext_cc import (
    # CLASSES
    ErrorInfo,
)


def priorfix_RemoveIllegalTags(ds: Dataset, parent_kw:str, log:list) -> bool:
    tags_to_be_removed = []
    fixed = False
    for k, a in ds.items():
        try:
            a = ds[k]
        except KeyError as err:
            if not k.is_private:
                if not Dictionary.dictionary_has_tag(k):
                    ttaagg = validate_vr.tag2str(a.tag)
                    eerr = mesgtext_cc.ErrorInfo("General Fix - tag {} in {}is not a standard dicom tag".format(
                        ttaagg, parent_kw),
                    'fixed by removing the attribute')
                    log.append(eerr.getWholeMessage())
                    tags_to_be_removed.append(a.tag)
                    continue
        if type(a.value) == Sequence:
            for item in a.value:
                fixed = fixed or priorfix_RemoveIllegalTags(item, a.keyword, log)
        elif type(a.value) == Dataset:
            fixed = fixed or priorfix_RemoveIllegalTags(a.value, a.keyword, log)
    for tg in tags_to_be_removed:
        del ds[tg]
    return fixed

