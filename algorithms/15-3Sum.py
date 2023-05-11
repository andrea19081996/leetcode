# DIFFICULTY: MEDIUM
#
# Given an integer array nums, return all the triplets[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are[-1, 0, 1] and [-1, -1, 2]. Notice that the order of the output and the order of the triplets does not matter.
#
# Example 2:
# Input: nums = [0, 1, 1]
# Output: []
# Explanation:
# The only possible triplet does not sum up to 0.
#
# Example 3:
# Input: nums = [0, 0, 0]
# Output: [[0, 0, 0]]
# Explanation:
# The only possible triplet sums up to 0.
#
# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue

            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # Skip duplicates
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # Skip duplicates
                        right -= 1
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res

    # OTHER SOLUTION
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     return [list(x) for x in set(tuple(x) for x in [sorted(tuple(x)) for x in self.aux_threeSum([], nums)])]
    #
    # def aux_threeSum(self, chosen_number, nums: List[int]) -> List[List[int]] | None:
    #     result = []
    #     # case chosen_number needs last element
    #     if len(chosen_number) == 3:
    #         if sum(chosen_number) == 0:
    #             return [chosen_number]
    #         return
    #     if len(nums) == 0:
    #         return
    #
    #     aux_array = chosen_number.copy()
    #     aux_array.append(nums[0])
    #     first_sub_result = self.aux_threeSum(aux_array, nums[1:])
    #     second_sub_result = self.aux_threeSum(chosen_number, nums[1:])
    #     if first_sub_result:
    #         result.extend(first_sub_result)
    #     if second_sub_result:
    #         result.extend(second_sub_result)
    #     return result


if __name__ == '__main__':
    s = Solution()
    result = s.threeSum([-15,6,7,0,-14,-5,-3,-10,-14,1,-14,-1,-11,-11,-15,-1,3,-12,7,14,1,6,-6,7,1,1,0,-4,8,7,2,1,-2,-6,-14,-9,-3,-1,-12,-2,7,11,4,12,-14,-4,-4,4,-1,10,3,-14,1,12,0,10,-9,8,-9,14,-8,8,0,-3,10,-6,4,-8,0,-1,-3,-8,-4,8,11,-3,-11,-8,8,3,10,-3,-4,-4,-14,12,13,-8,-3,12,-8,4,5,-1,-14,-8,8,-3,-9,-15,12,-5,-7,-15,-12,11,-11,14,11,12,3,6,-6])
    print(result)