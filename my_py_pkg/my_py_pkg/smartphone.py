#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartphoneNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("smartphone") # MODIFY NAME
        self.subscriber_ = self.create_subscription(
            String,"robot_news", self.callback_robot_news, 10)
        self.get_logger().info("Smartphone has been started.")
   
    def callback_robot_news(self, msg: String):
        self.get_logger().info(msg.data) # msg.data is from the publisher

def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == " __main__ ":
    main()
    

