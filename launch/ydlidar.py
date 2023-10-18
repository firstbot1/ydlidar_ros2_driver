from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # ydlidar 노드를 정의합니다
    ydlidar_node = Node(
        package='ydlidar_ros2_driver',
        executable='ydlidar_ros2_driver_node',
        name='ydlidar_ros2_driver_node',
        output='screen',
        respawn=True,  # 이것은 이전 ROS 버전에서 `restart_exit_handler`를 사용하는 것과 유사합니다.
    )

    # static tf publisher 노드를 정의합니다
    static_tf_publisher_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_tf_pub_laser',
        arguments=['0', '0', '0.02', '0', '0', '0', '1', 'base_link', 'laser_frame'],
    )

    return LaunchDescription([
        ydlidar_node,
        static_tf_publisher_node
    ])
