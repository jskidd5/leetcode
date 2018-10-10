class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.index = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if len(self.stack) > self.index:
            self.stack[self.index] = x
        else:
            self.stack.append(x)
        self.index += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.index -= 1

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.index > 0:
            return self.stack[self.index - 1]
        else:
            return None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.index == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
obj.push(11)
obj.push(12)
obj.push(13)
param_2 = obj.pop()
param_2 = obj.pop()
obj.push(13)
param_3 = obj.top()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
