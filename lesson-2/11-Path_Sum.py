# -*- coding: utf-8 -*-

"""
一棵二叉树是否存在一条从根节点到叶子节点的路径，其上所有节点之和等于一个指定的数。
"""

class TRee():
    def __init__(self, leftjd=0, rightjd=0, data=0):
        self.left = leftjd
        self.right = rightjd
        self.val = data

class Solution:
    def __init__(self, base=0):
        self.base = base

    # @param root, a tree node
    # @param target, an integer
    # @return a boolean
    def hasPathSum(self, root, target):
        if root == None:
            return False
        if root.val == target:
            print target
            return True
	
        if root.left != None:
            self.hasPathSum(root.left, target)
        if root.right != None:
            self.hasPathSum(root.right, target)

jd6 = TRee(None, None, data=7)
jd5 = TRee(jd6, None,data=6)
jd4 = TRee(None, None, data=5)
jd3 = TRee(None, None, data=4)
jd2 = TRee(None, jd5, data=3)
jd1 = TRee(jd3, jd4, data=2)
base = TRee(jd1, jd2, data=1)

x = Solution(base)

x.hasPathSum(x.base, 5)

