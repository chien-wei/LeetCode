# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        def list2tree(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)
            
            fast = slow = pre = head
            while fast and fast.next:
                fast = fast.next.next
                pre = slow
                slow = slow.next
                
            pre.next = None
            
            result = TreeNode(slow.val)
            result.left = list2tree(head)
            result.right = list2tree(slow.next)
            
            return result
        
        return list2tree(head)