class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def calc_sig(s):
            C = [0]*26
            for char in s:
                C[ord(char)-97]+=1
            return tuple(C)
        buckets = collections.defaultdict(list)
        for s in strs:
            buckets[calc_sig(s)].append(s)
        return list(buckets.values())

            