import math


def distance(*args: tuple):
    list_of_values = []
    for point_one, point_two in args:
        one_point_value = (point_two - point_one)**2
        list_of_values.append(one_point_value)
    return f'Distance between {len(args)} points is' \
           f' {round(math.sqrt(sum(list_of_values)), 2)}'


result = distance((1, 3), (3, 5), (5, 7))
print(result)
