class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = defaultdict(int)
        for i, num in enumerate(nums):
            z = target - num
            if z in diff:
                return [diff[z], i]
            diff[num] = i