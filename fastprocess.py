# 输入：[nodeid,[keywordset]]
# 输出：最优群组的经纬度集合
from typing import Dict, List
import networkx as nx
import json

G = nx.Graph()  # 上海徐汇区的图
dict_keyword2node: Dict[str, List[int]] = {}  # 倒排列表：关键字到节点
keyword_list = []
NodeDict: Dict[str, int] = {}  # 将所有顶点编号进行映射

# 将顶点映射到[0-5623]，建立邻接表
def init_input():
    filename1 = './data/xuEdges_I.json'
    filename2 = './data/xuNodes_I.json'
    with open(filename1, 'r', encoding='utf-8') as f:
        Data1 = json.load(f)
        EdgesData = Data1['xuEdges_I']
    with open(filename2, 'r', encoding='utf-8') as f:
        Data2 = json.load(f)
        NodesData = Data2['xuNodes_I']

    NodeNumber = 0
    #  将顶点映射到[0-5623]，将顶点加到G中和Nodes中
    for itm1 in NodesData:
        tmp_id, tmp_keyword, tmp_lat, tmp_lng = itm1['nId'], itm1['poiTypeId'], itm1['lat'], itm1['lng']
        NodeDict[tmp_id] = NodeNumber
        tmp_keywordlist = []
        # 对关键字的处理
        if tmp_keyword != 'null':
            if len(tmp_keyword) == 6:
                tmp_keywordlist.append(tmp_keyword)
            else:
                split_list = tmp_keyword.split('|')
                tmp_keywordlist = split_list
        # 此处以下是用networkx建立的路网
        G.add_node(NodeNumber)
        nx.set_node_attributes(G, {NodeNumber: tmp_lng}, "lng")
        nx.set_node_attributes(G, {NodeNumber: tmp_lat}, "lat")
        nx.set_node_attributes(G, {NodeNumber: tmp_keywordlist}, "keywordlist")
        for k in tmp_keywordlist:  # 对关键字的处理
            if k not in dict_keyword2node:  # 如果字典中没有这个键
                dict_keyword2node[k] = []
            dict_keyword2node[k].append(NodeNumber)
            if k not in keyword_list:
                keyword_list.append(k)
        # 此处以上是用networkx建立的路网

        NodeNumber = NodeNumber + 1

    # 建立邻接表
    for itm2 in EdgesData:
        spId = NodeDict[itm2["spId"]]
        epId = NodeDict[itm2["epId"]]
        length = itm2["length"]
        if (spId, epId) not in G.edges:
            G.add_weighted_edges_from([(spId, epId, length)])  # 向图中添加有向边
    G.add_weighted_edges_from([(0, 623, 1000.0), (0, 2045, 1000.0)])

def get_nodeId(query_nodeid, query_keywords):
    o_set = []  # 存储每个关键字的近邻
    distances = nx.single_source_dijkstra_path_length(G, source=query_nodeid)
    # print(distances)
    # 以下代码是求得每个关键字的近邻
    for k in query_keywords:
        tmp_list = dict_keyword2node[k]  # 能满足每个关键字的空间对象集合
        # print("k: ", k, " tmp_list:", tmp_list)
        target_node = -1
        target_node_distances = 1000000000
        for tmp_node in tmp_list:  # 枚举满足每个关键字的空间对象集合，找到每个关键字的近邻o
            if distances[tmp_node] < target_node_distances:
                target_node_distances = distances[tmp_node]
                target_node = tmp_node
        o_set.append(target_node)
    # print(o_set)
    return o_set

def nodeId2Position(nodeIdSet):
    positionSet = []
    for nodeid in nodeIdSet:
        tmp_lat = G.nodes[nodeid]['lat']
        tmp_lng = G.nodes[nodeid]['lng']
        positionSet.append((tmp_lng, tmp_lat))
    return positionSet

def fastprocess(query_nodeid, query_keywords):
    init_input()
    nodeIdSet = get_nodeId(query_nodeid, query_keywords)
    nodePositionSet = nodeId2Position(nodeIdSet)
    return nodePositionSet
if __name__ == '__main__':
    query_nodeid = 3131
    query_keywords = ['060411', '080601']
    ans = fastprocess(query_nodeid, query_keywords)
    print("node_position_set:", ans)
    print("node number:", G.number_of_nodes())
