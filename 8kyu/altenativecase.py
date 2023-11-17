def to_alternating_case(string):
    result = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result

my_string = "HeLLo WorLd 123!"
result = to_alternating_case(my_string)
print(result)
#after submission I saw easiest way to do this tast
#return string.swapcase() swapcase just do all this what is done above
