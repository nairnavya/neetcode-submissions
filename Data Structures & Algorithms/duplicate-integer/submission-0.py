class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_map = {}
        for n in nums:
            if n in seen_map:
                return True
            else:
                seen_map[n] = 1
        
        return False