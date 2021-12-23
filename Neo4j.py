from py2neo import Node, Graph, Relationship, NodeMatcher, data
from tqdm import tqdm

from CreateGraph import CreateGraph


def Init():
    graph = Graph("http://localhost:7474/browser/", auth=("neo4j", "123456"))

    print('graph 连接成功，开始清库')
    graph.delete_all()

    G = CreateGraph("课程设计数据集.txt")
    NodeList = []
    for n in G.nodes:
        NodeList.append(Node('node', name=n))
    for e in tqdm(G.edges):
        graph.create(Relationship(NodeList[e[0] - 1], 'edge', NodeList[e[1] - 1]))
        # graph.create(Relationship(NodeList[e[1] - 1], 'edge', NodeList[e[0] - 1]))


if __name__ == '__main__':
    Init()
