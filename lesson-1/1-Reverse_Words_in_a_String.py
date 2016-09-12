# -*- coding: utf-8 -*-

"""
给定一个字符串，字符串是以单词的形式拼接起来的，需要做的是把字符串里面的单词逆序输出，但单词内的顺序不变。

陷阱：两个单词间可能有多个空格，这是题目的陷阱
"""

class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		tmp = s.split(' ') # 将字符串分割成列表
		while '' in tmp:   # 清除空元素 
			tmp.remove('')
		tmp.reverse()      # 列表倒序
		tmp = ' '.join(tmp) # 列表转化为字符串，并以空格连接
		return tmp

s = "Hello  World"
sol = Solution()
string = sol.reverseWords(s)
print string
