first_name = 'Domingos'
last_name = 'Manuel'
print(first_name + ' ' + last_name)

one = 'Domingos'
two = 'Manuel'
print(f'{one} {two}')

name = 'Domingos';
surname = 'Manuel'
full_names = '{} {}'.format(name, surname)
print(full_names)

the_name = 'Domingos'
the_qty = 8
print(f'{the_name} has {the_qty} pairs of shoes')

statement = '''
Attention
Everyone
This
Is 
Very 
Important
'''
print(statement.upper())
print(statement.lower())
print(statement.capitalize())

message = 'Welcome to Python!'
print(message)
print(message.isdigit())
print(message.count('e'))
print(message.endswith('!'))

name = input('Name: ')
family_name = input('Surname: ')
real_age = input('Age: ')
print(f'{name} {family_name} is {real_age} years old')

item_one = input('Wish item 1: ')
item_two = input('Wish item 2: ')
print(f'For his birthday {name} {family_name} would like to have a {item_one} and a {item_two}'.upper())
