class Node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key




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


def height(root):

    if root is None:
        return -1


    left_height=height(root.left)
    right_height=height(root.right)
    return 1+max(left_height,right_height)





root2=Node(50)
insert(root2,30)
insert(root2,70)
insert(root2,20)
insert(root2,40)
insert(root2,60)
insert(root2,80)
print(height(root2))

inorder(root2)
