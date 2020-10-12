#5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
#5.2
car = 'bmw'
print(car == 'bmw')
print(car == 'BMW')
age = 33
print(age <= 18)
print(age >= 18)
banned_users = ['andrey', 'marat', 'sergey', 'yaroslav']
user = 'andrey'
if user in banned_users:
    print("yes, he is banned")
user = 'anton'
if user not in banned_users:
    print("user is not banned")