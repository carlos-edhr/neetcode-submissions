class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        count = 0
        nums.sort()

        for read in range(len(nums)):
            print("Read: ", read)
            print("Current: ", nums[read])

            if nums[read] == majority:
                count += 1

            if majority == None:
                majority = nums[read]
                count += 1

            if nums[read] != majority:
                count = 1
                majority = nums[read]
            
            print("Count: ", count)
            print("Majority: ", majority)
            print("----------")
            print( f" count " + str(count) + ",  count >  n / 2 : " + str(count > int(len(nums) / 2)))

            if count > int(len(nums) / 2):
                return majority
        
        return majority


        