# -*- coding: utf-8 -*-

"""
返回不包含重复元素的列表的长度
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A == []:
            return 0
        count = 1
        for i in range(1, len(A)):
            if A[i] != A[i-1]:
                A[count] = A[i]
                count += 1
        return count

    def remove(self, A):
        if A == []:
            return 0
        else:
            A = list(set(A))
            print A
            return len(A)

A = [1, 2, 3, 4, 2, 4]
sol = Solution()
#result = sol.removeDuplicates(A)
result = sol.remove(A)
print result

