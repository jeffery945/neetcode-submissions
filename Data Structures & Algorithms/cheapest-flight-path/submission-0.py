class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1): # iterate k + 1 times, each iteration updates the maximum i stop between src and dst
            tmpprices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                
                if prices[s] + p < tmpprices[d]: # if prices to s last round + p is less than last round p, we should update the price
                    tmpprices[d] = prices[s] + p
            prices = tmpprices
        return prices[dst] if prices[dst] != float("inf") else -1