class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):

        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.inOrder()

    def tes(self):
        print(self.val)


def drawbst(root, space=0):
    if root == None:
        return

    space += 4

    drawbst(root.right, space)

    print()
    for i in range(space):
        print(end=' ')
    print(root.val)

    drawbst(root.left, space)


inp = [40, 70, 50, 60, 20, 80, 30, 10, 90]

bst = Node()

for i in inp:
    bst.insert(i)

bst.insert(25)
bst.insert(85)

bst.inOrder()
print()
drawbst(bst)
