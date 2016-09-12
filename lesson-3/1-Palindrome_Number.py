# -*- coding: utf-8 -*-

"""
判断一个整数是不是回文
"""

class Solution:
    # @param x, integer
    # @return a boolean
    def isPalindrome(self, x):
        x = str(x) 
	print type(x)
        print x[::-1]
        if x == x[::-1]:
            return True
        else:
            return False


sol = Solution()
result = sol.isPalindrome(21)
print "回文" if result else "不是回文"
