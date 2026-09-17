class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right :
            result = numbers[left] + numbers[right]
            if result == target:
                return [left + 1, right + 1]
            elif result > target:
                right -= 1
            else: 
                left += 1 





























        # last = len(numbers) -1
        # first = 0

        # while last > 0:
        #     current_sum = numbers[first] + numbers[last]
        #     if current_sum == target and first < last:
        #         return [first + 1, last + 1]
        #     if current_sum <  target :
        #         first += 1
        #     if current_sum > target:
        #         last -= 1 
            
        
        # return []