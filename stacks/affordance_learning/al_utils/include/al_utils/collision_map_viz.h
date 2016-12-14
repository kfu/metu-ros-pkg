/*
 * collision_map_viz.h
 * Copyright (c) 2011, Kadir Firat Uyanik, KOVAN Research Lab, METU
 * kadir@ceng.metu.edu.tr
 *
 * All rights reserved.
 *
 * Software License Agreement (BSD License)
 *
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of KOVAN Lab nor the names of its
 *       contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef COLLISION_MAP_VIZ_H_
#define COLLISION_MAP_VIZ_H_

#include "ros/ros.h"

#include "arm_navigation_msgs/CollisionObject.h"

namespace al
{

  namespace perception
  {

    class CollisionMapViz
    {
    public:
      CollisionMapViz (ros::NodeHandle* nh);
      virtual
      ~CollisionMapViz ();
    private:
      ros::NodeHandle* nh_;
      ros::Subscriber sub_col_obj_;

      void colMapObjCallback(arm_navigation_msgs::CollisionObjectConstPtr col_obj);
    };

  }

}

#endif /* COLLISION_MAP_VIZ_H_ */