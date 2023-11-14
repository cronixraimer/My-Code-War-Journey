def findNeedle(haystack):
    for i, item in enumerate(haystack):
        if item == "needle":
            return f"found the needle at position {i}"
    return "needle not found in the haystack"
user_input = input()
haystack = user_input.split(", ")
result = findNeedle(haystack)
print(result)
