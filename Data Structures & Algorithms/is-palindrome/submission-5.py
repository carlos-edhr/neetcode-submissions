class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_array = [char.lower() for char in s if char.isalnum()]
        print(s_array)

        # for idx, char in enumerate(s_array):
        #     if not char.isalpha() or not char.isalnum() or char.isspace():
        #         s_array.pop(idx)
        
        left = 0 
        right = len(s_array) - 1

        while left < right:
            if s_array[left] != s_array[right]:
                return False
            left += 1
            right -= 1

        return True