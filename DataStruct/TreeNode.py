from typing import List


class Status:
    def __init__(self, tnid=0, nset: List[int] = []):
        self.tnid = tnid
        self.nset = nset


class TreeNode:
    def __init__(self, father=0, borders: List[int] = [], childen: List[int] = [],
                 isleaf=False, leafnodes: List[int] = [],
                 union_borders: List[int] = [], mind: List[int] = [], nonleafinvlist: List[int] = [],
                 leafinvlist: List[int] = [], up_pos: List[int] = [], current_pos: List[int] = []):
        self.borders = borders  # 边界节点集合
        self.childen = childen  #
        self.ifleaf = isleaf  # 是否是叶子节点
        self.leafnodes = leafnodes  # 如果是叶子节点
        self.father = father  # 父节点
        self.union_borders = union_borders  # for non leaf node
        self.mind = mind  # min dis

        self.nonleafinvlist = nonleafinvlist  #
        self.leafinvlist = leafinvlist  #
        self.up_pos = up_pos  #
        self.current_pos = current_pos  #
