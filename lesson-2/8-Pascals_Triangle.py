# -*- coding: utf-8 -*- 

"""
题目的意思是生成n行的Pascal's三角并存入到列表中。思路是第i(i>=3)的第j个元素等于第i-1行的第j-1个元素和第j个元素之和，初识化第一二行之后for一下就可以了，另外由于Pascal's三角是对称的，所以我们每次只需算前一半即可。
"""

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 1:
            return([[1]])
        elif numRows == 2:
            return([[1],[1,1]])
        elif numRows == 0:
            return([])
        else:
            result = [[1],[1,1]]
            for i in range(3, numRows+1):
                tmp = [1]*i
                last = result[i-2]
                for j in range(1,(i-1)//2 + 1):
                    tmp[j] = tmp[i-1-j] = last[j-1] +last[j]
                result.append(tmp)
            return(result)
