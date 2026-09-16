class Solution:
    def _is_palindrome(sef, arr, y, z):
        while y < z:
            if arr[y] != arr[z]:
                return False
            y += 1
            z -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left , right = 0 , len(s) - 1

        while left < right :
            if s[left] != s[right]:
                return self._is_palindrome(s, left +1, right) or self._is_palindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True
        

