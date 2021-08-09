#coding=utf-8
class MinHeap():
    def __init__(self):
        self.arr=[]

    def parent(self,x):
        #这里出现了当x为0时出现了-1的值
        if x==0:
            return 0
        return (x-1)//2
    def leftChild(self,x):
        return x*2+1
    def rightChild(self,x):
        return x*2+2

    def add(self,x):
        self.arr.append(x)
        i=len(self.arr)-1
        if i>0:
            self.siftUp(i)
    def extractMin(self):
        self.swap(self.arr,0,len(self.arr)-1)
        i=self.arr.pop()
        self.siftDown(0)
        return i
    '''
    Start这里是排序使用的函数
    '''
    def extractMinOutArr(self,arr,index): #index 为已经排好的顺序
        self.swap(self.arr,0,0-index)
        self.siftDownSort(arr,index,0)
    def siftDownSort(self,arr,index,x): #index为已经排好顺序的数字
        i = x
        while self.leftChild(i) < len(arr)-index:
            j = self.leftChild(i)
            if self.rightChild(i) < len(arr)-index and arr[j + 1] < arr[j]:
                j += 1
            if arr[i] <= arr[j]:
                break
            else:
                self.swap(arr, i, j)
                i = j
    '''
    End排序使用的函数
    '''

    def siftUp(self,x):
        i=x #这里的x是index
        while self.arr[i]<self.arr[self.parent(i)] and i>0:
            self.swap(self.arr,i,self.parent(i))
            i=self.parent(i)
    def siftDown(self,x):
        i=x
        while self.leftChild(i)<len(self.arr):
            j=self.leftChild(i)
            if self.rightChild(i)<len(self.arr) and self.arr[j+1]<self.arr[j]:
                j+=1
            if self.arr[i]<=self.arr[j]:
                break
            else:
                self.swap(self.arr,i,j)
                i=j
    def heapify(self,arr):
        self.arr=arr
        for i in range(len(self.arr)-1,-1,-1):
            self.siftDown(self.parent(i))
        return self.arr



    def toString(self):
        print(self.arr)



    def swap(self, arr, i, j):
        t = arr[j]
        arr[j] = arr[i]
        arr[i] = t

if __name__ == '__main__':
    arr = [62, 41, 30, 28, 16, 22, 13, 19, 17, 15]
    # arr = [62, 41, 30, 28]
    minHeap=MinHeap()
    print(minHeap.heapify(arr))
    # minHeap.add(20)
    # minHeap.add(40)
    # minHeap.toString()

#排序从大到小
    for i in range(1,len(arr),1):
        minHeap.extractMinOutArr(arr,i)
    print(arr)

