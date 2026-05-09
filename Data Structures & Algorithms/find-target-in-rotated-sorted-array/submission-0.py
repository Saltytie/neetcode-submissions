class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
       
        while (r - l) > 1:
            mid = (r + l) // 2
            if nums[mid] >= nums[r]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid 
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid 
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
            
         
