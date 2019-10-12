import statistics 
from scipy.stats.mstats import gmean  
import numpy as np

def portHPR_Stdev():
	"""

	The geometric mean is most appropriate for series that exhibit serial correlation. 
	This is especially true for investment portfolios.

	For volatile numbers, the geometric average provides a far more accurate measurement of the 
	true return by taking into account year-over-year compounding.

	"""

	years = input("How many years within the portfolio?: ")
	num_years = []
	returns = []
	geo_returns = []


	for number in range(0, int(years)):
		num_years.append(float(number))
	#print(num_years)

	for returnperc in range(0, int(years)):
		print("Note: use . to identify percent ie (.15 = 15%)")
	
		percent = input("What is the return for year " + str(returnperc) + " :")		
		returns.append(float(percent))
	print(returns)


	arthmetic_mean = '{0:.2%}'.format((statistics.mean(returns)))
	print("The arthmetic mean is: " + str(arthmetic_mean))

	# This is also the HOLDING PERIOD RETURN 
	# ((1+.08) + (1 +.09) + (1 +-.05))^(1/3) 
	for num in returns:
		geo_returns.append(num + 1)
	geometricmean = '{0:.4%}'.format(((np.prod(geo_returns)) ** (1/(float(years)))) - 1)
	print("The geometric mean (HPR) is: " + str(geometricmean))


	# NEED TO ADD: harmonic _mean() for python 3.8
	stddev = '{0:.2%}'.format((statistics.stdev(returns)))
	print("The standard deviation is: " + str(stddev))  
