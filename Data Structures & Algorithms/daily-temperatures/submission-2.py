class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        resInd = 0
        resTemp = 0
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                resInd, resTemp = stack.pop()
                res[resInd] = i - resInd

            stack.append([i, t])
        return res