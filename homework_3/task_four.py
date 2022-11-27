first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}
merged_dict = first_dict | second_dict
array_of_keys = merged_dict.keys()
array_of_united_values = []
counter = 0

for key in merged_dict:
    array_of_united_values\
        .append([first_dict.get(key), second_dict.get(key)])

first_dict.update(second_dict)
for key in first_dict:
    first_dict[key] = array_of_united_values[counter]
    counter += 1

print(first_dict)
