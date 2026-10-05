# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head    
        leng = 1
        tail = head
        while tail.next:
            tail = tail.next
            leng += 1    
        k = k % leng
        if k == 0:
            return head    
        tail.next = head
        s = leng - k - 1
        new = head
        for _ in range(s):
            new = new.next   
        newh = new.next
        new.next = None
        return newh