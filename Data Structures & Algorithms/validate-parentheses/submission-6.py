class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {"(":")", "[":"]", "{":"}"}
    
        for ch in s:
            if ch in open_to_close:
                stack.append(ch)
            elif stack and open_to_close.get(stack[-1]) == ch:
                stack.pop()
            else:
                return False
        return not stack
