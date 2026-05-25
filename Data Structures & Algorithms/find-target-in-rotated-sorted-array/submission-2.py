class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while (l <= r):
            mid = (l+r) // 2

            if (nums[mid] == target):
                return mid
            
            if nums[mid] >= nums[l]: # you're on left sorted
                if target > nums[mid] or target < nums[l]: # if target on right
                    l = mid+1 # move to the right
                else:
                    r = mid-1 # move to the left
            else: # you're on right sorted
                if target < nums[mid] or target > nums[r]: # if target on right
                    r = mid-1
                else:
                    l = mid+1

        return -1


