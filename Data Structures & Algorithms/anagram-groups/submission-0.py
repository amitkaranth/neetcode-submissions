class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sublist = defaultdict(list)
        res = []
        
        for string in strs:
            char_freq = [0]*26
            for c in string:
                char_freq[ord(c)-ord("a")] += 1
            sublist[tuple(char_freq)].append(string)
        
        for lists in sublist:
            res.append(sublist.get(lists))

        return res