class BinaryTree:
    def __init__(self, value, leftchild, rightchild):
        self.value = value
        self.leftchild = leftchild
        self.rightchild = rightchild

    def addNodes(self, list, index):
        if index = len(list):
            return
        else:
            self.BinaryTree(list[index], list[2*index + 1], list[2*index + 2])
            index += 1
            self.addNodes(self.leftchild)
            return self.addNodes(self.rightchild)


x = BinaryTree()
