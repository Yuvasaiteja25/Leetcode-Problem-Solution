# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy=ListNode(0)
        l=[]
        for i in lists:
            while(i):
                l.append(i.val)
                i=i.next
        l.sort()
        curr=dummy
        for i in l:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
            

        