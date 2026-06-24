class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1

        while nums[i] + nums[j ] != target:
            print("i: ",i)
            for k in range(len(nums) - 1):
                print("j: ",j)
                j += 1
                if( j >  len(nums) -1  ):
                    continue
                if nums[i] + nums[j ] == target:
                    return [i, j]
            
            i +=  1 
            j = i +1
        return [i, j]