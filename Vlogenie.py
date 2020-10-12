aliens =[]
for alien_number in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow',
                 }
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
#Вывод первых 5 пришельцев
for alien in aliens[:5]:
    print(alien)
print("...")

#Вывод количества созданных пришельцев
print(f"Total number of aliens: {len(aliens)}")

print('#########################################################')
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
print(f"You ordered a {pizza['crust']} - crust pizza with the following "
      f"toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)