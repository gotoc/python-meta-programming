from debugly import debug, debugmethods

@debug(prefix = '***')
def add(x,y):
    return x + y

@debugmethods
class Spam:
	def a(self):
		pass
	def b(self):
		pass