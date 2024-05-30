class Solution:
    def isValid(self, s:str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]: # stack needs to be empty
                return False
            stack.pop()

        return not stack # return True if not stack else False