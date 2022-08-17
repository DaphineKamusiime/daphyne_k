import math
class shape:
    def __init__(self):
        print("shape constructor")
    def area(self):
        print("Area of shape")
    def perimeter(self):
        print("perimeter of shape")
class circle(shape):
    def __init__(self):
        shape.__init__(self)#calling parent
        self.radius=r
        print("circle constuctor ")
    def are(self):
        print("area= ",3.142*self.radius*self.radius)
    c=circle(5)
    c.area()