#!/usr/bin/env sh
# generated from catkin/cmake/templates/env.sh.in

if [ $# -eq 0 ] ; then
  /bin/echo "Entering environment at '/home/kadir/workspace/work/Dropbox/metu-ros-pkg/trunk/affordance_learning/al_perception/devel', type 'exit' to leave"
  . "/home/kadir/workspace/work/Dropbox/metu-ros-pkg/trunk/affordance_learning/al_perception/devel/setup.sh"
  "$SHELL" -i
  /bin/echo "Exiting environment at '/home/kadir/workspace/work/Dropbox/metu-ros-pkg/trunk/affordance_learning/al_perception/devel'"
else
  . "/home/kadir/workspace/work/Dropbox/metu-ros-pkg/trunk/affordance_learning/al_perception/devel/setup.sh"
  exec "$@"
fi
