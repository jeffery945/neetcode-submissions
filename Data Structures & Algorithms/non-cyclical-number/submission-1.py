class Solution:
    def isHappy(self, n: int) -> bool:
        memo = defaultdict(bool)
        def countingcyclical(i):
            digits_i = [int(digit) for digit in str(i)]
            return sum(i**2 for i in digits_i)
        res = countingcyclical(n)
        while(res != 1 and res not in memo):
            memo[res] = True
            res = countingcyclical(res)
        if res in memo:
            return False
        if res == 1:
            return True
