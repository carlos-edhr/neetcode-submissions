class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        k =0 
        i = 0
        j = 0
        while len(word1) > i or len(word2) > j:
            if k % 2 == 0 and len(word1) > i:
                merged_string += word1[i]
                i += 1
                k+= 1
            if len(word2) > j and k % 2 == 1:
                merged_string += word2[j]
                j += 1
                k += 1
            if i >= len(word1):
                merged_string += word2[j:]
                break
            if j >= len(word2):
                merged_string += word1[i:]
                break

        return merged_string
        