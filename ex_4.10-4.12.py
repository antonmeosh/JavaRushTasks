#4.10
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are:")
for player in players[:3]:
    print(player.title())
print("Three items from the middle of the list are:")
for player in players[1:4]:
    print(player.title())
print("The last three items in the list are:")
for player in players[-3:]:
    print(player.title())
#4.11-4.12
pizzas = ['pepperoni', 'margarita', '4 cheeses']
friend_pizzas = pizzas[:]
pizzas.append('suprim')
friend_pizzas.append('americana')
print("My favorite pizzas are:")
for pizza in pizzas[:]:
    print(pizza.title())
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas[:]:
    print(friend_pizza.title())

