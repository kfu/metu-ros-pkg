"""autogenerated by genpy from al_msgs/Entities.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import arm_navigation_msgs.msg
import geometry_msgs.msg
import al_msgs.msg
import sensor_msgs.msg
import genpy
import std_msgs.msg

class Entities(genpy.Message):
  _md5sum = "85dd43f20f56dcd78caf1db583535320"
  _type = "al_msgs/Entities"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
al_msgs/Entity[] entities

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: al_msgs/Entity
arm_navigation_msgs/CollisionObject collision_object
sensor_msgs/PointCloud2 cloud_object
al_msgs/FeatureVector feature_vector

================================================================================
MSG: arm_navigation_msgs/CollisionObject
# a header, used for interpreting the poses
Header header

# the id of the object
string id

# The padding used for filtering points near the object.
# This does not affect collision checking for the object.  
# Set to negative to get zero padding.
float32 padding

#This contains what is to be done with the object
CollisionObjectOperation operation

#the shapes associated with the object
arm_navigation_msgs/Shape[] shapes

#the poses associated with the shapes - will be transformed using the header
geometry_msgs/Pose[] poses

================================================================================
MSG: arm_navigation_msgs/CollisionObjectOperation
#Puts the object into the environment
#or updates the object if already added
byte ADD=0

#Removes the object from the environment entirely
byte REMOVE=1

#Only valid within the context of a CollisionAttachedObject message
#Will be ignored if sent with an CollisionObject message
#Takes an attached object, detaches from the attached link
#But adds back in as regular object
byte DETACH_AND_ADD_AS_OBJECT=2

#Only valid within the context of a CollisionAttachedObject message
#Will be ignored if sent with an CollisionObject message
#Takes current object in the environment and removes it as
#a regular object
byte ATTACH_AND_REMOVE_AS_OBJECT=3

# Byte code for operation
byte operation

================================================================================
MSG: arm_navigation_msgs/Shape
byte SPHERE=0
byte BOX=1
byte CYLINDER=2
byte MESH=3

byte type


#### define sphere, box, cylinder ####
# the origin of each shape is considered at the shape's center

# for sphere
# radius := dimensions[0]

# for cylinder
# radius := dimensions[0]
# length := dimensions[1]
# the length is along the Z axis

# for box
# size_x := dimensions[0]
# size_y := dimensions[1]
# size_z := dimensions[2]
float64[] dimensions


#### define mesh ####

# list of triangles; triangle k is defined by tre vertices located
# at indices triangles[3k], triangles[3k+1], triangles[3k+2]
int32[] triangles
geometry_msgs/Point[] vertices

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: sensor_msgs/PointCloud2
# This message holds a collection of N-dimensional points, which may
# contain additional information such as normals, intensity, etc. The
# point data is stored as a binary blob, its layout described by the
# contents of the "fields" array.

# The point cloud data may be organized 2d (image-like) or 1d
# (unordered). Point clouds organized as 2d images may be produced by
# camera depth sensors such as stereo or time-of-flight.

# Time of sensor data acquisition, and the coordinate frame ID (for 3d
# points).
Header header

# 2D structure of the point cloud. If the cloud is unordered, height is
# 1 and width is the length of the point cloud.
uint32 height
uint32 width

# Describes the channels and their layout in the binary data blob.
PointField[] fields

bool    is_bigendian # Is this data bigendian?
uint32  point_step   # Length of a point in bytes
uint32  row_step     # Length of a row in bytes
uint8[] data         # Actual point data, size is (row_step*height)

bool is_dense        # True if there are no invalid points

================================================================================
MSG: sensor_msgs/PointField
# This message holds the description of one point entry in the
# PointCloud2 message format.
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 INT32   = 5
uint8 UINT32  = 6
uint8 FLOAT32 = 7
uint8 FLOAT64 = 8

string name      # Name of field
uint32 offset    # Offset from start of point struct
uint8  datatype  # Datatype enumeration, see above
uint32 count     # How many elements in the field

================================================================================
MSG: al_msgs/FeatureVector
al_msgs/Feature[] features

================================================================================
MSG: al_msgs/Feature
float32 min # min value
float32 max # max value
float32 avg # average value
float32 var # variance
float32 dev # standard deviation
float32[] his # histogram
std_msgs/Time stamp # time stamp when this feature is calculated
float32 range_min # min value that this feature can get
float32 range_max # max value that this feature can get
int16 n_hist_bins # number of bins in its histogram
string NORMAL_AZI=NormalAzimuth
string NORMAL_ZEN=NormalZenith
string CURV_MIN=MinCurvature
string CURV_MAX=MaxCurvature
string CURV_MEAN=MeanCurvature
string CURV_GAUSS=GaussCurvature
string SHAPE_INDEX=ShapeIndex
string R_COLOR=RedColor
string G_COLOR=GreenColor
string B_COLOR=BlueColor
string POS_X=PositionX
string POS_Y=PositionY
string POS_Z=PositionZ
string ROT_T=RotationTheta
string DIM_X=DimensionX
string DIM_Y=DimensionY
string DIM_Z=DimensionZ
string OBJECT_PRESENCE=ObjectPresence
string HUMAN_TORSO_X=HumanTorsoX
string HUMAN_TORSO_Y=HumanTorsoY
string HUMAN_TORSO_Z=HumanTorsoZ
string HUMAN_TORSO_ROLL=HumanTorsoRoll
string HUMAN_TORSO_PITCH=HumanTorsoPitch
string HUMAN_TORSO_YAW=HumanTorsoYaw
string HUMAN_HEAD_ROLL=HumanHeadRoll
string HUMAN_HEAD_PITCH=HumanHeadPitch
string HUMAN_HEAD_YAW=HumanHeadYaw
string HUMAN_PRESENCE=HumanPresence
string AFFORDANCE_ACC=AffordanceAccuracy
string type
string DISPERSIVE_VALUED=DispersiveValued
string SINGLE_VALUED=SingleValued
string val_type


================================================================================
MSG: std_msgs/Time
time data

"""
  __slots__ = ['header','entities']
  _slot_types = ['std_msgs/Header','al_msgs/Entity[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,entities

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Entities, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.entities is None:
        self.entities = []
    else:
      self.header = std_msgs.msg.Header()
      self.entities = []

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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.entities)
      buff.write(_struct_I.pack(length))
      for val1 in self.entities:
        _v1 = val1.collision_object
        _v2 = _v1.header
        buff.write(_struct_I.pack(_v2.seq))
        _v3 = _v2.stamp
        _x = _v3
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v2.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v1.id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_f.pack(_v1.padding))
        _v4 = _v1.operation
        buff.write(_struct_b.pack(_v4.operation))
        length = len(_v1.shapes)
        buff.write(_struct_I.pack(length))
        for val3 in _v1.shapes:
          buff.write(_struct_b.pack(val3.type))
          length = len(val3.dimensions)
          buff.write(_struct_I.pack(length))
          pattern = '<%sd'%length
          buff.write(struct.pack(pattern, *val3.dimensions))
          length = len(val3.triangles)
          buff.write(_struct_I.pack(length))
          pattern = '<%si'%length
          buff.write(struct.pack(pattern, *val3.triangles))
          length = len(val3.vertices)
          buff.write(_struct_I.pack(length))
          for val4 in val3.vertices:
            _x = val4
            buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        length = len(_v1.poses)
        buff.write(_struct_I.pack(length))
        for val3 in _v1.poses:
          _v5 = val3.position
          _x = _v5
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v6 = val3.orientation
          _x = _v6
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _v7 = val1.cloud_object
        _v8 = _v7.header
        buff.write(_struct_I.pack(_v8.seq))
        _v9 = _v8.stamp
        _x = _v9
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v8.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v7
        buff.write(_struct_2I.pack(_x.height, _x.width))
        length = len(_v7.fields)
        buff.write(_struct_I.pack(length))
        for val3 in _v7.fields:
          _x = val3.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3
          buff.write(_struct_IBI.pack(_x.offset, _x.datatype, _x.count))
        _x = _v7
        buff.write(_struct_B2I.pack(_x.is_bigendian, _x.point_step, _x.row_step))
        _x = _v7.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_B.pack(_v7.is_dense))
        _v10 = val1.feature_vector
        length = len(_v10.features)
        buff.write(_struct_I.pack(length))
        for val3 in _v10.features:
          _x = val3
          buff.write(_struct_5f.pack(_x.min, _x.max, _x.avg, _x.var, _x.dev))
          length = len(val3.his)
          buff.write(_struct_I.pack(length))
          pattern = '<%sf'%length
          buff.write(struct.pack(pattern, *val3.his))
          _v11 = val3.stamp
          _v12 = _v11.data
          _x = _v12
          buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
          _x = val3
          buff.write(_struct_2fh.pack(_x.range_min, _x.range_max, _x.n_hist_bins))
          _x = val3.type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3.val_type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.entities is None:
        self.entities = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.entities = []
      for i in range(0, length):
        val1 = al_msgs.msg.Entity()
        _v13 = val1.collision_object
        _v14 = _v13.header
        start = end
        end += 4
        (_v14.seq,) = _struct_I.unpack(str[start:end])
        _v15 = _v14.stamp
        _x = _v15
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v14.frame_id = str[start:end].decode('utf-8')
        else:
          _v14.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v13.id = str[start:end].decode('utf-8')
        else:
          _v13.id = str[start:end]
        start = end
        end += 4
        (_v13.padding,) = _struct_f.unpack(str[start:end])
        _v16 = _v13.operation
        start = end
        end += 1
        (_v16.operation,) = _struct_b.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v13.shapes = []
        for i in range(0, length):
          val3 = arm_navigation_msgs.msg.Shape()
          start = end
          end += 1
          (val3.type,) = _struct_b.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sd'%length
          start = end
          end += struct.calcsize(pattern)
          val3.dimensions = struct.unpack(pattern, str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%si'%length
          start = end
          end += struct.calcsize(pattern)
          val3.triangles = struct.unpack(pattern, str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val3.vertices = []
          for i in range(0, length):
            val4 = geometry_msgs.msg.Point()
            _x = val4
            start = end
            end += 24
            (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
            val3.vertices.append(val4)
          _v13.shapes.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v13.poses = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Pose()
          _v17 = val3.position
          _x = _v17
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v18 = val3.orientation
          _x = _v18
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          _v13.poses.append(val3)
        _v19 = val1.cloud_object
        _v20 = _v19.header
        start = end
        end += 4
        (_v20.seq,) = _struct_I.unpack(str[start:end])
        _v21 = _v20.stamp
        _x = _v21
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v20.frame_id = str[start:end].decode('utf-8')
        else:
          _v20.frame_id = str[start:end]
        _x = _v19
        start = end
        end += 8
        (_x.height, _x.width,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v19.fields = []
        for i in range(0, length):
          val3 = sensor_msgs.msg.PointField()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.name = str[start:end].decode('utf-8')
          else:
            val3.name = str[start:end]
          _x = val3
          start = end
          end += 9
          (_x.offset, _x.datatype, _x.count,) = _struct_IBI.unpack(str[start:end])
          _v19.fields.append(val3)
        _x = _v19
        start = end
        end += 9
        (_x.is_bigendian, _x.point_step, _x.row_step,) = _struct_B2I.unpack(str[start:end])
        _v19.is_bigendian = bool(_v19.is_bigendian)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v19.data = str[start:end].decode('utf-8')
        else:
          _v19.data = str[start:end]
        start = end
        end += 1
        (_v19.is_dense,) = _struct_B.unpack(str[start:end])
        _v19.is_dense = bool(_v19.is_dense)
        _v22 = val1.feature_vector
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v22.features = []
        for i in range(0, length):
          val3 = al_msgs.msg.Feature()
          _x = val3
          start = end
          end += 20
          (_x.min, _x.max, _x.avg, _x.var, _x.dev,) = _struct_5f.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sf'%length
          start = end
          end += struct.calcsize(pattern)
          val3.his = struct.unpack(pattern, str[start:end])
          _v23 = val3.stamp
          _v24 = _v23.data
          _x = _v24
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
          _x = val3
          start = end
          end += 10
          (_x.range_min, _x.range_max, _x.n_hist_bins,) = _struct_2fh.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.type = str[start:end].decode('utf-8')
          else:
            val3.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.val_type = str[start:end].decode('utf-8')
          else:
            val3.val_type = str[start:end]
          _v22.features.append(val3)
        self.entities.append(val1)
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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.entities)
      buff.write(_struct_I.pack(length))
      for val1 in self.entities:
        _v25 = val1.collision_object
        _v26 = _v25.header
        buff.write(_struct_I.pack(_v26.seq))
        _v27 = _v26.stamp
        _x = _v27
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v26.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v25.id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_f.pack(_v25.padding))
        _v28 = _v25.operation
        buff.write(_struct_b.pack(_v28.operation))
        length = len(_v25.shapes)
        buff.write(_struct_I.pack(length))
        for val3 in _v25.shapes:
          buff.write(_struct_b.pack(val3.type))
          length = len(val3.dimensions)
          buff.write(_struct_I.pack(length))
          pattern = '<%sd'%length
          buff.write(val3.dimensions.tostring())
          length = len(val3.triangles)
          buff.write(_struct_I.pack(length))
          pattern = '<%si'%length
          buff.write(val3.triangles.tostring())
          length = len(val3.vertices)
          buff.write(_struct_I.pack(length))
          for val4 in val3.vertices:
            _x = val4
            buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        length = len(_v25.poses)
        buff.write(_struct_I.pack(length))
        for val3 in _v25.poses:
          _v29 = val3.position
          _x = _v29
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v30 = val3.orientation
          _x = _v30
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _v31 = val1.cloud_object
        _v32 = _v31.header
        buff.write(_struct_I.pack(_v32.seq))
        _v33 = _v32.stamp
        _x = _v33
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v32.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v31
        buff.write(_struct_2I.pack(_x.height, _x.width))
        length = len(_v31.fields)
        buff.write(_struct_I.pack(length))
        for val3 in _v31.fields:
          _x = val3.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3
          buff.write(_struct_IBI.pack(_x.offset, _x.datatype, _x.count))
        _x = _v31
        buff.write(_struct_B2I.pack(_x.is_bigendian, _x.point_step, _x.row_step))
        _x = _v31.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.pack('<I%sB'%length, length, *_x))
        else:
          buff.write(struct.pack('<I%ss'%length, length, _x))
        buff.write(_struct_B.pack(_v31.is_dense))
        _v34 = val1.feature_vector
        length = len(_v34.features)
        buff.write(_struct_I.pack(length))
        for val3 in _v34.features:
          _x = val3
          buff.write(_struct_5f.pack(_x.min, _x.max, _x.avg, _x.var, _x.dev))
          length = len(val3.his)
          buff.write(_struct_I.pack(length))
          pattern = '<%sf'%length
          buff.write(val3.his.tostring())
          _v35 = val3.stamp
          _v36 = _v35.data
          _x = _v36
          buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
          _x = val3
          buff.write(_struct_2fh.pack(_x.range_min, _x.range_max, _x.n_hist_bins))
          _x = val3.type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val3.val_type
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.entities is None:
        self.entities = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.entities = []
      for i in range(0, length):
        val1 = al_msgs.msg.Entity()
        _v37 = val1.collision_object
        _v38 = _v37.header
        start = end
        end += 4
        (_v38.seq,) = _struct_I.unpack(str[start:end])
        _v39 = _v38.stamp
        _x = _v39
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v38.frame_id = str[start:end].decode('utf-8')
        else:
          _v38.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v37.id = str[start:end].decode('utf-8')
        else:
          _v37.id = str[start:end]
        start = end
        end += 4
        (_v37.padding,) = _struct_f.unpack(str[start:end])
        _v40 = _v37.operation
        start = end
        end += 1
        (_v40.operation,) = _struct_b.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v37.shapes = []
        for i in range(0, length):
          val3 = arm_navigation_msgs.msg.Shape()
          start = end
          end += 1
          (val3.type,) = _struct_b.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sd'%length
          start = end
          end += struct.calcsize(pattern)
          val3.dimensions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%si'%length
          start = end
          end += struct.calcsize(pattern)
          val3.triangles = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          val3.vertices = []
          for i in range(0, length):
            val4 = geometry_msgs.msg.Point()
            _x = val4
            start = end
            end += 24
            (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
            val3.vertices.append(val4)
          _v37.shapes.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v37.poses = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Pose()
          _v41 = val3.position
          _x = _v41
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v42 = val3.orientation
          _x = _v42
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          _v37.poses.append(val3)
        _v43 = val1.cloud_object
        _v44 = _v43.header
        start = end
        end += 4
        (_v44.seq,) = _struct_I.unpack(str[start:end])
        _v45 = _v44.stamp
        _x = _v45
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v44.frame_id = str[start:end].decode('utf-8')
        else:
          _v44.frame_id = str[start:end]
        _x = _v43
        start = end
        end += 8
        (_x.height, _x.width,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v43.fields = []
        for i in range(0, length):
          val3 = sensor_msgs.msg.PointField()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.name = str[start:end].decode('utf-8')
          else:
            val3.name = str[start:end]
          _x = val3
          start = end
          end += 9
          (_x.offset, _x.datatype, _x.count,) = _struct_IBI.unpack(str[start:end])
          _v43.fields.append(val3)
        _x = _v43
        start = end
        end += 9
        (_x.is_bigendian, _x.point_step, _x.row_step,) = _struct_B2I.unpack(str[start:end])
        _v43.is_bigendian = bool(_v43.is_bigendian)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v43.data = str[start:end].decode('utf-8')
        else:
          _v43.data = str[start:end]
        start = end
        end += 1
        (_v43.is_dense,) = _struct_B.unpack(str[start:end])
        _v43.is_dense = bool(_v43.is_dense)
        _v46 = val1.feature_vector
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v46.features = []
        for i in range(0, length):
          val3 = al_msgs.msg.Feature()
          _x = val3
          start = end
          end += 20
          (_x.min, _x.max, _x.avg, _x.var, _x.dev,) = _struct_5f.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sf'%length
          start = end
          end += struct.calcsize(pattern)
          val3.his = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
          _v47 = val3.stamp
          _v48 = _v47.data
          _x = _v48
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
          _x = val3
          start = end
          end += 10
          (_x.range_min, _x.range_max, _x.n_hist_bins,) = _struct_2fh.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.type = str[start:end].decode('utf-8')
          else:
            val3.type = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val3.val_type = str[start:end].decode('utf-8')
          else:
            val3.val_type = str[start:end]
          _v46.features.append(val3)
        self.entities.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_IBI = struct.Struct("<IBI")
_struct_b = struct.Struct("<b")
_struct_f = struct.Struct("<f")
_struct_2fh = struct.Struct("<2fh")
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_B2I = struct.Struct("<B2I")
_struct_4d = struct.Struct("<4d")
_struct_5f = struct.Struct("<5f")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")