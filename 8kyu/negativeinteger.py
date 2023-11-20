#After finishing this code I will see better option of doing this task
def make_negative(number):
    if number > 0:
        x = number - (number * 2)
        return x
    elif number < 0:
        return number
    else:
        return 0
number = -4
result = make_negative(number)
print(result)
#best solution: return -abs(number)
