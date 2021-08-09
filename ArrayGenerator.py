#coding=utf-8
import time
import random

class ArrayGenerator():
    def __init__(self):
        pass

    def generatorOrderedArray(self,n):
        arr=[]
        for i in range(0,n+1):
            arr.append(i)
        return arr

    def generatorRandomArray(self,n):
        arr=[]
        for i in range(0,n+1):
            #randint=[0,n) 表示的区间
            j=random.randint(0,n+1)
            arr.append(j)
        return arr

if __name__ == '__main__':
    arrGenerator=ArrayGenerator()
    time_start = time.time()
    arr=arrGenerator.generatorRandomArray(10)
    time_end = time.time()
    print('time cost', time_end - time_start, 's')
    print(arr)