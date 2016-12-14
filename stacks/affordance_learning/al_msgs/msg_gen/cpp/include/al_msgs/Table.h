/* Auto-generated by genmsg_cpp for file /home/kadir/workspace/work/Dropbox/metu-ros-pkg/trunk/affordance_learning/al_msgs/msg/Table.msg */
#ifndef AL_MSGS_MESSAGE_TABLE_H
#define AL_MSGS_MESSAGE_TABLE_H
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

#include "geometry_msgs/PoseStamped.h"
#include "arm_navigation_msgs/Shape.h"

namespace al_msgs
{
template <class ContainerAllocator>
struct Table_ {
  typedef Table_<ContainerAllocator> Type;

  Table_()
  : pose()
  , x_min(0.0)
  , x_max(0.0)
  , y_min(0.0)
  , y_max(0.0)
  , convex_hull()
  {
  }

  Table_(const ContainerAllocator& _alloc)
  : pose(_alloc)
  , x_min(0.0)
  , x_max(0.0)
  , y_min(0.0)
  , y_max(0.0)
  , convex_hull(_alloc)
  {
  }

  typedef  ::geometry_msgs::PoseStamped_<ContainerAllocator>  _pose_type;
   ::geometry_msgs::PoseStamped_<ContainerAllocator>  pose;

  typedef float _x_min_type;
  float x_min;

  typedef float _x_max_type;
  float x_max;

  typedef float _y_min_type;
  float y_min;

  typedef float _y_max_type;
  float y_max;

  typedef  ::arm_navigation_msgs::Shape_<ContainerAllocator>  _convex_hull_type;
   ::arm_navigation_msgs::Shape_<ContainerAllocator>  convex_hull;


  typedef boost::shared_ptr< ::al_msgs::Table_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::al_msgs::Table_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct Table
typedef  ::al_msgs::Table_<std::allocator<void> > Table;

typedef boost::shared_ptr< ::al_msgs::Table> TablePtr;
typedef boost::shared_ptr< ::al_msgs::Table const> TableConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::al_msgs::Table_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::al_msgs::Table_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace al_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::al_msgs::Table_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::al_msgs::Table_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::al_msgs::Table_<ContainerAllocator> > {
  static const char* value() 
  {
    return "886d01470541b85c431cbb9613db9497";
  }

  static const char* value(const  ::al_msgs::Table_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x886d01470541b85cULL;
  static const uint64_t static_value2 = 0x431cbb9613db9497ULL;
};

template<class ContainerAllocator>
struct DataType< ::al_msgs::Table_<ContainerAllocator> > {
  static const char* value() 
  {
    return "al_msgs/Table";
  }

  static const char* value(const  ::al_msgs::Table_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::al_msgs::Table_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# Informs that a planar table has been detected at a given location\n\
\n\
# The pose gives you the transform that take you to the coordinate system\n\
# of the table, with the origin somewhere in the table plane and the \n\
# z axis normal to the plane\n\
geometry_msgs/PoseStamped pose\n\
\n\
# These values give you the observed extents of the table, along x and y,\n\
# in the table's own coordinate system (above)\n\
# there is no guarantee that the origin of the table coordinate system is\n\
# inside the boundary defined by these values. \n\
float32 x_min\n\
float32 x_max\n\
float32 y_min\n\
float32 y_max\n\
\n\
# There is no guarantee that the table does NOT extend further than these \n\
# values; this is just as far as we've observed it.\n\
\n\
\n\
# Newer table definition as triangle mesh of convex hull (relative to pose)\n\
arm_navigation_msgs/Shape convex_hull\n\
\n\
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
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
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/Shape\n\
byte SPHERE=0\n\
byte BOX=1\n\
byte CYLINDER=2\n\
byte MESH=3\n\
\n\
byte type\n\
\n\
\n\
#### define sphere, box, cylinder ####\n\
# the origin of each shape is considered at the shape's center\n\
\n\
# for sphere\n\
# radius := dimensions[0]\n\
\n\
# for cylinder\n\
# radius := dimensions[0]\n\
# length := dimensions[1]\n\
# the length is along the Z axis\n\
\n\
# for box\n\
# size_x := dimensions[0]\n\
# size_y := dimensions[1]\n\
# size_z := dimensions[2]\n\
float64[] dimensions\n\
\n\
\n\
#### define mesh ####\n\
\n\
# list of triangles; triangle k is defined by tre vertices located\n\
# at indices triangles[3k], triangles[3k+1], triangles[3k+2]\n\
int32[] triangles\n\
geometry_msgs/Point[] vertices\n\
\n\
";
  }

  static const char* value(const  ::al_msgs::Table_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::al_msgs::Table_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.pose);
    stream.next(m.x_min);
    stream.next(m.x_max);
    stream.next(m.y_min);
    stream.next(m.y_max);
    stream.next(m.convex_hull);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct Table_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::al_msgs::Table_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::al_msgs::Table_<ContainerAllocator> & v) 
  {
    s << indent << "pose: ";
s << std::endl;
    Printer< ::geometry_msgs::PoseStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
    s << indent << "x_min: ";
    Printer<float>::stream(s, indent + "  ", v.x_min);
    s << indent << "x_max: ";
    Printer<float>::stream(s, indent + "  ", v.x_max);
    s << indent << "y_min: ";
    Printer<float>::stream(s, indent + "  ", v.y_min);
    s << indent << "y_max: ";
    Printer<float>::stream(s, indent + "  ", v.y_max);
    s << indent << "convex_hull: ";
s << std::endl;
    Printer< ::arm_navigation_msgs::Shape_<ContainerAllocator> >::stream(s, indent + "  ", v.convex_hull);
  }
};


} // namespace message_operations
} // namespace ros

#endif // AL_MSGS_MESSAGE_TABLE_H

