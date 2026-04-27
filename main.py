#Queue two stacks
class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def _reverse(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def dequeue(self):
        if self.size() == 0:
            return None
        
        self._reverse()
        return self.out_stack.pop()

    def front(self):
        if self.size() == 0:
            return None
            
        self._reverse()
        return self.out_stack[-1]

    def size(self):
        return len(self.in_stack) + len(self.out_stack)
