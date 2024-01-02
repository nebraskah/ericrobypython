'''
Flow Control - if statements
'''

number = 100

if number == 100:
    print(f'Number is equal to {number}')
    print('Line 2 within curly brackets')
    print('This is crazy')
    print('I prefer curly brackets for readability')
print('Enf of application')

'''
Flow Control - else statements
'''
number = 450
if number == 500:
    print(f'{number} is a good number')
else:
    print(f'{number} is a rotten number')
print('Done numbering')

hour = 19
if hour < 18:
    message = 'Good morning'
else:
    message = 'Good afternoon'
print(message)


'''
Flow Control - Elif statement (java's else-if)
'''

hour = 22
if hour < 13:
    message = 'Good morning!'
elif hour < 19:
    message = 'Good afternoon!'
elif hour < 21:
    message = 'Good evening!'
else:
    message = 'Good night!'
print(message)

student = input('Enter the student\'s name: ')
mark = int(input(f'Enter {student}\'s year mark: '))
grade = 'F'
if mark >= 90:
    grade = 'A'
elif mark >= 80:
    grade = 'B'
elif mark >= 70:
    grade = 'C'
elif mark >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'{student} got a grade {grade}')

