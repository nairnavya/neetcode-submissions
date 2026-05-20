class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            pair = target - nums[i]
            for j in range(i, len(nums)):
                if (nums[j] == pair) and (i!=j):
                    return [i, j]