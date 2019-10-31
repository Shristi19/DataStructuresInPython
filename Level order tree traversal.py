
class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val = key

def level_order_traversal(root1):
    visited = []
    visited.append(root1)
    while len(visited)>0:
        print(visited[0].val)
        temp =  visited.pop(0)
        if temp.left is not None:
            visited.append(temp.left)
        if temp.right is not None:
            visited.append(temp.right)





root=Node(25)
root.left=Node(15)
root.left.left= Node(10)
root.left.left.left=Node(4)
root.left.left.right=Node(12)
root.left.right  = Node(22)
root.left.right.left=Node(18)
root.left.right.right=Node(24)

level_order_traversal(root)
