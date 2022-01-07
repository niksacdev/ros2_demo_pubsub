from rclpy.node import Node
from std_msgs.msg import String


class DemoPublisher(Node):
    """Provides a simple publisher for ROS 2 Nodes to send messages"""
    def __init__(self):
        """Create the Node Publisher and set an initial timer
        """
        super().__init__('Minimal_Publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    def timer_callback(self):
        """Callback for the timer function to print the message"""
        msg = String()
        msg.data = f"Hello World: {self.i}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.i += 1
