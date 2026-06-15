class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        mid = 0
        while low < high:
            mid = (low + high) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours <= h:
                high = mid
            else:
                low = mid + 1
        return low
        
