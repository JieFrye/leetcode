# Linked List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # start = head
        # while head:
        #     while head.next and head.val == head.next.val:
        #         head.next = head.next.next
        #     head = head.next
        # return start
    # Optimization
        if not head:
            return None
        if not head.next:
            return head
        root = head
        check = head.next
        while head.next:
            if head.val == check.val:
                # check the next node
                head.next = check.next
                check = check.next
            else:
                # move the pointers
                head = head.next
                check = check.next
        return root
# test case sorted linked list
n = 5
head = ListNode(1)
head.next = ListNode(1)
cur = head.next
for i in range(n):
    cur.next = ListNode(i+1)
    cur = cur.next
L = []
cur = head
while cur:
    L.append(cur.val)
    cur = cur.next
print(L)
# solve it
sol = Solution()
ans = sol.deleteDuplicates(head)
# output the result
LL = []
cur = ans
while cur:
    LL.append(cur.val)
    cur = cur.next
print(LL)
