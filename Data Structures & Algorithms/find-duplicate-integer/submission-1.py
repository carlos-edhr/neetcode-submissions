class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find a meeting point inside the cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            # Tortoise one step
            slow = nums[slow]
            #hare two steps
            fast = nums[nums[fast]]

            if slow == fast:
                break
        # Phase 2: locate the cycle entrance, which is the duplicate
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

        