#After finishing this task I will better solution on this task
import re
def validate_code(code):
    pattern = r'^[123]'
    return re.match(pattern, str(code)) is not None

code = 9453
result = validate_code(code)
print(result)
#best solution return str(code).startswith(('1', '2', '3'))
