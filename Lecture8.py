'''
For Loops
'''

numbers_list = [1, 2, 3, 4, 5]
print(numbers_list[0])
print(numbers_list[1])
print(numbers_list[2])
print(numbers_list[3])
print(numbers_list[4])

for index in numbers_list:
    print(index)

for x in range(3, 8):
    print(x)

co_workers = ['Geraldene', 'Johan', 'Ryan', 'Raymond']
for colleague in co_workers:
    print(f'Hello {colleague}')
    if colleague == 'Ryan':
        print('You rock mate!')
        break

numbers_game = [1, 2, 3, 4, 5, 6, 7, 8]
for numb in numbers_game:
    if numb == 3 or numb == 7:
        continue
    print(numb)

'''
While Loops
'''
x = 0
while x < 10:
    x += 1;
    print(x)
else:
    print(f'{x} is now out of range')

i = 10

while 10 >= i > 0:
    if i % 2 == 0:
        print(f'{i} is divisible by 2')
    else:
        print(f'{i} sucks!!!')
    i -= 1

the_var = 5
while 5 >= the_var > 0:
    print(the_var)
    the_var -= 1
print('GO!')


for numb in range(1, 51):
    if numb % 3 == 0 and numb % 5 == 0:
        print('FizzBuzz')
    elif numb % 5 == 0:
        print('Buzz')
    elif numb % 3 == 0:
        print('Fizz')
    else:
        print(numb)

