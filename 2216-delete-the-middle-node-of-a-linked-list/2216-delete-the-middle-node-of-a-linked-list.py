# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next is None:
            return None
        
        n = 1
        node = head

        while node.next:
            n += 1
            node = node.next

        prev = head
        for _ in range(n // 2 - 1):
            prev = prev.next

        prev.next = prev.next.next
        return head