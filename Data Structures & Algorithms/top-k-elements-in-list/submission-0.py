class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # loop through array count occurences of each number 
        # sort this data structure by size - descending order 
        # return as many positions as k 
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, freq in counts.items():
            (buckets[freq]).append(n)

        result = []
        for item in reversed(buckets):
            for n in item:
                result.append(n)
                if len(result) == k:
                    return result

        