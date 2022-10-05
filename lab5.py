import numpy as np
from random import *
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

size = 100
ed = 200
array = np.zeros((size, size), dtype=int)

edges = 0

while edges < ed:
    edges += 1
    a = 1
    b = 1
    while a == b or array[a - 1][b - 1] == 1:
        a = randint(1, size)
        b = randint(1, size)
    array[a - 1][b - 1] = 1
    array[b - 1][a - 1] = 1

table = pd.DataFrame(data=array, columns=np.arange(1, array.shape[0] + 1), index=np.arange(1, array.shape[1] + 1))
print(table)

graph = {}
for i in range(1, size + 1):
    s = []
    for j in range(1, size + 1):
        if array[i - 1][j - 1] == 1:
            s.append(str(j))
    graph[str(i)] = s

for key, val in graph.items():
    print('{}:{}'.format(key, val))

G = nx.Graph(array)

options = {"font_size": 0, "node_size": 10, "node_color": "red", "edgecolors": "red", "linewidths": 1, "width": 1}

nx.draw(G, pos=nx.spring_layout(G), **options)
plt.savefig(fname="C:\Уник\Анализ и разработка алгоритмов\ЛР5\graph_1.png", dpi=300, facecolor='w', edgecolor='w',
            orientation='portrait')

mapping = {}
for i in range(0, array.shape[0]):
    mapping[i] = i + 1

G = nx.relabel_nodes(G, mapping)

S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
for i in range(nx.number_connected_components(G)):
    print(S[i].nodes)
    print()

s = randint(1, size)
t = randint(1, size)
print(f'{s} --> {t}')
p = nx.shortest_path(G, s, t)
print(p)
