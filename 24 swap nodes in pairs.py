"""
https://leetcode.com/problems/swap-nodes-in-pairs/
"""


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        guard_1 = head
        pre = guard_1
        head = head.next
        while guard_1 is not None:

            guard_2 = guard_1.next
            if guard_2 is None:
                return head
            pre.next = guard_1.next
            guard_1.next = guard_2.next
            guard_2.next = guard_1
            pre = guard_1
            guard_1 = guard_1.next

        return head
