#!/usr/bin/python
from networkx import *
from random import randint, expovariate

exp_int = lambda: int(round(expovariate(1)))

g = read_adjlist("sexual_net.csv", delimiter=',')

while g.size() < 300:
    n1 = g.nodes()[randint(0, g.order() - 1)]
    n2 = g.nodes()[randint(0, g.order() - 1)]
    g.add_edge(n1, n2)


times = {}

fo = open("dynamic_net.csv", 'w')

for e in g.edges():
    while e not in times:
        start = randint(-365, 365)
        end = start + exp_int()
        if end > 0:
            if start < 0:
                start = 0
            if end > 365:
                end = 365
            times[e] = (start, end)
            fo.write(','.join([e[0], e[1], str(start), str(end)]) + '\n')

fo.close()
