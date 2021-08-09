#coding=utf-8
class ShellSort():
    def __init__(self):
        pass
    def shellSort(self,arr):
        h=len(arr)//2
        while h>=1: #一个循环把arr分成几个小数组
            for i in range(0,h): # 需要遍历的小数组个数
                for j in range(i+h,len(arr),h): #对小数组进行插入排序
                    t=arr[j]
                    k=0
                    switch=False #这里判断switch是否向前改变位置
                    for k in range(j,-1,-h): #进行插入排序
                        if t<arr[k]:
                            arr[k+h]=arr[k]
                            switch=True
                    if switch==True: #改变了switch的位置则需要把值插入
                        arr[k]=t
            h//=2
        return arr


    def shellSort2(self, arr):
        # h = len(arr) // 2
        h=0
        '''
        这里改变了h的步进长度变成 h=h*3//2
        找到最大长度后每步执行/3的操作
        改变步进长度可以加快排序速度
        '''
        while h<len(arr):
            h=h*3+1
        '''
        可以加快排序的速度
        End
        '''
        while h >= 1:  # 一个循环把arr分成几个小数组
            if h<len(arr):
                for i in range(h,len(arr)): # 把shellSort1中的两个循环变成了一个循环因为每个元素都需要遍历，只是步进不同
                    t = arr[i]
                    k = 0
                    switch = False  # 这里判断switch是否向前改变位置
                    for k in range(i, -1, -h):  # 进行插入排序
                        if t < arr[k]:
                            arr[k + h] = arr[k]
                            switch = True
                    if switch == True:  # 改变了switch的位置则需要把值插入
                        arr[k] = t
            h //= 3
        return arr


if __name__ == '__main__':
    arr = [3, 6, 1, 8, 9, 10, 12]
    shellSort=ShellSort()
    print(shellSort.shellSort2(arr))