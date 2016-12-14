#include <ros/ros.h>
#include "ros/rate.h"

#include <tf/transform_listener.h>
#include <tf/transform_broadcaster.h>

const std::string BASE_FOOTPRINT_FRAME = "base_footprint";
//const std::string OPENNI_DEPTH_FRAME = "openni_depth_frame";
//const std::string OPENNI_DEPTH_FRAME = "left_camera_depth_frame";
//const std::string CAMERA_LINK = "camera_link";
//const std::string CAMERA_LINK = "left_camera_link";
const std::string LEFT_SHOULDER_FRAME = "left_shoulder_1";
const std::string RIGHT_SHOULDER_FRAME = "right_shoulder_1";
const std::string LEFT_UPPER_ARM_FRAME = "left_upper_arm_h";
const std::string RIGHT_UPPER_ARM_FRAME = "right_upper_arm_h";
const std::string LEFT_ELBOW_FRAME = "left_elbow_1";
const std::string RIGHT_ELBOW_FRAME = "right_elbow_1";
const std::string LEFT_LOWER_ARM_FRAME = "left_lower_arm_h";
const std::string RIGHT_LOWER_ARM_FRAME = "right_lower_arm_h";
const std::string LEFT_HAND_FRAME = "left_hand_1";
const std::string RIGHT_HAND_FRAME = "right_hand_1";
//const std::string LEFT_HAND_LEFT_GRIPPER = "left_hand_l_gripper";
//const std::string LEFT_HAND_RIGHT_GRIPPER = "left_hand_r_gripper";
//const std::string LEFT_HAND_LEFT_TIP = "left_hand_l_tip";
//const std::string LEFT_HAND_RIGHT_TIP = "left_hand_r_tip";
//const std::string RIGHT_HAND_LEFT_GRIPPER = "right_hand_l_gripper";
//const std::string RIGHT_HAND_RIGHT_GRIPPER = "right_hand_r_gripper";
//const std::string RIGHT_HAND_LEFT_TIP = "right_hand_l_tip";
//const std::string RIGHT_HAND_RIGHT_TIP = "right_hand_r_tip";

const double PI = 3.14159;
std::vector<std::string> frame_names;
ros::NodeHandle* nh;

int
main (int argc, char* argv[])
{
  ros::init (argc, argv, "human_tf_publisher");
  nh = new ros::NodeHandle ();

  static tf::TransformBroadcaster br;

  //  ros::WallRate r(50);
  ros::Rate r (50);
  while (nh->ok ())
  {
    tf::StampedTransform transform;

//    transform.frame_id_ = BASE_FOOTPRINT_FRAME;
//    transform.child_frame_id_ = OPENNI_DEPTH_FRAME;

//    transform.stamp_ = ros::Time::now ();
    //transform.setOrigin (tf::Vector3 (0.5, 0, 0.8));
//    transform.setOrigin (tf::Vector3 (0, 0, 0));
    tf::Quaternion quat;
//    quat.setRPY (0, 0, 0);
//    transform.setRotation (quat);
    //    quat.setX (0);
    //    quat.setY (0);
    //    quat.setZ (1);
    //    quat.setW (PI);
    //    transform.setRotation (quat);
//    br.sendTransform (transform);
//    ros::spinOnce ();

    transform.frame_id_ = LEFT_SHOULDER_FRAME;
    transform.child_frame_id_ = LEFT_UPPER_ARM_FRAME;
    transform.stamp_ = ros::Time::now ();
    //    transform.stamp_ = ros::Time(0);
    transform.setOrigin (tf::Vector3 (0.14, 0, 0));
    quat.setRPY (0, PI / 2, 0);
    transform.setRotation (quat);
    br.sendTransform (transform);
    ros::spinOnce ();

    transform.frame_id_ = RIGHT_SHOULDER_FRAME;
    transform.child_frame_id_ = RIGHT_UPPER_ARM_FRAME;
    transform.stamp_ = ros::Time::now ();
    //    transform.stamp_ = ros::Time(0);
    transform.setOrigin (tf::Vector3 (-0.14, 0, 0));
    quat.setRPY (0, -PI / 2, 0);
    transform.setRotation (quat);
    br.sendTransform (transform);
    ros::spinOnce ();

    transform.frame_id_ = LEFT_ELBOW_FRAME;
    transform.child_frame_id_ = LEFT_LOWER_ARM_FRAME;
    transform.stamp_ = ros::Time::now ();
    //    transform.stamp_ = ros::Time(0);
    transform.setOrigin (tf::Vector3 (0.14, 0, 0));
    quat.setRPY (0, PI / 2, 0);
    transform.setRotation (quat);
    br.sendTransform (transform);
    ros::spinOnce ();

    transform.frame_id_ = RIGHT_ELBOW_FRAME;
    transform.child_frame_id_ = RIGHT_LOWER_ARM_FRAME;
    transform.stamp_ = ros::Time::now ();
    //    transform.stamp_ = ros::Time(0);
    transform.setOrigin (tf::Vector3 (-0.14, 0, 0));
    quat.setRPY (0, -PI / 2, 0);
    transform.setRotation (quat);
    br.sendTransform (transform);
    ros::spinOnce ();

//    transform.frame_id_ = LEFT_HAND_FRAME;
//    transform.child_frame_id_ = LEFT_HAND_LEFT_GRIPPER;
//    transform.stamp_ = ros::Time::now ();
//    //    transform.stamp_ = ros::Time(0);
//    transform.setOrigin (tf::Vector3 (0, 0, 0));
//    quat.setRPY (0, 0, 0);
//    transform.setRotation (quat);
//    br.sendTransform (transform);
//    ros::spinOnce ();
//
//    transform.frame_id_ = LEFT_HAND_FRAME;
//    transform.child_frame_id_ = LEFT_HAND_RIGHT_GRIPPER;
//    transform.stamp_ = ros::Time::now ();
//    //    transform.stamp_ = ros::Time(0);
//    transform.setOrigin (tf::Vector3 (0, 0, 0));
//    quat.setRPY (0, 0, 0);
//    transform.setRotation (quat);
//    br.sendTransform (transform);
//    ros::spinOnce ();
//
//    transform.frame_id_ = LEFT_HAND_LEFT_GRIPPER;
//    transform.child_frame_id_ = LEFT_HAND_LEFT_TIP;
//    transform.stamp_ = ros::Time::now ();
//    //    transform.stamp_ = ros::Time(0);
//    transform.setOrigin (tf::Vector3 (0, 0, 0));
//    quat.setRPY (0, 0, 0);
//    transform.setRotation (quat);
//    br.sendTransform (transform);
//    ros::spinOnce ();
//
//    transform.frame_id_ = LEFT_HAND_RIGHT_GRIPPER;
//    transform.child_frame_id_ = LEFT_HAND_RIGHT_TIP;
//    transform.stamp_ = ros::Time::now ();
//    //    transform.stamp_ = ros::Time(0);
//    transform.setOrigin (tf::Vector3 (0, 0, 0));
//    quat.setRPY (0, 0, 0);
//    transform.setRotation (quat);
//    br.sendTransform (transform);
//    ros::spinOnce ();
//
//    transform.frame_id_ = RIGHT_HAND_FRAME;
//    transform.child_frame_id_ = RIGHT_HAND_LEFT_GRIPPER;
//    transform.stamp_ = ros::Time::now ();
//    //    transform.stamp_ = ros::Time(0);
//    transform.setOrigin (tf::Vector3 (0, 0, 0));
//    quat.setRPY (0, 0, 0);
//    transform.setRotation (quat);
//    br.sendTransform (transform);
//    ros::spinOnce ();
//
//    transform.frame_id_ = RIGHT_HAND_FRAME;
//    transform.child_frame_id_ = RIGHT_HAND_RIGHT_GRIPPER;
//    transform.stamp_ = ros::Time::now ();
//    //    transform.stamp_ = ros::Time(0);
//    transform.setOrigin (tf::Vector3 (0, 0, 0));
//    quat.setRPY (0, 0, 0);
//    transform.setRotation (quat);
//    br.sendTransform (transform);
//    ros::spinOnce ();
//
//    transform.frame_id_ = RIGHT_HAND_LEFT_GRIPPER;
//    transform.child_frame_id_ = RIGHT_HAND_LEFT_TIP;
//    transform.stamp_ = ros::Time::now ();
//    //    transform.stamp_ = ros::Time(0);
//    transform.setOrigin (tf::Vector3 (0, 0, 0));
//    quat.setRPY (0, 0, 0);
//    transform.setRotation (quat);
//    br.sendTransform (transform);
//    ros::spinOnce ();
//
//    transform.frame_id_ = RIGHT_HAND_RIGHT_GRIPPER;
//    transform.child_frame_id_ = RIGHT_HAND_RIGHT_TIP;
//    transform.stamp_ = ros::Time::now ();
//    //    transform.stamp_ = ros::Time(0);
//    transform.setOrigin (tf::Vector3 (0, 0, 0));
//    quat.setRPY (0, 0, 0);
//    transform.setRotation (quat);
//    br.sendTransform (transform);
//    ros::spinOnce ();

	/*
    transform.frame_id_ = OPENNI_DEPTH_FRAME;
    transform.child_frame_id_ = CAMERA_LINK;
    transform.stamp_ = ros::Time::now ();
    //    transform.stamp_ = ros::Time(0);
    transform.setOrigin (tf::Vector3 (0, 0.02, 0));
    quat.setRPY (0, 0, 0);
    transform.setRotation (quat);
    br.sendTransform (transform);
	*/
    ros::spinOnce ();
    r.sleep ();
    std::cout << "asd" << std::endl;

  }
  return 1;
}
