# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        for i in range(n):
            first = first.next
        
        second = dummy

        while first.next:
            first = first.next
            second = second.next

        second.next= second.next.next
        return dummy.next
