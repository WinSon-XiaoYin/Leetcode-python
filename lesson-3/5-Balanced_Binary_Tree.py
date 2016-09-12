# -*- coding: utf-8 -*-

"""
判断一棵树是否为平衡树

平衡树：任意两棵左右子树的深度之差不超过1
"""

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
        return self.getDepth(root) != -100

    def getDepth(self, root):
        if root == None:
            return 0
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)
        if l == -100 or r == -100 or abs(l-r) > 1:
            return -100
        return 1 + max(l, r)
