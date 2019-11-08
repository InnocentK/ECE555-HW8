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
import matplotlib.pyplot as plt


def getErlang2(u1, u2, l=1):
	return (-np.log(u1)/(2*l)) + (-np.log(u2)/(2*l))

# u is a number drawn from a random uniform distribution (between 0 and 1)
# l is the rate of the exp distrbution
def getEXP(u,l=1):
	return -np.log(u)/l

# Returns a list of all the values from a given list larger than a specific value
def getSmaller(list2Check, value):
	return [x for x in list2Check if x <= value]

def getBetween(list2Check, small_val, big_val):
	return [x for x in list2Check if x >= small_val and x <= big_val]

def addToQueue(list2Check, que):

	# add to queue
	if que.empty():
		for value in list2Check:
			que.put(value)
		return que

	# When queue has elementsd
	for value in list2Check:
		# add to queue
		if value > que.queue[-1]:
			que.put(value)

	return que

def graph(x, xlabel, ylabel, title):

	plt.plot(x)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.show()

	return 0
#
# Arrival time = exponentially distributed
# Service time = erlang distribution
# Iterations = number of seconds
def simulate_M_E2_1(total_jobs=1000, arrival_rate=1, mean_service_time=0.8):

	k = total_jobs # Total number of jobs
	rand_samples1 = np.random.random_sample((k,))
	rand_samples2 = np.random.random_sample((k,))
	rand_samples3 = np.random.random_sample((k,))

	arrival_queue = queue.Queue(maxsize=k-1)
	service_queue = queue.Queue(maxsize=1)

	arrival_times = np.zeros(k)
	continuous_arrivals = np.zeros(k)
	service_times = np.zeros(k)
	continuous_service = np.zeros(k)

	N_k = np.zeros(k+1)
	exit_times = np.copy(N_k) # related to X_t
	W_n = np.zeros(k+1)
	# Y_t 

	# Setting rates
	for i,_ in enumerate(arrival_times):
		arrival_times[i] = getEXP(rand_samples1[i])
		service_times[i] = getErlang2(rand_samples2[i], rand_samples3[i])

		if i == 0:
			continuous_arrivals[i] = arrival_times[i]
			continuous_service[i] = service_times[i] + arrival_times[i]
		#elif i == 1:
			#continuous_arrivals[i] = arrival_times[i] + continuous_arrivals[i-1]
			#continuous_service[i] = service_times[i] + continuous_service[i-1] + continuous_arrivals[i-1]
		else:
			continuous_arrivals[i] = arrival_times[i] + continuous_arrivals[i-1]
			continuous_service[i] = service_times[i] + continuous_service[i-1] #+ continuous_arrivals[i-1]

	#print(continuous_arrivals)
	#print(continuous_service)
	#print(continuous_service - service_times)
	
	# Figure 6.3
	for index, k in enumerate(continuous_service):
		service_queue.put(k)
		possible_arrivals = getSmaller(continuous_arrivals,k)
		addToQueue(possible_arrivals, arrival_queue)

		N_k[index+1] = arrival_queue.qsize()
		exit_times[index+1] = service_queue.get()
		if not arrival_queue.empty():
			arrival_queue.get()
	
	#graph(N_k,"k","Nk", "Figure 6.3")
	service_queue.queue.clear()
	arrival_queue.queue.clear()

	# Figure 6.4
	final_time = int( np.ceil(exit_times[-1]) )
	X_t = []
	for t in range(final_time):

		# Get the index of times less than current time
		result = np.where(exit_times <= t)
		target_index = result[0][-1]
		target_val = N_k[target_index]
		X_t.append(target_val)

	graph(X_t,"t","X(t)", "Figure 6.4")

	# Figure 6.5
	W_n = continuous_service - continuous_arrivals
	graph(W_n,"k","Wn", "Figure 6.5")

	# Figure 6.6

	return 0

def main():

	simulate_M_E2_1(25)

	return 0
main()