class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in nums:
            for idx, value in enumerate(nums):
                if idx  == len(nums) -1:
                    break
                if value > nums[idx + 1  ]:
                      nums[idx + 1  ],  nums[idx  ] =  nums[idx  ],  nums[idx + 1  ]
        return nums
            
        