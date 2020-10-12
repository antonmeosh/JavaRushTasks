# 7.4
prompt = "\nEnter toppings for you pizza:"
prompt += "\n(When you finished enter 'end'.) "
while True:
    topping = input(prompt)
    if topping == 'end':
        break
    else:
        print(f"{topping.title()} added in your pizza!")
# 7.5
prompt = "\nEnter you age for known ticket price"
prompt += "\nWhen you finish enter '00'. "
while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("\nFree enter!")
    elif 3 <= age < 12:
        print("\nTicket price is $10 for you!")
    elif 12 <= age:
        print("\nTicket price is $15 for you!")
    else:
        break
