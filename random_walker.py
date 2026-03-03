import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class RandomWalker(Node):

    def __init__(self):
        super().__init__('random_walker')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(2.0, self.move)

    def move(self):
        twist = Twist()
        twist.linear.x = random.uniform(0.0, 0.3)
        twist.angular.z = random.uniform(-1.0, 1.0)
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = RandomWalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
