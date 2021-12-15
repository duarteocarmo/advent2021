import networkx as nx
import numpy as np


with open("15/input.txt") as file:
    lines = file.read().strip()

matrix = np.array([list(map(int, l)) for l in lines.split()])
G = nx.grid_2d_graph(*matrix.shape, create_using=nx.DiGraph)

for _, v, d in G.edges(data=True):
    d["weight"] = matrix[v]

source, *_, target = G.nodes

print(nx.shortest_path_length(G, source, target, weight="weight"))
