class Stack:
    def __init__(self):
        self.stack=[]   #empty stack onto stack
    def push(self,item):
        self.stack.append(item)  #push item onto stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  #pop item top element
        else:
            return None              #Return None if stack is empty
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]   #Return top element without removing it
        else:
            return None             #Return None if stack is empty
    def is_empty(self):
        return len(self.stack)==0   #Check if stack is empty
    def size(self):
        return len(self.stack)  #Return number of items in stack
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.peek())
print(s.pop())
print(s.size())