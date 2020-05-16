# Linked List
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = s = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            s.next = ListNode(carry % 10)
            s = s.next
            carry = carry // 10
        return root.next


L1 = ListNode(2)
L1.next = ListNode(4)
# L1.next.next = ListNode(3)
L2 = ListNode(5)
L2.next = ListNode(6)
# L2.next.next = ListNode(4)
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
ans = sol.addTwoNumbers(L1, L2)
# output the result
LL = []
cur = ans
while cur:
    LL.append(cur.val)
    cur = cur.next
print(LL)
