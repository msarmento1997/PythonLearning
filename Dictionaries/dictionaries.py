fruit = {'orange': 'a sweet, orange, citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a small, sweet fruit growing in bunches',
         'lime': 'a sour, green citrus fruit',
         'grape': 'a small, sweet fruit used to make wine'}
# print(fruit)
# print(fruit['lemon'])
#
# # add item into a dictionary
# fruit['pear'] = 'an odd shaped apple'
# print(fruit)
# fruit['lime'] = 'great with tequila'
# print(fruit)
#
# # delete a key from dictionary, del fruit would delete the whole dictionary
# del fruit['lemon']
# print(fruit)
#
# # clears the contents of the dictionary
# fruit.clear()

# any time you write over the key of a dictionary it will use the most recent updated

# print(fruit)
# while True:
#     dict_key = input('Please enter a fruit: ')
#     if dict_key == 'quit':
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

    # alternative method
    # description = fruit.get(dict_key, "We don't have " + dict_key)
    # print(description)

# for snack in fruit:
#     print(snack + " is " + fruit[snack])

# alternative method
# ordered_key = list(fruit.keys())
# ordered_key.sort()

# can sort and get the list of keys in one line

# ordered_key = sorted(list(fruit.keys()))
# for f in ordered_key:
#     print(f + ' - ' + fruit[f])

# does the same thing as the other methods above, treats fruit.keys() as a sequence which allows us to sort it
# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# used to get the values after the keys in the dictionary
# for val in fruit.values():
#     print(val)
#
# print('=' * 50)
#
# for key in fruit:
#     print(fruit[key])

# fruit_keys = fruit.keys()
# print(fruit_keys)
# # print(fruit.keys())
# # print(fruit.values())
#
# fruit['tomato'] = 'not nice with ice cream'
# print(fruit_keys)

# pass a dictionary to a tuple
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + ' is ' + description)

# pass a tuple to a dictionary
print(dict(f_tuple))


