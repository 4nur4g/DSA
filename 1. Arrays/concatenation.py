# https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for ind in range(len(nums)):
            nums.append(nums[ind])
        return nums
