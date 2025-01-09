#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Daichi Hirose
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil  # バッテリー情報を取得するためのライブラリ

class BatteryTalker(Node):
    def __init__(self):
        super().__init__('battery_talker')
        self.publisher_ = self.create_publisher(String, 'battery_status', 10)
        self.timer = self.create_timer(1.0, self.publish_battery_percentage)  # 1秒ごとにバッテリー情報を送信

    def publish_battery_percentage(self):
        battery = psutil.sensors_battery()
        if battery is not None:
            status = f"{battery.percent}%"  # バッテリー残量
        else:
            status = "Battery information not available"
        msg = String()
        msg.data = status
        self.publisher_.publish(msg)  # トピックに送信

def main(args=None):
    rclpy.init(args=args)
    node = BatteryTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

