def multiply(n):
    x = str(abs(n))
    length = len(x)
    return n*(5 ** length)

n = int(input())
result = multiply(n)
print(result)

# best solution : return n **5*len(str(abs(n)))
