class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token == "+":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l) + int(r))
            elif token == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l) - int(r))
            elif token == "*":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l) * int(r))
            elif token == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l) / int(r))
            else:
                stack.append(token)

        return int(stack.pop())