from pydicom import *
from pydicom.datadict import *
from pydicom.dataelem import DataElement
from pydicom.multival import MultiValue
from pydicom.valuerep import *
from mesgtext_cc import *
from numpy import *
from strval_h import *


def isLongValueLengthInExplicitValueRepresentation(vr: str):
    # Check for known short form VRs, rather than known long form VRs,
    # since all new VRs will be long form, in case we encounter unrecognized
    # one but be sure and check that there really is a VR present
    return vr and vr[0] != 0 and vr[1] != 0 and (vr != "AE"
                                                 and vr != "AS"
                                                 and vr != "AT"
                                                 and vr != "CS"
                                                 and vr != "DA"
                                                 and vr != "DS"
                                                 and vr != "DT"
                                                 and vr != "FD"
                                                 and vr != "FL"
                                                 and vr != "IS"
                                                 and vr != "LO"
                                                 and vr != "LT"
                                                 and vr != "PN"
                                                 and vr != "SH"
                                                 and vr != "SL"
                                                 and vr != "SS"
                                                 and vr != "ST"
                                                 and vr != "TM"
                                                 and vr != "UI"
                                                 and vr != "UL"
                                                 and vr != "US"
                                                 )


def isKnownExplicitValueRepresentation(vr: str):
    return vr and (
            vr == "AE"
            or vr == "AS"
            or vr == "AT"
            or vr == "CS"
            or vr == "DA"
            or vr == "DS"
            or vr == "DT"
            or vr == "FL"
            or vr == "FD"
            or vr == "IS"
            or vr == "LO"
            or vr == "LT"
            or vr == "OB"
            or vr == "OD"
            or vr == "OF"
            or vr == "OL"
            or vr == "OW"
            or vr == "PN"
            or vr == "SH"
            or vr == "SL"
            or vr == "SQ"
            or vr == "SS"
            or vr == "ST"
            or vr == "TM"
            or vr == "UI"
            or vr == "UL"
            or vr == "UN"
            or vr == "UR"
            or vr == "US"
            or vr == "UT"
    )


def isStringVR(vr: str) -> bool:
    return vr and (vr == "AE"
                   or vr == "AS"
                   or vr == "CS"
                   or vr == "DA"
                   or vr == "DT"
                   or vr == "DS"
                   or vr == "IS"
                   or vr == "LO"
                   or vr == "LT"
                   or vr == "PN"
                   or vr == "SH"
                   or vr == "ST"
                   or vr == "TM"
                   or vr == "UC"
                   or vr == "UI"
                   or vr == "UR"
                   or vr == "UT")


def isNonOtherNumericOrDateOrTimeOrUIStringVR(vr: str) -> bool:
    return vr and (vr == "DA"
                   or vr == "DT"
                   or vr == "DS"
                   or vr == "IS"
                   or vr == "TM"
                   or vr == "UI")


def isNumericVR(vr: str) -> bool:
    return vr and (vr == "OB"
                   or vr == "OL"
                   or vr == "OW"
                   or vr == "OX"
                   or vr == "SL"
                   or vr == "SS"
                   or vr == "UL"
                   or vr == "US"
                   or vr == "XL"
                   or vr == "XS")


def isFloatVR(vr: str) -> bool:
    return vr and (vr == "FL"
                   or vr == "FD"
                   or vr == "OD"
                   or vr == "OF")


def verifyDefinedTerms(elem: DataElement, str_val: dict, verbose: bool,
                       log: list,
                       which: int) -> bool:
    val = elem.value
    vm = elem.VM
    if type(val) == MultiValue:
        if which == -1:
            candidate = val
        else:
            if which >= vm:
                return False
            else:
                candidate = [val[which]]
    else:
        if which >= 1:
            return False
        else:
            candidate = [val]

    for i, count in zip(candidate, range(0, len(candidate))):
        if type(i) != str:
            log.append(
                EMsgDC("TriedToVerifyDefinedTermsForNonStringAttribute") + \
                MMsgDC("ForAttribute") + "  <" + elem.description() + ">")
            return False
        if i in str_val:
            if verbose:
                log.append(
                    MMsgDC("RecognizedDefinedTerms") \
                    + " <" + i + "> " + MMsgDC("Is") + " <" + str_val[i] \
                    + "> " + MMsgDC("ForValue") + " {}".format(count + 1) \
                    + " " + MMsgDC("OfAttribute") + " <" \
                    + elem.description() + ">")
        else:
            msg = "{} <{}> {} {} {} {}".format(
                WMsgDC("UnrecognizedDefinedTerm"),
                i, MMsgDC("ForValue"), count + 1, MMsgDC("OfAttribute"),
                elem.description())
            log.append(msg)
            return True
    return False


def verifyEnumValues(elem: DataElement, str_val: dict, verbose: bool, log: list,
                     which: int) -> bool:
    success = True
    val = elem.value
    vm = elem.VM
    if type(val) == MultiValue:
        if which == -1:
            candidate = val
        else:
            if which >= vm:
                return False
            else:
                candidate = [val[which]]
    else:
        if which >= 1:
            return False
        else:
            candidate = [val]
    for i, count in zip(candidate, range(0, len(candidate))):
        converted_i = i
        if type(i) == DSfloat or \
                type(i) == DSdecimal or type(i) == IS:
            converted_i = str(i)
        elif type(i) == str:
            converted_i = i
        else:
            log.append(
                EMsgDC("TriedToVerifyEnumeratedValueForNonStringAttribute") + \
                MMsgDC("ForAttribute") + "  <" + elem.description() + ">")
            return False
        if converted_i in str_val:
            if verbose:
                log.append(
                    MMsgDC("RecognizedEnumeratedValue") \
                    + " <" + i + "> " + MMsgDC("Is") + " <" + str_val[i] \
                    + "> " + MMsgDC("ForValue") + " {}".format(count + 1) \
                    + " " + MMsgDC("OfAttribute") + " <" \
                    + elem.description() + ">")
        else:
            msg = "{} <{}> {} {} {} {}".format(
                EMsgDC("UnrecognizedEnumeratedValue"),
                i, MMsgDC("ForValue"), count + 1, MMsgDC("OfAttribute"),
                elem.description())
            log.append(msg)
            success = False
    return success


def verifyEnumValues_uint16(elem: DataElement, bin_method, verbose: bool,
                            log: list,
                            which: int) -> bool:
    success = True
    val = elem.value
    vm = elem.VM
    if type(val) == MultiValue:
        if which == -1:
            candidate = val
        else:
            if which >= vm:
                return False
            else:
                candidate = [val[which]]
    else:
        if which >= 1:
            return False
        else:
            candidate = [val]

    for i, count in zip(candidate, range(0, len(candidate))):
        if type(i) != int and type(i) != DSfloat and \
                type(i) != DSdecimal and type(i) != IS:
            log.append(
                EMsgDC("TriedToVerifyEnumeratedValueForNonNumericAttribute") + \
                MMsgDC("ForAttribute") + "  <" + elem.description() + ">")
        output = bin_method(uint16(i))
        if len(output) == 0:
            msg="{} <{}> {} {} {} {}".format(
                    EMsgDC("UnrecognizedEnumeratedValue"),
                    i, MMsgDC("ForValue"), count + 1, MMsgDC("OfAttribute"),
                    elem.description())
            log.append(msg)
            success = False
        else:
            if verbose:
                log.append(
                    MMsgDC("RecognizedEnumeratedValue") \
                    + " <{}> ".format(i) + MMsgDC("Is") + " <" + output \
                    + "> " + MMsgDC("ForValue") + " {}".format(count + 1) \
                    + " " + MMsgDC("OfAttribute") + " <" \
                    + elem.description() + ">")

    return success


def verifyBitMap(elem: DataElement, bin_method, verbose: bool, log: list,
                 which: int) -> bool:
    success = True
    val = elem.value
    vm = elem.VM
    if type(val) == MultiValue:
        if which == -1:
            candidate = val
        else:
            if which >= vm:
                return False
            else:
                candidate = [val[which]]
    else:
        if which >= 1:
            return False
        else:
            candidate = [val]

    for i, count in zip(candidate, range(0, len(candidate))):
        if type(i) != int and type(i) != DSfloat and \
                type(i) != DSdecimal and type(i) != IS:
            log.append(
                EMsgDC("TriedToVerifyBitMapForNonNumericAttribute") + \
                MMsgDC("ForAttribute") + "  <" + elem.description() + ">")
            return False
        output = bin_method(uint16(i))
        if len(output) == 0:
            msg = "{} <{}> {} {} {} {}".format(
                EMsgDC("UnrecognizedBitMap"),
                i, MMsgDC("ForValue"), count + 1, MMsgDC("OfAttribute"),
                elem.description())
            log.append(msg)
            success = False
        else:
            if verbose:
                log.append(
                    MMsgDC("RecognizedBitMap") \
                    + " <" + i + "> " + MMsgDC("Is") + " <" + output \
                    + "> " + MMsgDC("ForValue") + " {}".format(count + 1) \
                    + " " + MMsgDC("OfAttribute") + " <" \
                    + elem.description() + ">")
    return success


def verifyEnumValues_tag(elem: DataElement, tag_method, verbose: bool,
                         log: list,
                         which: int) -> bool:
    # I think group and element for all values of multivalue attribs is the same. I should ask this?
    success = True
    val = elem.value
    vm = elem.VM
    g = uint16(elem.tag.group)
    e = uint16(elem.tag.elemnt)
    output = tag_method(g, e)
    if len(output) == 0:
        msg = "{} <({},{})> {} {} {}".format(
            EMsgDC("UnrecognizedEnumeratedValue"),
            g,e, MMsgDC("ForValue"), MMsgDC("OfAttribute"),
            elem.description())
        log.append(msg)
        success = False
    else:
        if verbose:
            log.append(
                MMsgDC("RecognizedEnumeratedValue") \
                + " <" + "({},{})".format(g, e) + "> " + MMsgDC(
                    "Is") + " <" + output \
                + "> " + MMsgDC("ForValue") + val \
                + " " + MMsgDC("OfAttribute") + " <" \
                + elem.description() + ">")
    # if which == -1:
    #     candidate = val
    # else:
    #     if which >= vm:
    #         return False
    #     else:
    #         candidate = val[which]
    # for i in candidate:
    #     if type(i) != int:
    #         return False
    #     output = tag_method(uint16(elem.tag.group), uint16(elem.tag.elemnt))
    #     if len(output) == 0:
    #         print("Unrecognized defined term for {}".format(elem.keyword))
    #         success = False
    #     else:
    #         print("print sth if verbose")
    return success


def verifyNotZero(elem: DataElement, verbose: bool, log: list,
                  which: int, warningNotError: bool) -> bool:
    success = True
    if elem.is_empty:
        return True
    val = elem.value


    vm = elem.VM
    if type(val) == MultiValue:
        if which == -1:
            candidate = val
        else:
            if which >= vm:
                return False
            else:
                candidate = [val[which]]
    else:
        if which >= 1:
            return False
        else:
            candidate = [val]

    for i, count in zip(candidate, range(0, len(candidate))):
        if not (type(i) == int or type(i) == DSfloat or
                type(i) == DSdecimal or type(i) == IS or
                type(i) == float):
            log.append("{} {} <{}>".format(
                EMsgDC("TriedToVerifyNotZeroForNonNumericAttribute"),
                MMsgDC("ForAttribute"), elem.description()))
            return False
        if i == 0:
            log.append("{} {} {} {} <{}>".format(
                (WMsgDC("ZeroValue") if warningNotError else EMsgDC(
                    "ZeroValue")),
                MMsgDC("ForValue"), (count + 1) ,
                MMsgDC("OfAttribute"), elem.description()))
            success = False

    return success


def verifyVR(elem: DataElement, module: str, element: str, verbose: bool,
             log: list):
    # tag = getTag();

    # if (tag.isPrivateTag()) :
    #     return True
    v= elem.value
    try:
        vrd = dictionary_VR(elem.tag)
    except BaseException as err:
        print(err)
        mssg = EMsgDC("NoSuchElementInDictionary") + " "
        if len(element) != 0:
            mssg += MMsgDC("Element") + "=<" + element + ">"
        if len(module) != 0:
            mssg += MMsgDC("Module") + "=<" + module + ">"
        log.append(mssg)
        return False

    vre = elem.VR

    if vre != vrd and not (vrd == "OX" and vre == "OB" or vre == "OW") \
            and not (vrd == "XS" and vre == "US" or vre == "SS") \
            and not (vrd == "XO" and vre == "US" or vre == "SS" or vre == "OW") \
            and not (vrd == "XL" and vre == "UL" or vre == "SL"):
        mssg = EMsgDC("BadValueRepresentation") \
               + " " + vre + " (" + vrd + " " + MMsgDC("Required") + ")"
        if len(element) != 0:
            mssg += MMsgDC("Element") + "=<" + element + ">";
        if len(module) != 0:
            mssg += MMsgDC("Module") + "=<" + module + ">";
        log.append(mssg)
        return False
    else:
        return True


def vmpart2num(vmpart: str):
    if vmpart.isnumeric():
        return [uint32(vmpart), False]
    elif vmpart == 'n':
        return [1, True]
    elif vmpart[-1] == 'n':
        return [vmpart[:len(vmpart) - 1], True]
    else:
        return [-1, False]


def getVM_min_max(vm: str):
    has_min_multiplicity = False
    has_max_multiplicity = False
    if vm.isnumeric():
        mmin = uint32(vm)
        mmax = uint32(vm)
    else:
        minmax = vm.split('-')
        [mmin, has_min_multiplicity] = vmpart2num(minmax[0])
        [mmax, has_max_multiplicity] = vmpart2num(minmax[1])
    return [mmin, has_min_multiplicity, mmax, has_max_multiplicity]


def verifyVM(elem: DataElement, module: str, element: str, verbose: bool,
             log: list,
             multiplicityMin: uint32, multiplicityMax: uint32,
             specifiedSource = ""):
    ttag = elem.tag
    current_vm = elem.VM

    vm = dictionary_VM(ttag)
    if multiplicityMax == 0 and multiplicityMin == 0:
        [dictmin, has_min_multiplicity, dictmax,
         has_max_multiplicity] = getVM_min_max(vm)
        source = MMsgDC("Dictionary")
    else:
        dictmin = multiplicityMin
        dictmax = multiplicityMax
        has_min_multiplicity = False
        has_max_multiplicity = False
        source = specifiedSource if len(specifiedSource) > 0 else MMsgDC(
            "ModuleDefinition")
    min_err = False
    max_err = False
    if has_min_multiplicity:
        min_err = (current_vm % dictmin == 0)
    else:
        min_err = current_vm < dictmin

    if has_max_multiplicity:
        max_err = (current_vm % dictmax == 0)
    else:
        max_err = current_vm > dictmin
    message = ""
    err = min_err and max_err

    if err:
        mssg = EMsgDC("BadAttributeValueMultiplicity") \
               + "{}".format(vm) + " (" + dictmin
        if dictmin != dictmax:
            if not has_max_multiplicity and dictmax == 0xFFFFFFFF:
                mssg += "-n"
            elif has_max_multiplicity:
                mssg += "-{}n".format(dictmax)
            else:
                mssg += "-{}".format(dictmax)
        mssg += " " + MMsgDC("RequiredBy") + " " + source + ")"
        if len(element) != 0:
            mssg += MMsgDC("Element") + "=<" + element + ">";
        if len(module) != 0:
            mssg += MMsgDC("Module") + "=<" + module + ">"
        log.append(mssg)

    return not err


def isEmptyOrHasAnyEmptyValue(elem: DataElement) -> bool:
    if elem.is_empty:
        return True
    v = elem.value
    if type(v) != MultiValue:
        return v.is_empty
    else:
        for i in v:
            try:
                length = len(i)
            except:
                return False
            if length == 0:
                return True
    return False


def isEmptyOrHasAllEmptyValues(elem: DataElement) -> bool:
    if elem.is_empty:
        return True
    v = elem.value

    if type(v) != MultiValue:
        return elem.is_empty
    else:
        for i in v:
            try:
                length = len(i)
            except:
                return False
            if length > 0:
                return False
    return True
