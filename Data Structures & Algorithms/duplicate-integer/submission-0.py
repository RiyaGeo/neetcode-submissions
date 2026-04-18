class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_array = set()
        for i in nums:
            if i in new_array:
                return True
            else:
                new_array.add(i)
        return False