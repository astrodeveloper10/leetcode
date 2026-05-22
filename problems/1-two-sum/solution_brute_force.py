"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution:
    # we need indices of the two numbers that add up to target
    # so we should use either range or enumerate in order to get index

    # how do we check if two numbers equal to a target ?
    # Use two loops
    # First loop tracks i (0, n)
    # Second loop tracks j (i + 1 to n)
    # add them and see if they are equal
    # if nums[i] + num[j] == target:
    #   return [i, j]

    # we may not use the same element twice
    # "Just to clarify—when you say 'may not use the same element twice,'
    # do you mean I can't use the same index twice, or I can't use duplicate
    # values? For example, if the array is [3, 3] and target is 6, would
    # returning [0, 1] be valid?"

    # i = 0, j = 1, 2, 3, ...
    # i = 1, j = 2, 3, 4, ...

    # j = i + 1 avoids using the same element twice as
    # j is always greater than i

    # Problem with this solution:
    # We use two loops
    # First loop iterates from 0 to n
    # Second loop iterates from 1 to n
    # Worst case time complexity: O(n^2)
    # Can we improve our solution ?
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
