class Area:

    def __init__(self):
        self.__side = 5

    def area(self):
        print("Area of the square is: {}".format(self.__side))

    def setSide(self, Side):
        self.__side = Side

c = Area()
c.area()

c.__side = 10
c.area()

c.__setSide(10)
c.area()