class Queue(list):
    push = list.append
    pop = list.pop

queue = Queue()
queue.push(1)
print("queue ", queue)
queue.push(2)
print("queue ", queue)
queue.push(3)
print("queue ", queue)
queue.pop(0)
print("queue ", queue)