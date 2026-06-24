class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = dict()
        t_dict = dict()
        i = 0 

        for x in s:
            i = 0
            if x not in s_dict:
                s_dict.update({x: i })
                continue
            i += 1
            s_dict.update({x: i })

        for x in t:
            j = 0
            if x not in t_dict:
                t_dict.update({x: j})
                continue
            j += 1
            t_dict.update({x: j})


        if s_dict == t_dict:
            return True
        else:
            return False

        
             

        

        