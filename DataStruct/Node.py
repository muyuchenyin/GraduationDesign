from typing import List


class Node:

    def __init__(self, nodeId: int, isborder: bool, lat: float, lng: float,
                 poiNum: int = 0, poiTypeName: List[str] = [],
                 poiTypeId: List[str] = [], subPoiTypeId: List[str] = [],
                 adjNodes: List[int] = [], adjWeight: List[float] = []):
        self.nodeId = nodeId
        self.isborder = isborder
        self.lat = lat
        self.lng = lng
        self.poiNum = poiNum
        self.poiTypeName = poiTypeName
        self.poiTypeId = poiTypeId
        self.subPoiTypeId = subPoiTypeId
        self.adjNodes = adjNodes
        self.adjWeight = adjWeight
