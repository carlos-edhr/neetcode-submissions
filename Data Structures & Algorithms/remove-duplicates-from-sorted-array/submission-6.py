class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #'write' points to the position where the next unique element
        #will be placed
        write = 1
        # 'read' scans the array starting from the second element
        for read in range(1, len(nums)):
            # if current element is different from previous one
            # it is a new unique element
            if nums[read] != nums[read - 1 ]:
                nums[write] = nums[read]
                write += 1
        return write