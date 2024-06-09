class Stack:
    def __init__(self) -> None:
        self.items = []
        
    def is_empty(self):
        # return len(self.items) == 0
        return not self.items
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def __str__(self) -> str:
        return str(self.items)
    
if __name__ == '__main__':
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(48)
    s.push('school')
    s.push(8)
    print(s.is_empty())
    print(s.size())
    print(s.peek())
    print(s)
    s.pop()
    print(s.size())
    print(s)
    