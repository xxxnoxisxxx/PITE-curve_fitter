import matplotlib.pyplot as plt
import numpy as np

#Klasa sluzaca do rysowania wykresow
class Plotter(object):
	#Rysuje pojedynczy wykres
	@staticmethod
	def plot_chart(data, name):
		x = [x[0] for x in data]
		y = [y[1] for y in data]
		plt.clf()
		plt.plot(x,y,'o')
		plt.xlabel('x')
		plt.ylabel('y(x)')
		plt.title('Wykres')
		plt.grid(True)
		plt.savefig(name)
		
	#Rysuje kilka wykresow na jednym
	@staticmethod
	def plot_multi_chart(ori_data, noisy_data, fit_data, name):
		plt.xlabel('x')
		plt.ylabel('y(x)')
		plt.clf()
		
		x = [x[0] for x in ori_data]
		y = [y[1] for y in ori_data]
		plt.plot(x,y, label="sin(x)")
		
		x = [x[0] for x in noisy_data]
		y = [y[1] for y in noisy_data]
		plt.plot(x,y, label="sin(x) with noisy")
		
		x = [x[0] for x in fit_data]
		y = [y[1] for y in fit_data]
		plt.plot(x,y, label="fitting sin(x)")
		
		plt.grid(True)
		plt.legend()
		plt.savefig(name)
		
