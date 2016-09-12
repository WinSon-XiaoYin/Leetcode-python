# -*- coding: utf-8 -*-

"""
判断一棵树是不是对称树

思想：将这棵树分成左右两棵子树，然后遍历这两棵子树，比较时不再是左边和左边比，而是左子树的左节点和右子树的右节点以及左子树的右节点和右子树的左节点是否相等。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        else:
            return self.isSameTree(root.left, root.right)

    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                if self.isSameTree(p.left, q.right): # 递归调用，当两棵树的左节点同时为空返回True
                    return self.isSameTree(p.right, q.left) # 递归调用，当两棵树的右节点同时为空时返回True
                else:
                    return False
