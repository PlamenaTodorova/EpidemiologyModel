from testingGround import test
from sirModel import solveEquation
import random
import math

log = open("log.txt", "w")
result = open("result.txt", "w")

sucseptible, infected = solveEquation(0.0178, 2.79, 254, 7)
tries = 100;
length = len(infected)
infectionChance = random.random();
deathChance = random.random();
dh=0.001

def errorCalculation(infectionChance, deathChance):
	testDays, testResults = test(tries, infectionChance, deathChance)
	
	testLength = len(testResults)
	sum=0;

	if testLength < 400:
		raise ValueError("Too short")

	if testLength < length:
		for i in range(testLength):
			index = int(round(i*length/testLength))
			sum += (testResults[i] - infected[index])**2
	else:
		for i in range(length):
			index = int(round(i*testLength/length))
			sum += (testResults[index] - infected[i])**2

	return sum**0.5

def infectionChanceError(infectionChance, deathChance):
	times = 10
	usedDh = dh

	while True:
		try:
			return errorCalculation(infectionChance + usedDh, deathChance) - errorCalculation(infectionChance, deathChance);
		except:
			times-=1;
			usedDh *= 0.5

			if times == 0:
				raise ValueError("It's geting imposible")

def deathChanceError(infectionChance, deathChance):
	times = 10
	usedDh = dh

	while True:
		try:
			return errorCalculation(infectionChance, deathChance + usedDh) - errorCalculation(infectionChance, deathChance);
		except:
			times-=1;
			usedDh *= 0.5

			if times == 0:
				raise ValueError("It's geting imposible")
				

def makeBetter(infectionChance, deathChance, precision, coeff, oldError):
	dB = infectionChanceError(infectionChance, deathChance)
	dG = deathChanceError(infectionChance, deathChance)

	candidateError = oldError + 10**6
	newCoeff = 2*coeff
	currentinfectionChance = infectionChance
	currentdeathChance = deathChance
	iterations = 10

	log.write("Starting with " + str(oldError) + "\n")
	
	while candidateError -  oldError >= precision and currentinfectionChance > 0 and currentinfectionChance < 1 and currentdeathChance > 0 and currentdeathChance < 1 and iterations > 0:
		newCoeff *= 0.5;
		
		if infectionChance < newCoeff*dB or deathChance < newCoeff*dG:
			continue
		
		currentinfectionChance = infectionChance - newCoeff*dB
		currentdeathChance = deathChance - newCoeff*dG
		try:
			candidateError = errorCalculation(currentinfectionChance, currentdeathChance)
		except Exception as e:
			iterations-=1
			continue

		log.write("infectionChance: " + str(infectionChance) + ", deathChance: " + str(deathChance) + "\n")
		log.write(str(candidateError) + " - " + str(oldError) + " = " + str(candidateError-oldError) + "\n")

	return currentinfectionChance, currentdeathChance, candidateError

def gradientDescent(infectionChance, deathChance, error, precision, coeff):
	currentinfectionChance = infectionChance;
	currentdeathChance = deathChance;
	lastErr = error;
	
	while True:
		newinfectionChance, newdeathChance, newError = makeBetter(currentinfectionChance, currentdeathChance, precision, coeff, lastErr);
		
		if abs(lastErr - newError) < precision:
			break

		lastErr = newError
		currentinfectionChance = newinfectionChance
		currentdeathChance = newdeathChance
		
		if currentinfectionChance <= 0 or currentinfectionChance >= 1:
			break 
		
		if currentdeathChance <= 0 or currentdeathChance >= 1:
			break 
		
	return currentinfectionChance, currentdeathChance, lastErr

def findConstants():
	currentinfectionChance=0;
	currentdeathChance=0;
	currentError=10**20
	i = 0;
	while i < 10:
		infectionChance = random.uniform(0.001, 0.1)
		deathChance = random.uniform(0.001, 0.1)
		try:
			error = errorCalculation(infectionChance, deathChance);
		except ValueError as e:
			continue;
		
		log.write(str(i) + "/" + str(10) + " - starting with " + str(infectionChance) + " " + str(deathChance) + " " + str(error) + "\n");

		try:
			infectionChance, deathChance, error = gradientDescent(infectionChance, deathChance, error, 10, 0.02)
		except ValueError as error:
			continue;

		if error < currentError: 
			currentinfectionChance = infectionChance
			currentdeathChance = deathChance
			currentError = error

		i+=1;

	return currentinfectionChance, currentdeathChance, currentError

a, b, c = findConstants()
result.write(str(a)+ " " + str(b) + " " + str(c) + "\n")
days, data = test(1000, a, b)
result.write(str(days) + "\n")
result.write(str(data))