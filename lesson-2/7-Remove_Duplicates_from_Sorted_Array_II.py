# -*- coding: utf-8 -*-

"""
返回不包含重复元素的列表的长度
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
        count = 2
        for i in range(2, len(A)):
            if A[i] != A[count-1] or A[i] != A[count-2]:
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

A = [1, 2, 3, 4, 2, 4, 3, 4, 2, 3]
sol = Solution()
result = sol.removeDuplicates(A)
#result = sol.remove(A)
print result

