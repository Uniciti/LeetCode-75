class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        n = len(s)
        for v in t:
            if j < n and v == s[j]:
                j += 1
            
        if j == n:
            return True
        return False