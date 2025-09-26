class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:   # already seen → duplicate found
                return True
            seen.add(num)
        return False


# Time: O(n)
# Space: O(n)
