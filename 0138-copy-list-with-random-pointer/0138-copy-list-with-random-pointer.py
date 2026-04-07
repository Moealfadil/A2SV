"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dic = {}
        current = head

        while current:
            dic[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            dic[current].next = dic.get(current.next)
            dic[current].random = dic.get(current.random)
            current = current.next

        return dic[head]