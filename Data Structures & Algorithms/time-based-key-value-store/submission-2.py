class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.hashmap[key]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if self.hashmap[key][mid][1] <= timestamp:
                res = self.hashmap[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
