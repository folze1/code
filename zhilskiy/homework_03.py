import math

class Figure2D:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def mirror_point(self, point):
        pass

    def mirror_line(self, point1, point2):
        pass

    def belongs_point(self, point):
        pass

class Point2D(Figure2D):
    def __init__(self, name, x, y):
        super().__init__(name)
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name}: Точка({self.x}, {self.y})"

    def mirror_point(self, point):
        return Point2D(f"{self.name}_отражённая", 2 * point.x - self.x, 2 * point.y - self.y)

    def mirror_line(self, point1, point2):
        a, b, c = point2.y - point1.y, point1.x - point2.x, point2.x * point1.y - point1.x * point2.y
        x, y = self.x, self.y
        x_mirror = (b * (b * x - a * y) - a * c) / (a**2 + b**2)
        y_mirror = (a * (a * y - b * x) - b * c) / (a**2 + b**2)
        return Point2D(f"{self.name}_отражённая", x_mirror, y_mirror)

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y

class Segment2D(Figure2D):
    def __init__(self, name, start_point, end_point):
        super().__init__(name)
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        return math.sqrt((self.end_point.x - self.start_point.x)**2 + (self.end_point.y - self.start_point.y)**2)

    def __str__(self):
        return f"{self.name}: Отрезок от {self.start_point} до {self.end_point} (Длина: {self.length()})"

    def mirror_point(self, point):
        start_mirror = self.start_point.mirror_point(point)
        end_mirror = self.end_point.mirror_point(point)
        return Segment2D(f"{self.name}_отражённый", start_mirror, end_mirror)

    def mirror_line(self, point1, point2):
        start_mirror = self.start_point.mirror_line(point1, point2)
        end_mirror = self.end_point.mirror_line(point1, point2)
        return Segment2D(f"{self.name}_отражённый", start_mirror, end_mirror)

    def belongs_point(self, point):
        x_min = min(self.start_point.x, self.end_point.x)
        x_max = max(self.start_point.x, self.end_point.x)
        y_min = min(self.start_point.y, self.end_point.y)
        y_max = max(self.start_point.y, self.end_point.y)
        return x_min <= point.x <= x_max and y_min <= point.y <= y_max

class Triangle2D(Figure2D):
    def __init__(self, name, vertex1, vertex2, vertex3):
        super().__init__(name)
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3

    def area(self):
        return 0.5 * abs((self.vertex1.x * (self.vertex2.y - self.vertex3.y) +
                          self.vertex2.x * (self.vertex3.y - self.vertex1.y) +
                          self.vertex3.x * (self.vertex1.y - self.vertex2.y)))

    def perimeter(self):
        side1 = math.sqrt((self.vertex2.x - self.vertex1.x)**2 + (self.vertex2.y - self.vertex1.y)**2)
        side2 = math.sqrt((self.vertex3.x - self.vertex2.x)**2 + (self.vertex3.y - self.vertex2.y)**2)
        side3 = math.sqrt((self.vertex1.x - self.vertex3.x)**2 + (self.vertex1.y - self.vertex3.y)**2)
        return side1 + side2 + side3

    def __str__(self):
        return f"{self.name}: Треугольник с вершинами {self.vertex1}, {self.vertex2}, {self.vertex3} (Площадь: {self.area()}, Периметр: {self.perimeter()})"

    def mirror_point(self, point):
        vertex1_mirror = self.vertex1.mirror_point(point)
        vertex2_mirror = self.vertex2.mirror_point(point)
        vertex3_mirror = self.vertex3.mirror_point(point)
        return Triangle2D(f"{self.name}_отражённый", vertex1_mirror, vertex2_mirror, vertex3_mirror)

    def mirror_line(self, point1, point2):
        vertex1_mirror = self.vertex1.mirror_line(point1, point2)
        vertex2_mirror = self.vertex2.mirror_line(point1, point2)
        vertex3_mirror = self.vertex3.mirror_line(point1, point2)
        return Triangle2D(f"{self.name}_отражённый", vertex1_mirror, vertex2_mirror, vertex3_mirror)

    def belongs_point(self, point):
        area1 = Triangle2D(point.name, self.vertex1, self.vertex2, point).area()
        area2 = Triangle2D(point.name, self.vertex2, self.vertex3, point).area()
        area3 = Triangle2D(point.name, self.vertex3, self.vertex1, point).area()
        total_area = self.area()
        return math.isclose(area1 + area2 + area3, total_area)
