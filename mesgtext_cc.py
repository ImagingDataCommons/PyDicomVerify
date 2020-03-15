from mesgtext_h import EMSGDC_Table
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








