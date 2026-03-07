## 実行方法
1. Rvizの起動
```
$ ros2 launch vla_manipulator_moveit_config demo.launch.py
```

## moveitとso-101で同じ動きをさせる
1. 実機ドライバの起動
```
$ ros2 launch lerobot_controller so101_follower_controller.launch.py is_sim:=False usb_port:=/dev/ttyACM0

```
1. 姿形の配信
```
$ ros2 launch vla_manipulator_moveit_config rsp.launch.py
```
1. MoveItの起動
```
$ ros2 launch vla_manipulator_moveit_config move_group.launch.py
```
1. Rvizの起動
```
$ ros2 launch vla_manipulator_moveit_config moveit_rviz.launch.py
```
