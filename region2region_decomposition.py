# co-clustering 分解法
# 输入：最短路查询集合
# 输出：多个簇，这些簇中的每个查询彼此的起点终点很接近
import random
CONST_MAP = 6000
def coClustering(querySet):
    res = []
    i = 0
    while i < len(querySet):
        random_length = random.randint(10, 100)
        res.append(querySet[i:i + random_length])
        i += random_length
    return res
