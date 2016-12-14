"""autogenerated by genpy from tabletop_object_segmentation/TabletopDetectionResult.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import arm_navigation_msgs.msg
import geometry_msgs.msg
import sensor_msgs.msg
import std_msgs.msg
import tabletop_object_segmentation.msg
import household_objects_database_msgs.msg

class TabletopDetectionResult(genpy.Message):
  _md5sum = "026c0e5e13258b4a96f7d3999ea3cd64"
  _type = "tabletop_object_segmentation/TabletopDetectionResult"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Contains all the information from one run of the tabletop detection node

# The information for the plane that has been detected
Table table

# The raw clusters detected in the scan 
sensor_msgs/PointCloud[] clusters

# The list of potential models that have been detected for each cluster
# An empty list will be returned for a cluster that has no recognition results at all
household_objects_database_msgs/DatabaseModelPoseList[] models

# For each cluster, the index of the list of models that was fit to that cluster
# keep in mind that multiple raw clusters can correspond to a single fit
int32[] cluster_model_indices

# Whether the detection has succeeded or failed
int32 NO_CLOUD_RECEIVED = 1
int32 NO_TABLE = 2
int32 OTHER_ERROR = 3
int32 SUCCESS = 4
int32 result

================================================================================
MSG: tabletop_object_segmentation/Table
# Informs that a planar table has been detected at a given location

# The pose gives you the transform that take you to the coordinate system
# of the table, with the origin somewhere in the table plane and the 
# z axis normal to the plane
geometry_msgs/PoseStamped pose

# These values give you the observed extents of the table, along x and y,
# in the table's own coordinate system (above)
# there is no guarantee that the origin of the table coordinate system is
# inside the boundary defined by these values. 
float32 x_min
float32 x_max
float32 y_min
float32 y_max

# There is no guarantee that the table does NOT extend further than these 
# values; this is just as far as we've observed it.


# Newer table definition as triangle mesh of convex hull (relative to pose)
arm_navigation_msgs/Shape convex_hull

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

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
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

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
MSG: sensor_msgs/PointCloud
# This message holds a collection of 3d points, plus optional additional
# information about each point.

# Time of sensor data acquisition, coordinate frame ID.
Header header

# Array of 3d points. Each Point32 should be interpreted as a 3d point
# in the frame given in the header.
geometry_msgs/Point32[] points

# Each channel should have the same number of elements as points array,
# and the data in each channel should correspond 1:1 with each point.
# Channel names in common practice are listed in ChannelFloat32.msg.
ChannelFloat32[] channels

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
================================================================================
MSG: sensor_msgs/ChannelFloat32
# This message is used by the PointCloud message to hold optional data
# associated with each point in the cloud. The length of the values
# array should be the same as the length of the points array in the
# PointCloud, and each value should be associated with the corresponding
# point.

# Channel names in existing practice include:
#   "u", "v" - row and column (respectively) in the left stereo image.
#              This is opposite to usual conventions but remains for
#              historical reasons. The newer PointCloud2 message has no
#              such problem.
#   "rgb" - For point clouds produced by color stereo cameras. uint8
#           (R,G,B) values packed into the least significant 24 bits,
#           in order.
#   "intensity" - laser or pixel intensity.
#   "distance"

# The channel name should give semantics of the channel (e.g.
# "intensity" instead of "value").
string name

# The values array should be 1-1 with the elements of the associated
# PointCloud.
float32[] values

================================================================================
MSG: household_objects_database_msgs/DatabaseModelPoseList
# stores a list of possible database models recognition results
DatabaseModelPose[] model_list
================================================================================
MSG: household_objects_database_msgs/DatabaseModelPose
# Informs that a specific model from the Model Database has been 
# identified at a certain location

# the database id of the model
int32 model_id

# the pose that it can be found in
geometry_msgs/PoseStamped pose

# a measure of the confidence level in this detection result
float32 confidence

# the name of the object detector that generated this detection result
string detector_name

"""
  # Pseudo-constants
  NO_CLOUD_RECEIVED = 1
  NO_TABLE = 2
  OTHER_ERROR = 3
  SUCCESS = 4

  __slots__ = ['table','clusters','models','cluster_model_indices','result']
  _slot_types = ['tabletop_object_segmentation/Table','sensor_msgs/PointCloud[]','household_objects_database_msgs/DatabaseModelPoseList[]','int32[]','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       table,clusters,models,cluster_model_indices,result

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TabletopDetectionResult, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.table is None:
        self.table = tabletop_object_segmentation.msg.Table()
      if self.clusters is None:
        self.clusters = []
      if self.models is None:
        self.models = []
      if self.cluster_model_indices is None:
        self.cluster_model_indices = []
      if self.result is None:
        self.result = 0
    else:
      self.table = tabletop_object_segmentation.msg.Table()
      self.clusters = []
      self.models = []
      self.cluster_model_indices = []
      self.result = 0

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
      buff.write(_struct_3I.pack(_x.table.pose.header.seq, _x.table.pose.header.stamp.secs, _x.table.pose.header.stamp.nsecs))
      _x = self.table.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d4fb.pack(_x.table.pose.pose.position.x, _x.table.pose.pose.position.y, _x.table.pose.pose.position.z, _x.table.pose.pose.orientation.x, _x.table.pose.pose.orientation.y, _x.table.pose.pose.orientation.z, _x.table.pose.pose.orientation.w, _x.table.x_min, _x.table.x_max, _x.table.y_min, _x.table.y_max, _x.table.convex_hull.type))
      length = len(self.table.convex_hull.dimensions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.table.convex_hull.dimensions))
      length = len(self.table.convex_hull.triangles)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.table.convex_hull.triangles))
      length = len(self.table.convex_hull.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.table.convex_hull.vertices:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.clusters)
      buff.write(_struct_I.pack(length))
      for val1 in self.clusters:
        _v1 = val1.header
        buff.write(_struct_I.pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        for val2 in val1.points:
          _x = val2
          buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
        length = len(val1.channels)
        buff.write(_struct_I.pack(length))
        for val2 in val1.channels:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.values)
          buff.write(_struct_I.pack(length))
          pattern = '<%sf'%length
          buff.write(struct.pack(pattern, *val2.values))
      length = len(self.models)
      buff.write(_struct_I.pack(length))
      for val1 in self.models:
        length = len(val1.model_list)
        buff.write(_struct_I.pack(length))
        for val2 in val1.model_list:
          buff.write(_struct_i.pack(val2.model_id))
          _v3 = val2.pose
          _v4 = _v3.header
          buff.write(_struct_I.pack(_v4.seq))
          _v5 = _v4.stamp
          _x = _v5
          buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
          _x = _v4.frame_id
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _v6 = _v3.pose
          _v7 = _v6.position
          _x = _v7
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v8 = _v6.orientation
          _x = _v8
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
          buff.write(_struct_f.pack(val2.confidence))
          _x = val2.detector_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.cluster_model_indices)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.cluster_model_indices))
      buff.write(_struct_i.pack(self.result))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.table is None:
        self.table = tabletop_object_segmentation.msg.Table()
      if self.clusters is None:
        self.clusters = None
      if self.models is None:
        self.models = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.table.pose.header.seq, _x.table.pose.header.stamp.secs, _x.table.pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.table.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.table.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 73
      (_x.table.pose.pose.position.x, _x.table.pose.pose.position.y, _x.table.pose.pose.position.z, _x.table.pose.pose.orientation.x, _x.table.pose.pose.orientation.y, _x.table.pose.pose.orientation.z, _x.table.pose.pose.orientation.w, _x.table.x_min, _x.table.x_max, _x.table.y_min, _x.table.y_max, _x.table.convex_hull.type,) = _struct_7d4fb.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.table.convex_hull.dimensions = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.table.convex_hull.triangles = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.table.convex_hull.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.table.convex_hull.vertices.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.clusters = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointCloud()
        _v9 = val1.header
        start = end
        end += 4
        (_v9.seq,) = _struct_I.unpack(str[start:end])
        _v10 = _v9.stamp
        _x = _v10
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v9.frame_id = str[start:end].decode('utf-8')
        else:
          _v9.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.points = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point32()
          _x = val2
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
          val1.points.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.channels = []
        for i in range(0, length):
          val2 = sensor_msgs.msg.ChannelFloat32()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sf'%length
          start = end
          end += struct.calcsize(pattern)
          val2.values = struct.unpack(pattern, str[start:end])
          val1.channels.append(val2)
        self.clusters.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.models = []
      for i in range(0, length):
        val1 = household_objects_database_msgs.msg.DatabaseModelPoseList()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.model_list = []
        for i in range(0, length):
          val2 = household_objects_database_msgs.msg.DatabaseModelPose()
          start = end
          end += 4
          (val2.model_id,) = _struct_i.unpack(str[start:end])
          _v11 = val2.pose
          _v12 = _v11.header
          start = end
          end += 4
          (_v12.seq,) = _struct_I.unpack(str[start:end])
          _v13 = _v12.stamp
          _x = _v13
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v12.frame_id = str[start:end].decode('utf-8')
          else:
            _v12.frame_id = str[start:end]
          _v14 = _v11.pose
          _v15 = _v14.position
          _x = _v15
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v16 = _v14.orientation
          _x = _v16
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          start = end
          end += 4
          (val2.confidence,) = _struct_f.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.detector_name = str[start:end].decode('utf-8')
          else:
            val2.detector_name = str[start:end]
          val1.model_list.append(val2)
        self.models.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.cluster_model_indices = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (self.result,) = _struct_i.unpack(str[start:end])
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
      buff.write(_struct_3I.pack(_x.table.pose.header.seq, _x.table.pose.header.stamp.secs, _x.table.pose.header.stamp.nsecs))
      _x = self.table.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d4fb.pack(_x.table.pose.pose.position.x, _x.table.pose.pose.position.y, _x.table.pose.pose.position.z, _x.table.pose.pose.orientation.x, _x.table.pose.pose.orientation.y, _x.table.pose.pose.orientation.z, _x.table.pose.pose.orientation.w, _x.table.x_min, _x.table.x_max, _x.table.y_min, _x.table.y_max, _x.table.convex_hull.type))
      length = len(self.table.convex_hull.dimensions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.table.convex_hull.dimensions.tostring())
      length = len(self.table.convex_hull.triangles)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.table.convex_hull.triangles.tostring())
      length = len(self.table.convex_hull.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.table.convex_hull.vertices:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.clusters)
      buff.write(_struct_I.pack(length))
      for val1 in self.clusters:
        _v17 = val1.header
        buff.write(_struct_I.pack(_v17.seq))
        _v18 = _v17.stamp
        _x = _v18
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v17.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        for val2 in val1.points:
          _x = val2
          buff.write(_struct_3f.pack(_x.x, _x.y, _x.z))
        length = len(val1.channels)
        buff.write(_struct_I.pack(length))
        for val2 in val1.channels:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          length = len(val2.values)
          buff.write(_struct_I.pack(length))
          pattern = '<%sf'%length
          buff.write(val2.values.tostring())
      length = len(self.models)
      buff.write(_struct_I.pack(length))
      for val1 in self.models:
        length = len(val1.model_list)
        buff.write(_struct_I.pack(length))
        for val2 in val1.model_list:
          buff.write(_struct_i.pack(val2.model_id))
          _v19 = val2.pose
          _v20 = _v19.header
          buff.write(_struct_I.pack(_v20.seq))
          _v21 = _v20.stamp
          _x = _v21
          buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
          _x = _v20.frame_id
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _v22 = _v19.pose
          _v23 = _v22.position
          _x = _v23
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v24 = _v22.orientation
          _x = _v24
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
          buff.write(_struct_f.pack(val2.confidence))
          _x = val2.detector_name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.cluster_model_indices)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.cluster_model_indices.tostring())
      buff.write(_struct_i.pack(self.result))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.table is None:
        self.table = tabletop_object_segmentation.msg.Table()
      if self.clusters is None:
        self.clusters = None
      if self.models is None:
        self.models = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.table.pose.header.seq, _x.table.pose.header.stamp.secs, _x.table.pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.table.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.table.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 73
      (_x.table.pose.pose.position.x, _x.table.pose.pose.position.y, _x.table.pose.pose.position.z, _x.table.pose.pose.orientation.x, _x.table.pose.pose.orientation.y, _x.table.pose.pose.orientation.z, _x.table.pose.pose.orientation.w, _x.table.x_min, _x.table.x_max, _x.table.y_min, _x.table.y_max, _x.table.convex_hull.type,) = _struct_7d4fb.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.table.convex_hull.dimensions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.table.convex_hull.triangles = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.table.convex_hull.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.table.convex_hull.vertices.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.clusters = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointCloud()
        _v25 = val1.header
        start = end
        end += 4
        (_v25.seq,) = _struct_I.unpack(str[start:end])
        _v26 = _v25.stamp
        _x = _v26
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v25.frame_id = str[start:end].decode('utf-8')
        else:
          _v25.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.points = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point32()
          _x = val2
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _struct_3f.unpack(str[start:end])
          val1.points.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.channels = []
        for i in range(0, length):
          val2 = sensor_msgs.msg.ChannelFloat32()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8')
          else:
            val2.name = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          pattern = '<%sf'%length
          start = end
          end += struct.calcsize(pattern)
          val2.values = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
          val1.channels.append(val2)
        self.clusters.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.models = []
      for i in range(0, length):
        val1 = household_objects_database_msgs.msg.DatabaseModelPoseList()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.model_list = []
        for i in range(0, length):
          val2 = household_objects_database_msgs.msg.DatabaseModelPose()
          start = end
          end += 4
          (val2.model_id,) = _struct_i.unpack(str[start:end])
          _v27 = val2.pose
          _v28 = _v27.header
          start = end
          end += 4
          (_v28.seq,) = _struct_I.unpack(str[start:end])
          _v29 = _v28.stamp
          _x = _v29
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v28.frame_id = str[start:end].decode('utf-8')
          else:
            _v28.frame_id = str[start:end]
          _v30 = _v27.pose
          _v31 = _v30.position
          _x = _v31
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v32 = _v30.orientation
          _x = _v32
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          start = end
          end += 4
          (val2.confidence,) = _struct_f.unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.detector_name = str[start:end].decode('utf-8')
          else:
            val2.detector_name = str[start:end]
          val1.model_list.append(val2)
        self.models.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.cluster_model_indices = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (self.result,) = _struct_i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_f = struct.Struct("<f")
_struct_7d4fb = struct.Struct("<7d4fb")
_struct_2I = struct.Struct("<2I")
_struct_i = struct.Struct("<i")
_struct_3I = struct.Struct("<3I")
_struct_4d = struct.Struct("<4d")
_struct_3f = struct.Struct("<3f")
_struct_3d = struct.Struct("<3d")
