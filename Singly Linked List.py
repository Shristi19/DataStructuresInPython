class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

liist=LinkedList()

liist.head=Node(1)
second=Node(2)
third=Node(3)

liist.head.next=second
second.next=third

def printLiist(liist):
    temp=liist.head
    while temp:
        print(temp.data,end="-->>")
        temp=temp.next
    print()
printLiist(liist)

####Inserting Node at the begining####3



def insert_at_first(data):
    temp=liist.head

    liist.head=Node(data)
    liist.head.next=temp

insert_at_first(34)

printLiist(liist)

def insert_at_last(data):
    temp=liist.head
    while temp.next!=None:
        temp=temp.next
    temp.next=Node(data)

insert_at_last(90)
printLiist(liist)

def insert_after(tobe_inserted_after,data):
    temp=liist.head
    while temp.data!=tobe_inserted_after:
        temp=temp.next
    #temp.next====the one whose data is the one

    x=temp.next
    new_node=Node(data)
    temp.next=new_node
    new_node.next=x

insert_after(2,56)
printLiist(liist)

#####Deletion of a node #####
def delete_node(to_be_deleted):
    temp=liist.head
    if temp.data==to_be_deleted:
        liist.head=temp.next
        temp=None
        return
    else:
        prev=None
        while temp is not None:
            if temp.data==to_be_deleted:
                break
            prev=temp
            temp=temp.next
        prev.next=temp.next
        temp=None
         






delete_node(34)
printLiist(liist)











