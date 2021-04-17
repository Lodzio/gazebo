#!/bin/bash
#source /opt/ros/melodic/setup.bash
source /root/ws_moveit/devel/setup.bash
#roslaunch moveit_setup_assistant setup_assistant.launch
#roslaunch gazebo_ros empty_world.launch paused:=true use_sim_time:=false gui:=false throttled:=false recording:=false debug:=true verbose:=true
#rosrun gazebo_ros spawn_model -file /root/ws_moveit/src/my_project/robot.urdf -urdf -x 0 -y 0 -z 1 -model panda
#gzserver --verbose
#roslaunch my_project gazebo.launch
roslaunch my_project demo_gazebo.launch
