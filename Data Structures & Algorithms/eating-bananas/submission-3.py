class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i] = num of bananas in ith pile
        # h = num of hours to eat all bananas
        # k = num of bananas you can eat in an hour 

        l, r = 1, max(piles)
        ans = r 

        while (l <= r):
            k = (l+r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if (hours <= h):
                ans = k
                r = k - 1

            else:
                l = k + 1

        return ans