class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_numbers = len(numbers) -1
        last = len_numbers
        first = 0
        idx_array =list()

        while last > first:
            current_sum = numbers[first] + numbers[last]
            if current_sum == target and first < last:
                return [first + 1, last + 1]
            if current_sum <  target :
                first += 1
            if current_sum > target:
                last -= 1 
            
        
        return []