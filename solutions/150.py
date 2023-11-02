# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from operator import add, mul

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        functions = {
            "+": add,
            "-": lambda x, y: x-y,
            "*": mul,
            "/": lambda x, y: int(x / y)
        }
        
        stack = []
        for token in tokens:
            if func := functions.get(token):
                b, a = stack.pop(), stack.pop()
                stack.append(func(a, b))
            else:
                stack.append(int(token))

        return stack[-1]
