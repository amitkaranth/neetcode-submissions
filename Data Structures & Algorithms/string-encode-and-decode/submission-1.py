class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = []
        for s in strs:
            str_len = str(len(s))
            encode_str.append(str_len+"#"+s)
        encode_str = "".join(encode_str)
        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_str = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#" and s[j].isnumeric():
                j += 1
            str_len = int(s[i:j])
            decode_str.append(s[j+1:j+str_len+1])
            i = j+str_len+1
        return decode_str

    # time: O(n) - both work in O(n) time. even with two loops in decode
    # the inner loop only works to extract the numbers, which is almost O(1) time
    # space: O(n+k), n is the length of the string, and k is
    # is the extra pheriperals we add to decode the string (Eg:"5#")

