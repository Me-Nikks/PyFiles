import math

class Shape:
    def __init__(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius**2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.__side = side

    def get_area(self):
        return self.__side**2

    def get_perimeter(self):
        return 4 * self.__side

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_area(self):
       
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def get_perimeter(self):
        return self.__side1 + self.__side2 + self.__side3


circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 5)
triangle = Triangle(3, 4, 5)

print(f"Area of the circle: {circle.get_area():.2f}, Perimeter: {circle.get_perimeter():.2f}")
print(f"Area of the square: {square.get_area()}, Perimeter: {square.get_perimeter()}")
print(f"Area of the rectangle: {rectangle.get_area()}, Perimeter: {rectangle.get_perimeter()}")
print(f"Area of the triangle: {triangle.get_area():.2f}, Perimeter: {triangle.get_perimeter()}")
