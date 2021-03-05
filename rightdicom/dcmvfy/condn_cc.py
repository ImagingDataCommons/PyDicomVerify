from numpy import uint16, int32
import enum
import rightdicom.dcmvfy.attrverify_cc
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
    Tag,
    BaseTag,)


def ElementPresent(ds: Dataset, tagname: str):
    return tagname in ds


def ElementPresentMasked(ds: Dataset, tagname: str, mask: uint16):
    try:
        elem = ds[tagname]
    except(KeyError, ValueError):
        return False
    g = uint16(elem.tag.group) & mask
    e = uint16(elem.tag.element)
    for elem in ds.items():
        t = elem.tag
        if(not t.is_private) and(uint16(t.group) & mask == g) and(
                uint16(t.element) == e):
            return True
    return False


def ElementPresentAbove(parent_ds, tagname: str):
    if parent_ds == 0:
        return False
    return tagname in parent_ds


def ElementPresentWithin(ds: Dataset, tagname: str,
                         sequencetag: str) -> bool:
    present = False
    try:
        elem = ds[sequencetag]
    except(KeyError, ValueError):
        return False
    if type(elem.value) != Sequence:
        return False
    for d in elem.value:
        if tagname in d:
            present = True
            break
    return present


def ElementPresentInPath(ds: Dataset, tagname: str) -> bool:
    if tagname in ds:
        return True
    if type(ds) == Sequence:
        for inner_item in ds:
            return ElementPresentInPath(inner_item, tagname)

    for d in ds.items():
        current_elem = d[1]
        current_value = current_elem.value
        if type(current_value) == Sequence:
            for inner_d in current_value:
                return ElementPresentInPath(inner_d, tagname)
    return False


def ElementPresentInPathFirstItem(ds: Dataset, tagname: str) -> bool:
    if tagname in ds:
        return True
    for d in ds.items():
        current_elem = d[1]
        current_value = current_elem.value
        if type(current_value) == Sequence and len(current_value) > 1:
            inner_d = current_value[0]
            return ElementPresentInPathFirstItem(inner_d, tagname)
    return False


def ElementPresentInPathFromRoot(ds: Dataset, tagname: str,
                                 sequencetag: str) -> bool:
    try:
        elem = ds[sequencetag]
    except(KeyError, ValueError):
        return False
    if type(elem.value) != Sequence:
        return False
    for d in elem.value:
        if ElementPresentInPath(d, tagname):
            return True
    return False


def ElementPresentInPathFromRootFirstItem(ds: Dataset, tagname: str,
                                          sequencetag: str) -> bool:
    try:
        elem = ds[sequencetag]
    except(KeyError, ValueError):
        return False
    if type(elem.value) != Sequence:
        return False
    if len(elem.value) == 0:
        return False
    d = elem.value[0]
    if ElementPresentInPathFirstItem(d, tagname):
        return True
    return False


def GroupPresent(ds: Dataset, tagname: str) -> bool:
    try:
        elem = ds[tagname]
    except(KeyError, ValueError):
        return False
    # except TypeError:
    #     print("")
    g = uint16(elem.tag.group)
    for(key, elem) in ds.items():
        t = elem.tag
        if uint16(t.group) == g:
            return True
    return False


def GroupPresentMasked(ds: Dataset, tagname: str, mask: uint16) -> bool:
    try:
        elem = ds[tagname]
    except(KeyError, ValueError):
        return False
    g = uint16(elem.group) & mask
    for elem in ds.items():
        t = elem.tag
        if uint16(t.group) & mask == g:
            return True
    return False


def ValuePresent(ds: Dataset, tagname: str, valueselector: int) -> bool:
    try:
        elem = ds[tagname]
    except(KeyError, ValueError):
        return False
    if valueselector < 0:
        return elem.VM > 0
    if(valueselector >= elem.VM):
        return False
    else:
        return True


def StringValueMatch(ds: Dataset, tagname: str, valueselector: int,
                     value: str) -> bool:
    candidate = 0
    try:
        elem = ds[tagname]
    except(KeyError, ValueError):
        return False
    v = elem.value
    if type(v) == MultiValue:
        if valueselector < 0:
            candidate = v
        if valueselector >= len(v):
            return False
        else:
            candidate = [v[valueselector]]
    else:
        candidate = [v]
    for v in candidate:
        if v == value:
            return True
    return False


def TagValueMatch(ds: Dataset, tagname: str, valueselector: int,
                  tagnametomatch: BaseTag) -> bool:
    candidate = 0
    if tagname not in ds:
        return False
    elem = ds[tagname]
    if valueselector < 0:
        candidate = elem.value()
    if valueselector >= elem.VM:
        return False
    else:
        candidate = [elem.value[valueselector]]
    for v in candidate:
        if type(v) == int:
            x = Tag(v)
        elif type(v) == tuple:
            x = Tag(v)
        elif type(v) == BaseTag:
            x = v
        else:
            return False
        if x == tagnametomatch:
            return True
    return False


class BinaryValueMatchOperator(enum.IntEnum):
    Equals = 0
    NotEquals = 1
    LessThan = 2
    LessThanOrEquals = 3
    GreaterThan = 4
    GreaterThanOrEquals = 5


def BinaryValueMatch(ds: Dataset, tagname: str, valueselector: int,
                     matchoperator: BinaryValueMatchOperator,
                     valuetomatch: int32) -> bool:
    candidate = 0
    try:
        elem = ds[tagname]
    except(KeyError, ValueError):
        return False
    vm = elem.VM
    val = elem.value
    if vm > 1:
        if valueselector == -1:
            candidate = val
        else:
            if valueselector >= vm:
                return False
            else:
                candidate = [val[valueselector]]
    elif vm == 1:
        if valueselector >= 1:
            return False
        else:
            candidate = [val]
    elif vm == 0:
        return False
    for v in candidate:
        if not  rightdicom.dcmvfy.attrverify_cc.isPydicomNumeric(v):
            return False
        if(
                matchoperator == BinaryValueMatchOperator.Equals and v == valuetomatch) \
                or(
                matchoperator == BinaryValueMatchOperator.NotEquals and v != valuetomatch) \
                or(
                matchoperator == BinaryValueMatchOperator.LessThan and v < valuetomatch) \
                or(
                matchoperator == BinaryValueMatchOperator.LessThanOrEquals and v <= valuetomatch) \
                or(
                matchoperator == BinaryValueMatchOperator.GreaterThan and v > valuetomatch) \
                or(
                matchoperator == BinaryValueMatchOperator.GreaterThanOrEquals and v >= valuetomatch):
            return True
    return False


def SequenceHasItems(ds: Dataset, tagname: str) -> bool:
    try:
        elem = ds[tagname]
    except(KeyError, ValueError):
        return False
    if type(elem.value) != Sequence:
        return False
    return len(elem.value) > 0


def SequenceHasOneItem(ds: Dataset, tagname: str) -> bool:
    try:
        elem = ds[tagname]
    except(KeyError, ValueError):
        return False
    if type(elem.value) != Sequence:
        return False
    return len(elem.value) == 1


def SequenceHasMultipleItems(ds: Dataset, tagname: str) -> bool:
    try:
        elem = ds[tagname]
    except(KeyError, ValueError):
        return False
    if type(elem.value) != Sequence:
        return False
    return len(elem.value) > 1


def ElementStringValueMatchWithin(ds: Dataset, tagname: str,
                                  sequencetag: str, valueselector: int,
                                  string: str) -> bool:
    try:
        elem = ds[sequencetag]
    except(KeyError, ValueError):
        return False
    if type(elem.value) != Sequence:
        return False
    for d in elem.value:
        if tagname in d:
            return StringValueMatch(ds, tagname, valueselector, string)
    return False