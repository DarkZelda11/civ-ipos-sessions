crazy_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(crazy_list[3][1][2][0])

animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']

# Sequential Access

#for animal in animals:
#    if animal == 'Zebra':
#        has_Zebra = True
#        break
#    else:
#        has_Zebra = False

# try:
#    animals.index('Zebra')
# except ValueError:
#    print('No such animal')

# print("Has Zebra", "Zebra" in animals)


# Random Access

# print(animals[1])

animals_dict = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}

# animal_names = []
# for name in animals_dict:
#    animal_names.append(name)

# animal_names = [name for name in animals_dict.keys()]

# animal_characteristics = []
# for value in (animals_dict.keys()):
#    animal_characteristics.append(value)

# animals_names = list(animals_dict.keys())
# animal_characteristics = list(animals_dict.values())

animal_names = [name for name in animals_dict.keys()]
animal_characteristics = [value for value in animals_dict.values()]

for n, c in zip(animal_names, animal_characteristics):
    animals[n] = c
