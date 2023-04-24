from region2region_decomposition import coClustering

if __name__ == '__main__':
    original_list = [x for x in range(0, 10000)]
    res = coClustering(original_list)
    for t in res:
        print(t)
    print("len: ", len(res))

