# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        head = newHead
        
        part = cur = head
        while cur.next:
            if cur.next.val >= x:
                cur = cur.next
            elif cur.next.val < x:
                if part == cur:
                    part = part.next
                    cur = cur.next
                else :
                    tmp = cur.next.next
                    cur.next.next = part.next
                    part.next = cur.next
                    cur.next = tmp
                    part = part.next
            
        return newHead.next