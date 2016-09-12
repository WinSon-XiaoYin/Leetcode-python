# -*- coding: utf-8 -*-

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        add = 0
        l3 = ListNode(0)
        cur = l3
        while l1 or l2:
            node = ListNode(add)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            if node.val >= 10:
                add = 1
            else:
                add = 0
            node.val %= 10
            cur.next, cur = node, node
        if add:
            cur.next = ListNode(1)
        return l3.next
