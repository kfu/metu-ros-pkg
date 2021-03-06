/* Auto-generated by genmsg_cpp for file /home/user/metu-ros-pkg/affordance_learning/al_behavior/msg/ArmResult.msg */
#ifndef AL_BEHAVIOR_MESSAGE_ARMRESULT_H
#define AL_BEHAVIOR_MESSAGE_ARMRESULT_H
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

#include "al_msgs/JointCmd.h"
#include "geometry_msgs/Pose.h"

namespace al_behavior
{
template <class ContainerAllocator>
struct ArmResult_ {
  typedef ArmResult_<ContainerAllocator> Type;

  ArmResult_()
  : result_mode(false)
  , result_joint_pos()
  , result_cartesian_pos()
  {
  }

  ArmResult_(const ContainerAllocator& _alloc)
  : result_mode(false)
  , result_joint_pos(_alloc)
  , result_cartesian_pos(_alloc)
  {
  }

  typedef uint8_t _result_mode_type;
  uint8_t result_mode;

  typedef std::vector< ::al_msgs::JointCmd_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::al_msgs::JointCmd_<ContainerAllocator> >::other >  _result_joint_pos_type;
  std::vector< ::al_msgs::JointCmd_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::al_msgs::JointCmd_<ContainerAllocator> >::other >  result_joint_pos;

  typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _result_cartesian_pos_type;
   ::geometry_msgs::Pose_<ContainerAllocator>  result_cartesian_pos;


  typedef boost::shared_ptr< ::al_behavior::ArmResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::al_behavior::ArmResult_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ArmResult
typedef  ::al_behavior::ArmResult_<std::allocator<void> > ArmResult;

typedef boost::shared_ptr< ::al_behavior::ArmResult> ArmResultPtr;
typedef boost::shared_ptr< ::al_behavior::ArmResult const> ArmResultConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::al_behavior::ArmResult_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::al_behavior::ArmResult_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace al_behavior

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::al_behavior::ArmResult_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::al_behavior::ArmResult_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::al_behavior::ArmResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0432be3e44a007ce980ea10241972671";
  }

  static const char* value(const  ::al_behavior::ArmResult_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0432be3e44a007ceULL;
  static const uint64_t static_value2 = 0x980ea10241972671ULL;
};

template<class ContainerAllocator>
struct DataType< ::al_behavior::ArmResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "al_behavior/ArmResult";
  }

  static const char* value(const  ::al_behavior::ArmResult_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::al_behavior::ArmResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#result definition\n\
bool result_mode\n\
al_msgs/JointCmd[] result_joint_pos\n\
geometry_msgs/Pose result_cartesian_pos\n\
\n\
================================================================================\n\
MSG: al_msgs/JointCmd\n\
uint8 joint_id\n\
float64 joint_val\n\
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
";
  }

  static const char* value(const  ::al_behavior::ArmResult_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::al_behavior::ArmResult_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.result_mode);
    stream.next(m.result_joint_pos);
    stream.next(m.result_cartesian_pos);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ArmResult_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::al_behavior::ArmResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::al_behavior::ArmResult_<ContainerAllocator> & v) 
  {
    s << indent << "result_mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.result_mode);
    s << indent << "result_joint_pos[]" << std::endl;
    for (size_t i = 0; i < v.result_joint_pos.size(); ++i)
    {
      s << indent << "  result_joint_pos[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::al_msgs::JointCmd_<ContainerAllocator> >::stream(s, indent + "    ", v.result_joint_pos[i]);
    }
    s << indent << "result_cartesian_pos: ";
s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.result_cartesian_pos);
  }
};


} // namespace message_operations
} // namespace ros

#endif // AL_BEHAVIOR_MESSAGE_ARMRESULT_H

