from preprocessing import init_input, G
from filtration import filtration
from batchprocessing import localCache_BatchProcess, region2region_BatchProcess
import time

if __name__ == '__main__':
    print("main.py")
    # 预处理阶段：建立G树，建立倒排索引，建立图
    init_input()
    # print("G:nodenumber", G.number_of_nodes())

    # 读入查询
    dict_query = {}
    query_filename = './data/query_of_4keywords/query_datasize1k.txt'
    with open(query_filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmp = [x.strip() for x in line.split(',') if x.strip()]
            tmp_nodeid = int(tmp[0])
            tmp_keywordlist = tmp[1:]
            dict_query[tmp_nodeid] = tmp_keywordlist

    # 过滤阶段：对于每个查询q根据过滤边界过滤出候选群组=>将将候选群组转化成最短路查询集
    print("进行过滤阶段")
    start_time_filtration = time.time()
    querySet = []
    # query_number = 0
    for i in dict_query:
        query_nodeid = i
        query_keywords = dict_query[query_nodeid]
        tmp_queryset = filtration(query_nodeid, query_keywords)
        # print("len: tmp_queryset:", len(tmp_queryset))
        # print(query_number)
        # query_number = query_number + 1
        querySet.extend(tmp_queryset)
    print("len_queryset：", len(querySet))
    end_time_filtration = time.time()
    # 批处理阶段：基于localcache的批处理算法/基于region-to-region的批处理算法
    print("进行批处理阶段")

    print("利用localcache进行批处理")
    start_time_localcache = time.time()
    filename_ansdata_localCache = './data/ansdata_localCache.txt'
    localCache_BatchProcess(querySet, filename_ansdata_localCache)
    end_time_localcache = time.time()

    print("利用region-to-region进行批处理")
    start_time_region_to_region = time.time()
    filename_ansdata_region2region = './data/ansdata_region2region.txt'
    region2region_BatchProcess(querySet, filename_ansdata_region2region)
    end_time_retion_to_region = time.time()

    deltatime_filtration = end_time_filtration - start_time_filtration
    deltatime_localcache = end_time_localcache - start_time_localcache
    deltatime_region2region = end_time_retion_to_region - start_time_region_to_region
    print("过滤阶段运行时间：", deltatime_filtration)
    print("利用locache进行批处理运行时间：", deltatime_localcache)
    print("locache 运行总时间：", deltatime_filtration + deltatime_localcache)
    print("利用region-to-region进行批处理运行时间：", deltatime_region2region)
    print("region-to-region 运行总时间：", deltatime_filtration + deltatime_region2region)

