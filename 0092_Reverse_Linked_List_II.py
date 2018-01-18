class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        newHead = ListNode(0)
        newHead.next = head
        head = newHead
        for _ in range(m-1):
            head = head.next
        
        cur = head.next
        tmp = cur.next
        for _ in range(n-m):
            cur.next = tmp.next
            tmp.next = head.next
            head.next = tmp
            tmp = cur.next
        return newHead.next