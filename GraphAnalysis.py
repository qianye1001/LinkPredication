from CreateGraph import CreateGraph
import json

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx import in_degree_centrality, degree, degree_histogram

from PageRank import PageRank


class GraphAnalysis:
    def __init__(self, G):
        self.G = G
        self.G.remove_edges_from(nx.selfloop_edges(G))

    def AnaDegree(self):
        # print(self.G.in_degree())
        temp = []
        with open("1.csv", "w", encoding='utf8') as f:
            for x in nx.degree(self.G):
                temp.append(x[1])
                f.write(str(x[1]))
                f.write('\n')
        temp.sort(reverse=True)

        plt.loglog(range(0, len(temp)), temp, 0.8)
        plt.show()
        plt.scatter(range(0, len(temp)), temp, 0.8)
        plt.show()

    def CN(self):

        preds = nx.resource_allocation_index(G)
        for u, v, p in preds:
            print(f"({u}, {v}) -> {p:.8f}")



if __name__ == '__main__':
    G = CreateGraph("课程设计数据集.txt").GetNx()
    GA = GraphAnalysis(G)
    GA.CN()

    # G.remove_edges_from(nx.selfloop_edges(G))
    # aaa = nx.core_number(G)
    # plt.scatter(range(0, len(aaa.values())), sorted(aaa.values()), 0.8)
    # plt.show()
    # temp = {}
    # for x in aaa.values():
    #     if str(x) not in temp:
    #         temp[str(x)] = 1
    #     else:
    #         temp[str(x)] = temp[str(x)] + 1
    # fig, ax = plt.subplots(figsize=(10, 7))
    # ax.bar(x=temp.keys(), height=temp.values())
    # ax.set_title("Simple Bar Plot", fontsize=15)
    # plt.show()
    pass
