import random


class QuickSort():
    def __init__(self):
        pass

    #r都是数组最后一个元素，而非len(arr)
    def sortPort(self,arr):
        self.sort(arr,0,len(arr)-1)
    def sort(self,arr,l,r):
        print(arr[l:r+1]) #就只是加了一个print语句，可能有点问题，不太会需要学一下
        if l>=r:
            return
        p=self.partition(arr,l,r)
        self.sort(arr,l,p-1)
        self.sort(arr,p+1,r)

    #r都是数组最后一个元素，而非len(arr)
    def sortPort2(self,arr):
        self.sort2(arr,0,len(arr)-1)
    def sort2(self,arr,l,r):
#        print(arr[l:r+1]) #就只是加了一个print语句，可能有点问题，不太会需要学一下
        if l>=r:
            return
        p=self.partition2(arr,l,r)
        self.sort2(arr,l,p-1)
        self.sort2(arr,p+1,r)

    def partition(self,arr,l,r): #arr:List l:arrHeadPosition r:arrEndposition 右边界
        p=random.randint(l,r) #左闭右闭
        self.swap(arr,l,p)
       #这个代码是为了解决有序数组[1,2,3,4,5,6]
       # 导致一路快速排序错误的问题，但是无法解决全是一样数字的
       #数组快速排序退化的情况如[0,0,0,0,0]
        # arr[l+1,j]<v;v;arr[j+1,i]>=v
        focus=arr[l]
        j=l #j是一个左右的分界点，j的左边<j j的右边>j
        for i in range(l+1,r+1): #因为这里range为左闭右开区间，但传进来的l,r左闭右闭区间所以r要加1,这里从l的下一个note开始所以l也要+1
            '''
            if arr[l]<=arr[i]:
                pass
            这个判断其实可以不用写
            '''
            if arr[l]>arr[i]:
                '''''
                sw=arr[j+1]
                arr[j+1]=arr[i]
                arr[i]=sw
                j+=1
                这是我写的代码
                他这里把j++放在最前面就可不用对swap函数做多余的修改
                '''''
                j+=1
                self.swap(arr,i,j)

        '''       
        sw=arr[j]
        arr[j]=arr[l]
        arr[l]=sw
        整合成一个函数
        '''
        self.swap(arr,l,j)
        return j

    def swap(self,arr,i,j):
        t=arr[j]
        arr[j]=arr[i]
        arr[i]=t



    #快速排序之二路排序
    def partition2(self,arr,l,r):
        i=l+1;j=r;focus=l
 # 这里不能写i<j 因为当l=i时，arr中只有一个元素该方法就有问题       while i<j:
        while i<=j:
            orI=i;orJ=j
            if(arr[i]<=arr[l]):
                i+=1
            if(arr[j]>=arr[l]):
                j-=1
            if(orI==i and orJ==j): #这里是当I,J都与开始时一样，则交换位置
                self.swap(arr,i,j)
        self.swap(arr,l,min(i,j))
        return min(i,j)

    # r都是数组最后一个元素，而非len(arr)
    def sortPort3(self, arr):
        self.sort3(arr, 0, len(arr) - 1)

    def sort3(self, arr, l, r):
        #        print(arr[l:r+1]) #就只是加了一个print语句，可能有点问题，不太会需要学一下
        if l >= r:
            return
        p = self.partition3(arr, l, r)
        self.sort3(arr, l,p[0])
        self.sort3(arr, p[1], r)
    #快速排序之三路排序
    def partition3(self,arr,l,r):
        i=l+1;lt=l;gt=r;focus=l
        while i<=gt:
            if arr[i]<arr[l]:
                lt+=1
                self.swap(arr,lt,i)
                i+=1
            #这里写elif是因为这是进行一个操作所以写elif ，partition2 两个if分开写是因为从2个地方进行比较
            elif arr[i]>arr[l]:
                self.swap(arr,gt,i)
                gt-=1
            elif arr[i]==arr[l]:
                i+=1
        self.swap(arr,lt,l)
        # print(lt-1,gt+1)
        return lt-1,gt+1

#二分查找法,因为要对排好序的进行
class BinarySearch():
    def __init__(self):
        pass
    def binarySearchPort(self,arr,val):
        x=self.binarySearch(arr,0,len(arr)-1,val)
        return x
    #[l,r]
    def binarySearch(self,arr,l,r,val):
        mid=l+(r-l)//2
        if arr[mid]==val:
            return arr[mid]
        if l>r:
        # if l>=r: 这里l>=r 有可能出现最后一个数字刚好为要找的数字导致程序出现问题
            return None
        elif arr[mid]>val:
            i=self.binarySearch(arr,l,mid-1,val)
        else:
            i=self.binarySearch(arr,mid+1,r,val)
        return i

#二分查找法的非递归写法
    def binarySearchPort2(self,arr,val):
        i=self.binarySearch2(arr,0,len(arr)-1,val)
        return i
    def binarySearch2(self,arr,l,r,val):
        l=l;r=r
        while(l<=r):
            mid=l+(r-l)//2
            if arr[mid]==val:
                return mid
            elif arr[mid]>val:
                r=mid-1
            else:
                l=mid+1
        return None

    '''
    #二分查找法变形，找到大于某个值的最小值
    #等于从数组中找到 >80的数字
    #这里也可以使用while非递归完成
    '''

    def binarySearchUpperPort(self,arr,val):
        # 这里 len(arr)-1 会出现一个bug，当给的数字超过当前数组最大值时会返回最后一个数字，之后如果有搞不懂，可以画图理解
        # i=self.binarySearchUpper(arr,0,len(arr)-1,val)
        i=self.binarySearchUpper(arr,0,len(arr),val)
        return i
    def binarySearchUpper(self,arr,l,r,val):
        mid=l+(r-l)//2
        if l==r:
            return l
        # if l>r: 这里跟查找有区别的是，该搜索一定是有解的
            # return None
        ''' 
        等于时不应该返回mid+1有可能出现重复的数字，要注意
         # if arr[mid]==val:
            #如果刚好等于mid的值
            # return mid+1
        '''

        if arr[mid]>val:
            #这个地方，当arr[mid]值大于80时，找改值前面的数组
            #注意 这里要包括找到的数字arr[mid] 不能mid-1
            i=self.binarySearchUpper(arr,l,mid,val)
        elif arr[mid]<=val: #arr[mid]<val
            i=self.binarySearchUpper(arr,mid+1,r,val)
        return i


    # ceil 函数
    def binarySearchCeilPort(self,arr,val):
        # 这里 len(arr)-1 会出现一个bug，当给的数字超过当前数组最大值时会返回最后一个数字，之后如果有搞不懂，可以画图理解
        # i=self.binarySearchUpper(arr,0,len(arr)-1,val)
        '''其实不用再写一遍直接使用SearchUpperUpper即可'''
        i=self.binarySearchCeil(arr,0,len(arr),val)
        if arr[i-1]==val:
            i-=1
        return i
    def binarySearchCeil(self,arr,l,r,val):
        mid=l+(r-l)//2
        if l==r:
            return l
        # if l>r: 这里跟查找有区别的是，该搜索一定是有解的
        # return None
        '''
        if arr[mid]==val:
            #如果刚好等于mid的值
            while arr[mid]==val:
                mid+=1
            return mid-1
        #这里我写的有点问题写了一个循环，按照老师的说法，取到最小的最大值后，-1等于要找的值时，那就为要找的值得最大索引
        '''

        if arr[mid]>val:
            #这个地方，当arr[mid]值大于80时，找改值前面的数组
            #注意 这里要包括找到的数字arr[mid] 不能mid-1
            i=self.binarySearchCeil(arr,l,mid,val)
        elif arr[mid]<=val: #arr[mid]<val
            i=self.binarySearchCeil(arr,mid+1,r,val)
        return i

    #lower函数，找数组中<target 的最大值
    def binarySearchLowerPort(self,arr,val):
        i=self.binarySearchLower(arr,0,len(arr)-1,val)
        return i
    def binarySearchLower(self,arr,l,r,val):
        if l>=r:
            return r
        #这里是向下取整，默认去余数的方法是向上取整如1.5 取 1 所以不+1会出现死循环
        mid=l+(r-l+1)//2
        if arr[mid]>=val:
            i=self.binarySearchLower(arr,l,mid-1,val)
        else: #arr[mid]<val
            i=self.binarySearchLower(arr,mid,r,val)
        return i




# 还是要测试当数组量大的时候，需要大量的数据做测试
if __name__ == '__main__':
    # arr=[4,3,1,6,2,5,4]
    arr=[2,3,4,6,5,1]
    # arr=[4,3,1,6,2,5]
    # arr=[4,4,1,6,4,5,6,9,12,3,2,4,6,10,20,33,56,8,]
    # arr=[]
    # arr=[0,0,0,0,0,0,0,0]
    sort=QuickSort()
    # sort.partition3(arr,0,len(arr)-1)
#   测试全为0的数组
    sort.sortPort2(arr)
    # sort.partition3(arr,0,len(arr)-1)
    # p=sort.partition3(arr,0,len(arr)-1)
    # print(p,p[0])
    # print(arr)
    # sort.partition2(arr,0,len(arr)-1)
    # print(arr)
    #print(random.randint(10,30))#与java随机数不同，py可以指定区间生成随机数，但是java标准库不行
    #random,randint是一个闭区间函数
    binary=BinarySearch()
    # print(binary.binarySearchPort(arr,7))
    # print(binary.binarySearchPort2(arr,4))
    # arr1 = [23,56,65,69,72,89,89,96,99]
    arr1 = [1,1,3,3,5,5]
    print(binary.binarySearchLowerPort(arr1,3))