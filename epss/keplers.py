#!/usr/bin/env python
import pylab as plt
import numpy as np

def mean_anomaly(E,e):
	return E - e * np.sin(E)


def eccentric_anomaly(M,e):
	E = M + e * np.sin(M)
	iteration = 0
	delta_M = 1.0
	# Because M = E - e * sin(E) cannot be solved analytically, we use iteration.
	while (np.abs(delta_M / M) > 0.000001): 
		delta_M = M - mean_anomaly(E, e)
		E = E + delta_M / (1.0 - e * np.cos(E))
		iteration += 1
		if (iteration > 100000 and delta_M < 0.1):
			break
			# Sometimes, iteration can get stuck mostly due to high eccentricity.
			# This section helps the code jump out of the loop
	return E

def true_anomaly(E,e):
	f = np.arccos((np.cos(E) - e) / (1.0 - e * np.cos(E)))
	f *= np.sign(np.sin(f)) * np.sign(np.sin(E))
	return f

# radial_velocity returns the radial velocity of the star on our line of view,
# if we know all the companion orbit data.
def rad_v(A,f,e,cpi):
	return A * (np.sin(f + cpi) + e * np.sin(cpi))

# radial_velocity_predicted returns the radial velocity based on the machine learning parameters
# The arguments of this function are the 5 orbital parameters for MCMC
def rad_v_pred(t,amplitude,omega,phi,e,cpi):	
	M = omega * t + phi
	E = eccentric_anomaly(M, e)
	f = true_anomaly(E, e)
	return rad_v(amplitude, f, e, cpi)
