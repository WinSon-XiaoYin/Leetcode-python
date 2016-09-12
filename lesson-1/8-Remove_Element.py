# -*- coding: utf-8 -*-

"""
去掉序列中规定的元素之后求剩下的序列的长度。
"""

class Solution:
    def removeElement(self, A, elem):
        while elem in A:
            A.remove(elem)
        return len(A)


A = [1, 2, 3, 4]
sol = Solution()
result = sol.removeElement(A, 3)
print result

