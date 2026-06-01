class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ** correction explanation:
        # the 'else' condition handled two cases, one was
        # when char_right was false, and when char_right & char_left 
        # were false. While it passed test cases, this is a major logic flaw.

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
            elif char_right.isalnum(): # ** correction 
                l += 1
            else:
                r -= 1
                l += 1
        return True
                

