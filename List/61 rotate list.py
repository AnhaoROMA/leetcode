"""
https://leetcode.com/problems/rotate-list/

Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""


#
# 既然需要rotate，那不如先串成一个环吧！
#
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        length = 1
        tail = head
        while tail.next is not None:
            length += 1
            tail = tail.next

        # 此时此刻，tail指针指向链表的最后一个节点
        tail.next = head
        valid_k = k % length

        valid_k = length - valid_k
        for _ in range(valid_k):
            head = head.next
            tail = tail.next
        tail.next = None
        return head
