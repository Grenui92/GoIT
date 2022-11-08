class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 1:
            self.coordinates.y = value
        elif index == 0:
            self.coordinates.x = value

    def __getitem__(self, index):
        if index == 1:
            print("ssss")
        elif index == 0:
            print("qqqqq")


asd = Vector(Point(1, 10))
asd[5] = 11
print(type(asd.coordinates))
print(asd[1])