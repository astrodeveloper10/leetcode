"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        def reverse_list(head, prev=None):
            if head is None:
                return prev
            
            next = head.next
            head.next = prev

            return reverse_list(next, head)
        
        return reverse_list(head)

s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

print(s.reverseList(a))