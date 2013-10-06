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

#if we wanted to use a same decorator for many classes with inheritanceslike

#@debugmethods
#class Spam:

#@debugmethods
#class cap(Spam):

#@debugmethods
#class tap(cap):

#then we use metaclass

class debugmeta(type):
	def __new_(cls, clsname, bases, clsdict):
		clsobj = super().__new_(cls, clsname,
								bases, clsdict)
		clsobj = debugmethods(clsobj)
		return clsobj

#class Base(metaclass = debugmeta):
#class cap(Base)

#Making customized types through inheritence from type class

class mytype(type):
	def __new__(cls, clsname, bases, clsdict):
		if len(bases) > 1: 
			raise TypeError("NO!")
		return super().__new__(cls, clsname, clsdict)

#to use the custom type we require we need to inherit
#class Base(metaclss = mytype):
#	pass
#class A(Base):
#	pass
#class B(Base):
#	pass
#class C(A,B): 
#	pass
# Error is raised due to two bases


