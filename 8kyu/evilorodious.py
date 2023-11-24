def evil(n):
    count = bin(n).count('1')
    if count % 2 == 0:
        return f"It's Evil!"
    return f"It's Odious!"

n = 5
result = evil(n)
print(result)
