class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.topElem = Node(float("inf"), None)

    def top(self):
        return self.topElem.val

    def push(self, val):
        self.topElem = Node(val, self.topElem)

    def pop(self):
        self.topElem = self.topElem.next

class MinStack:
    def __init__(self):
        self.topElem: Node = Node()
        self.minElemStack = Stack()


    def push(self, val: int) -> None:
        self.topElem = Node(val, self.topElem)
        self.minElemStack.push(min(val, self.minElemStack.top()))

    def pop(self) -> None:
        if not self.isEmpty():
            self.topElem = self.topElem.next
            self.minElemStack.pop()

    def top(self) -> int:
        return self.topElem.val

    def getMin(self) -> int:
        return self.minElemStack.top()

    def isEmpty(self):
        return self.topElem.next == None
        

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())