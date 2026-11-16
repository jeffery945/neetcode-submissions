class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1 # the reason why I move i is because I know that l is 1, so I can just move on
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1 # the reason why I do not move i is because I do not know what a integer I swap in
            i += 1