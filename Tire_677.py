class Tire():
    def __init__(self):
        self.root=self.Node()
        self.size=0

    def insert(self,key,val):
        self.add(key,0,self.root,val)

    #递归写法
    def add(self,arr,index,cur,val): #这里的arr就是传入的数组
        if index==len(arr):
            if cur.iskey == False: #这里在哪结束思考了好久，最后终于定下来实在最后一个元素的子节点添加iskey=True
                cur.iskey = True
                self.size += 1
            cur.val=val
            return
        c=arr[index]
        if cur.next.__contains__(c)==False:
            cur.next[c]=self.Node()
        cur=cur.next[c]
        self.add(arr,index+1,cur,val)
    def sum(self,prefix):
        cur=self.root
        for i in prefix:
            if cur.next.__contains__(i):
                cur=cur.next[i]
            else:
                return 0
        return self.sumNode(cur)
    def sumNode(self,node):
        result=node.val
        '''
        这里不写递归结束的条件是因为，在node.next.keys()中包含循环结束的条件
        当len(node.next.keys())=0时，循环数组为0，所以不执行循环  
        # if len(node.next.keys())==0:
        #     return node.val
        '''
        for i in node.next.keys():
            result+=self.sumNode(node.next[i])
        return result



    class Node():
        def __init__(self):
            self.val=0
            self.iskey=False
            self.next={}

if __name__ == '__main__':
    tire=Tire()
    tire.insert('app',2)
    tire.insert('apple',6)
    tire.insert('appls',2)
    tire.insert('apples',2)
    tire.insert('applexxd',2)

    print(tire.sum('ap'))