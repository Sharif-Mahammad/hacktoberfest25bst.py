class Node:
    def _init_(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)  # ✅ Correct direction
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

root = None
for v in [5, 3, 7, 1]:
    root = insert(root, v)
inorder(root)  # ✅ Output: 1 3 5 7
