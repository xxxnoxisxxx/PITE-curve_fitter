import copy
import random

class DataGenerator(object):
	@staticmethod
	#Klasa generujaca przedzial z punktami do rysowania
	def frange(start, end, step):
		while start < end:
			yield start
			start += step

	@staticmethod
	#Generuje funkcje do narysowania bez zaklocen
	def generate_function_data(fun, start, end, step):
		step_generator = DataGenerator.frange(start, end, step)
		data = [[i,fun(i)] for i in step_generator]
		return data

	@staticmethod
	#Generuje funkcje do narysowania z zakloceniami
	def generate_noisy(data, start, end):
		noisy_data = copy.deepcopy(data)
		for i, val in enumerate(data):
			noisy_data[i][1] = val[1] + random.uniform(start, end) 
		return noisy_data
		
