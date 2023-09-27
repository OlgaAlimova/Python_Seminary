# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с
# передачей параметров.

import logging
import argparse
class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            logging.error("Invalid rectangle dimensions. Length and width must be positive.")
            raise ValueError("Invalid rectangle dimensions. Length and width must be positive.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

def main():
    parser = argparse.ArgumentParser(description="Rectangle Calculator")
    parser.add_argument("--length", type=float, required=True, help="Length of the rectangle")
    parser.add_argument("--width", type=float, required=True, help="Width of the rectangle")

    args = parser.parse_args()

    try:
        rectangle = Rectangle(args.length, args.width)
        print(f"Area: {rectangle.area()}")
        print(f"Perimeter: {rectangle.perimeter()}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# Пример использования:
#
# python rectangle_cli.py --length 5 --width 3
