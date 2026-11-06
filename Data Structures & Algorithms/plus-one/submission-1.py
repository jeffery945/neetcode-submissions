class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr = 0
        for i in range(len(digits) - 1, -1, -1):
            curr += digits[len(digits) - 1 -i] * (10 ** i)
        curr += 1
        return [i for i in str(curr)]