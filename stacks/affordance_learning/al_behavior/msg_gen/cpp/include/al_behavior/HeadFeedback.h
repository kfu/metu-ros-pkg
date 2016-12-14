/* Auto-generated by genmsg_cpp for file /home/user/metu-ros-pkg/affordance_learning/al_behavior/msg/HeadFeedback.msg */
#ifndef AL_BEHAVIOR_MESSAGE_HEADFEEDBACK_H
#define AL_BEHAVIOR_MESSAGE_HEADFEEDBACK_H
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

#include "geometry_msgs/Point.h"

namespace al_behavior
{
template <class ContainerAllocator>
struct HeadFeedback_ {
  typedef HeadFeedback_<ContainerAllocator> Type;

  HeadFeedback_()
  : feedback()
  {
  }

  HeadFeedback_(const ContainerAllocator& _alloc)
  : feedback(_alloc)
  {
  }

  typedef  ::geometry_msgs::Point_<ContainerAllocator>  _feedback_type;
   ::geometry_msgs::Point_<ContainerAllocator>  feedback;


  typedef boost::shared_ptr< ::al_behavior::HeadFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::al_behavior::HeadFeedback_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct HeadFeedback
typedef  ::al_behavior::HeadFeedback_<std::allocator<void> > HeadFeedback;

typedef boost::shared_ptr< ::al_behavior::HeadFeedback> HeadFeedbackPtr;
typedef boost::shared_ptr< ::al_behavior::HeadFeedback const> HeadFeedbackConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::al_behavior::HeadFeedback_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::al_behavior::HeadFeedback_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace al_behavior

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::al_behavior::HeadFeedback_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::al_behavior::HeadFeedback_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::al_behavior::HeadFeedback_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bcd3cc9315c46650280beb95ac8575e6";
  }

  static const char* value(const  ::al_behavior::HeadFeedback_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xbcd3cc9315c46650ULL;
  static const uint64_t static_value2 = 0x280beb95ac8575e6ULL;
};

template<class ContainerAllocator>
struct DataType< ::al_behavior::HeadFeedback_<ContainerAllocator> > {
  static const char* value() 
  {
    return "al_behavior/HeadFeedback";
  }

  static const char* value(const  ::al_behavior::HeadFeedback_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::al_behavior::HeadFeedback_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#feedback\n\
geometry_msgs/Point feedback\n\
\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
";
  }

  static const char* value(const  ::al_behavior::HeadFeedback_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::al_behavior::HeadFeedback_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::al_behavior::HeadFeedback_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.feedback);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct HeadFeedback_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::al_behavior::HeadFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::al_behavior::HeadFeedback_<ContainerAllocator> & v) 
  {
    s << indent << "feedback: ";
s << std::endl;
    Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "  ", v.feedback);
  }
};


} // namespace message_operations
} // namespace ros

#endif // AL_BEHAVIOR_MESSAGE_HEADFEEDBACK_H

