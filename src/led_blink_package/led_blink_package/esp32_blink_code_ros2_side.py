#!usr/bin/env python3

import rclpy
from rclpy.node  import Node
from std_msgs.msg import Int32


class LedBlinkNode(Node):
    def __init__(self):
        super().__init__('Publish_data_for_blink_led')
        
        self.count = 0
        self.pub = self.create_publisher(Int32,"/blink_led",10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        msg = Int32()
        msg.data = self.count%2
        self.count += 1
        self.pub.publish(msg)
        self.get_logger().info("Published data for blinking LED: %d" % msg.data)
        
        
def main(args=None):
    rclpy.init(args=args)
    node = LedBlinkNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
        
if __name__=='__main__':
    main()
        
        