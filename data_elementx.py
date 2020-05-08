import pydicom
import pydicom.dataelem
from collections import namedtuple
class DataElementX(pydicom.DataElement):
    _used_in_verification:bool
    def __init__(self, tag, VR, value, file_value_tell=None,
     is_undefined_length=False, already_converted=True,used=False):
        super().__init__(tag, VR, value, file_value_tell,
     is_undefined_length, already_converted) 
        self._used_in_verification = used
    @property
    def used_in_verification(self)->bool:
        return self._used_in_verification
    @used_in_verification.setter
    def used_in_verification(self, val:bool)->bool:
        if type(val) != bool:
            return
        self._used_in_verification=val

def ConvertDataset(ds:pydicom.Dataset)->pydicom.Dataset:
    msg = 'tag VR length value value_tell is_implicit_VR is_little_endian used_in_verification'
    MyRawDataElement = namedtuple('MyRawDataElement', msg)
    if type(ds) == pydicom.dataset.FileDataset:
        ds.file_meta = ConvertDataset(ds.file_meta)
    already_coverted = False
    for key, val in ds.items():
        try:
            elem = ds[key]
            already_coverted = True
        except KeyError:
            elem = val
            already_coverted = False
        
        if type(elem.value) == pydicom.Sequence:
            new_seq_elem = DataElementX(elem.tag, elem.VR, pydicom.Sequence())
            for item in elem.value:
                new_seq_elem.value.append(ConvertDataset(item))
            ds[key] = new_seq_elem 
        elif type(elem.value) == pydicom.Dataset:
            ds_elem = DataElementX(elem.tag, elem.VR, pydicom.Dataset())
            ds_elem = ConvertDataset(elem.value)
            ds[key] = ds_elem
        else:
            if type(elem) == pydicom.dataelem.RawDataElement:
                new_elem = MyRawDataElement(elem.tag, elem.VR, elem.lenght, elem.value,
                elem.value_tell, elem.is_implicit_VR, elem.is_little_endian, False)
                ds[key] = new_elem
            elif type(elem) == pydicom.DataElement:
                new_elem = DataElementX(elem.tag,elem.VR, elem.value,already_converted=already_coverted)
                ds[key] = new_elem
    return ds
    
