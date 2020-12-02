class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert()

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "Preorder":
            return self.preorder_print(btree.root, "")
        elif traversal_type == "Inorder":
            return self.inorder_print(btree.root, "")
        elif traversal_type == "Postorder":
            return self.postorder_print(btree.root, "")
        else:
            print("Traversal type" + str(traversal_type) + "is not supported")

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


btree = BinaryTree(1)
btree.root.left = Node(2)
btree.root.right = Node(3)
btree.root.left.left = Node(4)
btree.root.left.right = Node(5)
btree.root.right.left = Node(6)
btree.root.right.right = Node(7)

print(btree.print_tree("Preorder"))
print(btree.print_tree("Inorder"))
print(btree.print_tree("Postorder"))
