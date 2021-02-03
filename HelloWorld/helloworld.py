def string_rev(s):
    str = ''
    for i in s:
        print(i)
        str = i + str
        print(str)
    return str


def isGreater(a,b):
    if a > b:
        print(f"{a} is greater than {b}")
    if a < b:
        print(f"{a} is less than {b}")
    if a == b:
        print(f"{a} is equal to {b}")


def reverse(lst):
    lst.reverse()
    return lst


def sort_nums(lst):
    lst.sort()
    return lst


a = 15
b = 12

numbers = [5, 8, 10, 12, 15]
numbers2 = [2, 9, 3, 5, 1, 9, 4]
name = 'Hello World'
print(f'Before Reversal {name}')
print(f'After Reversal {string_rev(name)}')

isGreater(a,b)
print(sort_nums(numbers2))
print(reverse(numbers))







