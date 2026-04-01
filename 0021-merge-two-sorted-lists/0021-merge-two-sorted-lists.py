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
        temp1=list1
        temp2=list2  
        result=ListNode(0)
        head=result
        while temp1 or temp2:
            if temp1 is not None:
                if temp2 is None or temp1.val<= temp2.val:
                    result.next=temp1
                    temp1=temp1.next
                else:
                    result.next=temp2
                    temp2=temp2.next
            else:
                result.next=temp2
                temp2=temp2.next
            result = result.next
        return head.next