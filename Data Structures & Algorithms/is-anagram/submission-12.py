class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        count = [0] * 26

        for cs, ct in zip(s, t):

            count[ord(cs) - ord("a")] += 1
            count[ord(ct) - ord("a")] -= 1
        
        return all(value == 0 for value in count)

        # s_dict = dict()
        # t_dict = dict()
        # i = 0 

        # for x in s:
        #     s_dict[x] = s_dict.get(x, 0) + 1

        # for x in t:
        #     t_dict[x] = t_dict.get(x, 0) + 1


        # if s_dict == t_dict:
        #     return True
        # else:
        #     return False

        
             

        

        