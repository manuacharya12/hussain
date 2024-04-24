class Stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def display(self):
        return self.items
s=Stack()
s.isempty()
print("push operation")
s.push(14)
s.push(12)
s.push(11)
print("stack elements are")
print(s.display())
print("the top most element is",s.peek())
print("pop operation")
print("the deleted element is",s.pop())
print("the deleted element is",s.pop())
print("the stack elements are")
print(s.display())
print("size:",s.size())



