def partition(arr, classifier_method):
    # Write your solution
    first_list = [item for item in arr if classifier_method(item)]
    second_list = [item for item in arr if not classifier_method(item)]

    return first_list, second_list

animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
result = partition(animals, lambda x: len(x) == 3)
print(result)
