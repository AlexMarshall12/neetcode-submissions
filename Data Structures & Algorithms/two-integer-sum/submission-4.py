class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i,n in enumerate(nums):
            a[n] = i
        for i,n in enumerate(nums):
            s = target - n
            if s in a and a[s] != i:
                return [i,a[s]]
        