import math


def distance(*args: tuple):
    list_of_values = []
    list_of_distances = []
    index = 0
    for point_one, point_two in args:
        one_point_value = (point_two - point_one)**2
        list_of_values.append(one_point_value)
    while index < len(list_of_values) - 1:
        if index > len(list_of_values):
            break
        list_of_distances.append(math.sqrt(list_of_values[index]
                                           + list_of_values[index + 1]))
        index += 1

    return f'Distance between {len(args)} points is' \
           f' {round(sum(list_of_distances), 2)}'


result = distance((3, 5), (5, 7), (7, 9))
print(result)
