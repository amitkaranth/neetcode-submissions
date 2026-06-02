class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        seen = set()
        l, r = 0, 0

        resLen = 1
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            resLen = max(resLen, r-l+1)
            r += 1
        return resLen