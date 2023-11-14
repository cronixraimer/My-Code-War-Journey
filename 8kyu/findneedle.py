#very taff case when online platfor provides you test case when you trying to submit all code my platform
#was waiting only subclass to put piece of code into test case 
def findNeedle(haystack):
    for i, item in enumerate(haystack):
        if item == "needle":
            return f"found the needle at position {i}"
    return "needle not found in the haystack"
user_input = input()
haystack = user_input.split(", ")
result = findNeedle(haystack)
print(result)
