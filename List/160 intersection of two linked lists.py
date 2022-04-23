"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        a = headA
        b = headB
        while a is not None and b is not None:
            a = a.next
            b = b.next
        if a is None:
            a = headB
            while b is not None:
                a = a.next
                b = b.next
            b = headA
        else:
            b = headA
            while a is not None:
                a = a.next
                b = b.next
            a = headB
        while a is not None and b is not None:
            if a == b:
                return a
            a = a.next
            b = b.next

        return None
