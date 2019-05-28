class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = [self.val]
        cur = self.next
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return str(result)
        

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def reverse(head: ListNode) -> ListNode:
            pre, cur = None, head
            
            while cur != None:
                nxt = cur.next
                cur.next = pre
                pre, cur = cur, nxt
            return pre

        
        rev = reverse(head)
        if rev.val < 9:
            rev.val += 1
            return reverse(rev)
        else:
            rev_head = rev
            while rev.val == 9:
                rev.val = 0
                if rev.next is None:
                    rev.next = ListNode(1)
                else:
                    rev = rev.next

            return reverse(rev_head)

s = Solution()
l3 = ListNode(3)
l2 = ListNode(2)
l1 = ListNode(1)
l1.next = l2
l2.next = l3
print(l1)
print(s.plusOne(l1))

l91 = ListNode(9)
l92 = ListNode(9)
l91.next = l92
print(s.plusOne(l91))

l0 = ListNode(0)
print(s.plusOne(l0))