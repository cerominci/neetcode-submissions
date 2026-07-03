class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = len(s)-1
        res = 0
        mp = set()

        for r in range(len(s)):
            while(s[r] in mp):
                mp.remove(s[l])
                l +=1
            mp.add(s[r])
            res = max(res,r-l+1)
        return res