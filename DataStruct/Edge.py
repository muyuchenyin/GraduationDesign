class Edge:
    def __init__(self, eId: int, RoadName: str, spId: int, epId: int, Length: float = 0):
        self.eId = eId
        self.roadName = RoadName
        self.spId = spId
        self.epId = epId
        self.Length = Length

