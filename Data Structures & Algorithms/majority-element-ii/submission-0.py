class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for key, val in hashmap.items():
            if val > len(nums) // 3:
                res.append(key)
        return res