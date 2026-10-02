# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        before = dummy

        for _ in range(left - 1 ):
            before = before.next
        #old head of window, future tail
        first = before.next
        #3-pointer reversal
        prev, curr = None, first
        #reverse exactly the window
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #tail -> ndoe after the window
        first.next = curr
        #predecessor -> new head of window
        before.next = prev

        return dummy.next
        