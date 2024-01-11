def sea_sick(sea):
    changes = sum(1 for i in range(1, len(sea)) if sea[i] != sea[i-1])

    if changes > 0.2 * len(sea):
        return "Throw Up"

    else:
        return "No Problem"

sea_condtion = "~_~~__~~~"
result = sea_sick(sea_condtion)
print(result)
