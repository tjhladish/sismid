#!/usr/bin/python
from networkx import *
from random import *
from pylab import mean

### Define percolation simulation, using graph G and transmissibility T
def percolate(G, T):
    states = dict([(node, 's') for node in G.nodes()]) 

    p_zero = choice(G.nodes())
    states[p_zero] = 'i'
    infected = [p_zero]
    recovered = []

    while len(infected) > 0:
        v = infected.pop(0)
        for u in G.neighbors(v):
            if states[u] == 's' and random() < T:
                states[u] = 'i'
                infected.append(u)
        states[v] = 'r'
        recovered.append(v)
    ### return the epi size as a fraction of the ORIGINAL population
    return len(recovered)/float(net_size)


### Set transmissibility
### Corresponds to an R0 of about 2.5 for the urban network
T = 0.1357 

### Build urban network
file = open("urban_net.csv")
G = Graph()
for edge in file:
    G.add_edge(*edge.strip().split(','))
net_size = G.order()

### Random vaccination strategy
for n in G.nodes():
    if random() < 0.178:
        G.remove_edges_from(G.edges(n))
        # more verbose, but same result:
        # for e in G.edges(n):
        #   G.remove_edge(e)


### Run the simulation a bunch of times
results = []
for i in range(100):
    s =  percolate(G, T)
    results.append(s)

### Print the mean epidemic size
print mean(results)
