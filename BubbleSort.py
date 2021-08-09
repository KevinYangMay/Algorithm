class BubbleSort():
    def __init__(self,arr):
        self.arr=arr
    def bubbleSort(self):
        for i in range(0,len(self.arr)):
            for j in range(0,len(self.arr)-1-i):
                if self.arr[j]>self.arr[j+1]:
                    self.swap(self.arr,j,j+1)
        return self.arr

    def bubbleSort2(self):
        for i in range(0,len(self.arr)):
            switch=False
            for j in range(len(self.arr)-1,i-1,-1):
                if self.arr[j]<self.arr[j-1]:
                    self.swap(self.arr,j,j-1)
                    switch=True
            if switch==False:
                break
        return self.arr
    def swap(self, arr, i, j):
        t = arr[j]
        arr[j] = arr[i]
        arr[i] = t


if __name__ == '__main__':
    arr=[3,6,1,8,9,10,12]
    bubbleSort=BubbleSort(arr)
    print(bubbleSort.bubbleSort2())
