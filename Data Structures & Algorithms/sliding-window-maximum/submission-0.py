class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque() # queue stores the biggest index on the left
        i, j = 0, 0
        res = []

        while j < len(nums):
            while queue and nums[queue[-1]] < nums[j]:
                queue.pop()
            queue.append(j)

            if i > queue[0]:
                queue.popleft()
            if j - i + 1 >= k:
                res.append(nums[queue[0]])
                i += 1
            j += 1

        return res
