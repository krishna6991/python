class ShippingContainer:
	next_serial = 1337  #class attributes

	@classmethod
	def __get_next_serial_class(cls):
		result=cls.next_serial
		cls.next_serial +=1
		return result

	@classmethod
	def create_empty(cls, owner_code):
		return cls(owner_code, contents=None)  #create instance with the empty contents , you can directly call it use to create FACTORY METHOD.


	# @staticmethod
	# def __get_next_serial(self):
	# 	result=ShippingContainer.next_serial
	# 	ShippingContainer.next_serial +=1
	# 	return result
	@classmethod
	def create_with_items(cls, owner_code, items):
		return cls(owner_code,contents=list(items))


	def __init__(self, owner_code, contents):
		self.owner_code = owner_code
		self.contents = contents
		self.serial = ShippingContainer.__get_next_serial_class()

c =ShippingContainer.create_empty("OWN")
print (c)
c1 = ShippingContainer.create_with_items("KRI", ['fruits', 'veggies', 'grocery'])
print (c1.contents)