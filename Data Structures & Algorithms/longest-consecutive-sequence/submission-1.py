class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        nums.sort()
        print(nums)
        count = 0
        best_count = 0

        for i in range(0,len(nums)):
            print("")
            print(f"number is {nums[i]}")

            if (i != 0) and (nums[i]==nums[i-1]):
                print("skipped")
                continue

            if (i != 0) and (nums[i]==nums[i-1]+1):
                count += 1
                print("count was incremented")

            else: 
                count = 0

            if best_count < count:
                best_count = count

            print(f"count is {count}")
        return best_count+1
