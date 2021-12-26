# Tamsin Rogers
# October 1, 2019
# CS 152 
# Project 4: Population Variability Analysis
# Parts 1-9
# This program uses models the change in the population of Galapagos Penguins over time given certain ecological pressures by modeling the risk of extinction over some number of years.
# Run the program from the Terminal by entering "python3 penguin.py"

import random							#import the random package
import sys								#import the sys package
import matplotlib.pyplot as plt			#import the matplotlib package for use with plots as plt

"""This function takes in two parameters: the initial population size and the probability 
of an individual being female, and returns a list of the specified size. Each entry in the 
list will be either an 'f' or an 'm'."""
def initPopulation(popsize, probFemale):	#define a function initPopulation with two parameters
	population=[]							#initialize population to an empty list
	for i in range(popsize):				#start a loop for the size of the population
		number = random.random()			#each time through the loop generate a random number using random.random() and assign number to it
		if number<probFemale:				#if the value is less than the probability of an individual being female (probFemale)
			population.append("f")			#append an 'f' to the population list
		else:
			population.append("m")			#append an 'm' to the population list
	return population						#return the population list

"""This function takes in 6 parameters: pop (the population list), elNinoProb (the probability 
of an El Nino), stdRho (the growth factor in a regular year, which allows the population to 
grow each year and is expected to be greater than 1), elNinoRho (the growth factor in an El 
Nino year, which is meant to reduce the population and is therefore less than 1), probFemale
(the probability of a new individual being female), and maxCapacity (the max carrying capacity 
of the ecosystem) and uses them to determine if it is an El Nino year and append male/female
penguins to their respective lists depending on their probabilities."""
def simulateYear(pop, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity):
	elNinoYear = False
	if random.random()<elNinoProb:
		elNinoYear = True
	newpop = []
	 # for each penguin in the original population list
	for i in pop:
		# if the length of the new population list is greater than maxCapacity
		if (len(newpop))>maxCapacity:
			# break, since we don't want to make any more penguins
			break
		# if it is an El Nino year
		if elNinoYear == True:
			# if random.random() is less than the El Nino growth/reduction factor
			if random.random()<elNinoRho:
				# append the penguin to the new population list
				newpop.append(i)
		# else
		else:
			# append the penguin to the new population list
			newpop.append(i)
			# if random.random() is less than the standard growth factor - 1.0
			if random.random()<(stdRho-1.0):
				# if random.random() is less than the probability of a female
				if random.random()<probFemale:
					# append an 'f' to the new population list
					newpop.append("f")
				# else
				else:
					# append an 'm to the new population list
					newpop.append("m")
	return newpop

"""This function takes in 8 parameters: N (number of years to run the simulation), initPopSize 
(initial population size), probFemale (probability a penguin is female), elNinoProb (probability 
an El Nino will occur in a given year), stdRho (population growth in a non-El Nino year) elNinoRho
(population growth in an El Nino year), maxCapacity (maximum carrying capacity of the ecosystem), 
and minViable (minimum viable population), and uses them to call simulateYear, assign the return
value back to the population list, test if the population is smaller than the minimum viable population 
or it consists of only one gender (and return the year of extinction if it does).  If the loop 
completes all N times and there is still a viable population, the function returns N.""" 
def runSimulation(N, initPopSize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable):
	#initialize the population
	population = initPopulation(initPopSize, probFemale)
	#set endDate to N
	endDate = N
	#main loop
	for i in range(1,N+1):
		if (len(population)>minViable) and ("m" in population) and ("f" in population):
			newPopulation = simulateYear(population, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity)
			population = newPopulation
		
		else:
			endDate = i
			break
	return(endDate)

"""This test function for initPopulation prints out a randomized list of 10 individuals with an appropriate mix of 'f' and 'm' elements.
For simulateYear, it shows that the population reduces to 3-6 individuals in the El Nino year and grows to 11-14 individuals in the standard year."""
def test():
	popsize = 10
	probFemale = 0.5
	pop = initPopulation(popsize, probFemale)
	print(pop)
	newpop = simulateYear(pop, 1.0, 1.188, 0.4, 0.5, 3000)
	print ("El Nino year")
	print (newpop)
	newpop = simulateYear(pop, 0.0, 1.188, 0.4, 0.5, 3000)
	print ("Standard year")
	print (newpop)

	for i in range(10):
		runSimulation(201,500,0.5,(1.0/7.0),1.188,0.41,3000,10)

	return(newpop)

"""The top level function is the main function.	 It takes one argument, argv, which is the list
of strings from the command line.  The main function tests if there are at least three arguments 
on the command line, and returns a usage statement if there are not.  Main() then extracts the
second and third values from the command line arguments, sets up local variables, run simulations,
and calculates the probability of survival after N years.  This function also includes a call
to CAEPD() and prints out every 10th entry in the CEPD list."""
def main(argv):

	if (len(sys.argv)<3):
		print("enter: [1] program name, [2] # of simulations to run, [3] typical # of years between an El Nino event")
		return
	numSim = int(sys.argv[1])
	enYears = int(sys.argv[2])
	
	simResults = []		#sets results to an empty list
	CEPD = []	#sets CEPD to an empty list

	#default parameters
	N = 201
	initPopSize = 500
	probFemale = 0.5
	elNinoProb = (1.0/enYears)
	stdRho = 1.188
	elNinoRho = 0.41
	maxCapacity = 3000
	minViable = 10
	count = 0	#sets up count variable for division later
	
	for i in range(numSim):
		sResults = runSimulation(N, initPopSize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable)
		simResults.append(sResults)
		if simResults[i] < N:
			count = count+1
			
	result = (count/numSim)
	
	print("Overall probability that the penguin will go extinct in the next ", N, " years: ", (result*100), "%")
		
	"""This function takes the list of results (the set of numbers indicating the last year in 
	which the population was viable), and converts it to a cumulative extinction probability 
	distribution (CEPD). The CEPD will be a list that is as long as the number of years in the 
	simulation. Each entry Y in the CEPD is the number of simulations where the population has 
	gone extinct by year Y divided by the total number of simulations."""
	def computeCEPD(simResults, N):
		#create an empty list CEPD
		CEPD = []
		#create a list CEPD with N zeros
		for i in range(N):
			CEPD.append(0)

		#loop over the list of results (extinction years)
		for i in simResults:
			#if the extinction year is < N
			if i<N:
				#loop from the extinction year to N
				while i<N:
					#add one of each of those entries in the CEPD list
					CEPD[i]=CEPD[i]+1
					i = i+1

		#loop over the CEPD list			
		for i in range (len(CEPD)):
			#divide each entry by the length of the extinction year results list, which is also the number of simulations
			CEPD[i] = (CEPD[i]/len(simResults))
		return CEPD
		
	CEPD = computeCEPD(simResults, N)
	length = len(CEPD)
	
	#print out every 10th entry in the CEPD list and graph them
	for i in range(0, N, 10):
		print("In the year", i, " the chance of extinction is: ", (CEPD[i])*100, "%")
	
	#plot for the new 5 year El Nino cycle
	if enYears == 5:
		for i in range (0,N,10):
			year = i
			percent = (CEPD[i]*100)
			plt.plot(year,percent,"bs")
		plt.title("CEPD vs. Year for a 5 Year El Nino Cycle With Max Capacity 3000")
		plt.xlabel("Year")
		plt.ylabel("CEPD")
		plt.show()
	
if __name__ == "__main__":
	main(sys.argv)