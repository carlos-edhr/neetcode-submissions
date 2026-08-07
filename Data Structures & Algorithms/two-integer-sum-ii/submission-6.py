class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        last = len(numbers) -1
        first = 0

        while last > 0:
            current_sum = numbers[first] + numbers[last]
            if current_sum == target and first < last:
                return [first + 1, last + 1]
            if current_sum <  target :
                first += 1
            if current_sum > target:
                last -= 1 
            
        
        return []