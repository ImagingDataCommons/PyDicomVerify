from pydicom import (
    # SUBMODULES
    Dataset,
)
from rightdicom.dcmfix import (
    # SUBMODULES
    general_patches,
    specific_patches,
)
from rightdicom.dcmfix.prior_patches import (
    # FUNCTIONS
    priorfix_RemoveIllegalTags,
)
from rightdicom.dcmfix.specific_patches import (
    # FUNCTIONS
    fix_Trivials,
)


def fix_dicom(ds: Dataset, log_fix: list):
    priorfix_RemoveIllegalTags(ds, 'All', log_fix)
    # (1)general fixes:
    for ffix in dir(general_patches):
        if ffix.startswith("generalfix_"):
            item = getattr(general_patches, ffix)
            if callable(item):
                item(ds, log_fix)
    # (2)fix with verification:
    fix_Trivials(ds, log_fix)
    # (3)specific fixes:
    for ffix in dir(specific_patches):
        if ffix.startswith("fix_"):
            if ffix == "fix_Trivials":
                continue
            item = getattr(specific_patches, ffix)
            if callable(item):
                item(ds, log_fix)
    return ds