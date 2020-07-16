# Remove Duplicates from Sorted List II
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        use two pointers
        s,L  h
        |    |
        0 -> 1->2->3->3->4->4->5

        s    L  h
        |    |  |
        0 -> 1->2->3->3->4->4->5

        s       L  h
        |       |  |
        0 -> 1->2->3->3->4->4->5
        '''
        start = L = ListNode(0)
        start.next = head
        while head and head.next:
            # either same values
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next # move to 4
                L.next = head # skip 3's and connect to 4
            # or different values
            else:
                L = L.next
                head = head.next
        return start.next
