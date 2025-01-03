import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

# ROS 2ノードの初期化
rclpy.init()

# ノード作成
node = Node("listener")

# コールバック関数
def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

# メイン関数
def main():
    node.create_subscription(Int16, "countup", cb, 10)  # サブスクリプション作成
    rclpy.spin(node)  # ノードを実行（無限ループ）
