class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            dict[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict and dict[diff] != i:
                return [i, dict[diff]]
        return []