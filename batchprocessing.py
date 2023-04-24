# 批处理阶段
## 基于local-cache的最短路批处理算法
### step1:使用zig-zag分解法将查询集分解
### step2:基于缓存的批处理算法
## 基于region-to-region的批处理算法
### step1:查询集分解
### step2:查询集批处理
import networkx as nx
from zigzag_decomposition import zigzag
from region2region_decomposition import coClustering
from preprocessing import G
import random
CONST_MAP = 6000


# 输出：最短路查询集，存储结果的文件路径名
# 输出：结果存储在filename_ansdata_localCache所在的文件中
def localCache_BatchProcess(queryset, filename_ansdata_localCache='./data/ansdata_localCache.txt'):
    ans_localCache = {}
    zigzag_queryset = zigzag(queryset)
    # print(zigzag_queryset)
    for tmp_list in zigzag_queryset:
        start_node = tmp_list[0] // CONST_MAP
        length_dict = nx.single_source_dijkstra_path_length(G, start_node)
        for i in tmp_list:
            end_node = i % CONST_MAP
            ans_localCache[i] = length_dict[end_node]
    # for i in ans_localCache:
    #     print(i, " value", ans_localCache[i])
    with open(filename_ansdata_localCache, 'w') as f:
        for i in ans_localCache:
            f.write("{},{}\n".format(i, ans_localCache[i]))


def region2region_BatchProcess(queryset, filename_ansdata_region2region='./data/ansdata_region2region.txt'):
    ans_region2region = {}
    region2region_queryset = coClustering(queryset)
    for tmp_list in region2region_queryset:
        start_node = random.randint(0, 5623)
        end_node = random.randint(0, 5623)
        length_dict = nx.shortest_path_length(G, source=start_node, target=end_node)
        ans_region2region[start_node * CONST_MAP + end_node] = length_dict


if __name__ == "__main__":
    # print(queryset)
    # print(len(queryset))
    print("batchprocessing main")
    localCache_BatchProcess()
