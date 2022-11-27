user_name = input("Please specify user name with two words: ")
splitted_name = user_name.split(" ")
reversed_name = f'{splitted_name[1]} {splitted_name[0]}'
print(reversed_name)
