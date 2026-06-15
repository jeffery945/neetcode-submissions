class Solution:
    def isPalindrome(self, s: str) -> bool:
        return [c.lower() for c in s if c.isalnum()] == [c.lower() for c in reversed(s) if c.isalnum()]