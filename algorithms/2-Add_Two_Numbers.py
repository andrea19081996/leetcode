# DIFFICULTY: MEDIUM
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Examples:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        z = ListNode()
        cur_node = z
        prev_sum = 0
        while l1 or l2:
            curr_value = prev_sum
            if l1:
                curr_value += l1.val
                l1 = l1.next

            if l2:
                curr_value += l2.val
                l2 = l2.next

            prev_sum = curr_value // 10
            curr_value = curr_value % 10

            cur_node.next = ListNode(curr_value)
            cur_node = cur_node.next

        if prev_sum != 0:
            cur_node.next = ListNode(prev_sum)

        return z.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    solution = Solution()
    result = solution.addTwoNumbers(l1,l2)