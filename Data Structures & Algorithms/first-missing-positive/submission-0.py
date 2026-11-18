class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # using val - 1 to check if val appears or not
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums): # we do not care the value that out of this range, because result not over this range
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1) # change it to -(len(nums) + 1), so it won't be taken into consideration anymore
        
        # pick the first positive number, because it means that it doesn't appear
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1