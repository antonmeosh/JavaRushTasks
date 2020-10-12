def greet_user(username):
    """Выводит простое приветствие."""
    print(f"Hello, {username.title()}!")

# greet_user('alice')
# greet_user('olivia')

def favorite_book(book_name):
    """Выводит любимую книгу"""
    print(f"One of my favorite book is {book_name.title()}.")

# favorite_book('Lord of the rings')
# favorite_book("Alice in Wonderland")

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Бесконечный цикл!!!


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
