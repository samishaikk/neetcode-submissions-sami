class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min (heights[left],heights[right])
            area = width * current_height

            max_area = max(max_area,area)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1
        
        return max_area
    
## APPROACH
'''
I'll use two pointers from both ends. 
Calculate area with current pointers, then move the pointer with smaller height inward (since moving the taller one can't increase area). 
Track maximum area. Time O(n), space O(1).
'''