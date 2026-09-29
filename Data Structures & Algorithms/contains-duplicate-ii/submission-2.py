class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for right, value in enumerate(nums):
            if value in window: 
                return True
            window.add(value)
            if len(window) > k:
                window.remove(nums[right - k])
        return False
