class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('Inf')
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.insert(0, x)
        self.min = min(self.min, x)
        

    def pop(self):
        """
        :rtype: void
        """
        if self.top() == self.min:
            print("in")
            self.min = float('Inf')
            self.stack.pop(0)
            for x in self.stack:
                self.min = min(self.min, x)
        else:
            self.stack.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()