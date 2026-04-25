class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        low =0
        high = n-1
        max_water =0
        while low<high:
            current_vol=(high - low) * min(heights[high],heights[low])
            max_water = max(max_water, current_vol)
            
            if heights[low]> heights[high]:
                high -=1
            else:
                low +=1
        return max_water