class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def inorder_traversal(self, start, result=[]):
        if start:
            result = self.inorder_traversal(start.left, result)
            result.append(start.data)
            result = self.inorder_traversal(start.right, result)
        return result


# Usage example
if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("Inorder Traversal:", tree.inorder_traversal(tree.root))
