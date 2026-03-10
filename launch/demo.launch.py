from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    # 1. 引数の設定
    use_sim = LaunchConfiguration("use_sim")
    
    # 2. XACROに引数を渡すようにビルド
    moveit_config = (
        MoveItConfigsBuilder("so101_new_calib", package_name="vla_manipulator_moveit_config")
        .robot_description(mappings={"use_sim": use_sim}) # ここでスイッチを渡す
        .to_moveit_configs()
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "use_sim",
            default_value="true",
            description="Trueならシミュレーション、Falseなら実機を動かします"
        ),
        generate_demo_launch(moveit_config),
    ])