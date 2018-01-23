# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA = headA
        curB = headB
        flagA = True
        flagB = True
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
            
            if not curA and flagA:
                curA = headB
                flagA = False
            if not curB and flagB:
                curB = headA
                flagB = False
        return None