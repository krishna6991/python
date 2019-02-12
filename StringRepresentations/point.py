class Point2D:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return '({}, {})'.format(self.x, self.y)

	def __repr__(self):
		return 'Point2D(x={}, y={})'.format(self.x, self.y)

	def __format__(self, f):
		if f == 'r':
			return '{}, {}'.format(self.y, self.x)
		else:
			return '{}, {}'.format(self.x, self.y )

p = Point2D(3,4)
print (repr(p))

print ('{:r}'.format(Point2D(1,2)))
print ('{!r}'.format(Point2D(1,2))) #forces to use the repr
print ('{!s}'.format(Point2D(1,2))) #forces to use the str