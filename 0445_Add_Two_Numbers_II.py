# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = b = 0
        while l1:
            a *= 10
            a += l1.val
            l1 = l1.next
        while l2:
            b *= 10
            b += l2.val
            l2 = l2.next
        a += b
        newHead = ListNode(0)
        cur = newHead
        for c in str(a):
            cur.next = ListNode(int(c))
            cur = cur.next
        return newHead.next