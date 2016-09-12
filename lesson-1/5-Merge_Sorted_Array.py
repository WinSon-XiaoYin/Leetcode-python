# -*- coding: utf-8 -*-

"""
将两个排好序的序列合并为一个排好序的序列。

注意：当某一个序列为空是可能出现问题。

个人觉得我写的这个更简单好用
"""

class Solution:
    def merge(self, A, m, B, n):
        for i in range(m+n-1, -1, -1):
            if m == 0 or (n > 0 and B[n-1] > A[m-1]):
                A[i] = B[n-1]
                n -= 1
            else:
                A[i] = A[m-1]
                m -= 1
        return A

    def me(self, A, B):
        A.extend(B)
        A.sort()
        return A


A = [1, 3, 5]
#B = [2, 4, 6]
B = []
sol = Solution()
#result = sol.merge(A, len(A), B, len(B))
result = sol.me(A, B)
print len(result)
print result
