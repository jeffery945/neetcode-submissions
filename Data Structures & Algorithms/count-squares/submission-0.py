class CountSquares:

    def __init__(self):
        self.pt = []
        self.ptCount = defaultdict(int)
    def add(self, point: List[int]) -> None:
        self.ptCount[tuple(point)] += 1
        self.pt.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point[0], point[1]

        for x, y in self.pt:
            if abs(px - x) != abs(py - y) or (px == x) or (py == y):
                continue
            
            res += self.ptCount.get((px, y), 0) * self.ptCount.get((x, py), 0)
        return res


