from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i, n in enumerate(nums):
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i


# Python two-pointer
class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = sorted(zip(nums, range(len(nums))))
        print(l)
        left, right = 0, len(l) - 1
        while left < right:
            print(l[left][0], l[right][0])
            if v == target:
                return [l[left][1], l[right][1]]
            if v < target:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution2()
    s.twoSum(nums, target)
