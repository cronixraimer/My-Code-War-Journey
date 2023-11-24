def starting_mark(height):
    a = (1.22, 8.27)
    b = (2.13, 11.85)

    starting_point = a[1] + (height - a[0]) * (b[1] - a[1]) / (b[0] - a[0])

    return round(starting_point, 2)

height = 1.52
result = starting_mark(height)
print(result)
#linear equation calculation points got from description as min 1.22, 8.27 and max 2.13, 11.85 
