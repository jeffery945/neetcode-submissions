# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None

        # reverse
        prev = None
        while second_half != None:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        second_half = prev
        
        while second_half:
            temp1, temp2 = head.next, second_half.next
            head.next = second_half
            second_half.next = temp1
            head = temp1
            second_half = temp2

