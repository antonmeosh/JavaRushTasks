motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('dukati')
print(motorcycles)
motorcycles.insert(2, 'bmw')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles.remove('bmw')
print(motorcycles)