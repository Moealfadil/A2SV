# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first=l1
        second=l2
        result=ListNode(0)
        head=result
        carry=0
        while first and second:
            nxt=ListNode()
            c=first.val+second.val+carry
            print(c)
            nxt.val= c%10
            carry=c//10
            result.next=nxt
            result=result.next
            first=first.next
            second=second.next
            

        while first:
            
            nxt=ListNode()
            c=first.val+carry
            nxt.val= c%10
            carry=c//10
            result.next=nxt
            result=result.next
            first=first.next
        
        while second:
            nxt=ListNode()
            c=second.val+carry
            nxt.val= c%10
            carry=c//10
            result.next=nxt
            result=result.next
            second=second.next

        if carry:
            nxt=ListNode()
            nxt.val=carry
            result.next=nxt
            result=nxt

        return head.next