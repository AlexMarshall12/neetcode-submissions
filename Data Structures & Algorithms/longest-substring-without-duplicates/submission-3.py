class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window

        l = 0
        r = 0
        charset = set()
        maxsize = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            maxsize = max(maxsize, r-l+1)
        return maxsize
