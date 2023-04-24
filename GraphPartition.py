############################
## 作用：实现图划分算法

############################
from typing import List
import networkx as nx
import pymetis
import numpy as np
import load
from DataStruct.TreeNode import TreeNode
from DataStruct.TreeNode import Status

GTree: List[TreeNode] = []


# 输入：图的邻接表，每一次划分为多少个图
# 输出：划分后的四个子图中的点
def graphPartition(adj_list: List[list]):
    n_cuts, membership = pymetis.part_graph(4, adjacency=adj_list)
    # print(membership)
    nodes_part_0 = np.argwhere(np.array(membership) == 0).ravel()
    nodes_part_1 = np.argwhere(np.array(membership) == 1).ravel()
    nodes_part_2 = np.argwhere(np.array(membership) == 2).ravel()
    nodes_part_3 = np.argwhere(np.array(membership) == 3).ravel()
    return nodes_part_0, nodes_part_1, nodes_part_2, nodes_part_3


def build():
    root = TreeNode()
    root.isleaf = False
    root.father = -1
    GTree.append(root)

    buildstack: List[Status] = []
    rootstatus = Status(0, [i for i in range(0, 5624)])


if __name__ == "__main__":
    load.init_input()
    build()
    print(load.G.number_of_nodes())
    adj_list = [
        np.array([4, 2, 1]),
        np.array([0, 2, 3]),
        np.array([4, 3, 1, 0]),
        np.array([1, 2, 5, 6]),
        np.array([0, 2, 5]),
        np.array([4, 3, 6]),
        np.array([5, 3])
    ]
    part0, part1, part2, part3 = graphPartition(adj_list)
    print('part0:', part0)
    print('part1:', part1)
    print('part0:', part2)
    print('part1:', part3)
