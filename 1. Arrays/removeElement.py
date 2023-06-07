
# https://leetcode.com/problems/remove-element/description/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0
        for item in nums:
            if item != val:
                nums[ind] = item
                ind += 1
        return ind
