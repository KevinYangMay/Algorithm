#coding=utf-8
class SegmentTree():
    def __init__(self,arr):
        self.tree=[None]*4*len(arr)
        pass
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
        mid=l+(r-l)//2 #出现整型溢出问题
        self.buildSegmentTree(arr,leftChild,l,mid)
        self.buildSegmentTree(arr,rightChild,mid+1,r)
        #这里不一定是数字求和，也可能是其他的元素求和
        self.tree[index]=self.tree[leftChild]+self.tree[rightChild]

if __name__ == '__main__':
  arr=[1,2]
  #预先开空间
  a=[None]*4*len(arr)
