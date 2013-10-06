from debugly import debug, debugmethods, debugattr

@debug(prefix = '***')
def add(x,y):
    return x + y

#if you are using debugmethods we can't wrap if static methods and classmethods are use
@debugmethods
class Spam:
	def a(self):
		pass
	@debug(prefix = '***')#other than static and clasmethods every decorator might work but in the order of classdecorator and func decorator
	def b(self):
		pass

@debugattr
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y