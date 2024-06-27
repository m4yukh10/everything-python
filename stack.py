#stack implementation
class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.arr = [0] * self.size
        
        def push(val) -> None:
            self.top += 1
            self.arr[self.top] = val
        
        def pop() -> int:
            x = self.arr[self.top]
            self.top -= 1
            return x
        
        def display() -> str:
            stack = ""
            for i in range(self.top):
                stack += str(self.arr[i]) + " "
            stack.rstrip()
            return stack    
