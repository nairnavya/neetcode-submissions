import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i] = num of bananas in ith pile
        # h = num of hours to eat all bananas
        # k = num of bananas you can eat in an hour 

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            k = (low + high) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                ans = k
                high = k - 1
            else:
                low = k + 1
        return ans