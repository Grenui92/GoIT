class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__x = x
        self.__y = y

    def x(self):
        return self.__x

    def set_x(self, new_value):
        self.__x = new_value

    def y(self):
        return self.__y

    def set_y(self, new_value):
        self.__y = new_value


asd = Point(5, 10)
print(asd.x())
print(asd.y())