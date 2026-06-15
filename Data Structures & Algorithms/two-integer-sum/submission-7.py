class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev:
                return [prev[diff], i]
            prev[nums[i]] = i
