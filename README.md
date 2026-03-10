# 実行方法

## moveitとso-101で同じ動きをさせる
- デジタルツインさせるコマンド
```
$ sudo chmod 666 /dev/serial/by-id/usb-1a86_USB_Single_Serial_5AF7133194-if00

```
```
$ ros2 launch vla_manipulator_moveit_config demo.launch.py hardware_type:=real

```

- pcとシミュレーションだけで確認したい場合
```
$ ros2 launch vla_manipulator_sim spawn_robot_gazebo.launch.py

```

