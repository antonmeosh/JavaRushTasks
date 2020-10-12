#6.7
people = {
    'iam': {
        'first_name': 'Anton',
        'last_name': 'Kapranov',
        'age': 33,
        'city': 'Moscow',
        },
    'ritaneodna': {
        'first_name': 'Margarita',
        'last_name': 'Kapranova',
        'age': 30,
        'city': 'Moscow',
        },
    }
for username, user_info in people.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = f"{user_info['city']}"
    age = f"{user_info['age']}"
    print(f"{full_name.title()}, {age} years old, live in {location.title()}")
