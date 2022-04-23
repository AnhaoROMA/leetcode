"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        pre = None
        nkt = None
        ptrs = [None] * (k + 1)
        count = 0
        while count < k:
            if ptr is None:
                return head
            ptrs[count] = ptr
            ptr = ptr.next
            count += 1
        nkt = ptr
        pre = ptrs[0]
        pre.next = ptrs[k - 1]
        ptrs[k] = nkt
        head = ptrs[k - 1]
        # print(head)
        for count in range(k):
            ptrs[count].next = ptrs[count - 1]
        # print(head)

        while True:
            ptr = nkt
            count = 0
            while count < k:
                if ptr is None:
                    return head
                ptrs[count] = ptr
                ptr = ptr.next
                count += 1
            nkt = ptr
            pre.next = ptrs[k - 1]
            ptrs[k] = nkt
            for count in range(k):
                ptrs[count].next = ptrs[count - 1]
            pre = ptrs[0]
        return head
