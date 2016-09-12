# -*- coding: utf-8 -*-

"""
找出在列表中是否有两个数的和为一个给定数，并返回两个数的下标。
"""

class Solution:
    def twoSum(self, A, target):
        for i in A:
            for j in A[A.index(i)+1:]:
                if target == i+j:
                    print A.index(i), A.index(j)

    def Sum(self, A, target):
        tmp = {}
        for i in range(len(A)):
            if target - A[i] in tmp:
                print tmp[target-A[i]], i 
            else:
                tmp[A[i]] = i

A = [1, 2, 3, 4, 5, 6, 7]
sol = Solution()
sol.twoSum(A, 13)
#sol.Sum(A, 13)


