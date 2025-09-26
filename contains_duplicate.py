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

# class Solution: → wrapper class (LeetCode requires it).
# def containsDuplicate(self, nums: list[int]) -> bool: → function that returns True/False.
# seen = set() → keeps track of unique numbers.
# Loop through nums:
# If number already in seen → return True (duplicate found).
# Else → add it to seen.
# If loop ends → return False (no duplicates).
