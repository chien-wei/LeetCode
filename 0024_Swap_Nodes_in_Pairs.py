# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        head = newHead
        
        while head.next and head.next.next:
            nex1 = head.next
            nex2 = nex1.next
            nex1.next = nex2.next
            nex2.next = nex1
            head.next = nex2
            head = nex1
        return newHead.next