/* Auto-generated by genmsg_cpp for file /home/kadir/workspace/work/Dropbox/metu-ros-pkg/trunk/affordance_learning/al_msgs/msg/Object.msg */
#ifndef AL_MSGS_MESSAGE_OBJECT_H
#define AL_MSGS_MESSAGE_OBJECT_H
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

#include "al_msgs/Color.h"
#include "al_msgs/Shape.h"
#include "al_msgs/Spec.h"
#include "arm_navigation_msgs/CollisionObject.h"

namespace al_msgs
{
template <class ContainerAllocator>
struct Object_ {
  typedef Object_<ContainerAllocator> Type;

  Object_()
  : name()
  , model_xml()
  , color()
  , shapes()
  , spec()
  , object()
  {
  }

  Object_(const ContainerAllocator& _alloc)
  : name(_alloc)
  , model_xml(_alloc)
  , color(_alloc)
  , shapes(_alloc)
  , spec(_alloc)
  , object(_alloc)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  name;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _model_xml_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  model_xml;

  typedef  ::al_msgs::Color_<ContainerAllocator>  _color_type;
   ::al_msgs::Color_<ContainerAllocator>  color;

  typedef std::vector< ::al_msgs::Shape_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::al_msgs::Shape_<ContainerAllocator> >::other >  _shapes_type;
  std::vector< ::al_msgs::Shape_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::al_msgs::Shape_<ContainerAllocator> >::other >  shapes;

  typedef  ::al_msgs::Spec_<ContainerAllocator>  _spec_type;
   ::al_msgs::Spec_<ContainerAllocator>  spec;

  typedef  ::arm_navigation_msgs::CollisionObject_<ContainerAllocator>  _object_type;
   ::arm_navigation_msgs::CollisionObject_<ContainerAllocator>  object;


  typedef boost::shared_ptr< ::al_msgs::Object_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::al_msgs::Object_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct Object
typedef  ::al_msgs::Object_<std::allocator<void> > Object;

typedef boost::shared_ptr< ::al_msgs::Object> ObjectPtr;
typedef boost::shared_ptr< ::al_msgs::Object const> ObjectConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::al_msgs::Object_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::al_msgs::Object_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace al_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::al_msgs::Object_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::al_msgs::Object_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::al_msgs::Object_<ContainerAllocator> > {
  static const char* value() 
  {
    return "7a7a10bf94774ab3df7e3bd5c08b07f9";
  }

  static const char* value(const  ::al_msgs::Object_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x7a7a10bf94774ab3ULL;
  static const uint64_t static_value2 = 0xdf7e3bd5c08b07f9ULL;
};

template<class ContainerAllocator>
struct DataType< ::al_msgs::Object_<ContainerAllocator> > {
  static const char* value() 
  {
    return "al_msgs/Object";
  }

  static const char* value(const  ::al_msgs::Object_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::al_msgs::Object_<ContainerAllocator> > {
  static const char* value() 
  {
    return "string name\n\
string model_xml\n\
al_msgs/Color color\n\
al_msgs/Shape[] shapes\n\
al_msgs/Spec spec\n\
arm_navigation_msgs/CollisionObject object\n\
\n\
================================================================================\n\
MSG: al_msgs/Color\n\
int8 MAX_COLOR_INDEX=4\n\
\n\
int8 BLACK=0\n\
int8 RED=1\n\
int8 GREEN=2\n\
int8 BLUE=3\n\
int8 WHITE=4\n\
int8 color\n\
\n\
================================================================================\n\
MSG: al_msgs/Shape\n\
int8 MAX_SHAPE_INDEX=6\n\
int8 CUP=0\n\
int8 BOX=1\n\
int8 CYLINDER=2\n\
int8 BALL=3\n\
int8 SPHERE=4\n\
int8 CUBE=5\n\
int8 OTHER=6\n\
int8 shape\n\
float32 prob\n\
\n\
================================================================================\n\
MSG: al_msgs/Spec\n\
int8 MAX_SPEC_INDEX=7\n\
\n\
int8 THIN=0\n\
int8 THICK=1\n\
int8 ROUND=2\n\
int8 EDGY=3\n\
int8 TALL=4\n\
int8 SHORT=5\n\
int8 BIG=6\n\
int8 SMALL=7\n\
int8 spec\n\
float32 prob\n\
\n\
================================================================================\n\
MSG: arm_navigation_msgs/CollisionObject\n\
# a header, used for interpreting the poses\n\
Header header\n\
\n\
# the id of the object\n\
string id\n\
\n\
# The padding used for filtering points near the object.\n\
# This does not affect collision checking for the object.  \n\
# Set to negative to get zero padding.\n\
float32 padding\n\
\n\
#This contains what is to be done with the object\n\
CollisionObjectOperation operation\n\
\n\
#the shapes associated with the object\n\
arm_navigation_msgs/Shape[] shapes\n\
\n\
#the poses associated with the shapes - will be transformed using the header\n\
geometry_msgs/Pose[] poses\n\
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
MSG: arm_navigation_msgs/CollisionObjectOperation\n\
#Puts the object into the environment\n\
#or updates the object if already added\n\
byte ADD=0\n\
\n\
#Removes the object from the environment entirely\n\
byte REMOVE=1\n\
\n\
#Only valid within the context of a CollisionAttachedObject message\n\
#Will be ignored if sent with an CollisionObject message\n\
#Takes an attached object, detaches from the attached link\n\
#But adds back in as regular object\n\
byte DETACH_AND_ADD_AS_OBJECT=2\n\
\n\
#Only valid within the context of a CollisionAttachedObject message\n\
#Will be ignored if sent with an CollisionObject message\n\
#Takes current object in the environment and removes it as\n\
#a regular object\n\
byte ATTACH_AND_REMOVE_AS_OBJECT=3\n\
\n\
# Byte code for operation\n\
byte operation\n\
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
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
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
";
  }

  static const char* value(const  ::al_msgs::Object_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::al_msgs::Object_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.name);
    stream.next(m.model_xml);
    stream.next(m.color);
    stream.next(m.shapes);
    stream.next(m.spec);
    stream.next(m.object);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct Object_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::al_msgs::Object_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::al_msgs::Object_<ContainerAllocator> & v) 
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "model_xml: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.model_xml);
    s << indent << "color: ";
s << std::endl;
    Printer< ::al_msgs::Color_<ContainerAllocator> >::stream(s, indent + "  ", v.color);
    s << indent << "shapes[]" << std::endl;
    for (size_t i = 0; i < v.shapes.size(); ++i)
    {
      s << indent << "  shapes[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::al_msgs::Shape_<ContainerAllocator> >::stream(s, indent + "    ", v.shapes[i]);
    }
    s << indent << "spec: ";
s << std::endl;
    Printer< ::al_msgs::Spec_<ContainerAllocator> >::stream(s, indent + "  ", v.spec);
    s << indent << "object: ";
s << std::endl;
    Printer< ::arm_navigation_msgs::CollisionObject_<ContainerAllocator> >::stream(s, indent + "  ", v.object);
  }
};


} // namespace message_operations
} // namespace ros

#endif // AL_MSGS_MESSAGE_OBJECT_H

