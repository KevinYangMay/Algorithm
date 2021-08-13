class Tire():
    def __init__(self):
        self.root=self.Node()
        self.size=0

    def add(self,word):
        cur = self.root
        for i in word:
            if cur.next.__contains__(i)==False:
                cur.next[i]=self.Node()
            cur=cur.next[i]
        if cur.isWord==False:
            cur.isWord=True
            self.size+=1
    def addProt(self,word):
        self.add2(word,0,self.root)

    #递归写法
    def add2(self,arr,index,cur): #这里的arr就是传入的数组
        if index==len(arr):
            if cur.isWord == False: #这里在哪结束思考了好久，最后终于定下来实在最后一个元素的子节点添加isWord=True
                cur.isWord = True
                self.size += 1
            return
        c=arr[index]
        if cur.next.__contains__(c)==False:
            cur.next[c]=self.Node()
        cur=cur.next[c]
        self.add2(arr,index+1,cur)
    def search(self,word):
        return self.match(self.root,word,0)
    def match(self,node,arr,index):
        if index==len(arr):
            return node.isWord #递归到底，看是是否为一个单词，如果不是则返回False
        c=arr[index]
        if c!='.':
            if node.next.__contains__(c):
                return self.match(node.next[c],arr,index+1)
            return False
        else: #c=='.'
            keys=node.next.keys()
            for i in keys:
                if self.match(node.next[i],arr,index+1):
                    return True
                return False

    def __str__(self):
        print(self.root.next)

    class Node():
        def __init__(self):
            self.val=None
            self.isWord=False
            self.next={}

if __name__ == '__main__':
    tire=Tire()
    tire.addProt('bad')
    tire.addProt('dad')
    tire.addProt('mad')
    print(tire.search('pad'))
    print(tire.search('bad'))
    print(tire.search('.p.'))
    print(tire.search('...'))
    a=[True,False,False,True]
    print('------------')
    '''
    出现return 整个函数直接跳出
    def returnMap():
        for i in a:
            if i:
                return i
            print(1)
    returnMap()
    '''

    # print(tire.root.next['b'].next['a'].next)
    # booblen 为True则执行if 为False则不执行
    # i=True
    # if i:
        # print(i)
    # print(tire.__str__())
    # a='string'
    # print(a[0])