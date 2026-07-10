class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {"(":")", "[":"]", "{":"}"}
        if len(s)%2 != 0:
            return False

        for ch in s:
            if ch in bracket_dict:
                stack.append(ch)
            elif stack and bracket_dict.get(stack[-1]) == ch:
                q = stack.pop()
                print("q:",q)
            else:
                return False
        return True if not stack else False
