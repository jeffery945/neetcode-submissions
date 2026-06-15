class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        step = [0] * (n + 1)
        step[1], step[2] = 1, 2 #step[1] means the number of way to reach step1
        for i in range(3, n + 1):
            step[i] = step[i - 1] + step[i - 2]

        return step[n]