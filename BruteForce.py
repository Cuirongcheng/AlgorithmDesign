# 算法分析与设计实验
# 崔荣成 2020.3.18
# 蛮力法常用算法整理

print("1.排序算法")
import sys
A = [64, 25, 12, 22, 11]

def SelectionSort(A):
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):
            if A[min] > A[j]:
                min = j
        A[i], A[min] = A[min], A[i]

    print("排序后的数组：")
    for i in range(len(A)):
        print("%d" % A[i])

SelectionSort(A)