#!/usr/bin/env python3

import time

import rclpy
from rclpy.node import Node


class TimePrinter(Node):
    def __init__(self):
        super().__init__('time_printer')

        self.timer = self.create_timer(
            5.0,
            self.print_current_time
        )

        self.get_logger().info(
            'Узел time_printer запущен. '
            'Время будет выводиться каждые 5 секунд.'
        )

    def print_current_time(self):
        current_time = time.strftime(
            '%Y-%m-%d %H:%M:%S',
            time.localtime()
        )

        self.get_logger().info(
            f'Текущее время: {current_time}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = TimePrinter()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

