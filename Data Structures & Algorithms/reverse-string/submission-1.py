class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        def swap(i, j):
            tmp = s[i]
            s[i] =  s[j]
            s[j] = tmp

        

        while left < right:
            #s[left] , s[right] = s[right], s[left]
            swap(left, right)
            left += 1
            right -= 1
        




        