#coding=utf-8
import random
class QuickSort():
    def __init__(self):
        pass
    def sortPort(self,arr):
        self.sort(arr,0,len(arr)-1)
    def sort(self,arr,l,r):
        if l>=r:
            return
        p=self.partition(arr,l,r)
        self.sort(arr,l,p-1)
        self.sort(arr,p+1,r) #这里从p+1 和 p-1的位置进行递归的快速排序 是把p的位置固定住 然后把左右两个数组递归
    #区间为[l,r]
    def partition(self,arr,l,r):
        index=random.randint(l,r)
        self.swap(arr,index,l)
        j=l #j为最后一个小于标定点的位置
        for i in range(l+1,r+1):
            if arr[i]<arr[l]:
                j+=1
                self.swap(arr,i,j)
        self.swap(arr,l,j)
        return j
    #二路快速排序
    def sortPort2(self,arr):
        self.sort2(arr,0,len(arr)-1)
    def sort2(self,arr,l,r):
        if l>=r:
            return
        p=self.partition2(arr,l,r)
        self.sort2(arr,l,p-1)
        self.sort2(arr,p+1,r)
    #区间[l,r]
    '''
    双路快速排序的问题：
    当碰见与锚点 partition 相同的值时，只能分布在两边并不能分到一起，这是三路快速排序存在的原因
    '''
    def partition2(self,arr,l,r):
        index = random.randint(l, r)
        self.swap(arr, index, l)
        i=l+1;j=r # i 为小于标定点的结束值，j为大于标定点的开始值
        while i<=j:
            orI=i;orJ=j
            #这里if不写elif是应为双路快速排序两个指针都需要判断
            if arr[i]<=arr[l]:
                i+=1
            if arr[j]>=arr[l]:
                j-=1
            #当循环到j和i都没有改变时就需要交换位置
            if orI==i and orJ==j:
                self.swap(arr,i,j)
        self.swap(arr,l,min(i,j))
        return min(i,j)

    '''
    三路快速排序
    '''
    def sortPort3(self,arr):
        self.sort3(arr,0,len(arr)-1)
    def sort3(self,arr,l,r):
        if l>=r:
            return
        p=self.partition3(arr,l,r)
        self.sort3(arr,l,p[0])
        self.sort3(arr,p[1],r)
    #arr[l+1...lt]<fouce arr[lt+1....i-1]=fouce arr[gt....r]>fouce
    def partition3(self,arr,l,r):
        index = random.randint(l, r)
        self.swap(arr, index, l)
        i=l+1;lt=l;gt=r
        while i<=gt:
            if arr[l]>arr[i]:
                lt+=1
                self.swap(arr,i,lt)
                i+=1
            elif arr[l]<arr[i]:
                self.swap(arr,i,gt)
                gt-=1
            else: #arr[l]==arr[i]:
                i+=1
        self.swap(arr,l,lt)
        return lt-1,gt+1



    def swap(self,arr,i,j):
        t=arr[j]
        arr[j]=arr[i]
        arr[i]=t

if __name__ == '__main__':
    quickSort=QuickSort()
    arr = [2, 3, 4, 6, 5, 1]

    # arr=[4,4,1,6,4,5,6,9,12,3,2,4,6,10,20,33,56,8,]
    quickSort.sortPort3(arr)
    print(arr)


