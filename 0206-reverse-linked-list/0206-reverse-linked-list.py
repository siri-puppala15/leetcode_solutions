# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        p = None
        c = head
        while c is not None:
            new = c.next
            c.next = p
            p = c
            c = new
        return p
