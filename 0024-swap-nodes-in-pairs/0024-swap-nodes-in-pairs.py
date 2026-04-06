# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        prev=None
        prev2=None
        result=None
        if current and current.next:
                nxt=current.next #nxt=2
                nxt_nxt=current.next.next
                current.next=prev #current.next=None
                prev=current #prev=1
                current=nxt #current=2
                result=nxt
                current.next=prev
                prev2=prev
                prev=None
                current=nxt_nxt
        while current and current.next:#current=3
                nxt=current.next #nxt=4
                nxt_nxt=current.next.next
                current.next=prev #current.next=None
                prev=current #prev=3
                current=nxt #current=4
                current.next=prev
                prev2.next=current
                prev2=prev
                prev=None
                current=nxt_nxt
        if current and prev2:
            prev2.next=current
        if result:
            return result
        else:
            return head
        