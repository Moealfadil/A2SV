# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        original = ListNode(head.val)
        head_org = original
        
        current = head
        prev = None

        while current:
            if current.next:
                p = ListNode(current.next.val)
                original.next = p
                original = original.next

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        p1 = head_org
        p2 = prev

        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True