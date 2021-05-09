FROM ubuntu:focal
ENV DEBIAN_FRONTEND=noninteractive

# gozebo configuration
RUN apt-get update
RUN apt-get install lsb-release gnupg2 curl -y
RUN curl -sSL http://get.gazebosim.org | sh
#RUN apt-get install gazebo11 -y 
#9
# ROS configuration
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | apt-key add -
RUN apt-get update
#melodic
#RUN apt-get install ros-melodic-ros-base -y
RUN apt-get install ros-noetic-desktop-base -y
#RUN apt-get install ros-melodic-gazebo-ros ros-melodic-gazebo-dev ros-melodic-gazebo-plugins -y
RUN apt-get install ros-noetic-gazebo-ros ros-noetic-gazebo-dev ros-noetic-gazebo-plugins -y
#RUN apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control -y
RUN apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control -y
#RUN apt-get install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential -y
RUN apt-get install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential -y
SHELL ["/bin/bash", "-c"]
#RUN source /opt/ros/melodic/setup.bash
RUN source /opt/ros/noetic/setup.bash

# MoveIt configuration
RUN rosdep init
RUN rosdep update

RUN apt update
RUN apt dist-upgrade -y
#RUN apt-get install ros-melodic-catkin python-catkin-tools -y
RUN apt-get install ros-noetic-catkin python3-catkin-tools -y
#RUN apt-get install ros-melodic-moveit -y
RUN apt-get install python3-wstool -y

WORKDIR /root/ws_moveit/src
RUN apt-get install python3-pip -y
RUN pip3 install osrf-pycommon
RUN apt-get install wget -y

RUN wstool init .
RUN wstool merge -t . https://raw.githubusercontent.com/ros-planning/moveit/master/moveit.rosinstall
COPY ./my_project ./my_project
RUN wstool remove  moveit_tutorials
RUN wstool update -t .
#RUN rosdep install -y --from-paths . --ignore-src --rosdistro melodic
RUN rosdep install -y --from-path . --ignore-src --rosdistro noetic
WORKDIR /root/ws_moveit
#RUN catkin config --extend /opt/ros/melodic --cmake-args -DCMAKE_BUILD_TYPE=Release
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
RUN apt-get install gdb ros-melodic*joint-trajectory-controller* -y

COPY robots/ /opt/ros/melodic/share/franka_description/robots/
RUN echo "source /root/ws_moveit/devel/setup.bash" >> ~/.bashrc
COPY entrypoint.sh entrypoint.sh
#ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT [ "./entrypoint.sh"]
