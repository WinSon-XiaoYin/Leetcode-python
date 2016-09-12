# -*- coding: utf-8 -*-

"""
判断一个字符串是否是回文，回文的意思是正序和逆序都一样，这个题不区分大小写
"""

import re

class Solution:
    def isPalindrome(self, s):
        s = s.lower() # 将字符串转为小写
        s = re.sub('[^A-Za-z0-9]', '', s) # 正则表达式去除非字母和数字的符号
        if s == s[::-1]: # 如果是回文，即正序和逆序一样
            return True
        else:
            return False

s = "asdf*f*dsa"
sol = Solution()
result = sol.isPalindrome(s)
print result
