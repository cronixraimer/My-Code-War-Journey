#After finishing this task I will better solution on this task
def fuel_price(liters, price_per_liter):
    discount = 0
    if liters >= 10:
        discount = 0.25
    elif liters >= 8:
        discount = 0.20
    elif liters >= 6:
        discount = 0.15
    elif liters >= 4:
        discount = 0.10
    elif liters >= 2:
        discount = 0.05

    total_cost = liters * (price_per_liter - discount)

    return round(total_cost, 2)

liters = int(input())
price_per_liter = float(input())
result = fuel_price(liters, price_per_liter)
print(result)
#best solution : discount int(min(litres, 10) / 2) * 5 / 100
# return round((price_per_liter - discount) * litres, 2)
