# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:

    def twoSum(self, nums, target):

        complementDict = {}

        for i in range(len(nums)):
            n = nums[i]
            complement = target - n
            print(complement not in complementDict)

            if n in complementDict:
                return [i, complementDict[n]]

            if complement not in complementDict:
                complementDict[complement] = i
                print(complementDict)


        return []
    def twoSum_complements(self, nums, target):


        complement = {}

        for n in nums:
            if n not in complement:
                complement[target-n] = n
            if n in complement:
                return [n, complement[n]]

        return []

sol = Solution()
nums = [2,7,11,15]
target = 9

two_sums = sol.twoSum(nums, target)

print(two_sums)
