class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        prefixSum = {0: 1}
        for num in nums:
            currsum += num
            diff = currsum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currsum] = 1 + prefixSum.get(currsum, 0)

        return res