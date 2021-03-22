import logging
import logging.config
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
    logger = logging.getLogger(__name__)
    tags_to_be_removed = []
    fixed = False
    for k, a in ds.items():
        try:
            a = ds[k]
        except BaseException as err:
            ttaagg = validate_vr.tag2str(k)
            eerr = mesgtext_cc.ErrorInfo(
                "General Fix - attribute with tag {} in {} is not"
                " readable by pydicom".format(
                ttaagg, parent_kw),
            'fixed by removing the attribute')
            log.append(eerr.getWholeMessage())
            loggermsg = 'attribute with tag {} in {} is not '\
                'readable by pydicom because {}'.format(ttaagg, parent_kw, err)
            logger.error(loggermsg, stack_info=True)
            tags_to_be_removed.append(k)
            continue
        if type(a.value) == Sequence:
            for item in a.value:
                fixed = fixed or priorfix_RemoveIllegalTags(item, a.keyword, log)
        elif type(a.value) == Dataset:
            fixed = fixed or priorfix_RemoveIllegalTags(a.value, a.keyword, log)
    for tg in tags_to_be_removed:
        del ds[tg]
    return fixed

