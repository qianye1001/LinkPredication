from Tools.CreateGraph import CreateGraph
import networkx as nx
from Tools.GetEdges import GetEdges

print("读取数据")
test_edges = GetEdges(r"..\Date\test_date.txt",109580)
non_edges = GetEdges(r"..\Date\non_edges.txt",976560)
G = CreateGraph("../Date/课程设计数据集.txt").GetNx()
G.remove_edges_from(test_edges)

