#After finishing this task I will better solution on this task
def validate(username, password):
    database = Database()
    if "||" in password or "//" in password:
        return "Wrong username or password!"
    return database.login(username, password);

#this task was shit for me as I pass test case easily but some random case and database which was provided was pissing of me
#best solution was database = Database() return database.login(username, password)
#my version still good I like my version more
username = input()
password = input()
result = validate(username, password)
print(result)
