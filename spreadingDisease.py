import random
from socialGraph import generateGraph

class Human:
	def __init__(self, id): 
		self.id = id
		self.status = 0
		self.friends = [];
		self.timeInfected = 0;

	def getInfected(self, t):
		if self.status == 0:
			self.status = 1
			self.timeInfected = t;

	def getRemoved(self):
		self.status = 2

	def addConnection(self, id):
		if id not in self.friends:
			self.friends.append(id)

	def infect(self, infectionChance, t):
		for friendId in self.friends:
			#lets not infect dead people
			if humans[friendId].status==2:
				continue
			#infect at random
			num = random.random()
			if num <= infectionChance:
				humans[friendId].getInfected(t)


	def heal(self, deathchance, t):
		#kill at random
		num = random.random()
		if num < deathchance:
			self.getRemoved()

humans = []

def killPeople(infectionChance, deathchance):
	humans.clear()
	resultInfected = []
	resultInfected.append(7)
	
	for i in range(256):
		humans.append(Human(i))
	
	sum = 0
	edges = generateGraph(16,16,0.4)
	
	for edge in edges:
		a=edge[0]
		b=edge[1]

		humans[a].addConnection(b)
		humans[b].addConnection(a)

	for i in range(7):
		humans[i].getInfected(0);

	t = 1;
	
	while True:
		infected = [i for i in humans if i.status==1]
		if len(infected) == 0:
			break;

		for person in infected:
			person.infect(infectionChance, t)

		infected = [i for i in humans if i.status==1]

		for person in infected:
			person.heal(deathchance, t);

		resultInfected.append(len(infected))

		t+=1

	return resultInfected