class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class LinkedList:
    def __init__(self):
        self.head=None


liist=LinkedList()

liist.head=Node(1)
second=Node(2)
third=Node(3)
second.previous=liist.head
liist.head.next=second
second.next=third
third.previous=second


def printLiist(liist):
    temp=liist.head
    while temp:
        print(temp.data,end="-->>")
        temp=temp.next

printLiist(liist)

print("\n"+str(liist.head.next.next.previous.data))
