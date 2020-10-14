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


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(self, first_name, last_name, age)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ('разрешено добавлять сообщения',
                           'разрешено удалять пользователей',
                           'разрешено банить пользователей',
                           )

    def show_privileges(self):
        print(f"Admin have privileges: \n{self.privileges}")


admin = Admin('aaa', 'ddd', 'fff', 'sss')
admin.privileges.show_privileges()
