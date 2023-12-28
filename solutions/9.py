# Palindrome Number

from math import log, floor

class Solution:
    def isPalindrome(self, x) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        digits = floor(log(x, 10)) + 1

        digitsArr = []
        temp = x
        for digitIndex in range(digits):
            digitValue = temp
            for i in range(digits - 1 - digitIndex, 0, -1):
                digitValue %= 10 ** i
            digitsArr.append(digitValue)
            temp = (temp - digitValue) // 10

        for i in range(1, len(digitsArr) // 2 + 1):
            if digitsArr[i - 1] != digitsArr[-i]:
                return False

        return True
