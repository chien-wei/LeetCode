# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        head = newHead
        
        def checkNextK(h):
            for _ in range(k):
                if not h.next:
                    return False
                h = h.next
            return True
        
        
        while True:
            if not checkNextK(head): return newHead.next
            cur = head.next
            tmp = cur.next
            for _ in range(k-1):
                cur.next = tmp.next
                tmp.next = head.next
                head.next = tmp
                tmp = cur.next
            head = cur