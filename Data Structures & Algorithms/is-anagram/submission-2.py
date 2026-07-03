class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp1 = {}
        mp2 = {}

        for s_num in s:
            mp1[s_num] = mp1.get(s_num,0) + 1
        for t_num in t:
            mp2[t_num] = mp2.get(t_num,0) + 1

        return mp1 == mp2