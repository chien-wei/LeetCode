# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = cur = ListNode(0)
        while l1 or l2:
            if l1 and l2 and l1.val <= l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l1 and l2 and l1.val > l2.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            elif l1: 
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        return head.next