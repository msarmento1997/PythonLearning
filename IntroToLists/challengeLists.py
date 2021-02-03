menu = []
menu.append(['egg', 'spam', 'sausage'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

print(menu)

# for meal in menu:
#     if not 'spam' in meal:
#         print(meal)

for meal in menu:
    if 'spam' not in meal:
        for food_item in meal:
            print(food_item)
