# -*- coding: utf-8 -*-

"""
将整数逆序输出，如果是负数，符号不需要逆序。

思想：将其转化成字符串，然后逆序

注意：逆序之后，该数可能超出最大值2^31 - 1，需要做判断
"""

class Solution:
    def reverse(self, x):
        if x >= 0:
            x = str(x)
            if int(x[::-1]) > (2 ** 31 - 1):
                return 0
            else:
                return int(x[::-1])
        else:
            x = abs(x)
            x = str(x)
            if int("-" + x[::-1]) < - 2 ** 31:
                return 0
            else:
                return int("-" + x[::-1])

sol = Solution()
result = sol.reverse(-723423)
print result
