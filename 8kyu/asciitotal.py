def uni_total(s):
    ascii_value = [ord(char) for char in s]
    return sum(ascii_value)
s = input()
ascii_value = uni_total(s)
print(ascii_value)
