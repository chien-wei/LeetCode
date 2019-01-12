class MovingAverage:
    def __init__(self, size):
        self.queue = []
        self.size = size
    
    def next(self, val):
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.queue.pop(0)
        print(sum(self.queue)/len(self.queue))

ma = MovingAverage(3)
ma.next(1)
ma.next(10)
ma.next(3)
ma.next(5)
