from launch import LaunchDescription
from launch_ros.actions import Node
from so_arm100_description.launch_utils import MoveItConfigs
import pathlib

def generate_launch_description():
    from ament_index_python.packages import get_package_share_directory
    import os
    import yaml

    # (1) Load your standard MoveIt configs
    from so_arm100_description.launch_utils import MoveItConfigs
    moveit_configs = MoveItConfigs()
    moveit_params = moveit_configs.to_dict()

    # (2) Load moveit_controllers.yaml
    controllers_file = os.path.join(
        get_package_share_directory("so_arm100_moveit_config"),
        "config",
        "moveit_controllers.yaml"
    )
    with open(controllers_file, "r") as f:
        controllers_yaml = yaml.safe_load(f)

    # (3) Merge them
    moveit_params.update(controllers_yaml)

    # (4) Start move_group with these merged params
    return LaunchDescription([
        Node(
            package="moveit_ros_move_group",
            executable="move_group",
            output="screen",
            parameters=[moveit_params],
        ),
    ])

