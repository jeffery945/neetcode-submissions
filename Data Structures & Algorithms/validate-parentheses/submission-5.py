class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in dic:
                if stack and stack[-1] == dic[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False