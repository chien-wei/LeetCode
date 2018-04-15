# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        cur = head
        ans = 1
        while cur.val not in G:
            cur = cur.next
        while cur:
            if cur.val not in G and cur.next and cur.next.val in G:
                ans += 1
            elif cur.val in G:
                G.remove(cur.val)
            cur = cur.next
        return ans

# use hash
class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        cur = head
        ans = 1
        h = {}
        for el in G:
            h[el] = 1
        while cur.val not in h:
            cur = cur.next
        while cur:
            if cur.val not in h and cur.next and cur.next.val in h:
                ans += 1
            cur = cur.next
        return ans