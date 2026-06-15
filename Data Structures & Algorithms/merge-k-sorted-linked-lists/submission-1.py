# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return None
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists
        while len(lists) != 1:
            mergelist = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergelist.append(self.mergelinkedlist(l1, l2))
            lists = mergelist
        return lists[0]

        


    def mergelinkedlist(self, list1, list2):
        dummy = ListNode()
        node = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        if list1:
            node.next = list1
        if list2:
            node.next = list2

        return dummy.next