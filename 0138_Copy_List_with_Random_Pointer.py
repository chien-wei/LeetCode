# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = tmp
            cur = tmp
        cur = head
        
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        cur = head
        result = head.next
        while cur:
            tmp = cur.next.next
            if tmp:
                cur.next.next = tmp.next
            else:
                cur.next.next = None
            cur.next = tmp
            cur = tmp
            
        return result