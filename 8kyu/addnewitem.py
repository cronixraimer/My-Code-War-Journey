def add_extra(list_of_numbers):
new_item = None
new_list = list_of_numbers.copy()
new_list.append(new_item)
return new_list

quiver = [1, 2, 3]
result = add_extra(quiver)
print(result)
