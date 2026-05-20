class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return indices (one-indexed)
        # pair should add up to target 
        # first index num < second index num
        # cannot use the same index twice
        # always one distinct solution
        for i in range(0,len(numbers)):
            search = target-numbers[i]
            print("")
            print(f"num to search for is {search}")
            i2 = self.binarySearch(numbers,search)
            print(f"i2 output is {numbers[i2]}")
            if i2==-1:
                continue
                print(f"{search} skipped")
            print(f"correct nums are {numbers[i]} and {numbers[i2]}")
            return [i+1,i2+1]
        
    def binarySearch(self, nums: List[int], search: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if (search > nums[mid]):
                l = mid+1
            elif (search < nums[mid]):
                r = mid-1
            else:
                return mid
        return -1
        
