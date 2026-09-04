class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        a, b = 0, 0
        for c in tokens:
            if c == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif c == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif c == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif c == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a / b)
            else:
                stack.append(c)
        return int(stack[0])
