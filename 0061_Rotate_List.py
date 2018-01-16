# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        if not cur or k == 0:
            return head

        len = 1
        while cur.next:
            cur = cur.next
            len += 1
        
        times = k%len
        if times == 0:
            return head

        fast = slow = head

        for i in range(times):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        tmp = slow.next
        slow.next = None
        fast.next = head
        head = tmp
        return head

            
            
