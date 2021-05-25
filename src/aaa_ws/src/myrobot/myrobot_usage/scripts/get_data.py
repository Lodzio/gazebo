#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('get_data', anonymous=True)
print "Script running"

group = moveit_commander.MoveGroupCommander("manipulator")
robot = moveit_commander.RobotCommander()

print "Reference frame: %s" % group.get_planning_frame()
print "End effector: %s" % group.get_end_effector_link()
print "Robot Groups:"
print robot.get_group_names()
print "Current Joint Values:"
print group.get_current_joint_values()
print "Current Pose:"
print group.get_current_pose()
print "Robot State:"
print robot.get_current_state()
