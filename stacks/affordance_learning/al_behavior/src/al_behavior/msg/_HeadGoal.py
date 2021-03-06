"""autogenerated by genpy from al_behavior/HeadGoal.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class HeadGoal(genpy.Message):
  _md5sum = "0c855908049a7db3cdc96aae847fa9ab"
  _type = "al_behavior/HeadGoal"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#goal definition
geometry_msgs/Point goalPositon

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

"""
  __slots__ = ['goalPositon']
  _slot_types = ['geometry_msgs/Point']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       goalPositon

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HeadGoal, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.goalPositon is None:
        self.goalPositon = geometry_msgs.msg.Point()
    else:
      self.goalPositon = geometry_msgs.msg.Point()

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
      buff.write(_struct_3d.pack(_x.goalPositon.x, _x.goalPositon.y, _x.goalPositon.z))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.goalPositon is None:
        self.goalPositon = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 24
      (_x.goalPositon.x, _x.goalPositon.y, _x.goalPositon.z,) = _struct_3d.unpack(str[start:end])
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
      buff.write(_struct_3d.pack(_x.goalPositon.x, _x.goalPositon.y, _x.goalPositon.z))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.goalPositon is None:
        self.goalPositon = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 24
      (_x.goalPositon.x, _x.goalPositon.y, _x.goalPositon.z,) = _struct_3d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3d = struct.Struct("<3d")
