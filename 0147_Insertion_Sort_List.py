# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This answer is the insertion sort solution
# But the judger can not pass this solution
import math

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(-math.inf)
        newHead.next = head
        head = newHead
        
        n = head.next
        head.next = None
        
        while n:
            cur = head
            while cur:
                if (cur.val <= n.val and ((not cur.next) or cur.next.val > n.val)):
                    tmp = cur.next
                    cur.next = n
                    n = n.next
                    cur.next.next = tmp
                    break
                else:
                    cur = cur.next
        return head.next
        
# This solution can pass though
# class Solution(object):
#     def insertionSortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         list = []
#         cur = head
#         while cur:
#             list.append(cur.val)
#             cur = cur.next
#         result = ListNode(0)
#         cur = result
#         list = sorted(list)
#         for i in list:
#             cur.next = ListNode(i)
#             cur = cur.next
#         return result.next