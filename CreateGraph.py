import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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
            graph[end-1][start-1] = 1
        return graph


if __name__ == '__main__':
    # G = CreateGraph("课程设计数据集.txt").GetNx()
    # preds = nx.jaccard_coefficient(G)
    #
    # for u, v, p in preds:
    #     print(f"({u}, {v}) -> {p:.8f}")
    G = CreateGraph("课程设计数据集.txt").GetMatrix()
    pr = PageRank(G)
    print(pr.count_pr())