class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Shape have coordinate x={} and coordinate y={}'.format(self.x, self.y)


class Dot(Shape):
    def __init__(self, x=1, y=1):
        super().__init__(x, y)

    def __str__(self):
        return 'Dot have coordinate x={} and coordinate y={}'.format(self.x, self.y)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return 'Circle have coordinate x={} and coordinate y={}'.format(self.x, self.y)

    def check_dot_in_circle(self, dot):
        """
        https://ru.stackoverflow.com/questions/244030/%D0%9E%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%8C-%D0%BF%D0%BE%D0%BF%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%82%D0%BE%D1%87%D0%BA%D0%B8-%D0%B2-%D0%BA%D1%80%D1%83%D0%B3
        Вам можно воспользоваться следующим условием:
        (x - x0)^2 + (y - y0)^2 <= R^2
        Если условие выполняется, то точка находится внутри (или на окружности,
        в случае равенства левой и правой частей).
        Если не выполняется, то точка вне окружности.
        """
        if (dot.x - self.x) ** 2 + (dot.y - self.y) ** 2 <= self.radius:
            return True
        else:
            return False

dot1 = Dot(y=3)
print(dot1)

circle = Circle(5, 2, 10)  # точка вне окружности
circle2 = Circle(1, 1, 10)  # точка в окружности
dot = Dot()
print(Circle.check_dot_in_circle(circle, dot))
print(Circle.check_dot_in_circle(circle2, dot))
