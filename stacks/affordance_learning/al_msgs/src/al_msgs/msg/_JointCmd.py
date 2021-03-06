"""autogenerated by genpy from al_msgs/JointCmd.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class JointCmd(genpy.Message):
  _md5sum = "b2a85fe70feb7b1c690f154e093b79e0"
  _type = "al_msgs/JointCmd"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 joint_id
float64 joint_val

"""
  __slots__ = ['joint_id','joint_val']
  _slot_types = ['uint8','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       joint_id,joint_val

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(JointCmd, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.joint_id is None:
        self.joint_id = 0
      if self.joint_val is None:
        self.joint_val = 0.
    else:
      self.joint_id = 0
      self.joint_val = 0.

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
      buff.write(_struct_Bd.pack(_x.joint_id, _x.joint_val))
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
      end += 9
      (_x.joint_id, _x.joint_val,) = _struct_Bd.unpack(str[start:end])
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
      buff.write(_struct_Bd.pack(_x.joint_id, _x.joint_val))
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
      end += 9
      (_x.joint_id, _x.joint_val,) = _struct_Bd.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_Bd = struct.Struct("<Bd")
