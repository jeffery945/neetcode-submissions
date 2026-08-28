class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r= 0, len(heights) - 1
        while l < r:
            res = max(res, (r - l) * min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return res