class BST():
    def __init__(self):
        self.root=None
        self.size=0
    def add(self,val):
        self.root=self.addNote(self.root,val)
    def addNote(self,root,val):
        if root==None:
            self.size+=1
            return self.Note(val)
        if root.val>val:
            root.left=self.addNote(root.left,val)
        elif root.val<val:
            root.right=self.addNote(root.right,val)
        return root

    def query(self,val):
        result=self.queryNote(self.root,val)
        return result
    def queryNote(self,root,val):
        i=False
        if root==None:
            return i
        if root.val==val:
            i=root
            return i
        if root.val>val:
            i=self.queryNote(root.left,val)
        elif root.val<val:
            i=self.queryNote(root.right,val)
        return i

    def preOrderProt(self):
        self.preOrder(self.root)
    def preOrder(self,root):
        if root==None:
            return
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
    def midOrderProt(self):
        self.midOrder(self.root)
    def midOrder(self,root):
        if root==None:
            return
        self.midOrder(root.left)
        print(root.val)
        self.midOrder(root.right)
    def breadthOrderProt(self):
        arr=[]
        arr.append(self.root)
        self.breadthOrder(arr)
    def breadthOrder(self,arr):
        while arr:
            i=arr.pop(0)
            if i.left!=None:
                arr.append(i.left)
            if i.right!=None:
                arr.append(i.right)
            print(i.val)



    def minProt(self,root):
        return self.minNote(root)
    def minNote(self,root):
        if root.left==None:
            return root
        return self.minNote(root.left)

    def removeMinProt(self):
        self.root=self.removeMin(self.root)
    def removeMin(self,root):
        if root.left==None:
            root_right=root.right
            root.right=None
            self.size-=1
            return root_right
        root.left=self.removeMin(root.left)
        return root

    def removeNoteProt(self,val):
        self.removeNote(self.root,val)
    def removeNote(self,root,val):
        if root==None:
            return
        if root.val==val:
            if root.left==None: # and root.right!=None:这里可以不用这么写可以省略
                root_right=root.right
                root.right=None
                self.size-=1
                return root_right
            elif root.right==None:
                root_left=root.left
                root.left=None
                self.size-=1
                return root_left
            else:
                i=self.minProt(root.right)
                root_right=self.removeMin(root.right)
                root_left=root.left
                root.left=None;root.right=None
                i.left=root_left;i.right=root_right
                return i
        if root.val>val:
            root.left=self.removeNote(root.left,val)
        elif root.val<val:
            root.right=self.removeNote(root.right,val)
        return root


    class Note():
        def __init__(self,val):
            self.val=val
            self.left=None
            self.right=None
if __name__ == '__main__':
    arr = [28, 16, 30, 13, 22, 29, 40]
    BST=BST()
    for i in arr:
        BST.add(i)
    print('-------query----------')
    x=BST.query(13)
    print(x.val)
    print('---------------')
    BST.preOrderProt()
    print('-----------------')
    BST.midOrderProt()
    print('-----------------')
    BST.breadthOrderProt()
    i=BST.minProt(BST.root)
    print('------------------')
    print(i.val)
    print('----------removeNote--------')
    BST.removeNoteProt(30)
    # BST.removeMin(BST.root.right.right)
    BST.preOrderProt()