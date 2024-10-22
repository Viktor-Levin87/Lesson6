from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        self.__sides = []
        self.set_sides(*sides)

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 256 and 0 <= g <= 256 and 0 <= b <= 256:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if i > 0 and isinstance(i, int):
                    continue
                else:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = [*sides]
        elif len(sides) == 1 and self.sides_count == 12 and sides[0] > 0:
            self.__sides = []
            for i in range(12):
                self.__sides.append(*sides)
        elif self.__sides != []:
            pass
        else:
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(1)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = (self._Figure__sides[0] / (2 * pi))

    def get_square(self):
        self.__radius = (self._Figure__sides[0] / (2 * pi))
        b = pi * (self.__radius ** 2)
        return b


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        v = self._Figure__sides[0] ** 3
        return v


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = 0.5 * (self._Figure__sides[0] + self._Figure__sides[1] + self._Figure__sides[2])
        s = (p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2])) ** 0.5
        return s


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


# triangle1 = Triangle((5, 11, 4), 3, 3, 5)
# triangle1.set_sides(3, 7)
# print(triangle1.get_sides())
# print(triangle1.get_square())
