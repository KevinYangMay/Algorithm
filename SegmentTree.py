#coding=utf-8
class SegmentTree():
    def __init__(self,arr):
        self.arr=arr
        self.tree=[0]*4*len(arr)
        self.buildSegmentTree(arr,0,0,len(arr)-1)
    #返回完全二叉树的数组中，一个索引所表示的元素的左孩子节点的索引
    #完全二叉树 平衡二叉树
    def leftChild(self,x):
        return x*2+1
    def rightChild(self,x):
        return x*2+2
    #线段树
    #在index 位置创建表示[l....r]的线段树
    def buildSegmentTree(self,arr,index,l,r):
        if l==r:
            self.tree[index]=arr[l]
            return
        leftChild=self.leftChild(index)
        rightChild=self.rightChild(index)
        mid=l+(r-l)//2 #避免出现整型溢出问题
        self.buildSegmentTree(arr,leftChild,l,mid)
        self.buildSegmentTree(arr,rightChild,mid+1,r)
        #这里不一定是数字求和，也可能是其他的元素求和
        self.tree[index]=self.tree[leftChild]+self.tree[rightChild]
    def queryPort(self,queryL,queryR):
        #判断输入是否合法
        '''
        queryL<0,queryR<0,queryL>queryR,queryL>=len(arr),queryR>=lar(arr)
        '''
        return self.query(0,self.tree,queryL,queryR,0,len(self.arr)-1)
    def query(self,index,arr,queryL,queryR,l,r):
        if queryL==l and queryR==r:
            return arr[index]
        leftChild=self.leftChild(index)
        rightChild=self.rightChild(index)
        mid=l+(r-l)//2
        if queryL>mid:
            return self.query(rightChild,arr,queryL,queryR,mid+1,r)
        elif queryR<=mid:
            return self.query(leftChild,arr,queryL,queryR,l,mid)
        leftRueslt=self.query(leftChild,arr,queryL,mid,l,mid)
        rightRueslt=self.query(rightChild,arr,mid+1,queryR,mid+1,r)
        return leftRueslt+rightRueslt
    def updatePort(self,index,val): #index 为需要修改的下标 = updateIndex
        self.update(self.tree,0,len(self.arr)-1,0,index,val)

    def update(self,arr,l,r,index,updateIndex,val):
        if l==r==updateIndex:
            arr[index]=val
            return
        mid=l+(r-l)//2 #l+r//2=l+(r-l)//2 防止整型溢出的问题
        leftChild=self.leftChild(index)
        rightChild=self.rightChild(index)
        if updateIndex>mid:
            self.update(arr,mid+1,r,rightChild,updateIndex,val)
        elif updateIndex<=mid:
            self.update(arr,l,mid,leftChild,updateIndex,val)
        arr[index]=arr[leftChild]+arr[rightChild]
    def toString(self):
        print(self.tree)

if __name__ == '__main__':
  # arr=[1,2]
  # arr=[-2,0,3,-5,2,-1]
  arr=[1, 3, 5]
  #预先开空间
  # a=[None]*4*len(arr)
  segmentTree=SegmentTree(arr)
  # segmentTree.toString()
  # print(segmentTree.queryPort(0,5))
  # print(segmentTree.queryPort(1,4))
  # print(segmentTree.queryPort(0,2))
  segmentTree.updatePort(2,8)
  print(segmentTree.queryPort(0,2))
  print(arr)