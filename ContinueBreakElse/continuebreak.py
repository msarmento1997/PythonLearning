# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         continue
#     print("Buy " + item)

meal = ['egg', 'bacon', 'toast', 'sausages']
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
if nasty_food_item:
    print("Can't I have anything without spam in it")
else:
    print("I'll have a plate of that please")

for i in range (20):
    print(i, end= ' ')