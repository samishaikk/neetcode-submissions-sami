class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0

        for i in range(n):
            left_max = max(height[:i+1])
            right_max = max(height[i:])

            water = min(left_max,right_max) - height[i]
            total_water += water

        return total_water