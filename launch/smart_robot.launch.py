from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='smart_robot',
            executable='obstacle_avoidance',
            name='obstacle_avoidance_node'
        ),
        Node(
            package='smart_robot',
            executable='status_service',
            name='status_service_node'
        ),
    ])
