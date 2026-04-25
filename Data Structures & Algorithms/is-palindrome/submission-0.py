class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        middle = len(s) // 2
        left = s[:middle]
        right = s[middle + (1 if len(s) % 2 != 0 else 0):][::-1]
        if left == right:
                return True
        else: 
                return False