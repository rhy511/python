#! /usr/bin/env python
#coding=utf-8

data = [1,3,5,7,9,10,8,6,4,2]
#氣泡排序法
def bubbleSort():
    for i in range(len(data)-1,0,-1):
        for j in range(0,i,1):   
            if data[j] > data[j+1]:
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
    print("bubbleSort = %s" % data)      
#bubbleSort()
#插入排序法
def insertionSort():
    for i in range(1,len(data),1): #小於10
        tmp = data[i]
        j = i
        while j > 0 and data[j-1] > tmp:
            data[j] = data[j-1]
            j -= 1 #Python中沒有j--
        data[j] = tmp
    print("insertionSort = %s" % data)      
#insertionSort()
#選擇排序法
def selectionSort():
    for i in range(0,len(data)-1,1):
        min_number = i
        for j in range(i+1,len(data),1):
            if(data[j]<data[min_number]):
                min_number = j
        tmp = data[i]
        data[i] = data[min_number]
        data[min_number] = tmp
    print("selectionSort = %s" % data)   
selectionSort()
