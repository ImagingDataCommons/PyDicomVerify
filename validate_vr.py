from pydicom import *
from pydicom.tag import Tag
from pydicom.tag import BaseTag
from pydicom.dataset import Dataset
from pydicom.dataelem import DataElement
from pydicom.sequence import Sequence
from pydicom.multival import MultiValue
import pydicom.datadict as Dictionary
from pydicom.uid import UID
from pydicom.valuerep import *
from numpy import *
from mesgtext_cc import *
import curses.ascii
import pydicom.values
from sopclc_h import *
import module_cc
import re
import pydicom.config
from pydicom.dataelem import RawDataElement

default_encoding = pydicom.charset.convert_encodings([default_encoding])[0]


def isValidText(bytecodes: bytes, encodings: list) -> list:

    pydicom.config.enforce_valid_values = True
    badChars = []
    try:
        pydicom.charset.decode_string(bytecodes, encodings, [])
    except UnicodeDecodeError as err:
        badChars = [err.start, err.end]
    except ValueError as err:
        badChars = [-1, -1] # means bad escape char
    pydicom.config.enforce_valid_values = False
    return badChars


def tag2str(ttag: BaseTag):
    if Dictionary.dictionary_has_tag(ttag):
        desc = Dictionary.dictionary_description(ttag)
        vr = Dictionary.dictionary_VR(ttag)
        txt = "-> \t {}:\t{}".format(vr, desc)
    else:
        txt = ''
    msg = "(0x{:0>4x}, 0x{:0>4x}) {}".format(ttag.group, ttag.element, txt)
    return msg


def writeWarningVRValue(log: list, ttag: str, vr: str, valuenumber: int,
                        value: str):
    msg = "{} - {}, {}[{}] = <{}>"
    msg = msg.format(
        WMsgDC("ValueDubiousForThisVR"),
        tag2str(ttag), vr if vr else 0,
        valuenumber, value if value else "")
    log.append(msg)


def writeErrorBadVR(log: list, ttag: str, vr: str):
    msg = "{} - {} {} "
    msg = msg.format(
        EMsgDC("ValueInvalidForThisVR"),
        tag2str(ttag), vr if vr else 0,
    )
    log.append(msg)


def writeErrorBadVRValue(log: list, ttag: str, vr: str, valuenumber: int,
                         value: str):
    msg = "{} - {}, {}[{}] = <{}>"
    msg = msg.format(
        EMsgDC("ValueInvalidForThisVR"),
        tag2str(ttag), vr if vr else 0,
        valuenumber, value if value else "")
    log.append(msg)


def writeErrorBadTrailingChar(log: list, ttag: str, vr: str, c: str,
                              c_incoded: bytes):
    writeErrorBadVR(log, ttag, vr)
    msg = "{} = '{}' (0x{:>4x})"
    msg = msg.format(
        MMsgDC("TrailingCharacterInvalidForThisVR"),
        c, c_incoded[0] & 0xff)
    log[-1] += (" - " + msg)


def writeErrorBadVRCharNL(log: list, ttag: str, vr: str, c: str,
                          c_incoded: bytes):
    writeErrorBadVR(log, ttag, vr)
    msg = "{} = '{}' (0x{:0>4x})"
    msg = msg.format(
        MMsgDC("CharacterInvalidForThisVR"),
        c, c_incoded[0] & 0xff)
    log[-1] += (" - " + msg)


def writeErrorBadVRCharNL_withNumber(log: list, ttag: str, vr: str,
                                     valuenumber: int,
                                     value: str,
                                     c: str,
                                     c_incoded: bytes):
    writeErrorBadVRValue(log, ttag, vr, valuenumber, value)

    msg = "{} = '{}' (0x{:0>4x})"
    msg = msg.format(
        MMsgDC("CharacterInvalidForThisVR"),
        c, c_incoded[0] & 0xff)
    log[-1] += (" - " + msg)


def writeErrorBadCharacterRepertoireCharNL(log: list, ttag: str, vr: str,
                                           valuenumber: int, value: str,
                                           c: str,
                                           c_incoded: bytes):
    writeErrorBadVRValue(log, ttag, vr, valuenumber, value)

    msg = "{} = '{}' (0x{:0>4x})"
    msg = msg.format(
        MMsgDC("CharacterInvalidForCharacterRepertoire"),
        c, c_incoded[0] if len(c_incoded) > 0 else 0)
    log[-1] += (" - " + msg)


def writeErrorBadVRLengthNL(log: list, ttag: str, vr: str, valuenumber: int,
                            value: str,
                            length: int, expected: str):
    writeErrorBadVRValue(log, ttag, vr, valuenumber, value)

    msg = "{} = {}, {} {}"
    msg = msg.format(
        MMsgDC("CharacterInvalidForCharacterRepertoire"),
        length, MMsgDC("Expected"), expected)
    log[-1] += (" - " + msg)


def isnumber(n: str) -> bool:
    try:
        x = float(n)
        return True
    except:
        return False


def isinteger(n: str) -> bool:
    try:
        x = int(n)
        return True
    except:
        return False


def StringCheck(s: bytes) -> dict:
    out = {"TrailingNullBytes": False, "EmbededNullBytes": False,
           "TrainlingWhiteSpace": False}
    l = len(s)
    foundNonNullByte = False
    for ii in range(l - 1, -1, -1):

        asc = s[ii]
        if asc == 0:
            if foundNonNullByte:
                out["EmbededNullBytes"] = True
            else:
                out["TrailingNullBytes"] = True
        else:
            foundNonNullByte = True
    if curses.ascii.isspace(s[-1]):
        out["TrainlingWhiteSpace"] = True
    return out


def writeErrorBadVRRange(log: list, ttag: str, vr: str, valuenumber: int,
                         value: str,
                         expected: str):
    writeErrorBadVRValue(log, ttag, vr, valuenumber, value)

    msg = "{}, {} {}"
    msg = msg.format(
        MMsgDC("RangeInvalidForThisVR"), MMsgDC("Expected"), expected)
    log[-1] += msg


def validateVR_AE(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok

    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]

    for i, vn in zip(val, range(0, len(val))):
        if len(i) > 16:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 16")
            ok = False

        encoded = i.encode(default_encoding)
        for ch in encoded:
            if curses.ascii.iscntrl(ch) or curses.ascii.isspace(ch):
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, i, ch)
        out = StringCheck(encoded)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def validateVR_AS(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        if l != 4:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "== 4")
            ok = False

        for idx in range(0, 3):
            ch = i[idx]
            encoded = i[idx].encode(default_encoding)
            if not ch.isdigit():
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, i, ch)
        if not (i[3] == "D" or i[3] == "W" or i[3] == "M" or i[3] == "Y"):
            writeErrorBadVRCharNL_withNumber(log, elem.tag, elem.VR, vn, i, ch,
                                             encoded)
            ok = False
        out = StringCheck(i.encode(default_encoding))

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def validateVR_CS(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        if l > 16:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 16")
            ok = False
        if type(i) == str:
            decoded = i
        elif type(i) == bytes:
            decoded = i.decode(default_encoding)
        else:
            print("type i is {}".format(type(i)))

        for idx in range(0, len(decoded)):
            ch = decoded[idx]
            code = ch.encode(default_encoding)
            if not (ch.isupper() or ch.isdigit() or ch == " " or ch == "_"):
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, decoded, ch, code)
        out = StringCheck(i)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def validateVR_DA(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        if type(i) == date:
            i = i.original_string
        l = len(i)
        if l == 0:
            continue
        if l == 8 or l == 10:
            idx = 0
            if i[idx] != '1' and i[idx] != '2':
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, i, i[idx],
                    i[idx].encode(default_encoding))
                ok = False
            idx += 1
            if not i[idx].isdigit():
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, i, i[idx],
                    i[idx].encode(default_encoding))
                ok = False
            idx += 1
            if idx < l:
                if not i[idx].isdigit():
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False
                idx += 1
            if idx < l:
                if not i[idx].isdigit():
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False
                idx += 1

            if idx < l:
                if i[idx] == '.' and l == 10:
                    # CP 714 (000513)
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False
                    idx += 1
            if idx < l:
                if i[idx] != '0' and i[idx] != '1':
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False
                idx += 1
            if idx < l:
                if not i[idx].isdigit():
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False
                idx += 1
            if idx < l:
                if i[idx] == '.' and l == 10:
                    # CP 714 (000513)
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False
                    idx += 1
            if idx < l:
                if i[idx] != '0' and i[idx] != '1' and i[idx] != '2' and i[
                    idx] != '3':
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False
                idx += 1
            if idx < l:
                if not i[idx].isdigit():
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False

        else:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "== 8 or 10")
            ok = False
        out = StringCheck(i.encode(default_encoding))

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def validateVR_DT(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        if type(i) == datetime:
            i = i.original_string
        if l >= 2 or l <= 26:
            idx = 0
            if i[idx] != '1' and i[idx] != '2':
                writeErrorBadVRCharNL_withNumber(log, elem.tag, elem.VR, vn, i,
                                                 i[idx], i[idx].encode(
                        default_encoding))
                ok = False
            idx += 1
            if not i[idx].isdigit():
                writeErrorBadVRCharNL_withNumber(log, elem.tag, elem.VR, vn, i,
                                                 i[idx], i[idx].encode(
                        default_encoding))
                ok = False
            idx += 1
            if idx < l:  # Not just CC
                if not i[idx].isdigit():
                    writeErrorBadVRCharNL_withNumber(log, elem.tag, elem.VR, vn,
                                                     i, i[idx], i[idx].encode(
                            default_encoding))
                    ok = False
                idx += 1
                if idx < l:
                    if not i[idx].isdigit():
                        writeErrorBadVRCharNL_withNumber(log, elem.tag, elem.VR, vn,
                                                         i, i[idx], i[idx].encode(
                                default_encoding))
                        ok = False
                    idx += 1
                if idx < l:  # Not just CCYY
                    if i[idx] != '0' and i[idx] != '1':
                        writeErrorBadVRCharNL_withNumber(
                            log, elem.tag, elem.VR, vn, i, i[idx],
                            i[idx].encode(default_encoding))
                        ok = False
                    idx += 1
                    if idx < l:
                        if not i[idx].isdigit():
                            writeErrorBadVRCharNL_withNumber(
                                log, elem.tag, elem.VR, vn, i, i[idx],
                                i[idx].encode(default_encoding))
                            ok = False
                        idx += 1
                    if idx < l:  # Not just CCYYMM
                        if i[idx] != '0' and i[idx] != '1' and i[idx] != '2' and \
                                i[idx] != '3':
                            writeErrorBadVRCharNL_withNumber(
                                log, elem.tag, elem.VR, vn, i, i[idx],
                                i[idx].encode(default_encoding))
                            ok = False
                        idx += 1
                        if idx < l:
                            if not i[idx].isdigit():
                                writeErrorBadVRCharNL_withNumber(
                                    log, elem.tag, elem.VR, vn, i, i[idx],
                                    i[idx].encode(default_encoding))
                                ok = False
                            idx += 1
                            if idx < l:  # Not just CCYYMMDD
                                if i[idx] != '0' and i[idx] != '1' and i[
                                    idx] != '2':
                                    writeErrorBadVRCharNL_withNumber(
                                        log, elem.tag, elem.VR, vn, i, i[idx],
                                        i[idx].encode(
                                            default_encoding))
                                    ok = False
                                idx += 1
                                if idx < l:
                                    if not i[idx].isdigit():
                                        writeErrorBadVRCharNL_withNumber(
                                            log, elem.tag, elem.VR, vn, i, i[idx],
                                            i[idx].encode(
                                                default_encoding))
                                        ok = False
                                idx += 1
                                if idx < l:  # Not just CCYYMMDDHH
                                    if i[idx] != '0' and i[idx] != '1' and i[
                                        idx] != '2' and i[idx] != '3' and i[
                                        idx] != '4' and i[idx] != '5':
                                        writeErrorBadVRCharNL_withNumber(
                                            log, elem.tag, elem.VR, vn, i, i[idx],
                                            i[idx].encode(
                                                default_encoding))
                                        ok = False
                                    idx += 1
                                    if idx < l:
                                        if not i[idx].isdigit():
                                            writeErrorBadVRCharNL_withNumber(
                                                log, elem.tag, elem.VR, vn, i, i[idx],
                                                i[idx].encode(
                                                    default_encoding))
                                            ok = False
                                    idx += 1
                                    if idx < l:  # Not just CCYYMMDDHHMM
                                        if i[idx] != '0' and i[idx] != '1' and i[
                                            idx] != '2' and i[idx] != '3' and i[
                                            idx] != '4' and i[idx] != '5':
                                            writeErrorBadVRCharNL_withNumber(
                                                log, elem.tag, elem.VR, vn, i,
                                                i[idx], i[idx].encode(
                                                    default_encoding))
                                            ok = False
                                        idx += 1
                                        if idx < l:
                                            if not i[idx].isdigit():
                                                writeErrorBadVRCharNL_withNumber(
                                                    log, elem.tag, elem.VR, vn, i,
                                                    i[idx], i[idx].encode(
                                                        default_encoding))
                                                ok = False
                                            idx += 1

                                        if idx < l:  # Not just CCYYMMDDHHMMSS
                                            if i[idx] == '.':  # .FFFFFF
                                                idx += 1
                                                while idx < l and i[idx].isdigit():
                                                    idx += 1
                                        if idx < l:
                                            if i[idx] == '+' or i[
                                                idx] == '-':  # + or - ZZZZ
                                                idx += 1
                                                while idx < l:
                                                    if not i[idx].isdigit():
                                                        writeErrorBadVRCharNL_withNumber(
                                                            log, elem.tag, elem.VR,
                                                            vn, i, i[idx],
                                                            i[idx].encode(
                                                                default_encoding))
                                                        ok = False
                                                    idx += 1
                while idx < l:
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False
                    idx += 1
        else:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i, l,
                                    ">= 2 and <= 26")
            ok = False
        out = StringCheck(i.encode(default_encoding))

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False

    return ok


def validateVR_DS(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok

    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        if type(i) == DSfloat or type(i) == DSdecimal:
            i = i.original_string
        if len(i) > 16:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 16")
            ok = False
        encoded = i.encode(default_encoding)
        if not isnumber(i):
            writeErrorBadVRValue(log, elem.tag, elem.VR, vn, i)
            ok = False
        out = StringCheck(encoded)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def validateVR_IS(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]

    for i, vn in zip(val, range(0, len(val))):
        if type(i) == IS:
            i = i.original_string
        if len(i) > 12:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 12")
            ok = False
        if not isinteger(i):
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, vn, i,
                                  ' '.incode(default_encoding))
            ok = False

            if abs(int(i)) > 2147483647:
                writeErrorBadVRRange(log, elem.tag, elem.VR, vn, i,
                                     len(i),
                                     "-(2^31-1) <= n <= (2^31-1)")
                ok = False
        out = StringCheck(i.encode(default_encoding))

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def iscntrlok(c: chr):  # Per PS 3.5 6.1.3
    return c == 0x1b or c == 0x0a or c == 0x0c or c == 0x0d


def isescape(c: chr):  # Per PS 3.5 6.1.3
    return c == 0x1b


def validateVR_LO(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        if l > 64:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 64")
            ok = False
        i = pydicom.charset.encode_string(i, SpecificCharacterSetInfo)
        idces = isValidText(i, SpecificCharacterSetInfo)
        if len(idces) != 0:
            writeErrorBadCharacterRepertoireCharNL(
                log, elem.tag, elem.VR, vn, i, i[idces[0]])
        for idx in range(0, l):
            if (curses.ascii.iscntrl(i[idx]) and
                isescape(i[idx])) or \
                    i[idx] == '\\':
                writeErrorBadVRCharNL_withNumber(log, elem.tag, elem.VR, vn,
                                                 i[idx], [i[idx]])
                ok = False
        out = StringCheck(i)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0)
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0)
            ok = False

    return ok


def validateVR_PN(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        if type(i) == PersonName or type(i) == PersonName3 or \
                type(i) == PersonNameUnicode:
            i = i.original_string
            decoded = pydicom.charset.decode_string(i, SpecificCharacterSetInfo,
                                                    [])
        l = len(i)
        if l == 0:
            continue
        if l > 64:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 64")
            ok = False

        idces = isValidText(i, SpecificCharacterSetInfo)
        if len(idces) != 0:
            writeErrorBadCharacterRepertoireCharNL(
                log, elem.tag, elem.VR, vn, i, i[idces[0]])

        caretsTotal = int(0)
        caretsInGroup = int(0)
        equals = int(0)
        for idx in range(0, l):
            if (curses.ascii.iscntrl(i[idx]) and not curses.ascii.isescape(
                    i[idx])) \
                    or i[idx] == '\\' or (
                    curses.ascii.isspace(i[idx]) and decoded[idx] != ' '):
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, decoded,
                    decoded[idx],
                    bytes(i[idx]))
                ok = False
            elif i[idx] == '^':
                caretsTotal += 1
                caretsInGroup += 1
            elif i[idx] == '=':
                if caretsInGroup > 4:
                    writeErrorBadVRValue(
                        log, elem.tag, elem.VR, vn)
                    log[-1] += MMsgDC("TooManyComponentDelimitersInPersonName")
                    ok = False
                caretsInGroup = int(0)
                equals += 1
        if caretsTotal == 0:
            writeWarningVRValue(log, elem.tag, elem.VR, vn, i)
            log[-1] += MMsgDC("RetiredPersonNameForm")

        elif caretsInGroup > 4:
            writeErrorBadVRValue(log, elem.tag, elem.VR, vn, i)
            log[-1] += MMsgDC("TooManyComponentDelimitersInPersonName")
            ok = False

        if equals > 2:
            log[-1] += MMsgDC("TooManyComponentGroupDelimitersInPersonName")

        out = StringCheck(i)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def validateVR_LT(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        if l > 10240:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 10240")
            ok = False
        encoded = i.encode(default_encoding)
        idces = isValidText(i, SpecificCharacterSetInfo)
        if len(idces) != 0:
            if idces[0] == -1 and idces[1] == -1:
                enc_char = bytes(0)
                char = 'Bad Esc Char'
            else:
                enc_char = bytes(encoded[idces[0]])
                char = i[idces[0]]

            writeErrorBadCharacterRepertoireCharNL(
                log, elem.tag, elem.VR, vn, i, char, enc_char)
        for idx in range(0, l):
            if curses.ascii.iscntrl(encoded[idx]) and not iscntrlok(
                    encoded[idx]):
                writeErrorBadVRCharNL(log, elem.tag, elem.VR, vn, i[idx],
                                      i[idx].encode(
                                          SpecificCharacterSetInfo))
                ok = False
        out = StringCheck(encoded)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False

    return ok


def validateVR_SH(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        if l > 16:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 16")
            ok = False
        encoded = pydicom.charset.encode_string(
            i, SpecificCharacterSetInfo)
        idces = isValidText(encoded, SpecificCharacterSetInfo)
        if len(idces) != 0:
            if idces[0] == -1 and idces[1] == -1:
                enc_char = bytes(0)
                char = 'Bad Esc Char'
            else:
                enc_char = bytes(encoded[idces[0]])
                char = i[idces[0]]

            writeErrorBadCharacterRepertoireCharNL(
                log, elem.tag, elem.VR, vn, i, char, enc_char)
        for idx in range(0, l):
            if (curses.ascii.iscntrl(encoded[idx]) and
                isescape(encoded[idx])) or \
                    i[idx] == '\\':
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, i[idx],
                    pydicom.charset.encode_string(
                        i[idx], SpecificCharacterSetInfo))
                ok = False
        out = StringCheck(encoded)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok




def validateVR_TM(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        if type(i) == time:
            i = i.original_string
        if l >= 2 or l <= 16:
            idx = 0
            if i[idx] != '0' and i[idx] != '1' and i[idx] != '2':
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, i, i[idx],
                    i[idx].encode(default_encoding))
                ok = False
            idx += 1
            if not i[idx].isdigit():
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, i, i[idx],
                    i[idx].encode(default_encoding))
                ok = False
            idx += 1
            if idx < l:  # Not just HH
                if i[idx] == ':':
                    # CP 714 (000513)
                    writeErrorBadVRCharNL_withNumber(
                        log, elem.tag, elem.VR, vn, i, i[idx],
                        i[idx].encode(default_encoding))
                    ok = False
                    idx += 1
                if (i[idx] != '0' and i[idx] != '1' and i[idx] != '2' and
                        i[idx] != '3' and i[idx] != '4' and i[idx] != '5'):
                    writeErrorBadVRCharNL_withNumber(log, elem.tag, elem.VR, vn,
                                                     i, i[idx], i[idx].encode(
                            default_encoding))
                    ok = False
                idx += 1
                if idx < l:
                    if not i[idx].isdigit():
                        writeErrorBadVRCharNL_withNumber(
                            log, elem.tag, elem.VR, vn, i, i[idx],
                            i[idx].encode(default_encoding))
                        ok = False
                    idx += 1
                if idx < l:  # Not just HHMM
                    if i[idx] == ':':
                        # CP 714 (000513)
                        writeErrorBadVRCharNL_withNumber(
                            log, elem.tag, elem.VR, vn, i, i[idx],
                            i[idx].encode(default_encoding))
                        ok = False
                        idx += 1
                    if idx < l:
                        if (i[idx] != '0' and i[idx] != '1' and i[idx] != '2' and
                                i[idx] != '3' and i[idx] != '4' and
                                i[idx] != '5'):
                            writeErrorBadVRCharNL_withNumber(
                                log, elem.tag, elem.VR, vn, i, i[idx],
                                i[idx].encode(default_encoding))
                            ok = False
                        idx += 1

                    if idx < l:
                        if not i[idx].isdigit():
                            writeErrorBadVRCharNL_withNumber(
                                log, elem.tag, elem.VR, vn, i, i[idx],
                                i[idx].encode(default_encoding))
                            ok = False
                        idx += 1
                    if idx < l:
                        if i[idx] == '.':  # .FFFFFF
                            idx += 1
                            while idx < l:
                                if not i[idx].isdigit():
                                    writeErrorBadVRCharNL_withNumber(
                                        log, elem.tag, elem.VR, vn, i, i[idx],
                                        i[idx].encode(
                                            default_encoding))
                                    ok = False
                                idx += 1
                    while idx < l:
                        writeErrorBadVRCharNL_withNumber(
                            log, elem.tag, elem.VR, vn, i, i[idx],
                            i[idx].encode(default_encoding))
                        ok = False
                        idx += 1
        else:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i, l,
                                    ">= 2 and <= 16")
            ok = False
        out = StringCheck(i.encode(default_encoding))

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def validateVR_UI(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        if l > 64:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 64")
            ok = False
        idx = 0
        componentlength = int(0)
        countleadingzeroes = int(0)
        foundnonzerodigitsincomponent = False
        nothingbutzeroesinallcomponents = True
        while idx < l:
            if not i[idx].isdigit() and i[idx] != '.':
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, i, i[idx],
                    i[idx].encode(default_encoding))
                ok = False
            if i[idx] == '0':
                if not foundnonzerodigitsincomponent:
                    countleadingzeroes += 1
            else:
                if i[idx].isdigit():
                    foundnonzerodigitsincomponent = True
                if i[idx] != '.':
                    nothingbutzeroesinallcomponents = False
            componentlength = 0 if i[idx] == '.' else componentlength + 1
            idx += 1
            if (idx < l and i[idx] == '.') or idx >= l:
                if componentlength == 0:
                    writeErrorBadVRValue(log, elem.tag, elem.VR, vn, i)
                    log[-1] += MMsgDC("EmptyComponent")
                    ok = False
                elif (foundnonzerodigitsincomponent and countleadingzeroes > 0) \
                        or (not foundnonzerodigitsincomponent and
                            countleadingzeroes > 1):
                    writeErrorBadVRValue(log, elem.tag, elem.VR, vn, i)
                    log[-1] += MMsgDC("LeadingZeroes")
                    ok = False
                countleadingzeroes = int(0)
                foundnonzerodigitsincomponent = False
        if nothingbutzeroesinallcomponents:
            writeErrorBadVRValue(log, elem.tag, elem.VR, vn, i)
            log[-1] += MMsgDC("NothingButZeroComponents")

            ok = False
        out = StringCheck(i.encode(default_encoding))

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def validateVR_UR(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        if l > 1024:
            writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
                                    len(i), "<= 1024")
            ok = False
        encoded = i.encode(default_encoding)
        idces = isValidText(i, SpecificCharacterSetInfo)
        if len(idces) != 0:
            if idces[0] == -1 and idces[1] == -1:
                enc_char = bytes(0)
                char = 'Bad Esc Char'
            else:
                enc_char = bytes(encoded[idces[0]])
                char = i[idces[0]]

            writeErrorBadCharacterRepertoireCharNL(
                log, elem.tag, elem.VR, vn, i, char, enc_char)
        for idx in range(0, l):
            # pct-encoded = "%" HEXDIG HEXDIG reserved    = gen-delims /
            # sub-delims gen-delims  = ":" / "/" / "?" / "#" / "[" / "]" /
            # "@" sub-delims  = "!" / "$" / "&" / "'" / "(" / ")" / "*" / "+"
            # / "," / ";" / "=" unreserved  = ALPHA / DIGIT / "-" / "." / "_"
            # / "~"
            if not i[idx].isalnum() and i[idx] != ':' and i[idx] != '/' and i[
                idx] != '?' and i[idx] != '#' and i[idx] != '[' and i[
                idx] != ']' and i[idx] != '@' and i[idx] != '!' and i[
                idx] != '$' and i[idx] != '&' and i[idx] != '\'' and i[
                idx] != '(' and i[idx] != ')' and i[idx] != '*' and i[
                idx] != '+' and i[idx] != ',' and i[idx] != ';' and i[
                idx] != '=' and i[idx] != '-' and i[idx] != '.' and i[
                idx] != '_' and i[idx] != '~' and i[idx] != '%':
                writeErrorBadVRCharNL_withNumber(
                    log, elem.tag, elem.VR, vn, i, i[idx],
                    i[idx].encode(default_encoding))
                ok = False
        out = StringCheck(encoded)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


def validateVR_UC(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        encoded = i.encode(default_encoding)
        idces = isValidText(i, SpecificCharacterSetInfo)
        if len(idces) != 0:
            if idces[0] == -1 and idces[1] == -1:
                enc_char = bytes(0)
                char = 'Bad Esc Char'
            else:
                enc_char = bytes(encoded[idces[0]])
                char = i[idces[0]]

            writeErrorBadCharacterRepertoireCharNL(
                log, elem.tag, elem.VR, vn, i, char, enc_char)
        for idx in range(0, l):
            if (curses.ascii.iscntrl(encoded[idx]) and
                isescape(encoded[idx])) or \
                    i[idx] == '\\':
                writeErrorBadVRCharNL_withNumber(log, elem.tag, elem.VR, vn,
                                                 i[idx], i[idx].encode(
                        SpecificCharacterSetInfo))
                ok = False
        out = StringCheck(encoded)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok
# def validateVR_LT(elem: DataElement,
#                   log: list, SpecificCharacterSetInfo) -> bool:
#     ok = True
#     if elem.value is None:
#         return ok
#     if type(elem.value) == MultiValue:
#         val = elem.value
#     else:
#         val = [elem.value]
#     for i, vn in zip(val, range(0, len(val))):
#         l = len(i)
#         if l == 0:
#             continue
#         if l > 1024:
#             writeErrorBadVRLengthNL(log, elem.tag, elem.VR, vn, i,
#                                     len(i), "<= 1024")
#             ok = False
#         encoded = i.encode(default_encoding)
#         idces = isValidText(i, SpecificCharacterSetInfo)
#         if len(idces) != 0:
#             if idces[0] == -1 and idces[1] == -1:
#                 enc_char = bytes(0)
#                 char = 'Bad Esc Char'
#             else:
#                 enc_char = bytes(encoded[idces[0]])
#                 char = i[idces[0]]
#
#             writeErrorBadCharacterRepertoireCharNL(
#                 log, elem.tag, elem.VR, vn, i, char, enc_char)
#         for idx in range(0, l):
#             if curses.ascii.iscntrl(encoded[idx]) and not iscntrlok(
#                     encoded[idx]):
#                 writeErrorBadVRCharNL(log, elem.tag, elem.VR, vn, i[idx],
#                                       i[idx].encode(
#                                           SpecificCharacterSetInfo))
#                 ok = False
#         out = StringCheck(encoded)
#
#         if out["EmbededNullBytes"]:  # set during StringAttribute::read()
#             writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
#             ok = False
#
#         if out["TrailingNullBytes"]:  # set during StringAttribute::read()
#             writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
#             ok = False
#     return ok
#

def validateVR_LT(elem: DataElement,
                  log: list, SpecificCharacterSetInfo) -> bool:
    #www
    ok = True
    if elem.value is None:
        return ok
    if type(elem.value) == MultiValue:
        val = elem.value
    else:
        val = [elem.value]
    for i, vn in zip(val, range(0, len(val))):
        l = len(i)
        if l == 0:
            continue
        encoded = i.encode(default_encoding)
        idces = isValidText(encoded, SpecificCharacterSetInfo)
        if len(idces) != 0:
            if idces[0] == -1 and idces[1] == -1:
                enc_char = bytes(0)
                char = 'Bad Esc Char'
            else:
                enc_char = bytes(encoded[idces[0]])
                char = i[idces[0]]

            writeErrorBadCharacterRepertoireCharNL(
                log, elem.tag, elem.VR, vn, i, char, enc_char)
        for idx in range(0, l):
            if curses.ascii.iscntrl(encoded[idx]) and not iscntrlok(
                    encoded[idx]):
                writeErrorBadVRCharNL(log, elem.tag, elem.VR, vn, i[idx],
                                      bytes(encoded[idx]))
                ok = False
        out = StringCheck(encoded)

        if out["EmbededNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
            ok = False

        if out["TrailingNullBytes"]:  # set during StringAttribute::read()
            writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
            ok = False
    return ok


# def validateVR_UN(elem: DataElement,
#                   log: list, SpecificCharacterSetInfo) -> bool:
#     print(elem)
#     ok = True
#     if elem.value is None:
#         return ok
#     if type(elem.value) == MultiValue:
#         val = elem.value
#     else:
#         val = [elem.value]
#     for i, vn in zip(val, range(0, len(val))):

#         out = StringCheck(i)

#         if out["EmbededNullBytes"]:  # set during StringAttribute::read()
#             writeErrorBadVRCharNL(log, elem.tag, elem.VR, 0, [0])
#             ok = False

#         if out["TrailingNullBytes"]:  # set during StringAttribute::read()
#             writeErrorBadTrailingChar(log, elem.tag, elem.VR, 0, [0])
#             ok = False

#     return ok

