"""
스택: LIFO 자료구조
"""

class Stack(list):
    push = list.append
    pop = list.pop

    def is_empty(self):
        if not self:
            return True
        else:
            return False

stack = Stack()
stack.push(1)
print("stack", stack)
stack.push(2)
print("stack", stack)
stack.push(3)
print("stack", stack)
stack.pop()
print("stack", stack)