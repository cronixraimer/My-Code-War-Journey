def add(n):
    def add_to_number(x):
        return x + n
    return add_to_number

add_one = add(1)
result_one = add_one(3)
print(result_one)

add_three = add(3)
result_three = add_three(3)
print(result_three)

#liked solution return lambda x: x + n  
