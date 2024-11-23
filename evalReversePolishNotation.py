# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b - a))
            elif c == '/':
                a,b = stack.pop(), stack.pop()
                # stack.append(int( float(b) / float(a)))
                stack.append(int(b /a))
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))
        return stack[0]
