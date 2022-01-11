class BinaryTree:
    def __init__(self, key,leftTree=None,rightTree=None):
        self.key = key
        self.leftTree = leftTree
        self.rightTree = rightTree

    def setKey (self,key):
        self.key = key

    def getKey (self):
        return self.key

    def getLeftTree (self):
        return self.leftTree

    def getRightTree (self):
        return self.rightTree

    def insertLeft (self,key):
        #making the key the left subtree of self
        if self.leftTree == None:
            self.leftTree = BinaryTree (key)
        else:
            t =BinaryTree (key)
            # making the key insert in between self and self's left subtree
            self.leftTree, t.leftTree = t, self.leftTree

    def insertRight (self,key):
        if self.rightTree == None:
            self.rightTree = BinaryTree (key)
        else:
            t = BinaryTree (key)
            self.rightTree, t.rightTree = t, self.rightTree
    
    def printPreorder (self, level):
        #N
        print(str ( level*'.') + str (self.key))

        #L
        if self.leftTree != None:
            self.leftTree.printPreorder(level+1) # +1 to increase dashes

        #R
        if self.rightTree != None:
            self.rightTree.printPreorder(level+1)
    #reverse of inOrder (for CA2)
    def printInorder (self, level):
        #R
        if self.rightTree != None:
            self.rightTree.printInorder(level+1)

        #N
        print(str ( level*'.') + str (self.key))
        
        #L
        if self.leftTree != None:
            self.leftTree.printInorder(level+1) # +1 to increase dashes


# (2+(4*5))



tree = BinaryTree ("+", BinaryTree(2) , BinaryTree('*',BinaryTree(4),BinaryTree(5)) )
tree.printInorder(0)

print()



