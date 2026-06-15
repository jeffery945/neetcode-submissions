class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.checkTheOrder(s[i]):
                i += 1
            while i < j and not self.checkTheOrder(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True



    def checkTheOrder(self, s: str) -> bool:
        return  (ord("a") <= ord(s) <= ord("z") or
                ord("A") <= ord(s) <= ord("Z") or
                ord("0") <= ord(s) <= ord("9"))

