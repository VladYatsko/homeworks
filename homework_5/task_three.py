with open('text_for_hometask.txt', 'r') as file_reader:
    list_of_lines = []
    user_input = input('Please specify your character to be counted: ')
    occurrence = 0
    while True:
        line = file_reader.readline()
        if user_input.isupper():
            list_of_lines.append(line.upper().strip())
        else:
            list_of_lines.append(line.lower().strip())
        if not line:
            break
    for line in list_of_lines:
        for char in line:
            if char == user_input:
                occurrence += 1
    print(f'Specified character {user_input} was faced {occurrence} times')
