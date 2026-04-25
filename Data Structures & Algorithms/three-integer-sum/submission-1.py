class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        n= len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low = i+1
            high = n-1
            needed = -nums[i]
            while low<high:
                if nums[low]+nums[high] == needed:
                    results.append([nums[low],nums[high],-needed])
                    low +=1
                    high -=1
                    while low<high and nums[low]== nums[low-1]:
                        low +=1
                    while low<high and nums[high]==nums[high+1]:
                        high -=1
                elif nums[low]+nums[high]<needed:
                    low +=1
                else:
                    high -=1
        return results