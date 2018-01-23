# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        fast = slow = pre = head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
            
        half = pre
        cur = half.next
        while cur.next:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = half.next
            half.next = tmp
        
        cur = head
        tmp = half.next
        half.next = None
        half = tmp
        while half:
            tmp = cur.next
            cur.next = half
            print(cur.val, half.val)
            half = half.next
            if tmp:
                cur.next.next = tmp
                cur = tmp
            else:
                while cur:
                    cur = cur.next
                break