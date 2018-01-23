# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sliceListNode(listN):
            fast = slow = listN
            while fast and fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            tmp = slow.next
            slow.next = None
            slow = tmp
            return (listN, slow)
        
        def merge(listA, listB):
            head = None
            if listA.val <= listB.val:
                head = listA
                listA = listA.next
            else:
                head = listB
                listB = listB.next
            
            cur = head
            while listA or listB:
                if (listA and listB) and listA.val <= listB.val:
                    cur.next = listA
                    listA = listA.next
                elif listA and listB:
                    cur.next = listB
                    listB = listB.next
                elif listA:
                    cur.next = listA
                    listA = listA.next
                else:
                    cur.next = listB
                    listB = listB.next
                cur = cur.next
            return head
            
        def mergeSort(listN):
            if not listN:
                return None
            elif not listN.next:
                return listN
            
            a, b = sliceListNode(listN)
            a = mergeSort(a)
            b = mergeSort(b)
            return merge(a, b)
            
                
        if not head:
            return head
        return mergeSort(head)