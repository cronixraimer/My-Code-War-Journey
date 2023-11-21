#After finishing this task I will better solution on this task
from urllib.parse import quote

def generate_link(user):
    #Base Link
    main_link = 'http://www.codewars.com/users/'

    #encoding space or other charaters in user input
    encoded_user_input = quote(user)

    #Concatenate the base link and encoded user input
    final_link = main_link + encoded_user_input

    return final_link

user = input()
result = generate_link(user)
print(result)
#best solution : just import urllib and return 'http://www.codewars.com/users/' + urllib.quote(user)
#best solution is better then main as in the proccess of huger data will work faster  
