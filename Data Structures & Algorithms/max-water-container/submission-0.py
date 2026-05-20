class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        areas = []
        while l < r:
            areas.append((r-l) * min(heights[l], heights[r]))
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return max(areas)


        