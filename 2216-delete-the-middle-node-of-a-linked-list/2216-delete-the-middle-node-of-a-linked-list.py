# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        first = head
        node = head
        while node.next:
            n += 1
            node = node.next
        if n == 1:
            return None
        i = 0
        node = first
        prev = first
        while i < n // 2:
            i += 1
            node = node.next
            if i == (n // 2 - 1):
                prev = node
            print(i, n // 2)

        prev.next = node.next
        return first