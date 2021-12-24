import json

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from networkx import in_degree_centrality, degree, degree_histogram

from PageRank import PageRank


class CreateGraph:
    def __init__(self, path):
        with open(path, 'r', encoding='utf8') as f:
            lines = f.readlines()
            edges = []
            nodes = []
            for x in lines:
                start_node = int(x.strip('\n').split("\t")[0])
                end_node = int(x.strip('\n').split("\t")[1])
                nodes.append(start_node)
                nodes.append(end_node)
                edges.append((start_node, end_node))
        nodes.sort()
        self.edges = edges
        self.nodes = set(nodes)
        self.node_num = len(self.nodes)
        self.Mod = None

    def GetNxDi(self):
        graph = nx.DiGraph()
        graph.add_edges_from(self.edges)
        return graph

    def GetNx(self):
        graph = nx.Graph()
        graph.add_edges_from(self.edges)
        return graph

    def GetMatrix(self):
        graph = np.zeros((self.node_num, self.node_num),dtype=np.int8)
        for edge in self.edges:
            start = edge[0]
            end = edge[1]
            graph[start-1][end-1] = 1
        return graph

    def SetMod(self):
        with open("NC_Mod.json",'r',encoding='utf8') as f:
            dic = json.loads(f.readline())
        self.Mod = dic


if __name__ == '__main__':
    G = CreateGraph("课程设计数据集.txt").GetNx()
    print(degree_histogram(G))
    # print(len(list(nx.selfloop_edges(G))))
    # aaa = nx.core_number(G)
    # plt.scatter(aaa.keys(),aaa.values(),0.8)
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
    # preds = nx.jaccard_coefficient(G)
    #
    # for u, v, p in preds:
    #     print(f"({u}, {v}) -> {p:.8f}")
    # G = CreateGraph("课程设计数据集.txt").GetMatrix()
    # pr = PageRank(G)
    # print(pr.count_pr())
    # G = CreateGraph("课程设计数据集.txt").SetMod()
