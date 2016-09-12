# -*- coding: utf-8 -*-

"""
找出列表中出现次数大于n/2的元素
"""

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        for i in num:
            if num.count(i) > len(num)/2:
                return i
            

A = [1, 2, 4, 2, 2, 2]

sol = Solution()
print sol.majorityElement(A)
