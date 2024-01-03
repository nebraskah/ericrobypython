"""
Dictionaries - Key Value pairs
"""

user_dict = {
    'first_name': 'Diego',
    'last_name': 'Manuel',
    'dob': '10/10/2009'
}

print(user_dict)
print(user_dict['first_name'])
print(user_dict.get('last_name'))
user_dict['major'] = 'Computer Science'
print(user_dict)
print(len(user_dict))
user_dict.pop('major')
print(user_dict)
user_dict['major'] = 'Computer Science'
print(user_dict)
print(len(user_dict))
del user_dict['major']
print(user_dict)
print(len(user_dict))
user_dict.clear()
print(user_dict)


new_dict = {
    'first_name': 'Jordan',
    'last_name': 'Manuel',
    'birth_year': 2020
}

for x in new_dict:
    print(f'{x}: {new_dict[x]}')

for x, y in new_dict.items():
    print(x, y)

if 'birth_year' in new_dict:
    print(new_dict['birth_year'])

dict2 = new_dict.copy()
dict2.popitem()
print(dict2)
print(new_dict)
print(len(dict2))
print(len(new_dict))
print()


# Nested Dictionaries
family = {
    'father': {
        'first_name': 'Domingos',
        'last_name': 'Manuel',
        'birth_year': 1980
    },
    'mother': {
        'first_name': 'Carmina',
        'last_name': 'Dos Santos',
        'birth_year': 1981
    },
    'child1': {
        'first_name': 'Diego',
        'last_name': 'Manuel',
        'birth_year': 2009
    },
    'child2': {
        'first_name': 'Lara',
        'last_name': 'Manuel',
        'birth_year': 2011
    },
    'child3': {
        'first_name': 'Jordan',
        'last_name': 'Manuel',
        'birth_year': 2020
    }
}

for family_member in family:
    print(f'{family_member.capitalize()}: {family[family_member]}')
print()


for family_member, family_details in family.items():
    print(f'{family_member.capitalize()}: ', end="")
    for x, y in family_details.items():
        print(f'{y} ', end="")
    print()


challenge_dict = {

}
challenge = 'I am so happy to learn Python which makes my wife happy and interested in Python Python Python Python'
for word in challenge.split():
    challenge_dict[word] = challenge_dict.get(word, 0) + 1
print(challenge_dict)



