# -*- coding: utf-8 -*-

"""
这个题是上一个题目的升级版，只要出现重复的数字，这些数字都要从链表中删掉，方法是在链表前先加一个节点以及一个删除标识，然后遍历这个链表，比较后两个节点是否相同，如果相同，先删掉第一个节点，并让删除标识变为真，表明下一次操作需要把第二个节点删掉（即使下一次比较的时候两个节点值不同，但是上次只删掉了一个重复节点，所以还是要把它删掉），如果下两个节点不同且删除标识不为真则跳过。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return(head)
        cur = ListNode(head.val)
        cur.next, head = head, cur
        flag = False
        while cur:
            if cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                cur.next = cur.next.next
                flag = True
            elif flag and cur.next:
                cur.next = cur.next.next
                flag = False
            else:
                cur = cur.next
        return(head.next)
