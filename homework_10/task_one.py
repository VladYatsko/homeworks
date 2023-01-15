class Country:
	def __init__(self, population):
		self.population = population

	def set_population(self, population):
		self.population = population

	def get_population(self):
		return self.population


class Russia(Country):
	def __init__(self, population):
		super().__init__(population)


class Canada(Country):
	def __init__(self, population):
		super().__init__(population)


class Germany(Country):
	def __init__(self, population):
		super().__init__(population)


germany = Germany(400000)
print(germany.get_population())
germany.set_population(50)
print(germany.get_population())
