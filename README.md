# ROS2 Beginner Smart Robot

## Description
A beginner ROS 2 project demonstrating:

- Publisher / Subscriber
- Service
- Launch files
- Basic obstacle avoidance

## Requirements
- ROS 2 Humble or newer
- TurtleBot3 simulation (recommended)

## Build Instructions

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone <repo_url>
cd ..
colcon build
source install/setup.bash

## Run

ros2 launch smart_robot smart_robot.launch.py

## Test Service

ros2 service call /robot_status std_srvs/srv/Trigger
