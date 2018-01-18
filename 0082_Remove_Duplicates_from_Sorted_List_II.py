# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        head = newHead
        
        cur = head
        while cur.next:
            if cur.next.next and cur.next.val == cur.next.next.val and cur.next.next.next and cur.next.next.val == cur.next.next.next.val:
                cur.next.next = cur.next.next.next
            elif cur.next.next and cur.next.val == cur.next.next.val:
                cur.next = cur.next.next.next
            else:
                cur = cur.next
        return newHead.next