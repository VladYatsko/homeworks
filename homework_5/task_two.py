number_one = 0
number_two = 1
index_of_number = 1
requested_index = int(input('Please specify index of '
                            'number in Fibonacci numbers: '))
while True:
    index_of_number += 1
    next_number = number_one + number_two
    number_one = number_two
    number_two = next_number
    if index_of_number == requested_index:
        print(f'Number on index {index_of_number} equals {next_number}')
        break
