# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        pairs = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        stack = []
        try:
            for char in s:
                if (match := pairs.get(char)) and stack[-1] == match:
                    stack.pop()
                else:
                    stack.append(char)
        except IndexError:
            return False

        return not stack
