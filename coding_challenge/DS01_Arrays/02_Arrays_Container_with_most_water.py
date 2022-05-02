class Solution(object):
    def maxArea_brute(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        for l in range(len(height)-1):
            for r in range(l+1, len(height)):
                if area < (min(height[l], height[r]) * (r-l)):
                    area = min(height[l], height[r]) * (r-l)
        return area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l = 0
        r = len(height)-1
        while l != r:
            area = min(height[l], height[r]) * (r - l)
            print(l, r, area)
            if maxArea < area:
                maxArea = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea

solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))