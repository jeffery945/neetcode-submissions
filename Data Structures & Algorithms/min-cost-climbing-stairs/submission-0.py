class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1): #從倒數第三個算回來，因為最後兩個是一定要跳到的
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])