from mesgtext_h import EMSGDC_Table
from enum import Enum
import sys
fixmsg = "{error} :->: {fix} <function {}>"
class ErrorInfo:
    def __init__(self,m = '', f = ''):
        self.msg = m
        self.fix = f
    
    msg:str
    fix:str
    
    def getWholeMessage(self)->str:
        fixmsg = "{} :->: {} <function {} from file:{}> <function {} from file:{}>"
        function = sys._getframe(1).f_code.co_name
        filename = sys._getframe(1).f_code.co_filename
        function1 = sys._getframe(2).f_code.co_name
        filename1 = sys._getframe(2).f_code.co_filename
        fixmsg = fixmsg.format(self.msg,self.fix,function,
         filename, function1, filename1)
        return fixmsg





class ErrorType(Enum):
    Type1 = "Type1 Absent"
    Type1Empty = "Type1 Empty"
    Type1CPresent = "Type1C Present"
    Type1CAbsent = "Type1C Absent"
    Type1CRequiredEmpty = "Type1C Required Empty"
    Type1CRedundantEmpty = "Type1C Redundant Empty"
    Type2 = "Type2 Absent"
    Type2CPresent = "Type2C Present"
    Type2CAbsent = "Type2C Absent"
    Type1VR = "Type1 VR"
    Type1VM = "Type1 VM"
    Type2VR = "Type2 VR"
    Type2VM = "Type2 VM"
    Type3VR = "Type3 VR"
    Type3VM = "Type3 VM"
    Type1CVR = "Type1C VR"
    Type1CVM = "Type1C VM"
    Type2CVR = "Type2C VR"
    Type2CVM = "Type2C VM"
    Type3CVR = "Type3C VR"
    Type3CVM = "Type3C VM"
    VR = "VR"
    VM = "VM"
    EnumStr = "Enumerated String"
    BadValue = "Bad Value"
    Required = "Required Absent"
    RequiredEmpty = "Required Empty"
    RequiredVR = "RequiredVR"
    RequiredVM = "RequiredVM"
def EMsgDC(key_:str)->str:
    try:
        modifier = EMSGDC_Table["Error"]
        msg = EMSGDC_Table[key_]
    except:
        modifier = ""
        msg = "message table doesn't have the key <{}>".format(key_)
    return "{} - {}".format(modifier, msg)

def WMsgDC(key_:str)->str:
    try:
        modifier = EMSGDC_Table["Warning"]
        msg = EMSGDC_Table[key_]
    except:
        msg = "message table doesn't have the key <{}>".format(key_)
    return "{} - {}".format(modifier, msg)

def AMsgDC(key_:str)->str:
    try:
        modifier = EMSGDC_Table["Abort"]
        msg = EMSGDC_Table[key_]
    except:
        modifier = ""
        msg = "message table doesn't have the key <{}>".format(key_)
    return "{} - {}".format(modifier, msg)

def MMsgDC(key_:str)->str:
    try:
        msg = EMSGDC_Table[key_]
    except:
        msg = "message table doesn't have the key <{}>".format(key_)
    return "{}".format(msg)

