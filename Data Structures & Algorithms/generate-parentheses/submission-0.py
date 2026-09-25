class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(openp, closep):
            if openp == closep == n:
                res.append("".join(stack))
                return
            
            if openp < n:
                stack.append("(")
                dfs(openp + 1, closep)
                stack.pop()

            if closep < openp:
                stack.append(")")
                dfs(openp, closep + 1)
                stack.pop()

        dfs(0, 0)
        return res
