class Solution:
    def isValid(self, s: str) -> bool:
        stck  = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stck.append(ch)
            if not stck:
                return False
            elif ch == ')':
                    if stck.pop() != '(':
                        return False
            elif ch == ']':
                    if stck.pop() != '[':
                        return False
            elif ch == '}':
                    if stck.pop() != '{':
                        return False
        if stck:
            return False
        return True