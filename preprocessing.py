# 预处理阶段
## 建立图
## 建立倒排索引：{keyword1:[node1,node2,node3];}
## 建立G树
import json
import networkx as nx
from typing import Dict, List
from DataStruct.Node import Node

filename1 = './data/xuEdges_I.json'
filename2 = './data/xuNodes_I.json'

G = nx.Graph()  # 上海徐汇区的图
dict_keyword2node: Dict[str, List[int]] = {}  # 倒排列表：关键字到节点
keyword_list = []
NodeDict: Dict[str, int] = {}  # 将所有顶点编号进行映射
Nodes: List[Node] = []


# 将顶点映射到[0-5623]，建立邻接表
def init_input():
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
            # print(k)
            if k not in dict_keyword2node:  # 如果字典中没有这个键
                dict_keyword2node[k] = []
            dict_keyword2node[k].append(NodeNumber)
            if k not in keyword_list:
                keyword_list.append(k)
        # 此处以上是用networkx建立的路网

        # 此处以下是自己建立的路网
        # tmp_node = Node(NodeNumber, False, tmp_lat, tmp_lng,
        #                 len(itm1["poiTypeName"]), itm1["poiTypeName"],
        #                 itm1["poiTypeId"], itm1["subPoiTypeId"])
        # Nodes.append(tmp_node)
        # 此处以上是自己建立的路网
        NodeNumber = NodeNumber + 1
    # 将所有的关键字存储到'./data/keywordlist.txt'中
    with open('./data/keywordslist.txt', 'w') as f:
        for i in keyword_list:
            f.write('{}\n'.format(i))

    # 建立邻接表
    for itm2 in EdgesData:
        spId = NodeDict[itm2["spId"]]
        epId = NodeDict[itm2["epId"]]
        length = itm2["length"]
        # Nodes[spId].adjNodes.append(epId)
        # Nodes[spId].adjWeight.append(length)
        if (spId, epId) not in G.edges:
            G.add_weighted_edges_from([(spId, epId, length)])  # 向图中添加有向边
    G.add_weighted_edges_from([(0, 623, 1000.0), (0, 2045, 1000.0)])




if __name__ == '__main__':
    # print(NodesData)
    init_input()
    print("keyword number:", len(keyword_list))
    print('图中边的个数：', G.number_of_edges())
    print('图中点的个数：', G.number_of_nodes())
    print(nx.is_connected(G))
    # for i in dict_keyword2node:
    #     if len(dict_keyword2node[i]) == 0:
    #         print("!!!")
        # print(i)
        # print(len(dict_keyword2node[i]))
    # for i in dict_keyword2node:
    #     print(i)
