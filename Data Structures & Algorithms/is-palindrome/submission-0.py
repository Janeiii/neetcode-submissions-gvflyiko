class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        half = len(filtered) // 2
        for i in range(half):
            if filtered[i] != filtered[-(i + 1)]:
                return False
        return True