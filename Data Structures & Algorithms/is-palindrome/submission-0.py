class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        l, r = 0, n-1

        while l < r:
            char_left = s[l].lower()
            char_right = s[r].lower()

            if char_left.isalnum() and char_right.isalnum():
                if char_left == char_right:
                    r -= 1
                    l += 1
                else:
                    return False
            elif char_left.isalnum():
                r -= 1
            else:
                l += 1
        return True
                

