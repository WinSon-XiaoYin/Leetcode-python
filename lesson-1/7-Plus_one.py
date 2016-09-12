# -*- coding: utf-8 -*-

"""
实现大数加1的功能

注意：满十进一的规则
"""

class Solution:
    def plusOne(self, digits):
        flag = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            if digits[i]:
                flag = 0
                break
        if flag:
            digits.insert(0, 1)
        return digits

digits = [9, 8 , 99, 199]

sol = Solution()
print sol.plusOne(digits)
