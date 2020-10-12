#import making_car_function
#from making_car_function import make_car
# from making_car_function import make_car as mk
#import making_car_function as mkf
from making_car_function import *
# 8.12
def make_sandwiches(*toppings):
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")


make_sandwiches('cheese')
make_sandwiches('peperoni', 'cheese')
make_sandwiches('onion', 'turkey', 'olive')

# 8.14




car = make_car('subaru', 'outback', color='blue',
                             tow_package=True)
print(car)