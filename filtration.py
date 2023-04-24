# 过滤阶段
## 对于每个查询q根据过滤边界过滤出候选群组
### 过滤边界确定：
####          若查询q的关键字集合为{k1,k2,...,kt}找到每个关键字的近邻oi
### 根据过滤边界筛选出覆盖查询关键字集合的空间对象
### 对这些空间对象做笛卡尔积得到候选群组
## 将候选群组转化成最短路查询集
import itertools
import networkx as nx
from preprocessing import G, dict_keyword2node
from typing import List

CONST_MAP = 6000



# 作用：找到过滤边界
# 输入：查询q所在的节点id，查询关键字集合
# 输出：每个关键字的近邻
def get_filtration_boundry(nodeid: int, keywords: List[str]):
    # print("func get_filtration_boundry")
    res = 0.0
    o_set = []  # 存储每个关键字的近邻
    distances = nx.single_source_dijkstra_path_length(G, source=nodeid)
    # print(distances)
    # 以下代码是求得每个关键字的近邻
    for k in keywords:
        tmp_list = dict_keyword2node[k]  # 能满足每个关键字的空间对象集合
        # print("k: ", k, " tmp_list:", tmp_list)
        target_node = -1
        target_node_distances = 1000000000
        for tmp_node in tmp_list:  # 枚举满足每个关键字的空间对象集合，找到每个关键字的近邻o
            tmp_dis = distances[tmp_node]
            if tmp_dis < target_node_distances:
                target_node_distances = tmp_dis
                target_node = tmp_node
        res = max(res, target_node_distances)
        o_set.append(target_node)
    # 以上代码是求每个关键字的近邻，保存在o_set中

    # 求关键字的近邻中任意两元素的最短路距离
    for i in o_set:
        tmp_distances, tmp_paths = nx.single_source_dijkstra(G, source=i)
        for j in o_set:
            res = max(res, tmp_distances[j])
    return res


# 作用：得到候选群组
# 输入：查询的位置（节点id），关键字集合
# 输出：候选群组
def get_candidateGroup(nodeid: int, keywords: List[str]):
    # print("get_candidateGroup")
    # print("nodeid:", nodeid)
    # print("keywords:", keywords)
    res = []
    distances, paths = nx.single_source_dijkstra(G, source=nodeid)
    # 过滤边界的确定
    filtration_boundry = get_filtration_boundry(nodeid, keywords)
    # print("filtration_boundry:", filtration_boundry)
    dict_keword2candidateset = {}  # 关键字到覆盖该关键字集合的映射
    # 根据过滤边界选出满足每个关键字的空间对象（求dict_keyword2candidateset）
    for k in keywords:
        dict_keword2candidateset[k] = []
        for tmp_node in dict_keyword2node[k]:
            if distances[tmp_node] <= filtration_boundry:
                dict_keword2candidateset[k].append(tmp_node)
    # 对这些空间对象做笛卡尔积运算
    value_list = list(dict_keword2candidateset.values())
    cartesian_product = itertools.product(*value_list)
    for i in cartesian_product:
        res.append(i)
    return res


# 作用：根据候选群组得到最短路查询集合
# 输入：候选群组
# 输出：最短路查询集合
def get_shortestPathSet(candidateGroupSet):
    res = []
    for i in candidateGroupSet:
        result_combinations = list(itertools.combinations(i, 2))
        for combination in result_combinations:
            res.append(combination)
    return res


# 输入：最短路查询集合（元组形式）
# 输出：最短路查询集合（将元组形式map成一个数）
def query_map(querySet_tuple):
    # print("query_map")
    res = []
    for i in querySet_tuple:
        if i[0] > i[1]:
            tmp = i[1] * CONST_MAP + i[0]
        else:
            tmp = i[0] * CONST_MAP + i[1]
        if tmp not in res:
            res.append(tmp)
    return res


# 输入：查询点的id，查询的关键字集合
# 输出：最短路集合
def filtration(query_nodeid, query_keywords):
    # print("start init_input")
    # init_input()
    querySet_Map = []
    candidateGroupSet = get_candidateGroup(query_nodeid, query_keywords)
    # print("len: candidateGroupset", len(candidateGroupSet))
    # 获得元组形式的查询集
    querySet_Tuple = get_shortestPathSet(candidateGroupSet)
    # print(pathSet)
    # print("len: pathset_tuple", len(querySet_Tuple))
    # 获得哈希后的查询集
    tmpSet = query_map(querySet_Tuple)
    querySet_Map.extend(tmpSet)
    # print("len: queryset:", len(querySet))
    # for i in querySet:
    #     print(i//CONST_MAP, i % CONST_MAP)
    return querySet_Map


if __name__ == '__main__':
    filtration(3131, ['060411' , '080601'])
    # print("nodesnumber",G.number_of_nodes())
