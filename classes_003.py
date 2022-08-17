import math
class Circle:
    pi = math.pi
    # Circle instantiated with a radius (default is 2)
    def __init__(self, radius=2):
        self.radius = radius 
        self.area = radius * radius * Circle.pi
    # resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi # work with an existing Circle object that does have its own pi attribute
    # getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2
c = Circle()
print("Radius is: ",c.radius)
print("Area is: ",round(c.area,4))
print("Circumference is: ",round(c.getCircumference(),4))