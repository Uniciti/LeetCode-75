# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node is None or node.next is None:
            return node

        buf = node
        while node.next:
            buf = node
            node = node.next
        buf.next = None
        node.next = self.reverseList(head=head)
        return node