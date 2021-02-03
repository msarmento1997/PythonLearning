fruit = {'orange': 'a sweet, orange, citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a small, sweet fruit growing in bunches',
         'lime': 'a sour, green citrus fruit',
         'grape': 'a small, sweet fruit used to make wine'}

print(fruit)

veg = {'cabbage': "every child's favourite",
       'sprouts': 'mmhm, lovely',
       'spinach': 'can i have some more fruit, please'}
# fruit.update(veg)
print(veg)
veg.update(fruit)  # adds the fruit dictionary to the veg dictionary
print(veg)

print(fruit.update(veg))  # prints none since it doesn't return anything
print(fruit)
print()

nice_and_nasty = fruit.copy()  # creates a new dictionary that contains a copy of fruit and veg
nice_and_nasty.update(veg)
print(nice_and_nasty)
