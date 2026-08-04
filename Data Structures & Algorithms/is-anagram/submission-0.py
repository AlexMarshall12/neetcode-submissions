import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = collections.Counter()
        for char in s:
            h[char]+=1
        k = collections.Counter()
        for char in t:
            k[char]+=1
        if len(h.keys())!=len(k.keys()):
            return False
        for key,val in h.items():
            if k[key] != val:
                return False
        return True