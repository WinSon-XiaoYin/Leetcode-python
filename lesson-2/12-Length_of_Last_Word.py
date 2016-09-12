# -*- coding: utf-8 -*-

"""
求一行字符串最后一个单词的长度
"""

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == '':
            return 0
        result = s.split(' ')
        if result == []:
            return 0
        return len(result[-1])

s = "hello world!"
sol = Solution()
print sol.lengthOfLastWord(s)
