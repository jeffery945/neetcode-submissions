class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestsum = nums[0]
        currSum = 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            largestsum = max(largestsum, currSum)
        return largestsum