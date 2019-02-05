from datetime import date 

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	@classmethod
	def fromBirthYear(cls, name, birthYear):
		return cls(name, date.today().year - birthYear)

	def display(self):
		print(self.name + "'s age is: " + str(self.age))

person = Person('antra', 14)
person.display()

person1 = Person.fromBirthYear('krishna',  1996)
person1.display()