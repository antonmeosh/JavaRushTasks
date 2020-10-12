dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250        TypeError: 'tuple' object does not support item assignment
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
