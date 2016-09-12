# -*- coding: utf-8 -*-

"""
给定一个已经排好序的数组和一个数，如果这个数在这个数组里面，则返回这个数的下标，否则将这个输插入到数组中，并返回它的下标。
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for i in range(len(A)):
            if A[i] >= target:
                return i
            if A[len(A) - 1] < target:
                return len(A)
    
    def search(self, A, target):
        if target in A:
            return A.index(target)
        else:
            A.append(target)
            A.sort()
            return A.index(target)

A = [1, 2, 4, 5, 6, 8]
sol = Solution()
print sol.searchInsert(A, 1)
print sol.search(A, 1)
