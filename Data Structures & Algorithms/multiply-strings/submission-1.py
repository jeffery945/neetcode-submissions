class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        num_1, num_2 = int(num1), int(num2)
        i = 0
        if num_1 == 0 or num_2 == 0:
            return str(0)
        while num_2:
            if num_2 & 1:
                res += num_1 * (2 ** i)
            i += 1
            num_2 >>= 1
        return str(res)