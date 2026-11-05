class Solution:
    def isHappy(self, n: int) -> bool:
        history = defaultdict(bool)
        def cyclical(n):
            cyclical_num = [int(i) for i in str(n)]
            return sum([i**2 for i in cyclical_num])

        curr = cyclical(n)
        while curr != 1 and curr not in history:
            history[curr] = True
            curr = cyclical(curr)
        if curr in history:
            return False
        if curr == 1:
            return True
