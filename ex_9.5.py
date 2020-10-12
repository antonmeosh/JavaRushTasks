class User:
    def __init__(self, first_name, last_name, age, location):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("\nUser info:")
        print(f"Name: {self.first} {self.last}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first}!")

    def increment_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Anton', 'Meosh', 33, 'Moscow')
user2 = User('Rita', 'Meoshka', 30, 'Pushkino')
user1.greet_user()
user2.greet_user()
user1.describe_user()
user2.describe_user()
user1.increment_attempts()
print(f"Login attempts = {user1.login_attempts}")
user1.increment_attempts()
print(f"Login attempts = {user1.login_attempts}")
user1.increment_attempts()
print(f"Login attempts = {user1.login_attempts}")
user1.increment_attempts()
print(f"Login attempts = {user1.login_attempts}")
user1.increment_attempts()
print(f"Login attempts = {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts = {user1.login_attempts}")
