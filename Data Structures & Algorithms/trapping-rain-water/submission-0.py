class Solution:
    def trap(self, height: List[int]) -> int:
        # compute leftMax
        leftMax = [0]*len(height)
        for i in range(1,len(height)):
            leftMax[i] = max(height[i-1],leftMax[i-1])  

        # compute rightMax
        rightMax = [0]*len(height)
        for i in range(len(height)-2,-1,-1):
            rightMax[i] = max(height[i+1],rightMax[i+1])

        total = 0
        for i in range(len(height)):
            total += max(0,min(leftMax[i],rightMax[i])-height[i])
        return total
 