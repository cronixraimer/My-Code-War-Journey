def next_item(xs, item):
    found = False

    for i in xs:
        if found:
            return i

        if i == item:
            found = True
    return None

sequence = [1, 2, 3, 4, 5, 3, 6, 7]
specified_item = 3
result = next_item(sequence, specified_item)
print(result)

#I liked this solution
#it = iter(xs)
#for i in it:
#if i == item:
#break
#return next(it, None)
