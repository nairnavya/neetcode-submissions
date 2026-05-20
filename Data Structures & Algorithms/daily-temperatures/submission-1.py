class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        result = []
        for i in range(0,len(temperatures)):
            # s.push(temp)
            j = i+1
            count = 0
            while j != len(temperatures) and temperatures[i] >= temperatures[j]: 
                count += 1
                j += 1
            if j != len(temperatures):
                result.append(count+1)
            else:
                result.append(0)
        return result


        
        #for i in range(0,len(input)):
        #    s.push(temp)
        #    j = i+1
        #    count = 0
        #    while temp[i] < temp[j]: 
        #        count += 1
        #        j += 1
        #    result[i] = count+1

            
