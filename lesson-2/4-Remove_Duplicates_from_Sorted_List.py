# -*- coding: utf-8 -*-

"""
去除链表中所有重复的元素

思想：遍历整个链表，每次将当前节点的值跟下一个节点的值相比，如果相同则将当前节点指向下下个节点。

注意：如果没有下下个节点，则当前节点指向Node。
"""

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        else:
            cur = ListNode(head.val)
            cur.next, head = head, cur
            while cur:
                if cur.next and cur.val == cur.next.val:
                    if cur.next.next:
                        cur.next = cur.next.next
                    else:
                        cur.next = None

                else:
                    cur = cur.next

            return head

