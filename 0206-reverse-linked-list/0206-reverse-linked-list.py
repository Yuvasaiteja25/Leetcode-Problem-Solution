# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l=[]
        while(head):
            l.append(head.val)
            head=head.next
        print(l)
        dummy=ListNode(0)
        curr=dummy
        l=l[::-1]
        for i in l:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
        