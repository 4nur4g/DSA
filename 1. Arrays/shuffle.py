# https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newnum = []
        part1 = nums[:n]
        part2 = nums[n:]
        iterat = 1
        while iterat <= 2*n:
            if iterat % 2 == 0:
                toappend = part2.pop(0)
                newnum.append(toappend)
                iterat +=1
            else:
                toappend = part1.pop(0)
                newnum.append(toappend)
                iterat +=1
        return newnum