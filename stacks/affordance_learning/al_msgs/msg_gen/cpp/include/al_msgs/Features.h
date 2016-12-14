/* Auto-generated by genmsg_cpp for file /home/kadir/workspace/work/Dropbox/metu-ros-pkg/trunk/affordance_learning/al_msgs/msg/Features.msg */
#ifndef AL_MSGS_MESSAGE_FEATURES_H
#define AL_MSGS_MESSAGE_FEATURES_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "sensor_msgs/PointCloud2.h"

namespace al_msgs
{
template <class ContainerAllocator>
struct Features_ {
  typedef Features_<ContainerAllocator> Type;

  Features_()
  : cloud()
  , gaussian_curvatures()
  , mean_curvatures()
  , shape_indices()
  , curvedness()
  {
  }

  Features_(const ContainerAllocator& _alloc)
  : cloud(_alloc)
  , gaussian_curvatures(_alloc)
  , mean_curvatures(_alloc)
  , shape_indices(_alloc)
  , curvedness(_alloc)
  {
  }

  typedef  ::sensor_msgs::PointCloud2_<ContainerAllocator>  _cloud_type;
   ::sensor_msgs::PointCloud2_<ContainerAllocator>  cloud;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _gaussian_curvatures_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  gaussian_curvatures;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _mean_curvatures_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  mean_curvatures;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _shape_indices_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  shape_indices;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _curvedness_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  curvedness;


  typedef boost::shared_ptr< ::al_msgs::Features_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::al_msgs::Features_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct Features
typedef  ::al_msgs::Features_<std::allocator<void> > Features;

typedef boost::shared_ptr< ::al_msgs::Features> FeaturesPtr;
typedef boost::shared_ptr< ::al_msgs::Features const> FeaturesConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::al_msgs::Features_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::al_msgs::Features_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace al_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::al_msgs::Features_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::al_msgs::Features_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::al_msgs::Features_<ContainerAllocator> > {
  static const char* value() 
  {
    return "29cd0f25d72cdc511025d699579cd62d";
  }

  static const char* value(const  ::al_msgs::Features_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x29cd0f25d72cdc51ULL;
  static const uint64_t static_value2 = 0x1025d699579cd62dULL;
};

template<class ContainerAllocator>
struct DataType< ::al_msgs::Features_<ContainerAllocator> > {
  static const char* value() 
  {
    return "al_msgs/Features";
  }

  static const char* value(const  ::al_msgs::Features_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::al_msgs::Features_<ContainerAllocator> > {
  static const char* value() 
  {
    return "sensor_msgs/PointCloud2 cloud\n\
float32[] gaussian_curvatures\n\
float32[] mean_curvatures\n\
float32[] shape_indices\n\
float32[] curvedness\n\
\n\
================================================================================\n\
MSG: sensor_msgs/PointCloud2\n\
# This message holds a collection of N-dimensional points, which may\n\
# contain additional information such as normals, intensity, etc. The\n\
# point data is stored as a binary blob, its layout described by the\n\
# contents of the \"fields\" array.\n\
\n\
# The point cloud data may be organized 2d (image-like) or 1d\n\
# (unordered). Point clouds organized as 2d images may be produced by\n\
# camera depth sensors such as stereo or time-of-flight.\n\
\n\
# Time of sensor data acquisition, and the coordinate frame ID (for 3d\n\
# points).\n\
Header header\n\
\n\
# 2D structure of the point cloud. If the cloud is unordered, height is\n\
# 1 and width is the length of the point cloud.\n\
uint32 height\n\
uint32 width\n\
\n\
# Describes the channels and their layout in the binary data blob.\n\
PointField[] fields\n\
\n\
bool    is_bigendian # Is this data bigendian?\n\
uint32  point_step   # Length of a point in bytes\n\
uint32  row_step     # Length of a row in bytes\n\
uint8[] data         # Actual point data, size is (row_step*height)\n\
\n\
bool is_dense        # True if there are no invalid points\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: sensor_msgs/PointField\n\
# This message holds the description of one point entry in the\n\
# PointCloud2 message format.\n\
uint8 INT8    = 1\n\
uint8 UINT8   = 2\n\
uint8 INT16   = 3\n\
uint8 UINT16  = 4\n\
uint8 INT32   = 5\n\
uint8 UINT32  = 6\n\
uint8 FLOAT32 = 7\n\
uint8 FLOAT64 = 8\n\
\n\
string name      # Name of field\n\
uint32 offset    # Offset from start of point struct\n\
uint8  datatype  # Datatype enumeration, see above\n\
uint32 count     # How many elements in the field\n\
\n\
";
  }

  static const char* value(const  ::al_msgs::Features_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::al_msgs::Features_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.cloud);
    stream.next(m.gaussian_curvatures);
    stream.next(m.mean_curvatures);
    stream.next(m.shape_indices);
    stream.next(m.curvedness);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct Features_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::al_msgs::Features_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::al_msgs::Features_<ContainerAllocator> & v) 
  {
    s << indent << "cloud: ";
s << std::endl;
    Printer< ::sensor_msgs::PointCloud2_<ContainerAllocator> >::stream(s, indent + "  ", v.cloud);
    s << indent << "gaussian_curvatures[]" << std::endl;
    for (size_t i = 0; i < v.gaussian_curvatures.size(); ++i)
    {
      s << indent << "  gaussian_curvatures[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.gaussian_curvatures[i]);
    }
    s << indent << "mean_curvatures[]" << std::endl;
    for (size_t i = 0; i < v.mean_curvatures.size(); ++i)
    {
      s << indent << "  mean_curvatures[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.mean_curvatures[i]);
    }
    s << indent << "shape_indices[]" << std::endl;
    for (size_t i = 0; i < v.shape_indices.size(); ++i)
    {
      s << indent << "  shape_indices[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.shape_indices[i]);
    }
    s << indent << "curvedness[]" << std::endl;
    for (size_t i = 0; i < v.curvedness.size(); ++i)
    {
      s << indent << "  curvedness[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.curvedness[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // AL_MSGS_MESSAGE_FEATURES_H

