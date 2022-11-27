import random

random_list = [random.randrange(-100, 100) for element in range(10)]
print(f'firstly initialized list is {random_list}')
random_list[2] = random.randint(-100, 100)
del random_list[6]
print(f'our list after changes looks like {random_list}')
