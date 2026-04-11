"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        current= head
        after_father=None
        child_head=None
        while current:
            if current.child:
                if current.next:
                    after_father=current.next
                current.next= current.child
                current.child.prev= current
                current.child=None
                child_head=current.next
                while current and current.next:
                    current= current.next
                if after_father:
                    current.next=after_father
                    after_father.prev=current
                    after_father= None
                current=child_head
            else:
                current= current.next
        return head

                
