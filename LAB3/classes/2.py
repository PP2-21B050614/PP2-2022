class Shape:
    x=0
    def area():
        print(0)
class Square:
    def __init__(self,lenght):
        self.lenght = lenght

    def area(self):
        print(self.lenght*self.lenght)

p=Shape
p.x=10
p.area()
d=Square(5)
d.area()