class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if target == nums[i] + nums[j]  and i != j:
                    return [i, j]
