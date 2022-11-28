counter = 1
while counter != 101:
    if counter % 3 == 0 and counter % 5 != 0:
        print('Fuzz')
    elif counter % 5 == 0 and counter % 3 != 0:
        print('Buzz')
    elif counter % 3 == 0 and counter % 5 == 0:
        print('FizzBuzz')
    else:
        print(counter)
    counter += 1
