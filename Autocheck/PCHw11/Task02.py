class Point:
    def __init__(self):
        self.__x = None
        self.__y = None


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


asd = Point()
asd.y = 11