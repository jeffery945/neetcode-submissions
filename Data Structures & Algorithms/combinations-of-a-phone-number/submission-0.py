class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        subset = []
        hashmap = {"2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",}

        def dfs(i):
            if i == len(digits):
                res.append("".join(subset.copy()))
                return

            for c in hashmap[digits[i]]:
                subset.append(c)
                dfs(i + 1)
                subset.pop()
        if not digits:
            return res
        dfs(0)
        return res
            