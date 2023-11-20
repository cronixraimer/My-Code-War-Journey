import math
#After finishing this code I will see better option of doing this task
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_between_points(a, b):
    x1, y1 = a.x, a.y
    x2, y2 = b.x, b.y
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
# after submit I found best solution: return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
a = Point(1, 6)
b = Point(4, 2)

result = distance_between_points(a, b)
print(result)
