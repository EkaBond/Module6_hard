import math

class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides, filled):
        self.__color = color
        self.__sides = sides
        self.filled = False

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = r,g,b

    @staticmethod
    def __is_valid_sides(self, *args):
        for side in args:
            if not isinstance(side, int) or side<=0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.__sides):
            new_list = []
            for side in new_sides:
                if self.__is_valid_sides(side):
                    new_list.append(side)
            self.__sides = new_list


# *******************************************************************************************

class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], l, filled=False):
        super().__init__(color, l, filled=filled)
        self.__radius = l / (2 * math.pi)

    def get_square(self):
        return self.__radius ** 2 * math.pi


class Traingle(Figure):
    sides_count = 3

    def __init__(self, color: tuple[int, int, int], *sides, filled=False):
        super().__init__(color, *sides, filled=filled)

    def get_square(self):
        p = len(self) / 2
        s = (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5
        return s


class Cube(Traingle):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], a, filled = False):
        sides = [a] * self.sides_count
        super().__init__(color, *sides, filled =filled)

    def get_volume(self):
        v = self.get_sides()[0] ** 3
        return v



circlel = Circle((200, 200, 100), 10,True)
cubel = Cube((222, 35, 130), 6)

circlel.set_color(55, 66, 77)
print(circlel.get_color())

cubel.set_color(300,70,15)
print(cubel.get_color())

cubel.set_sides(5, 3, 12, 4, 5)
print(cubel.get_sides())
circlel.set_sides(15)
print(circlel.get_sides())


print(len(circlel))

print(cubel.get_volume())

