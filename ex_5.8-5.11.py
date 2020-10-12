#5.8-5.9
users = ['user1', 'user2', 'user3', 'user4', 'admin']
#users = []
if users:
    for user in users:
        if user == 'admin':
            print(f"Hello, {user}, would you like to see a status report?")
        else:
            print(f"Hello, {user}, thank you for logging in again")
else:
    print("We need to ind some users!")

#5.10
current_users = ['name1', 'name2', 'name3', 'name4', 'name5']
new_users = ['naMe5', 'name6', 'name7', 'name8', 'name9', 'Name1']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry, this name - "
              f"{new_user.title()} is used. Try again with another name.")
    else:
        print(f"You can use this name - {new_user.title()}.")
#5.11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f"1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")