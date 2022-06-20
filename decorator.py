from functools import wraps

def make_blink(function):
	"""Defines the decorator"""

	# This makes the decorator transparent in terms of its name and docstring
	@wraps(function)

	# Define the inner function
	def decorator():

		# get the return value of the function being decorated
		ret = function()

		# add new functionality to the function being decorated
		return "<blink>" + ret + "</blink>" 

	return decorator

def hello_world():
	"""Original function!"""
	return "Hello, World!"

@make_blink
def hello_world_blink():
	"""Original function!"""
	return "Hello, World!"

# show the result
print(hello_world())
print(hello_world_blink())

# by using @wrap, the decorator's effect is transparent, and so the function's docstring is not changed.
print(hello_world.__name__)
print(hello_world_blink.__name__)
print(hello_world.__doc__)
print(hello_world_blink.__doc__)

