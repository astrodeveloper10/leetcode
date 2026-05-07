"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)
        res = []

        for num, count in nums1_counter.items():
            if num in nums2_counter:
                for _ in range(min(count, nums2_counter[num])):
                    res.append(num)
        
        return res


s = Solution()
print(s.intersect([1,2,2,1], [2,2]))