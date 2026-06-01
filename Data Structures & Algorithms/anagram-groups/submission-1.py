class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sublist = defaultdict(list)

        for string in strs:
            char_freq = [0]*26
            for c in string:
                char_freq[ord(c)-ord("a")] += 1
            sublist[tuple(char_freq)].append(string)
        
        return list(sublist.values())