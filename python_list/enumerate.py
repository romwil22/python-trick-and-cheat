# List - Enumerate Function

namelst = ['rom', 'rj', 'steve', 'meann']

# print the index and value
for index, name in enumerate(namelst):
    print(index, name)

# print index start with 1
for index, name in enumerate(namelst, start=1):
    print(index, name)
