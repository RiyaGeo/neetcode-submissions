class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # for O(1) lookups
        longest = 0

        for num in num_set:
            # Only start counting if it's the START of a sequence
            # (i.e. num-1 doesn't exist)
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest