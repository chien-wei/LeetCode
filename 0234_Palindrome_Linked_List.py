# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        fast = head
        pre = ListNode(0)
        pre.next = head
        cur = head
        
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            # use cur as a slow pointer
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
            
        if fast.next:
            # even number of Listnode
            cur, head = cur.next, pre.next
        else:
            # odd number of Listnode
            cur, head = cur.next, pre.next.next
        
        while cur:
            if cur.val != head.val:
                return False
            cur, head = cur.next, head.next
        return True