class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        cnt = 0
        i, j = 0, 0

        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                cnt += 1
                i += 1
                j += 1
            elif s[i] != t[j]:
                j += 1
        return True if cnt == len(s) else False