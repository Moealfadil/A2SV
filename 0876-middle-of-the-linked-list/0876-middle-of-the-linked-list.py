# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)
        slow=dummy
        fast=dummy
        counter=1
        while fast.next:
            fast=fast.next
            if counter%2==0:
                slow=slow.next
            counter+=1
        return slow.next