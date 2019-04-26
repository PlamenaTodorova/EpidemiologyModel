from spreadingDisease import killPeople

def test(tries, infectionChance, deathChance):
	results = []
	
	for i in range(tries):
		results.append(killPeople(infectionChance, deathChance));
	
	totalData = results[0];
	totalDays = len(results[0]);

	for i in range(tries-1):
		dataLenght = len(totalData)
		currentLenght = len(results[i+1])
		totalDays += currentLenght;

		for j in range(min(dataLenght, currentLenght)):
			totalData[j] += results[i+1][j]

		if currentLenght > dataLenght:
			for j in range(currentLenght-dataLenght):
				totalData.append(results[i+1][j+dataLenght])
	
	totalDays /= tries;

	for i in range(len(totalData)):
		totalData[i] /= tries;

	return totalDays, totalData[:int(totalDays)]