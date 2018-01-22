# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = slow = head
        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False
            if fast == slow:
                return True