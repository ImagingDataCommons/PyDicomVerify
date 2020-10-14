import pydicom.datadict as Dic
from pydicom.datadict import tag_for_keyword
from pydicom.dataelem import(
    # CLASSES
    DataElement,)
from pydicom.dataset import(
    # CLASSES
    Dataset,)
from rightdicom.dcmvfy.attrverify_cc import(
    # FUNCTIONS
    isEmptyOrHasAllEmptyValues,
    verifyVM,
    verifyVR,)
from rightdicom.dcmvfy.mesgtext_cc import(
    # FUNCTIONS
    MMsgDC,
    WMsgDC,
    # CLASSES
    ErrorInfo,
    ErrorType,)
from numpy import uint32


def LogElementAndModule(module: str, element: str) -> str:
    mesg = ""
    if len(element) != 0:
        mesg += MMsgDC("Element") + " = <{}> ".format(element)
    if len(module) != 0:
        mesg += MMsgDC("Module") + " = <{}> ".format(module)
    return mesg


def ViolationMessage(error: str, elementtype: str,
                     module: str, element: str,
                     log: list, verbose: bool, has_fix=False):
    if not has_fix:
        mesg = "{} {} {}".format(#EMsgDC("Null"),
                                error, elementtype,
                                LogElementAndModule(module, element))
    else:
        mesg = error.format(#EMsgDC("Null"),
                             elementtype,
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


def fix_by_removing(ds: Dataset, kw: str, check_emptyness=True) -> str:
    exceptions = ['Laterality']
    for ex in exceptions:
        if ex == kw:
            return ''
    reason = ''
    attrib = ds[kw]
    if not(not attrib.is_empty and check_emptyness):
        del ds[kw]
        reason = "fixed by removing the attribute. "
    else:
        reason = "didn't fix since the attrib holds value = <{}>. ".format(
            attrib.value
       )
    return reason


def verifyRequired(ds: Dataset,
                   module: str, element: str,
                   verbose: bool,
                   log: list,
                   fix_trivials: bool,
                   multiplicityMin: uint32, multiplicityMax: uint32) -> bool:
    # Normalized Required Data Element

    err_vr = False
    err_vm = False
    err_empty = False
    err_not_exists = False
    reason = ""
    if element in ds:
        elem = ds[element]
    else:
        reason = "Error - T<{}> {}"
        reason = reason.format(ErrorType.Required.value,
                               MMsgDC("MissingAttribute"))
        err_not_exists = True
    if not err_not_exists:
        if elem.is_empty():
            reason = "Error - T<{}> {}"
            reason = reason.format(ErrorType.RequiredEmpty.value,
                                   MMsgDC("EmptyAttribute"))
            err_empty = True
        if not verifyVR(elem, module, element, verbose, log):
            reason = "Error - T<{}> {}"
            reason = reason.format(ErrorType.RequiredVR.value,
                                   MMsgDC("BadValueRepresentation"))
            err_vr = True
        else:
            if not verifyVM(elem, module, element, verbose, log,
                            multiplicityMin,
                            multiplicityMax, "source"):
                reason = "Error - T<{}> {}"
                reason = reason.format(ErrorType.RequiredVM.value,
                                       MMsgDC("BadAttributeValueMultiplicity"))
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
        fix_trivials: bool,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    err_vr = False
    err_vm = False
    err_empty = False
    err_not_exists = False
    reason = ""
    if element in ds:
        elem = ds[element]
    else:
        reason = "Error - T<{}> {}"
        reason = reason.format(ErrorType.Type1.value,
                               MMsgDC("MissingAttribute"))
        err_not_exists = True
    if not err_not_exists:
        if isEmptyOrHasAllEmptyValues(elem):
            reason = "Error - T<{}> {}"
            reason = reason.format(ErrorType.Type1Empty.value,
                               MMsgDC("EmptyAttribute"))
            err_empty = True
        if not verifyVR(elem, module, element, verbose, log):
            reason = "Error - T<{}> {}"
            reason = reason.format(ErrorType.Type1VR.value,
                                   MMsgDC("BadValueRepresentation"))
            err_vr = True
        else:
            if not verifyVM(elem, module, element,
                            log, multiplicityMin,
                            multiplicityMax, "source"):
                reason = "Error - T<{}> {}"
                reason = reason.format(ErrorType.Type1VM.value,
                                       MMsgDC("BadAttributeValueMultiplicity"))
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
        fix_trivials: bool,
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
    if element in ds:
        elem = ds[element]
    else:
        if not conditionNotSatisfied :
            reason = "Error - T<{}> {}"
            reason = reason.format(ErrorType.Type1CRequiredEmpty.value,
                                   MMsgDC("MissingAttribute"))
        err_not_exists = True
    if not err_not_exists:
        if condition_function != 0 and conditionNotSatisfied and not mbpo:
            reason = "Error - T<{}> {}"
            reason = reason.format(ErrorType.Type1CPresent.value,
                                   MMsgDC("AttributePresentWhenConditionUnsatisfied"
                       "WithoutMayBePresentOtherwise"))
            if fix_trivials:
                tmp = ErrorInfo(reason + "{} {}", fix_by_removing(ds, element))
                reason = tmp.getWholeMessage()
        if isEmptyOrHasAllEmptyValues(elem) and element in ds:
            if conditionNotSatisfied:
                reason = "Error - T<{}> {}"
                reason = reason.format(ErrorType.Type1CRedundantEmpty.value,
                                       MMsgDC("EmptyAttributeWhenConditionUnsatisfied"))
                if fix_trivials:
                    tmp = ErrorInfo(reason + "{} {}", fix_by_removing(ds, element))
                    reason = tmp.getWholeMessage()
            else:
                reason = "Error - T<{}> {}"
                reason = reason.format(ErrorType.Type1CRequiredEmpty.value,
                                       MMsgDC("EmptyAttribute"))
            err_empty = True
        else:
            if not verifyVR(elem, module, element, verbose, log):
                reason = "Error - T<{}> {}"
                reason = reason.format(ErrorType.Type1CVR.value,
                                       MMsgDC("BadValueRepresentation"))
                err_vr = True
            else:
                if not verifyVM(elem, module, element,
                                log, multiplicityMin,
                                multiplicityMax, "source"):
                    reason = "Error - T<{}> {}"
                    reason = reason.format(ErrorType.Type1CVM.value,
                                       MMsgDC("BadAttributeValueMultiplicity"))
                    err_vm = True
    if len(reason) != 0:
        if fix_trivials:
            ViolationMessage(reason, MMsgDC("Type1C"), module, element, log,
                         verbose, True)
        else:
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
        fix_trivials: bool,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    # Type 2 - Required Data Element (May be Empty)
    err_vr = False
    err_vm = False
    err_not_exists = False
    reason = ""
    if element in ds:
        elem = ds[element]
    else:
        reason = "Error - T<{}> {}"
        reason = reason.format(ErrorType.Type2.value,
                               MMsgDC("MissingAttribute"))
        err_not_exists = True
        if fix_trivials:  # add an empty attrib
            tmp = ErrorInfo(reason + "{} {}", fix_ByAddingEmptyAttrib(ds, element))
            reason = tmp.getWholeMessage()
    if not err_not_exists:
        # do not check emptiness
        if not elem.is_empty:
            if not verifyVR(elem, module, element, verbose, log):
                reason = "Error - T<{}> {}"
                reason = reason.format(ErrorType.Type2VR.value,
                                       MMsgDC("BadValueRepresentation"))
                err_vr = True
            else:
                if not verifyVM(elem, module, element, verbose, log,
                                multiplicityMin,
                                multiplicityMax):
                    reason = "Error - T<{}> {}"
                    reason = reason.format(ErrorType.Type2VM.value,
                                           MMsgDC("BadAttributeValueMultiplicity"))
                    err_vm = True
    if len(reason) != 0:
        if fix_trivials:
            ViolationMessage(reason, MMsgDC("Type2"), module, element, log,
                         verbose, True)
        else:
            ViolationMessage(reason, MMsgDC("Type2"), module, element, log,
                         verbose)
    else:
        ValidMessage(MMsgDC("Type2"), module, element, log, verbose)
    return len(reason) == 0


def fix_ByAddingEmptyAttrib(ds: Dataset, element:str) -> str:
    reason = ''
    ttag = tag_for_keyword(element)
    if ttag is not None:
        vr = Dic.dictionary_VR(ttag)
        element = DataElement(ttag, vr, '')
        element.value = element.empty_value
        ds[ttag] = element
        reason += "fixed by adding empty attribute"
    return  reason


def verifyType2C(
        ds: Dataset, module: str,
        element: str,
        verbose: bool,
        log: list,
        fix_trivials: bool,
        condition_function,
        mbpo: bool,
        parent_ds: Dataset,
        root_ds: Dataset,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    #    Type 2C - Conditional Data Element (May be Empty)

    err_not_exists = False
    err_vr = False
    err_vm = False
    reason = ""
    if condition_function == 0:
        conditionNotSatisfied = True
    else:
        conditionNotSatisfied = not condition_function(ds, parent_ds,
                                                       root_ds)
    if element in ds:
        elem = ds[element]
    else:
        if not conditionNotSatisfied :
            reason = "Error - T<{}> {}"
            reason = reason.format(ErrorType.Type2CAbsent.value,
                                   MMsgDC("MissingAttribute"))
        err_not_exists = True
    if not err_not_exists:
        if condition_function != 0 and conditionNotSatisfied and not mbpo:
            reason = "Error - T<{}> {}"
            reason = reason.format(ErrorType.Type2CPresent.value,
                                   MMsgDC(
                "AttributePresentWhenConditionUnsatisfiedWithoutMayBePresentOtherwise"))
            if fix_trivials:
                tmp = ErrorInfo(reason + "{} {}", fix_by_removing(ds, element))
                reason = tmp.getWholeMessage()
        if elem.is_empty:
            if not verifyVR(elem, module, element, verbose, log):
                reason = "Error - T<{}> {}"
                reason = reason.format(ErrorType.Type2CVR.value,
                                       MMsgDC("BadValueRepresentation"))
                err_vr = True
            else:
                if not verifyVM(elem, module, element, verbose,
                                log, multiplicityMin,
                                multiplicityMax, "source"):
                    reason = "Error - T<{}> {}"
                    reason = reason.format(ErrorType.Type2CVM.value,
                                           MMsgDC("BadAttributeValueMultiplicity"))
                    err_vm = True
    if len(reason) != 0:
        if fix_trivials:
            ViolationMessage(reason, MMsgDC("Type2C"), module, element, log,
                         verbose, True)
        else:
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
        fix_trivials: bool,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    # Type 3 - Optional Data Element

    not_exists = False
    reason = ""
    if element in ds:
        elem = ds[element]
    else:
        not_exists = True
         # this is optional

    err_vr = False
    err_vm = False
    # do not check emptiness
    if not not_exists:
        if not verifyVR(elem, module, element, verbose, log):
            reason = "Error - T<{}> {}"
            reason = reason.format(ErrorType.Type3VR.value,
                                   MMsgDC("BadValueRepresentation"))
            err_vr = True
        else:
            if not verifyVM(elem, module, element, verbose,
                            log, multiplicityMin,
                            multiplicityMax, "source"):
                reason = "Error - T<{}> {}"
                reason = reason.format(ErrorType.Type3VM.value,
                                       MMsgDC("BadAttributeValueMultiplicity"))
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
        fix_trivials: bool,
        condition_function,
        mbpo: bool,
        parent_ds: Dataset,
        root_ds: Dataset,
        multiplicityMin: uint32,
        multiplicityMax: uint32) -> bool:
    #   Type 3C - Conditional and Optional Data Element (May be Empty or Absent)
    reason = ""
    not_exists = False
    if condition_function == 0:
        conditionNotSatisfied = True
    else:
        conditionNotSatisfied = not condition_function(ds, parent_ds,
                                                       root_ds)
    if element in ds:
        elem = ds[element]
    else:
        not_exists = True
    if not not_exists:
        if not conditionNotSatisfied :
            WarningMessage(MMsgDC("Unexpected"),
                           MMsgDC("Type3C"), module, element, log, verbose)
        err_vr = False
        err_vm = False
        if not verifyVR(elem, module, element, verbose, log, fix_trivials):
            reason = "Error - T<{}> {}".format(
                ErrorType.Type3CVR.value, MMsgDC("BadValueRepresentation"))
            err_vr = True
        else:
            if not verifyVM(elem, module, element, verbose,
                            log, multiplicityMin,
                            multiplicityMax, "source"):
                reason = "Error - T<{}> {}"
                reason = reason.format(ErrorType.Type3CVM.value,
                                       MMsgDC("BadAttributeValueMultiplicity"))
                err_vm = True
    if len(reason) != 0:
        ViolationMessage(reason, MMsgDC("Type3C"), module, element, log,
                         verbose)
    else:
        ValidMessage(MMsgDC("Type3C"), module, element, log, verbose)
    return len(reason) == 0