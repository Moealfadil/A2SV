# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique=set()
        current=ListNode(0,head)
        while current and current.next:
            if current.next.val in unique:
                current.next=current.next.next
            else:
                unique.add(current.next.val)
                current=current.next
        return head
