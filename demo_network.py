import networkx as nx
import matplotlib.pyplot as plt
import pymetis
import numpy as np

if __name__ == '__main__':
    G = nx.DiGraph()
    G.add_edges_from([(0,4),(0,2),(0,1),
                      (1,0),(1,2),(1,3),
                      (2,4),(2,3),(2,1),(2,0),
                      (3,1),(3,2),(3,5),(3,6),
                      (4,0),(4,2),(4,5),
                      (5,4),(5,3),(5,6),
                      (6,5),(6,3)
                      ])
    nx.draw(G,with_labels=True)
    plt.show()
    adj_list = [
        np.array([4, 2, 1]),
        np.array([0, 2, 3]),
        np.array([4, 3, 1, 0]),
        np.array([1, 2, 5, 6]),
        np.array([0, 2, 5]),
        np.array([4, 3, 6]),
        np.array([5, 3])
    ]

    n_cuts, membership = pymetis.part_graph(2, adjacency=adj_list)
    print('membership', membership)
    nodes_part_0 = np.argwhere(np.array(membership) == 0).ravel()
    nodes_part_1 = np.argwhere(np.array(membership) == 1).ravel()
    print('nodes0',nodes_part_0)
    print('nodes1',nodes_part_1)
    G1 = nx.DiGraph()
    G1.add_nodes_from(nodes_part_0)
    nx.draw(G1, with_labels=True)
    plt.show()
    # num_vertices = G.number_of_nodes()
    # (partitions_obj, edgecuts) = metis.part_graph(adjacency_list, nparts=2)
    # print('Partition assignments:', partitions_obj)
    # print('Number of edge cuts:', edgecuts)
    # nx.draw(G, with_labels=True)
    # plt.show()

    # path = nx.dijkstra_path(G,source=0,target=7)
    # print('节点0到7的路径：', path)
    # print('dijkstra方法寻找最短距离：')
    # distance = nx.dijkstra_path_length(G, source=0, target=7)
    # print('节点0到7的距离为：', distance)
