"""
Collections - Sets and Tuples
Tuples are ordered and unchangeable
"""

my_tuple = (1, 2, 3, 4, 5)
#tuples are unchangeable. you cannot remove nor add
print(my_tuple)
print(my_tuple[2])
print(my_tuple[-1])
for x in my_tuple:
    print(x, end="")
print()
print(len(my_tuple))
print()

my_tuple = ('Dell', 'Hewlett Packard', 'Packard Bell', 'Toshiba', 'Lenovo')
print(my_tuple[2])
print(my_tuple[0:3])
print(my_tuple[0:6:2])
print(my_tuple[-1])
print(len(my_tuple))
for computer in my_tuple:
    print(computer)

# Sets are unordered
my_set = {'apples', 'bananas', 'oranges', 'melons', 'etc...'}
print(my_set)
print('melons' in my_set)
print('grapes' in my_set)
for fruits in my_set:
    print(fruits)

# print(my_set[3]) # CANNOT be done

my_set.discard('melons')
my_set.add('pear')
my_set.update(['mangoes', 'jambalao', 'watermelon'])
print(my_set)
print(len(my_set))

set_one = {1, 2, 3, 4, 5}
set_two = {'a', 'b', 'c', 'd', 'e'}
set_three = set_one.union(set_two)
print(set_one)
print(set_two)
print(set_three)



