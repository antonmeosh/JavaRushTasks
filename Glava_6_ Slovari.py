alien_0 = {
    'color': 'green',
    'points': 5,
    'x_position': 0,
    'y_position': 25,
    }
new_points = alien_0['points']
#print(f"You just earned {new_points} points!")
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}. ")
#
alien_0['speed'] = 'medium'
print(f"Original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
print(alien_0)
del alien_0['points']
print(alien_0)
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
