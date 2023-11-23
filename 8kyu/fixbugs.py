def my_first_kata(a,b):
    if type(a) or type(b) == isdigit(): return a % b + b % a
    else:
        return False
a = 3
b = 5
result = my_first_kata(a, b)
print(result)
