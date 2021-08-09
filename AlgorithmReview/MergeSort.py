#coding=utf-8
import copy

class MergeSort():
    def __init__(self):
        pass

    #[l,r]
    def mergeSortPort(self,arr):
        temp=copy.deepcopy(arr)
        l=0;r=len(arr)-1
        self.mergeSort(arr,l,r,temp)
    def mergeSort(self,arr,l,r,temp):
        if l>=r:
            return
        mid=l+(r-l)//2
        self.mergeSort(arr,l,mid,temp)
        self.mergeSort(arr,mid+1,r,temp)
        self.merge(arr,l,r,mid)


    #arr[l,r]
    def merge(self,arr,l,r,mid):
        temp=copy.deepcopy(arr) #这里deepcopy的原因是arr的数组一直在变化，所以要复制最新的arr数组
        i=l;j=mid+1
        #这里的for循环是判断值得个数，所以i和j都不会超过 所以不用考虑 j可能会大于r的情况
        for k in range(l,r+1):
            if i>mid:
                arr[k]=temp[j]
                j+=1
            elif j>r:
                arr[k]=temp[i]
                i+=1
            elif temp[i]<=temp[j]:
                arr[k]=temp[i]
                i+=1
            elif temp[j]<temp[i]:
                arr[k]=temp[j]
                j+=1

    #自低向上的归并排序算法
    def mergeSortPort2(self,arr):
        self.mergeSort2(arr)
    def mergeSort2(self,arr):
        for sz in range(1,len(arr)): #这个循环是取sz的值
            j=0
            while j+sz<len(arr):#这里判断第二个区间是否存在，如果不存在则不再需要进行归并
                self.merge(arr,j,min(j+sz+sz-1,len(arr)-1),j+sz-1)#这里的min是判断第二个区间是否超过len(arr)的长度，如果超过直接返回最后一个元素
                j=j+sz+sz


if __name__ == '__main__':
    arr = [7, 1, 4, 2, 8, 3, 6, 5]
    # arr = [4,3,1]
    merge=MergeSort()
    # merge.mergeSortPort(arr)
    merge.mergeSortPort2(arr)
    print(arr)
