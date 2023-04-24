# zigzag 分解法(nodenumber:5624 = 2812 * 2)
# 输入：最短路查询集
# 输出：多个最短路查询集，这些最短路查询集均起点相同终点相似或者终点相同起点相似

CONST_MAP = 6000
def zigzag(queryset):
    # print("zigzag")
    res = []
    # print("!!!!")
    # zigzag_querySet = querySet
    # print("len: zigzag_queryset", len(zigzag_querySet))
    dict_nodelist = {}  # 每个节点对应的节点
    for i in range(0, 5624):
        dict_nodelist[i] = []
    for i in queryset:
        st_node = i // CONST_MAP
        ed_node = i % CONST_MAP
        # print("stnode:",st_node, "ed_node:",ed_node)
        dict_nodelist[st_node].append(ed_node)
    for i in dict_nodelist:
        tmp_list = []
        if len(dict_nodelist[i]) > 0:
            for tmp_node in dict_nodelist[i]:
                tmp_list.append(i*CONST_MAP+tmp_node)
            res.append(tmp_list)
    # for i in res:
    #     print(i)
    return res

if __name__ == '__main__':
    print("zigzag_main")
    # zigzag()