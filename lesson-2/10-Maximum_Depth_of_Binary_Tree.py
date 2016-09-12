# -*- coding: utf-8 -*-

"""
计算一棵二叉树的最小深度，分别计算左右子树的深度，然后取较小。

方法：深度的计算方法是如果节点是叶子节点深度加1，如果节点有子节点深度加1。
"""

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        left = right = -1
        if root.left != None:
            left = 1 + self.minDepth(root.left)
        if root.right != None:
            right = 1+ self.minDepth(root.right)
        return max(left, right)
