class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i, num in enumerate(nums):
            seen[num] = i
        
        for i in range(len(nums)):
            check = target-nums[i]
            if check in seen:
                if seen[check] == i:
                    continue
                else:
                    return [i, seen[check]] if i < seen[check] else [seen[check], i]