import numpy as np
from scipy.optimize import curve_fit

class Fitter(object):
	@staticmethod
	#Metoda odpowiedzialna za fittowanie parametrow
	def fitting(data):
		xdata = np.array([x[0] for x in data])
		ydata = np.array([y[1] for y in data])
		
		freq = 1
		amplitude = np.std(ydata)/(2**0.5)
		phase = 0
		offset = np.mean(ydata)

		p0=[freq, amplitude, phase, offset]
	
		def my_sin(x, freq, amplitude, phase, offset):
			return np.sin(x * freq + phase) * amplitude + offset

		fit = curve_fit(my_sin, xdata, ydata, p0=p0)
		print("Parametry po fittowaniu: \nfreq: " + str(fit[0][0]) + "\namplitude: " + str(fit[0][1]) + "\nphase: " + str(fit[0][2]) + "\noffset: " + str(fit[0][3]))

		ydata = my_sin(xdata, *fit[0])
		
		new_data = [[xdata[i],ydata[i]] for i in range(len(xdata))]
		
		return new_data
