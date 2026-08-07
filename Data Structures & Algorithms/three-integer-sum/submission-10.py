class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        last = len(nums) - 1
        first = 0
        medium = 1
        triplets = []

        while first <= len(nums) - 3:
            # Skip duplicate 'first' values
            if first > 0 and nums[first] == nums[first - 1]:
                first += 1
                medium = first + 1          # reset medium
                last = len(nums) - 1        # reset last
                continue

            while medium < last:
                current_sum = nums[first] + nums[medium] + nums[last]

                if current_sum > 0:
                    last -= 1
                elif current_sum < 0:
                    medium += 1
                else:  # current_sum == 0
                    triplets.append([nums[first], nums[medium], nums[last]])

                    # Skip duplicate values for medium and last
                    while medium < last and nums[medium] == nums[medium + 1]:
                        medium += 1
                    while medium < last and nums[last] == nums[last - 1]:
                        last -= 1

                    # Move both pointers inward after skipping duplicates
                    medium += 1
                    last -= 1

            first += 1
            medium = first + 1
            last = len(nums) - 1

        return triplets