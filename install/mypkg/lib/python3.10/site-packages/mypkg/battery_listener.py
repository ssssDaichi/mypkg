#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Daichi Hirose
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BatteryListener(Node):
    def __init__(self):
        super().__init__('battery_listener')
        # battery_statusトピックのサブスクライバーを作成
        self.subscription = self.create_subscription(
            String,
            'battery_status',  # トピック名
            self.listener_callback,  # コールバック関数
            10  # キューサイズ
        )
        self.subscription  # サブスクリプションを保持するために必要

    def listener_callback(self, msg):
        # トピックから受信したメッセージを表示
        self.get_logger().info(f'Received: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
