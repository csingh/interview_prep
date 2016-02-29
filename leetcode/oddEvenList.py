# leetcode: https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import sys
sys.path.insert(0, '../CTCI6/')
from LLNode import *

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is not None and head.next is not None:
            insert = head # we move nodes to insert.next
            curr = head.next

            while curr is not None and curr.next is not None:
                # update curr pointer
                before_odd = curr
                curr = curr.next # this is an odd node

                print("insert:", insert)
                print("before_odd:", before_odd)
                print("curr:", curr)

                # save pointers before moving stuff around
                next_even_node = curr.next
                after_insert = insert.next

                # move stuff around
                insert.next = curr
                curr.next = after_insert
                before_odd.next = next_even_node

                # update insert pointer, reset curr pointer
                insert = insert.next
                curr = next_even_node

        LLNode.print_list(head)

        return head

if __name__ == '__main__':
    head = LLNode(1)
    head.next = LLNode(2)
    head.next.next = LLNode(3)
    head.next.next.next = LLNode(4)
    head.next.next.next.next = LLNode(5)

    LLNode.print_list(head)

    o = Solution()
    o.oddEvenList(head)