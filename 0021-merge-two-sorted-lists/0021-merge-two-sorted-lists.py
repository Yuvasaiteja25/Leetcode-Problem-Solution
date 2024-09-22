# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l=[]
        while(list1):
            l.append(list1.val)
            list1=list1.next
        while(list2):
            l.append(list2.val)
            list2=list2.next
        l.sort()
        dummy=ListNode(0)
        curr=dummy
        for i in l:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next