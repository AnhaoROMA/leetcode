"""
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

# 快慢指针


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast is not None:
            fast = fast.next
            if fast is None:
                return slow
            fast = fast.next
            slow = slow.next
        return slow
