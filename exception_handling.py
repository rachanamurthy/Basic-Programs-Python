# Exception Handling Example
import math

def squareroot(x):
	try:
		print('Square root of ',x,'is : ', math.sqrt(x))
	except (TypeError,ValueError):
		print('x must be valid')  	