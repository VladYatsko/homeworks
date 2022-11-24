first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}
letters_array = ['a', 'b', 'c', 'd', 'e']
array_of_united_values = []
counter = 0

for letter in letters_array:
    array_of_united_values\
        .append([first_dict.get(letter), second_dict.get(letter)])

first_dict.update(second_dict)
for letter in letters_array:
    first_dict[letter] = list(array_of_united_values[counter])
    counter += 1

print(first_dict)
