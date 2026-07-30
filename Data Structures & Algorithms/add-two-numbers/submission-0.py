# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        carry = 0
        dummy_node = ListNode(-1)
        curr_node = dummy_node

        while ptr1 or ptr2 or carry != 0:
            node_one_val = ptr1.val if ptr1 is not None else 0
            node_two_val = ptr2.val if ptr2 is not None else 0
            curr_sum = node_one_val + node_two_val + carry

            value = curr_sum % 10
            new_node = ListNode(value)
            curr_node.next = new_node
            curr_node = new_node

            carry = curr_sum // 10

            ptr1 = ptr1.next if ptr1 is not None else None
            ptr2 = ptr2.next if ptr2 is not None else None

        return dummy_node.next

        