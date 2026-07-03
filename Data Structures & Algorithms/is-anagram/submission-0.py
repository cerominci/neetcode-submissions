class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        for letter in s:
            if not letter in s_set.keys():
                s_set[letter] = 0;
            else: s_set[letter] = s_set[letter] + 1
        
        for letter in t:
            if not letter in t_set.keys():
                t_set[letter] = 0;
            else: t_set[letter] = t_set[letter] + 1       

        if(s_set == t_set):
            return True
        return False       
        