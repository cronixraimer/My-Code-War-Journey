def calculator(x,y,op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else: return 'unknown value'



x = int(input())
y = int(input())
op = input()
result = calculator(x, y, op)
print (result)
