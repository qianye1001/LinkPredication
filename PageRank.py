import numpy as np
import random


def create_data(N, alpha=0.5):  # random > alpha, then here is a edge.
    G = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if random.random() < alpha:
                G[i][j] = 1
    return G


class PageRank:
    def __init__(self, graph):
        self.node_num = graph.shape[0]
        self.graph = graph
        self.map = self.get_map()

    def get_map(self):
        map = np.zeros((self.node_num, self.node_num))
        for i in range(self.node_num):
            D_i = sum(self.graph[i])
            if D_i == 0:
                continue
            for j in range(self.node_num):
                map[j][i] = self.graph[i][j] / D_i
        return map

    def count_pr(self, t=300, eps=1e-6, beta=0.8):
        r = np.ones(self.node_num) / self.node_num
        teleport = np.ones(self.node_num) / self.node_num
        for time in range(t):
            r_new = beta * np.dot(self.map, r) + (1 - beta) * teleport
            if np.linalg.norm(r_new - r) < eps:
                break
            r = r_new.copy()
        return r_new


if __name__ == '__main__':
    G = create_data(10)
    pr = PageRank(G)
    print(pr.count_pr())

