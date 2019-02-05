from datetime import date 

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	@staticmethod
	def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
		return Person(name, date.today().year-fatherAge + fatherPersonAgeDiff)

	@classmethod
	def fromBirthYear(cls, name, birthYear):
		return cls(name, date.today().year - birthYear)

	def display(self):
		print(self.name+ "'s age is: "+ str(self.age))

class Man(Person):
	sex = 'Male'

man = Man.fromBirthYear('Krishna', 1996)
print(isinstance(man,Man))

man1 = Man.fromFathersAge('PNP', 1975, 20)
print(isinstance(man1, Man))