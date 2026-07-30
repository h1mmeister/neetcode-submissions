/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ptr1 {l1};
        ListNode* ptr2 {l2};

        int carry {0};
        ListNode* dummy_node = new ListNode(-1);
        ListNode* curr_node = dummy_node;

        while (ptr1 != nullptr || ptr2 != nullptr || carry != 0) {
            int ptr1_val = (ptr1 != nullptr) ? ptr1->val : 0;
            int ptr2_val = (ptr2 != nullptr) ? ptr2->val : 0;

            int curr_sum = ptr1_val + ptr2_val + carry;
            int value = curr_sum % 10;
            ListNode* new_node = new ListNode(value);
            curr_node->next = new_node;
            curr_node = new_node;

            carry = curr_sum / 10;
            ptr1 = (ptr1 != nullptr) ? ptr1->next: nullptr;
            ptr2 = (ptr2 != nullptr) ? ptr2->next: nullptr;
        }

        return dummy_node->next;   
    }
};
