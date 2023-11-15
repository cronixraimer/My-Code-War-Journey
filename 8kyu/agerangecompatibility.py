#age range compatibility equation
def dating_range(age):
    if age > 14:
        x = (age // 2) + 7
        y = (age - 7) * 2

    else:
        x = int(age - 0.10 * age)
        y = int(age + 0.10 * age)

    return f"{x}-{y}"

age = 35
result = dating_range(age)
print(result)
