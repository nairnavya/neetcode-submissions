class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = [] 

        for pos, spd in cars:
            curr_time = (target - pos) / spd

            
            if stack and curr_time <= stack[-1]:
                continue 

            stack.append(curr_time)

        return len(stack)

        
        # if ahead cars are faster, no chance of catching up
        # if ahead cars are slower, can catch up if:
        #   time for ahead car to reach target >= time for curr car to reach target
        #   (target-position[ahead])/speed[ahead] > (target-position[curr])/speed[curr]
        # for each car, find if cars ahead are slower
        # if there are slower cars ahead, see if you can catch up
        

        