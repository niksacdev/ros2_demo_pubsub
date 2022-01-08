from rclpy.node import Node
from std_msgs.msg import String


class DemoSubscriber(Node):
    """Subscriber type to create a subscriber and listen on a topic"""
    def __init__(self):
        """initialize the listener to subscribe to the desired topic"""
        super().__init__("demo_subscriber")
        self.subscription = self.create_subscription(String, 'demo_topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        """Callback for the listener on the topic"""
        self.get_logger().info(f"Message received {msg.data}")
