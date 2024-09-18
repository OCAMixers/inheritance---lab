class Stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.item = item
        if isinstance(item, str):
            self.data.append(item)
        else:
            raise ValueError("Chi co the them chuoi vao stack.")
    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            raise IndexError("Stack rong, khong the pop.")
    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            return None
    def is_empty(self):
        return len(self.data) == 0
    def __str__(self): 
        return f"Stack: {self.data}"
stack = Stack()
stack.push("Hello")
stack.push("World")
print(stack) 
print(stack.peek())  
print(stack.pop()) 
print(stack.is_empty())  
print(stack)