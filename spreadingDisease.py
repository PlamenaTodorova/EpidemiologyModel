import random
from socialGraph import generateGraph

class Human:
	def __init__(self, id): 
		self.id = id
		self.status = 0
		self.friends = [];

	def setAsImmuned(self):
		self.status = 3

	def getInfected(self):
		if self.status == 0:
			self.status = 1

	def getRemoved(self):
		self.status = 2

	def addConnection(self, id):
		if id not in self.friends:
			self.friends.append(id)

	def infect(self, infectionChance):
		for friendId in self.friends:
			#lets not infect dead people
			if humans[friendId].status>=2:
				continue
			#infect at random
			num = random.random()
			if num <= infectionChance:
				humans[friendId].getInfected()


	def heal(self, deathchance):
		#kill at random
		num = random.random()
		if num < deathchance:
			self.getRemoved()

humans = []

def killPeople(infectionChance, deathchance, startingProcent, immuneProcent, skipLog):
	log = open("log" + str(1) + ".txt", "w")
	humans.clear()
	resultInfected = []
	resultInfected.append(7)
	numPeople=256
	
	for i in range(numPeople):
		humans.append(Human(i))
	
	sum = 0
	edges = generateGraph(16,16,0.4)
	
	for edge in edges:
		a=edge[0]
		b=edge[1]

		humans[a].addConnection(b)
		humans[b].addConnection(a)

	for i in random.sample(humans, int(immuneProcent * numPeople)):
		i.setAsImmuned();

	for i in random.sample(humans, 7):
		i.getInfected();	

	if not skipLog:
		log.write(str(edges) + "\n");

		log.write(str([i.id for i in humans if i.status==0]) + "\n")
		log.write(str([i.id for i in humans if i.status==1]) + "\n")
		log.write(str([i.id for i in humans if i.status==3]) + "\n")

	t = 1;
	
	while True:
		infected = [i for i in humans if i.status==1]
		if len(infected) == 0:
			break;

		for person in infected:
			person.infect(infectionChance)

		infected = [i for i in humans if i.status==1]

		for person in infected:
			person.heal(deathchance);

		resultInfected.append(len(infected))

		if not skipLog:
			log.write(str([i.id for i in humans if i.status==0]) + "\n")	
			log.write(str([i.id for i in humans if i.status==1]) + "\n")
			log.write(str([i.id for i in humans if i.status==2]) + "\n")
			
		t+=1

	return resultInfected