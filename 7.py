import math
class Figure:
    sides_count = 0

    def __init__(self, colors, *args):
        self.__color = list(colors)
        self.__sides = []
        if len(list(args)) == self.sides_count:
            self.__sides = list(args)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):

        if (isinstance(r,int) and isinstance(g,int) and isinstance(b,int) and
                0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return True
        else:
            return False

    def set_color(self,r ,g ,b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r,g,b]


    def __is_valid_sides(self, *args):
        self.valid_sides = True
        for i in args:
            if not(isinstance(i, int) and i >0):
                print(i)
                self.valid_sides = False
        if len(args) != self.sides_count:
            self.valid_sides = False
        return self.valid_sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
         return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)




class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        super().__init__(color, *args)
        super().get_sides()
        super().set_sides()
        self.__radius = len(self)/(2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius**2



class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        super().__init__(color,*args)
        super().get_sides()
        super().set_sides()

    def get_square(self):
        self.p = len(self)/2
        return (self.p*(self.p-self._Figure__sides[0])*(self.p-self._Figure__sides[1])*(self.p-self._Figure__sides[2]))**0.5


class Cube(Figure):
    sides_count = 1
    cube_side_count = 12
    def __init__(self, color, *args):
        super().__init__(color, *args)
        self.side = self._Figure__sides[0]
        for i in range(11):
            self._Figure__sides.append(self.side)
        super().get_sides()
        super().set_sides()

    def get_volume(self):
        return self._Figure__sides[0]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())