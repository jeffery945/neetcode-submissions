class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        stars = []

        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                stars.append(i)
            else: # ")"
                if not left and not stars:
                    return False
                if left:
                    left.pop()
                else:
                    stars.pop()
        while left and stars:
            if left.pop() > stars.pop(): # if a ( is on the stars right, which means stars cannot eliminate it, return false
                return False

        return not left