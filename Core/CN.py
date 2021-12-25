import random

from Tools.CreateGraph import CreateGraph
import networkx as nx
from Tools.GetEdges import GetEdges

print("读取数据")
test_edges = GetEdges(r"..\Date\test_date.txt",109580)
non_edges = GetEdges(r"..\Date\non_edges.txt",976560)
G = CreateGraph("../Date/课程设计数据集.txt").GetNx()
G.remove_edges_from(test_edges)

print("计算CCPA开始")
jc_t = nx.common_neighbor_centrality(G, test_edges)
jc_n = nx.common_neighbor_centrality(G, non_edges)
print("计算CCPA结束")


count = 0
score = 0
for t in jc_t:
    for n in jc_n:
        count = count + 1
        if t[2] > n[2]:
            score = score + 1
        elif t[2] == n[2]:
            score = score + 0.5
print(score/count)


