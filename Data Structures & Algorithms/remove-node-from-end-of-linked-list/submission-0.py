# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        k = 0

        while k < n:
            second = second.next
            k += 1

        if second is None:
            head = first.next
            return head

        while second.next is not None:
            first = first.next
            second = second.next
        
        first.next = first.next.next

        return head
        