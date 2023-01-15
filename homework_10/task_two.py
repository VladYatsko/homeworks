class ValidationError(Exception):
	pass


class Student:
	def __init__(self, last_name, first_name, group_number, academic_performance: list):
		self.last_name = last_name
		self.first_name = first_name
		self.group_number = group_number
		self.academic_performance = academic_performance

	@property
	def last_name(self):
		return self._last_name

	@last_name.setter
	def last_name(self, value):
		if not isinstance(value, str):
			raise ValidationError('Incorrect data type. Str is expected')
		self._last_name = value

	@property
	def first_name(self):
		return self._first_name

	@first_name.setter
	def first_name(self, value):
		if not isinstance(value, str):
			raise ValidationError('Incorrect data type. Str is expected')
		self._first_name = value


class School:
	def __init__(self):
		self.list_of_pupils = []

	def add_student(self, student):
		self.list_of_pupils.append(student)

	def get_best_students(self):
		for student in self.list_of_pupils:
			if 9 or 10 in student.academic_performance:
				print(f'{student.last_name} is in {student.group_number} group')

	def get_students(self, group_number):
		for student in self.list_of_pupils:
			if student.group_number == group_number:
				print(f'{student.first_name} {student.last_name}')

	def get_students_without_exams(self):
		for student in self.list_of_pupils:
			if sum(student.academic_performance) / len(student.academic_performance) >= 7:
				print(f'{student.first_name} {student.last_name}')


first_student = Student('Petrov', 'Oleg', 23, [10, 9, 8, 6, 3])
second_student = Student('Sokolov', 'Igor', 22, [5, 7, 8, 6, 3])
third_student = Student('Ivanov', 'Aleksandr', 23, [1, 9, 8, 6, 3])
school = School()
school.add_student(first_student)
school.add_student(second_student)
school.add_student(third_student)
school.get_students(23)
