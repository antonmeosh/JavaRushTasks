sweden_table = ('chicken', 'potato', 'rice', 'sandwich', 'burger', 'pizza')
print("Our menu is:")
for menu in sweden_table:
    print(menu.title())
# sweden_table[3] = 'cheese'         TypeError: 'tuple' object does not support
# item assignment


sweden_table = ('chicken', 'cheese', 'ham', 'sushi' 'rice', 'sandwich',
                'burger', 'pizza')
print("\nOur new menu is:")
for menu in sweden_table:
    print(menu.title())
