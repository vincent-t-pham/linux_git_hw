import time

def calculate_time(func):
	def wrapper():
		x=time.time()
		func()
		y=time.time()
		z = y-x
		print(f'Total time {z}') 
	return wrapper

	
