class MinStack:

    def __init__(self):
        self.data = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        

    def pop(self) -> None:
        if len(self.data) != 0:
            del self.data[-1]

    def top(self) -> int:
        if len(self.data) != 0:
            return self.data[-1]

    def getMin(self) -> int:
        sart = sorted(self.data)
        return sart[0]
        
