def make_pizza(size, *toppings):
    """Вывод списка заказаных топингов."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")
