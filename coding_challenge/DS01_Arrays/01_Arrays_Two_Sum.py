# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complimentDict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in complimentDict:
                return [complimentDict[compliment], i]
            else:
                complimentDict[nums[i]] = i
        return None

nums = [2,7,11,15]
target = 22

sol = Solution()
print(sol.twoSum(nums, target))


