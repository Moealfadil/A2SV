# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head, k):
        current = head
        count = 0
        
        while current:
            count += 1
            current = current.next
        
        length = count // k
        carry = count % k
        
        result = []
        nxt = head
        
        for i in range(k):
            current = nxt
            sub_head = current
            
            if carry > 0:
                r = 1
                carry -= 1
            else:
                r = 0
            
            if current:
                for j in range(length + r - 1):
                    current = current.next
                nxt = current.next
                current.next = None
            else:
                nxt = None
                sub_head = None
            
            result.append(sub_head)
        
        return result