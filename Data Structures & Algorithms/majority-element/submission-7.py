class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        nums.sort()

        for read in range(len(nums)):

            if nums[read] == majority:
                count += 1

            if majority == None:
                majority = nums[read]
                count += 1

            if nums[read] != majority:
                count = 1
                majority = nums[read]
            

            if count > int(len(nums) / 2):
                return majority
        
        return majority


        