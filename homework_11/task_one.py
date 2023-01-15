import random


class User:
    def __init__(self):
        self.name = random.choice(['John', 'Jane', 'Mary', 'David',
                                   'Alex', 'Max', 'Nick', 'Anastasia', 'Leo'])
        self.nick_name = f'{self.name}{random.randint(10000,100000)}'
        self.age = random.randint(0, 101)
        self.eye_color = random.choice(['blue', 'green', 'brown',
                                        'grey', 'black'])
        self.info = {'Name': self.name, 'Nickname': self.nick_name,
                     'Age': self.age, 'Eyes_color': self.eye_color}

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age <= other.age

    def __ge__(self, other):
        return self.age >= other.age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def eye_color(self):
        return self._eye_color

    @eye_color.setter
    def eye_color(self, value):
        self._eye_color = value


def generate_users(number):
    current_user_count = 0
    while current_user_count < number:
        new_user = User()
        yield new_user
        current_user_count += 1


user_gen = generate_users(5)
for user in user_gen:
    print(user.info)
