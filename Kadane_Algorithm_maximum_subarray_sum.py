from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # assume len(nums) >= 1 (LeetCode guarantees this)
        max_ending = max_so_far = nums[0]
        for num in nums[1:]:
            max_ending = max(num, max_ending + num)
            max_so_far = max(max_so_far, max_ending)
        return max_so_far


# Input: A list of integers nums.
# Initialize:
# max_ending = nums[0] → max sum ending at current index.
# max_so_far = nums[0] → max sum found so far.
# Iterate through the array from index 1:
# max_ending = max(num, max_ending + num) → either start new subarray or extend current.
# max_so_far = max(max_so_far, max_ending) → update global max.
# Return: max_so_far → maximum subarray sum.
# Complexity:
# Time: O(n)
# Space: O(1)
# ✅ Example: For [-2,1,-3,4,-1,2,1,-5,4] → max sum = 6

