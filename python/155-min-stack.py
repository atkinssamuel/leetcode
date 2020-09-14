# Two stack solution, O(1) time-complexity, 80 ms, faster than 40.70%
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []
    
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        self.stack.append(x)
        if len(self.mins) == 0 or x < self.mins[-1]:
            self.mins.append(x)
        else:
            self.mins.append(self.mins[-1])
        
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()