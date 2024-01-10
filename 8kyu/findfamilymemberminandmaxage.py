def diffenrence_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))

result = diffenrence_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88])
print(result)
