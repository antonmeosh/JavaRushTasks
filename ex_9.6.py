class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}. It is {self.cuisine} food.")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is now open.")

    def today_served(self):
        print(f"{self.name} today served {self.number_served} people.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, new_served):
        self.number_served = new_served


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name):
        super().__init__(self, restaurant_name)
        self.name = restaurant_name
        self.flavors = None

    def show_flavors(self):
        print(f"{self.flavors}")


iceCream = IceCreamStand("Basking Robins",)
iceCream.flavors = ('cherry', 'chocolate', 'strawberry', 'raspberry')
iceCream.describe_restaurant()
iceCream.show_flavors()
