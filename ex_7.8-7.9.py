# 7.8
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'double cheese', 'pastrami',
                   'club', 'pastrami', 'blue cheese',
                   'chicken']
finished_sandwiches = []
print("Pastrami sandwich is over.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nI made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nThese sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} sandwich.")
