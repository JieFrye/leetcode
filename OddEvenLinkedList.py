# MAy 16 2020 LeetCode May Challenge
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        '''
        0 > 1->2->3->4->5
        odd 0 > 1->3->5->None
        even 0 > 2->4->None
        '''
        # two pointers for odd and even
        start1 = odd = ListNode(0)
        start2 = even = ListNode(0)
        while head:
            # pick up the odd/even nodes of the original LL
            odd.next = head
            even.next = head.next
            # move to the next node in the new odd/even LLs
            odd = odd.next
            even = even.next
            # move to the unassigned node of the original LL
            if even:
                head = head.next.next
            # end the loop if all nodes are assgined
            else:
                head = None
        # connect the odd LL to the even LL
        odd.next = start2.next
        return start1.next


# test case
n = 5
head = ListNode(1)
cur = head
for i in range(n-1):
    cur.next = ListNode(i+2)
    cur = cur.next
# solve it
sol = Solution()
ans = sol.oddEvenList(head)
# output the result
LL = []
cur = ans
for i in range(n):
    LL.append(cur.val)
    cur = cur.next
print(LL)
