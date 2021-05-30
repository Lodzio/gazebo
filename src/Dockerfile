FROM ubuntu:focal
ENV DEBIAN_FRONTEND=noninteractive

# gozebo configuration
RUN apt-get update
RUN apt-get install lsb-release gnupg2 curl -y
RUN curl -sSL http://get.gazebosim.org | sh
# ROS configuration
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | apt-key add -
RUN apt-get update
RUN apt-get install ros-noetic-ros-base -y
RUN apt-get install ros-noetic-gazebo-ros ros-noetic-gazebo-dev ros-noetic-gazebo-plugins -y
RUN apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control -y
RUN apt-get install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential -y
SHELL ["/bin/bash", "-c"]
RUN source /opt/ros/noetic/setup.bash

# MoveIt configuration
RUN rosdep init
RUN rosdep update
RUN apt update
RUN apt dist-upgrade -y
RUN apt-get install ros-noetic-catkin python3-catkin-tools -y
RUN apt-get install ros-noetic-moveit -y
WORKDIR /root/ws_moveit/src
RUN apt-get install python3-pip -y
RUN pip3 install osrf-pycommon
RUN apt-get install wget -y
RUN wstool init .
RUN wstool merge -t . https://raw.githubusercontent.com/ros-planning/moveit/master/moveit.rosinstall
COPY ./my_project ./my_project
RUN wstool update -t .
RUN rosdep install -y --from-paths . --ignore-src --rosdistro noetic
WORKDIR /root/ws_moveit
COPY chomp_planner.cpp /root/ws_moveit/src/moveit/moveit_planners/chomp/chomp_motion_planner/src/chomp_planner.cpp
RUN catkin config --extend /opt/ros/noetic --cmake-args -DCMAKE_BUILD_TYPE=Release
RUN catkin build
RUN source devel/setup.bash
WORKDIR /root/ws_moveit/src

# STOPM Planner configuration
#RUN wstool set stomp https://github.com/ros-industrial/stomp_ros.git --git -y
#RUN wstool update
#RUN catkin build
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics
WORKDIR /root/ws_moveit/
RUN apt-get install gdb ros-noetic*joint-trajectory-controller* -y

COPY robots/ /opt/ros/noetic/share/franka_description/robots/
RUN echo "source /root/ws_moveit/devel/setup.bash" >> ~/.bashrc
COPY entrypoint.sh entrypoint.sh
COPY my_world.world /usr/share/gazebo-11/worlds/my_world.world
COPY pick_place_tutorial.cpp src/moveit_tutorials/doc/pick_place/src/pick_place_tutorial.cpp
RUN catkin build
#ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT [ "./entrypoint.sh"]
