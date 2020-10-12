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


restaurant1 = Restaurant('Tanuki', 'asian')
restaurant2 = Restaurant('Fridys', 'american')
restaurant3 = Restaurant('Sbarro', 'italian')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.set_number_served(0)
restaurant2.set_number_served(0)

restaurant1.today_served()
restaurant2.today_served()

restaurant1.increment_number_served(22)
restaurant2.increment_number_served(44)

restaurant1.today_served()
restaurant2.today_served()
