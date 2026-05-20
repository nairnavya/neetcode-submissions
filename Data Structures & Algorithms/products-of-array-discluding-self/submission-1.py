class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total_product = 1
        total_product_0 = 1
        zerofreq = nums.count(0)
        for n in nums:
            total_product = n * total_product
            if n != 0 and zerofreq == 1:
                total_product_0 = n * total_product_0
        
        output = []
        
        for n in nums:
            if n == 0 and zerofreq == 1:
                output.append(total_product_0)
            elif zerofreq > 1:
                output.append(0)
            else:
                output.append(int(total_product/n))

        return output