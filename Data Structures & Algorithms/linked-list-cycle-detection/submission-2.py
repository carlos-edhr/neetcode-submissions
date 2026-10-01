# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        #use two pointers: slow and fast
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # condition to prove a cycle exists
            if slow is fast:
                return True
        
        return False



        # # dummy list node for initial list condition
        # prev = ListNode()
        # prev.index = -4
        # # Assign head index = 0
        # curr = head
        # curr.index = int(-1)
        # # Traverse linked list 
        # while curr:
        #     #evaluate if the current node was already visited before
        #     if curr.index < prev.index:
        #         #Cycle condition is positive
        #         prev.index = curr.index
        #         return True
        #     #assign the index for each node visited
        #     curr.index += 1
        #     #assign previous to current node
        #     curr.prev = curr
        #     #advance to next position
        #     curr = curr.next

        # curr.index = -1

        # return False


        # if there is a cyce ensure that index = index-th node
        # if no cycle then index = -1

        #return true or false depending if there is a cycle
        
        