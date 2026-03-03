import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class StatusService(Node):

    def __init__(self):
        super().__init__('status_service')
        self.srv = self.create_service(
            Trigger,
            'robot_status',
            self.status_callback
        )

    def status_callback(self, request, response):
        response.success = True
        response.message = "Robot is running normally."
        return response

def main(args=None):
    rclpy.init(args=args)
    node = StatusService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
