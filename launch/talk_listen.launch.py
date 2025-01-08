#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Daichi Hirose
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    battery_talker = launch_ros.actions.Node(
        package='mypkg',  # パッケージの名前を指定
        executable='battery_talker',  # 実行するファイルの指定
    )
    battery_listener = launch_ros.actions.Node(
        package='mypkg',
        executable='battery_listener',
        output='screen',  # ログを端末に出すための設定
    )
    return launch.LaunchDescription([battery_talker, battery_listener])
