class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = [0] * 26
        left = 0
        max_freq = 0
        max_len = 0

        for right, ch in enumerate(s):
            freq[ord(ch) - ord("A") ] += 1
            max_freq = max(max_freq, freq[ord(ch) - ord("A") ])

            while (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord("A") ] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
        
        return max_len
        