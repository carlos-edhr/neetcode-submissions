# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Sentinel before the head so every node has a predecessor
        dummy = ListNode(0, head)
        slow = fast = dummy

        #open a gap of n + 1 edges: fast ends up to n + 1 ahead of slow
        for _ in range(n + 1):
            fast = fast.next
        
        # slide both pointers until fast walks off the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        #slow is the predecessor of the n-th node from the end
        slow.next = slow.next.next

        return dummy.next

        