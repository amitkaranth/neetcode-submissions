class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        string1 = {}
        string2 = {}

        for c in s:
            string1[c] = 1+string1.get(c, 0)
        for c in t:
            string2[c] = 1+string2.get(c, 0)
        return string1==string2
