from launch import LaunchDescription
from launch_ros.actions import Node
from so_arm100_description.launch_utils import MoveItConfigs
import pathlib

def generate_launch_description():
    from ament_index_python.packages import get_package_share_directory
    import os
    import yaml

    # Your normal MoveItConfigs usage:
    from so_arm100_description.launch_utils import MoveItConfigs
    moveit_configs = MoveItConfigs()
    moveit_params = moveit_configs.to_dict()

    # Merge in moveit_controllers.yaml
    config_file = os.path.join(
        get_package_share_directory('so_arm100_moveit_config'),
        'config',
        'moveit_controllers.yaml'
    )
    with open(config_file, 'r') as f:
        controller_yaml = yaml.safe_load(f)
    moveit_params.update(controller_yaml)

    return LaunchDescription([
        Node(
            package='moveit_ros_move_group',
            executable='move_group',
            parameters=[moveit_params],
            output='screen',
        ),
    ])


