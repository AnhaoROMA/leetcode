"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""

"""
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prenode = head
        curnode = prenode.next
        while curnode is not None:
            if prenode.val == curnode.val:
                curnode = curnode.next
                prenode.next = curnode
                continue
            prenode = curnode
            curnode = curnode.next
        return head
