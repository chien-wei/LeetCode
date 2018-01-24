# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        result = []
        length = 0
        cur = root
        while cur:
            length += 1
            cur = cur.next
        
        subHead = ListNode(0)
        subHead.next = root
        number = int(length / k)
        remains = length % k
        for i in range(k):
            result.append(subHead.next)
            cur = subHead
            for j in range(number):
                cur = cur.next
            if i < remains:
                cur = cur.next
            subHead = ListNode(0)
            subHead.next = cur.next
            cur.next = None
            
        return result