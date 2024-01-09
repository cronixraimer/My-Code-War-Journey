def elevator(left, right, call):
    distance_left = abs(left - call)
    distance_right = abs(right - call)

    if distance_left < distance_right:
        return "left"
    else:
        return "right"

result = elevator(0, 2, 1)
print(result)

#I liked this code
#return "left" if abs(call - left) < abs(call -right) else "right"
#used same logic but it was in one line solution I would not missed top first one solution by users are done
