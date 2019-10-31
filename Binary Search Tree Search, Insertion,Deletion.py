class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key

def search(root,key):
    flag=0
    while root:
        if root.val == key:
            print("found")
            flag=1
            break
        else:
            if key>root.val:
                root=root.right
            else:
                root = root.left
    if flag == 0:
        print("Not found")


def insert(root1,key):
    x=Node(key)

    if root1 is None:
        root1 = x

    else:
        if key>root1.val:
            if root1.right is None:
                root1.right = x
            else:
                insert(root1.right,key)
        else:
            if root1.left is None:
                root1.left = x
            else:
                insert(root1.left,key)


###Just to print### And this will always give me a sorted list####
def inorder(root):
    if root:

        inorder(root.left)
        print(root.val)
        inorder(root.right)
def minvaluenode( node):
    current=node
    while current.left is not None:
        current=current.left
    return  current

def deletenode(r,key):
    if r is None:
        return r


    if r.val>key:
        r.left=deletenode(r.left,key)
    elif r.val<key:
        r.right=deletenode(r.right,key)
    else:
        if r.left is None:
            temp=r.right
            r=None
            return temp
        elif r.right is None:
            temp=r.left
            r=None
            return temp
        temp=minvaluenode(r.right)

        r.val=temp.val

        r.right=deletenode(r.right,temp.key)
    return r



###Check if a tree is a bst####
#
#
# check(root,int min=infinity##beg,int max==infinity#beg )
#     if root is null return true
#
#     if (root.data<=min || root.data>=max) ##return false
#         
#         return
#         ###left tree range between -infinity to root data ##3check(root,min,root.data)and ###right tree range between infinity to root data ###
#         # check(root,root.data,max)













root2=Node(50)
insert(root2,30)
insert(root2,70)
insert(root2,20)
insert(root2,40)
insert(root2,60)
insert(root2,80)
inorder(root2)
deletenode(root2,80)
inorder(root2)
