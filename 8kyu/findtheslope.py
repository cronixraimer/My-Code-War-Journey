#After finishing this task I will better solution on this task
def find_slope(points):
    if points[2] - points[0] == 0:
        return "undefined"

    m = (points[3] - points[1]) / (points[2] - points[0])

    return int(m)

points = [10, 50, 30, 150]
result = find_slope(points)
print(result)
