
# Linked List
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ml = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                ml.next = l1
                l1 = l1.next
            else:
                ml.next = l2
                l2 = l2.next
            ml = ml.next
        # if one of l1 and l2 is None then link the rest of nonempty one
        ml.next = l1 or l2
        return start.next


# test case sorted linked list
L1 = ListNode(1)
L1.next = ListNode(2)
L1.next.next = ListNode(4)
L2 = ListNode(1)
L2.next = ListNode(3)
L2.next.next = ListNode(4)
LL1 = []
def p(head):
    L = []
    while head:
        L.append(head.val)
        head = head.next
    return L
print(p(L1), p(L2))
# solve it
sol = Solution()
ans = sol.mergeTwoLists(L1, L2)
# output the result
LL = []
cur = ans
while cur:
    LL.append(cur.val)
    cur = cur.next
print(LL)
