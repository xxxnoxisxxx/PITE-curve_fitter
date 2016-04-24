from scipy.stats import chisquare

#Klasa wykonujaca Chi-squared test
class StatAnalyser(object):
	@staticmethod
	def analyse(exp_data, obs_data):
		for i, val in enumerate(exp_data):
			if val == 0:
				exp_data[i] = 0.0000000001
		res = chisquare(obs_data, exp_data)
		print(res)
