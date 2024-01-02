import math

class Circle:
    def __init__ (center, radius):
        this.center = cente;
        this.radius = radius

class Point:
    def __init__ (x,y):
        this.x = x
        this.y = y


def circle_are(circle):
    return round(math.pi * circle.radius*2, 6)

center = Point(0, 0)
my_cicrle = Circle(center, 5)
area = circle_are(my_cicrle)
print(area)

#best solution
#return round(2* circle.radius * math.pi, 6)
