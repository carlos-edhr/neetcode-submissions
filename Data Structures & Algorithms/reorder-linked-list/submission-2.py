# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return 
        
        # Phase 1: find the lef-middle node
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
        
        # Phase 2: split  after slow and reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev

        #Phase 3: interleave first half and reversed second half
        first = head
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next  = first_next 
            first = first_next 
            second = second_next
            

   








        #[0, 6, 1, 5, 2, 4, 3]

        