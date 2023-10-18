from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

import os

def generate_launch_description():
    share_dir = get_package_share_directory('ydlidar_ros2_driver')
    parameter_file = LaunchConfiguration('params_file')

    params_declare = DeclareLaunchArgument('params_file',
                                           default_value=os.path.join(
                                               share_dir, 'params', 'ydlidar.yaml'),
                                           description='FPath to the ROS2 parameters file to use.')

    ydlidar_node = Node(
        package='ydlidar_ros2_driver',
        executable='ydlidar_ros2_driver_node',
        name='ydlidar_ros2_driver_node',
        parameters=[parameter_file],
        namespace='/',
        output='screen'
    )

    cartographer_node = Node(
        package='cartographer_ros',
        executable='cartographer_node',
        parameters=[
            {'use_sim_time': True},
            os.path.join(share_dir, 'config', 'cartographer', 'your_cartographer_config.lua')
        ],
        remappings=[
            ('/scan', '/ydlidar_ros2_driver_node/scan')
        ],
        output='screen'
    )

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(share_dir, 'rviz', 'your_rviz_config.rviz')]
    )


    return LaunchDescription([
        params_declare,
        ydlidar_node,
        cartographer_node
    ])
