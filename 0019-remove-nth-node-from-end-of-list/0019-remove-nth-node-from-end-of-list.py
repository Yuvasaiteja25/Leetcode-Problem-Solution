# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both fast and slow until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Skip the nth node from the end
        slow.next = slow.next.next
        
        # Return the head of the modified list
        return dummy.next
