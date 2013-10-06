from debugly import debug, debugmethods

@debug(prefix = '***')
def add(x,y):
    return x + y

#if you are using debugmethods we can't wrap if static methods and classmethods are use
@debugmethods
class Spam:
	def a(self):
		pass
	def b(self):
		pass