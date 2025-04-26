#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts # used for accessing request and response

class AddTwoIntsServerNode(Node): 
    def __init__(self):
        super().__init__("add_two_ints_server") # node name
        self.server_ = self.create_service(AddTwoInts,"add_two_ints", self.callback_add_two_ints) # Topic Name
        self.get_logger().info("Add Teo Ints server has been started")


    def callback_add_two_ints(self, request:AddTwoInts.Request, response:AddTwoInts.Response): 
        response.sum = request.a + request.b  # when you type " ros2 interface show example_interfaces/srv/AddTwoInts " 
                                              # you will get -- Request -->  int64 a, int64 b and Response int64 sum
        self.get_logger().info(str(request.a) + " + " +
                               str(request.b) + " = " + str(response.sum))
        return response # Return is needed for response callback function "DO NOT FORGET"



def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
