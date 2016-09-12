# -*- coding: utf-8 -*-

"""
给定两棵二叉树，判断是否相同

一是结构相同，二是值相同

思想：需要对两棵树同时遍历(简单的递归)，遇到不同的则返回False，遍历一遍之后没有发现不同则说明这两棵树相同。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                if self.isSameTree(p.left, q.left): # 递归调用，当两棵树的左节点同时为空返回True
                    return self.isSameTree(p.right, q.right) # 递归调用，当两棵树的右节点同时为空时返回True
                else:
                    return False
