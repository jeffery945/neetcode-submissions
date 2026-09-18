class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        subset = []
        def dfs(pick):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if not pick[i]:
                    subset.append(nums[i])
                    pick[i] = True
                    dfs(pick)
                    subset.pop()
                    pick[i] = False

        dfs(pick)
        return res

        