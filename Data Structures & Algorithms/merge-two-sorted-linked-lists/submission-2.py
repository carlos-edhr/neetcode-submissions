# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()          # sentinel: lets every append be uniform
        tail = dummy                # last emitted node

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1   # take the smaller head from list1
                list1 = list1.next
            else:
                tail.next = list2   # take the smaller head from list2
                list2 = list2.next
            tail = tail.next        # advance the output tail

        tail.next = list1 or list2  # attach whichever suffix remains
        return dummy.next           
        # dummy = ListNode()
        # tail = dummy

        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         tail.next = list1
        #         list1 = list1.next
        #     else:
        #         tail.next = list2
        #         list2 = tail.next 
        #     tail = tail.next
        
        # tail.next = list1 or list2

        # return dummy.next



        # if list1.val is None and list2.val is None:
        #     return []
        
        # new_list = ListNode()

        

        # while new_list.val is not None:
        #     if list1 is not None:
        #         if list1.val <= list2.val:
        #             new_list.val = list1.val
        #             list1 = list1.next
        #             new_list.next =  None
        #         else:
        #             if list2 is not None:
        #                 new_list.val = list2.val




        