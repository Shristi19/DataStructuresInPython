

###Simple Implementation###


def deque(list):
    if len(list)!=0:
        print(list[0])
        del list[0]
    else:
        print('The queue is empty')


queue=[(8,'a'),(2,'B'),(78,'c')]

def enqueue(queue,priority,data):
    queue.append((priority,data))


enqueue(queue,89,'c')


###Every time you use a deque operation simply sort the list by the first element of the tuple which is the  priority number

queue.sort(key=lambda x:x[0])
deque(queue)
deque(queue)
deque(queue)
deque(queue)
deque(queue)





