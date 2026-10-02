# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            # pad a shorter number with 0
            x = l1.val if l1 else 0 
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next


        # l1_str = ""
        # l2_str = ""

        # while l1:
        #     l1_str += str(l1.val)
        #     l1 = l1.next
        
        # while l2:
        #     l2_str += str(l2.val)
        #     l2 = l2.next
        
        # l1_str_reversed = l1_str[: :-1]
        # l2_str_reversed = l2_str[: : -1]
        # l1_num = int(l1_str_reversed)
        # l2_num = int(l2_str_reversed)
        # total_str = str(l1_num + l2_num)

        # result_list = ListNode(0, None)
        # for char in total_str:
        #     result_list.val = int(char)
        #     result_list = result_list.next
        
        # return result_list
        