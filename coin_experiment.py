#!/bin/perl
	
import random
import numpy

# calculate mean and stdev for number of coins to amount to $0.25

coins = [0.01, 0.05, 0.1, 0.25, 0.5]
tot_turns = []

for i in range(10000):
	cash_total = 0
	turns = 0
	while cash_total < 0.25:
		random_selection = random.randrange(1, 5)
		coin_selection = coins[random_selection]
		#print coin_selection
		cash_total += coin_selection
		#print cash_total
		if cash_total >= 0.25:
			#print cash_total
			cash_total = 0.25
		#print cash_total
		turns += 1
	#print "It took " + str(turns) + " coins to amount to $0.25"
	tot_turns.append(turns)

mean = numpy.mean(tot_turns, dtype=numpy.float64)
print mean
stdev = numpy.std(tot_turns, dtype=numpy.float64)
print stdev

# calculate mean and stdev for number of coins to amount to $1.00
	
coins = [0.01, 0.05, 0.1, 0.25, 0.5]
tot_turns = []

for i in range(10000):
	cash_total = 0
	turns = 0
	while cash_total < 1.0:
		random_selection = random.randrange(1, 5)
		coin_selection = coins[random_selection]
		#print coin_selection
		cash_total += coin_selection
		#print cash_total
		if cash_total >= 1.0:
			#print cash_total
			cash_total = 1.0
		#print cash_total
		turns += 1
	#print "It took " + str(turns) + " coins to amount to $1.0"
	tot_turns.append(turns)

mean = numpy.mean(tot_turns, dtype=numpy.float64)
print mean
stdev = numpy.std(tot_turns, dtype=numpy.float64)
print stdev

# calculate mean and stdev for number of coins to amount to $10.00
	
coins = [0.01, 0.05, 0.1, 0.25, 0.5]
tot_turns = []

for i in range(10000):
	cash_total = 0
	turns = 0
	while cash_total < 10.0:
		random_selection = random.randrange(1, 5)
		coin_selection = coins[random_selection]
		#print coin_selection
		cash_total += coin_selection
		#print cash_total
		if cash_total >= 10.0:
			#print cash_total
			cash_total = 10.0
		#print cash_total
		turns += 1
	#print "It took " + str(turns) + " coins to amount to $10.00"
	tot_turns.append(turns)

mean = numpy.mean(tot_turns, dtype=numpy.float64)
print mean
stdev = numpy.std(tot_turns, dtype=numpy.float64)
print stdev

#2068 characters