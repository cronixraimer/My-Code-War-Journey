#After finishing this task I will better solution on this task
import re
def get_number_from_string(s):
    pattern = re.findall(r'\d+', s)
    cleaned_number = ''.join(pattern)

    if cleaned_number:
        return int(cleaned_number)
    else:
        return None

s = "$100 000 000"
result = get_number_from_string(s)
print(result)
#best solution : int(''.join(num for num in s if num.digit()))
