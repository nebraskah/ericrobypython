"""
Data Structures - Lists
"""

my_list = [6, 7, 8, 9, 10]
print(my_list)
print(my_list[0])

animal_list = ['Lion', 'Bear', 'Zebra', 'Tiger']
print(animal_list)
print(animal_list[2])
print(animal_list[-1]) # trick to print the last element
print(len(animal_list))

colour_list = ['red', 'blue', 'green', 'pink', 'purple']
print(colour_list)
print(colour_list[2])
print(len(colour_list))
print(colour_list[1:6:2]) # slicing - similar to substring :2 means increment in 2s. there is no OutOfBounds exception when slicing
print(colour_list.append('magenta'))
print(colour_list)
print(colour_list.insert(2, 'cyan'))
colour_list.reverse()
print(colour_list)
colour_list.pop(2)
print(colour_list)
colour_list.sort()
print(colour_list)

# nested lists (containers)
nested_list = [[1,2,3,4],[5,6,7,8],[9, 10,11,12]]
print(nested_list)
print(nested_list[1])
print(len(nested_list))
print(nested_list[0][-1]) # prints the last element of the list indexed at zero

