#the feast of many beasts
def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False

beast = ["brown bear"]
dish = ["bear claw"]
result = feast(beast, dish)
print(result)
