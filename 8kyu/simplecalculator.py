def calculator(x,y,op):
    try:
        x = int(x)
        y = int(y)

        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            return "unknown operation"
    except ValueError:
        return "unknown value"



x = int(input())
y = int(input())
op = input()
result = calculator(x, y, op)
print (result)
