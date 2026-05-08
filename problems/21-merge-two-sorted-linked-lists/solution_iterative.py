"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def merge_two_lists(self, list1, list2):
        dummy_head = Node(None)
        tail = dummy_head
        current1 = list1
        current2 = list2

        while current1 is not None and current2 is not None:
            if current1.val <= current2.val:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            
            tail = tail.next
        
        if current1 is not None:
            tail.next = current1
        
        if current2 is not None:
            tail.next = current2
        
        return dummy_head.next

    def print_list(self, list):
        current = list
        while current is not None:
            print(current.val, end=" ")
            current = current.next
        
        print()


a = Node(1)
b = Node(2)
c = Node(4)

a.next = b
b.next = c

d = Node(1)
e = Node(3)
f = Node(4)

d.next = e
e.next = f

s = Solution()
s.print_list(s.merge_two_lists(a, d))