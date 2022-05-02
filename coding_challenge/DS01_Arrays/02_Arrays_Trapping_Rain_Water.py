class Solution(object):
    def trap_brute(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        totalWater = 0
        for i in range(1, len(height) - 1):
            lMax = max(height[:i])
            rMax = max(height[(i + 1):])
            print(lMax, height[i], rMax)
            poolWater = min(lMax, rMax) - height[i]
            if poolWater > 0:
                totalWater += poolWater

            print({'i': i,
                   'poolWater': poolWater,
                   'totalWater': totalWater})
        return totalWater

    def trap(self, height):
        totalWater = 0
        lPointerID = 0
        rPointerID = len(height) - 1
        lMaxHeight = 0
        rMaxHeight = 0
        currentWater = 0
        while lPointerID < rPointerID:
            print('l Pointer ', height[lPointerID], 'r Pointer ', height[rPointerID])
            if height[lPointerID] <= height[rPointerID]:
                #   We need to update totalWater or update lMax
                print('Left Side Pointer ', height[lPointerID], 'Lmax ', lMaxHeight)
                if height[lPointerID] >= lMaxHeight:
                    lMaxHeight = height[lPointerID]

                else:
                    # currentWater = min(lMaxHeight, rMaxHeight) - height[lPointerID]
                    currentWater = lMaxHeight - height[lPointerID]
                    totalWater += currentWater
                lPointerID += 1
            else:
                print('Right Side Pointer ', height[rPointerID], 'Rmax ', rMaxHeight)
                #   We need to update totalWater or update lMax
                if height[rPointerID] >= rMaxHeight:

                    rMaxHeight = height[rPointerID]
                else:
                    # currentWater = min(lMaxHeight, rMaxHeight) - height[rPointerID]
                    currentWater = rMaxHeight - height[rPointerID]
                    totalWater += currentWater

                rPointerID -= 1

            print({'currentWater': currentWater,
                   'totalWater': totalWater})

        return totalWater

    def trap_clean(self, height):
        totalWater = 0
        lPointerID = 0
        rPointerID = len(height) - 1
        lMaxHeight = 0
        rMaxHeight = 0
        while lPointerID < rPointerID:
            if height[lPointerID] <= height[rPointerID]:
                if height[lPointerID] >= lMaxHeight:
                    lMaxHeight = height[lPointerID]
                else:
                    currentWater = lMaxHeight - height[lPointerID]
                    totalWater += currentWater
                lPointerID += 1
            else:
                if height[rPointerID] >= rMaxHeight:
                    rMaxHeight = height[rPointerID]
                else:
                    currentWater = rMaxHeight - height[rPointerID]
                    totalWater += currentWater
                rPointerID -= 1
        return totalWater


solution = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4,2,3]
print(height)
print(height[:3])
print(solution.trap_clean(height))
