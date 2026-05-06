# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        last = head
        past = head.next
        fpast = past

        while past and past.next:
            last.next = past.next
            last = last.next

            past.next = last.next
            past = past.next

        last.next = fpast
        return head