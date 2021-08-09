class MaxHeap():
    def __init__(self):
        self.arr=[62,41,30,28,16,22,13,19,17,15]
    def parent(self,index): #返回index节点的父亲节点
        if index==0:
            return 0
        return (index-1)//2
    def leftChild(self,index): #返回index节点的左孩子
        return index*2+1
    def rightChild(self,index): #返回index节点的右孩子
        return index*2+2
    def add(self,e):
        self.arr.append(e)
        index=len(self.arr)-1
        self.siftUp(index)
    #取出最大元素
    def extractMax(self):
        self.swap(self.arr,0,len(self.arr)-1)
        i=self.arr.pop()
        self.siftDown(0)
        return i
    def siftUp(self,x): #添加元素进入堆 上浮
        index=x
        while self.arr[index]>self.arr[self.parent(index)] and index!=0:
            self.swap(self.arr,index,self.parent(index))
            index=self.parent(index)
    def siftDown(self,x):#元素的下沉
        index=x
        while self.leftChild(index)<len(self.arr): #判断是index节点是否有孩子节点，如果没有左孩子则也没有右孩子，该节点是叶子节点，无需下浮
            j=self.leftChild(index)
            if(j+1<len(self.arr) and self.arr[j]<self.arr[j+1]): #判断是否存在右孩子，存在比较大小，不存在则不执行
                j=self.rightChild(index) #如果右孩子大于左孩子则赋值j，这里注意 可以写成j++
            if self.arr[index]>=self.arr[j]: #判断 index是否比左右孩子大，如果index大于或等于左右孩子则不作下浮
                break
            else:
                self.swap(self.arr,index,j)
                index=j
    #把随机的一个数组排列成一个堆
    def heapify(self, arr):
        self.arr=arr
        for i in range(len(self.arr)-1,-1,-1):
            j=self.parent(i)
            self.siftDown(j)
        return self.arr

    def toString(self):
        print(self.arr)

    def swap(self, arr, i, j):
        t = arr[j]
        arr[j] = arr[i]
        arr[i] = t




if __name__ == '__main__':
    MaxHeap=MaxHeap()
    MaxHeap.toString()
    #self.arr = [62, 41, 30, 28, 16, 22, 13, 19, 17, 15]
    # MaxHeap.add(12)
    MaxHeap.extractMax()

    MaxHeap.toString()
    arr=[62, 41, 30, 28, 22, 19, 17, 16, 15, 13]
    arr.sort()
    print(arr)
    print(MaxHeap.heapify(arr))
