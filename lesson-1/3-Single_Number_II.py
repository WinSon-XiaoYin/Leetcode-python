# -*- coding: utf-8 -*- 

"""
与上一题类似，只不过这个序列中的数字除了某一个数字外都出现了3次，需要找出这个数字。
"""

class Solution:
    def singleNumber(self, A):
        ones, twos = 0, 0
        for ele in A:
            ones = ones^ele & ~twos
            twos = twos^ele & ~ones
        return ones

    def Number(self, A):
        for i in A:
            if A.count(i) == 1:
                return i

A = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 4]
sol = Solution()
#result = sol.singleNumber(A)
result = sol.Number(A)
print result

"""
def singleNumber(A, m, n):
    tmp = [0]*(m-1)
    for ele in A:
        for i in range(m-1):
            tmp[i] = tmp[i]^ele
            for j in range(m-1):
                if i != j:
                    tmp[i] = tmp[i] & ~tmp[j]
    return tmp[n-1]
"""

