import random

import networkx as nx

from Tools.CreateGraph import CreateGraph

G = CreateGraph("../Date/课程设计数据集.txt").GetNx()
random.seed(1)
interval = random.randint(1000, 10000)
count = 0
with open("../Date/non_edges.txt", "w", encoding='utf8') as f:
    for x in nx.non_edges(G):
        count = count + 1
        if count == interval:
            f.write(str(x[0]) + ' ' + str(x[1]))
            f.write('\n')
            interval = random.randint(200, 500)
            count = 0
