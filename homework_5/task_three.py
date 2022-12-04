with open('text_for_hometask.txt', 'r') as file_reader:
    user_input = input('Please specify your character to be counted: ')
    occurrence = 0
    text = file_reader.read()
    if user_input.isupper():
        text = text.upper().strip()
    else:
        text = text.lower().strip()
    for char in text:
        if char == user_input:
            occurrence += 1
    print(f'Specified character {user_input} was faced {occurrence} times')
