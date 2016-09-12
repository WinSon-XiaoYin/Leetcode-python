# -*- coding: utf-8 -*-

"""
给定一个序列，这个序列中的数除了有一个数只出现过一次外，其他的数都出现两次，请找出这个只出现一次的数。

思想：两个相同的数异或为0,0和任何数异或为任何数。
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
        # 相同元素异或为0，0与任何数异或等于任何数，有a^b^a = b
        # 此外，异或还可以用于两个元素交换a = a^b^(b=a)
            result = result^i
        return result
    
    def Number(self, A):
        for i in A:
            if A.count(i) == 1:
                return i

A = [1, 2, 3, 4, 5, 1, 2, 3, 7, 4, 5]
sol = Solution()
#result = sol.singleNumber(A)
result = sol.Number(A)
print result
