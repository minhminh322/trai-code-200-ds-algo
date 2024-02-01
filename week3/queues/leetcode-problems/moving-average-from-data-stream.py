from collections import deque 
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val
        if len(self.queue) > self.size:
            popVal = self.queue.popleft()
            self.sum -= popVal
        
        return self.sum / len(self.queue)