from collections import deque
class Queue:
    def __init__(self):
        self.queue=deque() 
    def enqueue(self,item):
        self.queue.append(item)   #Add item to the end of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()  #Remove and return the item at the front of the queue
        else:
            return None         #Return None if the queue is empty
    def peek(self):
        if not self.is_empty():
            return self.queue[0]  #Return the item at the front of the queue without removing it
        else:
            return None         #Return None if the queue is empty
    def is_empty(self):
        return len(self.queue)==0           #Check if the queue is empty
    def size(self):
        return len(self.queue)      #Return the number of items in the queue
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.peek())
print(q.dequeue())
print(q.size()) 


