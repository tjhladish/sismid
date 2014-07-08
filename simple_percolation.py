#!/usr/bin/python
# 0.) Import functions
from networkx import *
from random import *

# 1.) Define parameters
T = 0.9        # probability of transmission

# 2.) Construct network
G=Graph()
#################################################
# Insert code to construct the network
# e.g. what you developed for Lab 2, Section 3
#################################################
net_size = float(G.order())

# 3.) Store node states
p_zero = choice(G.nodes()) # Randomly choose one node
infected    = [p_zero]
recovered   = []

# 4.) Run the simulation
while len(infected) > 0:
    v = infected.pop(0)
    for u in G.neighbors(v):
        # We need to make sure Node u is still susceptible
        if u not in infected and u not in recovered:
            if random() < T:
                infected.append(u)
    recovered.append(v)

# 5.) Tally the total fraction that got infected
epi_size = len(recovered)/net_size
print epi_size
