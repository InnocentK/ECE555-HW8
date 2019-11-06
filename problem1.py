# File:   problem1.py
# Author: Innocent Kironji
# Date:   11/06/2019
# Class:  ECE 555 - Probability for Electrical Engineers
# Description:
#	Write and run a program to simulate an M/E2/1 queue and obtain realizations of 
#	the four stochastic processes defined in Example 6.2. Plot these realizations. You
#	may use a simulation language such as SIMULA or GPSS or you may use one
#	of the standard high-level languages. You will have to generate random deviates
#	of the interarrival time distribution (assume arrival rate λ = 1 per second) and
#	the service time distribution (assume mean service time 0.8 s) using methods of
#	Chapter 3.

import math
import queue
import numpy as np


def getErlang2(u,l=1):
	return (-np.log(u)/(2*l)) + (-np.log(u)/(2*l))

# u is a number drawn from a random uniform distribution (between 0 and 1)
# l is the rate of the exp distrbution
def getEXP(u,l=1):
	return -np.log(u)/l

#
# Arrival time = exponentially distributed
# Service time = erlang distribution
# Iterations = number of seconds
def simulate_M_E2_1(total_jobs=1000, arrival_rate=1, mean_service_time=0.8):

	k = total_jobs # Total number of jobs
	rand_samples = np.random.random_sample((k,))

	arrival_queue = queue.Queue(maxsize=k-1)
	service_queue = queue.Queue(maxsize=1)

	arrival_times = np.zeros(k)
	continuous_arrivals = np.zeros(k)
	service_times = np.zeros(k)
	continuous_service = np.zeros(k)

	# Setting rates
	for i,_ in enumerate(arrival_times):
		arrival_times[i] = getEXP(rand_samples[i])
		service_times[i] = getErlang2(rand_samples[i])

		if i == 0:
			continuous_arrivals[i] = arrival_times[i]
			continuous_service[i] = service_times[i]
		else:
			continuous_arrivals[i] = arrival_times[i] + continuous_arrivals[i-1]
			continuous_service[i] = service_times[i] + continuous_service[i-1]

	return 0

def main():

	serviced = simulate_M_E2_1()

	print(serviced)

	return 0
main()