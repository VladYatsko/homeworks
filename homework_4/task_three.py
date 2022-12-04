import random

guessed_number = str(random.randint(1000, 10000))
item = set()
for number in guessed_number:
    item.add(number)

while len(item) != 4:
    item.add(str(random.randint(0, 9)))

guessed_number = f'{list(item)[0]}{list(item)[1]}' \
                 f'{list(item)[2]}{list(item)[3]}'
bulls = 0
cows = 0

while True:
    opponent_guessing = input('Please try to guess which '
                              'number is used. Do not repeat symbols')
    if guessed_number == opponent_guessing:
        print(f'You win! Bravo! Winning number is {guessed_number}')
        break

    for char in opponent_guessing:
        for character in guessed_number:
            if char == character and opponent_guessing.index(char) \
                    == guessed_number.index(character):
                cows += 1
                bulls += 1
            if char == character and opponent_guessing.index(char) \
                    != guessed_number.index(character):
                cows += 1
    print(f'User number is {opponent_guessing}')
    print(f'{cows} Cows, {bulls} Bulls')
    cows = 0
    bulls = 0
