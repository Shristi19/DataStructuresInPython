class node:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:

        postorder(root.left)
        postorder(root.right)
        print(root.val)

def inorder(root):
    if root:

        inorder(root.left)
        print(root.val)
        inorder(root.right)


root=node(25)
root.left=node(15)
root.left.left  = node(10)
root.left.left.left=node(4)
root.left.left.right=node(12)
root.left.right  = node(22)
root.left.right.left=node(18)
root.left.right.right=node(24)

root.right=node(50)
root.right.left=node(35)
root.right.left.left=node(31)
root.right.left.right=node(44)
root.right.right=node(70)
root.right.right.left=node(66)
root.right.right.right=node(90)

preorder(root)
print("\n")
inorder(root)
print("\n")
postorder(root)
print("\n")
