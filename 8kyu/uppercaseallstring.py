#After finishing this code I will see better option of doing this task
def is_uppercase(inp):
    return not any(char.islower() for char in inp)

my_string = "#!$&"
result = is_uppercase(my_string)
print(result)
# best solution return inp.upper() == inp mine still good but dont think it is best solution
