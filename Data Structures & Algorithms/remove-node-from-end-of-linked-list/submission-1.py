# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head 
        if not head.next:
            return None
        slow = head
        fast = head
        prev = None
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        if not prev:
            head = slow.next
            slow.next = None
    
        else:
            prev.next = slow.next
        
        return head
        