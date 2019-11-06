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

#
# Arrival time = exponentially distributed
# Service time = erlang distribution
# Iterations = number of seconds
def simulate_M_E2_1(iterations=25, arrival_rate=1, mean_service_time=0.8):

	N = [] # list of number of jobs in the system after service completion of the kth customer for all k customers
	N_k = 0 # number of jobs in the system after service completion of the kth customer
	total_customers = 1.0
	completed_jobs = 1.0
	arrival_queue = queue.Queue(maxsize=iterations)
	#serving = True

	time = 0
	while len(N) <= iterations:

		# Job arrival at EXP(1t)
		# Add jobs to queue
		num_jobs = math.floor( math.exp(time) - completed_jobs)
		total_customers += num_jobs

		# Push the new jobs waiting
		for i in range(num_jobs):
			arrival_queue.put(i)

		# A job is completes service
		N_k = arrival_queue.qsize()
		N.append(N_k)
		completed_jobs += 1

		# Pop the next job to be serviced
		arrival_queue.get()

		time = (5.0 * math.log(total_customers) ) / 4.0

	return N

def main():

	serviced = simulate_M_E2_1()

	print(serviced)

	return 0
main()