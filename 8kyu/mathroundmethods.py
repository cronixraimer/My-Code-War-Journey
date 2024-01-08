import math

def roundIT(n):
    left_digits, right_digits = str(n).split('.')

    if len(left_digits) < len(right_digits):
        #decicam point for the left side (ceil)
        return math.ceil(n)

    elif len(left_digits) > len(right_digits):
        #decimal for the right side (floor)
        return math.floor(n)

    else:
        return round(n)

print(roundIT(3.45))
print(roundIT(34.5))
print(roundIT(34.56))
