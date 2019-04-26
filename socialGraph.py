import random
 
def generateGraph(n,m,p):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
 
    edges = [];
 
    for x in range(n):
        for y in range(m):
            for i in range(4):
                nx = (n + x + dx[i])%n
                ny = (m + y + dy[i])%m
 
                v0 = x * n + y
                v1 = nx * n + ny
                if (v0 < v1):
                    edges.append([v0, v1])
 
    #print(edges)
 
    for i in range(len(edges)):
        if random.random() <= p:
            v3 = edges[i][0]
 
            while v3 == edges[i][0] or v3 == edges[i][1]:
                v3 = random.randint(0,n*m-1)
            edges[i][1] = v3
            #print(edges[i])
 
    return edges