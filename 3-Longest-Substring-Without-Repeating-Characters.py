class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        m = 0
        l = 0 
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
            m = max(m, r-l+1)
        return m
            
""" 
Runtime:
12ms
Beats
88.81% 
"""
