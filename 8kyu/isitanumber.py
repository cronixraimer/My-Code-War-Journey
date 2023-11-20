#After finishing this code I will see better option of doing this task
def is_digit(s):
    try:
        float_value = float(s)
        return True

    except:
        return False

s = "-3,14"
result = is_digit(s)
print(result)
#all solution was look like mine with a bit different path mostly it was done with try and except
