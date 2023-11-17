def even_or_odd(number):
    if number % 2 == 0:
        return f"Even"
    else:
        return f"Odd"


number = int(input())
result = even_or_odd(number)
print(result)
