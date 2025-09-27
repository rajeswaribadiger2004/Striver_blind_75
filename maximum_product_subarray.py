class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = result = nums[0]  # start with first element

        for num in nums[1:]:
            if num < 0:  
                # negative number flips things → swap
                curr_max, curr_min = curr_min, curr_max

            # choose between starting fresh (num) or extending previous product
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            # update global result
            result = max(result, curr_max)

        return result

# Time: O(n). Space: O(1).
# Array: [2, 3, -2, 4]
# Start: curr_max = 2, curr_min = 2, result = 2
# Next num = 3
# curr_max = max(3, 2*3) = 6
# curr_min = min(3, 2*3) = 3
# Result = 6
# Next num = -2
# Negative → swap → curr_max=3, curr_min=6
# curr_max = max(-2, 3 * -2) = max(-2, -6) = -2
# curr_min = min(-2, 6 * -2) = min(-2, -12) = -12
# Result = 6 (still best so far)
# Next num = 4
# curr_max = max(4, -2*4) = 4
# curr_min = min(4, -12*4) = -48
# Result = 6
# ✅ Final Answer = 6 (subarray [2,3]).
