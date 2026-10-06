# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        else:
            slow = head
            fast = head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next    
                if slow == fast:
                    s = head
                    t = slow
                    while s!=t:
                        s = s.next
                        t = t.next
                    return s
            return None

        