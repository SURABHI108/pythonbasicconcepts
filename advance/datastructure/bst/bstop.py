class Tree:
    def __init__(self,value = None):
        self.value = value
        
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
    def isEmpty(self):
        return (self.value == None)
    
    def insertData(self,data):
        if self.isEmpty():
            self.value = data
            self.left = Tree()
            self.right = Tree()
        elif self.value == data:
            return
        elif data < self.value:
            self.left.insertData(data)
            return
        elif data > self.value:
            self.right.insertData(data)
            return
    def isleaf(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False
    def maxval(self):
        # Find the maximum value in the Tree
        if self.right.right == None:
            return (self.value)
        else:
            return (self.right.maxval())
    def deleteNode(self,val):
        if self.isEmpty():
            return
        if val < self.value:
            self.left.deleteNode(val)
            return
        if val > self.value:
            self.right.deleteNode(val)
            return
        if val == self.value:
            if self.isleaf():
                self.value = None
                self.right = None
                self.left = None
                return
            elif self.left.isEmpty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
                return
    def inOrder(self):
        if self.isEmpty():
            return ([])
        else:
            return (self.left.inOrder() + [self.value] + self.right.inOrder())
    def preOrder(self):
        if self.isEmpty():
            return([])
        else:
            return([self.value]+self.left.preOrder()+self.right.preOrder())
    def postOrder(self):
        if self.isEmpty():
            return([])
        else:
            return(self.left.postOrder()+self.right.postOrder()+[self.value]) # recursion use
t = Tree(50)
t.insertData(40)
t.insertData(60)
t.insertData(35)
t.insertData(55)
t.insertData(45)
# t.insertData(20)
print("Before deleting 4: ")
print("inorder data: ",t.inOrder())
print("preorder data : ", t.preOrder())
print("postorder data",t.postOrder())
t.deleteNode(4)
print("After deleting 4: ")         
print(t.inOrder()) 