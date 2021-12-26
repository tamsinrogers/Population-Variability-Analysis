# Tamsin Rogers
# September 25, 2019
# CS 152 
# Lab 4: The random package and matplotlib
# Parts 1-4 - creating and plotting random numbers
# Run the program from the Terminal by entering "python3 rand.py"

import random							#import random
import matplotlib.pyplot as plt

def genNrandom(N):
	numbers = []						#assign an empty list to numbers
	for i in range(N):					#for loops that executes N times
		numbers.append(random.random())	#appends the random result to the list
	return numbers

def genNintegers(points, lowerBound, upperBound):
	points=int(points)
	lowerBound=int(lowerBound)
	upperBound=int(upperBound)
	numbers=[]
	for i in range(points):										#for loop that executes N times
		numbers.append(random.randint(lowerBound, upperBound))	#appends the random result to the list
	return numbers

def genNnormal(points, mean, std):
	points=int(points)
	mean=float(mean)
	std=float(std)
	numbers=[]
	for i in range(points):
		numbers.append(random.gauss(mean,std))
	return(numbers)

def test():							
	test1 = genNrandom(100)			#set test to result of random float
	print(test1)
	test2 = genNintegers(10,-10,10)
	print(test2)
	test3 = genNnormal(100,0,0.2)
	print(test3)
	x = random.randint(0,1)
	y = random.randint(-10,10)
	z = random.random()
	plt.plot(test1,test3,"o")
	plt.title("plot")
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.show()
	
test()