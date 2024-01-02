"""
String Methods
"""

greetings = 'Welcome to the Python World!'
cumprimentos = 'Welcome, to the, Python World!'

# Indexing
print(greetings[0])
print(greetings[-1])

# Slicing
print(greetings[0:7])
print(greetings[0:7:2])

# Length
print(len(greetings))

# Splitting
print(greetings.split()) # default split are white spaces
print(cumprimentos.split(", "))

# Finds and returns index
print(greetings.find('Python'))
print(cumprimentos.find('Cobra'))

# Joins
print(greetings, "".join('Jordan'))
print(greetings, ":".join('champ'))

# Strip - eliminating white spaces
senha = "       some very big spaces everywhere    "
leng = len(senha)
leng2 = len(senha.strip())
print(f'{senha}:{leng}')
print(f'{senha.strip()}:{leng2}')

# Replace
new_greetings = greetings.replace('Python', 'Anaconda').replace('Welcome to the', 'Benvindo ao')
print(greetings)
print(new_greetings)



