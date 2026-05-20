class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for n in nums:
            elements[n] = elements.get(n, 0) + 1
        count = 0
        output = []
        while count != k:
            output.append(max(elements, key=elements.get))
            del elements[max(elements, key=elements.get)]
            count += 1
        return output
            
                