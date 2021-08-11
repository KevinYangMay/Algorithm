class BST():
    def __init__(self):
        self.root=None
        self.size=0
    '''
    二分搜索树的添加
    '''
    def add(self,val):
        # note=self.Note(val)
        self.root=self.addNote(self.root,val)
        #这样写把添加第一个节点也考虑进去了，比我第一次写的要好太多了。
    def addNote(self,root,val):
        if root==None:
            self.size+=1
            return self.Note(val)
        if root.val<val:
            root.right=self.addNote(root.right,val)
        elif root.val>val:
            root.left=self.addNote(root.left,val)
        return root

    '''
        我写的二分搜索树的添加
        def addNotePort(self,val):
            #当BST List 中，第一个节点没有元素时，直接把新建的元素放在根节点
            note = self.Note(val)
            if self.size==0:
                self.root=note
                self.size+=1 #这是后面加的，之前忘了这事了。
            else:
                self.addNote(self.root,note)

        #实现addNoted 的递归调用逻辑
        def addNote(self,root,note):
            if root==None:
                return
            root=self.searchPosition(root,note)
            #这是递归调用
            self.addNote(root,note)
            #下面的这个新建的实例应该在上一个函数的时候加上
            # newNote=self.Note(val)
        def searchPosition(self,root,note):
            # print(root.val,note.val)
            if root.val<note.val:
                #判断下一个节点是不是None，如果不是返回下一个节点，如果是则返回当前节点root，并且在当前节点下添加元素
                if root.right!=None:
                    return root.right
                else:
                    root.right=note
                    self.size+=1
                    return None
            elif root.val>note.val:
                if root.left != None:
                    return root.left
                else:
                    root.left=note
                    self.size+=1
                    return None
            else:
                return None

    '''

    '''
    二分搜索树的搜索
    '''
    #老师写的二叉树搜索代码直接返回boolean型
    def containPort(self,val):
        return self.contains(self.root,val)
    def contains(self,root,val):
        if root==None:
            return False
        if root.val>val:
            return self.contains(root.left,val)
        if root.val<val:
            return self.contains(root.right,val)
        else:
            return True


    '''
        搜索函数
        #我这个代码时直接把查找的Note都返回出来了
        #searchPort接口
        def searchNotePort(self,val):
            root=self.searchNote(self.root,val)
            if root==None:
                print('没有找到元素')
            else:
                print("找到元素了")
        def searchNote(self,root,val):
            p=None
            if root ==None:
                return None
            if root.val>val:
                p=self.searchNote(root.left,val)
            elif root.val<val:
                p=self.searchNote(root.right,val)
            else:
                return root
            return p
    '''

    '''
    二分搜索树的遍历
    '''
    #二分搜索树的前序遍历
    def preOrderPort(self):
        self.preOrder(self.root)
    def preOrder(self,root):
        if root==None:
            return
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    #二分搜索树的前序遍历 中序遍历相当于输出一个排好顺序的数组
    #遍历顺序是先遍历这个树的左数组，再遍历根节点，最后遍历右节点
    #结果是排好顺序的所以把函数名命名为Order 这是中序遍历树的一个特有的特点
    def orderPort(self):
        self.order(self.root)
    def order(self,root):
        if root==None:
            return
        # print(root.val)
        self.order(root.left)
        print(root.val)
        self.order(root.right)

    #二分搜索树的后续遍历
    #后续遍历，是先把整个树从叶子节点开始遍历到root节点
    '''
    适用于文件的删除操作和树型结构程序的内存释放
    我觉得删除节点时候可以用到后序遍历
    '''
    def postOrderPort(self):
        self.postOrder(self.root)
    def postOrder(self,root):
        if root==None:
            return
        # print(root.val)
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val)



    '''
    二分搜索树的非递归写法
    '''
    #前序遍历
    def preOrderPort2(self):
        arr=[]
        arr.append(self.root)
        self.preOrder2(arr)
    def preOrder2(self,arr):
        while arr:
            i=arr.pop()
            print(i.val)
            if i.right!=None:
                arr.append(i.right)
            if i.left!=None:
                arr.append(i.left)
    #中序遍历非递归写法
    '''
    抄的人家的写法
    def orderPort2(self):
        #arr用来模拟栈
        arr=[]
        self.order2(arr)

    def order2(self,arr):
        root=self.root
        while root:
            arr.append(root)
            root = root.left
        while len(arr)!=0:
            root=arr.pop()
            print(root.val)
            root=root.right
            while root:
                arr.append(root)
                root=root.left
    '''
    #自己经过梳理后的写法
    def orderPort2(self):
        arr=[]
        arr.append(self.root)
        self.order2(arr)
    def order2(self,arr):
        root=self.root
        while arr:
            while root.left:
                arr.append(root.left)
                root=root.left
            i=arr.pop()
            print(i.val)
            if i.right!=None:
                arr.append(i.right)
                root=i.right
            else:
                root=i


    #后续遍历非递归写法
    def postOrderPort2(self):
        arr=[]
        arr.append(self.root)
        self.postOrder2(arr)
    def postOrder2(self,arr):
        preNote=None
        root=self.root
        while arr:
            while root.left and root!=preNote:
                arr.append(root.left)
                root=root.left
            i=arr.pop()
            if i.right==None or i.right==preNote:
               print(i.val)
               preNote=i
               root=i
            else:
                arr.append(i)
                arr.append(i.right)
                root=i.right

    #广度优先算法
    #该算法需要使用队列数据结构的方式辅助，一层一层对树这种数据进行遍历
    #是不是很简单知道怎么做了就变得简单了
    def breadthOrderPort(self):
        self.breadthOrder(self.root)
    def breadthOrder(self,root):
        arr=[]
        arr.append(root)
        while arr:
            i=arr.pop(0)
            if i.left!=None:
                arr.append(i.left)
            if i.right!=None:
                arr.append(i.right)
            print(i)



    '''

#删除元素
    def removeNotePort(self,note):
        root=self.root
        i=None
        if note=='max':
            while root:
                i=root
                root=root.right
            root=i
        elif note=='min':
            while root:
                i=root
                root=root.left
            root=i
        else:
            root=self.searchNotePort(note)
        print(root.val)
        self.removeNote(root)
        print('删除成功！')




    def removeNote(self,root):
        if root==None:
            return
        print(root.val)
        self.removeNote(root.left)
        self.removeNote(root.right)
        root=None
    
    '''
    #删除二叉树的最大元素和最小元素,但是没哟使用1000个随机树进行测试，以后在看过算法复杂度分析后需要补上

    #找到要删除的最小值，返回该元素
    #这里有怎么从递归中把底层把找的元素给传上来
    def removeMinPort2(self,root):
       res=None
       if root.left==None:
           res=root
           return res
       res=self.removeMinPort2(root.left)
       return res
    def removeMinPort(self):
        self.root=self.removeMin(self.root)
    def removeMaxPort(self):
        self.root=self.removeMax(self.root)
    def removeMin(self,root):
        if root.left==None:
            root_right=root.right #当最后的一个右节点右边有孩子节点时，需要把要被删除的节点的孩子节点挂到他的父节点的右侧
            self.size-=1
            root.right=None
            return root_right
        root.left=self.removeMin(root.left)
        return root
    def removeMax(self,root):
        if root.right==None:
            root_left=root.left #当最后的一个右节点左边有孩子节点时，需要把要被删除的节点的孩子节点挂到他的父节点的右侧
            self.size-=1
            root.left=None
            return root_left
        root.right=self.removeMax(root.right)
        return root

    #删除任意一个元素
    def removeNotePort(self,val):
        self.removeNote(self.root,val)
    def removeNote(self,root,val):
        if root==None:
            return root
        if root.val<val:
            root.right=self.removeNote(root.right,val)
        elif root.val>val:
            root.left=self.removeNote(root.left,val)
        else: # root.val=val
            if root.left==None:
                root_right=root.right
                root.right=None
                self.size-=1
                return root_right
            elif root.right==None:
                root_left=root.left
                root.left=None
                self.size-=1
                return root_left
            else: #root.left and root.right !==None
                #这里做的是， 当找到这个元素后，开始遍历以找到元素为根的右侧最小元素
                #把右边最小元素删除
                #再把继承子节点放到要删除的节点的位置
                #之前被困扰的是怎么一步把子节点删了再传出来。看来是不行的,只能先找到再删除，分2步

                successor=self.removeMinPort2(root.right)
                successor.right=self.removeMin(root.right)
                successor.left=root.left
                # print(root.right.val)
                # print(self.removeMin(root.right))
                ''' 
                # successor.right=self.removeMin(root.right) 
                连接的位置应该写在 successor.left的前面，这样导致执行removeMin出现了问题
                '''

                # print(successor.right.val)
                # print(successor.right.val)
                # print(successor.left.val)
                root.left=root.right=None
                return successor
        #这里的return root 是给上面两个if一个返回值 root.left= or root.right=
        return root






    class Note():
        def __init__(self,val):
            self.val=val
            self.left=None
            self.right=None
        #打印函数，这样就不用加val
        def __str__(self):
            return str(self.val)


'''
没有试过python内部类准备试一下，没有测试过代码，明天准备测试一下
还有二分排序法没有学，明天可以学一下
'''
if __name__ == '__main__':
    arr=[28,16,30,13,22,29,40]
    # arr=[28]
    BSTree=BST()
    for i in arr:
        BSTree.add(i)
    # print(BSTree.root.right.left.val)
    # print(BSTree.root.right.right.left)
    #搜索
    print(BSTree.containPort(33))
    #遍历方法
    '''
    print()
    print('---------------------')
    print('递归前中后序遍历')
    BSTree.preOrderPort()
    print('---------------------')
    BSTree.orderPort()
    print('---------------------')
    BSTree.postOrderPort()
    print('--------------------')
    print()
    print('--------------------')
    print('非递归前中后序遍历')
    BSTree.preOrderPort2()
    print('--------------------')
    BSTree.orderPort2()
    print('--------------------')
    BSTree.postOrderPort2()
    '''
    # BSTree.removeMinPort()
    # BSTree.removeMaxPort()
    print('-------')
    # BSTree.removeNotePort(30)
    # BSTree.preOrderPort()
    BSTree.removeMin(BSTree.root.right.right)
    BSTree.orderPort()
    # BSTree.breadthOrderPort()