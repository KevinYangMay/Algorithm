import copy

class MergeSort():
    def __init__(self):
        pass
    def sort(self,arr):
        temp=copy.deepcopy(arr) #提前先开辟空间，避免后面一直开辟空间。
        self.Msort(arr,0,len(arr)-1,temp)
    def Msort(self,arr,l,r,temp):
        if(l>=r):
            return
        # mid=(l+r)//2 这里使用下面的 l+(r-l) 是为了避免string 超出size 导致出现错误
        mid=l+(r-l)//2
        self.Msort(arr,l,mid,temp)
        self.Msort(arr,mid+1,r,temp)
        if arr[mid]>arr[mid+1]:  #这里在归并前判断需要归并的数组是否已经是有序的，如果已经排好顺序了，就不用再排序了。提高性能
            self.merge(arr,l,mid,r,temp)
    # [7,1,4,2,8,3,6,5]
    def merge(self,arr,l,mid,r,temp):
        temp=copy.copy(arr)
        # deepcopy 左闭右开
        i=l;j=mid+1
        for k in range(l,r+1):
            # 这里判断有个问题，就是出现了需要判断j的范围吗？
            if(i>mid):
                arr[k]=temp[j]
                j+=1
            elif(j>r):
                arr[k]=temp[i]
                i+=1
            elif(temp[i]<temp[j]):
                arr[k]=temp[i]
                i+=1
            elif(temp[i]>temp[j]):
                arr[k]=temp[j]
                j+=1


    # 归并排序，自下而上的排序
    def sort2(self, arr):
        temp = copy.deepcopy(arr)  # 提前先开辟空间，避免后面一直开辟空间。
        self.Msort2(arr,temp)

    def Msort2(self,arr,temp):
        for sz in range(1,len(arr)):
            j=0
            while j+sz<len(arr): #这里j+sz 表示存在第二个区间，如果不存在第二个区间则不需要再进行归并
                #遍历合并两个区间的起始位置i
                #合并[i,i+sz-1],[i+sz,i+sz+sz-1] 两个区间的元素
                self.merge(arr,j,j+sz-1,min(j+sz+sz-1,len(arr)-1),temp)
                j=j+sz+sz


    def printTostring(self,x):
        print(x)
if __name__ == '__main__':
    arr=[7,1,4,2,8,3,6,5]
    # arr=[4,3,1]
    Ms=MergeSort()
    Ms.sort2(arr)
    # 这里之前传了 len(arr) 没有传 len(arr)-1
    #要搞清楚具体的指针
    print(arr)
    # MergeSort.Msort(arr,0,3)
    # print(len(arr))
