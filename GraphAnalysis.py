import random

from CreateGraph import CreateGraph
import json

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx import in_degree_centrality, degree, degree_histogram

from PageRank import PageRank


class GraphAnalysis:
    def __init__(self, G, DiG):
        self.G = G
        self.DiG = DiG
        self.G.remove_edges_from(nx.selfloop_edges(G))
        self.DiG.remove_edges_from(nx.selfloop_edges(DiG))

    def AnaDegree(self):
        temp = []
        for x in nx.degree(self.G):
            temp.append(x[1])
        temp.sort(reverse=True)

        plt.loglog(range(0, len(temp)), temp, 0.8)
        plt.savefig("Degree_ll.jpg")
        plt.scatter(range(0, len(temp)), temp, 0.8)
        plt.savefig("Degree_sc.jpg")

    def CN(self):

        preds = nx.resource_allocation_index(G)
        for u, v, p in preds:
            print(f"({u}, {v}) -> {p:.8f}")

    def DevideDate(self):
        count = 0
        random.seed(1)
        with open("test.txt", "w", encoding='utf8') as f:
            while (count < 50000):
                print(count)
                i = random.randint(1, 944160 - 50000)
                s, e = list(nx.edges(self.G))[i]
                if nx.degree(self.G)[s] > 1 and nx.degree(self.G)[e] > 1:
                    self.G.remove_edge(s, e)
                    f.write(str(s) + ' ' + str(e))
                    f.write('\n')
                    count = count + 1


if __name__ == '__main__':
    G = CreateGraph("课程设计数据集.txt").GetNx()
    DiG = CreateGraph("课程设计数据集.txt").GetNxDi()
    GA = GraphAnalysis(G, DiG)
    a = GA.DevideDate()
    pass
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
