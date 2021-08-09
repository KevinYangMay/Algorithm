from MaxHeap import MaxHeap
#这是个函数是对MaxHeap 最大堆进行数组排序
class HeapSort():
    def __init__(self):
        self.arr=[]

    def heapSort(self):
        heap=MaxHeap()
        print(heap.arr)
        for i in range(0,len(heap.arr)):
            self.arr.append(heap.extractMax())
    def toString(self):
        print(self.arr)

if __name__ == '__main__':
    HeapSort=HeapSort()
    HeapSort.heapSort()
    HeapSort.toString()

    for i in range(0,10):
        print(i)
        i+=2

