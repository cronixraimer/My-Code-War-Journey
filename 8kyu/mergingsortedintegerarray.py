#After finishing this code I will see better option of doing this task
#I did my best to get solution clear and on easy way
def merge_arrays(first, second):
    merged_result = sorted(set(first).union(second))
    return merged_result

#here is best result after submission return sorted(set(first + second))
first = [1, 2, 3]
second = [4, 6, 5]
result = merge_arrays(first, second)
print(result)
