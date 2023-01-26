
"""
Launches low level go controls for the go1 with visualization in rviz.
"""

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, Shutdown, SetLaunchConfiguration, IncludeLaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch.conditions import LaunchConfigurationEquals
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
     return LaunchDescription([

          DeclareLaunchArgument(name='fixed_frame', default_value='base_footprint',
                                description='Fixed frame for RVIZ'),

          IncludeLaunchDescription(
               PythonLaunchDescriptionSource(
                    PathJoinSubstitution([FindPackageShare('go1_description'),
                                                           'launch',
                                                           'visualize.launch.py'])),
                    launch_arguments=[
                         ('use_jsp', 'none'),
                         ('fixed_frame', LaunchConfiguration('fixed_frame')),
                         ('enable_base_footprint', 'true'),
                    ]),

          IncludeLaunchDescription(
               PythonLaunchDescriptionSource(
                    PathJoinSubstitution([FindPackageShare('unitree_legged_real'),
                                                           'launch',
                                                           'high.launch.py'])))
    ])