"""autogenerated by genpy from al_msgs/Spec.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Spec(genpy.Message):
  _md5sum = "502e5954260a48221b6c746f55599d9c"
  _type = "al_msgs/Spec"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int8 MAX_SPEC_INDEX=7

int8 THIN=0
int8 THICK=1
int8 ROUND=2
int8 EDGY=3
int8 TALL=4
int8 SHORT=5
int8 BIG=6
int8 SMALL=7
int8 spec
float32 prob

"""
  # Pseudo-constants
  MAX_SPEC_INDEX = 7
  THIN = 0
  THICK = 1
  ROUND = 2
  EDGY = 3
  TALL = 4
  SHORT = 5
  BIG = 6
  SMALL = 7

  __slots__ = ['spec','prob']
  _slot_types = ['int8','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       spec,prob

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Spec, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.spec is None:
        self.spec = 0
      if self.prob is None:
        self.prob = 0.
    else:
      self.spec = 0
      self.prob = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_bf.pack(_x.spec, _x.prob))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.spec, _x.prob,) = _struct_bf.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_bf.pack(_x.spec, _x.prob))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.spec, _x.prob,) = _struct_bf.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_bf = struct.Struct("<bf")
