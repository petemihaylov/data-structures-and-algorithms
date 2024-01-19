class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class Treversal:
    
    @staticmethod
    def preorder(root):
        # if root is None,return
        if root is None:
            return None
        # print the current node
        print(root.data, end=", ")
        # traverse left subtree
        Treversal.preorder(root.leftChild)

        # traverse right subtree
        Treversal.preorder(root.rightChild)

    @staticmethod
    def postorder(root):
        if root is None:
            return None
        Treversal.postorder(root.leftChild)

        Treversal.postorder(root.rightChild)

        print(root.data, end=", ")

    @staticmethod
    def inorder(root):
        if root is None:
            return None

        Treversal.inorder(root.leftChild)

        print(root.data, end=", ")

        Treversal.inorder(root.rightChild)



# initialize the binary tree structure
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7

print("Pre-order treversal")
Treversal.preorder(node1)

print("\nPost-order treversal")
Treversal.postorder(node1)

print("\nIn-order treversal")
Treversal.inorder(node1)


