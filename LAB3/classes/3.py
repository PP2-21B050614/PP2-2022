class Rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width

    def area(self):
        print(self.width*self.lenght)

d=Rectangle(4,5)
d.area()