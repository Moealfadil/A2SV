# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count=0
        dummy=ListNode(0,head)
        current=dummy
        prev=None
        while current:
            if count==left-1:
                first_idx=current
                last=current.next
            if count==right:
                second_idx=current.next
                first=current
            if left<=count<=right:
                nxt=current.next
                current.next=prev
                prev=current
                current=nxt
            else:
                current=current.next
            count+=1
        first_idx.next=first
        last.next=second_idx
        return dummy.next