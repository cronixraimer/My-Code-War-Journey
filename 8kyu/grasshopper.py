def combat(health, damage):
    res = health - damage
    if res > 0:
        return res
    else:
        return 0

result = combat(100, 5)
print(result)

#return max(0, health - damage)
#this one way too easy
