def calc(x):
    #calculating total1 by converting to ascii character
    total1 = int(''.join(str(ord(char)) for char in x))

    #replacing last digits of my total1 to 1
    total2 = int(str(total1).replace('7', '1'))

    #difference between total1 and total2
    difference = sum(int(digit) for digit in str(total1)) - sum(int(digit) for digit in str(total2))

    return difference

input_string = 'aaaaaddddr'
result = calc(input_string)
print(result)
#liked solution total1 = ''.join(str(ord(char)) for char in x)
#total2 = total1.replace('7', '1')
#return sum(int(x) for x in total1) - sum(int(x) for x in total2)
