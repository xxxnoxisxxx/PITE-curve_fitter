from data_generator import *
from fitter import *
from stat_analyser import *
from plotter import *
from math import sin
import random

if __name__ == '__main__':

	print("Witaj w fitowaniu funkcji sin(x)")
	
	min_fun = float(input("Podaj poczatek przedzialu!\n"))
	max_fun = float(input("Podaj koniec przedzialu!\n"))
	step = float(input("Podaj krok!\n"))

	print("Podaj przedzial dla zaklocen!")
	min_noisy = float(input("Podaj poczatek przedzialu!\n"))
	max_noisy = float(input("Podaj koniec przedzialu!\n"))
	
	print("Rysuje funkcje bez zaklocen! - sin.png")
	fun_data = DataGenerator.generate_function_data(lambda x : sin(x), min_fun, max_fun, step)
	Plotter.plot_chart(fun_data,"sin.png")
	
	print("Rysuje funkcje z zakloceniami - sin_noisy.png")
	fun_data_noisy = DataGenerator.generate_noisy(fun_data, min_noisy, max_noisy)
	Plotter.plot_chart(fun_data_noisy,"sin_noisy.png")
	
	print("Fittowanie!")
	fit_data = Fitter.fitting(fun_data_noisy)
	print("Rysuje funkcje! - fitting_result.png")
	Plotter.plot_multi_chart(fun_data, fun_data_noisy, fit_data, "fitting_result.png")
	
	print("Chi-squared test")
	StatAnalyser.analyse([y[1] for y in fun_data],[y[1] for y in fun_data_noisy])
	

