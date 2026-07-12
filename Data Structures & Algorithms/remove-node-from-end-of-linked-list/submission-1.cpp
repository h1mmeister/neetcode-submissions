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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* first = head;
        ListNode* second = head;
        int k = 0;

        while (k < n) {
            second = second->next;
            k++;
        }

        if (second == nullptr) {
            head = first->next;
            return head;
        }

        while (second->next != nullptr) {
            first = first->next;
            second = second->next;
        }

        first->next = first->next->next;
        return head;
    }
};
