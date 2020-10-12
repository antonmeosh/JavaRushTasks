# 7.1
car = input("Hello, what car do you want? ")
print(f"\nLet me see if I can find you a {car.title()}.")
# 7.2
persons = int(input("Сколько человек Вас будет? "))
if persons > 8:
    print("\n Надо подождать.")
else:
    print("\nСтол готов.")
# 7.3
number = int(input("Введите число: "))
if number % 10 == 0:
    print("Число кратно 10!")
else:
    print("Число не кратно 10!")
