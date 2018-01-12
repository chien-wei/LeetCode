# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# time O(m*n)

# class Solution:
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         result = cur = ListNode(0)
#         count = 1
#         while count != 0:
#             minNode = math.inf
#             count = len(lists)
#             minIndex = -1
#             for i in range(len(lists)):
#                 if not lists[i]:
#                     count -= 1
#                     continue
#                 if lists[i].val < minNode:
#                     minNode = lists[i].val
#                     minIndex = i
#             if count == 0:
#                 break
#             cur.next = ListNode(minNode)
#             cur = cur.next
#             lists[minIndex] = lists[minIndex].next
#         return result.next


# time O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heapify, heappush, heappop

# We need this because python3 will compare both element in tuple
class pq_elem:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
    
    def __lt__(self, other):
        return self.priority < other.priority

class Solution:
    def mergeKLists(self, lists):
        result = cur = ListNode(0)
        h = []
        for li in lists:
            if li:
                heappush(h, pq_elem(li.val, li))
        while h:
            cur.next = heappop(h).data
            cur = cur.next
            if cur.next:
                heappush(h, pq_elem(cur.next.val, cur.next))
        return result.next