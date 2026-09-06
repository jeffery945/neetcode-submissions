class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        mid = 0
        while low < high:
            mid = (low + high) // 2
            time = sum((pile + mid - 1) // mid for pile in piles)

            if time > h:
                low = mid + 1
            else:
                high = mid
        return low
        
