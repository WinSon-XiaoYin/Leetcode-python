# -*- coding: utf-8 -*-

"""
组合数学题，总共有n阶台阶，每次只能走一步或者两步，总共有多少种走法。

思想：对于n+1阶台阶，有两种走法：
    一、前面n步台阶的f(n)种走法，然后一步到n+1
    二、前面n-1步台阶的f(n-1)种走法，然后两步到n+1
    因此得到的递推关系是：f(n+1) = f(n) + f(n+1)
	这是一个典型的斐波拉契数列
"""

class Solution:
    def climbStairs(self, n):
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i-2] + f[i-1])
        return f[n-1]

sol = Solution()
print sol.climbStairs(4)
