class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(heights) + 1): 
            # because you have to calculate all the pillar in the stack, so + 1
            while stack and (i == len(heights) or heights[i] <= heights[stack[-1]]):
                # WHenever iterating to a pillar that is lower than the stack[-1] pillar, we calaulate
                # the rectangle for stack[-1] pillar 
                # calculate the area of rectangle that expanding by stack[-1] heights
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1 # width is the number of pillar from left
                                                            # boarder to i minus left and right pillar
                res = max(res, height * width)

            stack.append(i)
        return res
