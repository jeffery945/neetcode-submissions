class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        currSize = 0
        end = 0
        for i, c in enumerate(s):
            currSize += 1
            end = max(end, last[c])
            if i == end:
                res.append(currSize)
                currSize = 0

        return res

        
