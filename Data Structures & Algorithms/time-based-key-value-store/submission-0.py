class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        low = 0
        res = ""
        high = len(self.hash_map[key]) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.hash_map[key][mid][1] <= timestamp:
                res = self.hash_map[key][mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return res

