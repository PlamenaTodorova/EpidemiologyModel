import numpy as np
import random
import time
import math
from mpmath import mp

mp.dps = 20

sucseptible = [254, 235, 201, 153.5, 121, 108, 97, 90, 83 ];
infected = [7, 14.5, 22, 29, 21, 8, 8, 4, 0];
step = 0.01;
samplePoints=np.arange(0, 5, 0.5);
dH = 0.001;

def solveEquatuon(bate, gamma):
	solveEquatuon(beta, gamma, sucseptible[0], infected[0])

def solveEquation(beta, gamma, startSusceptible, startInfected):
	currentS = startSusceptible
	currentI = startInfected

	calculatedSucseptible = []
	calculatedSucseptible.append(currentS)

	calculatedInfected = []
	calculatedInfected.append(currentI)
	
	while currentI > 1:
		dS = -beta * currentS *currentI;
		dI = beta * currentS *currentI - gamma*currentI;

		currentS += dS*step;
		currentI += dI*step;

		calculatedSucseptible.append(currentS)
		calculatedInfected.append(currentI)

	return calculatedSucseptible, calculatedInfected