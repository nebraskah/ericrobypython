"""
Functions
"""

print('Hello from outside the function!')


def my_hello_func():
    print('Hello')
    print('From a Python function')


my_hello_func()


def print_name(first_name, surname):
    print(f'Hello {first_name} {surname}')


print_name('Jordan', 'Manuel')


def class_mates(*bunch_of_names):
    print(f'Last one is {bunch_of_names[-1]}')


class_mates('Matana', 'Gamaliel', 'Gonzaga', 'Ganancio', 'Luzilde', 'Nelson', 'Paulo', 'Bia', 'Babu', 'Candinha')


def some_function(highest_numb, lowest_numb):
    print(lowest_numb)
    print(highest_numb)


some_function(lowest_numb=5, highest_numb=9)


def default_values(country = 'Mozambique'):
    print(f'My country is the beautiful {country}')


default_values('Portugal')
default_values('Holland')
default_values()
default_values('South Africa')


def times_function(numb_one, numb_two):
    return numb_one * numb_two


multiplied_numb = times_function(10, 5)
print(multiplied_numb)


def remove_elements(elements):
    elements.pop(0)
    elements.pop(-1)
    return elements


special_list = ['Banana', 'Apple', 'Orange', 'Grapefruit', 'Nectarine', 'Plum', 'Peach']
print(special_list)
special_list = remove_elements(special_list)
print(special_list)


def celsius_to_fahrenheit(c):
    return (c * 9) / 5 + 32;


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


fahrenheit = 81;
celsius = fahrenheit_to_celsius(fahrenheit)
print(f'{fahrenheit} degrees Fahrenheit is equivalent to {celsius} degrees Celsius')


celsius = 10
fahrenheit = celsius_to_fahrenheit(celsius)
print(f'{celsius} degrees Celsius is equivalent to {fahrenheit} degrees Fahrenheit')


"""
Recursive Functions
"""

def factorial(x):
    if x > 0:
        print(x)
        if x == 1:
            return 1
        return x * factorial(x-1)


number = 5
print(f'Factorial: {number}! = {factorial(number)}')


def fibonacci(numb):
    if numb == 0:
        return 0
    elif numb == 1:
        return 1
    else:
        return fibonacci(numb - 2) + fibonacci(numb - 1)


for number in range(10):
    print(fibonacci(number))

