def find_average(nums):
    if len(nums) > 0:
        x = sum(nums) / len(nums)
        return x
    return 0

nums = [1, 2, 4, 5]
result = find_average(nums)
print(result)
