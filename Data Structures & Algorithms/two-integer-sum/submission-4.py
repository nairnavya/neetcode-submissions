class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        first_occur = 1001
        for i in range(len(nums)):
            if (nums[i]) in seen_map:
                first_occur = seen_map[nums[i]]
            seen_map[nums[i]] = i
        print(first_occur)
        print(seen_map)

        search = 0
        for key in seen_map:
            search = target - key 
            print("search is", search)
            if search in seen_map and first_occur != 1001:
                return [first_occur, seen_map[search]]
            if search in seen_map and search != key:
                print("current key index is", seen_map[key])
                print("current seach index is", seen_map[search])
                return [seen_map[key], seen_map[search]]