class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}. It is {self.cuisine} food.")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is now open.")


restaurant1 = Restaurant('Tanuki', 'asian')
restaurant2 = Restaurant('Fridys', 'american')
restaurant3 = Restaurant('Sbarro', 'italian')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, location):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print("\nUser info:")
        print(f"Name: {self.first} {self.last}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first}!")


user1 = User('Anton', 'Meosh', 33, 'Moscow')
user2 = User('Rita', 'Meoshka', 30, 'Pushkino')
user1.greet_user()
user2.greet_user()
user1.describe_user()
user2.describe_user()
