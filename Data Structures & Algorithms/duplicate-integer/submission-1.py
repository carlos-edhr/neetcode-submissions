class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        foo = []
        for i in nums:
            if i not in foo:
                foo.append(i)
            else: 
                return True
        return False
        

         
        return False

        