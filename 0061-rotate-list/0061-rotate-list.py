# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        current=ListNode(0,head)
        while current.next:
            current=current.next
            count+=1
        current.next=head
        current=head
        if count==0:
            return head
        for i in range(count-k%count-1):
            current=current.next
        result=current.next
        current.next=None
        return result
        