import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x  # calls the setter
        self.y = y  # calls the setter

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        self._y = value

    @property
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"


def main():
    p = Point(3, 4)

    print(p)
    print(p.x)
    print(p.y)
    print(p.distance_from_origin)
    
    # p.distance_from_origin = 100

    p.move(2, 1)
    print(p)

    p.x = 10
    print(p)
    
    p.x = "Hello"

# p.y = "hello"  # Raises TypeError
    
    
if __name__ == "__main__":
    main()