# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevNode = dummy
        while True:
            kth = self.Kth(prevNode, k)
            if not kth:
                break
            nextNode = kth.next
            # prevNode is the last node of list that has already been reversed
            prev, curr = kth.next, prevNode.next
            while curr != nextNode:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            temp = prevNode.next
            prevNode.next = kth
            prevNode = temp
        return dummy.next




    def Kth(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr
