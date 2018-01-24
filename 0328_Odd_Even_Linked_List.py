# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        cur = head.next.next
        shift = True
        
        while cur:
            # odd
            if shift:
                even.next = cur.next
                cur.next = odd.next
                odd.next = cur
                odd = odd.next
            else:
                even = even.next
            cur = even.next
            shift = not shift
            
        return head