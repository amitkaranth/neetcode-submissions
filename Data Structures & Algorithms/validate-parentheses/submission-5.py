class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {"(":")", "[":"]", "{":"}"}
    
        for ch in s:
            if ch in bracket_dict:
                stack.append(ch)
            elif stack and bracket_dict.get(stack[-1]) == ch:
                stack.pop()
            else:
                return False
        return not stack
