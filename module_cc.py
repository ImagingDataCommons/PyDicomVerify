from pydicom import *
import pydicom.datadict as Dic
from pydicom.dataelem import DataElement
from pydicom.dataset import Dataset
import os
from numpy import *
from attrverify_cc import *
from mesgtext_cc import *


def LogElementAndModule(module: str, element: str) -> str:
    mesg = ""
    if len(element) != 0:
        mesg += MMsgDC("Element") + " = <{}>".format(element)
    if len(module) != 0:
        mesg += MMsgDC("Module") + " = <{}>".format(module)
    return mesg


def ViolationMessage(error: str, elementtype: str,
                     module: str, element: str,
                     log: list, verbose: bool):
    mesg = "{} {} {} {}".format(EMsgDC("Null"), error, elementtype,
                                LogElementAndModule(module, element))
    log.append(mesg)


def WarningMessage(error: str, elementtype: str,
                   module: str, element: str,
                   log: list, verbose: bool):
    mesg = "{} {} {} {}".format(WMsgDC("Null"), error, elementtype,
                                LogElementAndModule(module, element))
    log.append(mesg)


def ValidMessage(elementtype: str, module: str, element: str,
                 log: list, verbose: bool):
    if verbose:
        mesg = "{} - {} {}".format(MMsgDC("ValidElement"), elementtype,
                                   LogElementAndModule(module, element))


def verifyRequired(ds: Dataset,
                   module: str, element: str,
                   verbose: bool,
                   log: list,
                   ElementDictionary: dict,
                   multiplicityMin: uint32, multiplicityMax: uint32) -> bool:
    # Normalized Required Data Element

    err_vr = False
    err_vm = False
    err_empty = False
    err_not_exists = False
    reason = ""
    try:
        elem = ds[element]
    except (KeyError, ValueError):
        reason = MMsgDC("MissingAttribute")
        err_not_exists = True
    if not err_not_exists:
        if elem.is_empty():
            reason = MMsgDC("EmptyAttribute")
            err_empty = True
        if not verifyVR(elem, module, element, verbose, log):
            reason = MMsgDC("BadValueRepresentation")
            err_vr = True
        else:
            if not verifyVM(elem, module, element, verbose, log,
                            multiplicityMin,
                            multiplicityMax, "source"):
                reason = MMsgDC("BadAttributeValueMultiplicity")
                err_vm = True
    if len(reason) != 0:
        ViolationMessage(reason, MMsgDC("NormalizedRequired"), module, element,
                         log, verbose)
    else:
        ValidMessage(MMsgDC("NormalizedRequired"), module, element, log,
                     verbose)

    return len(reason) == 0


def verifyType1(
        ds: Dataset, module: str,
        element: str,
        verbose: bool,
        log: list,
        ElementDictionary: dict,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    err_vr = False
    err_vm = False
    err_empty = False
    err_not_exists = False
    reason = ""
    try:
        elem = ds[element]
    except (KeyError, ValueError):
        reason = MMsgDC("MissingAttribute")
        err_not_exists = True
    if not err_not_exists:
        if elem.is_empty:
            reason = MMsgDC("EmptyAttribute")
            err_empty = True

        if not verifyVR(elem, module, element, verbose, log):
            reason = MMsgDC("BadValueRepresentation")
            err_vr = True
        else:
            if not verifyVM(elem, module, element,
                            log, multiplicityMin,
                            multiplicityMax, "source"):
                reason = MMsgDC("BadAttributeValueMultiplicity")
                err_vm = True
    if len(reason) != 0:
        ViolationMessage(reason, MMsgDC("Type1"), module, element, log,
                         verbose)
    else:
        ValidMessage(MMsgDC("Type1"), module, element, log, verbose)
    return len(reason) == 0


def verifyType1C(
        ds: Dataset, module: str,
        element: str,
        verbose: bool,
        log: list,
        ElementDictionary: dict,
        condition_function,
        mbpo: bool,
        parent_ds: Dataset,
        root_ds: Dataset,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    err_not_exists = False
    err_empty = False
    err_vr = False
    err_vm = False
    reason = ""
    if condition_function == 0:
        conditionNotSatisfied = True
    else:
        conditionNotSatisfied = not condition_function(ds, parent_ds,
                                                       root_ds)
    try:
        elem = ds[element]
    except (KeyError, ValueError):
        if not conditionNotSatisfied:
            reason = MMsgDC("MissingAttribute")
        err_not_exists = True
    if not err_not_exists:
        if conditionNotSatisfied and not mbpo:
            ViolationMessage(
                MMsgDC("AttributePresentWhenConditionUnsatisfied"
                       "WithoutMayBePresentOtherwise"),
                MMsgDC("Type1C"), module, element, log, verbose);

        if isEmptyOrHasAllEmptyValues(elem):
            if conditionNotSatisfied:
                reason = MMsgDC("EmptyAttributeWhenConditionUnsatisfied")
            else:
                reason = MMsgDC("EmptyAttribute")
            err_empty = True
        else:
            if not verifyVR(elem, module, element, verbose, log):
                reason = MMsgDC("BadValueRepresentation")
                err_vr = True
            else:
                if not verifyVM(elem, module, element,
                                log, multiplicityMin,
                                multiplicityMax, "source"):
                    reason = MMsgDC("BadAttributeValueMultiplicity")
                    err_vm = True

    if len(reason) != 0:
        ViolationMessage(reason, MMsgDC("Type1C"), module, element, log,
                         verbose)
    else:
        ValidMessage(MMsgDC("Type1C"), module, element, log, verbose)
    return len(reason) == 0


def verifyType2(
        ds: Dataset, module: str,
        element: str,
        verbose: bool,
        log: list,
        ElementDictionary: dict,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    # Type 2 - Required Data Element (May be Empty)
    err_vr = False
    err_vm = False
    err_not_exists = False
    reason = ""
    try:
        elem = ds[element]
    except (KeyError, ValueError):
        reason = MMsgDC("BadValueRepresentation")
        err_not_exists = True
    if not err_not_exists:
        # do not check emptiness
        if not verifyVR(elem, module, element, verbose, log):
            reason = MMsgDC("BadValueRepresentation")
            err_vr = True
        else:
            if not verifyVM(elem, module, element, verbose, log,
                            multiplicityMin,
                            multiplicityMax):
                reason = MMsgDC("BadAttributeValueMultiplicity")
                err_vm = True
    if len(reason) != 0:
        ViolationMessage(reason, MMsgDC("Type2"), module, element, log, verbose)
    else:
        ValidMessage(MMsgDC("Type2"), module, element, log, verbose)

    return len(reason) == 0


def verifyType2C(
        ds: Dataset, module: str,
        element: str,
        verbose: bool,
        log: list,
        ElementDictionary: dict,
        condition_function,
        mbpo: bool,
        parent_ds: Dataset,
        root_ds: Dataset,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    #	 Type 2C - Conditional Data Element (May be Empty)

    err_not_exists = False
    err_vr = False
    err_vm = False
    reason = ""
    if condition_function == 0:
        conditionNotSatisfied = True
    else:
        conditionNotSatisfied = not condition_function(ds, parent_ds,
                                                       root_ds)
    try:
        elem = ds[element]
    except (KeyError, ValueError):
        if not conditionNotSatisfied:
            reason = MMsgDC("MissingAttribute")
        err_not_exists = True
    if not err_not_exists:

        if conditionNotSatisfied and not mbpo:
            ViolationMessage(MMsgDC(
                "AttributePresentWhenConditionUnsatisfiedWithoutMayBePresentOtherwise"),
                             MMsgDC("Type2C"), module, element, log, verbose)
        if not verifyVR(elem, module, element, verbose, log):
            reason = MMsgDC("BadValueRepresentation")
            err_vr = True
        else:
            if not verifyVM(elem, module, element,
                            log, multiplicityMin,
                            multiplicityMax, "source"):
                reason = MMsgDC("BadAttributeValueMultiplicity")
                err_vm = True
    if len(reason) != 0:
        ViolationMessage(reason, MMsgDC("Type2C"), module, element, log,
                         verbose)
    else:
        ValidMessage(MMsgDC("Type2C"), module, element, log, verbose)
    return len(reason) == 0


def verifyType3(
        ds: Dataset, module: str,
        element: str,
        verbose: bool,
        log: list,
        ElementDictionary: dict,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    # Type 3 - Optional Data Element

    err_not_exists = False
    reason = ""
    try:
        elem = ds[element]
    except (KeyError, ValueError):
        err_not_exists = True
        return True  # this is optional

    err_vr = False
    err_vm = False
    # do not check emptiness
    if not verifyVR(elem, module, element, verbose, log):
        reason = MMsgDC("BadValueRepresentation")
        err_vr = True
    else:
        if not verifyVM(elem, module, element,
                        log, multiplicityMin,
                        multiplicityMax, "source"):
            reason = MMsgDC("BadAttributeValueMultiplicity")
            err_vm = True
    if len(reason) != 0:
        ViolationMessage(reason, MMsgDC("Type3"), module, element, log, verbose)
    else:
        ValidMessage(MMsgDC("Type3"), module, element, log, verbose)
    return len(reason) == 0


def verifyType3C(
        ds: Dataset, module: str,
        element: str,
        verbose: bool,
        log: list,
        ElementDictionary: dict,
        condition_function,
        mbpo: bool,
        parent_ds: Dataset,
        root_ds: Dataset,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    #	 Type 2C - Conditional and Optional Data Element (May be Empty or Absent)
    reason = ""
    err_not_exists = False
    if condition_function == 0:
        conditionNotSatisfied = True
    else:
        conditionNotSatisfied = not condition_function(ds, parent_ds,
                                                       root_ds)
    try:
        elem = ds[element]
    except (KeyError, ValueError):
        err_not_exists = True
        return True

    if conditionNotSatisfied and not mbpo:
        WarningMessage(MMsgDC("Unexpected"),
                       MMsgDC("Type3C"), module, element, log, verbose)

    err_vr = False
    err_vm = False
    if not verifyVR(elem, module, element, verbose, log):
        reason = MMsgDC("BadValueRepresentation")
        err_vr = True
    else:
        if not verifyVM(elem, module, element,
                        log, multiplicityMin,
                        multiplicityMax, "source"):
            reason = MMsgDC("BadAttributeValueMultiplicity")
            err_vm = True
    if len(reason) != 0:
        ViolationMessage(reason, MMsgDC("Type3C"), module, element, log,
                         verbose)
    else:
        ValidMessage(MMsgDC("Type3C"), module, element, log, verbose)
    return len(reason) == 0
