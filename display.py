import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation as animation
from spreadingDisease import killPeople

killPeople(0.011815420986557242, 0.016641076237243986, 7, 0.25, False)

G = nx.Graph()

log = open("log1.txt", 'r')
elements=[];
for line in log:
	elements.append(line);

edges=[]

for i in elements[0][2:-3].split('], ['):
	edge = i.split(', ');
	edges.append((edge[0], edge[1]))

G.add_edges_from(edges);

pos=nx.spring_layout(G, k=0.8)

susceptible=[]
infected=[]
immune=[]

for i in elements[1][1:-2].split(', '):
	susceptible.append(i)

for i in elements[2][1:-2].split(', '):
	infected.append(i)

for i in elements[3][1:-2].split(', '):
	immune.append(i)

nx.draw_networkx_nodes(G, pos,
                       nodelist=susceptible,
                       node_color='b',
                       node_size=50)

nx.draw_networkx_nodes(G, pos,
                       nodelist=infected,
                       node_color='r',
                       node_size=50)

nx.draw_networkx_nodes(G, pos,
                       nodelist=immune,
                       node_color='g',
                       node_size=50)


nx.draw_networkx_edges(G, pos=pos, alpha=0.2)

plt.show()