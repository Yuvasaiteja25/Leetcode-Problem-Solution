# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        """
        dummy=ListNode(0)
        curr=dummy

        carry=0
        while(l1 or l2 or carry):
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            val=a+b+carry
            carry=val//10
            val=val%10
            print(val)
            curr.next=ListNode(val)
            curr=curr.next
            
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
        
        
        