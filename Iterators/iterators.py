string = '1234567890'

# for char in string:
#     print(char)

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

my_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
my_iterator = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)

for i in my_list:
    print(i)

number_list = [1, 4, 9, 16, 25, 36]
new_iterator = iter(number_list)

for i in range(len(number_list)):
    new_item = next(new_iterator)
    print(new_item)



