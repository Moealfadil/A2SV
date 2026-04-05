# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = ListNode(0, head)   
        last = ListNode(0)         
        last_head = last

        curr = first

        while curr and curr.next:
            if curr.next.val >= x:
                move = curr.next
                curr.next = curr.next.next  
                last.next = move            
                last = last.next
                last.next=None           
            else:
                curr = curr.next
        curr.next = last_head.next

        return first.next