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
        curr = head
        oldTonew = {None: None}
        while curr:
            copy = Node(curr.val)
            oldTonew[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldTonew[curr]
            copy.next = oldTonew[curr.next]
            copy.random = oldTonew[curr.random]
            curr = curr.next
        return oldTonew[head]