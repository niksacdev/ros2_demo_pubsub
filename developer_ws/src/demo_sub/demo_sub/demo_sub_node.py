from demo_sub import demo_subscriber
import rclpy


def main(args=None):
    """Execute the subscriber to ensure we are listening on the topic"""
    rclpy.init(args=args)
    _demo_subscriber = demo_subscriber.DemoSubscriber()
    rclpy.spin(_demo_subscriber)

    # close gracefully
    _demo_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
