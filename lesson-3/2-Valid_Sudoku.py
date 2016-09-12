# -*- coding: utf-8 -*-

"""
判断给定的数独二维数组是否合法，即
1、每一行只包含1-9，既每一行没有重复的数字
2、每一列只包含1-9，即每一列没有重复的数字
"""

class Solution:
    # @paran board, a 9x9 2D array
    # @return a boolean
    def isValidSuduku(self, board):
        for i in range(9):
            tmp = board[i] 
            for j in tmp:
                if j in tmp[tmp.index(j)+1:]:
                    return False
            l = [x[i] for x in board]
            for j in l:
                if j in l[l.index(j)+1:]:
                    return False
        return True

board = [
        [2, 4, 3, 8, 5, 9, 7, 6, 1],
        [8, 7, 6, 1, 4, 2, 5, 3, 9],
        [5, 9, 1, 3, 6, 7, 4, 2, 8],
        [3, 8, 7, 5, 2, 6, 9, 1, 4],
        [6, 5, 9, 4, 8, 1, 3, 7, 2],
        [1, 2, 4, 7, 9, 3, 8, 5, 6],
        [7, 3, 8, 6, 1, 4, 2, 9, 5],
        [9, 1, 5, 2, 3, 8, 6, 4, 7],
        [1, 6, 2, 9, 7, 5, 1, 8, 3]
        ]


sol = Solution()
result = sol.isValidSuduku(board)
print "合法" if result else "不合法"
