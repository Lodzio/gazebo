#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from std_msgs.msg import String

def adjustGripperOrientation():
  group_pose_values = group.get_current_pose()
  group_pose_values.pose.orientation.y = 0.7071
  group_pose_values.pose.orientation.z = 0.7071
  group.set_pose_target(group_pose_values)
  plan_adjustGripperOrientation = group.plan()
  group.execute(plan_adjustGripperOrientation, wait=True)

def goPick_approach():
  group.clear_pose_targets()
  group_variable_values = [0.86, -1.33, 1.31, 0.01, 0.86, 0.00]
  group.set_joint_value_target(group_variable_values)
  plan_goPick = group.plan()
  group.execute(plan_goPick, wait=True)

def moveIncremental(direction,num):
  group.clear_pose_targets()
  group_pose_values = group.get_current_pose()
  if direction is 'x':
    group_pose_values.pose.position.x = group_pose_values.pose.position.x + num
  elif direction is 'y':
    group_pose_values.pose.position.y = group_pose_values.pose.position.y + num
  elif direction is 'z':
    group_pose_values.pose.position.z = group_pose_values.pose.position.z + num
  group.set_pose_target(group_pose_values)
  plan_moveIncremental = group.plan()
  group.execute(plan_moveIncremental, wait=True)

def openGripper():
  gripper.clear_pose_targets()
  gripper.set_named_target("open")
  plan_open = gripper.plan()
  gripper.execute(plan_open, wait=True)

def closeGripper():
  gripper.clear_pose_targets()
  gripper_values = gripper.get_current_joint_values()
  gripper_values = [0.80392, -0.80392, 0.80392, 0.80392,- 0.80392, 0.80392]
  gripper.set_joint_value_target(gripper_values)
  plan_close = gripper.plan()
  gripper.execute(plan_close)

def goHome():
  group.clear_pose_targets()
  group.set_named_target("home")
  planX = group.plan()
  group.execute(planX, wait=True)

def obtainPoseValues():
  pose = group.get_current_pose()
  print "============ Pose: ", pose

if __name__=='__main__':

  print "============ Starting setup"
  moveit_commander.roscpp_initialize(sys.argv)
  rospy.init_node('manual_PandP_general_motion', anonymous=True)

  robot = moveit_commander.RobotCommander()
  scene = moveit_commander.PlanningSceneInterface()
  group = moveit_commander.MoveGroupCommander("panda_arm")
  gripper = moveit_commander.MoveGroupCommander("hand")
  display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

  rospy.sleep(7)

  vel = float(raw_input('Max vel parameter (0 - 1): '))
  group.set_max_velocity_scaling_factor(vel)

  print "============ Running pick and place"

  goPick_approach()
  adjustGripperOrientation()
  moveIncremental('z',-0.2)
  closeGripper()
  moveIncremental('z',0.2)
  moveIncremental('x',-0.6)
  adjustGripperOrientation()
  moveIncremental('z',-0.2)
  openGripper()
  moveIncremental('z',0.2)
  moveIncremental('x',0.6)

  print "============ Running go Home"

  goHome()

  moveit_commander.roscpp_shutdown()

  print "============ STOPPING"
